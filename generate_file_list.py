######### a MacOS datapath is something like:
######### ..../process/Steering/M1998/m052/pc/888878/
######### DATA_PATH   = "/Users/bosen/Desktop/Capstone⁩/⁨Machine stats⁩/process⁩/Steering/"

######### while a Windows datapath is something like:
######### DATA_PATH + machine\\module\\subdir\\ZG\\*.dfd
######### DATA_PATH   = "C:\\Stats_machine\\DATAS_MACHINES\\m"

DATA_PATH   = "/Users/bosen/Desktop/Machine_stats/process/Steering/"

import os
import glob
import platform
import datetime

# variable last_time_stamp should be global in scope
# recording the last time we dealt with the incoming data
# even after the program crashes and gets reopened, the value should persist
last_time_stamp = 0

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
def retrieve_new_file(machine, module, subdir, part_type):
	# path_list_raw = glob.glob("/Users/bosen/Downloads/Machine_stats/process/Steering/M1998/m052/pc/888878/*.dfd")
    # path_list_raw = glob.glob(DATA_PATH+machine+"/"+module+"/"+subdir+"/"+part_type+"/*.dfd")
    path_list_raw = glob.glob(DATA_PATH+machine+"/"+module+"/"+subdir+"/"+part_type+"/19*.dfd")
    path_list_raw.extend(glob.glob(DATA_PATH+machine+"/"+module+"/"+subdir+"/"+part_type+"/19*.dfx"))
    path_list_raw.extend(glob.glob(DATA_PATH+machine+"/"+module+"/"+subdir+"/"+part_type+"/19*.dfb"))
    # print(path_list_raw)
    
    # selecting the new files by looking at their creation dates
    path_list = []
    for i in path_list_raw:
    	if (is_new):
    		path_list.append(i)
    print(path_list)
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

    print(platform.system())
    if platform.system() == 'Windows':
        ctime = os.path.getctime(path_to_file)
        return (ctime < last_time_stamp)
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
        previous    = int(filelist[0].split('/')[-1].split('.')[0][0:10])
        # for example, for a file called ..../process/Steering/M1998/m052/pc/888878/1234567890.dfx
        # previous = int(1234567890) 
        for lines in range(1,len(filelist),1):
            if not previous < int(filelist[lines].split('/')[-1].split('.')[0][0:10]):
                ######################### error!!! ######################
                # previous won't change
                errors+=1
    return errors