import sympy as sp

q = sp.symbols('q', positive=True)
h = q - 1/q

def qbracket(k):
    return (q**k - q**(-k)) / h

def limit_ratio(k1, k2):
    ratio = qbracket(k1) / qbracket(k2)
    # limit q -> 1
    return sp.limit(ratio, q, 1)

print("T_{2,9} / T_{2,3}:", limit_ratio(9, 3))
print("T_{2,5} / T_{2,2}:", limit_ratio(5, 2))
print("T_{2,3} / T_{2,2}:", limit_ratio(3, 2))

