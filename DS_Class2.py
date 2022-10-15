#DescriptiveStatistic = max, min, mode, median, mean
from DS_Class1 import Sorting
import pandas as pd
import numpy as np

class DescriptiveStatistic():

    def __init__(self, a_list): # parameter: a_list
        self.sorting_instance = Sorting(a_list) # Create object of Sorting class. # parameter : a_list
        self.a_list = a_list
   
    def max_value(self): # parameter: , a_list2 -> # different design
         """It gives the maximum value in the dataset.
        
         Return:
         'x': Maximum element in the list.

         """
         # DESIGN 2:
         #sorting_instance2 = Sorting(a_list2)
         
         #x2 = a_list2[0]
         #for i in range(sorting_instance2.len_func()):
         #    if a_list2[i] > x2:
         #        x2 = a_list2[i]

         #return x2

         # DESIGN 1:
         x = self.a_list[0] 
         for i in range(self.sorting_instance.len_func()): # Using object to call a function in the Sorting class
             if self.a_list[i] > x: 
                 x = self.a_list[i] 
         return x
   
    def min_value(self):
         """It gives minimum value in the dataset. 
         
         Return:
         'x': Minimum element in the list. 
         
         """
         x = self.a_list[0]
         for i in range(self.sorting_instance.len_func()):
             if self.a_list[i] < x:
                 x = self.a_list[i]
         return x
   
    def mode_func(self):
         """Calculate the maximum repeated value.
         
         Return:
         'mode_result': Mode of the dataset

         """
         mods = dict()
         for i in range(self.sorting_instance.len_func()):
             if self.a_list[i] in mods.keys():
                 mods[self.a_list[i]] += 1
             else:
                 mods[self.a_list[i]] = 1
   
         max_value = 0
         for k, v in mods.items():
             if v > max_value:
                 max_value = v
   
             if mods[k] == max_value:
                 mode_result = k
   
         return mode_result
   
    def median_func(self):
         """Calculate the median value in the sorted dataset.
         
         Return:
         'median_value': Median of the dataset.

         """
         
         #num = 0 # Second way on sorting of the values.
         #while num < len(self.a_list):
         #    num += 1
         #    for i in range(len(self.a_list) - 1):
         #        if self.a_list[i] > self.a_list[i + 1]:
         #           self.a_list[i], self.a_list[i + 1] = self.a_list[i + 1], self.a_list[i]

         self.sorting_instance.sorter()
       
         if len(self.a_list) %2 == 0:
             index1 = int((len(self.a_list)/2) - 1)
             index2 = int(len(self.a_list)/2)
             median_value = ((self.a_list[index1] + self.a_list[index2])/2)
         elif len(self.a_list) %2 == 1:
             index = int((len(self.a_list) - 1)/2)
             median_value = self.a_list[index]
         return median_value
     ############################################################################################
    def surekli_median():
        pass

    def mean_func(self, mtype = "arithmetic"):
        """Calculate the mean of the dataset.
        
        Return:
        'mean_value': Mean of the dataset.
        
        """
        if mtype == "arithmetic":
            sum_value = 0
            for _, e in enumerate(self.a_list):
                sum_value += e
                mean_value = (sum_value/len(self.a_list))
            return mean_value
        elif mtype == "weighted":


     ###################################################################################
    def weighted_mean():
        pass

    def harmonic_mean():
        pass

    def geometric_mean():
        pass

    def frequencies(self, if_df = False):
        """

        """
        if if_df == False:
            self.a_list = self.sorting_instance.sorter()

        frequency = dict()
        for i, x in enumerate(self.a_list):
            if x not in frequency.keys():
                frequency[x] = 1
            else:
                frequency[x] += 1

        relative_frequency = np.array(list(frequency.values()))/sum(frequency.values())

        cumulative_frequency = []
        n = 0
        for i, e in enumerate(frequency.values()):
            n += e
            cumulative_frequency.append(n)

        cr_frequency = []
        n = 0
        for  i, e in enumerate(relative_frequency):
            n += e
            cr_frequency.append(n)

        frequency_dict = {  "x": list(set(self.a_list)),
                            "frequency": frequency.values(),
                            "cumulative frequency": cumulative_frequency,
                            "relative frequency": relative_frequency, 
                            "cumulative relative frequency": cr_frequency
                          }
        frequency_df = pd.DataFrame(frequency_dict)
        frequency_table = frequency_df.to_string(index=False)
        
        return frequency_table

    def descriptives(self, other):
        """
        
        """ 
        table_dict = {"Datasets" : ["list1", "list2"],
                      "N" : [self.sorting_instance.len_func(), other.sorting_instance.len_func()],
                      "Range" : [f"{self.min_value()}-{self.max_value()}", f"{other.min_value()}-{other.max_value()}"],
                      "Mean" : [self.mean_func(), other.mean_func()],
                      "Median" : [self.median_func(), other.median_func()],
                      "Mode" : [self.mode_func(), other.mode_func()],
                      "SD" : [self.sd_func(), other.sd_func()]
                      }

        df_descriptives = pd.DataFrame(table_dict)
        descriptives_table = df_descriptives.to_string(index=False)

        return descriptives_table
    