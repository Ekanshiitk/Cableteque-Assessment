"""
@author: ekanshbajpai
"""

import os
import pandas as pd
import itertools
import json
import sys 

def generate_bicycles(excel_path: str) -> str:
    

    if not os.path.isabs(excel_path):
        raise ValueError("Error: The input file path must be an absolute path.")

    if not os.path.isfile(excel_path):
        raise FileNotFoundError(f"Error: The file '{excel_path}' does not exist.")

    xls = pd.read_excel(excel_path, sheet_name=None)

    id_sheet = xls.get("ID")
    if id_sheet is None:
        raise ValueError("Error: Missing 'ID' sheet in the Excel file.")

    id_components = {col: id_sheet[col].dropna().astype(str).tolist() for col in id_sheet.columns}

    if "Wheels" in id_components:
        id_components["Wheels"] = [str(int(float(w))) for w in id_components["Wheels"]]


    id_keys = list(id_components.keys())
    id_values = list(itertools.product(*id_components.values()))

    id_list = ["".join(map(str, values)) for values in id_values]

    general_sheet = xls.get("GENERAL")
    if general_sheet is None:
        raise ValueError("Error: Missing 'GENERAL' sheet in the Excel file.")

    general_data = general_sheet.iloc[0].to_dict()

    for key in ["Has suspension", "Logo"]:
        if key in general_data:
            general_data[key] = bool(general_data[key])  

    modification_sheets = {
        sheet: data.dropna(how="all") for sheet, data in xls.items() if sheet not in ["ID", "GENERAL"]
    }
    
    modifications = {}
    for sheet_name, sheet_data in modification_sheets.items():
        for _, row in sheet_data.iterrows():
            if row.empty or pd.isna(row.iloc[0]):  
                continue

            designator_value = str(row.iloc[0]).strip()
            mod_data = row.iloc[1:].dropna().to_dict()

            for key in ["Has suspension", "Logo"]:
                if key in mod_data:
                    mod_data[key] = bool(mod_data[key])  

            if designator_value not in modifications:
                modifications[designator_value] = []
            modifications[designator_value].append(mod_data)

    # Generate all possible bicycle configurations
    bicycles = []
    for id_tuple in id_values:
        bike_data = {"ID": "".join(map(str, id_tuple)), **general_data}
        for key, value in zip(id_keys, id_tuple):
            if value in modifications:
                for mod in modifications[value]:
                    bike_data.update(mod)
        bicycles.append(bike_data.copy())

    return json.dumps(bicycles, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python bicycle_generator.py /absolute/path/to/Bicycle.xlsx")
        sys.exit(1)  # Exit the script if no argument is provided

    excel_file = sys.argv[1]  # Get file path from the command line

    # Ensure the file path is absolute
    if not os.path.isabs(excel_file):
        print("Error: Please provide an absolute path to the Excel file.")
        sys.exit(1)

    try:
        output_json = generate_bicycles(excel_file)  # Generate bicycles
        print(output_json)  # Print JSON output to the terminal
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)