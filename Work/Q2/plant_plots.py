import matplotlib.pyplot as plt
import argparse

def plot_data(plant, heights, leaf_counts, dry_weights):
    time_steps = range(1, len(heights) + 1)

    # Plot height over time
    plt.figure()
    plt.plot(time_steps, heights, marker='o', linestyle='-', color='b', label="Height")
    plt.xlabel("Time Steps")
    plt.ylabel("Height (cm)")
    plt.title(f"{plant} Height Over Time")
    plt.legend()
    plt.savefig(f"Diagrams_1/{plant}_height.png")

    # Plot leaf count over time
    plt.figure()
    plt.plot(time_steps, leaf_counts, marker='s', linestyle='--', color='g', label="Leaf Count")
    plt.xlabel("Time Steps")
    plt.ylabel("Leaf Count")
    plt.title(f"{plant} Leaf Count Over Time")
    plt.legend()
    plt.savefig(f"Diagrams_1/{plant}_leaf.png")

    # Plot dry weight over time
    plt.figure()
    plt.plot(time_steps, dry_weights, marker='^', linestyle='-.', color='r', label="Dry Weight")
    plt.xlabel("Time Steps")
    plt.ylabel("Dry Weight (g)")
    plt.title(f"{plant} Dry Weight Over Time")
    plt.legend()
    plt.savefig(f"Diagrams_1/{plant}_dry_weight.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Plot plant growth data")
    parser.add_argument("--plant", type=str, required=True, help="Plant name")
    parser.add_argument("--height", type=float, nargs='+', required=True, help="List of heights over time")
    parser.add_argument("--leaf_count", type=int, nargs='+', required=True, help="List of leaf counts over time")
    parser.add_argument("--dry_weight", type=float, nargs='+', required=True, help="List of dry weights over time")

    args = parser.parse_args()
    
    plot_data(args.plant, args.height, args.leaf_count, args.dry_weight)
