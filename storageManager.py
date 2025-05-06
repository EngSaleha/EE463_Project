import os
import subprocess


def display_menu():
    print("\n********** Menu: Disk Management **************")
    print("1. List all available disks")
    print("2. Partition a disk (test with /dev/loopX)")
    print("3. Delete Partition")
    print("4. Format Partition")
    print("5. Mount Partition")
    print("6. Unmount Partition")
    print("7. Display Disk Space Usage")
    print("8. Display a Directory Size")
    print("9. Suggest the Largest Files/Dirs to Delete")
    print("10. Exit\n")


def list_disks():
    subprocess.run(["sudo", "fdisk", "-l"])


def partition_disk():
    list_disks()
    disk = input("Enter the disk name (e.g., /dev/loop0): ")
    print("Opening fdisk... Use 'n' to create a partition, 'w' to write and exit.")
    subprocess.run(["sudo", "fdisk", disk])


def delete_partition():
    list_disks()
    disk = input("Enter the disk name (e.g., /dev/loop0): ")
    partition_number = input("Enter the partition number to delete (e.g., 1): ")
    subprocess.run(["sudo", "parted", "-s", disk, "rm", partition_number])


def format_partition():
    list_disks()
    disk = input("Enter the disk name (e.g., /dev/loop0): ")
    partition_number = input("Enter the partition number to format (e.g., 1): ")
    filesystem_type = input("Enter the filesystem type (e.g., ext4): ")
    subprocess.run(["sudo", "mkfs", f"-t{filesystem_type}", f"{disk}p{partition_number}"])


def mount_partition():
    list_disks()
    partition = input("Enter the partition to mount (e.g., /dev/loop0p1): ")
    mount_point = input("Enter the mount point (e.g., /mnt/test1): ")
    subprocess.run(["sudo", "mkdir", "-p", mount_point])
    subprocess.run(["sudo", "mount", partition, mount_point])
    print(f"{partition} mounted at {mount_point}")


def unmount_partition():
    mount_point = input("Enter the mount point to unmount (e.g., /mnt/test1): ")
    subprocess.run(["sudo", "umount", mount_point])
    print(f"Unmounted {mount_point}")


def display_disk_space_usage():
    subprocess.run(["df", "-h"])


def get_size():
    directory = input("Enter the directory path: ")
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return 0

    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            try:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
            except FileNotFoundError:
                continue
    print(f"Total size of '{directory}': {total_size} bytes")
    return total_size


def analyze_disk_space():
    try:
        limit = int(input("Enter the number of largest files/folders to show: "))
    except ValueError:
        print("Invalid number.")
        return

    directory = input("Enter the directory path: ")
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    items = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        try:
            if os.path.isdir(item_path):
                size = get_size_from_path(item_path)
            else:
                size = os.path.getsize(item_path)
            items.append((item, size))
        except Exception as e:
            continue

    items.sort(key=lambda x: x[1], reverse=True)
    print(f"\nTop {limit} largest items in '{directory}':")
    for item, size in items[:limit]:
        print(f"{item}: {size} bytes")


def get_size_from_path(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            try:
                filepath = os.path.join(dirpath, filename)
                total_size += os.path.getsize(filepath)
            except FileNotFoundError:
                continue
    return total_size


def main():
    print("Disk Manager Tool - Running in VM Test Environment")
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            list_disks()
        elif choice == "2":
            partition_disk()
        elif choice == "3":
            delete_partition()
        elif choice == "4":
            format_partition()
        elif choice == "5":
            mount_partition()
        elif choice == "6":
            unmount_partition()
        elif choice == "7":
            display_disk_space_usage()
        elif choice == "8":
            get_size()
        elif choice == "9":
            analyze_disk_space()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
