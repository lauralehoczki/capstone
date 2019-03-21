#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:11:25 2019

@author: laura
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
query = '''SELECT M1998.value, M2002.otherValue
           FROM M1998, M2002
           '''

# run the query
c.execute(query)

# fetch the data in the result set
result = c.fetchall()

#### VISUALIZE DATA
##for row in result:

# close the connection
conn.close()