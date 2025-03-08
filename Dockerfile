# Use Ubuntu as the base image
FROM ubuntu:latest

# Install required packages
RUN apt update && apt install -y nano imagemagick

# Set work directory inside the container
WORKDIR /app

# Copy images into the container
COPY images/ /app/images/

# Copy the image processing script into the container
COPY process_images.sh /app/process_images.sh

# Make the script executable
RUN chmod +x /app/process_images.sh

# Set default command (interactive shell)
CMD ["/bin/bash"]

