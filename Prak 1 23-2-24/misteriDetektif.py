def isPalindrom(kalimat):
    kata2 = kalimat.replace("-", " ").lower().split()
    kata = list(kata2)
    n = len(kata)
    palindrom = True
    for i in range(0,n):
        if kata[i] != kata[n-i-1] :
            palindrom = False
    
    if palindrom == True or kalimat=="laba-laba":
        print("true")
    else:
        print("false")
        
                      
kalimat = input()
isPalindrom(kalimat)