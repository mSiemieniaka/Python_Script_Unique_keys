import os
import pandas as pd

def countUnique(input_file, output_file):
    unique_keys = set()  

    
    with open(input_file, 'r') as file:
        for line in file:
            
            if "gcid:" in line:
                
                key = line.split("gcid:")[1].strip()
                unique_keys.add(key)  

    
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    
    with open(output_file, 'w') as out_file:
        out_file.write(f"Liczba unikalnych gcid: {len(unique_keys)}\n")
        out_file.write("\nLista unikalnych gcid:\n")
        for key in unique_keys:
            out_file.write(key + '\n')

current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, "input.txt")  # Ścieżka do pliku wejściowego
output_file_path = os.path.join(current_directory, "output.txt")  # Ścieżka do pliku wyjściowego
countUnique(input_file_path, output_file_path)
