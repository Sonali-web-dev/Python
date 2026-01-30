def isSumEqual(firstWord, secondWord, targetWord):
    def get_value(word):
        return int(''.join(str(ord(c) - ord('a')) for c in word))
    
    return get_value(firstWord) + get_value(secondWord) == get_value(targetWord)

