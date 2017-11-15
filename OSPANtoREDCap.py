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
filepath = '/Users/'+ username + '/Desktop/PEBLExports/Ospan/ospan-'+participant_id+'.csv'
filepath2 = '/Users/'+ username + '/Desktop/PEBLData/ospan_data.csv'
filepath3 = '/Users/'+ username + '/Desktop/PEBLData/'

if not os.path.exists(filepath3):
    os.mkdir(filepath3) #make the above filepath if it doesn't exist

DataExport = []
list_to_append = []

Header = ['record_id', 'redcap_event_name', 'ospan_probtime_22', 'ospan_length_22', 'ospan_stim_22', 'ospan_resp_22', 'ospan_memcorr_22', 'ospan_time_22', 'ospan_distcorr_22', 'ospan_numcorrdist_22', 'ospan_totnumdist_22', 'ospan_runningcorrect_22', 'ospan_runningtotal_22', 'ospan_probtime_24', 'ospan_length_24', 'ospan_stim_24', 'ospan_resp_24', 'ospan_memcorr_24', 'ospan_time_24', 'ospan_distcorr_24', 'ospan_numcorrdist_24', 'ospan_totnumdist_24', 'ospan_runningcorrect_24', 'ospan_runningtotal_24', 'ospan_probtime_31', 'ospan_length_31', 'ospan_stim_31', 'ospan_resp_31', 'ospan_memcorr_31', 'ospan_time_31', 'ospan_distcorr_31', 'ospan_numcorrdist_31', 'ospan_totnumdist_31', 'ospan_runningcorrect_31', 'ospan_runningtotal_31', 'ospan_probtime_36', 'ospan_length_36', 'ospan_stim_36', 'ospan_resp_36', 'ospan_memcorr_36', 'ospan_time_36', 'ospan_distcorr_36', 'ospan_numcorrdist_36', 'ospan_totnumdist_36', 'ospan_runningcorrect_36', 'ospan_runningtotal_36', 'ospan_probtime_43', 'ospan_length_43', 'ospan_stim_43', 'ospan_resp_43', 'ospan_memcorr_43', 'ospan_time_43', 'ospan_distcorr_43', 'ospan_numcorrdist_43', 'ospan_totnumdist_43', 'ospan_runningcorrect_43', 'ospan_runningtotal_43', 'ospan_probtime_46', 'ospan_length_46', 'ospan_stim_46', 'ospan_resp_46', 'ospan_memcorr_46', 'ospan_time_46', 'ospan_distcorr_46', 'ospan_numcorrdist_46', 'ospan_totnumdist_46', 'ospan_runningcorrect_46', 'ospan_runningtotal_46', 'ospan_probtime_50', 'ospan_length_50', 'ospan_stim_50', 'ospan_resp_50', 'ospan_memcorr_50', 'ospan_time_50', 'ospan_distcorr_50', 'ospan_numcorrdist_50', 'ospan_totnumdist_50', 'ospan_runningcorrect_50', 'ospan_runningtotal_50', 'ospan_probtime_54', 'ospan_length_54', 'ospan_stim_54', 'ospan_resp_54', 'ospan_memcorr_54', 'ospan_time_54', 'ospan_distcorr_54', 'ospan_numcorrdist_54', 'ospan_totnumdist_54', 'ospan_runningcorrect_54', 'ospan_runningtotal_54', 'ospan_probtime_61', 'ospan_length_61', 'ospan_stim_61', 'ospan_resp_61', 'ospan_memcorr_61', 'ospan_time_61', 'ospan_distcorr_61', 'ospan_numcorrdist_61', 'ospan_totnumdist_61', 'ospan_runningcorrect_61', 'ospan_runningtotal_61', 'ospan_probtime_67', 'ospan_length_67', 'ospan_stim_67', 'ospan_resp_67', 'ospan_memcorr_67', 'ospan_time_67', 'ospan_distcorr_67', 'ospan_numcorrdist_67', 'ospan_totnumdist_67', 'ospan_runningcorrect_67', 'ospan_runningtotal_67', 'ospan_probtime_72', 'ospan_length_72', 'ospan_stim_72', 'ospan_resp_72', 'ospan_memcorr_72', 'ospan_time_72', 'ospan_distcorr_72', 'ospan_numcorrdist_72', 'ospan_totnumdist_72', 'ospan_runningcorrect_72', 'ospan_runningtotal_72', 'ospan_probtime_75', 'ospan_length_75', 'ospan_stim_75', 'ospan_resp_75', 'ospan_memcorr_75', 'ospan_time_75', 'ospan_distcorr_75', 'ospan_numcorrdist_75', 'ospan_totnumdist_75', 'ospan_runningcorrect_75', 'ospan_runningtotal_75', 'ospan_probtime_79', 'ospan_length_79', 'ospan_stim_79', 'ospan_resp_79', 'ospan_memcorr_79', 'ospan_time_79', 'ospan_distcorr_79', 'ospan_numcorrdist_79', 'ospan_totnumdist_79', 'ospan_runningcorrect_79', 'ospan_runningtotal_79', 'ospan_probtime_82', 'ospan_length_82', 'ospan_stim_82', 'ospan_resp_82', 'ospan_memcorr_82', 'ospan_time_82', 'ospan_distcorr_82', 'ospan_numcorrdist_82', 'ospan_totnumdist_82', 'ospan_runningcorrect_82', 'ospan_runningtotal_82', 'ospan_probtime_89', 'ospan_length_89', 'ospan_stim_89', 'ospan_resp_89', 'ospan_memcorr_89', 'ospan_time_89', 'ospan_distcorr_89', 'ospan_numcorrdist_89', 'ospan_totnumdist_89', 'ospan_runningcorrect_89', 'ospan_runningtotal_89', 'ospan_probtime_94', 'ospan_length_94', 'ospan_stim_94', 'ospan_resp_94', 'ospan_memcorr_94', 'ospan_time_94', 'ospan_distcorr_94', 'ospan_numcorrdist_94', 'ospan_totnumdist_94', 'ospan_runningcorrect_94', 'ospan_runningtotal_94', 'ospan_probtime_100', 'ospan_length_100', 'ospan_stim_100', 'ospan_resp_100', 'ospan_memcorr_100', 'ospan_time_100', 'ospan_distcorr_100', 'ospan_numcorrdist_100', 'ospan_totnumdist_100', 'ospan_runningcorrect_100', 'ospan_runningtotal_100']
i = 0

with open (filepath) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.append(line[0])
			DataExport.append(line[2])
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
			i = i + 1
		else:
			DataExport.append(line[2])
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

redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

write_csv(DataExport)
