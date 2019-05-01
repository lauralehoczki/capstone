"""
This program enables the user to graph the offset from selected csv's instead of pulling
all new data from the database
WARNING: This method is significantly slower then the database method
"""
import glob, os
import seaborn as sns 
sns.set(color_codes=True)
import pandas as pd

save_folder = "C:\\Users\\supplier_admin\\Desktop\\Analysis\\"
DATA_PATH = "C:\\Users\\supplier_admin\\Desktop\\CSV\\"

def generate_graph():
    part_type = input("Part type to run correlation on: ")
    m052_path = DATA_PATH + "M1998_06_" + part_type + ".csv"
    m04_path = DATA_PATH + "M2002_04_" + part_type + ".csv"
    m06_path = DATA_PATH + "M1998_06_" + part_type + ".csv"
    if os.path.isfile(os.path.join(path, m04_path)) and 
    os.path.isfile(os.path.join(path, m06_path)) and os.path.isfile(os.path.join(path, m052_path)):
        m04file = open(m04path, 'r')
        m06file = open(m06path, 'r')
        m052fle = open(m052path, 'r')
        
        m04 = m04file.readlines()
        m06 = m06file.readlines()
        m052 = m052file.readlines()

        m04file.close()
        m06file.close()
        m052file.close()

        mm_with_load = []
        mm_without_load = []
        
        # Create a dictionary and match the M052 batch numbers with M06 batch numbers
        match_batch_nums = {}
        for line in m04:
            row = line.split(',').remove('\n')
            match_batch_nums[m04[11]] = m04[17]
            
        
        for line in m052:
            row1 = line.split(',').remove('\n')
            # The batch number of the record is at position 18, find it in the dictionary
            m06_part = match_batch_nums.get(row1[18])
            # The value we're interested in, "Quality Measuring MM after joining without load"
            # is at position 100 in the list, append it to the data to be graphed
            mm_without_load.append(row1[100])
            
            # Also iterate through m06 at the same time and 
            for li in m06:
                row2 = li.split(',').remove('\n')
                
                # Batch number is at position 17 in m06, if it matches with the one
                # we're looking for, get the metric to be graphed
                if row2[17] == m06_part:
                    # The value we're interested in, "P_Offset_A_1st_run"
                    # is at position 56 in the list, append it to the data to be graphed
                    mm_with_load.append(row2[56])
        
        data = [[mm_with_load[i],mm_without_load[i]] for i in range(len(mm_with_load))]
        df = pd.DataFrame(data, columns = ['mm_with_load', 'mm_without_load']) 

        ax = sns.regplot(x=df.mm_with_load, y=df.mm_without_load, color="b")
        fig = ax.get_figure()
        
        # The filename is going to be the time it was created
        currentDT = datetime.datetime.now()
        fig_name = currentDT.strftime("%H:%M:%S")
        fig.savefig(save_folder + fig_name + ".png")
    else:
        print("This part type has insufficient data")
    
generate_graph()