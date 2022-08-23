# anonymous function definition
import sys        
addop=lambda a,b:a+b
subop=lambda a,b:a-b
mulop=lambda a,b:a*b
divop=lambda a,b:a/b
floordivop=lambda a,b:a//b
modop=lambda a,b:a%b
expop=lambda a,b:a**b

# normal function definition
def aopmenu():     
    print("="*40)
    print("\tArithmetic Operations:")
    print("="*40)
    print("\t1.Addition:")
    print("\t2.Subtraction:")
    print("\t3.Multiplication:")
    print("\t4.Division:")
    print("\t5.Floor Division:")
    print("\t6.Modulus Division:")
    print("\t7.Exponentiation:")
    print("\t8.Exit:")
    print("="*40)

# main program
i=0
while(i<5):
    aopmenu()
    ch=int(input("Enter your choice:"))
    match (ch):
        case 1:
            x1=float(input("Enter First Value for Addition:"))
            x2=float(input("Enter Second Value for Addition:"))
            res=addop(x1,x2)
            print("Sum of {} and {} = {}".format(x1,x2,res))
            
        case 2:
            x1=float(input("Enter First Value for Subtraction:"))
            x2=float(input("Enter Second Value for Subtraction:"))
            res=subop(x1,x2)
            print("Difference of {} and {} = {}".format(x1,x2,res))
            
        case 3:
            x1=float(input("Enter First Value for Multiplication:"))
            x2=float(input("Enter Second Value for Multiplication:"))
            res=mulop(x1,x2)
            print("Product of {} and {} = {}".format(x1,x2,res))
            
        case 4:
            x1=float(input("Enter First Value for Division:"))
            x2=float(input("Enter Second Value for Division:"))
            res=divop(x1,x2)
            print("Division of {} and {} = {}".format(x1,x2,res))
            
        case 5:
            x1=float(input("Enter First Value for Floor Division:"))
            x2=float(input("Enter Second Value for Floor Division:"))
            res=floordivop(x1,x2)
            print("Floor Division of {} and {} = {}".format(x1,x2,res))
            
        case 6:
            x1=float(input("Enter First Value for Modulus Division:"))
            x2=float(input("Enter Second Value for Modulus Division:"))
            res=modop(x1,x2)
            print("Modulo Division of {} and {} = {}".format(x1,x2,res))
            
        case 7:
            x1=float(input("Enter Base for Exponentiation:"))
            x2=float(input("Enter Power for Exponentiation:"))
            res=expop(x1,x2)
            print("{} to the power of {} = {}".format(x1,x2,res))
            
        case 8:
            print("Thanks for using this program!")
            sys.exit()
            
        case _:
            print("Your choice of operation is wrong!--Try Again")   

    i=i+1  
