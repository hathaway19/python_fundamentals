# Draws number of stars in each index of array
def draw_stars(arr):
    for i in range(len(arr)):
        # Prints * if integer
        if isinstance(arr[i], int):
            for j in range(arr[i] - 1):
                print "*",
            print "*"
        # Prints first letter if string
        elif isinstance(arr[i], str):
            for j in range(len(arr[i])):
                print arr[i][0],
            print arr[i][0]
        
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
print x
draw_stars(x)