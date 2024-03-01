def okegas(n,tabungan):
    k = eval(tabungan)
    jumlah = 0
    jumlah_tabungan = sum(k)
    setengah = False
    cukup = False
    for i in range(len(k)):
        jumlah += k[i]
        if jumlah >= n/2 and not setengah:
            print("Sedikit lagi! Tabungan kamu udah setengahnya dalam waktu" , i+1 , "hari.")
            setengah = True
            
    if jumlah_tabungan >= n and not cukup:
            print("Keren! Tabungan kamu cukup dalam waktu", i+1, "hari.")
            cukup = True


n = int(input())
k = input()
okegas(n,k)