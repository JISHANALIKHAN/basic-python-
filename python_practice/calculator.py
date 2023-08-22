


print("hello,\nThis is an arithmetic operation calculator")
def Add():
    print("a + b =",a+b)
def Subtract():
    print("a - b =",a-b)
def Multiply():
    print("a * b =",a*b)
def Division():
    print("a / b =",a/b)
button=input('\nEnter "Proceed" for calculation:')
while ( "button==Proceed" , "more_operation"=="yes") :
 print('Valid operations in this calculator are \n"Add" for addition\n"Subtract" for subtraction\n"Multiply" for '
       'multiplication\n"Division" for division')
 a=float(input("Enter the value of the  first operand:"))
 b=float(input("Enter the value of the second operand:"))
 operation=input("enter the operation :")
 if b==0 and operation == "Division":
    print ("a/0= undefined")
 if operation == "Add" :
    Add()
 elif operation == "Subtract" :
    Subtract()
 elif operation == "Multiply":
    Multiply()
 elif b!=0 and operation == "Division":
    Division()
 elif operation!= "Add" or operation!= "Subtract" or operation!= "Multiply" or operation!="Division":
      print("Enter an appropriate operation")
 more_operation=input("Do you want to perform another calculation.(yes/no) :")
 if more_operation!="yes":
     print("have a nice day")
     break

