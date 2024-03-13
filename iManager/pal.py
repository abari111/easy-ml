def palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


if __name__=='__main__':
    print( palindrome("AbA"))