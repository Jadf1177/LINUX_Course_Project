# Use Ubuntu as the base image
FROM ubuntu:latest

# Install required packages
RUN apt update && apt install -y nano imagemagick

# Set work directory inside the container
WORKDIR /app

# Copy all images into the container
COPY images/ /app/images/

# Set default command (interactive shell)
CMD ["/bin/bash"]
