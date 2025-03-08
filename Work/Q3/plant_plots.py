import matplotlib.pyplot as plt
import pandas as pd
import os

# Define the correct directory
output_dir = os.path.join(os.getcwd(), "Diagrams_2/")
os.makedirs(output_dir, exist_ok=True)

# Read the CSV file
csv_file = "plants.csv"
if not os.path.exists(csv_file):
    print(f"Error: {csv_file} not found.")
    exit(1)

# Read plant data from CSV
data = pd.read_csv(csv_file)

# Ensure required columns exist
required_columns = ["Plant", "Height", "Leaf Count", "Dry Weight"]
for col in required_columns:
    if col not in data.columns:
        print(f"Error: Missing column {col} in CSV file.")
        exit(1)

# Get the first plant's data
plant = data["Plant"].iloc[0]
height_data = data["Height"].tolist()
leaf_count_data = data["Leaf Count"].tolist()
dry_weight_data = data["Dry Weight"].tolist()

# Scatter Plot - Height vs Leaf Count
plt.figure(figsize=(10, 6))
plt.scatter(height_data, leaf_count_data, color='b')
plt.title(f'Height vs Leaf Count for {plant}')
plt.xlabel('Height (cm)')
plt.ylabel('Leaf Count')
plt.grid(True)
plt.savefig(os.path.join(output_dir, f"{plant}_scatter.png"))
plt.close()

# Histogram - Distribution of Dry Weight
plt.figure(figsize=(10, 6))
plt.hist(dry_weight_data, bins=5, color='g', edgecolor='black')
plt.title(f'Histogram of Dry Weight for {plant}')
plt.xlabel('Dry Weight (g)')
plt.ylabel('Frequency')
plt.grid(True)
plt.savefig(os.path.join(output_dir, f"{plant}_histogram.png"))
plt.close()

# Line Plot - Plant Height Over Time
weeks = range(1, len(height_data) + 1)  # Create a range for weeks
plt.figure(figsize=(10, 6))
plt.plot(weeks, height_data, marker='o', color='r')
plt.title(f'{plant} Height Over Time')
plt.xlabel('Week')
plt.ylabel('Height (cm)')
plt.grid(True)
plt.savefig(os.path.join(output_dir, f"{plant}_line_plot.png"))
plt.close()

# Output confirmation
print(f"✅ Generated plots for {plant}:")
print(f"📂 Scatter plot saved as {output_dir}{plant}_scatter.png")
print(f"📂 Histogram saved as {output_dir}{plant}_histogram.png")
print(f"📂 Line plot saved as {output_dir}{plant}_line_plot.png")

