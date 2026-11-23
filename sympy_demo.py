import sympy

n = int(input())
print("Is this a prime number?")
if sympy.isprime(n):
    print("Yes")
else:
    print("No")
    print("Multipliers")
    print(*list(sympy.factorint(n).keys()))
print("Closest prime number")
print(sympy.nextprime(n))
print("Prime numbers less than n")
print(*list(sympy.primerange(1, n)))
