#!/bin/bash

CSV_FILE="plants.csv"

# Function to create a CSV file
create_csv() {
    echo "Plant,Height,Leaf Count,Dry Weight" > "$CSV_FILE"
    echo "CSV file created: $CSV_FILE"
}

# Function to display the CSV file
display_csv() {
    if [[ -f "$CSV_FILE" ]]; then
        column -s, -t < "$CSV_FILE" | less -S
    else
        echo "CSV file not found!"
    fi
}

# Function to add a new plant entry
add_plant() {
    echo "Enter plant name:"
    read plant
    echo "Enter heights (space-separated):"
    read -a height
    echo "Enter leaf counts (space-separated):"
    read -a leaf_count
    echo "Enter dry weights (space-separated):"
    read -a dry_weight

    echo "$plant,\"${height[*]}\",\"${leaf_count[*]}\",\"${dry_weight[*]}\"" >> "$CSV_FILE"
    echo "Plant added successfully!"
}

# Function to sort the CSV file by plant name
sort_csv() {
    if [[ -f "$CSV_FILE" ]]; then
        (head -n 1 "$CSV_FILE"; tail -n +2 "$CSV_FILE" | sort) > temp.csv
        mv temp.csv "$CSV_FILE"
        echo "CSV sorted by plant name."
    else
        echo "CSV file not found!"
    fi
}

# Function to delete a plant entry by name
delete_plant() {
    echo "Enter plant name to delete:"
    read plant
    if [[ -f "$CSV_FILE" ]]; then
        grep -v "^$plant," "$CSV_FILE" > temp.csv
        mv temp.csv "$CSV_FILE"
        echo "Plant deleted successfully!"
    else
        echo "CSV file not found!"
    fi
}

# Function to find the plant with the highest average leaf count
highest_leaf_count() {
    if [[ -f "$CSV_FILE" ]]; then
        awk -F, 'NR>1 {
            sum=0; n=split($3, counts, " ");
            for (i=1; i<=n; i++) sum+=counts[i];
            avg=sum/n;
            if (avg > max) { max = avg; plant = $1; }
        } END { print "Plant with highest average leaf count:", plant, "(Avg:", max, ")"}' "$CSV_FILE"
    else
        echo "CSV file not found!"
    fi
}

# Function to execute `plant_plots.py`
run_python_script() {
highest_leaf_count() {
    if [[ -f "$CSV_FILE" ]]; then
        awk -F, 'NR>1 {
            # Remove quotes from the Leaf Count column
            gsub(/"/, "", $3);
            
            # Split the values by space
            sum = 0;
            n = split($3, counts, " ");
            
            # Calculate sum and average
            for (i = 1; i <= n; i++) sum += counts[i];
            avg = sum / n;
            
            # Find the plant with the highest average leaf count
            if (avg > max) { max = avg; plant = $1; }
        } END {
            if (max > 0) 
                print "Plant with highest average leaf count:", plant, "(Avg:", max, ")";
            else
                print "No valid leaf count data found.";
        }' "$CSV_FILE"
    else
        echo "CSV file not found!"
    fi
}
    python3 Work/Q2/plant_plots.py --plant "Rose" --height 50 55 60 65 70 --leaf_count 35 40 45 50 55 --dry_weight 2.0 2.2 2.5 2.7 3.0
}

# Menu system
while true; do
    echo -e "\n🌱 Plant CSV Management 🌱"
    echo "1. Create CSV File"
    echo "2. Select CSV File"
    echo "3. Display CSV"
    echo "4. Add a New Plant"
    echo "5. Run plant_plots.py"
    echo "6. Sort CSV by Plant Name"
    echo "7. Delete a Plant Entry"
    echo "8. Find Plant with Highest Avg Leaf Count"
    echo "9. Exit"

    read -p "Choose an option: " option

    case $option in
        1) create_csv ;;
        2) echo "Selected file: $CSV_FILE" ;;
        3) display_csv ;;
        4) add_plant ;;
        5) run_python_script ;;
        6) sort_csv ;;
        7) delete_plant ;;
        8) highest_leaf_count ;;
        9) echo "Exiting..."; exit ;;
        *) echo "Invalid option, please try again!" ;;
    esac
done
