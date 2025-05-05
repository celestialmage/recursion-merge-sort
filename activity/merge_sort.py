from .mergelib import merge_sorted
from math import ceil

# Implement merge_sort
# merge_sorted is a helper function that merges 2
# already sorted lists in linear time and space
# with respect to the combined lengths of the lists.

def merge_sort(data):
    data_length = len(data)

    if data_length == 1:
        return data
    else:
        split_by = ceil(data_length / 2)
        list1= merge_sort(data[:split_by])
        list2= merge_sort(data[split_by:])

        return merge_sorted(list1, list2)