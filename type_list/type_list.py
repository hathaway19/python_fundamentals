def type_list(my_list):
    # variable to hold sum of floats and integers
    sum_of_ints = 0
    # variable to hold concatenated string
    new_string = ""
    # bool to keep track of whether it's a mixed string
    mixed_list = False

    print "my list: ", my_list
    # Checks first index to see which type it is
    type_to_look_for = int
    if isinstance(my_list[0], str):
        type_to_look_for = str
    elif isinstance(my_list[0], float):
        type_to_look_for = float

    # Goes through rest of list
    for i in my_list:
        # if index has different type, it's a mixed list
        if not isinstance(i, type_to_look_for):
            mixed_list = True
        # add to sum if integer or float
        if isinstance(i, int) or isinstance(i, float):
            sum_of_ints += i
        # if string, add to new string
        else:
            new_string += i + " "

    # print results
    if mixed_list:
        print "The array you entered is of mixed type"
    else:
        print "The array you entered is of type ", type_to_look_for

    print "the sum of ints in list is: ", sum_of_ints
    print "the concatenated string is: ", new_string

# Test 1
print "*************************** Test 1 *************************************"
my_list2 = [4 , 23]
type_list(my_list2)

# Test 2
print "*************************** Test 2 *************************************"
list_1 = [2,3,1,7,4,12]
type_list(list_1)
# Test 3
print "*************************** Test 3 *************************************"
list_1 = ['magical unicorns',19,'hello',98.98,'world']
type_list(list_1)
# Test 4
print "*************************** Test 4 *************************************"
list_1 = ['magical','unicorns']
type_list(list_1)