def print_prime_square(min_val, max_val):
    # Go through the range of numbers
    for num in range(min_val, max_val + 1):
        # Goes through all numbers less than current number
        for divide_num in range(2, num):
            # Sees if it's a perfect square
            if num == (divide_num * divide_num):
                print "Bar",
                break
            # Sees if it's not a prime number
            elif num % divide_num == 0:
                break
        # If still here, it's a prime number
        else:
            print "Foo", 
print_prime_square(100, 10000)