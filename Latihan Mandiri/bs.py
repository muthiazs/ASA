def binary_search(list, search):
    lower_bound = 0
    upper_bound = len(list) - 1

    while True:
        if upper_bound < lower_bound:
            print("Tidak Ketemu")
            return -1
        i = (lower_bound+upper_bound)//2

        if list[i]<search:
            lower_bound = i + 1
        elif list[i] > search:
            upper_bound = i - 1
        else:
            print("Element " + str(search) + " in " + str(i))
            return 0
        
def linear_search(list,search):
    for i in range(0, len(list)):
        if list[i] == search:
            print("Nilai ditemukan pada posisi " + str(i))
            return 0
    print("Nilai tidak ditemukan")
    return -1

def kali(a,b):
    res = 0 
    for i in range(a):
        for j in range(b):
            res += 1
        print("Hasil kali adalah " + str(res));

def check_number(n):
    if n%2==0:
        if n>2 and n<5:
            print("Not Weird")
        elif n>6 and n<20:
            print("Weird")
        else:
            print("Not Weird")
    else:
        print("Weird")

# Example usage:
check_number(4)

L1 = [ 1,2,3,4,5,6,7,8,9] 
binary_search(L1,7)
linear_search(L1,7)
kali(2,3);

