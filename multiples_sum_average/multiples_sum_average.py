#Part 1: Print all odd numbers from 1 to 1000
print" *************************** PART 1 ******************************"
print "printing all odd numbers from 1 to 1000"
for i in range(1,1000):
    if i % 2 == 1:
        print i,

print ""
print" *************************** PART 2 ******************************"
print "printing all multiples of 5 from 5 to 1,000,000"
#Part 2: Prints all multiples of 5 from 5 to 1,000,000
for i in range(5, 1000005):
    if i % 5 == 0:
        print i,

print ""
print " *************************** PART 3 ******************************"
print "prints the sum of all values in the list, a = [1, 2, 5, 10, 255, 3]"
#prints the sum of all values in the list, a = [1, 2, 5, 10, 255, 3]
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in range(len(a)):
    sum += a[i]
print "total sum of list a is: ", sum

print ""
print" *************************** PART 4 ******************************"
print "prints average of list, a = [1, 2, 5, 10, 255, 3]"
# Uses sum value up above
average = sum / len(a)
print "average of list a is : ", average