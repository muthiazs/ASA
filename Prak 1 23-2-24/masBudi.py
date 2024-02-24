
def catatanBudi(n):
    topping = ["coklat", "stroberi", "keju"]
    x=1
    for j in range(len(topping)):
        for i in range(n // len(topping)):
            print(f"Budi menaburkan topping {topping[j]} di atas kue ke-{x}")
            x=x+1

n = int(input())
catatanBudi(n)

