import csv
import tldextract

with open('top-1m.csv') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    with open('test.csv', mode='w') as new_csv_file:
        fieldnames = ['name', 'url' ]
        writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv_reader:
            ext = tldextract.extract(row[1])
            writer.writerow({'name': ext.domain, 'url': f'www.{row[1]}'})
            line_count += 1
    print(f'Processed {line_count} lines.')


