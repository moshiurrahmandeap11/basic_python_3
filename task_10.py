# JSON File Handling with dictiornaries and write and read

import json

def write_dict_to_json_file(data, filename):
    with open(filename, "w") as json_file:
        json.dump(data, json_file)

def read_dict_from_json_file(filename):
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    return data

# Example usage
data = {"name": "Alice", "age": 30, "city": "New York"}
filename = "data.json"
write_dict_to_json_file(data, filename)
read_data = read_dict_from_json_file(filename)
print("Data read from json file:", read_data)