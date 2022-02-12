#Number of Occurance of Words
a = int(input())

dict = {}
for i in range(a):
    str = input()
    if str in dict:
        dict[str] +=1
    else:
        dict[str] = 1
print(len(dict))
for i in dict.values():
    print(i ,end=' ')
