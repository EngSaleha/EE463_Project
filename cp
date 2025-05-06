fallocate -l 1G test_disk.img
sudo losetup -fP test_disk.img
losetup -a  # Note your loop device (e.g., /dev/loop0)
