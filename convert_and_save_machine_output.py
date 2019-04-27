#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 15:50:49 2019

@author: laura

This program converts a DFX file into a CSV file and creates a table in one of 
the following databases: M1998, M2002 and M04
"""

"""
1. Convert DFD into CSV
2. Save the name of the generated CSV into a variable called new_data
3. Update the correct table with the contents of the CSV file
"""

# import statements
import cgi, cgitb
cgitb.enable()
import sys, os
import codecs
import cx_Oracle
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Establish connection to Oracle database. Is it okay to hardcode credentials?
dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name')
conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns)

# set up the cursor
c = conn.cursor()

# create the query (as a string)
query = "sqlldr "+user+"/"+pw+"@"+server+" control=loader.ctl"

# run the query
c.execute(query)

query = ''' CREATE OR REPLACE TRIGGER test_trigger
			BEFORE INSERT
			ON M052
			REFERENCING NEW AS NEW
			FOR EACH ROW
			BEGIN
			SELECT M052IDs.nextval INTO :NEW.M052ID FROM dual;
			END;
			load data
 			infile '''+new_data+'''.csv'
 			into table M06
 			fields terminated by ","
		'''

# close the connection
conn.close()