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
import pymysql
from creds import *
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# create a connection to the MySQL database
conn = pymysql.connect(host,user,passwd,db,charset="utf8mb4",cursorclass=pymysql.cursors.DictCursor)

# set up the cursor
c = conn.cursor()

# Query user for the names of the tables they want to analyze
table1 = input("Enter the name for table 1")
table2 = input("Enter the name for table 2")

# create the query (as a string)
query = '''SELECT table1.value, table2.otherValue
           FROM M1998.table1, M2002.table2
           '''

# run the query
c.execute(query)

# fetch the data in the result set
result = c.fetchall()

#### VISUALIZE DATA
##for row in result:

# close the connection
conn.close()