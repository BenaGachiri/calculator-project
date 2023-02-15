#this is a calculator project

num1=eval(input("enter first number:"))
num2=eval(input("enter second number:"))

operator=input("enter operator:")
def add (num1,num2):
    result=num1+num2 
    print (result)

def subtract(num1,num2): 
    result=num1-num2
    print (result)

def divide(num1,num2):
    result=num1/num2
    print (result)

def mulplication(num1,num2):
    result=num1*num2
    print (result)  

if operator=="+":    
    add(num1,num2)
elif operator=="/":
    subtract(num1,num2) 
elif operator=="-":
    divide(num1,num2)
elif operator=="*":
    mulplication(num1,num2) 
    
elif operator =="X" or operator == "x" or operator=="*":
    mulplication(num1,num2)
else:
    print("invalid input")