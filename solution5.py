#WAS TO ENTER ANY NUMBER AND PRINT FROM WHICH NUMBER FROM 0 TO 9 IT IS DIVISABLE:
no1=0
no2=9
n=int(input("enter the number to be devided by:"))
for i in range(no1,no2):
    if(i%n==0):
        print(i)
        
