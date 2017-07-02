import random

def generate_rnd_score(num_grades):
    # Generates number of scores needed
    for i in range(num_grades):
        # default of D
        letter_grade = 'D'
        # generates random int between 60 and 100
        rnd_score = random.randrange(60,100)
        # Gives letter score based on range
        if rnd_score >= 90:
            letter_grade = 'A'
        elif rnd_score >= 80:
            letter_grade = 'B'
        elif rnd_score >= 70:
            letter_grade = 'C'
        print "Score: ", rnd_score, "; Your grade is ", letter_grade 

generate_rnd_score(10)