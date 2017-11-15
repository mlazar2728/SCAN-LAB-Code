import csv
import os
import getpass

def write_csv(value):
	while True:
		try: 
			with open(filepath3, 'r') as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				for line in readCSV:
					list_to_append.append(line)
				break
		except IOError:
			break
	list_to_append.append(value)
	if list_to_append[0] != Header:
		list_to_append.insert(0, Header)
	with open(filepath3, 'w', newline='\n') as csvfile:
		writeCSV = csv.writer(csvfile, delimiter=',')
		for list in list_to_append:
			writeCSV.writerow(list)
		csvfile.close()

username = getpass.getuser() #extract username
participant_id = input('Input participant ID:	')
participant_id = participant_id.lower()
filepath2 = '/Users/'+username+'/Desktop/PEBLExports/Tol/tol-summary-'+participant_id+'.csv'
filepath3 = '/Users/'+username+'/Desktop/PEBLData/tol_data.csv'
filepath4 = '/Users/'+username+'/Desktop/PEBLData/'

if not os.path.exists(filepath4):
    os.mkdir(filepath4) #make the above filepath if it doesn't exist

Header = ['record_id', 'redcap_event_name', 'tol_size_1', 'tol_shortest_1', 'tol_success_1', 'tol_steps_1', 'tol_time_1','tol_size_2', 'tol_shortest_2', 'tol_success_2', 'tol_steps_2', 'tol_time_2','tol_size_3', 'tol_shortest_3', 'tol_success_3', 'tol_steps_3', 'tol_time_3','tol_size_4', 'tol_shortest_4', 'tol_success_4', 'tol_steps_4', 'tol_time_4','tol_size_5', 'tol_shortest_5', 'tol_success_5', 'tol_steps_5', 'tol_time_5','tol_size_6', 'tol_shortest_6', 'tol_success_6', 'tol_steps_6', 'tol_time_6','tol_size_7', 'tol_shortest_7', 'tol_success_7', 'tol_steps_7', 'tol_time_7','tol_size_8', 'tol_shortest_8', 'tol_success_8', 'tol_steps_8', 'tol_time_8']

DataExport = []
list_to_append = []

i = 0

with open(filepath2) as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.append(line[0])
			DataExport.append(line[2])
			DataExport.append(line[3])
			DataExport.append(line[8])
			DataExport.append(line[11])
			DataExport.append(line[15])

			i = i + 1
		else:
			DataExport.append(line[2])
			DataExport.append(line[3])
			DataExport.append(line[8])
			DataExport.append(line[11])
			DataExport.append(line[15])

redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

write_csv(DataExport)
