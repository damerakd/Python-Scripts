if __name__ == '__main__':
    largest = None
    smallest = None
    while True:
        num = input("Enter a number: ")
        if num == "done" : break
        try :
            fnum = float(num)
        except :
            print("Invalid input")
            continue
        if smallest is None and largest is None :
            smallest = fnum
            largest = fnum
        elif fnum < smallest :
            smallest = fnum
        elif fnum > largest:
            largest = fnum
    print("Maximum is", float(largest))
    print("Minimum is", float(smallest))
