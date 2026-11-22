"""Sea-strand probe: does a traced 4th strand split n - p beyond a common factor?

Jimbo braiding on (C^3)^{x4}. Valence word V3 = (s1 s2^-1)^3 on strands 1-3,
coupled to strand 4 by its monodromy L4 = s3 s2 s1 s1 s2 s3 (strand 4 encircles
the three valence strands). Strand 4 is projected onto one flavour f (sea quark
of flavour f) or left unprojected (all flavours), then traced out. We compare
the bare trace on the proton (2,1,0) and neutron (1,2,0) valence weight spaces.
Exact in Q(q); no floats.
Structural expectation: every braid word is U_q(sl3)-invariant, and so is an
unprojected partial trace; weight spaces (2,1,0),(1,2,0) are Weyl-conjugate, so
an invariant operator has equal trace on them. A flavour projector is NOT
invariant, so a single-flavour sea strand can split p from n.
"""
import itertools, sympy as sp
q = sp.symbols('q', positive=True)
N = 3
def R():
    M = sp.zeros(N*N, N*N)
    for i in range(N):
        for j in range(N):
            s = i*N + j
            if i == j: M[s, s] = q
            elif i < j: M[j*N+i, s] = 1
            else: M[j*N+i, s] = 1; M[s, s] = q - 1/q
    return sp.SparseMatrix(M)
Rm = R(); Ri = sp.SparseMatrix(Rm.inv().applyfunc(sp.simplify)); I3 = sp.SparseMatrix(sp.eye(3))
def gen(k, inv=False):  # sigma_k on 4 strands, k=1,2,3
    A = Ri if inv else Rm
    mats = [I3]*(k-1) + [A] + [I3]*(3-k)
    out = mats[0]
    for m in mats[1:]: out = sp.SparseMatrix(sp.kronecker_product(out, m))
    return out
s1, s2, s3 = gen(1), gen(2), gen(3); s2i = gen(2, True)
V3 = (s1*s2i)**3
L4 = s3*s2*s1*s1*s2*s3
def idx(t): return ((t[0]*3+t[1])*3+t[2])*3+t[3]
def tr_on(Mx, w, sea):
    """sum over valence basis b of weight w and sea flavours in `sea` of <b,f| Mx |b,f>"""
    tot = 0
    for t in itertools.product(range(3), repeat=3):
        if tuple(t.count(k) for k in range(3)) != w: continue
        for f in sea:
            i = idx(t + (f,)); tot += Mx[i, i]
    return sp.factor(sp.simplify(tot))
words = {'V3 (sea uncoupled)': V3, 'V3*L4': V3*L4, 'V3*L4^-1-free: L4*V3*L4': L4*V3*L4}
names = {0: 'u-sea', 1: 'd-sea', 2: 's-sea'}
for wn, Mx in words.items():
    print(f"== {wn}")
    for sea, lab in [((0,), 'u-sea'), ((1,), 'd-sea'), ((2,), 's-sea'), ((0, 1, 2), 'all flavours')]:
        tp, tn = tr_on(Mx, (2,1,0), sea), tr_on(Mx, (1,2,0), sea)
        print(f"   {lab:13s} tr_p - tr_n = {sp.factor(sp.simplify(tp - tn))}")
