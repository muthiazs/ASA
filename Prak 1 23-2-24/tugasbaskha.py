def tugasBaskha(kata,n):
    panjang = len(kata)
    if panjang < n:
        kali = (n/panjang)
        katabaru = kata * int(kali)
        katabaru = katabaru[:n]
    else:
        katabaru = kata[:n]
    
    jumlah_vokal = 0
    for i in katabaru:
        if i in "aiueo":
            jumlah_vokal += 1
    print(jumlah_vokal)


l = input()
n = int(input())

tugasBaskha(l,n)
