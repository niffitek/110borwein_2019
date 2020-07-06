import sys
import math


def display_help():
    if len(sys.argv) == 2:
        if sys.argv[1] == '-h' or sys.argv[1] == '--help':
            print("USAGE")
            print("\t./110borwein n\n")
            print("DESCRIPTION")
            print("\tn\tconstant defining the integral to be computed")
            sys.exit(0)
    else:
        sys.exit(84)


def calc(x):
    res = 1
    i = 0
    n = float(sys.argv[1])
    while i <= n:
        if x != 0:
            res *= math.sin(x / (2 * i + 1)) / (x / (2 * i + 1))
        i += 1
    return res


def midpoint():
    h = 0.5
    i = 0.0
    res = 0.0
    while (i < 10000):
        x = i / 2
        res += calc(x + 0.25)
        i += 1
    res *= 0.5
    diff = res - (math.pi * 0.5)
    print("Midpoint:")
    print("I%d = %.10f" % (int(sys.argv[1]), res))
    if (round(diff, 10) == -0):
        print("diff = 0.0000000000")
    else:
        print("diff = %.10f" % (math.fabs(diff)))
    print()


def trapezoid():
    h = 0.5
    res = 0
    i = 1.0
    while (i < 10000):
        x = i * h
        res += calc(x)
        i += 1
    res = ((res * 2) + calc(0) + calc(5000))
    diff = (res * h / 2) - (math.pi * 0.5)
    print("Trapezoidal:")
    print("I%d = %.10f" % (int(sys.argv[1]), (res * h / 2)))
    if (round(diff, 10) == -0):
        print("diff = 0.0000000000")
    else:
        print("diff = %.10f" % (math.fabs(diff)))
    print()


def simpsons():
    h = 0.5
    res = 0
    i = 0
    while (i < 10000):
        x = i * h
        if (i < 1):
            res += 4 * calc(x + h / 2)
        else:
            res += 2 * calc(x) + 4 * calc(x + h / 2)
        i += 1
    res = (calc(0) + calc(5000) + res) * h / 6
    diff = res - (math.pi * 0.5)
    print("Simpson:")
    print("I%d = %.10f" % (int(sys.argv[1]), res))
    if (round(diff, 10) == -0):
        print("diff = 0.0000000000")
    else:
        print("diff = %.10f" % (math.fabs(diff)))


def main():
    display_help()
    try:
        if (int(sys.argv[1]) < 0):
            sys.exit(84)
    except ValueError:
        sys.exit(84)
    midpoint()
    trapezoid()
    simpsons()
    sys.exit(0)