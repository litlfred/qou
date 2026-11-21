"""H13: graded six-strand test of the folded descent. Exact arithmetic over QQ (DomainMatrix)."""
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from sympy import QQ
from itertools import product
N = 6; DIM = 2**N

def dm(M): return DomainMatrix.from_Matrix(sp.Matrix(M)).convert_to(QQ)

def build(q):
    h = q - 1/q
    R = sp.Matrix([[q,0,0,0],[0,0,1,0],[0,1,h,0],[0,0,0,q]])
    def gen(M, j):
        return sp.kronecker_product(sp.kronecker_product(sp.eye(2**(j-1)), M), sp.eye(2**(N-j-1)))
    G = {j: dm(gen(R, j)) for j in range(1, N)}
    I = dm(sp.eye(DIM))
    E = {j: (I*q - G[j]) * (1/(q + 1/q)) for j in range(1, N)}
    # mirror iota: reverse strands, flip each basis vector
    io = sp.zeros(DIM, DIM)
    for k in range(DIM):
        bits = [(k >> (N-1-b)) & 1 for b in range(N)]
        nb = [1 - x for x in reversed(bits)]
        io[int("".join(map(str, nb)), 2), k] = 1
    iota = dm(io)
    sig = {i: G[3+i]*G[3-i] for i in (1, 2)}
    b = {i: sig[i] - E[3+i]*E[3-i]*(2/q**2) for i in (1, 2)}
    return I, G, iota, sig, b, G[3]

def T(iota, X):
    L = (iota*X).to_list()
    return sum(L[k][k] for k in range(DIM))

def words(gens, L):
    out = []
    for n in range(L+1):
        out += list(product(gens, repeat=n))
    return out

def prod(I, seq):
    M = I
    for X in seq: M = M*X
    return M

for q in (sp.Rational(3,2), sp.Integer(2)):
    I, G, iota, sig, b, tau = build(q)
    comm = lambda A: (iota*A - A*iota).to_Matrix().is_zero_matrix
    c0 = all(comm(X) for X in [sig[1], sig[2], b[1], b[2], tau])
    gens = [b[1], b[2], tau]
    Fs = [prod(I, w) for w in words(gens, 3)]
    def holds(rel): return all(T(iota, F*rel) == 0 for F in Fs)
    quad = {i: (b[i] - I*q**2)*(b[i] + I*(1/q**2)) for i in (1, 2)}
    c1 = all(holds(quad[i]) for i in (1, 2))
    br = b[1]*b[2]*b[1] - b[2]*b[1]*b[2]
    brB = tau*b[1]*tau*b[1] - b[1]*tau*b[1]*tau
    c2 = holds(br) and holds(brB) and ((tau - I*q)*(tau + I*(1/q))).to_Matrix().is_zero_matrix
    quad_u = {i: (sig[i] - I*q**2)*(sig[i] + I*(1/q**2)) for i in (1, 2)}
    gens_u = [sig[1], sig[2], tau]
    Fu = [prod(I, w) for w in words(gens_u, 3)]
    c3_fail = not all(all(T(iota, F*quad_u[i]) == 0 for F in Fu) for i in (1, 2))
    print(f"q={q}: 0 iota-equivariant: {c0}; 1 folded quadratic under T: {c1}; 2 type-B braid under T: {c2}; 3 ungraded fails quadratic: {c3_fail}")
    if not c1:
        bad = [(i, k) for i in (1, 2) for k, F in enumerate(Fs) if T(iota, F*quad[i]) != 0]
        print("   first failures (letter, word index):", bad[:5], "of", len(bad))
