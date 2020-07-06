import sys
import math


class OutPut:
    def __init__(self, nbr, string):
        self.nb = nbr
        self.str = string
        self.diff = self.nb - (math.pi * 0.5)

    def get_nb(self):
        return self.nb

    def get_str(self):
        return self.str


def printing(mid, trap, sim):
    print("REAL: %.10f\n" % (math.pi * 0.5))
    my_list = [OutPut(mid, "Midpoint:"), OutPut(trap, "Trapezoidal:"), OutPut(sim, "Simpson:")]
    min_ = 0
    i = 0
    for i in range(len(my_list)):
        for j in range(0, len(my_list) - i - 1):
            if my_list[j].diff < my_list[j + 1].diff:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    print("\033[0;32m1. Best:")
    for i in range (len(my_list)):
        print("%s" % (my_list[i].str))
        print("I%d = %.10f" % (int(sys.argv[1]), my_list[i].nb))
        if (round(my_list[i].diff, 10) == -0):
            print("diff = 0.0000000000", end='')
        else:
            print("diff = %.10f" % (math.fabs(my_list[i].diff)), end='')
        if (i < len(my_list) - 2):
            print("\033[0;0;0m\n\n%i. Mid:" % (i + 2))
        if (i == len(my_list) - 2):
            print("\033[0;31m\n\n%i. Worst:" % (len(my_list)))
    print("\033[0;0;0m")
