import sys

def anagram():
    a = input("Enter your first string!\n")
    b = input("Enter your second string!\n")
    a = a.replace(" ", "")
    b = b.replace(" ", "")
    a = a.lower()
    b = b.lower()
    if len(a) == len(b):
        for i in a:
            if i in b:
                continue
            else:
                sys.exit("These strings are not anagrams!")
                
            
        for j in b:
            if j in a:
                continue
            else:
                sys.exit("These strings are not anagrams!")
        print("These strings are anagrams!")
    else:
        sys.exit("These strings are not anagrams!")


anagram()


