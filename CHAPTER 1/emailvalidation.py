email = input(" Enter your Email : ")#g@g.in, wscube@gmail.com
if len(email)>=6:
    if email[0].isalpha():
        #.isalpha () is a string function which tells the alphab.. otherwise it returns F
        if "@" in (email) and (email.count()==1) :
            
        pass
    else:
        print(' Wrong email 2')
    pass
else:
    print("Wrong email 1")
