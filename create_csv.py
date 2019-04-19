# in the original file, ZG means type number
# a difference with our case is that we don't have the ZG thing in filepath 
# original function looks like: create_CSV_FULL("1546","a33",ZG_from_file[0:6],"pc")

import sys
import time
import threading


import parse_dfb_dfd as parser
import generate_file_list as file_list


##############################################################################################################################
# INPUT:    a list of data titles, a specific title
# RETURN:   the index of this specific field
def find_field_in_dfd (dfd, field_to_find):
    found_field = 9999 #not found code
    for t in range(0,len(dfd),1):
        if dfd[t] == field_to_find:
            found_field = t
            break
    return found_field

##############################################################################################################################
# INPUT:    a list of data titles
# RETURN:   the index of title "Batch Number" and "Date/Time"
def find_field_in_dfd_MSN_DATETIME(dfd):
    MSN_pos         = find_field_in_dfd (dfd,"Batch Number")
    DATETIME_pos    = find_field_in_dfd (dfd,"Date/Time")
    return MSN_pos, DATETIME_pos

##############################################################################################################################
# INPUT:    directory information
# RETURN:   nothing, but create the final .csv file in the specified directory
def create_CSV_FULL(machine,module,filetype,part_type):
    dfd_fields          = []
    dfb_fields          = []
    additionnal_fields  = []

    print("Generating file for "+machine+"/"+module+" for part type: "+part_type)

    DATAS = []
    
    # create a list of file names (fullname) in increasing order
    dfd_filelist = file_list.retrieve_new_file(machine,module,filetype,part_type)
    # print(dfd_filelist)
    for files in dfd_filelist:
        # parsing .dfd and .dfb/.dfx file and mounting them
        dfd_fields, dfb_fields, additionnal_fields, error_code, file_errors = parser.dfd_dfb_parsing(files)
        if error_code == 0 and file_errors == 0:
            # if we are here, there's no error while parsing
            MSN_position, DATETIME_position  = find_field_in_dfd_MSN_DATETIME(dfd_fields)
            if MSN_position!=9999 and DATETIME_position !=9999:
                for lines in dfb_fields:
                    # print(dfd_fields)
                    # print(lines)
                    DATAS.append(lines)
            else:
                print("1_Errors occured while parsing : ", files)
        else:
            print("2_Errors occured while parsing : ", files)

    # generating CSV file
    # before this step we should have a list called DATA containing all the data
    # the following step is trivial, not as important as the last one
    f = open("/Users/bosen/Desktop/"+machine+"_"+module+"_"+part_type+".csv","w")
    txt = ""
    for title in dfd_fields:
        # print("title: ", title)
        txt+= titles
        txt+= ","
    f.write(txt+"\n")
    for row in DATAS:
        # print("row: ",row)
        txt = ""
        for fields in row:
            txt+=(fields+",")
        txt+="\n"
        f.write(txt)     
    f.close()
    
    # free memory
    # but I don't think that's needed
    # we return after this step 
    # and all the dynamic memory used should be auto released
    del dfd_fields
    del dfb_fields
    del additionnal_fields

    return

# above is function definition
##############################################################################################################################
# below is execution

# TEST **********************************************
# DATA_PATH   = "/Users/bosen/Downloads/⁨Machine stats⁩/process⁩/Steering/"
create_CSV_FULL("M1998","m052","pc","888878")
create_CSV_FULL("M1998","m052","pc","950273")

# MAIN **********************************************
# def main():
#     threading.Timer(300.0, main).start()
#     print("Start : %s" % time.ctime())
#     create_CSV_FULL("M1998","m052","pc","888878")
#     create_CSV_FULL("M1998","m052","pc","950273")
#     print("End : %s" % time.ctime())
#     print()

# main()
