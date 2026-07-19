import mpmath
mpmath.mp.dps = 50

import sys
from pathlib import Path
sys.path.append(str(Path("/Users/litlfred/space_cats/qou/computations").resolve()))

import sympy as sp
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic

q = sp.Symbol('q', positive=True)
h = q - 1/q

def eval_borromean_on_lambda(lam):
    syts, _, contents = __import__("y_lambda_wenzl_bridge")._standard_young_tableaux(lam)
    dim = len(syts)
    if dim == 0: return sp.Integer(0)
    sigmas = []
    for k in range(1, sum(lam)):
        M = sp.zeros(dim, dim)
        processed = set()
        for i in range(dim):
            if i in processed: continue
            ci_k = syts[i][k]
            ci_k1 = syts[i][k + 1]
            rho = contents[ci_k1] - contents[ci_k]
            a = h / (1 - q ** (-2 * rho))
            swap_map = dict(syts[i])
            swap_map[k] = ci_k1
            swap_map[k + 1] = ci_k
            j = next((jj for jj in range(dim) if jj != i and syts[jj] == swap_map), None)
            if j is None:
                M[i, i] = a
                processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b_sq = sp.cancel(a * a_prime + 1)
                bb = sp.sqrt(b_sq)
                M[i, i] = a
                M[j, j] = a_prime
                M[i, j] = bb
                M[j, i] = bb
                processed.add(i)
                processed.add(j)
        sigmas.append(M)
    s1 = sigmas[0]
    s2 = sigmas[1]
    
    # beta_bor = (s1 s2^-1)^3
    s2_inv = s2 - h*sp.eye(dim)
    w = (s1 * s2_inv)**3
    return sp.trace(w)

c3_sym = sp.simplify(y_lambda_wenzl_bridge_symbolic((3,)) * eval_borromean_on_lambda((3,)))
c21_sym = sp.simplify(y_lambda_wenzl_bridge_symbolic((2, 1)) * eval_borromean_on_lambda((2, 1)))
c111_sym = sp.simplify(y_lambda_wenzl_bridge_symbolic((1, 1, 1)) * eval_borromean_on_lambda((1, 1, 1)))

q_val = mpmath.mpf('1.1099785827513808075916690956107688798744991218736')
c3 = float(c3_sym.subs(q, q_val))
c21 = float(c21_sym.subs(q, q_val))
c111 = float(c111_sym.subs(q, q_val))

print("Borromean c3:", c3)
print("Borromean c21:", c21)
print("Borromean c111:", c111)
print("Sum:", c3 + c21 + c111)

target = float(((3*q_val**2 + 4 + 3/q_val**2)/4))
print("Target:", target)

