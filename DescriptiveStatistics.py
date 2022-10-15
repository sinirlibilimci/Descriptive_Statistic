########################################################################
######################## Fundamental Statistics ########################
########################################################################

# frequency table -> pandas (maybe, maybe not) +
# probability distribution +
# mean +
# median +
# mode +
# min value +
# max value +
# z-score calculation of a single value +
# standardization (!) + 
# variance +
# standard deviation + 
# mean-median-mode visualization +
# visualization of normal distribution +
# t-test statistics of independent samples (without any module) +

from Settings import *
from test_cases import *
from DS_Class3 import DistributionStatistic
from DS_Class4 import StatisticalTests
from visualization import VisualizeStatistics

# data instances
desc_list1_instance = DistributionStatistic(list1)
desc_list2_instance = DistributionStatistic(list2)

# frequencies
fr_list1 = desc_list1_instance.frequencies()
fr_list2 = desc_list2_instance.frequencies()
print("Frequency Table List1:\n", fr_list1)
print("Frequency Table List2:\n", fr_list2)

# descriptives
descriptives_table = desc_list1_instance.descriptives(desc_list2_instance)
print("Descriptive Statistic:\n", descriptives_table)

# t-test
t_test_instance = StatisticalTests(list1, list2)
t_independent = t_test_instance.t_test(independent_samples=True)
print("\nIndependent Samples t_test: ", t_independent)

desc_sta = VisualizeStatistics(list1)
#desc_sta.visualize_basic_descriptives(vis_mean = True, vis_median = True, vis_mode = True)
#desc_sta.visualize_normal_distribution()
desc_sta.visualize_data_and_distribution()
