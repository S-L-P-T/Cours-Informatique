def syracuse(n):
    a = 0
    if n == 0:
        print("non")
    else:
        print(a," ",n)
        while n != 1:
            if (n % 2) == 0:
                n = n//2
                a = a+1
                print(a," ",n)
            else:
                n = (n*3)+1
                a = a+1
                print(a," ",n)

syracuse(20)