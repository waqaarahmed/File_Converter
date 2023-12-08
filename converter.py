import pandas as pd

#from json to csv
to_csv = pd.read_json(r"C:\Users\ahmed\.vscode\File_Converter\intents.json")
to_csv.to_csv(r"C:\Users\ahmed\.vscode\File_Converter\intents.csv")

#from csv to json
from_csv = pd.read_csv(r"C:\Users\ahmed\.vscode\File_Converter\intents.csv")
from_csv.to_json(r"C:\Users\ahmed\.vscode\File_Converter\converted_from_csv.json")