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
filepath2 = '/Users/'+username+'/Desktop/PEBLExports/TLX/tlx-data.csv'
filepath3 = '/Users/'+username+'/Desktop/PEBLData/TLX_data.csv'
filepath4 = '/Users/'+username+'/Desktop/PEBLData/'

if not os.path.exists(filepath4):
    os.mkdir(filepath4) #make the above filepath if it doesn't exist

DataExport = []
list_to_append = []

Header = ['record_id', 'redcap_event_name', 'nasatlx_test_ tlx_score', 'nasatlx_test_ scale_mental', 'nasatlx_test_ scale_physical', 'nasatlx_test_ scale_temporal', 'nasatlx_test_ scale_perform', 'nasatlx_test_ scale_effort', 'nasatlx_test_ scale_frustration', 'nasatlx_test_ workload_mental', 'nasatlx_test_ workload_physical', 'nasatlx_test_ workload_temporal', 'nasatlx_test_ workload_perform', 'nasatlx_test_ workload_effort', 'nasatlx_test_ workload_frustration', 'nasatlx_test_ workloadweighted_mental', 'nasatlx_test_ workloadweighted_physical', 'nasatlx_test_ workloadweighted_temporal', 'nasatlx_test_ workloadweighted_perform', 'nasatlx_test_ workloadweighted_effort', 'nasatlx_test_ workloadweighted_frustration']
i = 0


with open (filepath2) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.append(line[2])
			DataExport.append(((int(line[4])*int(line[10]))+(int(line[5])*int(line[11]))+(int(line[6])*int(line[12]))+(int(line[7])*int(line[13]))+(int(line[8])*int(line[14]))+(int(line[9])*int(line[15])))/15)
			DataExport.append(line[4])
			DataExport.append(line[5])
			DataExport.append(line[6])
			DataExport.append(line[7])
			DataExport.append(line[8])
			DataExport.append(line[9])
			DataExport.append(line[10])
			DataExport.append(line[11])
			DataExport.append(line[12])
			DataExport.append(line[13])
			DataExport.append(line[14])
			DataExport.append(line[15])
			DataExport.append(int(line[4])*int(line[10]))
			DataExport.append(int(line[5])*int(line[11]))
			DataExport.append(int(line[6])*int(line[12]))
			DataExport.append(int(line[7])*int(line[13]))
			DataExport.append(int(line[8])*int(line[14]))
			DataExport.append(int(line[9])*int(line[15]))
			i = i + 1
			
	


redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

write_csv(DataExport)

