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
        min_i = i
        for j in range(i+1, n):
            if arr[min_i]>arr[j]:
                min_i=j
        arr[i],arr[min_i]=arr[min_i],arr[i]
    print("Sorted Array:",arr)



selectionSort()
