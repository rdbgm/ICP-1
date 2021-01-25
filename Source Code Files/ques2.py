if __name__ == '__main__':
    print ("enter string\n")
    n = input() # enter input in console
    s = n[:len(n)//2] + n[len(n)//2+2:] # len() function is used to traverse the string through half the way and skip 2 characters
    print("Output string is :\n",s[::-1]) #prints the resultant string in reverse