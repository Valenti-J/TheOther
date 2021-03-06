import random
import time
from Death import *


class Game:

    def __init__(self):
        self.first_names = ["Selena", "Mark", "Matthew", "Luke", "John", "Mary", "Grace", "Hope","Eli","Thomas"]
        self.supplies = ["Food", "Water", "Medicine","Weapons"]
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
        print("While sleeping you hear a voice telling you something.")
        time.sleep(1)
        print("It is hard to hear at first.")
        time.sleep(1)
        print("You are finally able to make out what it is saying: \n\n")
        time.sleep(1)
        dead = random.choice(self.dead_infected)
        script = dead.create_guilt()
        for str in script:
            print(str)
            time.sleep(1)

    def feel_zombie_memory1(self):
        dead = random.choice(self.dead_infected)
        script = dead.create_memory1()
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

        for i in range(5):
            x = random.randint(1, 100)
            if x < 25:
                random.choice(self.sub_events)()
            elif x < 50:
                print("You are able to find some %s." % (goal))
            else:
                print("Searching...")
            time.sleep(1)

        if self.car:
            print("After searching for a while, %s give up and start driving again." % (crew))
        else:
            print("After searching for a while, %s give up and start walking again." % (crew))




    def find_a_survivor(self):
        crew = "you"
        descriptions = ["that surprisingly looking healthy",
                        "with a spike though its eye", "missing an arm", "that wreaked of rotten flesh."]

        if self.crew:
            crew += "and your crew"

        if self.car:
            print("While driving, %s see some commotion by the side of the road." % (crew))
            time.sleep(1)
            print("It looks to be like a person.")
            time.sleep(1)
            x = random.randint(1,100)
            if x < 50:
                print("The person appears to be a zombie.")
                time.sleep(1)
                print("Do you...")
                s = input("[1] Ignore them, [2] Hit them")
                if s == "2":
                    cr = CrewMember(random.choice(self.first_names),random.randint(5,70),
                                    False,random.choice(descriptions))
                    self.dead_infected.append(Death(cr,True,"by running them over."))
                    y = random.randint(1,100)
                    if y < 50:
                        print("You damaged your vehicle while hitting the zombie"
                              " and are unable to drive with it anymore.")
                        self.car = False
            else:
                print("The person appears to be a survivor.")
                time.sleep(1)
                print("Do you...")
                s = input("[1] Ignore them, [2] Stop and talk to them")
                if s == "2":
                    cr = CrewMember(random.choice(self.first_names), random.randint(30, 70),
                                    False)
                    print("\"Oh, thank goodness!  I have been walking for miles in search of other people.\" They say.")
                    time.sleep(1)
                    print("\"Can I join you guys\"")
                    s2 = input("[1] Yes, [2] No")
                    if s2 == "1":
                        print("They join you in your vehicle.")
                        time.sleep(1)
                        print("\"Hi, my name is %s\" they introduce themselves as you drive away." % (cr.get_name()))
                        self.crew_members.append(cr)
                    else:
                        print("You drive off without talking to them further.")
        else:
            print("While walking, %s see some commotion by the up ahead." % (crew))
            time.sleep(1)
            print("It looks to be like a person.")
            time.sleep(1)
            x = random.randint(1, 100)
            if x < 50:
                print("The person appears to be a zombie.")
                time.sleep(1)
                print("Do you...")
                s = input("[1] Ignore them, [2] Kill them.")
                if s == "2":
                    if len(self.weapons) > 0:
                        w = random.choice(self.weapons)
                        print("You kill it using a %s" % w)
                        cr = CrewMember(random.choice(self.first_names), random.randint(5, 70),
                                    False, random.choice(descriptions))
                        self.dead_infected.append(Death(cr, True, "with a %s." % (w) ))
                    else:
                        print("You kill it by knocking it down and stomping its head in.")
                        cr = CrewMember(random.choice(self.first_names), random.randint(5, 70),
                                        False, random.choice(descriptions))
                        self.dead_infected.append(Death(cr, True, "by knocking it over and stomping its head in."))
                else:
                    print("The person appears to be a survivor.")
                    time.sleep(1)
                    print("Do you...")
                    s = input("[1] Ignore them, [2] Approach them")
                    if s == "2":
                        cr = CrewMember(random.choice(self.first_names), random.randint(30, 70),
                                        False)
                        print(
                            "\"Oh, thank goodness! I have been walking for miles in search of other people.\" They say.")
                        time.sleep(1)
                        print("\"Can I join you guys\"")
                        s2 = input("[1] Yes, [2] No")
                        if s2 == "1":
                            print("They join you as you continue to walk.")
                            time.sleep(1)
                            print(
                                "\"Hi, my name is %s\" they introduce themselves as you walk." % (cr.get_name()))
                            self.crew_members.append(cr)
                        else:
                            print("You walk off as they awkwardly stay behind.")
                            g = random.randint(1,100)
                            if g > 35:
                                time.sleep(1)
                                print("You hear a scream from behind you a while later.")

    def roadblock(self):
        print("While driving, you encounter a roadblock.")
        time.sleep(1)
        x = random.randint(1,100)
        if x < 25:
            print("You successfully find an alternate route.")
        else:
            print("You are unable to find your way around the roadblock and lose the car.")
            self.car = False

    def find_car(self):
        print("While walking you find a car.")
        time.sleep(1)
        x = random.randint(1, 100)
        if x < 25:
            print("You are able to start it. ")
            time.sleep(1)
            print("You begin to drive off with it. ")
            self.car = True
        else:
            print("You are unable to get it to work.")

    def crew_zombie_attack(self):
        if self.crew > 0:
            bit = False
            attacked = random.choice(self.crew_members)

            name = random.choice(self.first_names)
            descriptions = ["that surprisingly looking healthy", "wearing a name tag labeled: %s" % name,
                            "with a spike though its eye", "missing an arm", "that wreaked of rotten flesh."]
            age = random.randint(5, 70)
            desc = "a "
            if age < 18:
                desc += "little "
            desc += "zombie " + random.choice(descriptions)
            zombie = CrewMember(name, age, False, desc)

            print("While walking, %s is attacked by %s." % (attacked.get_name(), desc))
            time.sleep(1)
            print("What do you do? ")

            if len(self.weapons) == 0:
                s2 = input("[1] Ignore them, [2] Try to help them without a weapon ")
            else:
                s2 = input("[1] Ignore them, [2] Try to help them without a weapon,"
                           " [3] Try to help them with a weapon ")

            if s2 == "1":
                x = random.randint(1,50)
                if x < 45:
                    print("You watch in horror as %s gets bit." % (attacked.get_name()))
                    bit = True
                else:
                    print("%s is able to break free from the zombie and kills them." % (attacked.get_name()))
            elif s2 == "3":
                w = random.choice(self.weapons)
                print("You use your %s to break %s free from the zombie, "
                              "and then use it to kill them." % (attacked.get_name(),random.choice(self.weapons)))
                dead = Death(zombie, True, "by using your %s to save %s" % (w, attacked.get_name()))
                self.dead_infected.append(dead)
            else:
                x = random.randint(1, 50)
                if x < 15:
                    print("You manage to shove the zombie to the ground.")
                    print("You stomp its head in.")
                    dead = Death(zombie, True, "by stomping their head in to save %s" % attacked.get_name())
                    self.dead_infected.append(dead)
                else:
                    print("You watch in horror as %s gets bit despite trying to help." % (attacked.get_name()))
                    bit = True

            if bit:

                print("%s panics realizing they are bit" % (attacked.get_name()))
                time.sleep(1)
                print("\"I am going to turn!\" %s cries." % (attacked.get_name()))
                time.sleep(1)
                print("What do you do?")
                s = input("[1] Leave them behind, [2] Kill them before they turn")
                if s == "1":
                    print("You walk away leaving %s to turn into a zombie." % (attacked.get_name()))
                    attacked.set_infect("Just how you remembered.")
                    death = Death(attacked,True,"by leaving them for dead after letting them get bit.")
                    self.dead_infected.append(death)
                else:
                    if len(self.weapons) > 0:
                        w = random.choice(self.weapons)
                        print("You use your %s to kill %s before they turn into a zombie." % (w,attacked.get_name()))
                        attacked.set_infect("Just how you remembered.")
                        death = Death(attacked, True, "with using your %s before they turned into a zombie." % (w))
                        self.dead_infected.append(death)

                    else:
                        print("You use your bare hands to kill %s before they turn into a zombie."
                              % (attacked.get_name()))
                        attacked.set_infect("Just how you remembered.")
                        death = Death(attacked, True, "with using your bare hands before they "
                                                      "turned into a zombie.")
                        self.dead_infected.append(death)

            else:
                print("%s is grateful to be alive." % (attacked.get_name()))

        else:
            self.surprise_zombie()




















    def run(self):
        day = 1
        non_car_events = [self.find_weapon,self.surprise_zombie,
                          self.pit_stop,self.find_a_survivor,self.find_car,
                          self.crew_zombie_attack]
        car_events = [self.run_out_gas,self.pit_stop,self.find_a_survivor,self.roadblock]
        se = [self.find_weapon,self.surprise_zombie,self.crew_zombie_attack]

        dream = [self.feel_zombie_guilt,self.feel_zombie_memory1]

        for item in se:
            self.sub_events.append(item)

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

            if len(self.crew_members) > 0:
                print("You and your crew begin to set up camp for the night.")
            else:
                print("You begin to set up camp for the night.")
            time.sleep(1)
            print("You determine it is safe enough and lay down.")
            time.sleep(1)
            print("You begin to fall asleep.")
            if len(self.dead_infected) > 0:
                if day < 9:
                    top = 100 - 10*(day)
                else:
                    top = 2
                x = random.randint(1, top)
                if x < 10:
                    random.choice(dream)()
            print("\n\n")
            time.sleep(1)
            day += 1
            if day > 15:
                break