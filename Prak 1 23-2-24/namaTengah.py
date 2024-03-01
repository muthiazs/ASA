def namaTengah(nama):
    panjang = len(nama)
    huruf = ""
    if panjang % 2 == 0:
        tengah = panjang // 2
        huruf += nama[tengah-1] 
        huruf += nama[tengah]      
    else:
        tengah = panjang // 2
        huruf += nama[tengah]      #
    print(huruf)

nama = input()
namaTengah(nama)

