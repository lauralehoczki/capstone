import cx_Oracle
import visualize_from_db as vis

# Authentication information for database connection
user = 'sysdba'
pw = 'oracle'
server = 'orc1'
hostname = 'j4m8888'
portnum = '1521'

# Establish connection to Oracle database
conn = cx_Oracle.connect(user,pw,hostname+':'+portnum+'/'+server, cx_Oracle.SYSDBA)

c = conn.cursor()

path = input("Drag and drop the csv to be uploaded to the database")
path_list = path.split('_')
table_name = path_list[2].upper()

try:
    file = open(path, 'r')

    f = file.readlines()
    file.close()

# Uncomment below code if you want to create new tables in the database for other machines
# might need revision if column names are 30+ characters long
"""   
query = "DESC "+module.upper()
        c.execute(query)
        result = c.fetchall()
        
if "ERROR" in result:
    query = "CREATE TABLE '''+module.upper()+'''
    for title in dfd_fields:
        		query += title + " VARCHAR(40),"
        	query += ")"
        	c.execute(query)
"""
for line in f:
    query = "INSERT INTO "+table_name+" VALUES(" +line+")"

c.execute(query)
c.close()

try:
	vis.visualize_data()
