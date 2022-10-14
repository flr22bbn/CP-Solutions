countupper=countlower=0
s=input()
s1=""
for i in range(len(s)):
    if s[i].islower():
        countlower+=1
    elif s[i].isupper():
        countupper+=1
if countlower<countupper:
    for i in range(len(s)):
        print(s[i].upper(),end="")
else:
    for i in range(len(s)):
        print(s[i].lower(),end="")
