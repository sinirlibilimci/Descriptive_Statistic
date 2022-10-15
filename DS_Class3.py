#inheritance !!
#DistributionStatistic = sd, var, z-score, standardization, normal distribution
from math import pi, e
from DS_Class2 import DescriptiveStatistic
import numpy as np
import pandas as pd

class DistributionStatistic(DescriptiveStatistic):

    def __init__(self, a_list):
        super().__init__(a_list)
        self.a_list = a_list

    def variance_func(self):
        """Calculate the standard deviation of the dataset.
       
        Variance: The mean of the square of the distance from the mean of each value. 
        Formula =  Σ((X - Mean)^2)/(n - 1)
        
        Return:
        'variance': Variance value of the dataset.

        """
        mean = self.mean_func()
        vr = 0
        for i in range(len(self.a_list)):
            sub = self.a_list[i] - mean
            square = pow(sub, 2)
            vr += square # Sum of Squares (SS)
        
        variance = vr / (len(self.a_list) - 1)
        return variance
    
    def sd_func(self):
        """Calculate the standard deviation of the dataset.
        
        Standard deviation: The average of the euclidean 
        distances of the values from the mean of the dataset.
        Formula = ( Σ((X - Mean)^2)/(n - 1) )^(1/2)
        
        Return:
        'sd': Standard deviation

        """
        #mean = self.mean_func(self.a_list) # Second way on the calculation of variance.
        #ss2 = 0
        #for i in range(len(self.a_list)):
        #    sub = self.a_list[i] - mean 
        #    ss1 = pow(sub, 2) 
        #    ss2 += ss1 
        
        #variance = ss2 / (len(self.a_list) - 1) 
        
        variance = self.variance_func() 
        sd = variance**(1/2) 
        
        return sd
    
    def z_score_func(self, val):
        """Calculate z_score of the spesific value.
        
        Parameter: 
        'val': A value in the dataset.
        
        z-score: Subtract mean from the each value and divided by the standard deviation.
        Formula = (X - Mean) / sd

        Return:
        'result': z-score of the value.
        
        """
        if val in self.a_list: 
             mean = self.mean_func()
             sd = self.sd_func()
             sub = (val - mean)
             try: 
                result = sub/sd
             except:
                print("not calculate!")
 
        else: 
            print("no data!")

        return result

    def standardization(self): # normalization
        """Calculate standardization of the data distribution.
       
        Standardization: Find the z-scores of each value in the dataset.
        Formula = (X - Mean) / sd

        Return:
        'standard_list': z-scores of each data. (list)

        """
        standard_list = [] 
        for i in range(len(self.a_list)):
            #mean = self.mean_func(self.a_list) # Second way the standardization calculation.
            #sd = self.sd_func(self.a_list)
            #result = (self.a_list[i] - mean)/sd
            #standard_list.append(result)
            zs = self.z_score_func(self.a_list[i])
            standard_list.append(zs)

        return standard_list
    
    def nd_func(self):
        """Probability Density Function.
       
        Formula = (1 / (sd*sqrt(2pi)))*( e**(-0.5*(z**2)) )

        Return:
        'nd_list': Normal distribution probability values. (list)
       
        """ 
        nd_list = []
        for i in range(len(self.a_list)):
            f1 = 1/(self.sd_func()*((2*pi)**(1/2))) 
            f2 = e**(-0.5*(self.z_score_func(self.a_list[i])**2))
            formula = f1 * f2 
            nd_list.append(formula) 
        
        return nd_list

    def sum_of_square(self):
        ss = 0
        for el in self.a_list:
            part1 = el - self.mean_func()
            part2 = pow(part1, 2)
            ss += part2

        return ss

    

