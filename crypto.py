import random, math

STARTING_NUMBER=571828182881

def fast_module_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

def pow2(base, degree, module):
    result = base
    # i = 0
    bin_degree = "{:b}".format(degree)
    bin_degree = bin_degree[1:]
    for bit in bin_degree:
        # if i == 0:
            # print(bit, "| a", i, "=", result, "mod", module, "| iteration ##", i)
            # i = i + 1
            # continue
        # else:
        result = ((result ** 2) * (base ** int(bit))) % module
            # if bit == "0":
            #     result = (result ** 2) % module
            # else:
            #     result = ((result ** 2) * base) % module
            # print(bit, "| a", i, "=", result, "mod", module, "| iteration #", i)
            # i = i + 1
    return result


# def gcd(first_num, second_num):
#     while first_num != second_num:
#         if first_num > second_num:
#             first_num = first_num - second_num
#         else:
#             second_num = second_num - first_num        
#     return first_num 

def gcd(first_num, second_num):
  while second_num:
    first_num, second_num = second_num, first_num % second_num
  return first_num

def maurer_number(parent_number):
    maurer_modifier = random.randint((parent_number + 1)/2, (4 * parent_number + 2)/2) * 2
    new_prime = parent_number * maurer_modifier + 1
    return [int(new_prime), int(maurer_modifier)]

def pow_basic_presentation(new_prime):
    two_degree = 0
    inner_odd_number = new_prime - 1
    while (inner_odd_number % 2 == 0):
        two_degree += 1
        inner_odd_number /= 2
    return [int(inner_odd_number), int(two_degree)]

def hundred_primes_test(new_prime, prime_tab):
    flag = 0
    if (new_prime > 100):
        for i in range (25):
            if (new_prime % prime_tab[i] == 0):
                flag = 1
                break
    return flag

def rabin_miller_v2(inner_odd_number, new_prime, two_degree):
    random_test_number = random.randint(1, new_prime - 1)
    # print('Selected a number =', random_test_number)
    if (gcd(new_prime, random_test_number) != 1):
        # print("Checked (", random_test_number, ",", new_prime, ") != 1. Result = True. a - good number, new_prime - composite")
        return 1
    else:
        if (pow2(random_test_number, inner_odd_number, new_prime) == 1):
            return 0
        for i in range(two_degree - 1):
            if (pow2(random_test_number, pow(2, i) * inner_odd_number, new_prime) == -1):
                return 0
        return 1

def mauer_final_test(new_prime, maurer_modifier):
    for i in range(30):
        if i == 0:
            random_test_number = 2
        else:
            random_test_number = random.randint(2, new_prime - 2)
        # print(i, "(in maurer_final_test)")
        print('#' * 50)
        print('args:', random_test_number, new_prime - 1, new_prime)
        print('2args:', random_test_number, maurer_modifier, new_prime)
        if ((pow2(random_test_number, new_prime - 1, new_prime) == 1) and (gcd(pow(random_test_number, maurer_modifier)-1, new_prime) == 1)):
        # x = pow(random_test_number, maurer_modifier, new_prime)-1
        # print("I am in maurer_final_test and going to count if gcd(", x, "," , new_prime,")==1")
        #if (gcd(pow(random_test_number, maurer_modifier, new_prime)-1, new_prime) == 1):
            # print("(TRUE in maurer_final_test on iteration #)", i)
            return True
        # else:
            # print("meh #", i)
    # print("(False in maurer_final_test)")
    return False

# Main

parent_number = int(input('Enter basic number '))
random.seed()
numbers_checked = 0
prime_tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime_tab_counter = 0
rabin_fail_counter = 0
mauer_final_test_fail_counter = 0
while True:
    new = maurer_number(parent_number)
    new_prime = new[0]
    maurer_modifier = new[1]
    numbers_checked += 1
    basic_representation = pow_basic_presentation(new_prime)
    two_degree = basic_representation[1]
    inner_odd_number = basic_representation[0]
    flag = hundred_primes_test(new_prime, prime_tab)
    if (flag == 1):
        prime_tab_counter += 1
        continue
    rabin_test_result = 0
    for _ in range(5):
        rabin_test_result += rabin_miller_v2(inner_odd_number, new_prime, two_degree)
        if (rabin_test_result != 0):
            break
    if (rabin_test_result != 0):
        rabin_fail_counter += 1
    elif (mauer_final_test(new_prime, maurer_modifier) == True):
        break
    else:
        mauer_final_test_fail_counter += 1
        
print("Generated prime number:", new_prime)
print("To find it I checked", numbers_checked, "numbers, created with maurer algorithm")
print(prime_tab_counter, " of them failed on hundred prime numbers division test")
print(rabin_fail_counter, " of them failed on rabin-miller test")
print(mauer_final_test_fail_counter, " of them failed on mauer_final_test_fail_counter")

# POW2TEST
# random.seed()
# flag = True
# for _ in range(50):
#     a = random.randint(2, 100000000)
#     b = random.randint(2, 100000000)
#     c = random.randint(2, 100000000)
#     if pow(a, b, c) != pow2(a, b, c):
#         flag = False
# print(flag)
# # print(pow(a, b, c), pow2(a, b, c))
# print("for a =", a, "b =", b, "c =", c, "|", "pow =", pow(a, b, c), "| pow2 = ", pow2(a, b, c))