from CrewMember import *
import random

class Death:

    def __init__(self, crew, infected, cause):
        self.crew = crew
        self.infected = infected
        self.cause = cause


    def create_guilt(self):
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

    def create_memory1(self):
        script = []

        clothes = ["suit","dress","flannel and jeans","t-shirt and shorts"]

        if self.crew.get_age() < 18:
            age = "Young"
        else:
            age = "Old"

        script.append("You open your eyes.")
        script.append("Something feels weird about all this.")
        if age == "Young":
            script.append("The world feels larger than usual.")
        script.append("You hear a voice call out to you.")
        script.append("\"There you are %s.\" They say." % (self.crew.get_name()))
        script.append("Wait, that isn't your name...")
        script.append("You see a person smiling at you, they are wearing a %s." % (random.choice(clothes)))
        script.append("\"What are you doing?\" The person asks.")
        script.append("You turn your eyes and see a mirror.")
        script.append("Funnily enough, you look like the zombie you killed earlier that day.")
        script.append("But...")
        script.append("Humanly?")
        x = random.randint(1,100)
        if x < 75:
            script.append("Suddenly, your reflection begins to change.")
            script.append("It now looked like something had injured the person in your reflection %s." % (self.cause))

        return script