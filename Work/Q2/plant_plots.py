import argparse
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Argument parser
parser = argparse.ArgumentParser(description="Plant Growth Data Processor")
parser.add_argument("--plant", type=str, required=True, help="Name of the plant")
parser.add_argument("--height", nargs='+', type=int, required=True, help="List of plant heights")
parser.add_argument("--leaf_count", nargs='+', type=int, required=True, help="List of leaf counts")
parser.add_argument("--dry_weight", nargs='+', type=float, required=True, help="List of dry weight values")
args = parser.parse_args()

# Create Diagrams_2/Q2 directory
os.makedirs("Diagrams_2/Q2", exist_ok=True)

# Generate plots
plt.figure()
plt.plot(args.height, marker='o', linestyle='-', color='b', label="Height")
plt.xlabel("Time")
plt.ylabel("Height (cm)")
plt.title(f"Growth of {args.plant}")
plt.legend()
plt.savefig(f"Diagrams_2/Q2/height_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

plt.figure()
plt.plot(args.leaf_count, marker='s', linestyle='--', color='g', label="Leaf Count")
plt.xlabel("Time")
plt.ylabel("Number of Leaves")
plt.title(f"Leaf Count for {args.plant}")
plt.legend()
plt.savefig(f"Diagrams_2/Q2/leaf_count_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

plt.figure()
plt.plot(args.dry_weight, marker='^', linestyle='-.', color='r', label="Dry Weight")
plt.xlabel("Time")
plt.ylabel("Dry Weight (g)")
plt.title(f"Dry Weight of {args.plant}")
plt.legend()
plt.savefig(f"Diagrams_2/Q2/dry_weight_plot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

# Show plots (optional)
# plt.show()
