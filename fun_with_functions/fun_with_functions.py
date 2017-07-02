# Goes through a range of values and prints whether each one is odd or even
def odd_even(min_val, max_val):
    for i in range(min_val, max_val + 1):
        odd_even = "odd"
        if i % 2 == 0:
            odd_even = "even"
        print "Number is ", i, ". This is an ", odd_even, "number."

# Goes throug each value in list and returns a list where each value has been multiplied by a certain number
def multiply(list, num_to_mult):
    for i in range(len(list)):
        list[i] *= num_to_mult
    return list

# Hacker challenge (return list with list of one's in each index of array from multiply)
def layered_multiples(arr):
    new_arr = []
    for i in range(len(arr)):
        temp_arr = []
        for j in range(1, arr[i] + 1):
            temp_arr.append(1)
        new_arr.append(temp_arr)
    return new_arr

# Test case for odd/even
odd_even(1, 2000)
# Test case for multiply function
a = [2,4,10,16]
b = multiply(a, 5)
print b
# Test case fo hacker challenge
x = layered_multiples(multiply([2,4,5], 3))
print x