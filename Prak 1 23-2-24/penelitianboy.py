def berat(n, List):
    i = 1
    berat = 0
    for i in range (n):
        berat = berat + List[i]
    print(berat)

n= int(input())
L = list(map(int, input().split()))

berat(n,L)
