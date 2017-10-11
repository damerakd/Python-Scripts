if __name__ == '__main__':
    from collections import Counter
    numshoes = int(raw_input())
    lst = map(int,raw_input().split())
    lst = Counter(lst)
    numcust = int(raw_input())
    tmoney = 0
    for i in range(0,numcust):
        size, price = map(int, raw_input().split())
        if lst[size]:
            tmoney += price
            lst[size] -= 1
    print tmoney
