# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?


def largest_prime(num, div=2):

    while div < num:

        if num % div == 0 and num / div > 1:
            num = num / div
            div = 2
        else:
            div = div + 1
    return num


x = largest_prime(600851475143, 2)
print(x)
