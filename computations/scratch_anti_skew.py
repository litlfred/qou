import pyhecke_native
from itertools import permutations

def get_reduced_word(p):
    """Get a reduced word (0-indexed generators) for a permutation p (tuple 1..n)."""
    p = list(p)
    n = len(p)
    word = []
    for i in range(n):
        for j in range(n - 1 - i):
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
                word.append(j)
    return word

def get_sn_words(n):
    return [get_reduced_word(p) for p in permutations(range(1, n + 1))]

import sympy as sp
q, z, h = sp.symbols('q z h')

def trace_of_word(word, n_strands):
    try:
        zh_serialised = pyhecke_native.tr_m_word_lq(word, n_strands)
    except RuntimeError:
        return None
    val = 0
    for (z_exp, h_exp), coef_list in zh_serialised:
        c_zh = 0
        for q_half_exp, big_int_str in coef_list:
            c_zh += int(big_int_str) * (q ** (sp.Rational(q_half_exp, 2)))
        val += c_zh * (z ** z_exp) * (h ** h_exp)
    return val

for n in [2, 3, 4]:
    print(f"--- n = {n} ---")
    words = get_sn_words(n)
    
    # A^(n) = (1/c_n) sum_{w} (-q)^{-ell(w)} T_w
    # Let's first compute the sum
    sum_tr = 0
    c_n = 0
    for w in words:
        ell = len(w)
        tr = trace_of_word(w, n)
        if tr is None:
            print(f"Failed on word {w}")
            continue
        weight = (-q)**(-ell)
        sum_tr += weight * tr
        c_n += q**(-2*ell)
        
    print(f"c_{n} = {sp.simplify(c_n)}")
    tr_A = sp.simplify(sum_tr / c_n)
    print(f"tr(A^({n})) = {tr_A}")
    
    # Check what happens if z = 1/(sqrt(q) + 1/sqrt(q))? Wait, let's leave it symbolic.
