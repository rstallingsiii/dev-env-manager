FROM --platform=linux/amd64 archlinux:latest

# Maintainer info 
LABEL maintainer="rooseveltstallingsiii@gmail.com"

# Update system and istall EndeavourOS keyring + base tools
RUN pacman -Syu --noconfirm 
RUN pacman -S --noconfirm python git base-devel sudo nano wget

# Add a non-root user for testing
RUN useradd -m -s /bin/bash devuser 
RUN echo "devuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


# Set working directory
WORKDIR /app

# Switch to the non-root user
USER devuser

# Default command

CMD [ "/bin/bash" ]