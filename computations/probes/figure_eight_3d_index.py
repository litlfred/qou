#!/usr/bin/env python3
"""figure_eight_3d_index.py — the GGM 3D-index of the figure-eight (4_1) knot.

Closes the G3 3d-index gluing (docs/audits/2026-07-18-tetrahedron-index-triality-pin.md,
#3805): assembles the two-tetrahedron 4_1 index on the triality-validated tetrahedron
index I_Delta and validates it against the primary source to 11 coefficients.

SOURCE. [garoufalidis-hodgson-hoffman-rubinstein2016] Garoufalidis-Hodgson-Hoffman-Rubinstein, "The 3D-index and normal surfaces"
(arXiv:1604.02688), Example 4.1 (p.8). The figure-eight cusp gluing data gives

    I_T(x mu + y lam) = sum_{k in Z} q^k J_D(2k, k, x) J_D(2k - x + 2y, k, -2y),

where J_D is the SYMMETRIC tetrahedron index (eq 4):

    J_D(a,b,c) = (-q^1/2)^{-b} I_D(b-c, a-b)          [three equal forms; S_3-invariant]
    J_D(A,B,0) = I_D(-A,B) = q^{AB/2} + h.o.t  (A,B >= 0)   [eq 6]

The three equal forms of eq (4) ARE the S_3 triality of I_D pinned empirically in
#3868 (tetrahedron_index_triality_pin.py): the cyclic generator
I_D(m,e) = (-q^1/2)^m I_D(-e-m, m) is exactly the equality of eq (4)'s forms. So the
"normalization prefactor" the gluing needs is NOT a new object — it is that triality.

CONVERGENCE. For the 1-efficient 4_1 triangulation each term q^k J_D(2k,k,0)^2 is a
genuine POWER series of q-degree ~2k^2 (Cor 10.21), so only |k| <~ sqrt(N/2)
contribute to q^N; the naive Laurent sum sum_k I_D(k,k)^2 is the same object but with
delicate cancellation of negative powers (why a direct Laurent sum mis-converged).

VALIDATION (this probe, exact integer q-series):
    I_T(0)    = 1 - 2q - 3q^2 + 2q^3 + 8q^4 + 18q^5 + 18q^6 + 14q^7 - 12q^8 - 52q^9
                - 106 q^10           (matches the paper to 11 coefficients)
    I_T(lam)  = q^3 + 2q^4 + 5q^5 + 2q^6 - 3q^7 - 16q^8 - 32q^9 - 52q^10   (exact)
    I_T(2 mu) = -q - q^2 + 3q^3 + 6q^4 + 12q^5 + 9q^6 + 3q^7 - 19q^8 - ...  (exact)

Audit-only; no production wiring; scope-(a); comparison-only. The GGM Stokes data
for the odd/even faces is read from these q-series in follow-on work.
"""
from __future__ import annotations

import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401
from witness_base import WitnessBuilder  # noqa: E402

HI = 26  # Q = q^{1/2} powers tracked; enough for q^13


def _mul(a, b):
    r = {}
    for pa, ca in a.items():
        for pb, cb in b.items():
            p = pa + pb
            if p <= HI:
                r[p] = r.get(p, 0) + ca * cb
    return {p: c for p, c in r.items() if c}


def _inv(a):
    r = {0: 1}
    for p in range(1, HI + 1):
        r[p] = -sum(a.get(k, 0) * r.get(p - k, 0) for k in range(1, p + 1))
    return r


@lru_cache(maxsize=None)
def _qpoch(n):
    r = {0: 1}
    for j in range(1, n + 1):
        r = _mul(r, {0: 1, 2 * j: -1})
    return tuple(sorted(r.items()))


@lru_cache(maxsize=None)
def _inv_qpoch_product(n, n_plus_e):
    """1/((q)_n (q)_{n+e}) in Q — depends only on (n, n+e), not m; cached."""
    return _inv(_mul(dict(_qpoch(n)), dict(_qpoch(n_plus_e))))


def I_D(m, e):
    """Tetrahedron index I_Delta(m,e)(q) as a dict in Q=q^{1/2} (may be Laurent)."""
    lo = max(0, -e)
    tot = {}
    n = lo
    # For m <= 0 (the only case J_D calls) expo = n^2+n-(2n+e)m is monotone
    # increasing in n, so `expo > HI` lets us break early. For m > 0 (never
    # reached here) fall back to scanning the fixed window.
    mono = m <= 0
    while n <= lo + HI + 8:
        expo = n * (n + 1) - (2 * n + e) * m
        if expo > HI:
            if mono:
                break
        else:
            invd = _inv_qpoch_product(n, n + e)
            for p, c in invd.items():
                pp = p + expo
                if pp <= HI:
                    tot[pp] = tot.get(pp, 0) + ((-1) ** n) * c
        n += 1
    return {p: c for p, c in tot.items() if c}


def J_D(a, b, c):
    """Symmetric tetrahedron index J_Delta(a,b,c) (eq 4/6), a power series in Q."""
    m = min(a, b, c)
    sh = [a - m, b - m, c - m]
    sh.remove(0)
    A, B = sh  # both >= 0
    base = I_D(-A, B)  # power series from Q^{AB}
    sign = -1 if (m % 2) else 1  # (-q^{1/2})^{-m} sign part
    out = {}
    for p, cc in base.items():
        pp = p - m
        if pp <= HI:
            out[pp] = out.get(pp, 0) + sign * cc
    return {p: c for p, c in out.items() if c}


def index(x, y, kmax=8):
    """I_T(x mu + y lam)(q) as a dict in Q (Example 4.1 gluing)."""
    tot = {}
    for k in range(-kmax, kmax + 1):
        t = _mul(J_D(2 * k, k, x), J_D(2 * k - x + 2 * y, k, -2 * y))
        for p, cc in t.items():
            pp = p + 2 * k  # q^k = Q^{2k}
            tot[pp] = tot.get(pp, 0) + cc
    return {p: c for p, c in tot.items() if c}


def qcoeffs(d, n=11):
    return [d.get(2 * j, 0) for j in range(n)]


def main() -> int:
    print("=" * 74)
    print(" GGM 3D-index of the figure-eight (4_1) — assembly + primary-source check")
    print("=" * 74)

    checks = {
        "I_T(0)": (index(0, 0), [1, -2, -3, 2, 8, 18, 18, 14, -12, -52, -106]),
        "I_T(lam)": (index(0, 1), [0, 0, 0, 1, 2, 5, 2, -3, -16, -32, -52]),
        "I_T(2mu)": (index(2, 0), [0, -1, -1, 3, 6, 12, 9, 3, -19, -50, -88]),
    }
    all_ok = True
    neg_ok = True
    for name, (d, tgt) in checks.items():
        got = qcoeffs(d)
        ok = got == tgt
        negs = {p: c for p, c in d.items() if p < 0}
        neg_ok = neg_ok and not negs
        all_ok = all_ok and ok
        print(f"  {name:9} = {got}")
        print(f"  {'paper':9} = {tgt}   {'MATCH' if ok else 'MISMATCH'}"
              f"{'' if not negs else '  neg-powers: ' + str(negs)}")

    print(f"\n  power series (no negative q-powers): {neg_ok}")
    print(f"  all {len(checks)} classes match the primary source: {all_ok}")
    print("\n  The J_D symmetric form (eq 4) = the S_3 triality pinned in #3868;")
    print("  the '1/(pi b1)-style normalization' the gluing needed IS that triality.")

    wb = WitnessBuilder("figure-eight-3d-index", engine="python-exact")
    wb.set_description(
        "GGM 3D-index of the figure-eight 4_1 assembled on the triality-validated "
        "tetrahedron index I_Delta (Garoufalidis-Hodgson-Hoffman-Rubinstein 1604.02688 "
        "Ex 4.1). I_T(x mu + y lam) = sum_k q^k J_D(2k,k,x) J_D(2k-x+2y,k,-2y), with "
        "J_D the symmetric index (eq 4) whose S_3-invariance IS the triality pinned in "
        "#3868. Exact integer q-series validated to 11 coefficients: I_T(0) = "
        "1-2q-3q^2+2q^3+8q^4+18q^5+18q^6+14q^7-12q^8-52q^9-106q^10; I_T(lam), I_T(2mu) "
        "also match. Corrects the #3868 gluing record (the [1,-8,-9,...] target was a "
        "wrong secondary value; the real one is [1,-2,-3,2,8,18,...] and the "
        "normalization is eq 4, not an open problem). Audit-only; scope-(a); no fit.")
    wb.set_content_block("conj:faddeev-phi-b-quasiperiod")
    wb.add_data("I_T_0_q0_q10", qcoeffs(index(0, 0)))
    wb.add_data("I_T_lam_q0_q10", qcoeffs(index(0, 1)))
    wb.add_data("I_T_2mu_q0_q10", qcoeffs(index(2, 0)))
    wb.add_data("formula", "sum_k q^k J_D(2k,k,x) J_D(2k-x+2y,k,-2y)  (1604.02688 Ex 4.1)")
    wb.add_data("normalization_is_triality", "J_D symmetric form eq(4) = S_3 triality (#3868)")
    wb.add_assertion("index_matches_primary_source", computed=float(all_ok),
                     expected=1.0, tolerance=0.5,
                     source="I_T(0), I_T(lam), I_T(2mu) match 1604.02688 Ex 4.1 to q^10")
    wb.add_assertion("index_is_power_series", computed=float(neg_ok),
                     expected=1.0, tolerance=0.5,
                     source="no negative q-powers (1-efficient, Cor 10.21)")
    wb.save()

    print(f"\n  RESULT: {'ALL OK — 3D-index validated' if all_ok and neg_ok else 'CHECK'}")
    return 0 if (all_ok and neg_ok) else 1


if __name__ == "__main__":
    raise SystemExit(main())
