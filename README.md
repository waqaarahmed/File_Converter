# File Converter

This Python script allows you to convert data between different file formats, including JSON, CSV, and text files. You can convert data from JSON to CSV, CSV to JSON, JSON to text, and text to JSON.

## Usage

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Navigate to the directory containing the Python script.
4. Modify the file paths in the script to point to your input and output files.
5. Run the Python script using a Python interpreter.

## Dependencies

- pandas (`pd`): Used for reading and writing data in CSV format.
- json: Used for reading and writing data in JSON format.

You can install the required dependencies using pip:

```bash
pip install pandas
```

## Functionality

### JSON to CSV Conversion

Converts data from JSON format to CSV format.

```
import pandas as pd

# Read JSON file
to_csv = pd.read_json("intents.json")

# Convert to CSV file
to_csv.to_csv("intents.csv")
```

### CSV to JSON Conversion

Converts data from CSV format to JSON format.

```
import pandas as pd

# Read CSV file
from_csv = pd.read_csv("intents.csv")

# Convert to JSON file
from_csv.to_json("converted_from_csv.json")
```

### JSON to Text File Conversion

Converts data from JSON format to a text file.

```
import json

# Read JSON file
with open('intents.json') as file:
    data = json.load(file)

# Convert to text file
js_file = json.dumps(data)
with open("intents.txt", "w") as f:
    f.write(js_file)
```
