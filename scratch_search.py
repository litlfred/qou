import sys
from pathlib import Path
sys.path.append(str(Path("/Users/litlfred/space_cats/qou/computations").resolve()))

import sympy as sp
from hoefsmit_symbolic import chi_lambda_symbolic
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_symbolic, classical_dim

q = sp.Symbol('q', positive=True)

# Load c3, c21, c111 from previous output (pasted here to save time)
c3 = (q**(31/2) + q**(29/2) + q**(27/2) + q**(25/2) - 4*q**(23/2) - 4*q**(21/2) - 2*q**(19/2) - 2*q**(17/2) + 5*q**(15/2) + 5*q**(13/2) + q**(11/2) + q**(9/2) - 2*q**(7/2) - 2*q**(5/2) + q**16 + q**13 - q**12 - 2*q**10 - 3*q**9 - q**8 + 4*q**6 + 3*q**5 + q**4 - 2*q**2 - q)/(4*(q**14 + 2*q**13 - 2*q**11 - 2*q**10 - 2*q**9 - q**8 + q**6 + 2*q**5 + 2*q**4 + 2*q**3 - 2*q - 1))
# wait c21 from previous output is very long and has sqrt(q). Let's re-eval it in sympy.
h = q - 1/q
def eval_word_on_lambda(lam):
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
    s1_avg = s1 - (h/2)*sp.eye(dim)
    s2_inv = s2 - h*sp.eye(dim)
    s2_avg = s2 - (h/2)*sp.eye(dim)
    w1 = s1**4 * s1_avg * s1**2
    w2 = s2_inv**3 * s2_avg
    return sp.trace(w1 * w2)

c3 = sp.simplify(y_lambda_wenzl_bridge_symbolic((3,)) * eval_word_on_lambda((3,)))
c21 = sp.simplify(y_lambda_wenzl_bridge_symbolic((2, 1)) * eval_word_on_lambda((2, 1)))
c111 = sp.simplify(y_lambda_wenzl_bridge_symbolic((1, 1, 1)) * eval_word_on_lambda((1, 1, 1)))

target = (3*q**2 + 4 + 3*q**-2)/4

# Candidates for Delta
dimq = [1, q+q**-1, 1]
fq = [1, q+q**-1, 1]
dq = [1, q+q**-1, 1]
W_inv = [(q**2+1+q**-2), (q**2+1+q**-2)/(q+q**-1)**2, (q**2+1+q**-2)]

sign = [1, -1, -1]
c_list = [c3, c21, c111]

# Try combinations
for p in range(-3, 4):
    for sig in [True, False]:
        delta = [ (sign[i] if sig else 1) * (dimq[i]**p) for i in range(3)]
        val = sp.simplify(sum(c_list[i]*delta[i] for i in range(3)))
        if sp.simplify(val - target) == 0:
            print(f"FOUND EXACT MATCH! p={p}, sig={sig}")

# check if proportional to target
for p in range(-3, 4):
    delta = [ (sign[i]) * (dimq[i]**p) for i in range(3)]
    val = sp.simplify(sum(c_list[i]*delta[i] for i in range(3)))
    ratio = sp.simplify(val / target)
    print(f"Ratio for p={p}, sig=True: {ratio}")

