import numpy as np
from collections import deque
from itertools import product

# ---------------------------------------------------------------------------
# Metathesis / double-displacement: cations C_i, anions A_j; a "state" is a
# contingency table T[i,j] = moles of salt (C_i)(A_j).  TWO conservation laws:
#   row sums = cation budget r_i ,  col sums = anion budget c_j.
# That double conservation = transportation polytope = type-A crystal of
# contingency tables (RSK / Danilov-Koshevoy); the fiber's Markov basis is the
# 2x2 swap, which IS an elementary balanced metathesis reaction.
# ---------------------------------------------------------------------------

cations = ["Na","K","Ag"]
anions  = ["Cl","NO3","Br"]

def fiber(r, c):
    """all nonneg integer matrices with row sums r, col sums c"""
    R, C = len(r), len(c)
    out = []
    def rec(i, remc, T):
        if i == R:
            if all(v == 0 for v in remc): out.append(np.array(T))
            return
        # distribute r[i] across columns without exceeding remaining col budgets
        def dist(j, left, row):
            if j == C:
                if left == 0: rec(i+1, [remc[k]-row[k] for k in range(C)], T+[row])
                return
            for v in range(0, min(left, remc[j])+1):
                dist(j+1, left-v, row+[v])
        dist(0, r[i], [])
    rec(0, list(c), [])
    return out

def swap_moves(T):
    """2x2 ± moves preserving both margins; each is a balanced metathesis."""
    R, C = T.shape
    nbrs = []
    for i in range(R):
        for k in range(i+1, R):
            for j in range(C):
                for l in range(j+1, C):
                    for s in (+1, -1):
                        U = T.copy()
                        U[i,j]+=s; U[k,l]+=s; U[i,l]-=s; U[k,j]-=s
                        if (U >= 0).all(): nbrs.append((U,(i,k,j,l,s)))
    return nbrs

def connected_by_swaps(S):
    """is the whole fiber connected under 2x2 swaps? (Markov-basis property)"""
    keys = {T.tobytes(): n for n,T in enumerate(S)}
    seen = {0}; dq = deque([0])
    while dq:
        n = dq.popleft()
        for U,_ in swap_moves(S[n]):
            m = keys.get(U.tobytes())
            if m is not None and m not in seen:
                seen.add(m); dq.append(m)
    return len(seen) == len(S)

def reaction_of_move(i,k,j,l,s):
    """the elementary 2x2 move written as a chemical metathesis"""
    salt = lambda ci,aj: f"{cations[ci]}{anions[aj]}"
    if s>0:  # +(ij)+(kl) -(il)-(kj):  (C_i A_l)+(C_k A_j) -> (C_i A_j)+(C_k A_l)
        return f"{salt(i,l)} + {salt(k,j)}  ->  {salt(i,j)} + {salt(k,l)}"
    else:
        return f"{salt(i,j)} + {salt(k,l)}  ->  {salt(i,l)} + {salt(k,j)}"

# formula matrix check: cations 3, anions 3 -> 6 "elements" (treat each ion a token)
def formula_vector(T):
    """net (cation_i count, anion_j count) — conserved by every swap"""
    return np.concatenate([T.sum(axis=1), T.sum(axis=0)])

print("=== Example 1: r=c=[1,1,1]  (permutation matrices = S_3) ===")
S = fiber([1,1,1],[1,1,1])
print("fiber size:", len(S), "  (= 3! ; |Weyl(A_2)| = 6)")
print("connected by 2x2 swaps (Markov basis):", connected_by_swaps(S))

print("\n=== Example 2: r=[2,1,1], c=[1,2,1] (genuine non-permutation fiber) ===")
S2 = fiber([2,1,1],[1,2,1])
print("fiber size:", len(S2))
print("connected by 2x2 swaps:", connected_by_swaps(S2))
# verify EVERY swap conserves the ion budgets (is mass-balanced)
ok = all((formula_vector(T)==formula_vector(U)).all() for T in S2 for U,_ in swap_moves(T))
print("every 2x2 swap conserves both ion budgets (balanced):", ok)

print("\n=== An elementary move read as chemistry (the classic precipitation) ===")
T0 = np.array([[1,0,0],[0,1,0],[0,0,1]])   # AgNO3? show a concrete swap
for U,(i,k,j,l,s) in swap_moves(np.array([[0,1,0],[1,0,0],[0,0,1]]))[:1]:
    pass
print(reaction_of_move(2,0,0,1,+1), "   <-- Ag/Na with Cl/NO3 exchange")
print(reaction_of_move(0,1,0,1,-1))

print("\nfiber count vs permanent (transportation count) for [1,1,1]/[1,1,1]:",
      len(S), "= per(J_3)=", 6)
