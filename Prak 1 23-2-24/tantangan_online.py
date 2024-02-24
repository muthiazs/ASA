def bil_prima(n):
    if n <= 1:
        print("Bukan Prima")
        return

    for i in range(2, int(n**0.5) + 1):
     if n % i == 0:
        print("Bukan Prima")
        return

    print("Prima")

n = int(input())
bil_prima(n)
