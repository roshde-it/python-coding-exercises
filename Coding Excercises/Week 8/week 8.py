# WEEK 8
# type guesser
s = input().strip()

try:
    int(s)
    print("int")
except ValueError:
    try:
        float(s)
        print("float")
    except ValueError:
        print("str")
