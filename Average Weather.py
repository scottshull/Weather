weather = { 'January' : '73', 'February' : '73', 'March' : '77', 'April' : '79', 'May' : '81', 'June' : '82', 'July' : '82', 'August' : '82', 'September' : '82', 'October' : '81', 'November' : '77', 'December' : '75'}
print weather

def ave_temp(month):
    total = 0
    for temp in month:
        total += month[temp]
    ave = total / len(weather)
    print(" The average temperature for Cancun this year was: " str(ave))

