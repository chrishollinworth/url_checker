import csv
import json

with open('test.csv') as csv_file:
    json_array = []
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    with open('output.json', 'w') as f:
        for row in csv_reader:
            json_array.append(row)

        json_output = json.dumps(json_array, indent=4)
        f.write(json_output)