def devisible(num):
    num=int(num)
    count=0
    
    temp=num
    while num>0:
        if temp%num==0:
            print(num)
            count+=1
       
        num-=1
    if count==2 and temp!=1 :
        print("this number is prime")    

def perfect_num(num):
    num=int(num)
    total=0
    temp=num
    while num>0:
        
        if temp%num==0 and temp>num:
            total+=num
        num-=1


    if temp==total:
        print("this number is pefect!")
    else:
        print("this number is not perfect!")        


#this program was written by amirjaz

print("hi this program gives the divisible numbers of the entered number")

num=input("please enter your number: ")
num=int(num)
if num<=0:
    print("your number must be bigger than zero!")
else:



 print(f"the divisible numbers of the {num} is: ")

 devisible(num)
 perfect_num(num)


