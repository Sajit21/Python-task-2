#nonchanges

# import random.choice 
import random
letter=['a','b','c','d']
number=['1','2','3','4','5','6']
symbol=['!','@','#','$','%','^','&','*','(',')']

print("create a random password")
n_letter=int(input("enter the length of the letter"))
n_number=int(input("enter the lenght of the number"))
n_symbol=int(input("enter the length of the sybmol"))

# password=""
#easy format password generator
# for i in range(1,n_letter+1):
#       ran=random.choice(letter)
#       password+=ran
#     #   print("password")
    
# for i in range(1,n_number+1):
#       ran=random.choice(number)
#       password+=ran
#     #   print("password")
    
# for i in range(1,n_symbol+1):
#       ran=random.choice(symbol)
#       password+=ran
#     #   print("password")

# print(password)

#hard level password generator


password=[]   # here we change string to the list 
for i in range(1,n_letter+1):
      ran=random.choice(letter)
      password+=ran
    #   print("password")
    
for i in range(1,n_number+1):
      ran=random.choice(number)
      password+=ran
    #   print("password")
    
for i in range(1,n_symbol+1):
      ran=random.choice(symbol)
      password+=ran
    #   print("password")

print(password)
random.shuffle(password)
print(password)

naya_pass=""
for i in password:
      naya_pass+=i
    
print(f"here your password is : {naya_pass}")  #f stands as the value inside curly bracket ie: { } the result are embidded and provided in string fornmat
