import action as act


class S3DSAgent:
    energy = 0

    starstuff = 0
    starcoins = 0
    starfood = 0

    starstuff_2_starfood = 0

    possessions = list()

    def __init__(self, starting_vals: dict):

        self.energy = starting_vals['energy']
        self.starfood = starting_vals['food']
        self.starstuff_2_starfood = starting_vals['stuff2food']

    def move(self, hour):

        energy_expended = 0

        # assign a schedule for both agents (we can keep it simple and give them both the same schedule)
        # NOTE: maximum daily energy expenditure, IF the schedule is perfectly followed
        #       AND we calculate for the maximum possible expenditure for any one activity state
        #       we get: 131 energy units (as is displayed below)

        schedule = {0: 'sleep',  # 2
                    1: 'sleep',  # 2
                    2: 'sleep',  # 2
                    3: 'sleep',  # 2
                    4: 'sleep',  # 2
                    5: 'sleep',  # 2
                    6: 'daily_prep',  # 4
                    7: 'eat',  # 3
                    8: 'travel',  # 3
                    9: 'work',  # 5 to 10
                    10: 'work',  # 5 to 10
                    11: 'work',  # 5 to 10
                    12: 'work',  # 5 to 10
                    13: 'eat',  # 3
                    14: 'work',  # 5 to 10
                    15: 'work',  # 5 to 10
                    16: 'work',  # 5 to 10
                    17: 'work',  # 5 to 10
                    18: 'travel',  # 3
                    19: 'exercise',  # 8 to 10
                    20: 'eat',  # 3
                    21: 'shop',  # 6
                    22: 'sleep',  # 2
                    23: 'sleep'}  # 2

        if schedule[hour] == 'sleep':
            energy_expended += self.sleep()
        if schedule[hour] == 'daily_prep':
            energy_expended += self.daily_prep()
        if schedule[hour] == 'eat':
            energy_expended += self.eat()
        if schedule[hour] == 'travel':
            energy_expended += self.travel()
        if schedule[hour] == 'work':
            energy_expended += self.work()
        if schedule[hour] == 'exercise':
            energy_expended += self.exercise()
        if schedule[hour] == 'shop':
            energy_expended += self.shop()


        self.energy -= energy_expended

    def sleep(self):

        # energy used for sleeping
        return 2

    def daily_prep(self):

        # energy required for prepping
        return 4

    def eat(self):

        energy_report = 0

        # energy require for eating
        energy_report -= 3

        # determine how much food is needed
        # max daily expenditure (calculated above, at schedule) is 131
        mde = 131
        if self.energy < (mde // 2):
            # prepare a portion of food
            self.starfood -= 1
            # energy gained from eating
            energy_report += self.starstuff_2_starfood

        return energy_report

    def travel(self):

        return 3

    def work(self):

        # this method will be overridden in the inheriting classes
        pass

    def exercise(self):

        return 10

    def shop(self):

        return 6
