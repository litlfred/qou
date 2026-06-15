#!/usr/bin/env python3
import sympy as sp

q = sp.Symbol('q')

def jackson(k):
    if k == 0: return sp.Integer(0)
    return sp.simplify((1 - q**k) / (1 - q))

def mu_lambda(part):
    hbar2 = ((q - 1) / q)**2
    s = 0
    # contents
    contents = [j - i for i, row in enumerate(part) for j in range(row)]
    for c in contents:
        s += jackson(c) * jackson(c + 1)
    return sp.simplify(hbar2 * s)

def hook_dim(part):
    n = sum(part)
    conj = [sum(1 for r in part if r > j) for j in range(part[0])] if part else []
    import math
    hooks = 1
    for i, row in enumerate(part):
        for j in range(row):
            hooks *= (part[i] - j) + (conj[j] - i) - 1
    return math.factorial(n) // hooks

def main():
    part2 = (2,)
    part21 = (2, 1)
    
    k2 = sp.simplify((q - 1) * mu_lambda(part2))
    k21 = sp.simplify((q - 1) * mu_lambda(part21))
    
    print(f"k2 = {k2}")
    print(f"k21 = {k21}")
    
    # We want to change basis to epsilon = (q - 1)
    # The ladder variable is u = b * hbar_q^2
    # where b^2 = (q^4 + q^2 + 1) / (q^2 + 1)^2
    
    b2 = (q**4 + q**2 + 1) / (q**2 + 1)**2
    b = sp.sqrt(b2)
    hbar2 = ((q - 1)/q)**2
    u_ladder = b * hbar2
    
    # We want to map this to c_k * u^k. So we want to solve for a_1 / c_3.
    # Actually let's just do a Taylor series of k2 around q=1.
    eps = sp.Symbol('eps')
    k2_eps = sp.series(k2.subs(q, 1+eps), eps, 0, 5)
    print(f"k2 in eps: {k2_eps}")
    
    u_eps = sp.series(u_ladder.subs(q, 1+eps), eps, 0, 5)
    print(f"u_ladder in eps: {u_eps}")
    
if __name__ == "__main__":
    main()
