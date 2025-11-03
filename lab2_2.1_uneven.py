from collections import Counter

text = "ЧТО ОН УМЕН И ОЧЕНЬ МИЛ. МЫ ВСЕ УЧИЛИСЬ ПОНЕМНОГУ"

freq = Counter(text.replace('.', '').replace(',', ''))
total = sum(freq.values())
prob = {char: count/total for char, count in freq.items()}

sorted_chars = sorted(prob.items(), key=lambda x: x[1], reverse=True)

def generate_codes(chars):
    codes = {}
    used_codes = set()
    
    def next_code(length):
        """ Генерация следующего кода длины length, начинающегося с 1, без двух нулей подряд в середине """
        from itertools import product
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
        length = 3
        while True:
            code = next_code(length)
            if code:
                codes[char] = code
                break
            length += 1
    return codes

codes = generate_codes(sorted_chars)

# Вывод таблицы
print(f"{'Буква':<5} {'Код':<8} {'pi':<8} {'ki':<3}")
for char, p in sorted_chars:
    code = codes[char]
    k = len(code)
    print(f"{char:<5} {code:<8} {p:<8.3f} {k:<3}")
