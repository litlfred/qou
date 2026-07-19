import sys
from pathlib import Path
sys.path.append(str(Path("/Users/litlfred/space_cats/qou/computations").resolve()))

import sympy as sp
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic

q = sp.Symbol('q', positive=True)
h = q - 1/q

def eval_word(lam):
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
                M[i, i] = a; processed.add(i)
            else:
                a_prime = h / (1 - q ** (2 * rho))
                b_sq = sp.cancel(a * a_prime + 1)
                bb = sp.sqrt(b_sq)
                M[i, i] = a; M[j, j] = a_prime; M[i, j] = bb; M[j, i] = bb
                processed.add(i); processed.add(j)
        sigmas.append(M)
    s1, s2 = sigmas[0], sigmas[1]
    w1 = s1**4 * (s1 - h/2*sp.eye(dim)) * s1**2
    w2 = (s2 - h*sp.eye(dim))**3 * (s2 - h/2*sp.eye(dim))
    return sp.trace(w1 * w2)

c3 = sp.simplify(y_lambda_wenzl_bridge_symbolic((3,)) * eval_word((3,)))
c21 = sp.simplify(y_lambda_wenzl_bridge_symbolic((2, 1)) * eval_word((2, 1)))
c111 = sp.simplify(y_lambda_wenzl_bridge_symbolic((1, 1, 1)) * eval_word((1, 1, 1)))

q_val = float('1.10997858275138080759')
c3_num = float(c3.subs(q, q_val))
c21_num = float(c21.subs(q, q_val))
c111_num = float(c111.subs(q, q_val))

print(f"c3: {c3_num}, c21: {c21_num}, c111: {c111_num}")
target = (3*q_val**2 + 4 + 3*q_val**-2)/4
print(f"target H4 scalar: {target}")
trace_bare = c3_num + c21_num + c111_num
print(f"trace_bare: {trace_bare}")
print(f"ratio target/bare: {target/trace_bare}")

