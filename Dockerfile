FROM --platform=linux/amd64 archlinux:latest

# Maintainer info 
LABEL maintainer="rooseveltstallingsiii@gmail.com"

# Update system and istall EndeavourOS keyring + base tools
RUN pacman -Syu --noconfirm python git base-devel sudo nano  python-pip

# Copy requirements and install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install --break-system-packages --no-cache-dir -r /tmp/requirements.txt

# Add a non-root user for testing
RUN useradd -m -s /bin/bash devuser 
RUN echo "devuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Set working directory
WORKDIR /app

# Switch to the non-root user
USER devuser

# Default command

CMD [ "/bin/bash" ]