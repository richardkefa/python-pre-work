import datetime
print("Enter your age")
age=input()
date=datetime.datetime.now()
currentyear=int(date.year)
yearborn=currentyear-age
whichyear80=(80-age)+currentyear
print("You were born in "+yearborn)
print("You will be 80 in "+whichyear80)
