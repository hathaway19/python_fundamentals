# prints values of list that contain a specific character
def find_characters(char, list):
    # new list to add strings to
    new_list = []
    # Checks each string in list for the specific character, adds if found
    for string in list:
        if char in string:
            new_list.append(string)
    print new_list

# Test Case 1
print "***************************** Test Case 1 ************************************"
word_list = ['hello','world','my','name','is','Anna']
char_1 = 'o'
find_characters(char_1, word_list)