import pandas as pd
import os 

current_directory = os.getcwd()
input_file_path = os.path.join(current_directory, "data.csv")
df = pd.read_csv(input_file_path)

df
