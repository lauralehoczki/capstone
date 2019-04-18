# in the original file, ZG means type number
# a difference with our case is that we don't have the ZG thing in filepath 
# original function looks like: create_CSV_FULL("1546","a33",ZG_from_file[0:6],"pc")

import sys
import time
import threading


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
    MSN_pos         = find_field_in_dfd (dfd,"Batch Number")
    DATETIME_pos    = find_field_in_dfd (dfd,"Date/Time")
    return MSN_pos, DATETIME_pos

##############################################################################################################################
def posix_time_from_date(date_qs_stat):
    dt = datetime.strptime(date_qs_stat,"%d.%m.%Y/%H:%M:%S")
    return time.mktime(dt.timetuple())

##############################################################################################################################
##############################################################################################################################
# no need for this object
##############################################################################################################################
# class STAT_LINE(object):
#     def __init__(self):
#         self.MSN            = 0
#         self.POSIX_TIME     = 0
#         self.DATETIME       = ""
#         self.DATA           = ""

##############################################################################################################################
def create_CSV_FULL(machine,module,filetype,part_type):
    dfd_fields          = []
    dfb_fields          = []
    additionnal_fields  = []
    dfd_max_length      = 0
    # here since dfd files have different lengths
    # we only want the longest one


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
            # if we are here, there's no error while parsing
            MSN_position, DATETIME_position  = find_field_in_dfd_MSN_DATETIME(dfd_fields)
            if MSN_position!=9999 and DATETIME_position !=9999:
                for lines in dfb_fields:
                    # print(dfd_fields)
                    # print(lines)
##############################################################################################################################
# no need for this object
##############################################################################################################################
                    # tmp             = STAT_LINE()
                    # tmp.MSN         = lines[MSN_position][1:12]
                    # tmp.DATETIME    = lines[DATETIME_position]
                    # tmp.POSIX_TIME  = int(posix_time_from_date(tmp.DATETIME))
                    # tmp.DATA        = lines
                    # DATAS.append(tmp)
                    DATAS.append(lines)
                    # del tmp
            else:
                print("1_Errors occured while parsing : ", files)
        else:
            print("2_Errors occured while parsing : ", files)

    # generating CSV file
    # after last step we should have a list called DATA containing all the data
    # the following step is trivial, not as important as the last one
    f = open("/Users/bosen/Desktop/"+machine+"_"+module+"_"+part_type+".csv","w")
    txt = ""
    for titles in dfd_fields:
        # print("i: ",i)
        txt+= titles
        txt+= ","
    f.write(txt+"\n")
    for row in DATAS:
        # print("i: ",i)
        # txt = (str(i.MSN)+",")
        # txt+= (i.DATETIME+",")
        # txt+= (str(i.POSIX_TIME)+",")
        txt = ""
        for fields in row:
            txt+=(fields+",")
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

# for part_type_from_file in f:
# DATA_PATH   = "/Users/bosen/Downloads/⁨Machine stats⁩/process⁩/Steering/"
create_CSV_FULL("M1998","m052","pc","888878")
create_CSV_FULL("M1998","m052","pc","950273")

# def main():
#     threading.Timer(300.0, main).start()
#     print("Start : %s" % time.ctime())
#     create_CSV_FULL("M1998","m052","pc","888878")
#     create_CSV_FULL("M1998","m052","pc","950273")
#     print("End : %s" % time.ctime())
#     print()

# main()





