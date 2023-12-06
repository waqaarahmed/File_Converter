import pandas as pd
file = pd.read_json(r"C:\Users\ahmed\.vscode\File_Converter\intents.json")
file.to_csv(r"C:\Users\ahmed\.vscode\File_Converter\intents.csv")