# ZG means type number
# a difference with our case is that we don't have the ZG thing in filepath """1546","a33",ZG_from_file[0:6],"pc"""

import sys
import os
from datetime import *
import time


import parse_dfb_dfd as parser
import generate_file_list as file_list


##############################################################################################################################
def find_field_in_dfd (dfd,field_to_find):
    found_field = 9999 #not found code
    for t in range(0,len(dfd),1):
        if dfd[t] == field_to_find:
            found_field = t
            break
    return found_field

##############################################################################################################################
def find_field_in_dfd_MSN_DATETIME(dfd):
    MSN_pos         = find_field_in_dfd (dfd,"MSN")
    DATETIME_pos    = find_field_in_dfd (dfd,"datetime")
    return MSN_pos, DATETIME_pos

##############################################################################################################################
def posix_time_from_date(date_qs_stat):
    dt = datetime.strptime(date_qs_stat,"%d.%m.%Y/%H:%M:%S")
    return time.mktime(dt.timetuple())

##############################################################################################################################
class STAT_LINE(object):
    def __init__(self):
        self.MSN            = 0
        self.POSIX_TIME     = 0
        self.DATETIME       = ""
        self.DATA           = ""

##############################################################################################################################
def create_CSV_FULL(machine,module,filetype,part_type):
    dfd_fields          = []
    dfb_fields          = []
    additionnal_fields  = []


    print("Generating file for "+machine+"/"+module+" for part type: "+part_type)

    #collecting all datas
    DATAS = []
    
    dfd_filelist = file_list.retrieve_new_file(machine,module,filetype,part_type)
    # print(dfd_filelist)
    # dfd_filelist is a list of file names (fullname) in increasing order
    for files in dfd_filelist:
        # parsing dfd / dfb or dfx file and mounting it in Ram
        dfd_fields, dfb_fields, additionnal_fields, error_code, file_errors = parser.dfd_dfb_parsing(files)
        if error_code == 0 and file_errors == 0:
            MSN_position, DATETIME_position  = find_field_in_dfd_MSN_DATETIME(dfd_fields)
            if MSN_position!=9999 and DATETIME_position !=9999:
                for lines in dfb_fields:
                    tmp             = STAT_LINE()
                    tmp.MSN         = lines[MSN_position][1:12]
                    tmp.DATETIME    = lines[DATETIME_position]
                    tmp.POSIX_TIME  = int(posix_time_from_date(tmp.DATETIME))
                    tmp.DATA        = lines
                    DATAS.append(tmp)
                    # del tmp
            else:
                print("Errors occured while parsing : ", files)
        else:
            print("Errors occured while parsing : ", files)

    # generating CSV file
    # after last step we should have a list called DATA containing all the data
    # the following step is trivial, not as important as the last one
    f = open("/Users/bosen/Desktop/"+machine+"_"+module+"_"+part_type+".csv","w")
    txt = "MSN,DATETIME,POSIX_TIME_LINE,"
    for i in dfd_fields:
        txt+= (i+",")
    f.write(txt+"\n")
    for i in DATAS:
        txt = (str(i.MSN)+",")
        txt+= (i.DATETIME+",")
        txt+= (str(i.POSIX_TIME)+",")
        for i in i.DATA:
            txt+=(i+",")
        txt+="\n"
        f.write(txt)     
    f.close()
    
    # free memory!
    del dfd_fields
    del dfb_fields
    del additionnal_fields
    return

# above is function definitions
##############################################################################################################################
# below is execution

# 1546
# f = open("part_type_file.txt","r")

# for part_type_from_file in f:
# DATA_PATH   = "/Users/bosen/Downloads/⁨Machine stats⁩/process⁩/Steering/"
create_CSV_FULL("M1998","m052","pc","888878")
create_CSV_FULL("M1998","m052","pc","950273")

# while True: 
#     print("Start : %s" % time.ctime())
#     create_CSV_FULL("M1998","m052","pc","888878")
#     create_CSV_FULL("M1998","m052","pc","950273")
#     sleep(3)
#     # sleep(300)
#     # do this every 300 seconds
#     print("End : %s" % time.ctime())







