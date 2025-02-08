'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code

import json

def parse_packaging(packaging_data: str) -> list[dict]:
    parsed_data = []
    packaging_data = packaging_data.replace('in', '/')
    packaging_data = packaging_data.replace(' / ', '/')
    packaging_list = packaging_data.split('/')
    for thing in packaging_list:
        items = thing.strip().split(' ')
        if len(items) == 2:
            object = {items[1]: int(items[0])}
            parsed_data.append(object)

    return parsed_data

def calc_total_units(package: list[dict]) -> int:
    
    total = 1
    for item in package:
        for value in item.values():
            total *= value

    return total

def get_unit(package: list[dict]) -> str:
    first = package[0]
    for key in first.keys():
        return key

packages = []
input_file = "data/packaging.txt"
output_file = "data/packaging.json"

with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            parsed_package = parse_packaging(line)
            packages.append(parsed_package)
            total_units = calc_total_units(parsed_package)
            unit = get_unit(parsed_package)
            print(f"{line} => total units: {total_units} {unit}")

with open(output_file, "w") as file:
    json.dump(packages, file, indent=4)
