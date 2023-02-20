print("This is python using VS_CODE")
print(5 + 6)

# a = 5
# b = 2

# try:
#     print(a/b)
# except ZeroDivisionError as ze:
#       print(ze)
      
try:
    a = int(input("Enter the value of a :"))
    b = int(input("Enter the value of b :"))

    try:
        c = a * b
        print(c)
    except:
        print('Error while multiplication')
    
    try:
        d = a / b
        print(d)
    except ZeroDivisionError as ze:
        print(ze)
        
    try:
        e = a + b
        print(e)
    except:
        print('Error while addition')
    
except:
    print("Error in your program check the input")