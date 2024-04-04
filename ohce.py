
from datetime import datetime

def greet(name, t):
    hour = t.hour
    if 20 <= hour or hour < 6:
        return f'¡Buenas noches {name}!'
    elif 6 <= hour < 12:
        return f'¡Buenos días {name}!'
    else:
        return f'¡Buenas tardes {name}!'

def isPalindrome(s1,s2):
    return "¡Bonita palabra!" if s1==s2 else None

def reverseWord(s):
    return s[::-1]

def stop(s):
    return f'Adios {s}'

if __name__ == "__main__":
    name = input("$ ")

    print('> ' + greet(name,datetime.now().time()))

    while True:
        user_input = input("$ ")
        if user_input == "Stop!":
            print(stop(name))
            break
        else:
            reversedWord = reverseWord(user_input)
            print('> ' + reversedWord)
            isNice = isPalindrome(user_input,reversedWord)
            if isNice is not None:
                print('> ' + isNice)

