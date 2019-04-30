#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program is for running further analysis on data after it has been stored 
in the database
"""

# import statements
import cgi, cgitb
cgitb.enable()
import sys, os
import codecs
#import cx_Oracle
from creds import *
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns 
sns.set(color_codes=True)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Authentication information for Oracle
user = 'sys'
password = 'oracle'
server = 'orc1'

# Location for analysis graphs
#save_folder = "/Users/bosen/Desktop/"
save_folder = "C:\Users\supplier_admin\Desktop\Analysis"

"""
# Establish connection to Oracle database
dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name')
conn = cx_Oracle.connect(user, password, dsn=dsn_tns)

# set up the cursor
c = conn.cursor()

# create the query (as a string)
query = '''SELECT M06.P_Offset_A_1st_run,
			M052.Q052QualMeasMMaftJoinWOload
           FROM M052, M06, M04 
           WHERE M06.M06BatchNumber = M04.BatchNumber
           AND M052.M052BatchNumber = M04.DMC_GearUnit
           '''

# run the query
c.execute(query)

# fetch the data in the result set
result = c.fetchall()

mm_with_load = []
mm_without_load = []
#### VISUALIZE DATA
for row in result:
	mm_with_load.append(float(row[0]))
	mm_without_load.append(float(row[1]))
	
# close the connection
conn.close()
"""

data = [[mm_with_load[i],mm_without_load[i]] for i in range(len(mm_with_load))]
df = pd.DataFrame(data, columns = ['mm_with_load', 'mm_without_load']) 

ax = sns.regplot(x=df.mm_with_load, y=df.mm_without_load, color="b")
fig = ax.get_figure()
fig_name = "sample.png"
fig.savefig(save_folder + fig_name)

print("Finished! Files saved at: ", save_folder + fig_name)