import pandas as pd
import json

#from json to csv
to_csv = pd.read_json(r"C:\Users\ahmed\.vscode\File_Converter\intents.json")
to_csv.to_csv(r"C:\Users\ahmed\.vscode\File_Converter\intents.csv")

#from csv to json
from_csv = pd.read_csv(r"C:\Users\ahmed\.vscode\File_Converter\intents.csv")
from_csv.to_json(r"C:\Users\ahmed\.vscode\File_Converter\converted_from_csv.json")

#from json to text file
file = open('intents.json')
data = json.load(file)
js_file = json.dumps(data)
with open("intents.txt", "w") as f:
    f.write(js_file)
    
#from text to json
file = 'intents.txt'
dict1 = {}
with open(file) as fh:
 
    for line in fh:
        command, description = line.strip().split(None, 1)
        dict1[command] = description.strip()

out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()
        
