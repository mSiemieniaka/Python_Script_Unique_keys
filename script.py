import csv
import os

def count_unique_g_keys(input_file, output_file):
    unique_keys = set()  

    
    with open(input_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            
            if "g-key" in row:
                key = row["g-key"].strip()
                unique_keys.add(key)  

    
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    
    with open(output_file, 'w') as out_file:
        out_file.write(f"Liczba unikalnych g-keys: {len(unique_keys)}\n")
        out_file.write("Lista unikalnych g-keys:\n")
        for key in unique_keys:
            out_file.write(key + '\n')


current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, "input.csv")  # Ścieżka do pliku CSV
output_file_path = os.path.join(current_directory, "output.txt")  # Ścieżka do pliku wyjściowego
count_unique_g_keys(input_file_path, output_file_path)
