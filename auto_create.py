import threading
import os
import time
import create_csv as pc_csv
import linkage_csv as bd_csv
# pc_csv creates the csv for data files
# bd_csv creates the csv for lankage files

timestamp_path = "C:\\Users\\supplier_admin\\Desktop\\timestamp.txt"
JOB_PATH = "C:\\Users\\supplier_admin\\Desktop\\JOB_PATH.txt"

def main():
	print("Start : %s" % time.ctime())
	# ********************************************************************
	job_file = open(JOB_PATH, "r")
	#job_file = ["T,M2002,m06,pc"]
	for line in job_file:
		#print(line)
		info_list = line.rstrip('\n').split(",")
		#print(info_list)
		
		if info_list[3] == "pc":
			pc_csv.create_CSV_FULL(info_list[0], info_list[1], info_list[2], info_list[3])
		if info_list[3] == "bd":
			bd_csv.create_CSV_FULL(info_list[0], info_list[1], info_list[2], info_list[3])

	# part_lis = glob.glob("M2002/m06/pc")
	# for part in part_lis:
	# 	pc_csv.create_CSV_FULL("M2002","m06","pc",part)

	# ********************************************************************
	print("End : %s" % time.ctime())
    
    #Record new current timestamp before exiting the file list generator
	timestamp = open(timestamp_path,"w")
	timestamp.write(str(time.time()-300))
	timestamp.close()
    
	print()

main()