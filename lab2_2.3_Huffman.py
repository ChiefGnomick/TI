from collections import Counter
import heapq
import itertools

text = "ЧТО ОН УМЕН И ОЧЕНЬ МИЛ. МЫ ВСЕ УЧИЛИСЬ ПОНЕМНОГУ"

freq = Counter(text)
total = sum(freq.values())
prob = {char: count/total for char, count in freq.items()}

counter = itertools.count()
heap = [(p, next(counter), (char, None, None)) for char, p in prob.items()]
heapq.heapify(heap)

while len(heap) > 1:
    p1, _, left = heapq.heappop(heap)
    p2, _, right = heapq.heappop(heap)
    new_node = (None, left, right)
    heapq.heappush(heap, (p1 + p2, next(counter), new_node))

huffman_tree = heap[0][2]

def generate_huffman_codes(node, prefix=''):
    char, left, right = node
    if char is not None:
        return {char: prefix or '0'}
    codes = {}
    if left:
        codes.update(generate_huffman_codes(left, prefix + '1'))
    if right:
        codes.update(generate_huffman_codes(right, prefix + '0'))
    return codes

codes = generate_huffman_codes(huffman_tree)

print(f"{'Символ':<5} {'Код':<10} {'Вероятность':<10}")
for char, p in sorted(prob.items(), key=lambda x: x[1], reverse=True):
    print(f"{char:<5} {codes[char]:<10} {p:<10.8f}")

def print_tree(node, prefix='', branch=''):
    char, left, right = node
    if char is not None:
        print(f"{prefix}{branch}─ {char} ({prob[char]:.3f})")
    else:
        def get_prob(n):
            c, l, r = n
            if c is not None:
                return prob[c]
            return get_prob(l) + get_prob(r)
        node_prob = get_prob(node)
        print(f"{prefix}{branch}─ * ({node_prob:.3f})")
        if left:
            print_tree(left, prefix + "    ", "1")
        if right:
            print_tree(right, prefix + "    ", "0")

print("\nБинарное дерево Хаффмана:")
print_tree(huffman_tree)
