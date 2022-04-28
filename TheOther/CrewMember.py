class CrewMember:

    def __init__(self,name,age,family,infected=False):
        self.name = name
        self.age = age
        self.family = family
        self.infect = infected

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_family(self):
        return self.family

    def get_infected(self):
        return self.infected


