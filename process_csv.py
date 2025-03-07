import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from datetime import datetime

# Validate argument
if len(sys.argv) < 2:
    print("Usage: python3 process_csv.py <CSV_FILE>")
    sys.exit(1)

csv_file = sys.argv[1]

# Load CSV
try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print(f"Error reading CSV: {e}")
    sys.exit(1)

# Ensure expected columns exist
required_columns = ["Plant", "Height", "Leaf Count", "Dry Weight"]
for col in required_columns:
    if col not in df.columns:
        print(f"Error: Missing required column '{col}' in CSV.")
        sys.exit(1)

# Convert numeric values from string to lists
df["Height"] = df["Height"].apply(lambda x: list(map(int, x.strip('"').split())))
df["Leaf Count"] = df["Leaf Count"].apply(lambda x: list(map(int, x.strip('"').split())))
df["Dry Weight"] = df["Dry Weight"].apply(lambda x: list(map(float, x.strip('"').split())))

# Create output directory
output_dir = "Diagrams_3/Q4"
os.makedirs(output_dir, exist_ok=True)

# Generate Plots
for index, row in df.iterrows():
    plant_name = row["Plant"]

    # Height plot
    plt.figure()
    plt.plot(row["Height"], marker='o', linestyle='-', label="Height")
    plt.xlabel("Time")
    plt.ylabel("Height (cm)")
    plt.title(f"{plant_name} - Growth Over Time")
    plt.legend()
    plt.savefig(f"{output_dir}/{plant_name}_height.png")

    # Leaf count plot
    plt.figure()
    plt.plot(row["Leaf Count"], marker='s', linestyle='--', label="Leaf Count")
    plt.xlabel("Time")
    plt.ylabel("Leaf Count")
    plt.title(f"{plant_name} - Leaf Growth")
    plt.legend()
    plt.savefig(f"{output_dir}/{plant_name}_leaf.png")

    # Dry weight plot
    plt.figure()
    plt.plot(row["Dry Weight"], marker='^', linestyle='-.', label="Dry Weight")
    plt.xlabel("Time")
    plt.ylabel("Dry Weight (g)")
    plt.title(f"{plant_name} - Dry Weight Over Time")
    plt.legend()
    plt.savefig(f"{output_dir}/{plant_name}_dry_weight.png")

print("✅ Plots successfully generated in", output_dir)
