import pandas as pd

try:
    df = pd.read_csv('/Users/mac/Downloads/ufc_dataset/raw_fighter_details.csv')
    print("CSV file found and loaded successfully!")
    # Do your data analysis tasks on the DataFrame here
except FileNotFoundError:
    print("File not found!")



