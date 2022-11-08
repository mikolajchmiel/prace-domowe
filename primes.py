
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]

primes_short = primes[0:3]

result_string = ''

if __name__ == '__main__':
    for prime in primes_short:
        result_string += str(prime) + ' '
    print(result_string)
