def urutanSembako(de,du):
    posisi1 = de.index(du[0])
    posisi2 = de.index(du[1])

    if abs(posisi1 - posisi2)==1:
        print("Ya")
    else:
        print("Tidak")

de = list(map(int, input().split()))
du = list(map(int, input().split()))

urutanSembako(de,du)
