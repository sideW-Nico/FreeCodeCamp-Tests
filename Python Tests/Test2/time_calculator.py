from typing import SupportsRound


def roundDay (n):
  if n - round(n) > 0:
    return round(n) + 1
  return round(n)
  
def roundDay (n):
  if n - round(n) > 0:
    return round(n) + 1
  return round(n)
  
def calculateHourPeriod(period, hours):
  calculatedPeriod = hours // 12
  if calculatedPeriod % 2 == 0:
    return period
  else:
    if period == "AM": 
      return "PM"
    else:
      return "AM"

def calculateTime(actualTime, newTime, hourPeriod):
  newMinutes = None
  newHours = None
  
  splitActualTime = actualTime.split(":")
  splitNewTime = newTime.split(":")
  
  calculatedHours = int(splitActualTime[0]) + int(splitNewTime[0])
  calculatedMinutes = int(splitActualTime[1]) + int(splitNewTime[1])
  
  newHours = round((calculatedHours)/288) + int(splitActualTime[0])
  
  if calculatedMinutes >= 60:
    newHours = round(calculatedMinutes/60) + calculatedHours
    newMinutes = calculatedMinutes - 60
  else:
    newHours = calculatedHours
    newMinutes = calculatedMinutes
    
  hourPeriod = calculateHourPeriod(hourPeriod, newHours)

  if newHours > 12:
    newHours = newHours % 12
    if newHours == 0:
      newHours = 12

  if newMinutes < 10:
    newMinutes = "0" + str(newMinutes)

  return str(newHours) + ":" + str(newMinutes) + " " + hourPeriod


def add_time(start, duration, day = None):
  dayNames = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
  
  new_time = str()
  splitStart = start.split()

  actualTime = splitStart[0]
  hourPeriod = splitStart[1]
  
  cleanActualTime = int(splitStart[0].replace(":", ""))
  cleanDuration = int(duration.replace(":", ""))
  
  new_time += calculateTime(actualTime, duration, hourPeriod)

  daysCalculation = (cleanActualTime + cleanDuration) / 2400
  if day != None:
    find = day.capitalize()
    if cleanDuration == 2400 and find == "Saturday":
      new_time += ", " + dayNames[0]
    elif cleanActualTime + cleanDuration >= 1200 and daysCalculation >= 1:
      new_time += ", " + dayNames[(dayNames.index(find) + roundDay(daysCalculation)) % 7]
    else:
      new_time += ", " + find
      
  if cleanDuration == 2400:
    new_time += " (next day)"    
  elif daysCalculation > 0.50:
    if daysCalculation <= 1 and new_time.split()[1] == "AM":
      new_time += " (next day)"
    elif roundDay(daysCalculation) > 1:
      new_time += " ({0} days later)".format(roundDay(daysCalculation))

  return new_time 