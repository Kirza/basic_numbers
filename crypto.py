import random, math

STARTING_NUMBER=571828182881

def fast_module_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

def gcd(first_num, second_num):
    while first_num != second_num:
        if first_num > second_num:
            first_num = first_num - second_num
        else:
            second_num = second_num - first_num        
    return first_num 

def maurer_number(parent_number):
    maurer_modifier = random.randint((parent_number + 1)/2, (4 * parent_number + 2)/2) * 2
    new_prime = parent_number * maurer_modifier + 1
    return new_prime

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
    # attempts = 5
    # for _ in range(attempts):
        random_test_number = random.randint(2, new_prime - 2)
        test_equation = pow(random_test_number, inner_odd_number, new_prime)
        if (test_equation == 1) or (test_equation == (new_prime - 1)):
            return 1
        for _ in range(two_degree - 1):
            test_equation = pow(test_equation, 2, new_prime)
            # if (test_equation == 1):
            #     return 1
            if (test_equation == (new_prime - 1)):
                return 1
        # if (test_equation == (new_prime - 1)):
                # return 
        return 0
    # return 4*(-attempts)

def rabin_miller_v2(inner_odd_number, new_prime, two_degree):
    random_test_number = random.randint(2, new_prime - 2)
    print('Selected a number =', random_test_number)
    if (gcd(new_prime, random_test_number) != 1):
        print("Checked (", random_test_number, ",", new_prime, ") != 1. Result = True. a - good number, new_prime - composite")
        return 1
    else:
        print("Checked (", random_test_number, ",", new_prime, ") != 1. Result = False. Proceeding to second condition")
        print(new_prime, "- 1 = 2 ^", two_degree, "*", inner_odd_number)
        print("So it will be", two_degree + 1, "conditions")
        even_counter = int((two_degree + 1) / 2)
        for i in range(even_counter):
            if ((pow(random_test_number, pow(2, i) * inner_odd_number, new_prime) == 1)):
                print("#1", random_test_number, "^", pow(2, i) * inner_odd_number, "== 1 mod ", new_prime)
                return 0
            else:
                print("#2", random_test_number, "^", pow(2, i) * inner_odd_number, "!= 1 mod ", new_prime)
            if ((pow(random_test_number, pow(2, i) * inner_odd_number, new_prime) == -1)):
                print("#3", random_test_number, "^", pow(2, i) * inner_odd_number, "== -1 mod ", new_prime)
                return 0
            else:
                print("#4", random_test_number, "^", pow(2, i) * inner_odd_number, "!= -1 mod ", new_prime)
        if ((two_degree + 1) % 2 == 1):
            if (pow(random_test_number, pow(2, even_counter) * inner_odd_number, new_prime) == 1):
                print("#5", random_test_number, "^", pow(2, even_counter) * inner_odd_number, "== 1 mod ", new_prime)
                return 0
            else:
                print("#6", random_test_number, "^", pow(2, even_counter) * inner_odd_number, "!= 1 mod ", new_prime)
        return 1

# Main

parent_number = int(input('Enter basic number '))
random.seed()
numbers_checked = 0
prime_tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_tab_counter = 0
rabin_fail_counter = 0
while True:
    new_prime = maurer_number(parent_number)
    numbers_checked += 1
    basic_representation = pow_basic_presentation(new_prime)
    two_degree = basic_representation[1]
    inner_odd_number = basic_representation[0]
    flag = hundred_primes_test(new_prime, prime_tab)
    if (flag == 1):
        prime_tab_counter += 1
        continue
    rabin_test_result = 1
    for _ in range(4):
        rabin_test_result *= rabin_miller(inner_odd_number, new_prime)
    if rabin_test_result == 1:
        break
    else:
        rabin_fail_counter += 1
print("Generated prime number:", new_prime)
print("To find it I checked", numbers_checked, "numbers, created with maurer algorithm")
print(prime_tab_counter, " of them failed on hundred prime numbers division test")
print(rabin_fail_counter, " of them failed on rabin-miller test")

rabin_miller_v2_result = rabin_miller_v2(inner_odd_number, new_prime, two_degree)
if (rabin_miller_v2_result == 0):
    print ("a test number is bad, maybe new_prime is prime")
else:
    print("a test number is good, new_prime is composite")