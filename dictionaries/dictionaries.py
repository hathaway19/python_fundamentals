my_dict = {'Name': 'Justin', 'Age': 21, 'country_of_birth': 'USA', 'favorite_language': 'Java'}

# Prints all keys and values inside the dictionary
for key, value in my_dict.iteritems():
    print key, ":", value

print "My name is", my_dict["Name"]
print "My age is", my_dict["Age"]
print "My country of birth is the", my_dict["Age"]
print "My favorite language is", my_dict["favorite_language"]