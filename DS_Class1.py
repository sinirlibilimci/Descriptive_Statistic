#Sorter
class Sorting:
    def __init__(self, a_list):
        self.a_list = a_list #attribute name

    def len_func(self): #completed
        """Calculates the length of the instance attribute list.

        Return:
        'num' : Number of elements.       
        """
        num = 0
        for _ in self.a_list:
            num += 1
        return num

    def sorter(self, ascending = True): #completed
        """ 'Sorts the values in the attribute list from the smallest to the largest.' or 
        'In an ascending or descending order.'

        Parameters:
        'ascending': to determine which direction the sorting should be done (ascending or descending) (bool). 
        Default is 'True'. To sort in descending order, give 'False' as parameter value.

        Return:
        'a_list': Sorted attribute instance (list).
        """
        if ascending:
            num = 0
            while num < self.len_func():
                num += 1
                for i in range(self.len_func() - 1):
                    if self.a_list[i] > self.a_list[i + 1]:
                       self.a_list[i], self.a_list[i + 1] = self.a_list[i + 1], self.a_list[i]
        else: 
            num = 0
            while num < self.len_func():
                num += 1
                for i in range(self.len_func(self.a_list) - 1):
                    if self.a_list[i] < self.a_list[i + 1]:
                       self.a_list[i], self.a_list[i + 1] = self.a_list[i + 1], self.a_list[i]
        return self.a_list

    def fantastic_sorter(self, ascending = True): #completed
        """Categorizing odd - even values and in an ascending or descending order.
              
        Parameters:
        'ascending': to determine which direction the sorting should be done (ascending or descending) (bool).
        Default is 'True'. To sort in descending order, give 'False' as parameter value.

        Return:
        'a_list': Sorted attribute instance (list).
        """
        if ascending == True:
            num = 0
            while num < self.len_func():
                for i in range(self.len_func() - 1):
                    if self.a_list[i] %2 == 1 and self.a_list[i + 1] %2 == 1:
                        if self.a_list[i] > self.a_list[i + 1]:
                           self.a_list[i], self.a_list[i + 1] =  self.a_list[i + 1], self.a_list[i]

                    elif self.a_list[i] %2 == 0 and self.a_list[i + 1] %2 == 0:
                        if  self.a_list[i] > self.a_list[i + 1]:
                            self.a_list[i], self.a_list[i + 1] =  self.a_list[i + 1], self.a_list[i]

                    elif self.a_list[i] %2 == 1 and self.a_list[i + 1] %2 == 0:
                        continue

                    elif self.a_list[i] %2 == 0 and self.a_list[i + 1] %2 == 1:
                         self.a_list[i], self.a_list[i + 1] =  self.a_list[i + 1], self.a_list[i]

                num += 1
        else:
            num = 0
            while num < self.len_func():
                for i in range(self.len_func() - 1):
                    if self.a_list[i] %2 == 0 and self.a_list[i + 1] %2 == 0:
                        if self.a_list[i] < self.a_list[i + 1]:
                           self.a_list[i], self.a_list[i + 1] =  self.a_list[i + 1], self.a_list[i]

                    elif self.a_list[i] %2 == 1 and self.a_list[i + 1] %2 == 1:
                        if  self.a_list[i] < self.a_list[i + 1]:
                            self.a_list[i], self.a_list[i + 1] =  self.a_list[i + 1], self.a_list[i]

                    elif self.a_list[i] %2 == 0 and self.a_list[i + 1] %2 == 1:
                        continue

                    elif self.a_list[i] %2 == 1 and self.a_list[i + 1] %2 == 0:
                         self.a_list[i], self.a_list[i + 1] =  self.a_list[i + 1], self.a_list[i]

                num += 1
        return self.a_list

    def sorter_algorithm(self, sorter_type = "asc"): #completed
        """Values sorted in an ascending or descending order to see the 'Recursive' structure. Can be 'print' choice.
         
        Parameter:
        'sorter_type': to determine which direction the sorting should be done. (ascending or descending) (bool creating)
        Default is 'asc'. To sort descending order, give 'desc' as parameter value.
        
        Return:
        'a_list': Sorting attribute instance (list).
        """
        if  sorter_type == "asc":
            num = 0
            while num < self.len_func():
                num += 1
                for i, _ in enumerate(self.a_list):
                    if i == len(self.a_list) - 1:
                        break

                    if self.a_list[i] > self.a_list[i + 1]:
                       self.a_list[i], self.a_list[i + 1] = self.a_list[i + 1], self.a_list[i]
        elif sorter_type == "desc":
            num = 0
            while num < self.len_func():
                num += 1
                for i, _ in enumerate(self.a_list):
                    if i == len(self._list) - 1:
                         break
                    if self.a_list[i] < self.a_list[i + 1]:
                       self.a_list[i], self.a_list[i + 1] = self.a_list[i + 1], self.a_list[i]

        else:
            print("Wrong keyword argument! Showing result as ascending by default.")
            self.a_list = self.sorter_algorithm(self.a_list, sorter_type = "asc") # recursive

        return self.a_list

