#Crypto
import random, math

STARTING_SIMPLE_NUMBER=571828182881

def fast_module_pow(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

def pow_basic_presentation(new_basic_number):
    two_degree = 0
    inner_basic_number = new_basic_number - 1
    while (inner_basic_number % 2 == 0):
        two_degree += 1
        inner_basic_number /= 2
    return [int(inner_basic_number), int(two_degree)]

def rabin_miller(inner_basic_number, new_basic_number):
    # attempts = int(math.log(new_basic_number, 2))
    attempts = 4
    for _ in range(attempts):
        # print(k, 'In first cycle \n')
        random_test_number = random.randint(2, new_basic_number - 2)
        # temp = fast_module_pow(random_test_number, inner_basic_number, new_basic_number)
        temp = pow(random_test_number, inner_basic_number, new_basic_number)
        if (temp == 1) or (temp == (new_basic_number - 1)):
            continue
        for _ in range(two_degree - 1):
            # print(i, 'In second cycle \n')
            # temp = fast_module_pow(temp, 2, new_basic_number)
            temp = pow(temp, 2, new_basic_number)
            if (temp == 1):
                return 1
            if (temp == (new_basic_number - 1)):
                break
        if (temp == (new_basic_number - 1)):
                continue
        return 1
    return 4*(-attempts)

parent_basic_number = int(input('Enter basic number '))
# parent_basic_number = 571828182881
random.seed()
while True:
    random_temp = random.randint(parent_basic_number + 1, 4 * parent_basic_number + 2)
    # print("Generated random temporary number =", random_temp)
    new_basic_number = parent_basic_number * random_temp + 1
    # print("Generated new ?basic? number =", new_basic_number)
    basic_representation = pow_basic_presentation(new_basic_number)
    # print('here')
    two_degree = basic_representation[1]
    inner_basic_number = basic_representation[0]
    # print("new_basic_number - 1 =", new_basic_number - 1, "= 2 ^", two_degree, "*", inner_basic_number)
    basic_chance = 0
    attempts = int(math.log(new_basic_number, 2))
    # for i in range(attempts):
    #     if (rabin_miller(inner_basic_number, new_basic_number) == True):
    #         basic_chance += 1
    # print('Probablity that new number =', new_basic_number, " is basic =", (basic_chance/attempts)*100, "%")
    if ((rabin_miller(inner_basic_number, new_basic_number) < 0.01)):
        break
print(new_basic_number)
