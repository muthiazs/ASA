def hitungGenap(n, List):
    i = 1
    total = 0
    for i in range (n):
        if List[i] % 2 == 0:
            total += 1
    print(total)

banyakBilangan = int(input())
L = list(map(int, input().split()))
hitungGenap(banyakBilangan, L)