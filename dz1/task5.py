stroka = input().split()
num_of_groups = int(stroka[0])
string = stroka[1]
p = []
num = 0
while num != len(string):
    temp = string[num : num + len(string) // num_of_groups]
    p.append(temp)
    num = num + len(string) // num_of_groups
ans = ''
for i in p:
    i = i[::-1]
    ans += i
print(ans)