import sys
import os

def add(a,b):
    c = a+b
    return c


def sub(a,b):
    c = a-b
    return c

def mul(a,b):
    c = a*b
    return c

action = sys.argv[1]

if action == "add":
    output = add(int(sys.argv[2]), int(sys.argv[3]))
elif action == "mul":
    output = mul(int(sys.argv[2]), int(sys.argv[3]))
elif action == "sub":
    output = sub(int(sys.argv[2]),int(sys.argv[3]))
else:
    print("invalid")

print(output)

o=os.getenv("apio")
l=os.getenv("")
print(o)