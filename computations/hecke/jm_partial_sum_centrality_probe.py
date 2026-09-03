"""Jucys's CENTRALITY route -- it sidesteps the product obstruction entirely.

Context. Mathas Prop 3.24 derives JM commutativity (iv) from (iii), which asserts T_i
commutes with the PRODUCT L_i L_{i+1}. From the recursion alone we can only reach the
SWAPPED form (HeckeAdditiveJucysMurphy.addJM_sigma_prod_swap), which is commutation only
if (iv) already holds -- so that route is circular for us.

**Mathas is not wrong.** The swapped identity is CONSISTENT with (iii) given (iv); the
problem is provability ORDER, not correctness. But there is a different classical
argument -- Jucys's -- which Mathas alludes to at 3.25 (symmetric polynomials in the L's
are central) rather than at 3.24, and it avoids the product entirely.

THE ROUTE. Let S_m = A_1 + ... + A_m. Then A_m = S_m - S_{m-1}, and for i < m every
generator occurring in A_i is one that BOTH S_m and S_{m-1} commute with -- so A_m
commutes with A_i. No product statement is used anywhere.

MEASURED HERE (H_5 regular rep, faithful; exact Fractions; q in {2,3}; d in {1/2,1/3,1},
including d=1 which is NOT Mathas's normalisation):

  S_m commutes with sigma_j for EVERY j != m.

  m=1: Y n Y Y     m=2: Y Y n Y     m=3: Y Y Y n     m=4: Y Y Y Y

and the second block shows why the exception is exactly j = m:

  sigma_j commutes with the INDIVIDUAL A_i except for i in {j, j+1}

which is Mathas 3.24(i). At j = m the summation cutoff SPLITS the pair (A_m, A_{m+1}),
and that pair is exactly what addJM_sigma_comm_add handles. Everything else in the sum
commutes term by term.

WHAT THIS DOES AND DOES NOT BUY. It replaces the circular (iii)->(iv) with a
non-circular route, and it is d-independent. But it still needs 3.24(i) IN FULL, and
the i >= j+2 half of that is NOT provable from the recursion by induction: at i = j+2
the recursion introduces sigma_{j+1}, adjacent to sigma_j, and the commutation holds
only by cancellation. Mathas proves that case from the explicit transposition form
("T_{k+1} commutes with T_(j,k) for j = 1..k").

So the conclusion of HeckeAdditiveJucysMurphy stands and is reinforced: the missing
ingredient is the explicit sum-of-transpositions expansion, not a better invariant and
not a different convention. The centrality route is nonetheless the RIGHT one to
formalise once that expansion exists, because it never touches the product.

Emits no witness: this measures which proof route survives.
"""
from fractions import Fraction as F
exec(open(__file__.replace('jm_partial_sum_centrality_probe','jm_adjacent_widen_q_and_n')).read().split('print("jm words')[0])

def elt_ops(n,q):
    word = build(n,q)
    def add(a,b):
        r=dict(a)
        for k,v in b.items():
            r[k]=r.get(k,F(0))+v
            if r[k]==0: del r[k]
        return r
    def smul(c,a): return {k:c*v for k,v in a.items() if c*v!=0}
    def mulE(a,b):
        # multiply two elements: expand b over its support words is hard; instead
        # build products only from generator words, so we multiply via right-mult by gens
        raise NotImplementedError
    return word, add, smul

# ADDITIVE JM by the recursion, as ELEMENTS: A_0 = 0, A_{k+1} = s_k A_k s_k + d s_k
# We can realise these because every term is a generator word.
def addJM_terms(k, d):
    """return list of (coeff_exponent_of_d, generator-word) for A_k"""
    if k == 0: return []
    prev = addJM_terms(k-1, d)
    out = [(c, [k-1]+w+[k-1]) for (c,w) in prev]
    out.append((1, [k-1]))
    return out

def build_elt(word, add, smul, terms, d):
    r = {}
    for (c, w) in terms:
        r = add(r, smul(F(c)*d, word(w)))
    return r

for (n,q,d) in [(5, F(2), F(1,2)), (5, F(3), F(1,3)), (5, F(2), F(1))]:
    word, add, smul = elt_ops(n,q)
    print(f"n={n} q={q} d={d}")
    for m in range(1, n):
        S = {}
        for i in range(1, m+1):
            S = add(S, build_elt(word, add, smul, addJM_terms(i, d), d))
        # does S commute with sigma_j for j <= m-2 ?
        res=[]
        for j in range(0, n-1):
            # S * s_j  vs  s_j * S : need left-mult; emulate by building words
            # left multiply: rebuild each term with j prepended
            Sl = {}
            for i in range(1, m+1):
                for (c,w) in addJM_terms(i,d):
                    Sl = add(Sl, smul(F(c)*d, word([j]+w)))
            Sr = {}
            for i in range(1, m+1):
                for (c,w) in addJM_terms(i,d):
                    Sr = add(Sr, smul(F(c)*d, word(w+[j])))
            res.append((j, Sl==Sr))
        print("   m=%d  commutes with s_j:" % m, {j:("Y" if ok else "n") for j,ok in res})

print()
print("Does sigma_j commute with INDIVIDUAL A_i for i >= j+2 ?  (decides the Lean induction)")
n,q,d = 5, F(2), F(1,2)
word, add, smul = elt_ops(n,q)
def elt(i):
    r={}
    for (c,w) in addJM_terms(i,d): r=add(r, smul(F(c)*d, word(w)))
    return r
def lmul(i,j):
    r={}
    for (c,w) in addJM_terms(i,d): r=add(r, smul(F(c)*d, word([j]+w)))
    return r
def rmul(i,j):
    r={}
    for (c,w) in addJM_terms(i,d): r=add(r, smul(F(c)*d, word(w+[j])))
    return r
for j in range(0,3):
    row={}
    for i in range(1,5):
        row[i] = "Y" if lmul(i,j)==rmul(i,j) else "n"
    print(f"   sigma_{j} vs A_i :", row)
