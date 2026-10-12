#!/usr/bin/env python3
"""Exact probe: weight-space traces of the torus braid gamma^p on V^{(x)r}, gcd(r, p) = d >= 1.

Bean qou-gd90 (parent qou-q425). Companion of QOU/Archimedean/RossoJonesTorusLink.lean.

Arithmetic: Laurent polynomials in q with Python int coefficients (exact; no floats anywhere).

Objects (same conventions as the Lean files QOU/IwahoriHecke/TensorMarkovModel.lean and
QOU/Archimedean/RossoJonesMiddle.lean):
  * sigma_i = embedded R-check on sites (i, i+1), rCheck(a,b) = q if a=b const, q - q^-1 on
    the diagonal (0,1)->(0,1), 1 on the swap, 0 otherwise; gamma = sigma_0 ... sigma_{r-2}.
  * T_m(X) = sum of diagonal entries of X over basis states with m ones.
  * rho, rho' = the weighted rotations of RossoJonesMiddle (M e_b = f(b) e_{rot b}), with
      f_rho (b)  = q^{#zeros(init b)}           if last b = 0, q^{#ones(init b)} q^-2  else
      f_rho'(b)  = q^{#zeros(init b)} q^-2      if last b = 0, q^{#ones(init b)}       else.

Checked, for every 2 <= r <= 6 and 1 <= p <= 2r + 2:
  (1) telescoping  T_{m+1}(g^p) = T_{m+1}(rho^p) + T_m(g^p) - T_m(rho'^p)   (no coprimality);
  (2) periodic-state closed form: with d = gcd(r, p), e = r/d, a = p/d,
        T_j(rho^p)  = C(d,k) q^{a[(r-j-1)(d-k) + (j-3)k]}   if j = k e,  else 0,
        T_j(rho'^p) = C(d,k) q^{a[(r-j-3)(d-k) + (j-1)k]}   if j = k e,  else 0;
  (3) the resulting trace formula for tr(W gamma^p) = sum_m q^{2m} T_m(gamma^p), W = diag(q^{2 ones}).
Exit status 0 iff every check passes.
"""
from math import comb, gcd
import itertools, sys

# --- exact Laurent polynomials: dict exponent -> int --------------------------------------
def lp(d):
    return {k: v for k, v in d.items() if v != 0}
def ladd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + v
    return lp(r)
def lneg(a):
    return {k: -v for k, v in a.items()}
def lmul(a, b):
    r = {}
    for k1, v1 in a.items():
        for k2, v2 in b.items():
            r[k1 + k2] = r.get(k1 + k2, 0) + v1 * v2
    return lp(r)
def mono(e, c=1):
    return {e: c} if c else {}
ZERO = {}

def states(r):
    return list(itertools.product((0, 1), repeat=r))

def sigma(r, i):
    """sparse matrix as dict col -> list of (row, coeff); acts on column states b."""
    M = {}
    for b in states(r):
        x, y = b[i], b[i + 1]
        out = []
        if x == y:
            out.append((b, mono(1)))
        else:
            sw = list(b); sw[i], sw[i + 1] = y, x
            out.append((tuple(sw), mono(0)))
            if x < y:  # (0,1) diagonal entry q - q^-1
                out.append((b, {1: 1, -1: -1}))
        M[b] = out
    return M

def matmul(A, B, r):
    """(A*B) e_b = A (B e_b)."""
    C = {}
    for b in states(r):
        acc = {}
        for (v, cv) in B[b]:
            for (a, ca) in A[v]:
                acc[a] = ladd(acc.get(a, ZERO), lmul(ca, cv))
        C[b] = [(a, c) for a, c in acc.items() if c]
    return C

def identity(r):
    return {b: [(b, mono(0))] for b in states(r)}

def mpow(A, p, r):
    R = identity(r)
    for _ in range(p):
        R = matmul(A, R, r)
    return R

def T(A, m, r):
    acc = ZERO
    for b in states(r):
        if sum(b) == m:
            for (a, c) in A[b]:
                if a == b:
                    acc = ladd(acc, c)
    return acc

def rot(b):
    return (b[-1],) + b[:-1]

def rotmat(f, r):
    return {b: [(rot(b), f(b))] for b in states(r)}

def f_rho(b):
    c, x = b[:-1], b[-1]
    return mono(c.count(0)) if x == 0 else mono(c.count(1) - 2)

def f_rho2(b):
    c, x = b[:-1], b[-1]
    return mono(c.count(0) - 2) if x == 0 else mono(c.count(1))

def closed_rho(r, p, j, prime):
    d = gcd(r, p); e = r // d; a = p // d
    if j % e:
        return ZERO
    k = j // e
    if not prime:
        ex = a * ((r - j - 1) * (d - k) + (j - 3) * k)
    else:
        ex = a * ((r - j - 3) * (d - k) + (j - 1) * k)
    return mono(ex, comb(d, k))

def main():
    fails = 0; checks = 0
    for r in range(2, 7):
        g = identity(r)
        for i in range(r - 1):
            g = matmul(g, sigma(r, i), r)
        rho, rho2 = rotmat(f_rho, r), rotmat(f_rho2, r)
        gp, rp, r2p = identity(r), identity(r), identity(r)
        for p in range(1, 2 * r + 3):
            gp, rp, r2p = matmul(g, gp, r), matmul(rho, rp, r), matmul(rho2, r2p, r)
            Tg = [T(gp, m, r) for m in range(r + 1)]
            Tr = [T(rp, m, r) for m in range(r + 1)]
            Tr2 = [T(r2p, m, r) for m in range(r + 1)]
            # (1) telescoping
            for m in range(r):
                checks += 1
                lhs = Tg[m + 1]
                rhs = ladd(ladd(Tr[m + 1], Tg[m]), lneg(Tr2[m]))
                if ladd(lhs, lneg(rhs)):
                    fails += 1; print("telescoping FAIL", r, p, m)
            # (2) closed forms
            for j in range(r + 1):
                checks += 2
                if ladd(Tr[j], lneg(closed_rho(r, p, j, False))):
                    fails += 1; print("rho FAIL", r, p, j, Tr[j])
                if ladd(Tr2[j], lneg(closed_rho(r, p, j, True))):
                    fails += 1; print("rho' FAIL", r, p, j, Tr2[j])
            # (3) trace formula: sum_m q^{2m} T_m(g^p),
            #     T_m(g^p) = sum_{j<=m} T_j(rho^p) - sum_{j<m} T_j(rho'^p)
            checks += 1
            tr = ZERO
            for m in range(r + 1):
                tr = ladd(tr, lmul(mono(2 * m), Tg[m]))
            pred = ZERO
            for j in range(r + 1):
                for m in range(j, r + 1):
                    pred = ladd(pred, lmul(mono(2 * m), closed_rho(r, p, j, False)))
                for m in range(j + 1, r + 1):
                    pred = ladd(pred, lneg(lmul(mono(2 * m), closed_rho(r, p, j, True))))
            if ladd(tr, lneg(pred)):
                fails += 1; print("trace FAIL", r, p)
            if gcd(r, p) > 1 and r <= 4 and p <= 6:
                print(f"r={r} p={p} d={gcd(r,p)}  T(gamma^p) by weight:",
                      [sorted(t.items()) for t in Tg])
    print(f"checks={checks} fails={fails}")
    return 1 if fails else 0

if __name__ == "__main__":
    sys.exit(main())
