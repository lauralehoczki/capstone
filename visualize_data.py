#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:11:25 2019

@author: laura

This program is for running further analysis on data after it has been stored 
in a database
"""

# import statements
import cgi, cgitb
cgitb.enable()
import sys, os
import codecs
import cx_Oracle
from creds import *
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Establish connection to Oracle database
dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name')
conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns)

# set up the cursor
c = conn.cursor()

# create the query (as a string)
query = '''SELECT P_052_Quality_measuring_MM_after_joining_with_load, 
				Q_052_Quality_measuring_MM_after_joining_without_load
           FROM M052
           '''

# run the query
c.execute(query)

# fetch the data in the result set
result = c.fetchall()

#### VISUALIZE DATA
##for row in result:

# close the connection
conn.close()