from collections import Counter

text = "ЧТО ОН УМЕН И ОЧЕНЬ МИЛ. МЫ ВСЕ УЧИЛИСЬ ПОНЕМНОГУ"

freq = Counter(text)
total = sum(freq.values())
prob = {char: count/total for char, count in freq.items()}

sorted_chars = sorted(prob.items(), key=lambda x: x[1], reverse=True)

def shannon_fano(chars):
    if len(chars) == 1:
        return {chars[0][0]: ''}
    total_prob = sum(p for _, p in chars)
    acc = 0
    for i, (_, p) in enumerate(chars):
        acc += p
        if acc >= total_prob / 2:
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

print(f"{'Буква':<3} {'Shannon-Fano':<12} {'pi':<6}")
for char, p in sorted_chars:
    code = codes_sf[char]
    print(f"{char:<3} {code:<12} {p:<.3f}")
