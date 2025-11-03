def gamma_encode(N):
    """Элиас гамма-кодирование числа N"""
    binary = bin(N)[2:]
    prefix = '0' * (len(binary) - 1)
    gamma_code = prefix + binary
    print(f"Гамма-кодирование {N}:")
    print(f"  Двоичное представление: {binary}")
    print(f"  Префикс нулей: {prefix}")
    print(f"  Итоговый гамма-код: {gamma_code}\n")
    return gamma_code

def delta_encode(N):
    """Элиас дельта-кодирование числа N"""
    binary_N = bin(N)[2:]
    L = len(binary_N)
    gamma_L = gamma_encode(L)
    without_msb = binary_N[1:]
    delta_code = gamma_L + without_msb
    print(f"Дельта-кодирование {N}:")
    print(f"  Двоичное представление N: {binary_N}")
    print(f"  L (кол-во бит) = {L}")
    print(f"  Гамма-код L: {gamma_L}")
    print(f"  Двоичное представление без старшей единицы: {without_msb}")
    print(f"  Итоговый дельта-код: {delta_code}\n")
    return delta_code

def omega_encode(N):
    """Элиас омега-кодирование числа N"""
    code = '0'
    trace = ["Начальный ноль: 0"]
    while N > 1:
        binary = bin(N)[2:]
        code = binary + code
        trace.append(f"N={N}, двоичное: {binary}, код слева: {code}")
        N = len(binary) - 1
    print(f"Омега-кодирование исходного числа:")
    for t in reversed(trace):
        print("  " + t)
    print(f"Итоговый омега-код: {code}\n")
    return code

number = 44
print("Примеры кодирования числа:", number)
gamma_code = gamma_encode(number)
delta_code = delta_encode(number)
omega_code = omega_encode(number)
