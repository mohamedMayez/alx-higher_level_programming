#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = abs(number) % 10
if number < 0:
    temp = -temp
    if temp == 0:
         print('Last digit of', number,'is', temp, 'and is 0')
    else:
         print('Last digit of', number, 'is', temp, 'and is less than 6 and not 0')
else:
     if temp > 5:
          print('Last digit of', number, 'is', temp, 'and is greater than 5')
     elif temp == 0:
           print('Last digit of', number, 'is', temp, 'and is 0')
     else:
          print('Last digit of', number, 'is', temp, 'and is less than 6 and not 0')
