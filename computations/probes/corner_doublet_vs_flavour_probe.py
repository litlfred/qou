#!/usr/bin/env python3
"""Is the n = 4 corner doublet the same thing as flavour (sigma_3 -> sigma_3^{-1})?

Bean qou-wkcj, owner priority 3 (2026-11-15 summary): "test whether the n = 4 corner
multiplicity space is the same thing as flavour (sigma_3 -> sigma_3^{-1}). It decides
whether building the H_4 doublet is worth it."

Setting (audit 2026-11-15-weak-chirality-doublet-singlet.md section 6.4). In H_4(q) the
q-line of sigma_1 meets the block lambda = (3,1) in a 2-dimensional multiplicity space D,
spanned by the two standard tableaux with 1, 2 in the first row. The left corner
P_+ H_4 P_+ acts on D through M_2(K), so it contains an sl_2 (a Furey-type doublet on the
left line). The question is whether the two states of D are "u" and "d", where flavour
means letter orientation (#7836): u ~ sigma_3, d ~ sigma_3^{-1}. sigma_3 commutes with
sigma_1, so it acts inside the corner.

What is computed, all exact (sympy, symbolic q; no floats, no fit, no witness):

1. Young's seminormal form of H_4 on (3,1). The braid relations and the quadratic
   relation sigma^2 = h sigma + 1 (h = q - q^{-1}) are CHECKED, not assumed.
2. D = the q-eigenspace of sigma_1 in (3,1); its dimension (expect 2).
3. sigma_3 restricted to D: its eigenvalues (expect q and -q^{-1}, one each).
4. sigma_3^{-1} restricted to D equals sigma_3|_D - h I (the corpus definition
   flip q s = s - h 1, HelicityCommonSource.lean). So the flavour flip is a shift by a
   central scalar on D.
5. Consequences on D, all exact:
   a. sigma_3|_D and sigma_3^{-1}|_D are simultaneously diagonal; each eigenline of
      sigma_3 in D is FIXED by the flip, so the flip never exchanges the two states.
   b. span{sigma_3|_D, sigma_3^{-1}|_D} = span{I, sigma_3|_D} is commutative (dim 2):
      it is the Cartan (diagonal) part of gl_2, and contains no raising/lowering element.
   c. The full corner action on D is M_2(K) (dim 4): the off-diagonal part comes from
      P_+ sigma_2 P_+, i.e. from the letter that does NOT commute with sigma_1.
   d. The two doublet states are the two eigenlines of sigma_3: one left (q) and one right
      (-q^{-1}) for sigma_3. So the doublet label is sigma_3's chirality bit, not its
      orientation.
6. Same test for every sl_2-carrying block of the left corner, n = 4..6, and every letter
   sigma_j (j >= 3) commuting with sigma_1: does the flip ever act on the multiplicity
   space other than as a central shift? (It cannot, by item 4; the loop confirms.)
"""
import sys
from itertools import product

import sympy as sp

q = sp.symbols("q", positive=True)
h = q - 1 / q


def partitions(n, m=None):
    m = n if m is None else m
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def syt(shape):
    n = sum(shape)
    out = []

    def rec(rows, k):
        if k > n:
            out.append(tuple(tuple(r) for r in rows))
            return
        for i, r in enumerate(rows):
            if len(r) < shape[i] and (i == 0 or len(rows[i - 1]) > len(r)):
                r.append(k)
                rec(rows, k + 1)
                r.pop()

    rec([[] for _ in shape], 1)
    return out


def pos(t, k):
    for i, r in enumerate(t):
        if k in r:
            return i, r.index(k)
    raise ValueError


def content(t, k):
    r, c = pos(t, k)
    return c - r


def swap(t, i):
    """Swap entries i, i+1; return None if not standard."""
    m = {i: i + 1, i + 1: i}
    s = tuple(tuple(m.get(x, x) for x in r) for r in t)
    for r in s:
        if list(r) != sorted(r):
            return None
    for c in range(len(s[0])):
        col = [r[c] for r in s if len(r) > c]
        if col != sorted(col):
            return None
    return s


def seminormal(shape, n):
    """sigma_i, i = 1..n-1, on the SYT basis. Diagonal entry x(d) = h q^d / (q^d - q^-d),
    d = axial distance c(i+1) - c(i); off-diagonal (T, s_i T) = 1 and (s_i T, T) =
    x(d) x(-d) + 1, ordered so the pair matrix has determinant -1."""
    T = syt(shape)
    idx = {t: a for a, t in enumerate(T)}
    N = len(T)
    gens = []
    for i in range(1, n):
        M = sp.zeros(N, N)
        for t in T:
            a = idx[t]
            d = content(t, i + 1) - content(t, i)
            x = sp.simplify(h * q**d / (q**d - q**(-d)))
            M[a, a] = x
            s = swap(t, i)
            if s is not None:
                b = idx[s]
                if a < b:
                    M[a, b] = 1
                else:
                    y = sp.simplify(h * q**(-d) / (q**(-d) - q**d))
                    M[a, b] = sp.simplify(x * y + 1)
        gens.append(M)
    return T, gens


def zero(M):
    return all(sp.simplify(e) == 0 for e in M)


ok = True


def check(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


def eigenspace(M, val):
    return (M - val * sp.eye(M.shape[0])).nullspace(simplify=True)


def restrict(M, B):
    """Matrix of M on the invariant subspace with basis columns B."""
    Bm = sp.Matrix.hstack(*B)
    X = (Bm.T * Bm).inv() * Bm.T * M * Bm
    X = X.applyfunc(sp.simplify)
    check("  subspace is invariant", zero((M * Bm - Bm * X).applyfunc(sp.simplify)))
    return X


# ---- 1. relations --------------------------------------------------------------
print("== 1. seminormal form of H_4 on (3,1): relations ==")
T, g = seminormal((3, 1), 4)
I3 = sp.eye(len(T))
for k, M in enumerate(g, 1):
    check(f"sigma_{k}^2 = h sigma_{k} + 1", zero((M * M - h * M - I3).applyfunc(sp.simplify)))
check("s1 s2 s1 = s2 s1 s2", zero((g[0] * g[1] * g[0] - g[1] * g[0] * g[1]).applyfunc(sp.simplify)))
check("s2 s3 s2 = s3 s2 s3", zero((g[1] * g[2] * g[1] - g[2] * g[1] * g[2]).applyfunc(sp.simplify)))
check("s1 s3 = s3 s1", zero((g[0] * g[2] - g[2] * g[0]).applyfunc(sp.simplify)))

# ---- 2. the doublet D ------------------------------------------------------------
print("\n== 2. D = q-line of sigma_1 in (3,1) ==")
D = eigenspace(g[0], q)
print("  SYT basis:", T)
print("  dim D =", len(D))
check("dim D = 2 (the (3,1) multiplicity on the left line)", len(D) == 2)

# ---- 3. sigma_3 on D ------------------------------------------------------------
print("\n== 3. sigma_3 restricted to D ==")
S3 = restrict(g[2], D)
ev = S3.eigenvals()
ev = {sp.simplify(k): v for k, v in ev.items()}
print("  sigma_3|_D eigenvalues:", ev)
check("sigma_3|_D has eigenvalues q and -1/q, once each",
      set(ev) == {sp.simplify(q), sp.simplify(-1 / q)} and all(v == 1 for v in ev.values()))

# ---- 4. the flip ------------------------------------------------------------------
print("\n== 4. sigma_3^{-1} on D ==")
S3inv = restrict(g[2].inv().applyfunc(sp.simplify), D)
check("sigma_3^{-1}|_D = sigma_3|_D - h I  (flip q s = s - h 1)",
      zero((S3inv - (S3 - h * sp.eye(2))).applyfunc(sp.simplify)))

# ---- 5. consequences -------------------------------------------------------------
print("\n== 5. consequences on D ==")
P, Dg = S3.diagonalize()
P = P.applyfunc(sp.simplify)
D3inv = (P.inv() * S3inv * P).applyfunc(sp.simplify)
check("5a. sigma_3^{-1}|_D is diagonal in sigma_3's eigenbasis (flip fixes both states)",
      sp.simplify(D3inv[0, 1]) == 0 and sp.simplify(D3inv[1, 0]) == 0)
print("     sigma_3 eigenbasis diag:", list(Dg.diagonal()),
      " flip diag:", [sp.simplify(D3inv[i, i]) for i in range(2)])
flav = sp.Matrix([list(sp.eye(2)), list(S3), list(S3inv)]).T  # vectorised 2x2s as columns? use rank of flattened
flat = sp.Matrix([[*sp.eye(2)], [*S3], [*S3inv]])
check("5b. span{I, sigma_3|_D, sigma_3^{-1}|_D} has dim 2 (commutative Cartan + identity)",
      flat.rank(simplify=True) == 2)
check("     sigma_3|_D and sigma_3^{-1}|_D commute", zero((S3 * S3inv - S3inv * S3).applyfunc(sp.simplify)))
S2 = None
# P_+ sigma_2 P_+ on D: compress sigma_2 by the sigma_1 q-projector Pp = (sigma_1 + q^{-1}) / [2]
Pp = ((g[0] + (1 / q) * I3) / (q + 1 / q)).applyfunc(sp.simplify)
C2 = restrict((Pp * g[1] * Pp).applyfunc(sp.simplify), D)
C2e = (P.inv() * C2 * P).applyfunc(sp.simplify)
print("     P+ sigma_2 P+ on D, in sigma_3 eigenbasis:", C2e.tolist())
offd = sp.simplify(C2e[0, 1]) != 0 and sp.simplify(C2e[1, 0]) != 0
check("5c. P+ sigma_2 P+ is off-diagonal in sigma_3's eigenbasis (raising/lowering present)", offd)
flat4 = sp.Matrix([[*sp.eye(2)], [*S3], [*C2], [*(S3 * C2).applyfunc(sp.simplify)]])
check("5c. I, sigma_3, P+sigma_2P+, product span M_2(K) on D (dim 4)", flat4.rank(simplify=True) == 4)
check("5d. doublet states = sigma_3 eigenlines: one q (left), one -1/q (right)",
      set(sp.simplify(x) for x in Dg.diagonal()) == {sp.simplify(q), sp.simplify(-1 / q)})

# ---- 6. sweep n = 4..6 ------------------------------------------------------------
print("\n== 6. every sl2-carrying left-corner block, n = 4..6, every sigma_j (j >= 3) ==")
count = 0
for n in range(4, 7):
    for lam in partitions(n):
        if len(syt(lam)) < 2:
            continue
        T_, g_ = seminormal(lam, n)
        Dn = eigenspace(g_[0], q)
        if len(Dn) < 2:
            continue
        for j in range(3, n):
            Sj = restrict(g_[j - 1], Dn)
            Sji = restrict(g_[j - 1].inv().applyfunc(sp.simplify), Dn)
            shift = zero((Sji - (Sj - h * sp.eye(len(Dn)))).applyfunc(sp.simplify))
            evs = {sp.simplify(k) for k in Sj.eigenvals()}
            count += 1
            print(f"  n={n} lambda={lam} dimD={len(Dn)} sigma_{j}: flip = shift by -h: {shift};"
                  f" eigenvalues on D: {sorted(map(str, evs))}")
            check(f"  n={n} {lam} sigma_{j}: flip is a central shift on D", shift)
print(f"  cases checked: {count}")

print("\nVERDICT:", "all checks pass" if ok else "SOME CHECK FAILED")
print("""
Reading. The flavour flip sigma_3 -> sigma_3^{-1} acts on the corner doublet as
sigma_3|_D - h I: a shift by a central scalar. It fixes both doublet states (the two
eigenlines of sigma_3) and so never exchanges them, and the pair {u, d} restricted to D
spans only the commutative Cartan {I, sigma_3|_D}. The doublet's two states are labelled
by sigma_3's EIGENLINE (its chirality bit: q vs -q^{-1}), not by its orientation. The
raising/lowering part of the corner sl_2 comes from P_+ sigma_2 P_+, the non-commuting
letter. So the (3,1) multiplicity doublet is NOT flavour-as-orientation.
The invariant is the quadratic relation (flip q s = s - h 1, HelicityCommonSource.lean),
which holds in every corner of every H_n: scope (b) for this identification, conditional
on the #7836 reading 'flavour = letter orientation'.""")
sys.exit(0 if ok else 1)
