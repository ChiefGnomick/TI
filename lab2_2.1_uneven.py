from collections import Counter
from itertools import product

text = "ЧТО ОН УМЕН И ОЧЕНЬ МИЛ. МЫ ВСЕ УЧИЛИСЬ ПОНЕМНОГУ"

freq = Counter(text)
total = sum(freq.values())
prob = {char: count/total for char, count in freq.items()}
sorted_chars = sorted(prob.items(), key=lambda x: x[1], reverse=True)

# пробел кодируется строго как 000
SPACE_CODE = "000"

def valid_core(bits):
    """Допустима ли внутренняя часть кода (без завершающих 00)."""
    s = ''.join(bits)
    return "00" not in s

def generate_codes(chars):
    codes = {}

    # сначала задаём код пробела
    if " " in [c for c,_ in chars]:
        codes[" "] = SPACE_CODE

    for char, _ in chars:
        if char == " ":
            continue

        # длина "ядра" без конечных 00
        length = 1
        while True:
            for bits in product('01', repeat=length):
                s = ''.join(bits)
                if s[0] != '1':
                    continue
                if not valid_core(bits):
                    continue

                code = s + "00"     # обязательный конец знака

                if code not in codes.values() and code != SPACE_CODE:
                    codes[char] = code
                    break
            if char in codes:
                break
            length += 1

    return codes


codes = generate_codes(sorted_chars)

print(f"{'Буква':<5} {'Код':<10} {'pi':<8} {'ki':<3}")
for char, p in sorted_chars:
    code = codes[char]
    print(f"{char:<5} {code:<10} {p:<8.3f} {len(code):<3}")
