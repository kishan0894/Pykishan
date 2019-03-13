import random
import time
import operator
import copy

class Sorting:

    def __init__(self):
        return None

    def bubble_sort(self,list):
        """Bubble Sort"""
        for i in range(len(list)):
            for j in range(0,len(list)-i-1):
                if(list[j] > list[j+1]):
                    list[j],list[j+1] = list[j+1],list[j]
        return list

    def insertion_sort(self,list):
        """Insertion Sort"""
        for i in range(1,len(list)):
            key = list[i]
            j = i-1
            while(j >= 0 and list[j] > key):
                list[j+1] = list[j]
                j=j-1
            list[j+1] = key
        return list

    def insertion_sort(self,list):
        """Insertion Sort"""
        i = 0
        while(i < len(list)):
            j = i
            while(j > 0 and (list[j-1] > list[j])):
                list[j],list[j-1] = list[j-1],list[j]
                j = j - 1
            i = i + 1
        return list

    def quick_sort(self,list):
        """"Quick Sort"""
        self.qsort(list)

    def qsort(self,list):
        """Quick sort implementation"""
        if not list:
            return []
        else:
            pivot = list[0]
            less = [x for x in list     if x <  pivot]
            more = [x for x in list[1:] if x >= pivot]
            return self.qsort(less) + [pivot] + self.qsort(more)

    def randomized_quick_sort(self,list):
        self.r_quick_sort(list)

    def r_quick_sort(self,list):
        if not list:
            return []
        else:
            pivot = random.choice(list)
            less = [x for x in list  if x < pivot]
            pivot_eq = [x for x in list  if x == pivot]
            more = [x for x in list  if x > pivot]
            return self.r_quick_sort(less) + pivot_eq + self.r_quick_sort(more)

    def merge_sort(self,list):
        self._merge_sort(list,compare=operator.lt)

    def _merge_sort(self,list,compare):
        if (len(list) < 2):
            return list[:]
        else:

            middle = int(len(list)/2)
            left =self._merge_sort(list[:middle],compare)
            right = self._merge_sort(list[middle:],compare)
            return self.merge(left,right,compare)


    def merge(self,left,right,compare):
        result = []
        i,j = 0,0

        while(i < len(left) and j < len(right)):
            if(compare(left[i],right[j])):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1
        return result


if __name__ == "__main__":

    obj = Sorting()
    input_list = random.sample(range(0,1000),7)

    cpy_input_list = copy.copy(input_list)
    obj.bubble_sort(cpy_input_list)

    cpy_input_list = copy.copy(input_list)
    obj.insertion_sort(cpy_input_list)

    cpy_input_list = copy.copy(input_list)
    obj.quick_sort(cpy_input_list)

    cpy_input_list = copy.copy(input_list)
    obj.randomized_quick_sort(cpy_input_list)

    cpy_input_list = copy.copy(input_list)
    obj.merge_sort(cpy_input_list)