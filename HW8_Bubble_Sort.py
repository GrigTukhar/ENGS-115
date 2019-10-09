def selectionSort():
    n = int(input("Input size of array: "))
    arr = []
    count = 0
    for _ in range(n):
        count = count + 1
        x = int(input("Input element: "))
        arr.append(x)
    print("Inputed Array:" ,arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted Array:",arr)


selectionSort()
