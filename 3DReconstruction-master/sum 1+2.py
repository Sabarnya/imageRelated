s1=input("Enter string1:")
s2=input("Enter string2:")
print(s1)
print("\r")
n=(len(s2)//2)+1
for i in range(n):
    string=s2
    for j in range(len(s2)):
        if((j!=i) and ((len(s2)-i)!=j+1)):
            string=string[:j]+" "+string[j+1:]
    print(string)
    print("\r")