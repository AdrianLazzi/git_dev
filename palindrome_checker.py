"""
palindrome_checker.py
"""

__author__ = "Adrian Lazzi"
__version__ = "2023-02-22"

from atds import Deque

class PalindromeChecker(object): 
    def __init__(self): 
        self.set_strict_mode(False)
    def set_strict_mode(self, state):
        self.strict = state
    def is_palindrome(self, phrase):
        if phrase == "":
            return False
        chars = [".", ",", "/", "?", "\'", "\\", ";", ":", "]", "}", "[", "{", "|", "=", "+", "-", "(", ")", "_", "0", "!", " ", "9", "8", "*", "7", "&", "6", "5", "4", "3", "2", "1", "@", "#", "$"]
        if not self.strict:
            for char in chars: 
                phrase = phrase.replace(char, "")
            phrase = phrase.lower()
            
        deque = Deque()
        for letter in phrase:
            deque.add_rear(letter)
        while deque.size() > 1:
            if deque.remove_front() != deque.remove_rear():
                return False 
        return True

def main(): 
    p = PalindromeChecker()
    strict_mode = input("Do you want strict mode on? (y/N) ")
    if strict_mode.lower() == "y": 
        p.set_strict_mode(True)
    phrase = input("What phrase are you wondering is a palindrome? ")
    is_palindrome = p.is_palindrome(phrase)
    if is_palindrome: 
        print("This phrase is a palindrome!")
    else: 
        print("This phrase is not a palindrome")

if __name__ == "__main__":
    main()