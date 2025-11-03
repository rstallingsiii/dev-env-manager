#!/usr/bin/env python3

import subprocess
import time



def install_package(package_name):
	
	print(f"Installing {package_name}...")
	result = subprocess.run(['sudo', 'pacman', '-S', package_name, '--noconfirm'])

	if result.returncode == 0:
		print(f"✅ {package_name} installed successfully!")
	else: 
		print(f"❌ Failed to install {package_name}")	

def install_aur_package(package_name):
	print(f"Installing {package_name}...")
	result = subprocess.run(['yay', '-S', package_name, '--noconfirm'])

	if result.returncode == 0:
		print(f"✅ {package_name} installed successfully!")
	else: 
		print(f"❌ Failed to install {package_name}")	


def main():
	print("🚀 Dev Environment Manager")
	print("Setting up your environment...")

	# List of packages to install
	pacman_packages = ['htop', 'neofetch', 'tree', 'bat', 'tldr']

	aur_packages = ['bat-extras', 'downgrade', 'ttf-meslo-nerd-font-powerlevel10k']

	# Show what will be installed
	print(f"\nThe following Pacman packages will be installed: \n {', '.join(pacman_packages)}")

	time.sleep(2)

	print(f"\nThe following AUR packages will be installed: \n {', '.join(aur_packages)}")


	response = input("Continue with installation? (y/n): ")

	while response.lower() not in ['y','n']: 
		response = input("Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): ")
	
		# Install if user confirms 
	if response.lower() == 'y':
		print("\nStarting installation...\n")
		for package in pacman_packages:
			install_package(package)
		print("\n✅ All packages installed")
	else: 
		print("❌ Installation cancelled")

	# Install AUR Packages if user confirms 
	if response.lower() == 'y':
		print("\nStarting installation...\n")
		for package in aur_packages:
			install_package(package)
		print("\n✅ All packages installed")
	else: 
		print("❌ Installation cancelled")




if __name__ == "__main__":
	main()
