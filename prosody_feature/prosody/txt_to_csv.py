import csv

with open('featuresDDKst.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    lines = (line.split(" ") for line in stripped if line)
    with open('log.csv', 'a') as out_file:
        writer = csv.writer(out_file)
       # writer.writecol(('title', 'intro'))
        writer.writerows(lines)