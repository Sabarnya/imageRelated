data = {"January":31,"February":28,"March":31,"April":30,"May":31,"June":30,"July":31,
        "August":31,"September":30,'October':31,"November":30,"December":31}
a=input("Enter the name of Month:")
if a in data:
    print("No of days are:",data[a])
else:
    print("Invalid input")
print("The alphabetical order is:")
for i in sorted (data.keys()) :  
     print(i, end = " ") 
print(" ")
print("Months with 31 days:")
for i in data :  
    if(data[i]==31):
        print(i, end=" ")
print(" ")
print("Alphabetical month and days combination is:")
for i in sorted (data.keys()) :  
     print(i,data[i], end = "\n") 
print(" ")