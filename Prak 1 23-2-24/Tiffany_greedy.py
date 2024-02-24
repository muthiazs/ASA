def hitung(a):
    array = eval(a)
    sorted_array = sorted(array,reverse=True)
    total = sum(sorted_array[:3])
    print(total)

array = input()
hitung(array)