#!/usr/bin/env python3
import shutil
import subprocess
import time
from pathlib import Path

from colorist import Color

errorLog = Path("errorLog.txt").touch


def install_package(package_name):
    print(f"Installing {package_name}...")
    result = subprocess.run(["sudo", "pacman", "-S", package_name, "--noconfirm"])

    if result.returncode == 0:
        print(f"✅ {Color.GREEN} {package_name} installed successfully!{Color.OFF}")
        return True
    else:
        print(f"❌ {Color.RED} Failed to install {package_name}")
        return False


def install_aur_package(package_name):
    print(f"Installing {package_name}...")
    result = subprocess.run(["yay", "-S", package_name, "--noconfirm"])

    if result.returncode == 0:
        print(f"✅ {Color.GREEN} {package_name} installed successfully{Color.OFF}!")
        return True
    else:
        print(f"❌ {Color.RED} Failed to install {package_name}")
        return False


def restore_config(config_file):
    home_dir = Path.home()

    # Copy each file to its actual location

    dest = home_dir / config_file.name

    # Backup existing file before restoring
    if dest.exists():
        try:
            backup = dest.with_suffix(dest.suffix + ".backup")
            shutil.copy2(dest, backup)
            print(f"✅ {Color.GREEN} Backed up existing {dest.name}{Color.OFF}")
        except Exception as e:
            print(f"❌ {Color.RED} Failed to backup {dest.name}: {e}{Color.OFF}")

    try:
        shutil.copy2(config_file, dest)
        print(f"✅ {Color.GREEN} Restored {config_file.name}{Color.OFF}!")
        return True
    except Exception as e:
        print(f"❌ {Color.RED} Failed to restore {config_file.name}: {e}{Color.OFF}")
        return False


def clone_git(repo):
    home_dir = Path.home()
    dest = home_dir / "git_projects"
    repoName = Path(repo.split("/")[-1]).stem
    projectPath = dest / repoName
    

    print(projectPath)
    time.sleep(3)
    # Copy Git Projects

    result = subprocess.run(["git", "clone", repo, projectPath])

    if result.returncode == 0:
        print(f"✅ {Color.GREEN} {repo} has been cloned successfully{Color.OFF}!")
        return True
    else:
        print(f"❌ {Color.RED} Failed to install {repo} {Color.OFF}")
        return False


def main():
    print("🚀 Dev Environment Manager")
    print("Setting up your environment...")

    packageCounter = 0
    configCounter = 0
    gitCounter = 0

    # List of packages to install
    pacman_packages = ["htop", "neofetch", "tree", "bat", "tldr"]

    aur_packages = ["bat-extras", "downgrade", "ttf-meslo-nerd-font-powerlevel10k"]

    # Show what will be installed
    print("================\n")
    print(f"📦 {Color.BLUE}PACKAGE INSTALLATION{Color.OFF}")
    print("================\n")

    print(
        f"\nThe following Pacman packages will be installed: \n {', '.join(pacman_packages)}"
    )

    time.sleep(2)

    print(
        f"\nThe following AUR packages will be installed: \n {', '.join(aur_packages)}"
    )

    packageResponse = input("Continue with installation? (y/n): ")

    while packageResponse.lower() not in ["y", "n"]:
        packageResponse = input(
            "Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): "
        )

        # Install if user confirms
    if packageResponse.lower() == "y":
        print("\nStarting installation...\n")
        pacman_length = len(pacman_packages)
        for index, package in enumerate(pacman_packages, start=1):
            print(f"[{index}/{pacman_length}] : {package}")
            if install_package(package):
                packageCounter += 1
        print(f"\n✅ {Color.GREEN} All packages installed {Color.OFF}")
    else:
        print(f"❌ {Color.RED} Installation cancelled {Color.OFF}")

    # Install AUR Packages if user confirms
    if packageResponse.lower() == "y":
        print("\nStarting installation...\n")
        aur_length = len(aur_packages)

        for index, package in enumerate(aur_packages, start=1):
            print(f"[{index}/ {aur_length}] : {package}")
            if install_package(package):
                packageCounter += 1
        print(f"\n✅ {Color.GREEN} All packages installed {Color.OFF}")
    else:
        print(f"❌ {Color.RED} Installation cancelled {Color.OFF}")

    # Restore dotfiles to new computer
    print("================\n")
    print(f"\n 📁 {Color.BLUE}CONFIGURATION FILE RESTORATION{Color.OFF}")
    print("================\n")

    print("Dotfiles will now be restored...\n")
    time.sleep(3)

    configResponse = input("Continue with installation? (y/n): ")

    while configResponse.lower() not in ["y", "n"]:
        configResponse = input(
            "Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): "
        )

        # Install if user confirms
    if configResponse.lower() == "y":
        print("Beginning Restoration Process...\n")
        time.sleep(3)
        for config_file in Path("./configs").iterdir():
            if restore_config(config_file):
                configCounter += 1

        print(f"\n✅ {Color.GREEN} All configs have been restored {Color.OFF}")
    else:
        print(f"\n❌ {Color.RED} Restoration cancelled {Color.OFF}")

    time.sleep(3)

    # Git Projects
    print("================\n")
    print(f"\n 🌐 {Color.BLUE}PACKAGE INSTALLATION{Color.OFF}")
    print("================\n")

    git_Projects = [
        "https://github.com/rstallingsiii/robofriends.git",
        "https://github.com/rstallingsiii/Virtual-Assistant.git",
        "https://github.com/rstallingsiii/SpurgeonAi.git",
        "https://github.com/rstallingsiii/Todo-List.git",
    ]

    print(
        f"\nThe following Git Projects will be installed: \n {', '.join(git_Projects)}"
    )

    gitResponse = input("Continue with installation? (y/n): ")

    while gitResponse.lower() not in ["y", "n"]:
        gitResponse = input(
            "Please answer with 'y' for 'yes' or 'n' for 'no'. \nContinue with installation? (y/n): "
        )

        # Install if user confirms
    if gitResponse.lower() == "y":
        # Clone git projects
        print("Cloning git projects...\n")
        time.sleep(3)
        for repo in git_Projects:
            if clone_git(repo):
                gitCounter += 1
        print(f"\n✅ {Color.GREEN} All packages installed {Color.OFF}")
    else:
        print(f"\n❌ {Color.RED} Installation cancelled {Color.OFF}")

    time.sleep(3)

    print("================\n")
    print(f"\n 🌐 {Color.BLUE}SUMMARY{Color.OFF}")
    print("================\n")
    print(f"Installed {packageCounter} packages\n")
    print(f"Installed {configCounter} packages\n")
    print(f"Installed {gitCounter} packages\n")


if __name__ == "__main__":
    main()
