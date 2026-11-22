"""Capture as a conditional expectation; flavour ratio on 5 and 6 strands.

Pre-registered in np_capture_conditional_expectation_preregistration.md (P1-P5).
Exact arithmetic only: Fraction at rational q for the exhaustive word sweeps, sympy over Q(q)
for the closed forms. No float enters any computed quantity.
"""
from fractions import Fraction as Fr
from itertools import product
import sympy as sp

# ---------- exact sparse engine at rational q (P1, P2) ----------
def rmat(q):
    h = q - 1 / q
    # Ř on basis 00,01,10,11 (column images)
    return {0: {0: q}, 1: {2: Fr(1)}, 2: {1: Fr(1), 2: h}, 3: {3: q}}

def rmat_inv(q):
    h = q - 1 / q
    R = rmat(q)
    out = {}
    for c, col in R.items():
        d = dict(col)
        d[c] = d.get(c, Fr(0)) - h
        out[c] = {k: v for k, v in d.items() if v != 0}
    return out

def apply_letter(vec, i, M, n):
    # strand 0 is the most significant bit
    out = {}
    sh = n - i - 2
    for s, a in vec.items():
        pair = (s >> sh) & 3
        base = s & ~(3 << sh)
        for t, m in M[pair].items():
            k = base | (t << sh)
            out[k] = out.get(k, Fr(0)) + a * m
    return {k: v for k, v in out.items() if v != 0}

def sector_traces(word, n, q, nuc):
    """Return (Tr(K Π_p W), Tr(K Π_n W)) with the nucleon on strands nuc (3 consecutive)."""
    R, Ri = rmat(q), rmat_inv(q)
    tp = tn = Fr(0)
    for s in range(2 ** n):
        bits = [(s >> (n - 1 - j)) & 1 for j in range(n)]
        z_nuc = sum(1 for j in nuc if bits[j] == 0)
        if z_nuc not in (1, 2):
            continue
        vec = {s: Fr(1)}
        # product in list order: W = L1 L2 ... ; apply rightmost first to the vector
        for (i, inv) in reversed(word):
            vec = apply_letter(vec, i, Ri if inv else R, n)
        diag = vec.get(s, Fr(0))
        if diag == 0:
            continue
        z = bits.count(0)
        w = q ** (2 * z - n)
        if z_nuc == 2:
            tp += w * diag
        else:
            tn += w * diag
    return tp, tn

def sweep(n, maxlen, q, nuc):
    letters = [(i, b) for i in range(n - 1) for b in (False, True)]
    tested = fails = 0
    first_fail = None
    for L in range(0, maxlen + 1):
        for word in product(letters, repeat=L):
            tp, tn = sector_traces(list(word), n, q, nuc)
            tested += 1
            if tn != tp / q ** 2:
                fails += 1
                if first_fail is None:
                    first_fail = word
    return tested, fails, first_fail

# ---------- symbolic engine (P3, P4) ----------
q = sp.symbols('q', positive=True)
h = q - 1 / q
d2 = q + 1 / q
Rs = sp.Matrix([[q, 0, 0, 0], [0, 0, 1, 0], [0, 1, h, 0], [0, 0, 0, q]])
Rsi = Rs - h * sp.eye(4)
K = sp.diag(q, 1 / q)

def gen(i, n, inv):
    return sp.kronecker_product(sp.kronecker_product(sp.eye(2 ** i), Rsi if inv else Rs), sp.eye(2 ** (n - i - 2)))

def word(L, n):
    W = sp.eye(2 ** n)
    for (i, inv) in L:
        W = W * gen(i, n, inv)
    return W

def kron_list(ms):
    out = ms[0]
    for m in ms[1:]:
        out = sp.kronecker_product(out, m)
    return out

def E_last(X, n):
    """K-weighted partial trace over the last strand, divided by [2]. X acts on n strands."""
    Y = X * kron_list([sp.eye(2 ** (n - 1)), K])
    out = sp.zeros(2 ** (n - 1))
    for a in range(2 ** (n - 1)):
        for b in range(2 ** (n - 1)):
            out[a, b] = sum(Y[2 * a + c, 2 * b + c] for c in range(2))
    return (out / d2).applyfunc(sp.simplify)

def proj3(nz):
    P = sp.zeros(8)
    for s in range(8):
        if [(s >> (2 - j)) & 1 for j in range(3)].count(0) == nz:
            P[s, s] = 1
    return P

K3 = kron_list([K, K, K])

def eps3(X):
    return sp.simplify(((K3 * proj3(2) * X).trace() - (K3 * proj3(1) * X).trace()) / d2 ** 3)

def main():
    q0s = [Fr(111, 100), Fr(7, 5)]
    print("== P1: nucleon on strands 0-2, extra strands on the right ==")
    for n, ml in ((5, 4), (6, 3)):
        for qq in q0s:
            t, f, ff = sweep(n, ml, qq, (0, 1, 2))
            print(f"n={n} len<={ml} q={qq}: words={t} ratio failures={f}")
    print("== P2: nucleon not at the left end (n=5, len<=3) ==")
    for nuc in ((1, 2, 3), (2, 3, 4)):
        t, f, ff = sweep(5, 3, Fr(111, 100), nuc)
        print(f"nucleon {nuc}: words={t} failures={f} first={ff}")

    V3 = word([(0, False), (1, True)] * 3, 3)
    eV = sp.factor(eps3(V3))
    print("== P3: adjacent capture sigma_2^-2 ==")
    Eadj = E_last(word([(2, True), (2, True)], 4), 4)
    cadj = sp.simplify(Eadj[0, 0])
    print("E(sigma_2^-2) scalar:", sp.simplify(Eadj - cadj * sp.eye(8)) == sp.zeros(8))
    print("c_adj =", sp.factor(cadj), " predicted 1+h^2-h q^2/[2] diff:",
          sp.simplify(cadj - (1 + h ** 2 - h * q ** 2 / d2)))
    W_adj = word([(0, False), (1, True)] * 3 + [(2, True), (2, True)], 4)
    eps_adj4 = sp.simplify((kron_list([K3, K]) * sp.kronecker_product(proj3(2) - proj3(1), sp.eye(2)) * W_adj).trace() / d2 ** 4)
    print("eps(W_adj,L) - c_adj*eps(V3) =", sp.simplify(eps_adj4 - cadj * eV))

    print("== P4: cabled capture (Jucys-Murphy inverse) ==")
    C = word([(2, True), (1, True), (0, True), (0, True), (1, True), (2, True)], 4)
    EC = E_last(C, 4)
    gens3 = [gen(i, 3, False) for i in range(2)]
    print("E(C) central:", all(sp.simplify(EC * g - g * EC) == sp.zeros(8) for g in gens3))
    # isotypic blocks of (C^2)^{x3}: (3) = q-symmetrizer image; (2,1) = complement
    # use the central idempotent of (3): projection onto the span of the 4-dim highest-weight module.
    # eigenvalues of E(C) and their multiplicities
    ev = {sp.factor(sp.simplify(k)): m for k, m in EC.eigenvals().items()}
    for k in ev:
        print(f"  eigenvalue {k}")  # block dimensions are printed below as projector traces
    # spectral decomposition of eps(V3 * E(C))
    eps_L = sp.factor(eps3(V3 * EC))
    print("eps(W_L) via E:", eps_L)
    W_L = word([(0, False), (1, True)] * 3 + [(2, True), (1, True), (0, True), (0, True), (1, True), (2, True)], 4)
    eps_L4 = sp.simplify((kron_list([K3, K]) * sp.kronecker_product(proj3(2) - proj3(1), sp.eye(2)) * W_L).trace() / d2 ** 4)
    print("eps(W_L) direct - via E:", sp.simplify(eps_L4 - eps_L))
    vals = sorted(ev.keys(), key=lambda e: sp.N(e.subs(q, sp.Rational(111, 100))))
    if len(vals) == 2:
        a, b = vals
        Pa = sp.simplify((EC - b * sp.eye(8)) / (a - b))
        Pb = sp.simplify((EC - a * sp.eye(8)) / (b - a))
        ea, eb = sp.factor(eps3(V3 * Pa)), sp.factor(eps3(V3 * Pb))
        print("  block with c =", a, ": eps_block(V3) =", ea, " dim", sp.simplify(Pa.trace()))
        print("  block with c =", b, ": eps_block(V3) =", eb, " dim", sp.simplify(Pb.trace()))
        print("  check a*ea + b*eb - eps(W_L):", sp.simplify(a * ea + b * eb - eps_L))
    qv = sp.Rational(1109978582751380, 10 ** 15)  # proton-pinned q0 to 16 digits, display only
    print("== P5: factors at q0 (display; 30 digits) ==")
    print("eps(V3)       =", sp.N(eV.subs(q, qv), 30))
    print("c_adj         =", sp.N(cadj.subs(q, qv), 30))
    print("eps(W_L)/eps(V3) =", sp.N((eps_L / eV).subs(q, qv), 30))

if __name__ == "__main__":
    main()
