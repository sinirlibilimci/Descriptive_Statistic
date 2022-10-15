# calculate t-tests in the dataset
from DS_Class2 import *
from DS_Class3 import *

class StatisticalTests:
    def __init__(self, a_list, b_list = None):
        self.descriptive_instance_a = DescriptiveStatistic(a_list)
        self.distribution_instance_a = DistributionStatistic(a_list)
        self.sorting_instance_a= Sorting(a_list)
        self.a_list = a_list

        self.b_list = b_list
        if self.b_list is not None:
            self.descriptive_instance_b = DescriptiveStatistic(b_list)
            self.distribution_instance_b = DistributionStatistic(b_list)
            self.sorting_instance_b = Sorting(b_list)        
            
    def t_test(self, one_sample = False, independent_samples = False, paired_sample = False):
        """Calculate different types t-test in the dataset. 
        
        t-test: Calculate whether there is a statistical difference between two different awerages. 

        Formula One Sample t-test = (Mean - µ)/(sd/len(n)**(1/2)) #  µ = theoretical value or population mean

        Formula Independent Samples t-test = (Mean1 - Mean2) / ( ( (S2) / n1) + ((S2) / n2) ) )**(1/2) 
        # S2 = (ss_1 + ss_2) / (n1 + n2 - 2)

        Formula Paired Sample t-test = (Mean)/(sd/len(n)**(1/2))

        Return: 
        't': Calculate formula

        """
        
        if  one_sample == True and independent_samples == False and paired_sample == False:
            mean = self.descriptive_instance_a.mean_func()
            sd = self.distribution_instance_a.sd_func()
            lf = self.sorting_instance_a.len_func()
            t = (mean - 0) / (sd / (lf**(1/2))) # theoretical value(µ) = 0
            return t

        elif independent_samples == True and self.b_list is not None and one_sample == False and paired_sample == False:
             mean_a_list = self.descriptive_instance_a.mean_func()
             mean_b_list = self.descriptive_instance_b.mean_func()

             lf_a_list = self.sorting_instance_a.len_func()
             lf_b_list = self.sorting_instance_b.len_func()

             formula_part_1 = mean_a_list - mean_b_list

             ss_a = self.distribution_instance_a.sum_of_square()
             ss_b = self.distribution_instance_b.sum_of_square()
             vr = (ss_a + ss_b) / (lf_a_list + lf_b_list - 2)

             formula_part_2 = ((vr / lf_a_list) + (vr / lf_b_list))**(1/2)

             t = formula_part_1/formula_part_2
             return t

        elif paired_sample == True and one_sample == False and independent_samples == False:
             mean = self.descriptive_instance_a.mean_func()
             sd = self.distribution_instance_a.sd_func()
             lf = self.sorting_instance_a.len_func()
             t = mean/(sd/(lf**(0.5)))
             return t

        else:
            print("You have entered wrong parameter values. Please check your parameters.")
            return 0








