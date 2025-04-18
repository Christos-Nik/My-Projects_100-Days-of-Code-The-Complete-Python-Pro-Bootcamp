def is_leap_year(year):
    leap_year = False
    a = year % 4
    if a == 0:
        leap_year = True
        b = year % 100
        if b == 0:
            leap_year = False
            c = year % 400
            if c == 0:
                leap_year = True
    
    return leap_year
    # Don't change the function name.

print(is_leap_year(1700))    #should output True or False
