# Part 1
print "********************************************* Part 1 ****************************************"

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

for dictionary in students:
    print dictionary["first_name"], dictionary["last_name"]

# Part 2
print "********************************************* Part 1 ****************************************"
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

print "Students"
# Go to first dictionary, students and go through all those dictionaries
for student in users["Students"]:
    length_of_name = len(student["first_name"]) + len(student["last_name"])
    print "1 -", student["first_name"], student["last_name"], "-", length_of_name
print "Instructors"
for teacher in users["Instructors"]:
    length_of_name = len(teacher["first_name"]) + len(teacher["last_name"])
    print "1 -", teacher["first_name"], teacher["last_name"], "-", length_of_name