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
	    # create_CSV_FULL("M1998","m052","pc","888878")
	    # create_CSV_FULL("M1998","m052","pc","950273")
	    time.sleep(2)
	    print("End : %s" % time.ctime())
	    print()

main()