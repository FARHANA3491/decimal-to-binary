decimal = 77
res = ""
if decimal == 0:
    print("0")
   
    
while decimal > 0:
    rem = decimal % 2
    res = str(rem) + res
    decimal //= 2
    
print(res)
