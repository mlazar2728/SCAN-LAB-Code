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
filepath = "/Users/" + username + "/Desktop/PEBLExports/BART/bart_"+participant_id+".csv"
filepath2 = "/Users/" + username + "/Desktop/PEBLData/bart_data.csv"
filepath3 = "/Users/" + username + "/Desktop/PEBLData"

if not os.path.exists(filepath3):
    os.mkdir(filepath3) #make the above filepath if it doesn't exist

DataExport = []
list_to_append = []

Header = ['record_id','redcap_event_name', 'bart_type_1', 'bart_life_1', 'bart_pumps_1', 'bart_collected_1', 'bart_time_1', 'bart_type_2', 'bart_life_2', 'bart_pumps_2', 'bart_collected_2', 'bart_time_2', 'bart_type_3', 'bart_life_3', 'bart_pumps_3', 'bart_collected_3', 'bart_time_3', 'bart_type_4', 'bart_life_4', 'bart_pumps_4', 'bart_collected_4', 'bart_time_4', 'bart_type_5', 'bart_life_5', 'bart_pumps_5', 'bart_collected_5', 'bart_time_5', 'bart_type_6', 'bart_life_6', 'bart_pumps_6', 'bart_collected_6', 'bart_time_6', 'bart_type_7', 'bart_life_7', 'bart_pumps_7', 'bart_collected_7', 'bart_time_7', 'bart_type_8', 'bart_life_8', 'bart_pumps_8', 'bart_collected_8', 'bart_time_8', 'bart_type_9', 'bart_life_9', 'bart_pumps_9', 'bart_collected_9', 'bart_time_9', 'bart_type_10', 'bart_life_10', 'bart_pumps_10', 'bart_collected_10', 'bart_time_10', 'bart_type_11', 'bart_life_11', 'bart_pumps_11', 'bart_collected_11', 'bart_time_11', 'bart_type_12', 'bart_life_12', 'bart_pumps_12', 'bart_collected_12', 'bart_time_12', 'bart_type_13', 'bart_life_13', 'bart_pumps_13', 'bart_collected_13', 'bart_time_13', 'bart_type_14', 'bart_life_14', 'bart_pumps_14', 'bart_collected_14', 'bart_time_14', 'bart_type_15', 'bart_life_15', 'bart_pumps_15', 'bart_collected_15', 'bart_time_15', 'bart_type_16', 'bart_life_16', 'bart_pumps_16', 'bart_collected_16', 'bart_time_16', 'bart_type_17', 'bart_life_17', 'bart_pumps_17', 'bart_collected_17', 'bart_time_17', 'bart_type_18', 'bart_life_18', 'bart_pumps_18', 'bart_collected_18', 'bart_time_18', 'bart_type_19', 'bart_life_19', 'bart_pumps_19', 'bart_collected_19', 'bart_time_19', 'bart_type_20', 'bart_life_20', 'bart_pumps_20', 'bart_collected_20', 'bart_time_20', 'bart_type_21', 'bart_life_21', 'bart_pumps_21', 'bart_collected_21', 'bart_time_21', 'bart_type_22', 'bart_life_22', 'bart_pumps_22', 'bart_collected_22', 'bart_time_22', 'bart_type_23', 'bart_life_23', 'bart_pumps_23', 'bart_collected_23', 'bart_time_23', 'bart_type_24', 'bart_life_24', 'bart_pumps_24', 'bart_collected_24', 'bart_time_24', 'bart_type_25', 'bart_life_25', 'bart_pumps_25', 'bart_collected_25', 'bart_time_25', 'bart_type_26', 'bart_life_26', 'bart_pumps_26', 'bart_collected_26', 'bart_time_26', 'bart_type_27', 'bart_life_27', 'bart_pumps_27', 'bart_collected_27', 'bart_time_27', 'bart_type_28', 'bart_life_28', 'bart_pumps_28', 'bart_collected_28', 'bart_time_28', 'bart_type_29', 'bart_life_29', 'bart_pumps_29', 'bart_collected_29', 'bart_time_29', 'bart_type_30', 'bart_life_30', 'bart_pumps_30', 'bart_collected_30', 'bart_time_30', 'bart_type_31', 'bart_life_31', 'bart_pumps_31', 'bart_collected_31', 'bart_time_31', 'bart_type_32', 'bart_life_32', 'bart_pumps_32', 'bart_collected_32', 'bart_time_32', 'bart_type_33', 'bart_life_33', 'bart_pumps_33', 'bart_collected_33', 'bart_time_33', 'bart_type_34', 'bart_life_34', 'bart_pumps_34', 'bart_collected_34', 'bart_time_34', 'bart_type_35', 'bart_life_35', 'bart_pumps_35', 'bart_collected_35', 'bart_time_35', 'bart_type_36', 'bart_life_36', 'bart_pumps_36', 'bart_collected_36', 'bart_time_36', 'bart_type_37', 'bart_life_37', 'bart_pumps_37', 'bart_collected_37', 'bart_time_37', 'bart_type_38', 'bart_life_38', 'bart_pumps_38', 'bart_collected_38', 'bart_time_38', 'bart_type_39', 'bart_life_39', 'bart_pumps_39', 'bart_collected_39', 'bart_time_39', 'bart_type_40', 'bart_life_40', 'bart_pumps_40', 'bart_collected_40', 'bart_time_40', 'bart_type_41', 'bart_life_41', 'bart_pumps_41', 'bart_collected_41', 'bart_time_41', 'bart_type_42', 'bart_life_42', 'bart_pumps_42', 'bart_collected_42', 'bart_time_42', 'bart_type_43', 'bart_life_43', 'bart_pumps_43', 'bart_collected_43', 'bart_time_43', 'bart_type_44', 'bart_life_44', 'bart_pumps_44', 'bart_collected_44', 'bart_time_44', 'bart_type_45', 'bart_life_45', 'bart_pumps_45', 'bart_collected_45', 'bart_time_45', 'bart_type_46', 'bart_life_46', 'bart_pumps_46', 'bart_collected_46', 'bart_time_46', 'bart_type_47', 'bart_life_47', 'bart_pumps_47', 'bart_collected_47', 'bart_time_47', 'bart_type_48', 'bart_life_48', 'bart_pumps_48', 'bart_collected_48', 'bart_time_48', 'bart_type_49', 'bart_life_49', 'bart_pumps_49', 'bart_collected_49', 'bart_time_49', 'bart_type_50', 'bart_life_50', 'bart_pumps_50', 'bart_collected_50', 'bart_time_50', 'bart_type_51', 'bart_life_51', 'bart_pumps_51', 'bart_collected_51', 'bart_time_51', 'bart_type_52', 'bart_life_52', 'bart_pumps_52', 'bart_collected_52', 'bart_time_52', 'bart_type_53', 'bart_life_53', 'bart_pumps_53', 'bart_collected_53', 'bart_time_53', 'bart_type_54', 'bart_life_54', 'bart_pumps_54', 'bart_collected_54', 'bart_time_54', 'bart_type_55', 'bart_life_55', 'bart_pumps_55', 'bart_collected_55', 'bart_time_55', 'bart_type_56', 'bart_life_56', 'bart_pumps_56', 'bart_collected_56', 'bart_time_56', 'bart_type_57', 'bart_life_57', 'bart_pumps_57', 'bart_collected_57', 'bart_time_57', 'bart_type_58', 'bart_life_58', 'bart_pumps_58', 'bart_collected_58', 'bart_time_58', 'bart_type_59', 'bart_life_59', 'bart_pumps_59', 'bart_collected_59', 'bart_time_59', 'bart_type_60', 'bart_life_60', 'bart_pumps_60', 'bart_collected_60', 'bart_time_60', 'bart_type_61', 'bart_life_61', 'bart_pumps_61', 'bart_collected_61', 'bart_time_61', 'bart_type_62', 'bart_life_62', 'bart_pumps_62', 'bart_collected_62', 'bart_time_62', 'bart_type_63', 'bart_life_63', 'bart_pumps_63', 'bart_collected_63', 'bart_time_63', 'bart_type_64', 'bart_life_64', 'bart_pumps_64', 'bart_collected_64', 'bart_time_64', 'bart_type_65', 'bart_life_65', 'bart_pumps_65', 'bart_collected_65', 'bart_time_65', 'bart_type_66', 'bart_life_66', 'bart_pumps_66', 'bart_collected_66', 'bart_time_66', 'bart_type_67', 'bart_life_67', 'bart_pumps_67', 'bart_collected_67', 'bart_time_67', 'bart_type_68', 'bart_life_68', 'bart_pumps_68', 'bart_collected_68', 'bart_time_68', 'bart_type_69', 'bart_life_69', 'bart_pumps_69', 'bart_collected_69', 'bart_time_69', 'bart_type_70', 'bart_life_70', 'bart_pumps_70', 'bart_collected_70', 'bart_time_70', 'bart_type_71', 'bart_life_71', 'bart_pumps_71', 'bart_collected_71', 'bart_time_71', 'bart_type_72', 'bart_life_72', 'bart_pumps_72', 'bart_collected_72', 'bart_time_72', 'bart_type_73', 'bart_life_73', 'bart_pumps_73', 'bart_collected_73', 'bart_time_73', 'bart_type_74', 'bart_life_74', 'bart_pumps_74', 'bart_collected_74', 'bart_time_74', 'bart_type_75', 'bart_life_75', 'bart_pumps_75', 'bart_collected_75', 'bart_time_75', 'bart_type_76', 'bart_life_76', 'bart_pumps_76', 'bart_collected_76', 'bart_time_76', 'bart_type_77', 'bart_life_77', 'bart_pumps_77', 'bart_collected_77', 'bart_time_77', 'bart_type_78', 'bart_life_78', 'bart_pumps_78', 'bart_collected_78', 'bart_time_78', 'bart_type_79', 'bart_life_79', 'bart_pumps_79', 'bart_collected_79', 'bart_time_79', 'bart_type_80', 'bart_life_80', 'bart_pumps_80', 'bart_collected_80', 'bart_time_80', 'bart_type_81', 'bart_life_81', 'bart_pumps_81', 'bart_collected_81', 'bart_time_81', 'bart_type_82', 'bart_life_82', 'bart_pumps_82', 'bart_collected_82', 'bart_time_82', 'bart_type_83', 'bart_life_83', 'bart_pumps_83', 'bart_collected_83', 'bart_time_83', 'bart_type_84', 'bart_life_84', 'bart_pumps_84', 'bart_collected_84', 'bart_time_84', 'bart_type_85', 'bart_life_85', 'bart_pumps_85', 'bart_collected_85', 'bart_time_85', 'bart_type_86', 'bart_life_86', 'bart_pumps_86', 'bart_collected_86', 'bart_time_86', 'bart_type_87', 'bart_life_87', 'bart_pumps_87', 'bart_collected_87', 'bart_time_87', 'bart_type_88', 'bart_life_88', 'bart_pumps_88', 'bart_collected_88', 'bart_time_88', 'bart_type_89', 'bart_life_89', 'bart_pumps_89', 'bart_collected_89', 'bart_time_89', 'bart_type_90', 'bart_life_90', 'bart_pumps_90', 'bart_collected_90', 'bart_time_90']

i = 0
with open (filepath) as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			DataExport.append(line[0])
			DataExport.append(line[2])
			DataExport.append(line[3])
			DataExport.append(line[4])
			DataExport.append(line[6])
			DataExport.append(line[8])
			i = i + 1
		else:
			DataExport.append(line[2])
			DataExport.append(line[3])
			DataExport.append(line[4])
			DataExport.append(line[6])
			DataExport.append(line[8])

redcap_event_name = 'day_2_arm_1'
DataExport.insert(1, redcap_event_name)

write_csv(DataExport)
