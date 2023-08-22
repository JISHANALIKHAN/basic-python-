def myprogram1():
    #  recursion is the process of defining something in terms of itself.
    def factorial(n):
        """ Takes value of n and returns the factorial of n
        """
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    if __name__=="__main__" :
        n = int(input("Enter the value of the number:"))
        print("factorial of", n, "=", factorial(n))
def myprogram2():
    print("hello \nThis program can classify your age group")
    age = int(input("enter the age in years "))
    if age <= 0:
        print("please enter a positive number or you will get slap ")
    elif 0 < age < 10:
        print("the person is a kid")
    elif 10 <= age < 21:
        print("the person is an adolescent ")
    elif age >= 21 and age < 40:
        print("the person is a young - aged adult")
    elif age >= 40 and age < 60:
        print("the person is a middle - aged adult ")
    elif age >= 60:
        print("the person is a old - aged adult ")
    print("have a nice day")

