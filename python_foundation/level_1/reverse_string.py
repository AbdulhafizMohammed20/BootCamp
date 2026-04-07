def reverse_string(s): # this function accepts a string as a parameter

    s = s[::-1] # this is used to reverse a string

    return s # this returns the reversed string

while True:
    s = input()
    print(reverse_string(s))
