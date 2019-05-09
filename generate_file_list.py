######### a MacOS datapath is something like:
######### ..../process/Steering/M1998/m052/pc/888878/
######### DATA_PATH   = "/Users/bosen/Desktop/Capstone⁩/⁨Machine stats⁩/process⁩/Steering/"

######### while a Windows datapath is something like:
######### DATA_PATH + machine\\module\\subdir\\ZG\\*.dfd
######### DATA_PATH   = "C:\\Stats_machine\\DATAS_MACHINES\\m"

DATA_PATH = "T:\\steering\\"

import os
import glob
import platform
import datetime

# record the last time we dealt with the incoming data in a file so it persists
timestamp_path = "C:\\Users\\supplier_admin\\Desktop\\CSV\\timestamp.txt"
timestamp = open(timestamp_path,"r")
last_time_stamp = float(timestamp.readline().replace('\n',''))
timestamp.close()

##############
# INPUT:    directory information
# RETURN:   a list of new files in the target directory
# NOTE:     many of them are old files, we'll have to find the new ones
def retrieve_new_file(machine, module, part_type):
    part_list = glob.glob(machine+"\\"+module+"\\"+part_type+"\\*")

    # selecting the new files by looking at their creation dates
    final_list = []
    for path in part_list:
        temp_list = retrieve_new_file_from_part(path)
        final_list.extend(temp_list)
    
    #Record new current timestamp before exiting the file list generator
    timestamp = open(timestamp_path,"w")
    timestamp.write(str(os.path.getctime(timestamp_path)))
    timestamp.close()
    return final_list

##############################################################################################################################
# glob module finds all pathnames matching a specified pattern
# for example:
# >>> glob.glob('./[0-9].*')
# ['./1.gif', './2.txt']
# >>> glob.glob('*.gif')
# ['1.gif', 'card.gif']
# the return type is a list of full file names (including the path) in increasing order
##############
# INPUT:	directory information
# RETURN:	a list of new files in the target directory
# NOTE:		many of them are old files, we'll have to find the new ones
def retrieve_new_file_from_part(path):
    path_list_raw = glob.glob(DATA_PATH+path+"\\*.dfd")

    # selecting the new files by looking at their creation dates
    path_list = []
    for i in path_list_raw:
        if path_list_raw.index(i)==0:
            print("Last time stamp: "+str(last_time_stamp))
            print("Current time stamp: "+str(os.path.getctime(i)))
            print(is_new(i))
        if (is_new(i)):
            path_list.append(i)
    
    #Record new current timestamp before exiting the file list generator
    return path_list

##############################################################################################################################
    # From Wikipedia
    """
    A timestamp is a sequence of characters or encoded information 
    identifying when a certain event occurred, 
    usually giving date and time of day, 
    sometimes accurate to a small fraction of a second
    """
    """
    os.path.getctime() will give us a time stamp looking like:
            1551348525.5509124
    the bigger the time stamp is, the older the file is
    so we can locate new files by comparing the time stamp
    """
# INPUT:	full file name including the path
# RETURN:	True if it's a new file, false otherwise
def is_new(path_to_file):

    if platform.system() == 'Windows':
        ctime = os.path.getctime(path_to_file)
        return (ctime > last_time_stamp)
    else:
        stat = os.stat(path_to_file)
        ctime = stat.st_birthtime
        try:
	        return (ctime < last_time_stamp)
        except AttributeError:
            mtime = stat.st_birthtime
            return (mtime < last_time_stamp)

##############################################################################################################################
# INPUT:	a list of files
# RETURN:	0 if the filenames are in increasing order
# RETURN:	a positive integer otherwise
def verify_files_chronologic_order(filelist):
    errors      = 0
    if len(filelist) > 0:
        previous    = int(filelist[0].split('\\')[-1].split('.')[0][0:10])
        # for example, for a file called ..../process/Steering/M1998/m052/pc/888878/1234567890.dfx
        # previous = int(1234567890) 
        for lines in range(1,len(filelist),1):
            if not previous < int(filelist[lines].split('\\')[-1].split('.')[0][0:10]):
                ######################### error!!! ######################
                # previous won't change
                errors+=1
    return errors
