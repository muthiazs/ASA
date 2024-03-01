def kombinasi_password(n):
    def pengombinasi(password):
        if len(password) == n:
            results.append(password)
            return
        pengombinasi(password + 'a')
        if len(password)==0 or password[-1] != 'b':
            pengombinasi(password + 'b')
    results = []
    pengombinasi('')
    return results
n = int(input())
passwords = kombinasi_password(n)
for password in passwords:
    print(password)



