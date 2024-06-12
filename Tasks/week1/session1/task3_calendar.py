import calendar

def print_cal(yy,mm):
    cal = calendar.month(yy,mm)
    print(cal)

year=int(input('Input the year:'))
month=int(input('Input the month:'))
print_cal(year,month)
