def print_checkerboard(rows, cols):
    # goes through each row
    for i in range(rows):
        # If it's an even row, offset
        if i % 2 == 0:
            print " ",
        # prints stars on same line untill last star
        for i in range(cols - 1):
            print " *",
        print " *"

print_checkerboard(4, 8)
