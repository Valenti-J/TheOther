import random
import time
from Death import *


class Game:

    def __init__(self):
        self.first_names = ["Selena", "Mark", "Matthew", "Luke", "John", "Mary", "Grace", "Hope"]
        self.supplies = ["Food", "Water", "Medicine"]
        self.weapons = []
        self.locations = ["Diner", "Gas Station", "Convenient Store", "Supermarket"]
        self.members = ["Dad", "Mom", "Older Brother", "Younger Brother", "Older Sister", "Younger Sister"]
        self.dead_infected = []
        self.crew_members = []
        self.dead_crew_members = []
        self.sub_events = []
        self.car = False
        self.in_car = False
        self.family = False
        self.crew = False

    def string_fam(self):
        str = []
        for item in self.crew_members:
            str.append(item.get_family())
        if len(str) == 1:
            stri = str[0]
        else:
            stri = ""
            for i in range(len(str)):
                if i == len(str) - 1:
                    stri += "and " + str[i]
                else:
                    stri += str[i] + ", "
        return stri

    def create_family(self, all_dead = False):
        if all_dead:
            size = 0
        else:
            size = random.randint(1, 6)
        for i in range(size):
            family_member = random.choice(self.members)
            self.members.remove(family_member)
            if family_member == "Mom" or "Dad":
                age = random.randint(40, 70)
            else:
                age = random.randint(5,30)
            member = CrewMember(random.choice(self.first_names),age,family_member)
            self.crew_members.append(member)

        for family_member in self.members:
            if family_member == "Mom" or "Dad":
                age = random.randint(40, 70)
            else:
                age = random.randint(5,30)
            member = CrewMember(random.choice(self.first_names),age,family_member)
            self.dead_crew_members.append(member)

    def hospital_opening(self):
        self.create_family(True)
        l1 = "You awake in a hospital bed not remembering what got you there."
        l2 = "You look around and notice that this room seems completely abandoned."
        script = [l1, l2]
        for str in script:
            print(str)
            time.sleep(1)

    def family_opening(self):
        self.create_family()
        family = True
        l1 = "You are sitting at home with your family watching some television."
        l2 = "Suddenly, the channel switches to a news screen that flashes \"BREAKING NEWS\"."
        script = [l1, l2]
        for str in script:
            print(str)
            time.sleep(1)

    def car_opening(self):
        self.create_family()
        self.crew = True
        self.family = True
        self.car = True
        self.in_car = True
        l1 = "You look out the window at the lines of abandoned cars."
        l2 = "The car your dad is driving continues to pass what feels like thousands of the deserted vehicles."
        l3 = "Everything feels like it happened so quickly."
        l4 = "Just a few hours ago you were sitting in your living room with your family watching some television."
        l5 = "Now you and your %s were driving as far away from the city as possible." % self.string_fam().lower()
        l6 = "Apparently, some new disease was causing thousands of people to die."
        l7 = "But what was different about this disease is that it was causing people to come back from the dead too."
        l8 = "Real life zombies... The concept still is impossible to grasp..."
        script = [l1, l2, l3, l4, l5, l6, l7, l8]
        for str in script:
            print(str)
            time.sleep(1)

    def surprise_zombie(self):
        script = []
        name = random.choice(self.first_names)
        descriptions = ["that surprisingly looking healthy","wearing a name tag labeled: %s" % name,
                        "with a spike though its eye", "missing an arm", "that wreaked of rotten flesh."]
        age = random.randint(5, 70)
        desc = "A "
        if age < 18:
            desc += "little "
        desc += "zombie " + random.choice(descriptions)
        zombie = CrewMember(name,age,False,desc)
        script.append("While walking around, you are suddenly attacked by a zombie.")
        x = random.randint(1,100)
        if x < 50:
            script.append("You notice the zombie is %s " % (desc.lower()))
        script.append("You reach for your pocket and find...")
        if len(self.weapons) == 0:
            script.append("Nothing there.")
        else:
            for weapon in self.weapons:
                script.append("Your %s" % weapon)
        script.append("You decide to...")

        for str in script:
            print(str)
            time.sleep(1)

        script = []

        if len(self.weapons) == 0:
            s = input("[1] Try to escape, [2] Try to kill it without a weapon ")
        else:
            s = input("[1] Try to escape, [2] Try to kill it without a weapon, [3] Try to kill it with a weapon ")

        if s == "1":
            x = random.randint(1, 100)
            if x < 50:
                script.append("The zombie grabs you as you try to escape and you struggle to break its grasp.")
                script.append("You decide to...")
                for str in script:
                    print(str)
                    time.sleep(1)

                script = []

                if len(self.weapons) == 0:
                    s2 = input("[1] Try to escape, [2] Try to kill it without a weapon ")
                else:
                    s2 = input("[1] Try to escape, [2] Try to kill it without a weapon,"
                               " [3] Try to kill it with a weapon ")

                if s2 == "1":
                    script.append("You escape successfully with no blood on your hands.")
                elif s2 == "3":
                    w = random.choice(self.weapons)
                    script.append("You use your %s to break free from the zombie, "
                           "and then use it to kill them." % (random.choice(self.weapons)))
                    dead = Death(zombie, True, "by using your %s" % w)
                    self.dead_infected.append(dead)
                else:
                    script.append("You manage to shove the zombie to the ground.")
                    script.append("You stomp its head in.")
                    dead = Death(zombie, True, "by stomping their head in")
                    self.dead_infected.append(dead)
            else:
                script.append("You escape successfully with no blood on your hands.")
        elif s == "3":
            w = random.choice(self.weapons)
            script.append("You use your %s to kill them." % w)
            dead = Death(zombie,True,"by using your %s" % w)
            self.dead_infected.append(dead)
        else:
            script.append("You manage to shove the zombie to the ground.")
            script.append("You stomp their head in.")
            dead = Death(zombie, True, "by stomping their head in")
            self.dead_infected.append(dead)

        for str in script:
            print(str)
            time.sleep(1)

    def feel_zombie_guilt(self):
        dead = random.choice(self.dead_infected)
        script = dead.create_string()
        for str in script:
            print(str)
            time.sleep(1)

    def find_weapon(self):
        weapons = ["Gun","Knife","Ax","Baseball Bat"]
        w = random.choice(weapons)
        print("While walking around you find a %s." % (w))
        print("You decide to...")
        if len(self.crew_members) > 0:
            c = random.choice(self.crew_members)
            if type(c.get_family()) == str:
                s = input("[1] Keep it, [2] Leave it, [3] Give to %s, your %s " % (c.get_name(), c.get_family()))
            else:
                s = input("[1] Keep it, [2] Leave it, [3] Give to %s" % (c.get_name()))
            if s == "1":
                self.weapons.append(w)
        else:
            s = input("[1] Keep it, [2] Leave it ")
            if s == "1":
                self.weapons.append(w)

    def run_out_gas(self):
        print("While driving you carelessly run out of gas.")
        time.sleep(1)
        print("You begin to walk until you can find a gas station.")
        time.sleep(1)
        x = random.randint(1,100)
        if x < 25:
            random.choice(self.sub_events)()
        x = random.randint(1, 100)
        if x < 20:
            print("You are able to find gas and can go back to your car to use it.")
        else:
            print("You are unable to find gas efficiently and have to travel on foot.")
            self.car = False

    def pit_stop(self):
        location = random.choice(self.locations)
        goal = random.choice(self.supplies)
        if len(self.crew_members) > 0:
            crew = "you and your crew"
        else:
            crew = "you"
        if self.car:
            transport = "driving"
        else:
            transport = "walking"

        print("While %s are %s, you decide to stop at a %s to find %s." % (crew,transport,location,goal))
        time.sleep(1)
        print("You begin to stroll around the %s." % (location))
        time.sleep(1)

        x = random.randint(1, 100)
        if x < 25:
            random.choice(self.sub_events)()



















    def run(self):
        day = 1
        non_car_events = [self.find_weapon,self.surprise_zombie,self.pit_stop]
        car_events = [self.run_out_gas,self.pit_stop]
        se = [self.find_weapon,self.surprise_zombie]

        for item in se:
            self.sub_events.append(se)

        while True:
            print("Day %s" % (day))
            if day == 1:
                self.car_opening()
            print("\n")
            time.sleep(2)
            if self.car:
                random.choice(car_events)()
            else:
                random.choice(non_car_events)()
            print("\n")
            time.sleep(2)

            if len(self.dead_infected) > 0:
                print("While sleeping you hear a voice telling you something.")
                time.sleep(1)
                print("It is hard to hear at first.")
                time.sleep(1)
                print("You are finally able to make out what it is saying: \n\n")
                time.sleep(1)
                self.feel_zombie_guilt()
            print("\n\n")
            time.sleep(1)
            day += 1
            if day > 10:
                break