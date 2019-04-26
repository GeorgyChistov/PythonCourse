def prime_numb_gen(n):             #Функция генерирует n-e простое число
    primes = [2]
    add = 3
    while len(primes) <= n-1:
        flag = False           #True, когда число не простое(оно делится на какое-то число из списка)
        for num in primes:
            if add % num == 0:
                flag = True
        if flag:
            add += 1
            continue
        else:
            primes.append(add)
            add += 1
    yield primes[len(primes)-1]
