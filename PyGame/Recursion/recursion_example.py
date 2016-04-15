__author__ = 'k_eryomenko'
def f(level):
    print("Recursion call, level ",level)
    if level<10:
        f(level+1)

def factorial_recursive(n):
    if (n==1):
        return n
    else:
        x = factorial_recursive(n-1)
        print(n, "*", x, "=", n*x)
        return n*x

answer = factorial_recursive(8)
print(answer)
