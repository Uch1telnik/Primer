from math import sqrt

def is_prime(n):
    if n == 1:
        return False
    if n <= 3:
        return True
    for i in range(2, int(sqrt(n))+1):
        if fermat_test(n, i):
            return True
    return False

def fermat_test(n, a):
    if pow(a, n-1, n) == 1:
        return True
    else:
        return False

assert is_prime(2)
assert is_prime(3)
assert is_prime(7)
assert is_prime(13)

assert not is_prime(1)
assert not is_prime(4)
assert not is_prime(9)
assert not is_prime(15)
#Не работает для чисел Кармайкла, наименьшее 561
assert not is_prime(561)
print("All tests passed!")