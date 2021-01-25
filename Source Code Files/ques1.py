#defining main function
if __name__ == '__main__':

    print(type("Python"))      #prints type
    print(type(b"Python"))     #prints type of bytes stored

    a=7
    b=2
    result=a/b
    print(result) #gives the expected result with float value

    print("Python")

    list = [1,2,3,4,5,6,7,8]
    for i in range(1,5):    #range funtion iterates the list
        print(i),
    for i in xrange(1,5):    #NameError: name 'xrange' is not defined
        print(i)




