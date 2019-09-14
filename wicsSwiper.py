import pandas as pd

print("Enter the path to the card swipe file: ") 
filepathInput = input() 

df = pd.read_csv(filepathInput)

df["card_number"] = df["card_number"].str[18:28]

print("Enter the path where you want the file saved: ")
filepathOutput = input()

print("Enter the the name of the file: ")
name = input()

filepathOutput += "/"
filepathOutput += name

df.to_csv(filepathOutput)

