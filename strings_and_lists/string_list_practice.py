words = "It's thanksgiving day. It's my birthday,too!"

print "string words: ", words

print "first instance of day in string words: ", words.find("day")

new_words = words.replace(" day.", " month.")

print "new string with month: ", new_words

x = [2, 54, -2, 7, 12, 98]
print "array x: ", x
print "min of array: ", min(x)
print "max of array: ", max(x)

x = ["hello", 2, 54, -2, 7, 12, 98, "world"]
print "array x: ", x
print "array with last and first indicies of array x: ", "[", x[:1], ",", x[len(x)-1:] , "]"

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x = sorted(x)
print "array x: ", x
print "list sorted: ", x

first_half_x = x[:len(x) / 2]
second_half_x = x[len(x) / 2:]
# for i in range(len(x)/2):
#     first_half_x[i] = x[i]

print "first half of array x: ", first_half_x
second_half_x.insert(0, first_half_x)
print "new array: ", second_half_x