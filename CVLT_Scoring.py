import csv #this is needed to interact with csv files
import os #this is needed for using directory paths and manipulating them
import getpass #this is needed to extract username
import io
import itertools

username = getpass.getuser() #extract username
filepath = "/Users/" + username + "/Desktop/CVLTExports/"
filepath2 = "/Users/" + username + "/Desktop/CVLTExports/CVLT_Test_Data.csv"
filepath3 = "/Users/" + username + "/Desktop/CVLTExports/test_file.csv"

if not os.path.exists(filepath):
    os.mkdir(filepath) #make the above filepath if it doesn't exist

def pause():
	programPause = input("Press the <ENTER> key to continue when file is in the correct place")

def write_csv(value):
	with open(filepath2, 'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for line in readCSV:
			list_to_append.append(line)
		csvfile.close()
	list_to_append.append(value)
	if list_to_append[0] != header_labels:
		list_to_append.insert(0, header_labels)
	with open(filepath2, 'w', newline='\n') as csvfile:
		writeCSV = csv.writer(csvfile, delimiter=',')
		for list in list_to_append:
			writeCSV.writerow(list)
		csvfile.close()


header_labels = ['record_id','redcap_event_name', 'cvlt_completed', 'cvlt_examiner', 'cvlt_fr_1_raw', 'cvlt_fr_1_std', 'cvlt_fr_1_sc_raw', 'cvlt_fr_1_sc_std', 'cvlt_fr_1_rd_raw', 'cvlt_fr_1_rd_std', 'cvlt_fr_2_raw', 'cvlt_fr_2_std', 'cvlt_fr_2_sc_raw', 'cvlt_fr_2_sc_std', 'cvlt_fr_2_rd_raw', 'cvlt_fr_2_rd_std', 'cvlt_fr_3_raw', 'cvlt_fr_3_std', 'cvlt_fr_3_sc_raw', 'cvlt_fr_3_sc_std', 'cvlt_fr_3_rd_raw', 'cvlt_fr_3_rd_std','cvlt_fr_4_raw', 'cvlt_fr_4_std', 'cvlt_fr_4_sc_raw', 'cvlt_fr_4_sc_std', 'cvlt_fr_4_rd_raw', 'cvlt_fr_4_rd_std', 'cvlt_fr_5_raw', 'cvlt_fr_5_std', 'cvlt_fr_5_sc_raw', 'cvlt_fr_5_sc_std', 'cvlt_fr_5_rd_raw', 'cvlt_fr_5_rd_std', 'cvlt_frtotal_raw', 'cvlt_frtotal_tscore', 'cvlt_frtotal_sc_raw', 'cvlt_frtotal_sc_std', 'cvlt_frtotal_rd_raw', 'cvlt_frtotal_rd_std','cvlt_listb_raw', 'cvlt_listb_std', 'cvlt_listb_sc_raw', 'cvlt_listb_sc_std', 'cvlt_listb_rd_raw', 'cvlt_listb_rd_std', 'cvlt_sdfr_raw', 'cvlt_sdfr_std', 'cvlt_sdfr_sc_raw', 'cvlt_sdfr_sc_std', 'cvlt_sdfr_rd_raw', 'cvlt_sdfr_rd_std','cvlt_sdcr_raw', 'cvlt_sdcr_std', 'cvlt_sdcr_sc_raw', 'cvlt_sdcr_sc_std', 'cvlt_sdcr_rd_raw', 'cvlt_sdcr_rd_std','cvlt_ldfr_raw', 'cvlt_ldfr_std', 'cvlt_ldfr_sc_raw', 'cvlt_ldfr_sc_std', 'cvlt_ldfr_rd_raw', 'cvlt_ldfr_rd_std', 'cvlt_ldcr_raw', 'cvlt_ldcr_std', 'cvlt_ldcr_sc_raw', 'cvlt_ldcr_sc_std', 'cvlt_ldcr_rd_raw', 'cvlt_ldcr_rd_std',
'cvlt_lc_sc_raw', 'cvlt_lc_sc_std', 'cvlt_lc_scf_raw', 'cvlt_lc_scf_std', 'cvlt_lc_scb_raw', 'cvlt_lc_scb_std', 'cvlt_lc_subjcb_raw','cvlt_lc_subjcb_std', 'cvlt_lc_rfp_raw', 'cvlt_lc_rfp_std', 'cvlt_lc_rfm_raw', 'cvlt_lc_rfm_std', 'cvlt_lc_rfr_raw', 'cvlt_lc_rfr_std', 'cvlt_lc_tls_1_5_raw', 'cvlt_lc_tls_1_5_std', 'cvlt_lc_tls_1_2_raw', 'cvlt_lc_tls_1_2_std', 'cvlt_lc_tls_2_5_raw', 'cvlt_lc_tls_2_5_std', 'cvlt_lc_atrc_raw', 'cvlt_lc_atrc_std', 'cvlt_rcm_pi_pc', 'cvlt_rcm_pi_zscore', 'cvlt_rcm_sdri_pc', 'cvlt_rcm_sdri_zscore', 'cvlt_rcm_ldr_trial5_pc', 'cvlt_rcm_ldr_trial5_zscore', 'cvlt_rcm_ldr_sdfr_pc', 'cvlt_rcm_ldr_sdfr_zscore', 'cvlt_re_tr_raw',
'cvlt_re_tr_std', 'cvlt_re_ti_raw', 'cvlt_re_ti_std', 'cvlt_re_tiri_raw', 'cvlt_re_tiri_std', 'cvlt_re_tdri_raw', 'cvlt_re_tdri_std', 'cvlt_re_tfri_raw', 'cvlt_re_tfri_std', 'cvlt_re_tcri_raw', 'cvlt_re_tcri_std', 'cvlt_re_tnci_raw', 'cvlt_re_tnci_per_with', 'cvlt_re_tnci_cum_bet', 'cvlt_re_tsi_raw', 'cvlt_re_tsi_per_with', 'cvlt_re_tsi_cum_bet', 'cvlt_re_tali_raw',
'cvlt_re_tali_per_with', 'cvlt_re_tali_cum_bet', 'cvlt_re_trd_raw', 'cvlt_re_trd_std', 'cvlt_re_ird_raw', 'cvlt_re_ird_std', 'cvlt_re_drd_raw', 'cvlt_re_drd_std', 'cvlt_re_frd_raw', 'cvlt_re_frd_std', 'cvlt_re_cr_raw', 'cvlt_re_cr_std', 'cvlt_drt_th_raw', 'cvlt_drt_th_std', 'cvlt_drt_rtfp_raw', 'cvlt_drt_rtfp_std',
'cvlt_drt_rtrd_raw', 'cvlt_drt_rtrd_std', 'cvlt_drt_srd_raw', 'cvlt_drt_srd_std', 'cvlt_drt_srdis_raw', 'cvlt_drt_srdis_std', 'cvlt_drt_nrd_raw', 'cvlt_drt_nrd_std', 'cvlt_drt_rtrb_raw', 'cvlt_drt_rtrb_std', 'cvlt_drt_fcr_tot_acc_raw', 'cvlt_drt_fcr_tot_acc_per_with', 'cvlt_drt_fcr_tot_acc_cum_bet', 'cvlt_drt_fcr_con_acc_raw', 'cvlt_drt_fcr_con_acc_per_with',
'cvlt_drt_fcr_con_acc_cum_bet', 'cvlt_drt_frc_abs_acc_raw', 'cvlt_drt_frc_abs_acc_per_with', 'cvlt_drt_frc_abs_acc_cum_bet', 'cvlt_rcm_trd_ldfr_pc', 'cvlt_rcm_trd_ldfr_zscore', 'cvlt_rcm_trd_ldfrd_pc', 'cvlt_rcm_trd_ldfrd_zscore', 'cvlt_ciwc_recall_1_raw', 'cvlt_ciwc_recall_1_per_with', 'cvlt_ciwc_recall_1_cum_bet', 'cvlt_ciwc_hit_yn_raw', 'cvlt_ciwc_hit_yn_per_with', 'cvlt_ciwc_hit_yn_cum_bet']
data_line = [6, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 45, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 68, 70, 72, 73, 82, 83, 84, 85, 86, 87, 90, 91, 92,
95, 96, 97, 98, 99, 108, 109, 111, 113, 114, 115, 116, 110, 112, 120, 121, 126, 127]
raw_data = []
wanted_data = []
data_organized = []
list_to_append = []
cvlt_examiner = [input('Name of examiner:	')] 
redcap_event_name = 'day_2_arm_1'

while True:
	try: 
		with open(filepath3, 'r') as csvfile:
			CSVreader = csv.reader(csvfile, delimiter=' ')
			for row in CSVreader:
				if row:
					str1 = ' '.join(str(e) for e in row)
					str1 = str1.split(' ')
					str1 = list(filter(None, str1))
					raw_data.append(str1)
	except IOError:
		pause()
		continue
	else:
		break


for values in data_line:
	if values == 29 or values == 30 or values == 31 or values == 32 or values == 33 or values == 35:
		wanted_data.append(raw_data[values][2:8])
	elif values == 6:
		wanted_data.append(['1'])
		wanted_data.insert(1, [redcap_event_name])

		with open(filepath2, 'a', newline='\n') as csvfile:
			writeCSV = csv.writer(csvfile, delimiter=',')
		with open(filepath2, 'r', newline='') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for line in readCSV:
				if str(wanted_data[0][0]) in line:
					print('Participant data has all ready been inputted. Do you want to continue?')
					answer = input('y/n:	')
					if answer == 'n':
						quit()
					else:
						csvfile.close()
						break
		complete_file = False
		while complete_file == False:
							cvlt_completed = input('Is CVLT complete? (y/n)	')
							if cvlt_completed == 'y' or cvlt_completed == 'Y':
								cvlt_completed = '1'
								wanted_data.insert(2,[cvlt_completed])
								complete_file = True
							elif cvlt_completed == 'n' or cvlt_completed == 'N':
								cvlt_completed = '0'
								wanted_data.insert(2,[cvlt_completed])
								complete_file = True
							else:
								complete_file == False
		wanted_data.insert(3, cvlt_examiner)
	elif values == 34:
		wanted_data.append(raw_data[values][3:5])
		wanted_data.append(raw_data[values][6:10])
	elif values == 42 or values == 43 or values == 44 or values == 45:
		wanted_data.append(raw_data[values][4:10])
	elif values == 30:
		wanted_data.append(raw_data[values])
	elif values == 53 or values == 57 or values == 58 or values == 59 or values == 61 or values == 62:
		wanted_data.append(raw_data[values][4:6])
	elif values == 60 or values == 54 or values == 55 or values == 56 or values == 68 or values == 82:
		wanted_data.append(raw_data[values][5:7])
	elif values == 63 or values == 109:
		wanted_data.append(raw_data[values][3:5])
	elif values == 70 or values == 72 or values == 83:
		wanted_data.append(raw_data[values][7:9])
	elif values == 73 or values == 85 or values == 86 or values == 121 or values == 111:
		wanted_data.append(raw_data[values][9:11])
	elif values == 84 or values == 120:
		wanted_data.append(raw_data[values][8:10])
	elif values == 87:
		wanted_data.append(raw_data[values][6:8])
	elif values == 90 or values == 91:
		wanted_data.append(raw_data[values][6:9])
	elif values == 92:
		wanted_data.append(raw_data[values][9:12])
	elif values == 95 or values == 97 or values == 99:
		wanted_data.append(raw_data[values][10:12])
	elif values == 96 or values == 113:
		wanted_data.append(raw_data[values][11:13])
	elif values == 115 or values == 98:
		wanted_data.append(raw_data[values][13:15])
	elif values == 110 or values == 112:
		wanted_data.append(raw_data[values][5:8])
	elif values == 114:
		wanted_data.append(raw_data[values][15:17])
	elif values == 116:
		wanted_data.append(raw_data[values][22:24])
	elif values == 126:
		wanted_data.append(raw_data[values][14:17])
	elif values == 127:
		wanted_data.append(raw_data[values][16:19])
	elif values == 108:
		wanted_data.append(raw_data[values][2:4])

wanted_data.insert(49, raw_data[108][9:12])


for sublist in wanted_data:
    for item in sublist:
    	if item == '---':
    		item = item.replace('---', '')
    	data_organized.append(item)


# Use above line of code if using a blank csv file to have headers be inserted into the csv file

write_csv(data_organized)