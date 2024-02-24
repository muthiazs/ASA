def bintangTerbalik(n):
    for i in range(n, 0, -1): #n untuk nilai awal , 0 untuk nilai akhir , dan -1 untuk prosesnya 
        for j in range(i):  
            print("*", end="")  
        print()

n = int(input())
bintangTerbalik(n)
