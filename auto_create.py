import threading
import time
# import create_csv as pc_csv
# import linkage_csv as bd_csv
# pc_csv creates the csv for data files
# bd_csv creates the csv for lankage files

def main():
	while True:
		# in this test example, it's 300 seconds
		# we can change it to whatever we want
	    threading.Timer(300.0, main).start()
	    print("Start : %s" % time.ctime())
	    time.sleep(2)
	    # ********************************************************************
	    job_file = open(JOB_PATH, "r")
	    for line in job_file:
	    	info_list = line.split(",")
	    	if info_list[2] == "pc":
		    	pc_csv.create_CSV_FULL(info_list[0], info_list[1], info_list[2])
	    	if info_list[2] == "bd":
		    	bd_csv.create_CSV_FULL(info_list[0], info_list[1], info_list[2])

	    # part_lis = glob.glob("M2002/m06/pc")
	    # for part in part_lis:
	    # 	pc_csv.create_CSV_FULL("M2002","m06","pc",part)

	    # ********************************************************************
	    print("End : %s" % time.ctime())
	    print()

main()