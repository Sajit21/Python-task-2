#a vitual represntation of the movement of the turtle
#use of the funtion with multiple output
#return with multiple output

def myfun(name1,name2):
    nam1=name1.title()  #title() make first letter of each word in uppercase
    nam2=name2.title()
    return f"{nam1} and  {nam2}"  #return the value in string format 

#confused whether we can pass directly the value to the argument 
hero=myfun("sajit","hari")
# hero=myfun(name1:"sajit",name2:"hari")

print(hero)


#check no is prime or not
def is_prime(num):
    if num > 1:
        is_prime = True  #include the fun is true
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print("The given number is prime")
        else:
            print("The number is not a prime")
    else:
        print("The number is not a prime")

is_prime(7)
