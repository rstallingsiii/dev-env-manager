#!/usr/bin/env python3

import subprocess
import time
from pathlib import Path
import shutil

errorLog = Path('errorLog.txt').touch

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

def restore_configs():
	home_dir = Path.home()
	
# Copy each file to its actual location
	for config_file in Path('./configs').iterdir():
		dest = home_dir / config_file.name
		
		# Backup existing file before restoring
		if dest.exists():
			try:
				backup = dest.with_suffix(dest.suffix + '.backup')
				shutil.copy2(dest, backup)
				print(f"Backed up existing {dest.name}")
			except Exception as e:	
				print(f"❌ Failed to backup {dest.name}: {e}")	

		
		try: 
			shutil.copy2(config_file, dest)
			print(f"✅ Restored {config_file.name}!")
		except Exception as e:
			print(f"❌ Failed to restore {config_file.name}: {e}")	
		

def clone_git(git_Projects):
	home_dir = Path.home()
	dest = home_dir / 'git_projects'
	
	print(dest)

	# Copy Git Projects
	for project in git_Projects:
		try:
			subprocess.run(['git', 'clone', project, dest])
			print(f"✅ {project} has been cloned successfully!")	
		except Exception as e: 
			print(f"❌ Failed to install {project}: {e}")	
			



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


	packageResponse = input("Continue with installation? (y/n): ")

	while packageResponse.lower() not in ['y','n']: 
		packageResponse = input("Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): ")
	
		# Install if user confirms 
	if packageResponse.lower() == 'y':
		print("\nStarting installation...\n")
		for package in pacman_packages:
			install_package(package)
		print("\n✅ All packages installed")
	else: 
		print("❌ Installation cancelled")

	# Install AUR Packages if user confirms 
	if packageResponse.lower() == 'y':
		print("\nStarting installation...\n")
		for package in aur_packages:
			install_package(package)
		print("\n✅ All packages installed")
	else: 
		print("❌ Installation cancelled")

	# Restore dotfiles to new computer
	print("Dotfiles will now be restored...\n")
	time.sleep(3)

	configResponse = input("Continue with installation? (y/n): ")

	while configResponse.lower() not in ['y','n']: 
		configResponse = input("Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): ")
	
		# Install if user confirms 
	if configResponse.lower() == 'y':
		# Clone git projects
		print("Beginning Restoration Process...\n")
		time.sleep(3)
		restore_configs()
		print("\n✅ All configs have been restored")
	else: 
		print("\n❌ Restoration cancelled")

	time.sleep(3)


	# Git Projects 
	git_Projects = ['https://github.com/rstallingsiii/robofriends.git', 'https://github.com/rstallingsiii/Virtual-Assistant.git' , 'https://github.com/rstallingsiii/SpurgeonAi.git', 'https://github.com/rstallingsiii/Todo-List.git' ]

	print(f"\nThe following Git Projects will be installed: \n {', '.join(git_Projects)}")

	gitResponse = input("Continue with installation? (y/n): ")

	while gitResponse.lower() not in ['y','n']: 
		gitResponse = input("Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): ")
	
		# Install if user confirms 
	if gitResponse.lower() == 'y':
		# Clone git projects
		print("Cloning git projects...\n")
		time.sleep(3)
		clone_git(git_Projects)
		print("\n✅ All packages installed")
	else: 
		print("\n❌ Installation cancelled")


	

if __name__ == "__main__":
	main()
