def fibonanci(n):
    if n <= 1:
        return n
    else:
        return fibonanci(n-1)+fibonanci(n-2)

def pesanAlvin(n):
    fn = fibonanci(n)
    print(fn)

n = int(input())
pesanAlvin(n)