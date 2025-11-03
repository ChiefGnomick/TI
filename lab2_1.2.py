subsequence = "10101100101000000011011110000101000111010110111101100110000001011110111101001101110111110111"

codes = {
    "000": " ",
    "001": "о",
    "0100": "е,ё",
    "0101": "а",
    "0110": "и",
    "0111": "т",
    "1000": "н",
    "1001": "с",
    "10100": "р",
    "10101": "в",
    "10110": "л",
    "10111": "к",
    "11000": "м",
    "110010": "д",
    "110011": "п",
    "110100": "у",
    "110110": "я",
    "110111": "ы",
    "111000": "з",
    "111001": "ь,ъ",
    "111010": "б",
    "111011": "г",
    "111100": "ч",
    "1111010": "й",
    "1111011": "х",
    "1111100": "ж",
    "1111101": "ю",
    "11111100": "ш",
    "11111101": "ц",
    "11111110": "щ",
    "111111110": "э",
    "111111111": "ф"
}

def decode_shannon_fano(seq: str):
    """Пошаговое декодирование строки с трассировкой."""
    result = []
    buffer = ""
    steps = []
    for bit in seq:
        buffer += bit
        if buffer in codes:
            char = codes[buffer]
            used_bits = sum(len(code) for code, _, _ in steps)
            remaining = seq[used_bits + len(buffer):]
            steps.append((buffer, char, remaining))
            result.append(char.split(',')[0])
            buffer = ""
    if buffer:
        steps.append((buffer, "Неизвестный код", "—"))
    return steps, "".join(result)

steps, decoded_text = decode_shannon_fano(subsequence)

print("Исходная последовательность:", subsequence)
print("\nШаги декодирования:")
for i, (code, char, remaining) in enumerate(steps, 1):
    print(f"{i:2}. {code:<9} -> {char:<6} | Остаток: {remaining if remaining else '—'}")

print("\nРезультат:", decoded_text)
