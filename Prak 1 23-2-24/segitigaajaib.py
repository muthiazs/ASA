def segitigaAjaib(n):
    pascal = []
    for i in range (0,n):
        x = []
        if ( i == 0 ):
            x = x + [1]
        else:
            for j in range (0,(i+1)):
                if ( j== 0 or j==i):
                    x = x + [1]
                else:
                    jumlah = pascal[i-1][j-1] + pascal[i-1][j]
                    x = x + [jumlah]
        pascal = pascal + [x]
    return pascal
    
n = int(input())
segitigaAjaib(n)
        
print(segitigaAjaib(n))
                
    