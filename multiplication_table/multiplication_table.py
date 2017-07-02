def print_multiplication_table(number):
    print "x ",

    # Print the number of values we want in table
    for i in range(1, number):
        print i,
    print number

    # Go through each row
    for i in range(1, number + 1):
        print i, " ",
        # Go through each col
        for j in range(1, number):
            print j * i, 
        print number * i

print_multiplication_table(14)