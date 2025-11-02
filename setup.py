#!/usr/bin/env python3

import subprocess
import time


def install_package(package_name):
	subprocess.run(['sudo', 'pacman', '-S', package_name ])
    # Hint: you'll need 'sudo pacman -S package_name'
    # Hint: subprocess.run() takes a list of arguments
    


def main():
	print("🚀 Dev Environment Manager")
	print("Setting up your environment...")

	print("Testing subprocesses...")
	time.sleep(2)

	subprocess.run(['echo', 'Hello from subprocess!'])	

	# Test: Listing Files
	print("\nListing files:")
	subprocess.run(['ls', '-la'])

	# Test3: Check installed packages
	print("\nChecking for Python:")
	subprocess.run(['pacman', '-Q', 'python'])

	install_package('libreoffice-fresh')

if __name__ == "__main__":
	main()
