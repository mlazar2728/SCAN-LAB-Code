import csv
import os
import getpass

def write_csv(value):
	while True:
		try: 
			with open(filepath2, 'r') as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				for line in readCSV:
					list_to_append.append(line)
				break
		except IOError:
			break
	list_to_append.append(value)
	if list_to_append[0] != Header:
		list_to_append.insert(0, Header)
	with open(filepath2, 'w', newline='\n') as csvfile:
		writeCSV = csv.writer(csvfile, delimiter=',')
		for list in list_to_append:
			writeCSV.writerow(list)
		csvfile.close()


username = getpass.getuser() #extract username
participant_id = input('Input participant ID:	')
participant_id = participant_id.lower()
filepath = "/Users/" + username + "/Desktop/PEBLExports/Tapping/tapping-summary-"+participant_id+".txt"
filepath2 = "/Users/" + username + "/Desktop/PEBLData/tapping_data.csv"
filepath3 = "/Users/" + username + "/Desktop/PEBLData/"

if not os.path.exists(filepath3):
    os.mkdir(filepath3) #make the above filepath if it doesn't exist

Header = ['record_id','redcap_event_name','tapping_dominant_hand','tappping_dominant_hits_1','tapping_dominant_rt_1','tapping_dominant_sd_1','tappping_dominant_hits_2','tapping_dominant_rt_2','tapping_dominant_sd_2','tappping_dominant_hits_3','tapping_dominant_rt_3','tapping_dominant_sd_3','tapping_non_dominant_hand','tappping_non_dominant_hits_1','tapping_non_dominant_rt_1','tapping_non_dominant_sd_1','tappping_non_dominant_hits_2','tapping_non_dominant_rt_2','tapping_non_dominant_sd_2','tappping_non_dominant_hits_3','tapping_non_dominant_rt_3','tapping_non_dominant_sd_3']
data_line = [15, 16, 17, 25, 26, 27,]
data_store = []
DataExport = []
list_to_append = []

with open(filepath) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if line:
			str1 = ' '.join(str(e) for e in line)
			str1 = str1.split(' ')
			str1 = list(filter(None, str1))
			data_store.append(str1)

for values in data_line:
	if values == 15:
		DataExport.append(data_store[7][2])
		DataExport.append(data_store[9][2])
		DataExport.append(data_store[values][1])
		DataExport.append(data_store[values][2])
		DataExport.append(data_store[values][3])

	elif values == 16 or values == 17:
		DataExport.append(data_store[values][1])
		DataExport.append(data_store[values][2])
		DataExport.append(data_store[values][3])

	elif values == 25:
		DataExport.append(data_store[26][2])
		DataExport.append(data_store[values][1])
		DataExport.append(data_store[values][2])
		DataExport.append(data_store[values][3])

	elif values == 26 or values == 27:
		DataExport.append(data_store[values][1])
		DataExport.append(data_store[values][2])
		DataExport.append(data_store[values][3])


redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

write_csv(DataExport)