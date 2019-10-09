import pandas as pd
import numpy as np

cardList = []

'''
  get the filename for the event  
'''
print("enter desired event file name:") 
filename = input() + ".csv"

'''
    get each individual card number
'''
print("input card numbers (N to stop):")
choice = input()

while (choice != 'N'):
    choice = choice[18:28]
    print("Now adding", choice, "\n")
    cardList.append(choice)
    choice = input()

cardList = np.array(cardList)

np.savetxt(filename, cardList, fmt='%s', delimiter=",")

