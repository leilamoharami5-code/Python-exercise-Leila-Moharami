#برنامه ای بنویسید ک از کاربر رمز دریافت کند
#algoritm:
#start
#daryafte input
#baresi len password
#baresi upper
#baresi lower
#baresi digit -> adad
#baresi character -> #@$%-.
#agar shart bargharar nabod -> print reason
#agar hame shart brgharar bod -> print pass ok
#end

error = []
has_upper = False
has_lower = False
has_digit = False
has_ch = False


pass1 = input(" ENTER YOUR PASSWORD: ")
ch = "@#$%&!-._"
if len(pass1) < 8:
    error.append("your password is less than 8 characters")
for i in pass1:
    if i.isupper():
        has_upper = True
    if i.islower():
        has_lower = True
    if i.isdigit():
        has_digit = True
    if i in ch:
        has_ch = True
#if not has_upper:-> man daram migam meghdar ghabli to shod true 
#hala barax on not hasupper yani false bod khata ha ro chap kon
if not has_upper: 
    error.append("Your password doesn't have capital letters!")
if not has_lower:
    error.append("Your password doesn't have small letters!")
if not has_digit:
    error.append("Your password doesn't have number")
if not has_ch:
    error.append("Your password doesn't have any charactor")
if len(error) == 0:
    print("valid")
else:
    for i in error:
        print(i)
            
            
   
        
        
    
    
    
    
    
    
    
    
    
    