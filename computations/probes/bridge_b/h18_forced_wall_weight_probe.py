"""H18: twisted-trace test that forces the wall weight. See h18_preregistration.md."""
from fractions import Fraction as Fr
import itertools

v = Fr(2)
def kron(A, B):
    n, m = len(A), len(B)
    return [[A[i//m][j//m]*B[i%m][j%m] for j in range(n*m)] for i in range(n*m)]
def eye(d): return [[Fr(int(i == j)) for j in range(d)] for i in range(d)]
def mul(A, B):
    Bt = list(zip(*B))
    return [[sum((a*b for a, b in zip(r, c) if a and b), Fr(0)) for c in Bt] for r in A]
def tr(A): return sum((A[i][i] for i in range(len(A))), Fr(0))
h = v - 1/v
R = [[v,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,v]]
R = [[Fr(x) for x in r] for r in R]

def run(n):
    d = 2**n
    def Rop(i):   # strands i, i+1 (1-based)
        M = eye(2**(i-1)); M = kron(M, R); return kron(M, eye(2**(n-i-1)))
    rho = {i: Rop(i) for i in range(1, n)}
    # J = F . P : reverse tensor factors, then flip each spin
    J = [[Fr(0)]*d for _ in range(d)]
    for idx in range(d):
        bits = [(idx >> (n-1-k)) & 1 for k in range(n)]
        nb = [1-b for b in reversed(bits)]
        j = sum(b << (n-1-k) for k, b in enumerate(nb))
        J[j][idx] = Fr(1)
    JJ = mul(J, J)
    ok_inv = JJ == eye(d)
    ok_int = all(mul(mul(J, rho[i]), J) == rho[n-i] for i in range(1, n))
    print(f"n = {n}: J^2 = 1 {ok_inv}; J rho(T_i) J = rho(T_(n-i)) for all i {ok_int}")
    if not (ok_inv and ok_int): return
    print(f"  3. p_0 = tr J = {tr(J)}")
    orbits = sorted({tuple(sorted({i, n-i})) for i in range(1, n)})
    for I in orbits:
        if len(I) == 1: word, L = [I[0]], 1
        elif I[1] - I[0] == 1: word, L = [I[0], I[1], I[0]], 3
        else: word, L = [I[0], I[1]], 2
        A = eye(d)
        for i in word: A = mul(A, rho[i])
        assert mul(A, J) == mul(J, A)
        p = []; P = J
        for k in range(11):
            p.append(tr(P)); P = mul(P, A)
        res = {}
        for Lc in (1, 2, 3, 4):
            for sgn in (-1, 1):
                a, b = v**Lc, sgn*v**(-Lc)
                res[(Lc, sgn)] = all(p[k+2] == (a+b)*p[k+1] - a*b*p[k] for k in range(9))
        passing = [k for k, ok in res.items() if ok]
        verdict = all(Lc == L for Lc, _ in passing) and len(passing) >= 1
        print(f"  orbit {I}, word {word}, ambient length L = {L}: passing (L', sign of v^-L') = {passing}; 1. weight forced to L: {verdict}")
        print(f"     p_0..p_3 = {[str(x) for x in p[:4]]}")

for n in (4, 5, 6, 7):
    run(n)
