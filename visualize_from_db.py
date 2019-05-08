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
import datetime
#import cx_Oracle
import pandas as pd
import seaborn as sns 
sns.set(color_codes=True)
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

# Authentication information for Oracle
user = 'sys'
password = 'oracle'
server = 'orc1'

# Location for analysis graphs
save_folder = "C:\\Users\\supplier_admin\\Desktop\\Analysis\\"
last_analyzed = open(save_folder+"last_rownum.txt","r")
last_analyzed_row = last_analyzed.readline().replace('\n', '')
last_analyzed.close()

def visualize_data():
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
           WHERE rownum > ''' +last_analyzed_row+ '''
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
        
    
    # data = [[mm_with_load[i],mm_without_load[i]] for i in range(len(mm_with_load))]
    # df = pd.DataFrame(data, columns = ['mm_with_load', 'mm_without_load']) 

    # ax = sns.regplot(x=df.mm_with_load, y=df.mm_without_load, color="b")
    # fig = ax.get_figure()
    plt.scatter(mm_with_load, mm_without_load)
    

    # Update the last analyzed record's row number
    query = "SELECT MAX(ROWNUM) FROM " + machine.upper()
    c.execute(query)
    result = c.fetchall()
    c.close()
    last_analyzed = open("C:\\Users\\supplier_admin\\Desktop\\Analysis\\last_rownum.txt","w")
    last_analyzed.write(result)
    last_analyzed.close()
    
    # The filename is going to be the time it was created
    currentDT = datetime.datetime.now()
    fig_name = currentDT.strftime("%H:%M:%S")
    # fig.savefig(save_folder + fig_name + ".png")
    plt.savefig(save_folder + fig_name + ".png")

visualize_data()