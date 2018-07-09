# Name: Eliza Thornton
# Date: 7-9-2018

# proj01: A Simple Program

# Part I:
# This program asks the user for his/her name and grade.
#Then, it prints out a sentence that says the number of years until they graduate.
name = raw_input("Enter your name: ")
grade = raw_input("Enter your grade: ")
name = name[0].upper() + name[1:len(name)].lower()
if grade == 12:
    print str(name) + ", you will graduate high school in 1 year!"
#so it doesn't say "you'll graduate in 1 years!"
elif int(grade) > 12 or int(grade) < 1:
    print "That's not a valid grade."
#grade has to be between 1 and 12
else:
    print str(name) + ", you will graduate high school in " + str(13 - int(grade)) + " years!"

# Part II:
# This program asks the user for his/her name and birth month.
# Then, it prints a sentence that says the number of days and months until their birthday
import datetime
birth_month = int(raw_input("What's your birth month? (The number please): "))
birth_day = int(raw_input("What's your birth date? "))
d = datetime.date.today()
current_month = d.month
current_day = d.day
#now the program checks the actual date and returns it (mostly) accurately!
if birth_month >= current_month:
    months_till_bday = birth_month - current_month
else:
    months_till_bday = (birth_month + 12) - current_month
if birth_day >= current_day:
    days_till_bday = birth_day - current_day
else:
    days_till_bday = (30 + birth_day) - current_day
    months_till_bday -= 1
print "You have " + str(months_till_bday) + " months and " + str(days_till_bday) + " days until your birthday!"

age = int(raw_input("How old are you? "))
if age < 13:
    print "You can see G and PG movies."
elif age >= 13 and age < 17:
    print "You can see G, PG, and PG-13 movies."
else:
    print "You can see G, PG, PG-13, and R movies."
# If you complete extensions, describe your extensions here!

# Part I: made the first (or 0th) item in the name string uppercase while everything else
#(i.e. from index 1 to the length of the string) is lowercase so it looks nice
# also added an if/then statement to avoid grades higher than 12 and lower than 1
# also changed 12th grade to say "1 year" instead of "1 years"
