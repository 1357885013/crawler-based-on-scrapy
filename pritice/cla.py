#!/usr/bin/python3
year = mon = day = 1


def inputs():
    try:
        year = int(input("year:"))
        mon = int(input("month:"))
        day = int(input("day:"))
    except ValueError:
        print("only int can be input!")
        inputs()


inputs()
days = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)


ans = days[mon - 1] + day
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    if mon > 2:
        ans += 1
print("it is the {}th day".format(ans))
