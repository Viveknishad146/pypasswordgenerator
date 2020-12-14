import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    #print(s1)
    s2 = string.ascii_uppercase
    #print(s2)
    s3 = string.digits
    #print(s3)
    s4 = string.punctuation
    #print(s4)
    while True:
        try:
            plen = int(input("enter password length\n"))#TODO1 : Handle Gibberish
            break
        except ValueError:
            print("oops that's not valid number try again")
    s = []
    s.extend(list(s1))
    s.extend(list(s))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)
    # print(s)
    print("your password is: ")
    print("".join(s[0:plen]))

       

