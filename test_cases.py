import numpy as np
import pandas as pd

#Test Data
num_list_data = [1, 4, 9, 15, 33, 22, 16, 8, 10, 23, 15, 29, 3, 5, 7, 9, 17, 13, 16, 9, 12] #calculate mod & frequency & probability distribution
num_list = [1, 5, 2, 21, 13, 8, 17, 6, 19, 15, 4, 14, 7, 12, 11, 9]
question_num_list = [105, 108, 124, 213, 437, 265, 173, 329, 381, 496, 149, 292, 238, 351, 307]

#Test Data from file
df_data = pd.read_csv("Data.csv")
list1 = df_data["list1"]
list2 = df_data["list2"]

for i in range(len(list2)):
    if list2[i] == 0:
        list2.pop(i)


#Random data



#Random normal data



