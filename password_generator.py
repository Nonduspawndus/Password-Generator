import random
import time

print("Welcome to Python Password Generator")
time.sleep(1)
print("What should be the length of the password?")
leng = input('>')
leng = int(leng)

def step(leng):
    smol = [chr(i) for i in range(97, 97+26)]
    big = [chr(i) for i in range(65, 65+26)]
    digits = [str(i) for i in range(10)]
    spc = ['@', '#', '$', '*', '&', '!']
    pasw = []
    for i in range(leng):
        lc = random.choice([smol, big, digits, spc])
        lch = random.choice(lc)
        pasw.append(lch)
    return ''.join(pasw)
password = step(leng)
print("Your password is", password)






# print("How many numbers should the password contain?")
# numbers = input('>')
# print("How many Uppercase letters should the password contain?")
# bigletters = input('>')
# print("How many Lowercase letters should the password contain?")
# smolletters = input('>')
# print("How many Special characters should the password contain?")
# specialc = input('>')
