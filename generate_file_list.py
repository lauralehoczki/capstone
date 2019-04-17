# path_list = glob.glob("/Users/bosen/Downloads/Machine_stats/process/Steering/M1998/m052/pc/888878/*.dfd")

######### this is something we need to change
######### our datapath is something like this:
######### ..../process/Steering/M1998/m052/pc/888878/
######### original datapath is something like this:
######### DATA_PATH+machine\\module\\subdir\\ZG\\*.dfd

# DATA_PATH   = "C:\\Stats_machine\\DATAS_MACHINES\\m"
# DATA_PATH   = "/Users/bosen/Desktop/Capstone⁩/⁨Machine stats⁩/process⁩/Steering/"
DATA_PATH   = "/Users/bosen/Downloads/Machine_stats/process/Steering/"

######### also, the file extensions are different
######### we have types of .dfd and .dfx 

import os
import glob
import platform
import datetime
# variable last_time_stamp should be global in scope
# recording the last time we dealt with the incoming data
last_time_stamp = 0


##############################################################################################################################
# glob module finds all the pathnames matching a specified pattern
# for example:
# >>> glob.glob('./[0-9].*')
# ['./1.gif', './2.txt']
# >>> glob.glob('*.gif')
# ['1.gif', 'card.gif']
# the return of this funtion is a list of file names (fullname) in increasing order
def retrieve_new_file(machine, module, subdir, part_type):
	# get all files in the target directory
	# however, some of them can be old files, we'll have to find the new ones
    path_list_raw = glob.glob(DATA_PATH+machine+"/"+module+"/"+subdir+"/"+part_type+"/*.dfd")

	# to verify whether the files are in chronologic order
	# what's the point of doing so?
    # path_list = glob.glob(DATA_PATH+machine+"/"+module+"/"+subdir+"/"+part_type+"/19*.dfd")
    # print(path_list)
    # if verify_files_chronologic_order(path_list)!=0:
    #     path_list = []
    #     print("Critical Error files were not chronologically ordered !!!")
    
    # get the new files
    path_list = []
    for i in path_list_raw:
    	if (is_new):
    		path_list.append(i)

    return path_list

##############################################################################################################################
    """
    os.path.getctime() will give us somehting like this
            1551348525.5509124
    this is called a time stamp
    the bigger the time stamp is, the older the file is
    so we can locate new files by comparing the time stamp"""

    # From Wikipedia
    """
    A timestamp is a sequence of characters or encoded information 
    identifying when a certain event occurred, 
    usually giving date and time of day, 
    sometimes accurate to a small fraction of a second"""

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
# the input is a list of files derived by glob
# returns 0 if the filenames are in increasing order
# returns a positive integer otherwise
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