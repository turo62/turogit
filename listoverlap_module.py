def listoverlap(list1, list2):
    c = []
    for items in list1:
        if items in list2 and items not in c:
            c.append(items)
    print(c)
    return c


def main():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    listoverlap(a, b)
    

if __name__ == '__main__':
    main()
