import csv #this is needed to interact with csv files
import os #this is needed for using directory paths and manipulating them
import getpass #this is needed to extract username

def write_csv(value):
	with open(filepath3, 'r') as csvfile:
		readCSV = csv.reader(csvfile, delimiter=',')
		for line in readCSV:
			list_to_append.append(line)
		csvfile.close()
	list_to_append.append(value)
	if list_to_append[0] != header_labels:
		list_to_append.insert(0, header_labels)
	with open(filepath3, 'w', newline='\n') as csvfile:
		writeCSV = csv.writer(csvfile, delimiter=',')
		for list in list_to_append:
			writeCSV.writerow(list)
		csvfile.close()

username = getpass.getuser() #extract username
filepath2 = "/Users/" + username + "/Desktop/Data Files/"
filepath3 = "/Users/" + username + "/Desktop/Data Files/Tol_Test_Data.csv"

if not os.path.exists(filepath2):
    os.mkdir(filepath2) #make the above filepath if it doesn't exist

header_labels = ['record_id','redcap_event_name','tol_shortest_moves_1', 'tol_move_taken_1', 'tol_correct_1', 'tol_rt_1', 'tol_shortest_moves_2', 'tol_move_taken_2', 'tol_correct_2', 'tol_rt_2', 'tol_shortest_moves_3', 'tol_move_taken_3', 'tol_correct_3', 'tol_rt_3', 'tol_shortest_moves_4', 'tol_move_taken_4', 'tol_correct_4', 'tol_rt_4', 'tol_shortest_moves_5', 'tol_move_taken_5', 'tol_correct_5', 'tol_rt_5', 'tol_shortest_moves_6', 'tol_move_taken_6', 'tol_correct_6', 'tol_rt_6', 'tol_shortest_moves_7', 'tol_move_taken_7', 'tol_correct_7', 'tol_rt_7', 'tol_shortest_moves_8', 'tol_move_taken_8', 'tol_correct_8', 'tol_rt_8', 'tol_shortest_moves_9', 'tol_move_taken_9', 'tol_correct_9', 'tol_rt_9', 'tol_shortest_moves_10', 'tol_move_taken_10', 'tol_correct_10', 'tol_rt_10', 'tol_shortest_moves_11', 'tol_move_taken_11', 'tol_correct_11', 'tol_rt_11', 'tol_shortest_moves_12', 'tol_move_taken_12', 'tol_correct_12', 'tol_rt_12']

New_Data = []
list_to_append = []
event_name = 'day_2_arm_1'

i = 0

with open('/Users/michaellazar/Desktop/Data Files/tol-summary-simon.csv', 'r') as csvfile:
	readCSV = csv.reader(csvfile, delimiter = ',')
	for line in readCSV:
		if i == 0:
			i = i + 1
		elif i == 1:
			New_Data.append(line[0])
			New_Data.append(line[3])
			New_Data.append(line[11])
			New_Data.append(line[8])
			New_Data.append(line[15])
			i = i + 1
		else:
			New_Data.append(line[3])
			New_Data.append(line[11])
			New_Data.append(line[8])
			New_Data.append(line[15])

New_Data.insert(1, event_name)

write_csv(New_Data)
