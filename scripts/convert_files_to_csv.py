import os
import json
import polars as pl


def fetch_json_files(folder_path = "output_research") -> list[str]:
    json_files = []
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            json_files.append(file_path)
    return json_files

 
csvHeader = {
    "firstName": "",
    "lastName": "",
    "customerNote": "",
    "email": "",
    "linkdin": "",
    "title": "",
    "website": "",
    "companyName": "",
    "companySummary": "",
    "products": "[]" # list of products string
 }



def load_json_to_df(file_path: str) -> pl.DataFrame:
    with open(file_path) as f:
        data = json.load(f)
    return pl.DataFrame(data)


json_file_paths = fetch_json_files()
