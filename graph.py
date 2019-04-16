# this file only generates the graph, as the title shows
# the user won't be able to interact with the graph
# I'll write a seperate script for locating the defective parts

import seaborn as sns 
sns.set(color_codes=True)
import pandas as pd

save_folder = "/Users/bosen/Desktop/"

def generate_graph(file_path = "NULL"):
	
	print("Generating graph for files in folder: ", file_path)

####################################################################################
	# the codes within the hashtag is for test purposes
	mm_with_load = [0,1,2,3,4]
	mm_without_load = [10,20,6,2,1]
	data = [[mm_with_load[i],mm_without_load[i]] for i in range(len(mm_with_load))]
	df = pd.DataFrame(data, columns = ['mm_with_load', 'mm_without_load']) 
####################################################################################

####################################################################################
	# the codes are for implementation
	# NOTE:	the column name should be exactly the same as 
	# 		1). mm_with_load 		2). mm_without_load 	
	# Create the pandas DataFrame 
	# df = pd.read_csv("file_path")
####################################################################################

	ax = sns.regplot(x=df.mm_with_load, y=df.mm_without_load, color="b")
	fig = ax.get_figure()
	fig_name = "sample.png"
	fig.savefig(save_folder + fig_name)

	print("Finished! Files saved at: ", save_folder + fig_name)

# generate_graph()