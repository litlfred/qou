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

# Branching Delta_mu
# mu=(3): lambda=(4), (3,1)
# dim_q(4) = 1, dim_q(3,1) = q^2+1+q^-2
delta3 = sp.simplify(1 + q**2+1+q**-2)

# mu=(2,1): lambda=(3,1), (2,2), (2,1,1)
# dim_q(3,1) = q^2+1+q^-2
# dim_q(2,2) = q^2+q^-2
# dim_q(2,1,1) = q^2+1+q^-2
sum_21 = sp.simplify( (q**2+1+q**-2) + (q**2+q**-2) + (q**2+1+q**-2) )
dim_21 = sp.simplify(q + 1/q)
delta21 = sp.simplify(sum_21 / dim_21)

# mu=(1,1,1): lambda=(2,1,1), (1,1,1,1)
# dim_q(2,1,1) = q^2+1+q^-2, dim_q(1,1,1,1) = 1
delta111 = sp.simplify( (q**2+1+q**-2) + 1 )

ans = sp.simplify(c3 * delta3 + c21 * delta21 + c111 * delta111)

target = sp.simplify((3*q**2 + 4 + 3*q**-2)/4)

print("ans:", ans)
print("target:", target)
print("diff:", sp.simplify(ans - target))

q_val = float('1.10997858275138080759')
print("num ans:", float(ans.subs(q, q_val)))

