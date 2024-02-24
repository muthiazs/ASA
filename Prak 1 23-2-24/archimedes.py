def faktorBilangan(n):
    faktor = []
    for i in range (1 , n+1):
        if n % i == 0:
            faktor.append(i)
    print(faktor)

n = int(input())
faktorBilangan(n)
