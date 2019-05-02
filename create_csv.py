# import statements
import sys, os
import time
import threading
import cgi, cgitb
cgitb.enable()
import sys, os
import codecs
#import cx_Oracle
#import visualize_data as vis
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import parse_dfb_dfd as parser
import generate_file_list as file_list

# Authentication information for database connection
user = 'sys'
pw = 'oracle'
server = 'orc1'

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
    MSN_pos         = find_field_in_dfd (dfd, "Batch Number")
    DATETIME_pos    = find_field_in_dfd (dfd, "Date/Time")
    return MSN_pos, DATETIME_pos

##############################################################################################################################
# INPUT:    directory information
# RETURN:   nothing, but create the final .csv file in the specified directory
def create_CSV_FULL(machine,module,filetype,part_type):
    dfd_fields          = []
    dfb_fields          = []
    additionnal_fields  = []

    print("Generating file for "+machine+"/"+module+" for part type: "+part_type)

    DATA = []
    
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
                    DATA.append(lines)
            else:
                print("1_Errors occured while parsing : ", files)
        else:
            print("2_Errors occured while parsing : ", files)
#################################################################################################
	"""
	# Establish connection to Oracle database
	dsn_tns = cx_Oracle.makedsn('Host Name', 'Port Number', service_name='Service Name')
	conn = cx_Oracle.connect(user=r'User Name', password='Personal Password', dsn=dsn_tns)

	# set up the cursor
	try:
		c = conn.cursor()
	except:
		print("Unable to connect to the database")
	"""
#################################################################################################
    # generating CSV file
    # before this step we should have a list called DATA containing all the data
    # the following step is trivial, not as important as the last one
    f = open("C:\\Users\\supplier_admin\\Desktop\\CSV\\"+machine+"_"+module+"_"+part_type+".csv", "w")
    txt = ""
    for title in dfd_fields:
        # print("title: ", title)
        txt+= title
        txt+= ","
    f.write(txt+"\n")
    for row in DATA:
        # print("row: ",row)
        txt = ""
        for fields in row:
            txt+=(fields+",")
        txt+="\n"
        f.write(txt)     
        """
        # Check if a table already exists for this module, if not, create the table based on
        # the schema of the titles
        
        query = "DESC "+module.upper()
        c.execute(query)
        result = c.fetchall()
        
        
        if "ERROR" in result:
        	query = '''CREATE TABLE '''+module.upper()+'''
        	for title in dfd_fields:
        		query += title + " VARCHAR(40),"
        	query += ")"
        	c.execute(query)
        		        
        # At the same time update the database too
        query = '''INSERT INTO '''+module.upper()+''' VALUES '''+txt
		c.execute(query)
	f.close()
    c.close()
    vis.visualize_data()
    """

    return

# above is function definition
##############################################################################################################################
# below is execution


#create_CSV_FULL("M1998","m052","pc","950273")
#create_CSV_FULL("M1998","m052","pc","944436")
#create_CSV_FULL("M1998","m052","pc","888878")
# MAIN **********************************************
# def main():
#     threading.Timer(300.0, main).start()
#     print("Start : %s" % time.ctime())
#     create_CSV_FULL("M1998","m052","pc","888878")
#     create_CSV_FULL("M1998","m052","pc","950273")
#     print("End : %s" % time.ctime())
#     print()

# main()
