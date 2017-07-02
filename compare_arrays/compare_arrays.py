def compare_two_lists(list_1, list_2):
    # variable to keep track if list is so far equal
    equal = True
    if len(list_1) == len(list_2):
        # Checks each index of both arrays with each other
        for i in range(0, len(list_1)):
            # If not equal break since we don't need to continue
            if list_1[i] != list_2[i]:
                print "The array's values are not equal"
                equal = False
                break
        if equal:
            print "The two arrays are identical!"
    # If not equal length, they can't be identical
    else:
        print "The arrays aren't equal since they have different lengths."

# Test Case 2
print "****************************** Test 2 *********************************"
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
print "list 1: ", list_one, " list 2: ", list_two
compare_two_lists(list_one, list_two)

# Test Case 2
print "****************************** Test 2 *********************************"
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
print "list 1: ", list_one, " list 2: ", list_two
compare_two_lists(list_one, list_two)

# Test Case 3
print "****************************** Test 3 *********************************"
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
print "list 1: ", list_one, " list 2: ", list_two
compare_two_lists(list_one, list_two)

# Test Case 4
print "****************************** Test 4 *********************************"
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
print "list 1: ", list_one, " list 2: ", list_two
compare_two_lists(list_one, list_two)