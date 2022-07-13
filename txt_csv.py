import pandas as pd

file = pd.read_csv(r'C:\Users\Usuario\OneDrive\Desktop\Python\Data.txt')
new_csv_file = file.to_csv(r'C:\Users\Usuario\OneDrive\Desktop\Python\Data_csv.csv')