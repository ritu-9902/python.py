#LAPINDROME

from tokenize import String


def Lapindrome(str):

    strlen = len(str)
    print(strlen)
    if(strlen%2==0):
        a = str[:(strlen//2)]
        b = str[(strlen//2):]
    else: 

        a = str[:(strlen//2)]
        b = str[(strlen//2)+1:]
        print(b)
    list_a = list(a)

    list_a.sort()
    print(list_a)
    list_b = list(b)

    list_b.sort()
    print(list_b)
    if (list_a==list_b):
        print("YES")
    else:
        print("NO")

a = int(input())

for i in range(a):
    String =  input()
    Lapindrome(String)