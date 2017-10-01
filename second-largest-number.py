if __name__ == '__main__':
    n = int(raw_input())
    a = None
    b = None
    j = 0
    arr = map(int, raw_input().split())
    for i in range(0,len(arr)):
        if a is None and arr[i] > a:
            a = arr[i]
        if arr[i] > a:
            a = arr[i]
    rem = arr.count(a)
    while j < rem :
        arr.remove(a)
        j = j + 1
    for i in range(0,len(arr)):
        if b is None and arr[i] > b:
            b = arr[i]
        if arr[i] > b:
            b = arr[i]
    print(b)
