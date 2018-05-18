import random, math

STARTING_NUMBER=571828182881

def fast_module_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

def pow_basic_presentation(new_prime):
    two_degree = 0
    inner_odd_number = new_prime - 1
    while (inner_odd_number % 2 == 0):
        two_degree += 1
        inner_odd_number /= 2
    return [int(inner_odd_number), int(two_degree)]

def hundred_primes_test(new_prime, prime_tab):
    flag = 0
    if (new_prime>100):
        for i in range (25):
            if (new_prime % prime_tab[i] == 0):
                flag = 1
                break
    return flag

def rabin_miller(inner_odd_number, new_prime):
    attempts = 4
    for _ in range(attempts):
        random_test_number = random.randint(2, new_prime - 2)
        test_equation = pow(random_test_number, inner_odd_number, new_prime)
        if (test_equation == 1) or (test_equation == (new_prime - 1)):
            continue
        for _ in range(two_degree - 1):
            test_equation = pow(test_equation, 2, new_prime)
            if (test_equation == 1):
                return 1
            if (test_equation == (new_prime - 1)):
                break
        if (test_equation == (new_prime - 1)):
                continue
        return 1
    return 4*(-attempts)

# Main

parent_number = int(input('Enter basic number '))
random.seed()
numbers_checked = 0
prime_tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_tab_counter = 0
while True:
    mauer_modifier = random.randint((parent_number + 1)/2, (4 * parent_number + 2)/2) * 2
    new_prime = parent_number * mauer_modifier + 1
    numbers_checked += 1
    basic_representation = pow_basic_presentation(new_prime)
    two_degree = basic_representation[1]
    inner_odd_number = basic_representation[0]
    flag = hundred_primes_test(new_prime, prime_tab)
    if (flag == 1):
        prime_tab_counter += 1
        continue
    if ((rabin_miller(inner_odd_number, new_prime) < 0.01)):
        break
print("Generated prime number:", new_prime)
print("To find it I checked", numbers_checked, "numbers, created with Mauer algorithm")
print(prime_tab_counter, " of them failed on hundred prime numbers division test")