#!/bin/bash

echo "Processing images..."

# Create processed images directory if not exists
mkdir -p /app/processed

# Loop through all images in the images directory
for img in /app/images/*.{jpg,png}; do
    if [[ -f "$img" ]]; then
        filename=$(basename "$img")
        
        # Resize the image
        convert "$img" -resize 200x200 "/app/processed/resized_$filename"

        # Add a watermark
        convert "/app/processed/resized_$filename" -gravity south -pointsize 20 -draw "text 0,10 'Watermark'" "/app/processed/watermarked_$filename"

        echo "Processed $filename"
    fi
done

echo "Processing complete. Images saved in /app/processed"
