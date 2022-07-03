import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet, LabelSet, DataTable, TableColumn, DateFormatter
from bokeh.io import curdoc
from bokeh.embed import components
from bokeh.resources import CDN
import datetime


def humidity_plot():
	df = pd.read_csv('D:\MRP\___website_server\\files\\raw.csv', parse_dates=['date'])
	data_source = ColumnDataSource(df)

	x=df['date']
	y=df['max_hum']

	y=df['min_hum']

	output_file("hum.html")

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"


	p = figure(tools=TOOLS,title="Maximum  and Minimum Humidity", 
                x_axis_label='Date', 
                y_axis_label='Humidity', 
                x_axis_type='datetime',
                plot_height=264, plot_width=558)
	p.hover.tooltips = [("date", "@date{%F}"),
                        ("max_hum", "@max_hum"),
                       ("min_hum" , "@min_hum")]



	p.hover.formatters = {'@date' : 'datetime'}

	p.line(x='date', y='max_hum', source=data_source, line_width=1, legend_label='Maximum Humidity', color="cornflowerblue")
	p.line(x='date', y='min_hum', source=data_source, line_width=1, legend_label='Minimum_Humidity', color="red")

	p.circle(x='date', y='max_hum', source=data_source, line_width=1, legend_label='Maximum Humidity', color="cornflowerblue")
	p.circle(x='date', y='min_hum', source=data_source, line_width=1, legend_label='Minimum_Humidity', color="red")

	return p

def humidity_plot_full():
	df = pd.read_csv('D:\MRP\___website_server\\files\\raw.csv', parse_dates=['date'])
	data_source = ColumnDataSource(df)

	x=df['date']
	y=df['max_hum']

	y=df['min_hum']

	output_file("hum.html")

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"


	p = figure(tools=TOOLS,title="Maximum  and Minimum Humidity", 
                x_axis_label='Date', 
                y_axis_label='Humidity', 
                x_axis_type='datetime',
                plot_height=536, plot_width=1132)
	p.hover.tooltips = [("date", "@date{%F}"),
                        ("max_hum", "@max_hum"),
                       ("min_hum" , "@min_hum")]



	p.hover.formatters = {'@date' : 'datetime'}

	p.line(x='date', y='max_hum', source=data_source, line_width=1, legend_label='Maximum Humidity', color="cornflowerblue")
	p.line(x='date', y='min_hum', source=data_source, line_width=1, legend_label='Minimum_Humidity', color="red")

	p.circle(x='date', y='max_hum', source=data_source, line_width=1, legend_label='Maximum Humidity', color="cornflowerblue")
	p.circle(x='date', y='min_hum', source=data_source, line_width=1, legend_label='Minimum_Humidity', color="red")

	return p


def temperature_plot():
	df = pd.read_csv('D:\MRP\___website_server\\files\\raw.csv', parse_dates=['date'])
	data_source = ColumnDataSource(df)

	#df.sort_values(by=['date'])
	#df['collection_date'] = pd.to_datetime(df['collection_date']) 

	#defining axis
	x=df['date']
	y=df['max_temp']


	y=df['min_temp']

	#output to html file
	output_file("temp.html")

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"


	#HUMIDITY
	p2 = figure(tools=TOOLS,title="Maximum  and Minimum Temperature", 
	            x_axis_label='Date', 
	            y_axis_label='Temperature in celcius', 
	            x_axis_type='datetime',
	            plot_height=264, plot_width=555)
	p2.hover.tooltips = [("date", "@date{%F}"),
	                    ("max_temp", "@max_temp"),
	                   ("min_temp" , "@min_temp")]

	p2.hover.formatters = {'@date' : 'datetime'}

	p2.line(x='date', y='max_temp', source=data_source, line_width=1, legend_label='Maximum Temperature', color="cornflowerblue")
	p2.line(x='date', y='min_temp', source=data_source, line_width=1, legend_label='Minimum Temperature', color="red")

	p2.circle(x='date', y='max_temp', source=data_source, line_width=1, legend_label='Maximum Temperature', color="cornflowerblue")
	p2.circle(x='date', y='min_temp', source=data_source, line_width=1, legend_label='Minimum Temperature', color="red")

	return p2

def temperature_plot_full():
	df = pd.read_csv('D:\MRP\___website_server\\files\\raw.csv', parse_dates=['date'])
	data_source = ColumnDataSource(df)

	#df.sort_values(by=['date'])
	#df['collection_date'] = pd.to_datetime(df['collection_date']) 

	#defining axis
	x=df['date']
	y=df['max_temp']


	y=df['min_temp']

	#output to html file
	output_file("temp.html")

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"


	#HUMIDITY
	p2 = figure(tools=TOOLS,title="Maximum  and Minimum Temperature", 
	            x_axis_label='Date', 
	            y_axis_label='Temperature in celcius', 
	            x_axis_type='datetime',
	            plot_height=536, plot_width=1132)
	p2.hover.tooltips = [("date", "@date{%F}"),
	                    ("max_temp", "@max_temp"),
	                   ("min_temp" , "@min_temp")]

	p2.hover.formatters = {'@date' : 'datetime'}

	p2.line(x='date', y='max_temp', source=data_source, line_width=1, legend_label='Maximum Temperature', color="cornflowerblue")
	p2.line(x='date', y='min_temp', source=data_source, line_width=1, legend_label='Minimum Temperature', color="red")

	p2.circle(x='date', y='max_temp', source=data_source, line_width=1, legend_label='Maximum Temperature', color="cornflowerblue")
	p2.circle(x='date', y='min_temp', source=data_source, line_width=1, legend_label='Minimum Temperature', color="red")

	return p2


def material_plot():
	df = pd.read_csv('D:\MRP\___website_server\\files\\material.csv')
	todos=df.values.tolist()
	return todos

	
	return p5

def airin_plot():
	df = pd.read_csv('D:\MRP\___website_server\\files\\air_in.csv', parse_dates=['Time'])
	data_source = ColumnDataSource(df)

	#df.sort_values(by=['date'])
	#df['collection_date'] = pd.to_datetime(df['collection_date']) 

	#defining axis
	x=df['Time']
	y=df['percentage_in']


	#output to html file
	output_file("inside.html")

	curdoc().theme = "dark_minimal"

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

	p3 = figure(tools=TOOLS, title="Inside Air Flow", 
	            x_axis_label='Time', 
	            y_axis_label='air %', 
	            x_axis_type='datetime',
	            plot_height=269, plot_width=352)

	p3.hover.tooltips = [("inside air", "@percentage_in")]

	p3.hover.formatters = {'@Time' : 'datetime'}




	p3.line(x='Time', y='percentage_in', source=data_source, line_width=1, legend_label='Inside Air Flow', color="red")


	p3.circle(x='Time', y='percentage_in', source=data_source, line_width=1, legend_label='Inside Air Flow', color="red")
	return p3


def airout_plot():
	df = pd.read_csv('D:\MRP\___website_server\\files\\air_out.csv', parse_dates=['Time'])
	data_source = ColumnDataSource(df)

	#df.sort_values(by=['date'])
	#df['collection_date'] = pd.to_datetime(df['collection_date']) 

	#defining axis
	x=df['Time']
	y=df['air_out']


	#output to html file
	output_file("outside.html")

	curdoc().theme = "dark_minimal"

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

	p4 = figure(tools=TOOLS, title="Outside Air Flow", 
	            x_axis_label='Time', 
	            y_axis_label='air %', 
	            x_axis_type='datetime',
	            plot_height=269, plot_width=352)

	p4.hover.tooltips = [
	                    ("outside air", "@{air_out}")]

	p4.hover.formatters = {'@Time' : 'datetime'}




	p4.line(x='Time', y='air_out', source=data_source, line_width=1, legend_label='Outside Air Flow', color="cornflowerblue")


	p4.circle(x='Time', y='air_out', source=data_source, line_width=1, legend_label='Outside Air Flow', color="cornflowerblue")
	return p4



def airin_plot_full():
	df = pd.read_csv('D:\MRP\___website_server\\files\\air_in.csv', parse_dates=['Time'])
	data_source = ColumnDataSource(df)

	#df.sort_values(by=['date'])
	#df['collection_date'] = pd.to_datetime(df['collection_date']) 

	#defining axis
	x=df['Time']
	y=df['percentage_in']


	#output to html file
	output_file("inside.html")

	curdoc().theme = "dark_minimal"

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

	p3 = figure(tools=TOOLS, title="Inside Air Flow", 
	            x_axis_label='Time', 
	            y_axis_label='air %', 
	            x_axis_type='datetime',
	            plot_height=265, plot_width=1132)

	p3.hover.tooltips = [("inside air", "@percentage_in")]

	p3.hover.formatters = {'@Time' : 'datetime'}




	p3.line(x='Time', y='percentage_in', source=data_source, line_width=1, legend_label='Inside Air Flow', color="red")


	p3.circle(x='Time', y='percentage_in', source=data_source, line_width=1, legend_label='Inside Air Flow', color="red")
	return p3


def airout_plot_full():
	df = pd.read_csv('D:\MRP\___website_server\\files\\air_out.csv', parse_dates=['Time'])
	data_source = ColumnDataSource(df)

	#df.sort_values(by=['date'])
	#df['collection_date'] = pd.to_datetime(df['collection_date']) 

	#defining axis
	x=df['Time']
	y=df['air_out']


	#output to html file
	output_file("outside.html")

	curdoc().theme = "dark_minimal"

	TOOLS = "hover,pan,wheel_zoom,box_zoom,reset,save"

	p4 = figure(tools=TOOLS, title="Outside Air Flow", 
	            x_axis_label='Time', 
	            y_axis_label='air %', 
	            x_axis_type='datetime',
	            plot_height=265, plot_width=1132)

	p4.hover.tooltips = [
	                    ("outside air", "@{air_out}")]

	p4.hover.formatters = {'@Time' : 'datetime'}




	p4.line(x='Time', y='air_out', source=data_source, line_width=1, legend_label='Outside Air Flow', color="cornflowerblue")


	p4.circle(x='Time', y='air_out', source=data_source, line_width=1, legend_label='Outside Air Flow', color="cornflowerblue")
	return p4