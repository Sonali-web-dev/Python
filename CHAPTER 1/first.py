s = " A man , a plan , a canal : Panama"
n = ""
for chr in s:
    if(chr.isspace()):continue
    elif(chr.isalnum()):continue
    elif(not chr.isupper()):continue
    n += chr.lower()
else:
    n += chr
    print(n)
    

 
