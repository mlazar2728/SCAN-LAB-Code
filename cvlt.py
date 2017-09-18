import csv #this is needed to interact with csv files
import os #this is needed for using directory paths and manipulating them
import getpass #this is needed to extract username
import io
import itertools

username = getpass.getuser() #extract username
filepath = "/Users/" + username + "/Desktop/CVLTExports/"
filepath2 = "/Users/" + username + "/Desktop/CVLTExports/CVLT_Test_Data.csv"

if not os.path.exists(filepath):
    os.mkdir(filepath) #make the above filepath if it doesn't exist


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



header_labels = ['Participant ID', 'IR Trial 1 Raw', 'IR Trail 1 SS', 'IR Trial 1 SC Raw', 'IR Trial 1 SC SS', 'IR Trial 1 RD Raw', 'IR Trial 1 RD SS', 'IR Trial 2 Raw', 'IR Trail 2 SS', 'IR Trial 2 SC Raw', 'IR Trial 2 SC SS', 'IR Trial 2 RD Raw', 'IR Trial 2 RD SS', 'IR Trial 3 Raw', 'IR Trail 3 SS', 'IR Trial 3 SC Raw', 'IR Trial 3 SC SS', 'IR Trial 3 RD Raw', 'IR Trial 3 RD SS','IR Trial 4 Raw', 'IR Trail 4 SS', 'IR Trial 4 SC Raw', 'IR Trial 4 SC SS', 'IR Trial 4 RD Raw', 'IR Trial 4 RD SS', 'IR Trial 5 Raw', 'IR Trial 5 SS', 'IR Trial 5 SC Raw', 'IR Trial 5 SC SS', 'IR Trial 5 RD Raw', 'IR Trial 5 RD SS', 'Total Trials 1-5 Raw', 'Totals Trials 1-5 T-score', 'Trials 1-5 SC Raw', 'Trials 1-5 SC SS', 'Trials 1-5 RD Raw', 'Trials 1-5 RD SS','IR Trial B Raw', 'IR Trail B SS', 'IR Trial B SC Raw', 'IR Trial B SC SS', 'IR Trial B RD Raw', 'IR Trial B RD SS', 'SD FR Raw', 'SD FR SS', 'SD FR SC Raw', 'SD FR SC SS', 'SD FR RD Raw', 'SD FR RD SS','SD CR Raw', 'SD CR SS', 'SD CR SC Raw', 'SD CR SC SS', 'SD CR RD Raw', 'SD CR RD SS','LD FR Raw', 'LD FR SS', 'LD FR SC Raw', 'LD FR SC SS', 'LD FR RD Raw', 'LD FR RD SS', 'LD CR Raw', 'LD CR SS', 'LD CR SC Raw', 'LD CR SD SS', 'LD CR RD Raw', 'LD CR RD SS',
'LC Semantic Clustering Raw', 'LC Semantic Clustering SS', 'LC Serial Clustering Forward Raw', 'LC Serial Clustering Forward SS', 'LC Serial Clustering Bidiretional Raw', 'LC Serial Clustering Bidirectional SS', 'LC Subjective Clustering Bidirectional Raw','LC Subjective Clustering Bidirectional SS', 'LC % Recall from Primacy Raw', 'LC % Recall from Primacy SS', 'LC % Recall from Middle Raw', 'LC % Recall from Middle SS', 'LC % Recall from Recency Raw', 'LC % Recall from Recency SS', 'LC Total Learning Slope Trials 1-5 Raw', 'LC Total Learning Slope Tirals 1-5 SS', 'LC Learning Slope Trials 1-2 Raw', 'LC Learning Slope Trials 1-2 SS', 'LC Learning Slope Trials 2-5 Raw', 'LC Learning Slope Trials 2-5 SS', 'LC Across-Trial Recall Consistency Raw', 'LC Across-Trial Recall Consistency SS', 'RCM Proactive Interference List B vs. Trial 1 Percent Change', 'RCM Proactive Interference List B vs. Trial 1 Z-Score Difference', 'RCM Short-Delay Retention/Retroactive Interference Short Delay Free Recall vs. Trial 5 Percent Change', 'RCM Short-Delay Retention/Retroactive Interference Short Delay Free Recall vs. Trial 5 Z-Score Difference', 'RCM Long-Delay Retention Long Delay Free Recall vs. Trial 5 Percent Change', 'RCM Long-Delay Retention Long Delay Free Recall vs. Trial 5 Z-Score Difference', 'RCM Long-Delay Retention Long Delay Free Recall vs. Short Delay Free Recall Percent Change', 'RCM Long-Delay Retention Long Delay Free Recall vs. Short Delay Free Recall Z-score Difference', 'RE Total Repetitions (All Recall Trials) Raw',
'RE Total Repetitions (All Recall Trials) SS', 'RE Total Intrusions (All Recall Trials, All Types) Raw', 'RE Total Intrusions (All Recall Trials, All Types) SS', 'RE Total Imediate Recall Intrusions (Trials 1-5, All Types) Raw', 'RE Total Imediate Recall Intrusions (Trials 1-5, All Types) SS', 'RE Total Delayed Recall Intrusions (Free & Cued All Types) Raw', 'RE Total Delayed Recall Intrusions (Free & Cued All Types) SS', 'RE Total Free Recall Intrusions (Immed. & Delayed, All Types) Raw', 'RE Total Free Recall Intrusions (Immed. & Delayed, All Types) SS', 'RE Total Cued Recall Intrusions (All Types) Raw', 'RE Total Cued Recall Intrusions (All Types) SS', 'RE Total Non-Category Intrusions (All Recall Trials) Raw', 'RE Total Non-Category Intrusions (All Recall Trials) % with this score', 'RE Total Non-Category Intrusions (All Recall Trials) Cum. % w/better score', 'RE Total Synonym/Subordinate Intrusions (All Recall Trials) Raw', 'RE Total Synonym/Subordinate Intrusions (All Recall Trials) % with this score', 'RE Total Synonym/Subordinate Intrusions (All Recall Trials) Cum. % w/better score', 'RE Total Across-List Intrusions (List B & Delayed Recall Trials) Raw',
'RE Total Across-List Intrusions (List B & Delayed Recall Trials) % with this score', 'RE Total Across-List Intrusions (List B & Delayed Recall Trials) Cum. % w/better score', 'RE Total Recall Discriminability (List A, All Trials vs. Total Intrusions) Raw', 'RE Total Recall Discriminability (List A, All Trials vs. Total Intrusions) SS', 'RE Immediate Recall Discriminability (List A, Trials 1-5 vs. Intrusions, Trials 1-5) Raw', 'RE Immediate Recall Discriminability (List A, Trials 1-5 vs. Intrusions, Trials 1-5) SS', 'RE Delayed Recall Discriminability (List A vs. Intrusions, Delayed Recall Trials) Raw', 'RE Delayed Recall Discriminability (List A vs. Intrusions, Delayed Recall Trials) SS', 'Free Recall Discriminability (List A vs. Intrusions, Immed. & Delayed Free Recall Trials) Raw', 'Free Recall Discriminability (List A vs. Intrusions, Immed. & Delayed Free Recall Trials) SS', 'RE Cued Recall (List A vs. Intrusions, Cued Recall Trials) Raw', 'RE Cued Recall (List A vs. Intrusions, Cued Recall Trials) SS', 'DRT Yes/No Recognitions Total Hits Raw', 'DRT Yes/No Recognitions Total Hits SS', 'DRT Yes/No Recognitions Total False Positives Raw', 'DRT Yes/No Recognitions Total False Positives SS',
'DRT Yes/No Recognitions Total Recognition Dsicriminability (d) (Hits vs. Total False Positives) Raw', 'DRT Yes/No Recognitions Total Recognition Discriminability (d) (Hits vs. Total False Positives) SS', 'DRT Yes/No Recognitions Source Recognition Discriminability (d) (Hits vs. List B False Positives [5]) Raw', 'DRT Yes/No Recognitions Source Recognition Discriminability (d) (Hits vs. List B False Positives [5]) SS', 'DRT Yes/No Recognitions Semantic Recognition Discriminability (List A vs. List B Shared [8] & Prototypical [8] False Positives) Raw', 'DRT Yes/No Recognitions Semantic Recognition Discriminability (List A vs. List B Shared [8] & Prototypical [8] False Positives) SS', 'DRT Yes/No Recognitions Novel Recognition Discriminability (Hits vs. Prototypical[8] & Unrelated [8] False Positives) Raw', 'DRT Yes/No Recognitions Novel Recognition Discriminability (Hits vs. Prototypical[8] & Unrelated [8] False Positives) SS', 'DRT Yes/No Recognition Total Response Bias (C) Raw', 'DRT Yes/No Recognition Total Response Bias (C) SS', 'DRT Forced Choice Recognition % Total Accuracy (Hits [8]/16)*100 Raw', 'DRT Forced Choice Recognition % Total Accuracy (Hits [8]/16)*100 % with this score', 'DRT Forced Choice Recognition % Total Accuracy (Hits [8]/16)*100 Cum. % w/better score', 'DRT Forced Choice Recognition % Concrete Accuracy (Hits [4]/8)*100 Raw', ' DRT Forced Choice Recognition % Concrete Accuracy (Hits [4]/8)*100 % with this score',
'DRT Forced Choice Recognition % Concrete Accuracy (Hits [4]/8)*100 Cum % w/better score', 'DRT Forced Choice Recognition % Abstract Accuracy (Hits [4]/8)*100 Raw', 'DRT Forced Choice Recognition % Abstract Accuracy (Hits [4]/8)*100 % with this score', 'DRT Forced Choice Recognition % Abstract Accuracy (Hits [4]/8)*100 Cum. % w/better score', 'RRCM Total Recognition Discriminability vs. Long Delay Free Recall Percent Change', 'RRCM Total Recognition Discriminability vs. Long Delay Free Recall Z-Score Difference', 'RRCM Total Recognition Discriminability vs. Long Delay Free Recall Discriminability Percent Change', 'RRCM Total Recognition Discriminability vs. Long Delay Free Recall Discriminability Z-Score Difference', 'CIWC Number of target words recalled at least once, but missed on Forced Choice Recognition Raw', 'CIWC Number of target words recalled at least once, but missed on Forced Choice Recognition % with this score', 'CIWC Number of target words recalled at least once, but missed on Forced Choice Recognition Cum. % w/better score', 'CIWC Number of target words that were Hits on Yes/No Recognition, but missed on Forced Choice Recognition Raw', 'CIWC Number of target words that were Hits on Yes/No Recognition, but missed on Forced Choice Recognition % with this score', 'CIWC Number of target words that were Hits on Yes/No Recognition, but missed on Forced Choice Recognition Cum. % w/better score']
data_line = [6, 29, 30, 31, 32, 33, 34, 35, 42, 43, 44, 45, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 68, 70, 72, 73, 82, 83, 84, 85, 86, 87, 90, 91, 92,
95, 96, 97, 98, 99, 108, 110, 112, 114, 115, 116, 117, 109, 111, 113, 121, 122, 127, 128]
raw_data = []
wanted_data = []
data_organized = []
list_to_append = []

filepath3 = "/Users/" + username + "/Desktop/CVLTExports/test_file.csv"

with open(filepath3, 'r') as csvfile:
	CSVreader = csv.reader(csvfile, delimiter=' ')
	for line in CSVreader:
		str1 = ' '.join(str(e) for e in line)
		str1 = str1.split(' ')
		str1 = list(filter(None, str1))
		raw_data.append(str1)

for values in data_line:
	if values == 29 or values == 30 or values == 31 or values == 32 or values == 33 or values == 35:
		wanted_data.append(raw_data[values][2:8])
	elif values == 6:
		wanted_data.append(raw_data[values][2:3])
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
	elif values == 34:
		wanted_data.append(raw_data[values][3:9])
	elif values == 42 or values == 43 or values == 44 or values == 45:
		wanted_data.append(raw_data[values][4:10])
	elif values == 30:
		wanted_data.append(raw_data[values])
	elif values == 53 or values == 57 or values == 58 or values == 59 or values == 61 or values == 62:
		wanted_data.append(raw_data[values][4:6])
	elif values == 60 or values == 54 or values == 55 or values == 56 or values == 68 or values == 82:
		wanted_data.append(raw_data[values][5:7])
	elif values == 63 or values == 110:
		wanted_data.append(raw_data[values][3:5])
	elif values == 70 or values == 72 or values == 83:
		wanted_data.append(raw_data[values][7:9])
	elif values == 73 or values == 85 or values == 86 or values == 122 or values == 112:
		wanted_data.append(raw_data[values][9:11])
	elif values == 84 or values == 121:
		wanted_data.append(raw_data[values][8:10])
	elif values == 87:
		wanted_data.append(raw_data[values][6:8])
	elif values == 90 or values == 91:
		wanted_data.append(raw_data[values][6:9])
	elif values == 92:
		wanted_data.append(raw_data[values][9:12])
	elif values == 95 or values == 97 or values == 99:
		wanted_data.append(raw_data[values][10:12])
	elif values == 96 or values == 114:
		wanted_data.append(raw_data[values][11:13])
	elif values == 116 or values == 98:
		wanted_data.append(raw_data[values][13:15])
	elif values == 109 or values == 111 or values == 113:
		wanted_data.append(raw_data[values][5:8])
	elif values == 115:
		wanted_data.append(raw_data[values][15:17])
	elif values == 117:
		wanted_data.append(raw_data[values][22:24])
	elif values == 127:
		wanted_data.append(raw_data[values][14:17])
	elif values == 128:
		wanted_data.append(raw_data[values][16:19])
	elif values == 108:
		wanted_data.append(raw_data[values][2:4])


for sublist in wanted_data:
    for item in sublist:
        data_organized.append(item)


# Use above line of code if using a blank csv file to have headers be inserted into the csv file

write_csv(data_organized)
