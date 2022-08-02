# Password Generator
import random, string

length_pass = int(input("What is the length of the password?"))  #user input to get the length of the requested password
num_in_pass = input("Do you wont numbers in your password (yes/no)?")  #user input to now if he wants numbers in the password
if num_in_pass.lower == "yes":
    num_in_pass = True
else:
    num_in_pass = False
strength_of_pass = input("What is the strength of the password (weak, strong, very strong)?").lower()  #user input to get the strength of the password


def password(length, num=False, strength='weak'):
    """length- the length of the password
    num- if you wont numbers in your password
    strength- weak, strong, very"""
    lower= string.ascii_lowercase
    upper = string.ascii_uppercase
    letters = lower + upper
    dig = string.digits
    punct = string.punctuation
    pwd = ''

    # Generate weak password
    if strength == 'weak':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(lower)

    # Generate strong password
    elif strength == 'strong':
        if num:
            length -= 2
            for i in range(2):
                pwd += random.choice(dig)
        for i in range(length):
            pwd += random.choice(letters)

    # Generate very strong password
    elif strength == 'very strong':
        ran = random.randint(2, 4)
        if num:
            length -= ran
            for i in range(ran):
                pwd += random.choice(dig)
        length -= ran
        for i in range(ran):
            pwd += random.choice(punct)
        for i in range(length):
            pwd += random.choice(letters)

    pwd = list(pwd)
    random.shuffle(pwd)
    return ''.join(pwd)


print("Your new password is:", password(length_pass, num_in_pass, strength_of_pass))

