from hashlib import sha256
import string
import random

flag = open('flag.txt').read()

def generatehash():
    text = "sometext here" + "".join([random.choice(string.ascii_letters) for _ in range(1,10)])
    #print text
    return sha256(text).digest()

def main():
    shasum = generatehash()

    print "Find x such that sha2(x)[:6] ==", shasum[:6]

    input_string = raw_input()

    if shasum[:6] == sha256(input_string).digest()[:6]:
        print flag

    else:
        print "Incorrect!"

main()
