import calendar
import datetime

def getDate():
    dataAgora = datetime.datetime.now()
    year = int(datetime.datetime.strftime(dataAgora, '%Y'))
    month = int(datetime.datetime.strftime(dataAgora, '%m'))
    day = int(datetime.datetime.strftime(dataAgora, '%d'))
    return year, month, day


dataAgora = getDate()

print(dataAgora)
# display the calendar
month = calendar.month(dataAgora[0], dataAgora[1])
text_cal = calendar.TextCalendar(firstweekday = 0)
print(text_cal.formatmonth(dataAgora[0], dataAgora[1], w = 5))
print(month)

obj = calendar.Calendar(firstweekday = 2)
  
for day in month.iterweekdays():
    if day in [5, 6]:
        continue
    print(day)