
from datetime import time

def greet(name, t):
    hour = t.hour
    if 20 <= hour or hour < 6:
        return f'¡Buenas noches {name}!'
    elif 6 <= hour < 12:
        return f'¡Buenos días {name}!'
    else:
        return f'¡Buenas tardes {name}!'

def isPalindrome(s1,s2):
    return

def reverseWord(s):
    return s[::-1]

def stop(s):
    return

