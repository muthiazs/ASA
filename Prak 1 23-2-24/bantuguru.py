def mainGuru(n):
    i =  1
    total = 0
    if(n <= 0):
        print("Harus Bilangan Bulat Positif")
    else:
        for i in range (1, n + 1):
            if i % 2 != 0:
                total = total + i
    print(total)
n = input()
mainGuru(n)

