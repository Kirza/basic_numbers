#Crypto
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
    # attempts = int(math.log(new_prime, 2))
    attempts = 4
    for _ in range(attempts):
        # print(k, 'In first cycle \n')
        random_test_number = random.randint(2, new_prime - 2)
        # test_equation = fast_module_pow(random_test_number, inner_odd_number, new_prime)
        test_equation = pow(random_test_number, inner_odd_number, new_prime)
        if (test_equation == 1) or (test_equation == (new_prime - 1)):
            continue
        for _ in range(two_degree - 1):
            # print(i, 'In second cycle \n')
            # test_equation = fast_module_pow(test_equation, 2, new_prime)
            test_equation = pow(test_equation, 2, new_prime)
            if (test_equation == 1):
                return 1
            if (test_equation == (new_prime - 1)):
                break
        if (test_equation == (new_prime - 1)):
                continue
        return 1
    return 4*(-attempts)

parent_number = int(input('Enter basic number '))
# parent_number = 571828182881
random.seed()
numbers_checked = 0
prime_tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_tab_counter = 0
while True:
    mauer_modifier = random.randint((parent_number + 1)/2, (4 * parent_number + 2)/2) * 2
    # print("Generated random temporary number =", mauer_modifier)
    new_prime = parent_number * mauer_modifier + 1
    numbers_checked += 1
    # print("Generated new ?basic? number =", new_prime)
    basic_representation = pow_basic_presentation(new_prime)
    # print('here')
    two_degree = basic_representation[1]
    inner_odd_number = basic_representation[0]
    # print("new_prime - 1 =", new_prime - 1, "= 2 ^", two_degree, "*", inner_odd_number)
    # basic_chance = 0
    # attempts = int(math.log(new_prime, 2))
    # for i in range(attempts):
    #     if (rabin_miller(inner_odd_number, new_prime) == True):
    #         basic_chance += 1
    # print('Probablity that new number =', new_prime, " is basic =", (basic_chance/attempts)*100, "%")
    flag = hundred_primes_test(new_prime, prime_tab)
    if (flag == 1):
        prime_tab_counter += 1
        continue
    if ((rabin_miller(inner_odd_number, new_prime) < 0.01)):
        break
    # print('New number', new_prime, "is not basic")
print("Generated prime number:", new_prime)
print("To find it I checked", numbers_checked, "numbers, created with Mauer algorithm")
print(prime_tab_counter, " of them failed on hundred prime numbers division test")