from collections import Counter
from itertools import product

text = "АААББВГДЕЖЗИ"

# Частоты
freq = Counter(text)
total = sum(freq.values())
prob = {char: count/total for char, count in freq.items()}

# Сортировка по убыванию
sorted_chars = sorted(prob.items(), key=lambda x: x[1], reverse=True)

# Жадный метод с твоими правилами
def generate_codes(chars):
    codes = {}
    used_codes = set()
    
    def next_code(length):
        for bits in product('01', repeat=length):
            code = ''.join(bits)
            if code[0] != '1':
                continue
            if '00' in code[:-2]:
                continue
            if code in used_codes:
                continue
            used_codes.add(code)
            return code
        return None
    
    for char, _ in chars:
        length = 2
        while True:
            code = next_code(length)
            if code:
                codes[char] = code
                break
            length += 1
    return codes

codes_greedy = generate_codes(sorted_chars)

# Shannon-Fano
def shannon_fano(chars):
    if len(chars) == 1:
        return {chars[0][0]: ''}
    total_prob = sum(p for _, p in chars)
    acc = 0
    for i, (_, p) in enumerate(chars):
        acc += p
        if acc >= total_prob/2:
            break
    left = chars[:i+1]
    right = chars[i+1:]
    codes = {}
    for k, v in shannon_fano(left).items():
        codes[k] = '0' + v
    for k, v in shannon_fano(right).items():
        codes[k] = '1' + v
    return codes

codes_sf = shannon_fano(sorted_chars)

# Вывод
print(f"{'Символ':<3} {'Жадный':<6} {'Shannon-Fano':<12}")
for char, _ in sorted_chars:
    print(f"{char:<3} {codes_greedy[char]:<6} {codes_sf[char]:<12}")
    