#only use of class while displaying

#donw with the python task 

class User:


#single use of class
#     pass
# user1="sajit"
# user2="hari"
# print(user1)

#now use of class and constructor

 def __init__(self,user_id,username):
    self.id=user_id
    self.name=username
    self.followers=0       #default value 
    self.following=0      #default value

 def follows(self,user):
   user.followers+=1     #maile follow garda kheri user ko follower 1 le badna paryo
   self.following+=1    #mero following 1 le badna paryo   

user1=User("101","sajit")
user2=User("101","sajit")
user2.follows(user1)   #follow method use gareko
print(user1.followers)
print(user1.following)


print(user1.id)
print(user1.name)


