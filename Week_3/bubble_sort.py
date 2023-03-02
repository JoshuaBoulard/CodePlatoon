#takes in a set
#has to an index, and compare it to the value before
#if less than prev value, swap, else move to next index
#if they swap, restart at beginning of set, move again one index at a time
#continues until it is out of range of the set length 
#all values should be re ordered


def bubble_sort(set_to_sort):

    count = 1
    current = 0
    prev = 0

    while count < len(set_to_sort):
        print(set_to_sort)
        if set_to_sort[count] > set_to_sort[count - 1]:
            count += 1
        else:
            prev = set_to_sort[count - 1]
            current = set_to_sort[count]
            set_to_sort[count] = prev
            set_to_sort[count-1] = current
            count = 1
    return set_to_sort



test_list = [4,5,2,1,0,3] 
test_list2 = [4, 3, 5, 0, 1]
print(bubble_sort(test_list2))