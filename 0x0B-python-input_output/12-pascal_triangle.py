def pascal_triangle(n):

    for i in range(n):
        # adjust space
        print(''*(n-i), end='')
 
        # compute power of 11
        print("[{}]".format(','.join(map(str, str(11**i)))))
        ret = ''
    return ret