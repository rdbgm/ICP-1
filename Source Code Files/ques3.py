if __name__ == '__main__':
    print("Enter the string\n")
    s = input() # enter input in console
    for i in s.split():   # split() function used to split the given string
        if i == "Python":
            s = s.replace(i,"Pythons")   #replacing Python with Pythons
        elif i == "python":
            s = s.replace(i,"pythons")     #replacing python with pythons
    print(s)