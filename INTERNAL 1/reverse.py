num=123
rev=0
n= num
while  n>0:
    digit=n%10
    rev=rev*10+digit
    n//=10
    print("The reversed code is:",rev)
