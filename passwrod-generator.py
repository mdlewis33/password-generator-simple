import random as rd
from random_word import RandomWords
import string

# Generates a simple password which is a combination of 2 words or just one word.
# Returns the completed password
def simple_password():
    r = RandomWords()
    rd_num = rd.randint(1,2)
    password = ""
    
    for x in range(rd_num):
        password += r.get_random_word()

    return password

# Genarates a meduim password which ranges from a length of 6 to 12 with random letters which could be capitalized or lowercased.
def meduim_password():
    rd_num = rd.randint(6,12)
    password = ""
    
    for x in range(rd_num):
        password += rd.choice(string.ascii_letters)

# Generates a strong password wich ranges from a length of 6 to 12 with random letters, which could be capitalized or lowercased, numbers, and punctuation.
def strong_password():
    pass_char = string.ascii_letters + string.digits + string.punctuation
    rd_num = rd.randint(6,12)
    password = ""
    
    for x in range(rd_num):
        password += rd.choice(pass_char)
