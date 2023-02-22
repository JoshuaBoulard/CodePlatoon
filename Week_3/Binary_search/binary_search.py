
import math
import random

def binary_search(num, list_to_check):
    split = math.floor(len(list_to_check) / 2)
    middle_value = list_to_check[split]
    print(middle_value)
    count = 0

    if num == middle_value:
        return f'Found: {num} at index {count}'
    elif len(list_to_check) == 1:
        return -1
    elif num > middle_value:
        count += split
        return count + binary_search(num, list_to_check[split:])
    elif num < middle_value:
        count -= split
        return count + binary_search(num, list_to_check[:split])
       
    



values = random.sample(list(range(1,10000)), 1000)
values.sort() # We now have a sorted list of 1000 unique values between 1 and 10,000

print(binary_search(537, values)) # this returns the index of 537 in values if it exists and -1 if it doesn't exist


#Here's the basic premise of the algorithm:

#Say you're searching for a value number_to_find in a search set of sorted_values
#Find the middle value in sorted_values we'll call middle_value
#If number_to_find is equal to middle_value then your target is found
#If number_to_find is less than middle_value, split your sorted_values in half and repeat the algorithm on your new subset (the half of sorted_values before middle_value)
#If number_to_find is greater than middle_value, repeat step but with the half of sorted_values valuesaftermiddle_value`
#Repeat until you find number_to_find or return -1 if it doesn't exist#

def binary_search(search_value, lst):
    start_index = 0
    end_index = len(lst) - 1

    while start_index < end_index:
        middle_index = start_index + (end_index - start_index) // 2
        middle_value = lst[middle_index]
        if middle_value == search_value:
            return middle_value
        elif middle_value < search_value:
            start_index = middle_index + 1
        elif middle_value > search_value:
            end_index = middle_index

    return -1