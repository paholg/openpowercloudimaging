#!/usr/bin/python2
import os, subprocess, argparse, requests, shutil
import kickstarts

distrobutions = ["Ubuntu"]

parser = argparse.ArgumentParser(description="Setup cloud things")
parser.add_argument("distro", type=str, help="Linux distrobution to setup", choices=distrobutions)
parser.add_argument("--packages", type=str, nargs="+", help="List of packages to install. These should exist in the repos for the distrobution")
args = parser.parse_args()

if args.distro == "Ubuntu":
    kickstart = kickstarts.ubuntu(args.packages)
    image = "images/ubuntu.iso"
    if not os.path.exists(image):
        os.makedirs("images")
        url = "http://ports.ubuntu.com/ubuntu-ports/dists/trusty-updates/main/installer-ppc64el/current/images/netboot/mini.iso"
        print "Image not found. Downloading."
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(image, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
else:
    print "Invalid distrobution: " + args.distro
    print "This script should have errored earlier. This is a bug."
    exit(1)

# Do shit here with qemu
# should only need kickstart and image at this point
