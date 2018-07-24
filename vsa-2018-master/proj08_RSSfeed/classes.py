class Dude(object):
    # methods

    #initializr
    def __init__(self, name, age):
        #storing attributes
        self.name = name
        self.age = age
        self.living = True
        # assuming living is True, but can be changed to False later


    #moar non-initilization methods
    def update_age(self):
        self.age += 1

    # accessor method

    def get_age(self):
        return self.age

    def kill(self):
        if self.living is True:
            self.living = False
            return "You just killed %s. You monster." % self.name
        else:
            return "You can't kill something that's already dead!"


class Student(Dude):
    def set_grade(self, grade):
        self.grade = grade

    def years_until_graduate(self):
        return 13 - self.grade

manman = Dude("ManMan", 19)
print manman.kill