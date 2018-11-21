import csv

def str_column_to_float(dataset, column):
	for row in dataset:
		row[column] = float(row[column].strip())

def dataset_minmax(dataset):
	minmax = list()
	for i in range(len(dataset[0])):
		col_values = [row[i] for row in dataset]
		value_min = min(col_values)
		value_max = max(col_values)
		minmax.append([value_min, value_max])
	return minmax
 
def normalize_dataset(dataset, minmax):
	for row in dataset:
		for i in range(len(row)):
			row[i] = 7*((row[i] - minmax[i][0]) / (minmax[i][1] - minmax[i][0]))
 

filename = '/home/sowmyasudan/Documents/DisVoice-master/prosody/log.csv'
with open(filename) as csvfile:
	    lines = csv.reader(csvfile, delimiter=' ', quotechar='|')
	    dataset = list(lines)
for i in range(len(dataset[0])):
	str_column_to_float(dataset, i)

print(dataset[0])

minmax = dataset_minmax(dataset)

normalize_dataset(dataset, minmax)

print(dataset[0])
