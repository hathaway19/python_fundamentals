def filter_by_type(val):
    print "The current value is: ", val
    # Check to see if value is integer
    if isinstance(val, int):
        print "The value is an integer!"
        if(val >= 100):
            print "That's a big number!"
        else:
            print "That's a small number"

    # Check to see if value is a string
    if isinstance(val, str):
        print "The value is a string!"
        if len(val) >= 50:
            print "Long Sentence"
        else:
            print "Short Sentence"

    # Check to see if value is a list
    if isinstance(val, list):
        print "The value is a list!"
        if len(val) >= 10:
            print "Big list!"
        else:
            print "Short list."

sI = 45
filter_by_type(sI)
mI = 100
filter_by_type(mI)
bI = 455
filter_by_type(bI)
eI = 0
filter_by_type(eI)
spI = -23
filter_by_type(spI)
sS = "Rubber baby buggy bumpers"
filter_by_type(sS)
mS = "Experience is simply the name we give our mistakes"
filter_by_type(mS)
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
filter_by_type(bS)
eS = ""
filter_by_type(eS)
aL = [1,7,4,21]
filter_by_type(aL)
mL = [3,5,7,34,3,2,113,65,8,89]
filter_by_type(mL)
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
filter_by_type(lL)
eL = []
filter_by_type(eL)
spL = ['name','address','phone number','social security number']
filter_by_type(spL)