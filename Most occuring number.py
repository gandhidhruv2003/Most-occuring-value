from statistics import *
import statistics
import re
try:
    def most_occuring_number():
        s = str(input("Enter a string: "))
        number = re.findall(r"[0-9]",s)
        print("List of number in the sentence is: ",number)
        print("The most occuring Number is: ",mode(number))
    most_occuring_number()
except statistics.StatisticsError:
    print("Enter a number and not a character")
except:
    print("Enter correctly")