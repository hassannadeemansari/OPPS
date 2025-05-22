class requirementforjob():
    def __init__(self , name , age , position):
        self.name = name
        self.age = age
        self.position = position

    def Check_eligibility(self):
        if self.age < 18:
            return "you are under age !!!"
        if self.position in ["developer" , "designer"]:
            return "you are able to work with us...."
        else:
            return "your are not able for the job"


NewPerson = requirementforjob("hassan", 19, "developer")
print(NewPerson.Check_eligibility())

