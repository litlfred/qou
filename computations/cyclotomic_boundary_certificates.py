#!/usr/bin/env python3
"""cyclotomic_boundary_certificates.py — exact Habiro tails D(n) and finite non-cyclotomicity
witnesses, for conj:cyclotomic-boundary-at-keystone.

Definitions (as in the content block and in QOU.Mass.CyclotomicBoundaryCertified):
    [k]_q   = (q^k - q^{-k}) / (q - q^{-1})            (balanced quantum integer)
    dim_q λ = [n]_q! / prod_{cells} [hook]_q
    S(n)    = sum_{λ ⊢ n} dim_q λ
    D(n)    = S(n) - S(n-1) - [n-1]_q S(n-2)
    P_n     = q^{m_n} D(n) in Z[q],  P_n(0) != 0       (the cleared tail)

Everything is exact integer arithmetic on Laurent polynomials; no floats, no fitting.

Witness search (n >= 6): a prime p, an integer a with p | P_n(a), p ∤ a, multiplicative order
m of a mod p with phi(m) > deg P_n, and b with p ∤ P_n(b).  By
`not_isCycloProduct_of_witness` such a witness proves P_n is not c * X^j * prod Phi_k.
The Lean module re-checks every number; this script only finds them.

Usage: python3 computations/cyclotomic_boundary_certificates.py [N]   (default N = 14)
Writes computations/cyclotomic-boundary-certificates.witness.json.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path


def partitions(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, m), 0, -1):
        for r in partitions(n - k, k):
            yield (k,) + r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])] if lam else []
    return [(row - j) + (conj[j] - i) - 1 for i, row in enumerate(lam) for j in range(row)]


# polynomials in t as coefficient lists (ints)
def pmul(a, b):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                r[i + j] += x * y
    return r


def pdiv_exact(a, b):
    a = a[:]
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(q) - 1, -1, -1):
        c, rem = divmod(a[i + len(b) - 1], b[-1])
        assert rem == 0
        q[i] = c
        for j, y in enumerate(b):
            a[i + j] -= c * y
    assert not any(a)
    return q


def ub(k):  # 1 + t + ... + t^{k-1}
    return [1] * k


def laurent_dim(lam):
    """dim_q(lam) as {exponent of q: coeff}; = q^{-e} g(q^2)."""
    n = sum(lam)
    num = [1]
    for k in range(1, n + 1):
        num = pmul(num, ub(k))
    den = [1]
    for h in hooks(lam):
        den = pmul(den, ub(h))
    g = pdiv_exact(num, den)
    e = n * (n - 1) // 2 - sum(h - 1 for h in hooks(lam))
    return {2 * k - e: c for k, c in enumerate(g) if c}


def ladd(a, b, s=1):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0) + s * v
    return {k: v for k, v in r.items() if v}


def lmul(a, b):
    r = {}
    for i, x in a.items():
        for j, y in b.items():
            r[i + j] = r.get(i + j, 0) + x * y
    return {k: v for k, v in r.items() if v}


def qbal(k):
    return {k - 1 - 2 * i: 1 for i in range(k)}


_S = {}


def S(n):
    if n <= 0:
        return {0: 1}
    if n not in _S:
        r = {}
        for lam in partitions(n):
            r = ladd(r, laurent_dim(lam))
        _S[n] = r
    return _S[n]


def tail(n):
    D = ladd(ladd(S(n), S(n - 1), -1), lmul(qbal(n - 1), S(n - 2)), -1)
    if not D:
        return None
    m = -min(D)
    P = [0] * (max(D) + m + 1)
    for k, v in D.items():
        P[k + m] = v
    return m, P


def is_prime(p):
    if p < 2:
        return False
    i = 2
    while i * i <= p:
        if p % i == 0:
            return False
        i += 1
    return True


def order(a, p):
    x, k = a % p, 1
    while x != 1:
        x, k = x * a % p, k + 1
    return k


def phi(m):
    r, x, f = m, m, 2
    while f * f <= x:
        if x % f == 0:
            while x % f == 0:
                x //= f
            r -= r // f
        f += 1
    if x > 1:
        r -= r // x
    return r


def witness(P):
    d = len(P) - 1
    ev = lambda a, p: sum(c * pow(a, i, p) for i, c in enumerate(P)) % p
    for p in range(3, 5000):
        if not is_prime(p):
            continue
        for a in range(2, p):
            if ev(a, p) == 0 and phi(order(a, p)) > d:
                b = next((b for b in range(1, p) if ev(b, p) != 0), None)
                if b is not None:
                    return {"p": p, "a": a, "order": order(a, p), "phi_order": phi(order(a, p)),
                            "b": b, "deg": d}
    return None


def main() -> int:
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 14
    out = {}
    for n in range(2, N + 1):
        t = tail(n)
        if t is None:
            out[n] = {"D": 0}
            print(f"n={n}: D(n) = 0")
            continue
        m, P = t
        rec = {"shift": m, "coeffs": P}
        if n >= 6:
            w = witness(P)
            rec["witness"] = w
            print(f"n={n}: deg {len(P)-1}, witness {w}")
        else:
            print(f"n={n}: deg {len(P)-1}, coeffs {P}")
        out[n] = rec
    path = Path(__file__).with_name("cyclotomic-boundary-certificates.witness.json")
    path.write_text(json.dumps(out, indent=1) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
