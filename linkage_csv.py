# import statements
import sys, os
import time
import threading
import cgi, cgitb
cgitb.enable()
import sys, os
import codecs
import cx_Oracle
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

import linkage_parser as parser
import generate_file_list as file_list

# Authentication information for database connection
user = 'sysdba'
pw = 'oracle'
server = 'orc1'
hostname = 'j4m8888'
portnum = '1521'

##############################################################################################################################
# INPUT:	a list of data titles, a specific title
# RETURN:	the index of this specific field
def find_field_in_dfd (dfd, field_to_find):
	found_field = 9999 #not found code
	for t in range(0,len(dfd),1):
		if dfd[t] == field_to_find:
			found_field = t
			break
	return found_field

##############################################################################################################################
# INPUT:	a list of data titles
# RETURN:	the index of title "Batch Number" and "Date/Time"
def find_field_in_dfd_MSN_DATETIME(dfd):
	MSN_pos 		 = find_field_in_dfd (dfd, "Batch Number")
	DATETIME_pos	= find_field_in_dfd (dfd, "Date/Time")
	return MSN_pos, DATETIME_pos

#############################################################################################################################
# INPUT:	directory information
# RETURN:	nothing, but create the final .csv file in the specified directory
def create_CSV_FULL(machine,module,part_type):
	dfd_fields			= []
	dfb_fields			= []
	additionnal_fields	= []

	print("Generating file for "+machine+"/"+module+"/"+part_type)

	DATA = []

	# create a list of file names (fullname) in increasing order
	dfd_filelist = file_list.retrieve_new_file(machine, module, part_type)
	# print(dfd_filelist)
	for files in dfd_filelist:
		# parsing .dfd and .dfb/.dfx file and mounting them
		dfd_fields, dfb_fields, additionnal_fields, error_code, file_errors = parser.parsing(files)
		# print(dfb_fields)
		if error_code == 0 and file_errors == 0:
			# if we are here, there's no error while parsing
			# print("No error from parsing")
			MSN_position, DATETIME_position  = find_field_in_dfd_MSN_DATETIME(dfd_fields)
			if MSN_position!=9999 and DATETIME_position !=9999:
				for lines in dfb_fields:
					DATA.append(lines)
			else:
				print("1_Errors occured while parsing: ", files)
		else:
			print("2_Errors occured while parsing: ", files)
	if error_code == 0 and file_errors == 0:
		# if we are here, there's no error while parsing
		# print("No error from parsing")
		MSN_position, DATETIME_position  = find_field_in_dfd_MSN_DATETIME(dfd_fields)
		if MSN_position!=9999 and DATETIME_position !=9999:
			for lines in dfb_fields:
				# print(dfd_fields)
				# print(lines)
				DATA.append(lines)
              
##############################################################################################################################
	
	# Establish connection to Oracle database
	#conn = cx_Oracle.connect(user,pw,hostname+':'+portnum+'/'+server, cx_Oracle.SYSDBA)
	#c = conn.cursor()
####################################################################################################

	# generate CSV file
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
			txt+=("'"+fields+"',")
		
		# At the same time update the database too
		#query = '''INSERT INTO '''+machine.upper()+''' VALUES('''+txt+''')'''
		#c.execute(query)
		
		txt+="\n"
		f.write(txt)

	f.close()
    	#c.close()

	return

# above is function definition
##############################################################################################################################
# below is execution

#test m04
#create_CSV_FULL("M2002","m04","bd")
