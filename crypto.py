import random, math

STARTING_NUMBER = 571828182881

def pow2(base, degree, module):
    result = base
    bin_degree = "{:b}".format(degree)
    bin_degree = bin_degree[1:]
    for bit in bin_degree:
        result = ((result ** 2) * (base ** int(bit))) % module
    return result

def gcd(first_num, second_num):
  while second_num:
    first_num, second_num = second_num, first_num % second_num
  return first_num

def maurer_number(parent_number):
    maurer_modifier = random.randint((parent_number + 1) / 2, (4 * parent_number + 2) / 2) * 2
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
    flag = 0 # test passed
    if (new_prime > 100):
        for i in range (25):
            if (new_prime % prime_tab[i] == 0):
                flag = 1 # test failed
                break
    return flag

def rabin_miller(inner_odd_number, new_prime, two_degree):
    test_number = random.randint(1, new_prime - 1)
    if (gcd(new_prime, test_number) != 1):
        return 1 # test_number is "good"
    else:
        if (pow2(test_number, inner_odd_number, new_prime) == 1):
            return 0 # test_number is "bad"
        for i in range(two_degree - 1):
            if (pow2(test_number, pow(2, i) * inner_odd_number, new_prime) == -1):
                return 0 # test_number is "bad"
        return 1 # test_number is "good"

def maurer_final_test(new_prime, maurer_modifier):
    for i in range(30):
        if i == 0:
            test_number = 2
        else:
            test_number = random.randint(2, new_prime - 2)
        if ((pow2(test_number, new_prime - 1, new_prime) == 1) and (gcd(pow(test_number, maurer_modifier)-1, new_prime) == 1)):
            return True # test passed
    return False # test failed

# Main:values
numbers_checked = 0
prime_tab = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
hundred_primes_test_fail = 0
rabin_fail_counter = 0
maurer_final_test_fail_counter = 0
# Main:algo
parent_number = int(input('Enter prime number '))
random.seed()
while True:
    new = maurer_number(parent_number)
    new_prime = new[0]
    maurer_modifier = new[1]
    numbers_checked += 1
    basic_representation = pow_basic_presentation(new_prime)
    two_degree = basic_representation[1]
    inner_odd_number = basic_representation[0]
    if (hundred_primes_test(new_prime, prime_tab) == 1):
        hundred_primes_test_fail += 1
        continue
    rabin_test_result = 0
    for _ in range(5):
        rabin_test_result += rabin_miller(inner_odd_number, new_prime, two_degree)
        if (rabin_test_result != 0):
            break
    if (rabin_test_result != 0):
        rabin_fail_counter += 1
        continue
    elif (maurer_final_test(new_prime, maurer_modifier) == True):
        break
    else:
        maurer_final_test_fail_counter += 1
# Main:output   
print("Generated prime number:", new_prime)
print("To find it I checked", numbers_checked, "numbers, created with Maurer algorithm")
print(hundred_primes_test_fail, " of them failed on hundred primes division test")
print(rabin_fail_counter, " of them failed on Rabin-Miller test")
print(maurer_final_test_fail_counter, " of them failed on Maurer final test")