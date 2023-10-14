n = input("nの値を入力: ")
n = int(n)

def jud(n):
    if n <= 1:
        print("nは素数でない")
    for i in range(2, n):
        if n % i == 0:
            print("nは素数でない")
            return
    print("nは素数")
jud(n)