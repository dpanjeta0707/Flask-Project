import pandas as pd
from datetime import datetime



def material_append(start_date, end_date, c_lot, l_lot, p_lot, t_formula):
	start_date = start_date
	end_date = end_date
	c_lot= c_lot
	l_lot = l_lot
	p_lot = p_lot
	t_formula = t_formula
	

	s_date=datetime.strptime(start_date, '%Y-%m-%d').date()
	e_date=datetime.strptime(end_date, '%Y-%m-%d').date()


	daterange = pd.date_range(s_date,e_date)
	print(type(daterange))

	final_list=[]
	for x in daterange:
		a=[]
		a.append(x)
		a.append(c_lot)
		a.append(l_lot)
		a.append(p_lot)
		a.append(t_formula)

		final_list.append(a)

	df=pd.DataFrame(final_list)

	df.to_csv('D:\MRP\___website_server\\files\material.csv', mode ='a', sep=',', header = False, index=False)

def temphum_append(file):
	file = file
	this_df=pd.read_csv(file)
	this_df.to_csv('D:\MRP\___website_server\\files\\raw.csv', mode ='a', sep=',', header = False, index=False)

def airin_append(file):
	file = file
	this_df=pd.read_csv(file)
	this_df.to_csv('D:\MRP\___website_server\\files\\air_in.csv', mode ='a', sep=',', header = False, index=False)


def airout_append(file):
	file = file
	this_df=pd.read_csv(file)
	this_df.to_csv('D:\MRP\___website_server\\files\\air_out.csv', mode ='a', sep=',', header = False, index=False)



