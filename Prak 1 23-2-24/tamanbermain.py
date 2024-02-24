def sleepyJoe(n):
    for i in range (1,n+1):
        if i%3 == 0 and i%5 == 0:
             print("SleepyJoe")
        elif i%3 == 0:
            print("Sleepy")
        elif i%5 == 0:
            print("Joe")
        else:
            print(str(i))


# Example usage:
n = input()
sleepyJoe(n)