from test_cases import *
from DS_Class1 import *

def stem_leaf_table(a_list):
    stem_dict = dict()
    sorter_list_instance = Sorting(a_list)
    sorter_list = sorter_list_instance.sorter()

    for i, e in enumerate(sorter_list):
        stem = int(e / 100)
        leaf = e - (stem*100)
        
        if stem not in stem_dict:
            stem_dict[stem] = []
            stem_dict[stem].append(leaf)
        else:
            stem_dict[stem].append(leaf)
    
    for k, v in stem_dict.items():
        print(f"{k}:{v}\n")

    return stem_dict

print("List:\n", pd.DataFrame(question_num_list, columns = ['Question Num List']))
print(stem_leaf_table(question_num_list))