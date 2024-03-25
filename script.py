import os

def count_unique_g_keys(input_file, output_file):
    unique_keys = set()  # Zbiór dla przechowywania unikalnych g-keys

    # Otwieranie pliku wejściowego do odczytu
    with open(input_file, 'r') as file:
        for line in file:
            # Szukanie linii zawierających "g-key:"
            if "g-key:" in line:
                # Wycinanie g-key z linii
                key = line.split("g-key:")[1].strip()
                unique_keys.add(key)  # Dodawanie g-key do zbioru unikalnych kluczy

    # Sprawdzanie istnienia pliku wyjściowego i tworzenie go, jeśli nie istnieje
    if not os.path.exists(output_file):
        open(output_file, 'w').close()

    # Zapisywanie liczby unikalnych g-keys do pliku wyjściowego
    with open(output_file, 'w') as out_file:
        out_file.write(f"Liczba unikalnych g-keys: {len(unique_keys)}\n")
        out_file.write("Lista unikalnych g-keys:\n")
        for key in unique_keys:
            out_file.write(key + '\n')

# Pobieranie ścieżki bieżącego katalogu
current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, "input.txt")  # Ścieżka do pliku wejściowego
output_file_path = os.path.join(current_directory, "output.txt")  # Ścieżka do pliku wyjściowego
count_unique_g_keys(input_file_path, output_file_path)
