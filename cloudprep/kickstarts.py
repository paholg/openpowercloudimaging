def ubuntu(packages):
    kickstart = """
lang en_US
langsupport en_US
keyboard us
mouse
timezone America/Los_Angeles

rootpw root
user ubuntu --fullname "Ubuntu User" --password root4me2

reboot
text
install

#Installation media
cdrom
#nfs --server=server.com --dir=/path/to/ubuntu/

#System bootloader configuration
bootloader --location=mbr

#Clear the Master Boot Record
zerombr yes

#Partition clearing information
clearpart --all --initlabel

#Basic disk partition
part / --fstype ext4 --size 1 --grow --asprimary
part swap --size 256
part /boot --fstype ext4 --size 256 --asprimary

#System authorization infomation
auth  --useshadow  --enablemd5

#Network information
network --bootproto=dhcp --device=eth0

#Firewall configuration
firewall --disabled --trust=eth0 --ssh

#Do not configure the X Window System
skipx
"""
    if packages is not None:
        kickstart += "%packages\n"
        for package in packages:
            kickstart += package + "\n"
    return kickstart
