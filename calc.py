num1= float(input("Enter the first Number format # + x = # > "))

op = input("Enter the operator: ")

num2= float(input("Enter the 3nd Number #+x=# >  "))

if op =="+" :
    print(f'x+{num1} = {num2}  x = {num2 + num1}')

if op == "-":
    print(f'x-{num1} = {num2}  x = {num2 - num1}')
    
if op == "*" : 
    print(f'x*{num1} = {num2}  x = {num2 / num1}') 

if op == "/" :
    print(f'x/{num1} = {num2}  x = {num2 * num1}')    

else:
    print("pls redo your equation.")
