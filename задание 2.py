def get_lists_of_pime_number_and_of_power_of_prime_number(n):
    list_of_prime_number = []
    list_of_power_prime_number = []
    i = 0
    divider = 2
    while divider * divider <= n:
        list_of_power_prime_number.append(0)
        while n % divider == 0:
            if list_of_prime_number.count(divider) == 1:
                list_of_power_prime_number[i] += 1
            else:
                list_of_prime_number.append(divider)
                n //= divider
                list_of_power_prime_number[i] += 1
        divider += 1
        i += 1
    if n > 1:
        list_of_prime_number.append(n)
        list_of_power_prime_number.append(1)
    return list_of_prime_number, list_of_power_prime_number
 
list1, list2 = get_lists_of_pime_number_and_of_power_of_prime_number(int(input()))
for i in range(len(list1) - 1):
    print(f"{list1[i]}^{list2[i]}*", sep="", end="")
print(f"{list1[-1]}^{list2[-1]}", sep="", end="")