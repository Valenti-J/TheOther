class CrewMember:

    def __init__(self,name,age,family,infect=False):
        self.name = name
        self.age = age
        self.family = family
        self.infect = infect

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_family(self):
        return self.family

    def get_infect(self):
        return self.infect

    def set_infect(self, desc):
        self.infect = desc


