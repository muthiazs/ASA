def FikBazz(n):
    for i in range (1,n+1):
        if i%3 == 0 and i%5 == 0:
             print("Fikk Bazz")
        elif i%3 == 0:
            print("Fikk")
        elif i%5 == 0:
            print("Bazz")
        else:
            print(str(i))


# Example usage:
n = int(input())
FikBazz(n)