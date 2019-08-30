def sum():
    n = int(input("Input size of array: "))
    arr = []
    brr = []
    count = 0
    for _ in range(n):
        count = count + 1
        x = int(input("Input element: "))
        arr.append(x)
        if (count == 1):
            brr.append(x)
        else:
            brr.append(x+y)
        y = max(brr)
    print("Original array:" ,arr)
    print("New array:",brr)


sum()
