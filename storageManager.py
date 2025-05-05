import os
import subprocess
def display_menu():
    print("********** Menu: Disk Management **************")
    print("1. List all available disks")
    print("2. Partition a disk")
    print("3. Delete Partition ")
    print("4. Format Partition ")
    print("5. Mount Partition ")
    print("6. Unmount Partition ")
    print("7. Display Disk Space Usage")
    print("8. Exit")

def list_disks():
    subprocess.run(["fdisk", "-l"])

def partition_disk():
    subprocess.run(["fdisk", "-l"])
    disk = input("Enter the disk name (e.g., /dev/sdX): ")
    subprocess.run(["fdisk", disk])
    
def delete_partition():
    subprocess.run(["fdisk", "-l"])
    disk = input("Enter the disk name (e.g., /dev/sdX): ")
    partition_number = input("Enter the partition number to delete (e.g., 1,2,): ")
    subprocess.run(["parted", disk, "rm", partition_number])
    
def format_partition():
    subprocess.run(["fdisk", "-l"])
    disk = input("Enter the disk name (e.g., /dev/sdX): ")
    partition_number = input("Enter the partition number to format (e.g., 1): ")
    filesystem_type = input("Enter the filesystem type (e.g., ext4): ")
    subprocess.run(["mkfs", f"-t{filesystem_type}", f"{disk}{partition_number}"])
    
def mount_partition():
    subprocess.run(["fdisk", "-l"])
    partition = input("Enter the partition to mount (e.g., /dev/sdXn): ")
    mount_point = input("Enter the mount point (e.g., /mnt/dir/:")
    subprocess.run(["mkdir", "-p", mount_point])
    subprocess.run(["mount", partition, mount_point])

def unmount_partition():
    subprocess.run(["fdisk", "-l"])
    mount_point = input("Enter the mount point to unmount (e.g., /mnt/my_partition): ")
    subprocess.run(["umount", mount_point])

def display_disk_space_usage():
    subprocess.run(["df", "-h"])

def main():
    print("Starting...", flush=True)
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
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

