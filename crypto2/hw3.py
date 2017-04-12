from hashlib import sha256
from myutils import generatehash

flag = open('flag.txt').read()

def main():
    shasum = generatehash()

    print "Welcome to Workout Server 2017!"
    print "Everybody knows that your brain, just like any other muscle, need a good workout to stay healthy and strong"
    print "This server will help your computer's brain get a workout!"
    print "Find x such that sha2(x).encode('hex')[:6] ==", shasum[:6]

    input_string = raw_input()

    if shasum[:6] == sha256(input_string).digest().encode('hex')[:6]:
        print flag

    else:
        print "Incorrect!"

main()
