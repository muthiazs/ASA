def kamus700m(kata):
    jumlah = 0
    for i in range(len(kata) - 1):
        if kata[i] == kata[i+1]:
            jumlah += 1
    
    if jumlah == 0:
        print("1")
    else:
        print("0")

kata = input()
kamus700m(kata)
