n = int(input())
s = input()
l = []
s = s.lower()
for i in s:
    if i not in l:
        l.append(i)
print("YES") if len(l) == 26 else print("NO")
