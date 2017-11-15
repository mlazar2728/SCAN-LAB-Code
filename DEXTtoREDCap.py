# Header = []
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
filepath2 = "/Users/" + username + "/Desktop/PEBLExports/Dext/dext-"+participant_id+".csv"
filepath3 = "/Users/" + username + "/Desktop/PEBLData/Dext_Data.csv"
filepath4 = "/Users/" + username + "/Desktop/PEBLData/"

if not os.path.exists(filepath4):
    os.mkdir(filepath4) #make the above filepath if it doesn't exist

DataExport = []
list_to_append = []

Header = ['record_id','redcap_event_name','dext_startx_1', 'dext_starty_1', 'dext_noise_1', 'dext_targx_1', 'dext_targy_1', 'dext_distance_1', 'dext_complete_1', 'dext_time_1', 'dext_moves_1', 'dext_startx_2', 'dext_starty_2', 'dext_noise_2', 'dext_targx_2', 'dext_targy_2', 'dext_distance_2', 'dext_complete_2', 'dext_time_2', 'dext_moves_2', 'dext_startx_3', 'dext_starty_3', 'dext_noise_3', 'dext_targx_3', 'dext_targy_3', 'dext_distance_3', 'dext_complete_3', 'dext_time_3', 'dext_moves_3', 'dext_startx_4', 'dext_starty_4', 'dext_noise_4', 'dext_targx_4', 'dext_targy_4', 'dext_distance_4', 'dext_complete_4', 'dext_time_4', 'dext_moves_4', 'dext_startx_5', 'dext_starty_5', 'dext_noise_5', 'dext_targx_5', 'dext_targy_5', 'dext_distance_5', 'dext_complete_5', 'dext_time_5', 'dext_moves_5', 'dext_startx_6', 'dext_starty_6', 'dext_noise_6', 'dext_targx_6', 'dext_targy_6', 'dext_distance_6', 'dext_complete_6', 'dext_time_6', 'dext_moves_6', 'dext_startx_7', 'dext_starty_7', 'dext_noise_7', 'dext_targx_7', 'dext_targy_7', 'dext_distance_7', 'dext_complete_7', 'dext_time_7', 'dext_moves_7', 'dext_startx_8', 'dext_starty_8', 'dext_noise_8', 'dext_targx_8', 'dext_targy_8', 'dext_distance_8', 'dext_complete_8', 'dext_time_8', 'dext_moves_8', 'dext_startx_9', 'dext_starty_9', 'dext_noise_9', 'dext_targx_9', 'dext_targy_9', 'dext_distance_9', 'dext_complete_9', 'dext_time_9', 'dext_moves_9', 'dext_startx_10', 'dext_starty_10', 'dext_noise_10', 'dext_targx_10', 'dext_targy_10', 'dext_distance_10', 'dext_complete_10', 'dext_time_10', 'dext_moves_10', 'dext_startx_11', 'dext_starty_11', 'dext_noise_11', 'dext_targx_11', 'dext_targy_11', 'dext_distance_11', 'dext_complete_11', 'dext_time_11', 'dext_moves_11', 'dext_startx_12', 'dext_starty_12', 'dext_noise_12', 'dext_targx_12', 'dext_targy_12', 'dext_distance_12', 'dext_complete_12', 'dext_time_12', 'dext_moves_12', 'dext_startx_13', 'dext_starty_13', 'dext_noise_13', 'dext_targx_13', 'dext_targy_13', 'dext_distance_13', 'dext_complete_13', 'dext_time_13', 'dext_moves_13', 'dext_startx_14', 'dext_starty_14', 'dext_noise_14', 'dext_targx_14', 'dext_targy_14', 'dext_distance_14', 'dext_complete_14', 'dext_time_14', 'dext_moves_14', 'dext_startx_15', 'dext_starty_15', 'dext_noise_15', 'dext_targx_15', 'dext_targy_15', 'dext_distance_15', 'dext_complete_15', 'dext_time_15', 'dext_moves_15', 'dext_startx_16', 'dext_starty_16', 'dext_noise_16', 'dext_targx_16', 'dext_targy_16', 'dext_distance_16', 'dext_complete_16', 'dext_time_16', 'dext_moves_16', 'dext_startx_17', 'dext_starty_17', 'dext_noise_17', 'dext_targx_17', 'dext_targy_17', 'dext_distance_17', 'dext_complete_17', 'dext_time_17', 'dext_moves_17', 'dext_startx_18', 'dext_starty_18', 'dext_noise_18', 'dext_targx_18', 'dext_targy_18', 'dext_distance_18', 'dext_complete_18', 'dext_time_18', 'dext_moves_18', 'dext_startx_19', 'dext_starty_19', 'dext_noise_19', 'dext_targx_19', 'dext_targy_19', 'dext_distance_19', 'dext_complete_19', 'dext_time_19', 'dext_moves_19', 'dext_startx_20', 'dext_starty_20', 'dext_noise_20', 'dext_targx_20', 'dext_targy_20', 'dext_distance_20', 'dext_complete_20', 'dext_time_20', 'dext_moves_20', 'dext_startx_21', 'dext_starty_21', 'dext_noise_21', 'dext_targx_21', 'dext_targy_21', 'dext_distance_21', 'dext_complete_21', 'dext_time_21', 'dext_moves_21', 'dext_startx_22', 'dext_starty_22', 'dext_noise_22', 'dext_targx_22', 'dext_targy_22', 'dext_distance_22', 'dext_complete_22', 'dext_time_22', 'dext_moves_22', 'dext_startx_23', 'dext_starty_23', 'dext_noise_23', 'dext_targx_23', 'dext_targy_23', 'dext_distance_23', 'dext_complete_23', 'dext_time_23', 'dext_moves_23', 'dext_startx_24', 'dext_starty_24', 'dext_noise_24', 'dext_targx_24', 'dext_targy_24', 'dext_distance_24', 'dext_complete_24', 'dext_time_24', 'dext_moves_24', 'dext_startx_25', 'dext_starty_25', 'dext_noise_25', 'dext_targx_25', 'dext_targy_25', 'dext_distance_25', 'dext_complete_25', 'dext_time_25', 'dext_moves_25', 'dext_startx_26', 'dext_starty_26', 'dext_noise_26', 'dext_targx_26', 'dext_targy_26', 'dext_distance_26', 'dext_complete_26', 'dext_time_26', 'dext_moves_26', 'dext_startx_27', 'dext_starty_27', 'dext_noise_27', 'dext_targx_27', 'dext_targy_27', 'dext_distance_27', 'dext_complete_27', 'dext_time_27', 'dext_moves_27', 'dext_startx_28', 'dext_starty_28', 'dext_noise_28', 'dext_targx_28', 'dext_targy_28', 'dext_distance_28', 'dext_complete_28', 'dext_time_28', 'dext_moves_28', 'dext_startx_29', 'dext_starty_29', 'dext_noise_29', 'dext_targx_29', 'dext_targy_29', 'dext_distance_29', 'dext_complete_29', 'dext_time_29', 'dext_moves_29', 'dext_startx_30', 'dext_starty_30', 'dext_noise_30', 'dext_targx_30', 'dext_targy_30', 'dext_distance_30', 'dext_complete_30', 'dext_time_30', 'dext_moves_30', 'dext_startx_31', 'dext_starty_31', 'dext_noise_31', 'dext_targx_31', 'dext_targy_31', 'dext_distance_31', 'dext_complete_31', 'dext_time_31', 'dext_moves_31', 'dext_startx_32', 'dext_starty_32', 'dext_noise_32', 'dext_targx_32', 'dext_targy_32', 'dext_distance_32', 'dext_complete_32', 'dext_time_32', 'dext_moves_32', 'dext_startx_33', 'dext_starty_33', 'dext_noise_33', 'dext_targx_33', 'dext_targy_33', 'dext_distance_33', 'dext_complete_33', 'dext_time_33', 'dext_moves_33', 'dext_startx_34', 'dext_starty_34', 'dext_noise_34', 'dext_targx_34', 'dext_targy_34', 'dext_distance_34', 'dext_complete_34', 'dext_time_34', 'dext_moves_34', 'dext_startx_35', 'dext_starty_35', 'dext_noise_35', 'dext_targx_35', 'dext_targy_35', 'dext_distance_35', 'dext_complete_35', 'dext_time_35', 'dext_moves_35', 'dext_startx_36', 'dext_starty_36', 'dext_noise_36', 'dext_targx_36', 'dext_targy_36', 'dext_distance_36', 'dext_complete_36', 'dext_time_36', 'dext_moves_36', 'dext_startx_37', 'dext_starty_37', 'dext_noise_37', 'dext_targx_37', 'dext_targy_37', 'dext_distance_37', 'dext_complete_37', 'dext_time_37', 'dext_moves_37', 'dext_startx_38', 'dext_starty_38', 'dext_noise_38', 'dext_targx_38', 'dext_targy_38', 'dext_distance_38', 'dext_complete_38', 'dext_time_38', 'dext_moves_38', 'dext_startx_39', 'dext_starty_39', 'dext_noise_39', 'dext_targx_39', 'dext_targy_39', 'dext_distance_39', 'dext_complete_39', 'dext_time_39', 'dext_moves_39', 'dext_startx_40', 'dext_starty_40', 'dext_noise_40', 'dext_targx_40', 'dext_targy_40', 'dext_distance_40', 'dext_complete_40', 'dext_time_40', 'dext_moves_40', 'dext_startx_41', 'dext_starty_41', 'dext_noise_41', 'dext_targx_41', 'dext_targy_41', 'dext_distance_41', 'dext_complete_41', 'dext_time_41', 'dext_moves_41', 'dext_startx_42', 'dext_starty_42', 'dext_noise_42', 'dext_targx_42', 'dext_targy_42', 'dext_distance_42', 'dext_complete_42', 'dext_time_42', 'dext_moves_42', 'dext_startx_43', 'dext_starty_43', 'dext_noise_43', 'dext_targx_43', 'dext_targy_43', 'dext_distance_43', 'dext_complete_43', 'dext_time_43', 'dext_moves_43', 'dext_startx_44', 'dext_starty_44', 'dext_noise_44', 'dext_targx_44', 'dext_targy_44', 'dext_distance_44', 'dext_complete_44', 'dext_time_44', 'dext_moves_44', 'dext_startx_45', 'dext_starty_45', 'dext_noise_45', 'dext_targx_45', 'dext_targy_45', 'dext_distance_45', 'dext_complete_45', 'dext_time_45', 'dext_moves_45', 'dext_startx_46', 'dext_starty_46', 'dext_noise_46', 'dext_targx_46', 'dext_targy_46', 'dext_distance_46', 'dext_complete_46', 'dext_time_46', 'dext_moves_46', 'dext_startx_47', 'dext_starty_47', 'dext_noise_47', 'dext_targx_47', 'dext_targy_47', 'dext_distance_47', 'dext_complete_47', 'dext_time_47', 'dext_moves_47', 'dext_startx_48', 'dext_starty_48', 'dext_noise_48', 'dext_targx_48', 'dext_targy_48', 'dext_distance_48', 'dext_complete_48', 'dext_time_48', 'dext_moves_48', 'dext_startx_49', 'dext_starty_49', 'dext_noise_49', 'dext_targx_49', 'dext_targy_49', 'dext_distance_49', 'dext_complete_49', 'dext_time_49', 'dext_moves_49', 'dext_startx_50', 'dext_starty_50', 'dext_noise_50', 'dext_targx_50', 'dext_targy_50', 'dext_distance_50', 'dext_complete_50', 'dext_time_50', 'dext_moves_50', 'dext_startx_51', 'dext_starty_51', 'dext_noise_51', 'dext_targx_51', 'dext_targy_51', 'dext_distance_51', 'dext_complete_51', 'dext_time_51', 'dext_moves_51', 'dext_startx_52', 'dext_starty_52', 'dext_noise_52', 'dext_targx_52', 'dext_targy_52', 'dext_distance_52', 'dext_complete_52', 'dext_time_52', 'dext_moves_52', 'dext_startx_53', 'dext_starty_53', 'dext_noise_53', 'dext_targx_53', 'dext_targy_53', 'dext_distance_53', 'dext_complete_53', 'dext_time_53', 'dext_moves_53', 'dext_startx_54', 'dext_starty_54', 'dext_noise_54', 'dext_targx_54', 'dext_targy_54', 'dext_distance_54', 'dext_complete_54', 'dext_time_54', 'dext_moves_54', 'dext_startx_55', 'dext_starty_55', 'dext_noise_55', 'dext_targx_55', 'dext_targy_55', 'dext_distance_55', 'dext_complete_55', 'dext_time_55', 'dext_moves_55', 'dext_startx_56', 'dext_starty_56', 'dext_noise_56', 'dext_targx_56', 'dext_targy_56', 'dext_distance_56', 'dext_complete_56', 'dext_time_56', 'dext_moves_56', 'dext_startx_57', 'dext_starty_57', 'dext_noise_57', 'dext_targx_57', 'dext_targy_57', 'dext_distance_57', 'dext_complete_57', 'dext_time_57', 'dext_moves_57', 'dext_startx_58', 'dext_starty_58', 'dext_noise_58', 'dext_targx_58', 'dext_targy_58', 'dext_distance_58', 'dext_complete_58', 'dext_time_58', 'dext_moves_58', 'dext_startx_59', 'dext_starty_59', 'dext_noise_59', 'dext_targx_59', 'dext_targy_59', 'dext_distance_59', 'dext_complete_59', 'dext_time_59', 'dext_moves_59', 'dext_startx_60', 'dext_starty_60', 'dext_noise_60', 'dext_targx_60', 'dext_targy_60', 'dext_distance_60', 'dext_complete_60', 'dext_time_60', 'dext_moves_60', 'dext_startx_61', 'dext_starty_61', 'dext_noise_61', 'dext_targx_61', 'dext_targy_61', 'dext_distance_61', 'dext_complete_61', 'dext_time_61', 'dext_moves_61', 'dext_startx_62', 'dext_starty_62', 'dext_noise_62', 'dext_targx_62', 'dext_targy_62', 'dext_distance_62', 'dext_complete_62', 'dext_time_62', 'dext_moves_62', 'dext_startx_63', 'dext_starty_63', 'dext_noise_63', 'dext_targx_63', 'dext_targy_63', 'dext_distance_63', 'dext_complete_63', 'dext_time_63', 'dext_moves_63', 'dext_startx_64', 'dext_starty_64', 'dext_noise_64', 'dext_targx_64', 'dext_targy_64', 'dext_distance_64', 'dext_complete_64', 'dext_time_64', 'dext_moves_64', 'dext_startx_65', 'dext_starty_65', 'dext_noise_65', 'dext_targx_65', 'dext_targy_65', 'dext_distance_65', 'dext_complete_65', 'dext_time_65', 'dext_moves_65', 'dext_startx_66', 'dext_starty_66', 'dext_noise_66', 'dext_targx_66', 'dext_targy_66', 'dext_distance_66', 'dext_complete_66', 'dext_time_66', 'dext_moves_66', 'dext_startx_67', 'dext_starty_67', 'dext_noise_67', 'dext_targx_67', 'dext_targy_67', 'dext_distance_67', 'dext_complete_67', 'dext_time_67', 'dext_moves_67', 'dext_startx_68', 'dext_starty_68', 'dext_noise_68', 'dext_targx_68', 'dext_targy_68', 'dext_distance_68', 'dext_complete_68', 'dext_time_68', 'dext_moves_68', 'dext_startx_69', 'dext_starty_69', 'dext_noise_69', 'dext_targx_69', 'dext_targy_69', 'dext_distance_69', 'dext_complete_69', 'dext_time_69', 'dext_moves_69', 'dext_startx_70', 'dext_starty_70', 'dext_noise_70', 'dext_targx_70', 'dext_targy_70', 'dext_distance_70', 'dext_complete_70', 'dext_time_70', 'dext_moves_70']

i = 0

with open (filepath2) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.append(line[0])
			DataExport.append(line[2])
			DataExport.append(line[3])
			DataExport.append(line[4])
			DataExport.append(line[5])
			DataExport.append(line[6])
			DataExport.append(line[7])
			DataExport.append(line[8])
			DataExport.append(line[9])
			DataExport.append(line[10])
			i = i + 1
		else:
			DataExport.append(line[2])
			DataExport.append(line[3])
			DataExport.append(line[4])
			DataExport.append(line[5])
			DataExport.append(line[6])
			DataExport.append(line[7])
			DataExport.append(line[8])
			DataExport.append(line[9])
			DataExport.append(line[10])

redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

write_csv(DataExport)
		
