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
filepath = '/Users/'+username+'/Desktop/PEBLExports/Corsi/corsi-detail-'+participant_id+'.csv'
filepath2 = '/Users/'+username+'/Desktop/PEBLExports/Corsi/corsi-trial-'+participant_id+'.csv'
filepath3 = '/Users/'+username+'/Desktop/PEBLData/corsi_data.csv'
filepath4 = '/Users/'+username+'/Desktop/PEBLData/'

if not os.path.exists(filepath4):
    os.mkdir(filepath4) #make the above filepath if it doesn't exist

DataExport = []
list_to_append = []

Header = ['record_id', 'redcap_event_name','corsi_posx_p_1_1', 'corsi_posy_p_1_1', 'corsi_posx_p_1_2', 'corsi_posy_p_1_2', 'corsi_posx_p_1_3', 'corsi_posy_p_1_3', 'corsi_numcorr_p_1', 'corsi_nummiss_p_1', 'corsi_allcorr_p_1', 'corsi_rt_p_1', 'corsi_posx_p_2_1', 'corsi_posy_p_2_1', 'corsi_posx_p_2_2', 'corsi_posy_p_2_2', 'corsi_posx_p_2_3', 'corsi_posy_p_2_3', 'corsi_numcorr_p_2', 'corsi_nummiss_p_2', 'corsi_allcorr_p_2', 'corsi_rt_p_2', 'corsi_posx_p_3_1', 'corsi_posy_p_3_1', 'corsi_posx_p_3_2', 'corsi_posy_p_3_2', 'corsi_posx_p_3_3', 'corsi_posy_p_3_3', 'corsi_numcorr_p_3', 'corsi_nummiss_p_3', 'corsi_allcorr_p_3', 'corsi_rt_p_3', 'corsi_posx_t_1_1', 'corsi_posy_t_1_1', 'corsi_posx_t_1_2', 'corsi_posy_t_1_2', 'corsi_numcorr_t_1', 'corsi_nummiss_t_1', 'corsi_allcorr_t_1', 'corsi_rt_t_1', 'corsi_posx_t_2_1', 'corsi_posy_t_2_1', 'corsi_posx_t_2_2', 'corsi_posy_t_2_2', 'corsi_numcorr_t_2', 'corsi_nummiss_t_2', 'corsi_allcorr_t_2', 'corsi_rt_t_2', 'corsi_posx_t_3_1', 'corsi_posy_t_3_1', 'corsi_posx_t_3_2', 'corsi_posy_t_3_2', 'corsi_posx_t_3_3', 'corsi_posy_t_3_3', 'corsi_numcorr_t_3', 'corsi_nummiss_t_3', 'corsi_allcorr_t_3', 'corsi_rt_t_3', 'corsi_posx_t_4_1', 'corsi_posy_t_4_1', 'corsi_posx_t_4_2', 'corsi_posy_t_4_2', 'corsi_posx_t_4_3', 'corsi_posy_t_4_3', 'corsi_numcorr_t_4', 'corsi_nummiss_t_4', 'corsi_allcorr_t_4', 'corsi_rt_t_4', 'corsi_posx_t_5_1', 'corsi_posy_t_5_1', 'corsi_posx_t_5_2', 'corsi_posy_t_5_2', 'corsi_posx_t_5_3', 'corsi_posy_t_5_3', 'corsi_posx_t_5_4', 'corsi_posy_t_5_4', 'corsi_numcorr_t_5', 'corsi_nummiss_t_5', 'corsi_allcorr_t_5', 'corsi_rt_t_5', 'corsi_posx_t_6_1', 'corsi_posy_t_6_1', 'corsi_posx_t_6_2', 'corsi_posy_t_6_2', 'corsi_posx_t_6_3', 'corsi_posy_t_6_3', 'corsi_posx_t_6_4', 'corsi_posy_t_6_4', 'corsi_numcorr_t_6', 'corsi_nummiss_t_6', 'corsi_allcorr_t_6', 'corsi_rt_t_6', 'corsi_posx_t_7_1', 'corsi_posy_t_7_1', 'corsi_posx_t_7_2', 'corsi_posy_t_7_2', 'corsi_posx_t_7_3', 'corsi_posy_t_7_3', 'corsi_posx_t_7_4', 'corsi_posy_t_7_4', 'corsi_posx_t_7_5', 'corsi_posy_t_7_5', 'corsi_numcorr_t_7', 'corsi_nummiss_t_7', 'corsi_allcorr_t_7', 'corsi_rt_t_7', 'corsi_posx_t_8_1', 'corsi_posy_t_8_1', 'corsi_posx_t_8_2', 'corsi_posy_t_8_2', 'corsi_posx_t_8_3', 'corsi_posy_t_8_3', 'corsi_posx_t_8_4', 'corsi_posy_t_8_4', 'corsi_posx_t_8_5', 'corsi_posy_t_8_5', 'corsi_numcorr_t_8', 'corsi_nummiss_t_8', 'corsi_allcorr_t_8', 'corsi_rt_t_8', 'corsi_posx_t_9_1', 'corsi_posy_t_9_1', 'corsi_posx_t_9_2', 'corsi_posy_t_9_2', 'corsi_posx_t_9_3', 'corsi_posy_t_9_3', 'corsi_posx_t_9_4', 'corsi_posy_t_9_4', 'corsi_posx_t_9_5', 'corsi_posy_t_9_5', 'corsi_posx_t_9_6', 'corsi_posy_t_9_6', 'corsi_numcorr_t_9', 'corsi_nummiss_t_9', 'corsi_allcorr_t_9', 'corsi_rt_t_9', 'corsi_posx_t_10_1', 'corsi_posy_t_10_1', 'corsi_posx_t_10_2', 'corsi_posy_t_10_2', 'corsi_posx_t_10_3', 'corsi_posy_t_10_3', 'corsi_posx_t_10_4', 'corsi_posy_t_10_4', 'corsi_posx_t_10_5', 'corsi_posy_t_10_5', 'corsi_posx_t_10_6', 'corsi_posy_t_10_6', 'corsi_numcorr_t_10', 'corsi_nummiss_t_10', 'corsi_allcorr_t_10', 'corsi_rt_t_10', 'corsi_posx_t_11_1', 'corsi_posy_t_11_1', 'corsi_posx_t_11_2', 'corsi_posy_t_11_2', 'corsi_posx_t_11_3', 'corsi_posy_t_11_3', 'corsi_posx_t_11_4', 'corsi_posy_t_11_4', 'corsi_posx_t_11_5', 'corsi_posy_t_11_5', 'corsi_posx_t_11_6', 'corsi_posy_t_11_6', 'corsi_posx_t_11_7', 'corsi_posy_t_11_7', 'corsi_numcorr_t_11', 'corsi_nummiss_t_11', 'corsi_allcorr_t_11', 'corsi_rt_t_11', 'corsi_posx_t_12_1', 'corsi_posy_t_12_1', 'corsi_posx_t_12_2', 'corsi_posy_t_12_2', 'corsi_posx_t_12_3', 'corsi_posy_t_12_3', 'corsi_posx_t_12_4', 'corsi_posy_t_12_4', 'corsi_posx_t_12_5', 'corsi_posy_t_12_5', 'corsi_posx_t_12_6', 'corsi_posy_t_12_6', 'corsi_posx_t_12_7', 'corsi_posy_t_12_7', 'corsi_numcorr_t_12', 'corsi_nummiss_t_12', 'corsi_allcorr_t_12', 'corsi_rt_t_12']

i = 0

with open(filepath) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.append(line[0])
			DataExport.append(line[10])
			DataExport.append(line[11])
			i = i + 1
		else:
			DataExport.append(line[10])
			DataExport.append(line[11])

redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

i = 0

with open(filepath2) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.insert(8, line[8])
			DataExport.insert(9, line[9])
			DataExport.insert(10, line[10])
			DataExport.insert(11, line[11])
			i = i + 1
		elif i == 2:
			DataExport.insert(18, line[8])
			DataExport.insert(19, line[9])
			DataExport.insert(20, line[10])
			DataExport.insert(21, line[11])
			i = i + 1
		elif i == 3:
			DataExport.insert(28, line[8])
			DataExport.insert(29, line[9])
			DataExport.insert(30, line[10])
			DataExport.insert(31, line[11])
			i = i + 1
		elif i == 4:
			DataExport.insert(36, line[8])
			DataExport.insert(37, line[9])
			DataExport.insert(38, line[10])
			DataExport.insert(39, line[11])
			i = i + 1
		elif i == 5:
			DataExport.insert(44, line[8])
			DataExport.insert(45, line[9])
			DataExport.insert(46, line[10])
			DataExport.insert(47, line[11])
			i = i + 1
		elif i == 6:
			DataExport.insert(54, line[8])
			DataExport.insert(55, line[9])
			DataExport.insert(56, line[10])
			DataExport.insert(57, line[11])
			i = i + 1
		elif i == 7:
			DataExport.insert(64, line[8])
			DataExport.insert(65, line[9])
			DataExport.insert(66, line[10])
			DataExport.insert(67, line[11])
			i = i + 1
		elif i == 8:
			DataExport.insert(76, line[8])
			DataExport.insert(77, line[9])
			DataExport.insert(78, line[10])
			DataExport.insert(79, line[11])
			i = i + 1
		elif i == 9:
			DataExport.insert(88, line[8])
			DataExport.insert(89, line[9])
			DataExport.insert(90, line[10])
			DataExport.insert(91, line[11])
			i = i + 1
		elif i == 10:
			DataExport.insert(102, line[8])
			DataExport.insert(103, line[9])
			DataExport.insert(104, line[10])
			DataExport.insert(105, line[11])
			i = i + 1
		elif i == 11:
			DataExport.insert(116, line[8])
			DataExport.insert(117, line[9])
			DataExport.insert(118, line[10])
			DataExport.insert(119, line[11])
			i = i + 1
		elif i == 12:
			DataExport.insert(132, line[8])
			DataExport.insert(133, line[9])
			DataExport.insert(134, line[10])
			DataExport.insert(135, line[11])
			i = i + 1
		elif i == 13:
			DataExport.insert(148, line[8])
			DataExport.insert(149, line[9])
			DataExport.insert(150, line[10])
			DataExport.insert(151, line[11])
			i = i + 1
		elif i == 14:
			DataExport.insert(166, line[8])
			DataExport.insert(167, line[9])
			DataExport.insert(168, line[10])
			DataExport.insert(169, line[11])
			i = i + 1
		elif i == 15:
			DataExport.append(line[8])
			DataExport.append(line[9])
			DataExport.append(line[10])
			DataExport.append(line[11])

write_csv(DataExport)
