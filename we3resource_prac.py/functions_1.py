def maximum(x,y,z):
    

    if x >= y and x >= z:
        return x
    elif y >= x and y >=z:
        return y
    else :
        return z
    
num_1 = float(input("enter the first num:"))
num_2 = float(input("enter the second num:"))
num_3 = float(input("enter the third num:"))
    
supermax = maximum(num_1, num_2, num_3)
print("The maximum number is:", supermax)
    