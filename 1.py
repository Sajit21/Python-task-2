#a 2ns part starting for python task

#here we have to display fizz if the number is divisible by 3 ,if divisible by 5 then display buzz and if divisible by both 3 and 5 then display fizz buzz
#here we learned about the range where we started from 1 to the last. we incremented by 1 since last value should be displayed and we gapped the valued by 2


x=int(input())
# even_sum=0
for i in range(1,x+1,2):
    # even_sum+=i
   print(i)
   if(i%3==0):
    print("fizz")
   elif(i%5==0):
    print("buzz")
   elif(i%3==0 and i%5==0):
    print("fizzbuzz")
#    else:
#     print("nothing")

