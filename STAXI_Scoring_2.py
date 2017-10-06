# This program will take raw scores from STAXI-2 and write raw scores and t-scores in an excel file
import csv #this is needed to interact with csv files
import os #this is needed for using directory paths and manipulating them
import getpass #this is needed to extract username

def get_accepted_value(value):
	if int(value) < 0 or int(value) > 4:
		print('Only values between 1-4 are accepted. You attempted to input '+str(value))
		quit()

def find_t_value(name, value, gender, age, filepath):
	if Age == 19:
		with open(filepath2+name+'_16_19.csv', 'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if row[0] == str(value):
					if Gender == 'Male' or Gender == 'male' or Gender == 'm' or Gender == 'M':
						T_Scores.append(row[1])
					elif Gender == 'Female' or Gender == 'female' or Gender == 'F' or Gender == 'f':
						T_Scores.append(row[2])
	elif Age > 19 and Age < 30:
		with open(filepath2+name+'_20_29.csv', 'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if row[0] == str(value):
					if Gender == 'Male' or Gender == 'male' or Gender == 'm' or Gender == 'M':
						T_Scores.append(row[1])
					elif Gender == 'Female' or Gender == 'female' or Gender == 'F' or Gender == 'f':
						T_Scores.append(row[2])
	elif Age > 29:
		with open(filepath2+name+'_30.csv', 'r') as csvfile:
			readCSV = csv.reader(csvfile, delimiter=',')
			for row in readCSV:
				if row[0] == str(value):
					if Gender == 'Male' or Gender == 'male' or Gender == 'm' or Gender == 'M':
						T_Scores.append(row[1])
					elif Gender == 'Female' or Gender == 'female' or Gender == 'F' or Gender == 'f':
						T_Scores.append(row[2])


def write_csv(value):
	while True:
		try: 
			with open(filepath4, 'r') as csvfile:
				readCSV = csv.reader(csvfile, delimiter=',')
				for line in readCSV:
					list_to_append.append(line)
				break
		except IOError:
			break
	list_to_append.append(value)
	if list_to_append[0] != header_labels:
		list_to_append.insert(0, header_labels)
	with open(filepath4, 'w', newline='\n') as csvfile:
		writeCSV = csv.writer(csvfile, delimiter=',')
		for list in list_to_append:
			writeCSV.writerow(list)


username = getpass.getuser() #extract username
filepath = "/users/" + username + "/Desktop/staxi_raw.csv"
filepath2 = '/users/' + username+ '/Desktop/python/STAXI_Scoring_Files/'
filepath3 = "/Users/" + username + "/Desktop/STAXIExports/"
filepath4 = "/Users/" + username + "/Desktop/STAXIExports/STAXI_Test_Data.csv"

if not os.path.exists(filepath3):
    os.mkdir(filepath3) #make the above filepath if it doesn't exist

correct_age = False
correct_gender = False
print ('Welcome to STAXI-2 scoring program')
while correct_gender == False:
	Gender = input('Is the participant male or female:		')
	if Gender == 'M' or Gender == 'F' or Gender == 'm' or Gender == 'f' or Gender == 'Male' or Gender == 'Female' or Gender == 'male' or Gender == 'female':
		correct_gender = True
	else:
		print('Invalid response. Please input the participants gender.')
		correct_gender = False
		continue

while correct_age == False:
	while True:
		try: 
			Age = int(input('How old is the participant:	'))
		except ValueError:
			print('Sorry, that was an invalid response. Please input a number.')
			continue
		else:
			break
	if Age < 19 or Age > 30:
		print('The participant is to old or too young for the study.')
		correct_age = False
		continue
	else:
		correct_age = True

Raw_scores = []
T_Scores = []
Total_Scores = []
list_to_append = []
x = float('nan')

header_labels = []
header_labels_original = []
header_labels_to_add = ['staxi_s_ang_tscore', 'staxi_s_ang_f_tscore', 'staxi_s_ang_v_tscore', 'staxi_s_ang_p_tscore', 'staxi_t_ang_tscore', 'staxi_t_ang_t_tscore', 'staxi_t_ang_r_tscore', 'staxi_ax_o_tscore', 'staxi_ax_i_tscore', 'staxi_ac_o_tscore', 'staxi_ac_i_tscore', 'staxi_ax_index_tscore']
Score_Categories = ['S_Ang', 'S_Ang_F', 'S_Ang_V', 'S_Ang_P', 'T_Ang', 'T_Ang_T', 'T_Ang_R', 'AX_O', 'AX_I', 'AC_O', 'AC_I', 'AX_Index']

z = 0
t = 0
with open(filepath, 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for line in readCSV:
		if z == 0:
			header_labels_original.append(line)
			z = z + 1
		elif z == 1:
			for value in line:
				if t == 0:
					t = t + 1
				elif t == 1:
					t = t + 1
				elif t > 1 and t < 59:
					get_accepted_value(value)
					t = t + 1
			Raw_scores.append(line)
			

for i in range(len(Score_Categories)):
	find_t_value(Score_Categories[i], Raw_scores[0][i+59], Raw_scores[0][2], Raw_scores[0][3], filepath2)


Total_Scores = Raw_scores[0] + T_Scores
header_labels = header_labels_original[0] + header_labels_to_add

write_csv(Total_Scores)



