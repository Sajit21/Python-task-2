#nested list and dictionary
#here we done the nested list and dictionary


#dictionary
mydata={"ram":"he is a male ",
        "sita":"she is a female"}

print(mydata["ram"]) #display the value of the key pair

# mydata={"john":"he is a non-binary"}
#use of big bracket in the key pair for addition
mydata["john"]={"he is a non-binary"} #here we add the key value pair to the main variable and dispaly them

print(mydata)

mydata["sita"]={"she is really pretty"} #override the previous data with the new value
print(mydata)
