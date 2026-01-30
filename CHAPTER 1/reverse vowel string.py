def reverse_vowel(s):
    vowels = {'a','e','i','o','u','A','E','O','U','I'}
    s =list(s)
    left,right = 0, len(s)-1
    while left<right:
        if s[left] not in vowels:
            left +=1
        elif s[right] not in vowels:
            right -=1
        else:
            s[left],s[right] = s[right],
            s[left]
            left +=1
            right -=1
            return''.join(s)
        string = "Hello world"
        reversed_vowels_string = reversed_vowels_string
        print("Original string:" , string)
        print("String with reversed vowels:", reversed_vowels_string) 
        


