# This program generates Chinese Zodiac upon entering a valid date

year = int(input("Input your birth year: "))
if (year - 2000) % 12 == 0:
    sign = 'Monkey'
elif (year - 2000) % 12 == 1:
    sign = 'dog'
elif (year - 2000) % 12 == 2:
    sign = 'pig'
elif (year - 2000) % 12 == 3:
    sign = 'rat'
elif (year - 2000) % 12 == 4:
    sign = 'ox'
elif (year - 2000) % 12 == 5:
    sign = 'tiger'
elif (year - 2000) % 12 == 6:
    sign = 'rabbit'
elif (year - 2000) % 12 == 7:
    sign = 'dragon'
elif (year - 2000) % 12 == 8:
    sign = 'snake'
elif (year - 2000) % 12 == 9:
    sign = 'horse'
elif (year - 2000) % 12 == 10:
    sign = 'sheep'
else:
    sign = 'Hare'

print("Your Zodiac sign :",sign)



