import csv
import json

data_path = "./data/debt_collector_list/debt_collector_list_uncleaned.csv"
new_file_path = "./data/debt_collector_list/debt_collector_list_cleaned.csv"

if __name__ == "__main__":
    all_name = set()

    with open(data_path, newline='') as f:
        [
            all_name.add(
                line.strip('\n').strip(', LLC').strip(', Inc.')
                )
            for line in f
        ]

    with open(new_file_path, "w") as f:
        for name in all_name:
            f.write(name+'\n')