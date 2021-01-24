if __name__ == '__main__':
    print ("enter string\n")
    n = input()
    s = n[:len(n)//2] + n[len(n)//2+2:]
    print(s[::-1])