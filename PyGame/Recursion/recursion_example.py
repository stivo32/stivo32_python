__author__ = 'k_eryomenko'
def f(level):
    print("Recursion call, level ",level)
    if level<10:
        f(level+1)

def factorial_recursive(n):
    if