import matplotlib.pyplot as plt
import pandas as pd
from DS_Class3 import *
from DS_Class1 import *

class VisualizeStatistics(DistributionStatistic):
    def __init__(self, a_list):
        self.sorting_instance = Sorting(a_list)
        self.a_list = self.sorting_instance.sorter()
        super().__init__(self.a_list)

    def visualize_basic_descriptives(self, vis_mean = False, vis_median = False, vis_mode = False):
        
        plt.plot(self.a_list, range(len(self.a_list)))
        if vis_mean == True:
            plt.axvline(self.mean_func(), label = "mean", color = "black") #vertical = axvline, horizontal = axhline

        if vis_median == True:
            plt.axvline(self.median_func(), label = "median", color = "grey")

        if vis_mode == True:
            plt.axvline(self.mode_func(), label = "mode", color = "brown")

        plt.legend(loc = "upper left")
        plt.grid(axis = "y", color = "grey", linewidth = 0.5, linestyle = "--")
        plt.xlabel("data")
        plt.ylabel("indexes")

        plt.show()

    def visualize_normal_distribution(self):       
        plt.plot(self.standardization(), self.nd_func(), "o", linestyle = "-", color = "purple")
        plt.show()

    def visualize_data_and_distribution(self):
        fig, ax = plt.subplots(1, 2)
        fig.suptitle("Descriptive and Distribution Statistics")
        ax[0].plot(self.a_list)
        ax[0].axhline(self.mean_func(), label = "Mean", color = "black")
        ax[0].axhline(self.median_func(), label = "Median", color = "grey")
        ax[0].axhline(self.mode_func(), label = "Mode", color = "brown")
        ax[0].grid(axis = "x", color = "grey", linewidth = 0.5, linestyle = "--")
        ax[0].legend(title = "Central Tendency", loc = "upper left")
        ax[1].plot(self.standardization(), self.nd_func(), "o", linestyle = "-", color = "purple", label = "Normal\nDistribution")
        ax[1].legend(loc = "upper right")
        plt.show()

    #fig, (ax1, ax2) = plt.subplot(2)
    #fig.suptitle("Descriptive and Distribution Statistic")
    #ax1.plot()
    #ax2.plot()
    #plt.show()
# mean-median-mode visualization
#import matplotlib.pyplot as plt

# data visual
#plt.plot(num_list_data, "o", color = "green")f4dv

## median visual
##x_axis = (0, len(num_list_data))
##y_axis = (median_func(num_list_data), median_func(num_list_data))
##plt.plot(x_axis, y_axis, "red")
#plt.axhline(median_func(num_list_data), color = "blue", linestyle = ":", label = f"median = {median_func(num_list_data)}")

## mean visual
##plt.plot(x_axis, (mean_func(num_list_data), mean_func(num_list_data)), "-", color = "yellow")
#plt.axhline(mean_func(num_list_data), color = "red", linestyle = "--", label = f"mean = {mean_func(num_list_data)}")

##mode visual
#plt.axhline(mode_func(num_list_data), color = "pink", linestyle = "-", label = f"mode = {mode_func(num_list_data)}")

## label visual => legend
#plt.legend(loc = "upper right")

## show visuals all together
#plt.show()

###############################################################

#num_list_data_sorted = sorter(num_list_data)
#plt.plot(standardization(num_list_data_sorted), nd_func(num_list_data_sorted), "o", linestyle = "-", color = "orange")
#plt.grid(which = "major", axis = "both", color = "purple", linestyle = "--", linewidth = 1.5) 
#plt.grid(which = "minor", axis = "x", color = "black", linestyle = ":", linewidth = 0.8)
#plt.grid(which = "minor", axis = "y", color = "black", linestyle = ":", linewidth = 0.8)
#plt.minorticks_on()
#plt.xlabel("Standardization", color = "black")
#plt.ylabel("Normal Distribution", color = "black")
#plt.show()


#scatter??
#colormap

