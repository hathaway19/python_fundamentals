my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

# Array to hold tuples
my_tuples = []
# Go through every key and store key and value in tuple
for key, value in my_dict.iteritems():
    a_tuple = (key, value)
    # add to array
    my_tuples.append(a_tuple)
print my_tuples
    