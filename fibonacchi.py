

def fibonacchi(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        print(a, end=" ")

n = int(input("Enter a number: "))
fibonacchi(n)