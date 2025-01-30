import json
import csv
import sys
import pathlib

if len(sys.argv) != 2:
    exit()

in_filename = sys.argv[1]

with open(in_filename, "r") as file:
    output = open(pathlib.Path(in_filename).with_suffix(".json"), "w")
    reader = csv.reader(file)
    header = next(reader)
    next(reader)
    dictionary = {}
    for line in reader:
        state = line[0]
        dictionary.update({state : {}})
        for key, value in zip(header[1:], line[1:]):
            dictionary[state].update({key : float(value)})
        
    output.write(json.dumps(dictionary, ensure_ascii=True))