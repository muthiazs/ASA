def PetualanganJanggar(n):
        jumlah = 1
        for i in range(2, n + 1):
            if (i % 2 == 0):
                print("Janggar tidak memetik buah ke-" + str(i))
                jumlah += 1
            else:
                print("Janggar telah memetik buah ke-" + str(i))
        print("Jumlah buah yang dipetik Janggar =", jumlah)

n = int(input())
PetualanganJanggar(n)
