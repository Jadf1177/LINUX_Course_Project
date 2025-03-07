#!/bin/bash

# Check if a CSV file argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <CSV_FILE>"
    exit 1
fi

CSV_FILE="$1"

# Validate that the file exists
if [ ! -f "$CSV_FILE" ]; then
    echo "Error: CSV file '$CSV_FILE' not found!"
    exit 1
fi

# Validate CSV format (Checking if it has at least a header row)
HEADER=$(head -n 1 "$CSV_FILE")
if [[ ! "$HEADER" =~ "Plant,Height,Leaf Count,Dry Weight" ]]; then
    echo "Error: CSV format is incorrect!"
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed!"
    exit 1
fi

# Check if VENV exists, if not, create one
if [ ! -d "venv" ]; then
    echo "Creating a new virtual environment..."
    python3 -m venv venv
fi

# Activate VENV
source venv/bin/activate

# Install required dependencies if not already installed
pip install --upgrade pip
pip install matplotlib pandas argparse

# Run Python script to process CSV
mkdir -p Diagrams_3/Q4
python3 process_csv.py "$CSV_FILE"

# Backup Diagrams_3
mkdir -p BACKUPS/Diagrams_3
cp -r Diagrams_3 BACKUPS/

echo "CSV processing complete! Plots saved in Diagrams_3/Q4/"
