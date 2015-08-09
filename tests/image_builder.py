import os
import sys

IMG="../bin/brcm2708/openwrt-brcm2708-bcm2708-sdcard-vfat-ext4.img"

LOOPDEV="/dev/loop7"
OFFSET=29360128
MPOINT="mpoint"


def build():
    os.system("cd .. && time nice make -j 8")

def mount():
    umount()
    try: os.makedirs(MPOINT)
    except: pass
    print("sudo losetup -o %s -r %s %s" % (OFFSET, LOOPDEV, IMG))
    print("sudo mount -r %s %s" % (LOOPDEV, MPOINT))
    os.system("sudo losetup -o %s -r %s %s" % (OFFSET, LOOPDEV, IMG))
    os.system("sudo mount -r %s %s" % (LOOPDEV, MPOINT))

def umount():
    os.system("sudo umount %s &>/dev/null" % (LOOPDEV))
    os.system("sudo losetup -d %s &>/dev/null" % (LOOPDEV))

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'mount':
        mount()
    elif len(sys.argv) > 1 and sys.argv[1] == 'umount':
        umount()
    else:
        print("mount|umount")