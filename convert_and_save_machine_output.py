#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:50:49 2019

@author: laura

This program converts a DFX file into a CSV file and creates a table in one of 
the following databases: M1998, M2002 and M04
"""

"""
1. Convert DFX into CSV
2. Save the name of the generated CSV into a variable called new_table
3. Create the table and populate it with the contents of the CSV file
4. Run the linear regression right away
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

# create the query (as a string)
query = '''CREATE TABLE new_table
            LOAD DATA INFILE newtable+'.txt' 
            INTO TABLE new_table 
            FIELDS TERMINATED BY ',' 
            LINES TERMINATED BY '\n'
            IGNORE 1 ROWS;
           '''

# run the query
c.execute(query)

# close the connection
conn.close()