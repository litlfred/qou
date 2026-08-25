"""tetrahedron_index.py — Dimofte–Gaiotto–Gukov tetrahedron index I_Δ(m,e)(q).

Canonical building block for the 3d-index face of the figure-eight (4₁)
resurgent structure (G3 keystone attack,
docs/audits/2026-07-14-g3-stokes-via-3d-index.md).

Definition (DGG 2011; Garoufalidis, "The 3D index of an ideal
triangulation and angle structures", arXiv:1208.1663):

    I_Δ(m, e)(q) = Σ_{n=max(0,-e)}^∞ (-1)^n
                     q^{ n(n+1)/2 - (n + e/2) m }
                     / ( (q;q)_n · (q;q)_{n+e} )

with (q;q)_n = ∏_{j=1}^n (1 - q^j).  The half-integer q-powers make this
a series in q^{1/2}; we carry q as an mpmath value and evaluate the
truncated sum (the summand decays factorially in n via the Pochhammers).

Self-validation: the tetrahedron index satisfies the S₃ triality
    I_Δ(m, e) = (-q^{1/2})^{-e}? ...  (several conventions in the
literature differ by q^{1/2} vs q factors).  Rather than hardcode one
convention as a gate, `check_symmetries` evaluates BOTH the (-q) and the
(-q^{1/2}) forms of
    I_Δ(m, e) =? (±q^?)^e I_Δ(-e-m, m) =? (±q^?)^{e+m} I_Δ(e, -e-m)
numerically and reports which holds — an empirical correctness check on
the implementation that does not depend on remembering the exact power.

No production wiring; audit-only building block.
"""

from __future__ import annotations

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402


def q_pochhammer(q, n):
    """(q;q)_n = ∏_{j=1}^n (1 - q^j).  n may be 0 (empty product = 1)."""
    if n < 0:
        return mp.inf  # 1/(q;q)_{negative} = 0 by convention
    prod = mp.mpf(1)
    for j in range(1, n + 1):
        prod *= (1 - q ** j)
    return prod


def tetrahedron_index(m, e, q, nmax=80):
    """I_Δ(m,e)(q), truncated at n = nmax.

    m, e are integers; q an mpmath real/complex with |q| < 1.
    """
    lo = max(0, -e)
    total = mp.mpf(0)
    for n in range(lo, nmax + 1):
        denom = q_pochhammer(q, n) * q_pochhammer(q, n + e)
        if denom == 0 or denom == mp.inf:
            continue
        expo = mp.mpf(n * (n + 1)) / 2 - (mp.mpf(n) + mp.mpf(e) / 2) * m
        total += (-1) ** n * q ** expo / denom
    return total


def check_symmetries(q, cases, tol=None):
    """Empirically detect which triality convention the implementation
    satisfies.  Returns a list of dicts with the residuals of each
    candidate relation so the caller can assert the true one."""
    if tol is None:
        tol = mp.mpf(10) ** (-mp.mp.dps + 8)
    out = []
    for (m, e) in cases:
        base = tetrahedron_index(m, e, q)
        # candidate A: (-q)^e I_Δ(-e-m, m)
        relA = (-q) ** e * tetrahedron_index(-e - m, m, q)
        # candidate B: (-q^{1/2})^e I_Δ(-e-m, m)
        relB = (-(q ** mp.mpf("0.5"))) ** e * tetrahedron_index(-e - m, m, q)
        # candidate C: q^{e/2} I_Δ(-e-m, m)  (unsigned half-power)
        relC = (q ** (mp.mpf(e) / 2)) * tetrahedron_index(-e - m, m, q)
        out.append({
            "m": m, "e": e,
            "base": mp.nstr(base, 12),
            "resid_negq^e": mp.nstr(abs(base - relA), 6),
            "resid_neg_sqrtq^e": mp.nstr(abs(base - relB), 6),
            "resid_sqrtq^e_unsigned": mp.nstr(abs(base - relC), 6),
        })
    return out


if __name__ == "__main__":
    set_compute_dps()
    q = mp.mpf("0.1")  # small real q for a clean convergence self-test
    print("Tetrahedron index self-test at q = 0.1")
    print(f"  I_Δ(0,0)  = {mp.nstr(tetrahedron_index(0, 0, q), 12)}")
    print(f"  I_Δ(0,1)  = {mp.nstr(tetrahedron_index(0, 1, q), 12)}")
    print(f"  I_Δ(1,0)  = {mp.nstr(tetrahedron_index(1, 0, q), 12)}")
    print(f"  I_Δ(0,-1) = {mp.nstr(tetrahedron_index(0, -1, q), 12)}")
    print("\nTriality residuals (smallest column = the true convention):")
    for row in check_symmetries(q, [(0, 1), (1, 1), (2, -1), (1, -2)]):
        print(f"  m={row['m']:>2} e={row['e']:>2}: "
              f"(-q)^e {row['resid_negq^e']:>12}  "
              f"(-√q)^e {row['resid_neg_sqrtq^e']:>12}  "
              f"√q^e {row['resid_sqrtq^e_unsigned']:>12}")
