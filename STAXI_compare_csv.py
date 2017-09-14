import pandas as pd
import numpy as np

def report_diff(x):
	if x[0] == x[1]:
		return x[0] 
	else:
		return '{} ---> {}'.format(*x)

def has_change(row):
	# if '\033[1m + {} ---> {}' in row.to_string():
	if '--->' in row.to_string():
		return "Y"
	else:
		return "N"

staxi1 = pd.read_csv("STAXIExports/STAXI_Test_Data.csv")
staxi2 = pd.read_csv("STAXIExports/STAXI_Test_Data_2.csv")

diff_panel = pd.Panel(dict(staxi1=staxi1, staxi2=staxi2))

diff_output = diff_panel.apply(report_diff, axis=0)

diff_output['has_change'] = diff_output.apply(has_change, axis=1)

diff_output[(diff_output.has_change == 'Y')].to_csv('/Users/mplazar/Desktop/Staxi_Dif.csv', index=False, columns=['record_id', 'redcap_event_name', 'staxi_s_ang_tscore', 'staxi_s_ang_f_tscore',	'staxi_s_ang_v_tscore',	'staxi_s_ang_p_tscore',	'staxi_t_ang_tscore',	'staxi_t_ang_t_tscore',	'staxi_t_ang_r_tscore',	'staxi_ax_index_tscore', 'staxi_ax_o_tscore', 'staxi_ax_i_tscore', 'staxi_ac_o_tscore', 'staxi_ac_i_tscore'])

