def units_place(number):
    """Return the units place number of a given integer"""
    digit = number % 10
    return digit

def tens_place(numbernew):
    """Return the tens place number of a given integer"""
    tensCounter = numbernew / 10
    newCounter = tensCounter % 10
    return newCounter

def resultt():
    result = digitnew + digitt

def hundreds_place(numbernew):
    """Return the hundreds place of a given integer"""
    count = numbernew / 10
    anotherCounter = count / 10
    return anotherCounter
    
number1 = raw_input("Enter a number:\n")
number = int(number1)
numbernew = number

result = " "
unitword = " "
tenword = " "
hundredword = " "
digit = 0
tens = 0
tensCounter = 0
newCounter = 0
anotherCounter = 0
count = 0

words = ["One", "Two", "Three", "Four",
         "Five", "Six", "Seven", "Eight", "Nine"]

words1 = ["Ten", "Twenty", "Thirty", "Forty", "Fifty",
          "Sixty", "Seventy", "Eighty", "Ninety"]

words2 = ["One Hundred", "Two Hundred", "Three Hundred", "Four Hundred",
          "Five Hundred", "Six Hundred", "Seven Hundred", "Eight Hundred",
          "Nine Hundred"]

special = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen",
            "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

digit = units_place(number)
if digit == 1:
        unitword = words[0]
elif digit == 2:
        unitword = words[1]
elif digit == 3:
        unitword = words[2]    
elif digit == 4:
        unitword = words[3]
elif digit == 5:
        unitword = words[4]
elif digit == 6:
        unitword = words[5]
elif digit == 7:
        unitword = words[6]
elif digit == 8:
        unitword = words[7]
elif digit == 9:
        unitword = words[8]
 
newCounter = tens_place(numbernew)
if newCounter == 1:
        tenword = words1[0]
elif newCounter == 2:
        tenword = words1[1]
elif newCounter == 3:
        tenword = words1[2]
elif newCounter == 4:
        tenword = words1[3]
elif newCounter == 5:
        tenword = words1[4]
elif newCounter == 6:
        tenword = words1[5]
elif newCounter == 7:
        tenword = words1[6]
elif newCounter == 8:
        tenword = words1[7]
elif newCounter == 9:
        tenword = words1[8]

anotherCounter = hundreds_place(numbernew)
if anotherCounter == 1:
    hundredword = words2[0]
elif anotherCounter == 2:
    hundredword = words2[1]
elif anotherCounter == 3:
    hundredword = words2[2]
elif anotherCounter == 4:
    hundredword = words2[3]
elif anotherCounter == 5:
    hundredword = words2[4]
elif anotherCounter == 6:
    hundredword = words2[5]
elif anotherCounter == 7:
    hundredword = words2[6]
elif anotherCounter == 8:
    hundredword = words2[7]
elif anotherCounter == 9:
    hundredword = words2[8]

#if digit == 0 and newCounter == 1:
    

print hundredword
print tenword
print unitword

