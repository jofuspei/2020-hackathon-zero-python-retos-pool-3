#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    #
    #
    chars=string.ascii_letters + string.digits + string.punctuation
    #
    #

    return "".join(random.choice(chars) for _ in range(int(passLen)))

print(RandomPasswordGenerator(str(input("Longitud: "))))
