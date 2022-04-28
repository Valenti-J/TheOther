from CrewMember import *

class Death:

    def __init__(self, crew, infected, cause):
        self.crew = crew
        self.infected = infected
        self.cause = cause


    def create_string(self):
        script = []
        script.append("You killed %s." % (self.crew.get_name()));
        if type(self.crew.get_family()) == str:
            script.append("They were your own %s." % self.crew.get_family())
        if self.crew.get_age() < 18:
            script.append("They were only %s years old." % (self.crew.get_age()))
        else:
            script.append("They were %s years old." % (self.crew.get_age()))
        if self.infected:
            script.append("They may have been infected.")
            script.append("So I hope you take solace in knowing that when you remember...")
        script.append("You killed them %s." % (self.cause))

        return script