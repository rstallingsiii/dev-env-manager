# Dev Environment Manager

A Python script to automatically set up my development environment on Arch-based Linux systems.

## What It Does

Currently:
- Installs a list of packages using pacman
- Asks for user confirmation before installing

Coming soon:
- AUR package support
- Config file management (dotfiles)
- Git repository cloning
- Command-line arguments for modular installation

## Requirements

- Arch Linux or Arch-based distro (EndeavourOS, Manjaro, etc.)
- Python 3.x
- sudo privileges

## Usage
```bash
chmod +x setup.py
./setup.py
```

## Current Package List

- htop - system monitor
- neofetch - system info display
- tree - directory viewer
- bat - syntax-highlighting cat alternative

## Testing with Docker

To test on macOS or other systems:
```bash
docker build -t dev-env-test .
docker run -it -v $(pwd):/app dev-env-test
```

## Project Goals

This is a learning project to:
- Practice Python scripting
- Learn subprocess and system automation
- Understand package management
- Build something I'll actually use

## Progress

- [x] Basic script structure
- [x] Single package installation
- [x] Multiple package installation
- [ ] User confirmation
- [ ] AUR support
- [ ] Config file management
- [ ] Git repo cloning

## License

Personal project - do whatever you want with it.