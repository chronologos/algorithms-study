import random
from termcolor import colored, cprint
class Tester():
    def __init__(self,sort_function):
        self.sort_function = sort_function
        self.failures = 0
        print("testing %s", sort_function.__name__)
    def test(self):
        for i in range(0, 20):
            print("--")
            rand_list = []
            for i in range(0, random.randint(5, 20)):
                rand_list.append(random.randint(1, 100))
            original_list = rand_list[:]
            sorted_list = self.sort_function(rand_list)
            print("ol is: ", original_list)
            print("rl is: ", rand_list)
            print("sl is:", sorted_list)
            original_list.sort()
            if original_list != sorted_list:
                print("sort() gives: ", original_list)
                print("wrong")
                self.failures += 1
        if self.failures:
            msg = "Failed %d times.", self.failures
            cprint(msg,"red")
        else:
            cprint("Passed all.","green",attrs=["bold"])

