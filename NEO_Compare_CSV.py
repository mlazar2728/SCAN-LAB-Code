import pandas as pd
import numpy as np

def report_diff(x):
	if x[0] == x[1]:
		return x[0] 
	else:
		return '{} ---> {}'.format(*x)

def has_change(row):
	if '--->' in row.to_string():
		return "Y"
	else:
		return "N"

Neo1 = pd.read_csv("/Users/mplazar/Desktop/NEOExports/NEO_Test_Data.csv")
Neo2 = pd.read_csv("/Users/mplazar/Desktop/NEOExports/NEO_Test_Data_2.csv")

diff_panel = pd.Panel(dict(Neo1=Neo1, Neo2=Neo2))

diff_output = diff_panel.apply(report_diff, axis=0)

diff_output['has_change'] = diff_output.apply(has_change, axis=1)

diff_output[(diff_output.has_change == 'Y')].to_csv('/Users/mplazar/Desktop/Neo_Dif.csv', index=False, columns=['record_id', 'redcap_event_name neo_pi_3_n1_tscore', 'neo_pi_3_n2_tscore', 'neo_pi_3_n3_tscore', 'neo_pi_3_n4_tscore', 'neo_pi_3_n5_tscore', 'neo_pi_3_n6_tscore', 'neo_pi_3_e1_tscore', 'neo_pi_3_e2_tscore', 'neo_pi_3_e3_tscore', 'neo_pi_3_e4_tscore', 'neo_pi_3_e5_tscore', 'neo_pi_3_e6_tscore', 'neo_pi_3_o1_tscore', 'neo_pi_3_o2_tscore', 'neo_pi_3_o3_tscore', 'neo_pi_3_o4_tscore', 'neo_pi_3_o5_tscore', 'neo_pi_3_o6_tscore', 'neo_pi_3_a1_tscore', 'neo_pi_3_a2_tscore', 'neo_pi_3_a3_tscore', 'neo_pi_3_a4_tscore', 'neo_pi_3_a5_tscore', 'neo_pi_3_a6_tscore', 'neo_pi_3_c1_tscore', 'neo_pi_3_c2_tscore', 'neo_pi_3_c3_tscore', 'neo_pi_3_c4_tscore', 'neo_pi_3_c5_tscore', 'neo_pi_3_c6_tscore', 'neo_pi_3_n_tscore', 'neo_pi_3_e_tscore', 'neo_pi_3_o_tscore', 'neo_pi_3_a_tscore', 'neo_pi_3_c_tscore'])

