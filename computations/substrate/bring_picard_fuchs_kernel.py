"""Identification half of the keystone — charpoly(M) → recurrence kernel.

The existence half (`prop:prolonged-periods-fixed-depth`, merged into PR
#1903) proves that the prolonged periods satisfy a fixed-depth recurrence
whose kernel is the **characteristic-polynomial coefficients of the
prolongation operator `M`** (Cayley–Hamilton). This module is the
identification machinery: given `M` (the Gauss–Manin / prolongation matrix
on the rank-`r` period space), `recurrence_kernel(M)` returns `(d, c)` with

    M^d = Σ_{j<d} c_j M^j ,   d = r,   c_j = −(charpoly coeff of x^j).

So `R` (the q-difference kernel = prolongation symbol) is `charpoly(M)`.
The OPEN input is the explicit `M` for the Bring curve — its branch-point
local-monodromy / Picard–Fuchs data (`docs/workplans/...keystone...`).

Self-validation: the 2×2 companion matrix of the torus Chebyshev recurrence
`a_{n+2} = 2cosh(2η₀)·a_{n+1} − a_n` is `[[0,1],[−1, 2cosh(2η₀)]]`; its
charpoly must return kernel `c = [−1, 2cosh(2η₀)]` — matching the depth-2
recurrence `sw_prolongation_symbol.py` recovers from the torus periods.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_HERE = _Path(__file__).resolve().parent
_sys.path.insert(0, str(_HERE.parent))  # computations/
_sys.path.insert(0, str(_HERE))         # substrate/
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402


def _charpoly_coeffs(A: mp.matrix):
    """Monic characteristic polynomial coefficients `[p_0, …, p_{d-1}, 1]`
    of `A` (so `p(x) = Σ_i p_i x^i`, `p_d = 1`), via Faddeev–LeVerrier.
    mpmath has no `charpoly`; FL is exact and mpf-friendly."""
    n = A.rows
    I = mp.eye(n)
    M = mp.eye(n)            # M_0 = I
    p = [mp.mpf(1)] * (n + 1)  # p[n] = 1 (monic)
    for k in range(1, n + 1):
        AM = A * M
        tr = sum(AM[i, i] for i in range(n))
        ck = -tr / k          # coefficient p_{n-k}
        p[n - k] = ck
        M = AM + ck * I       # M_k
    return p


def recurrence_kernel(M: mp.matrix):
    """Given the prolongation matrix `M` (square, rank `r`), return
    `(d, c)` where `M^d = Σ_{j<d} c_j M^j` is the Cayley–Hamilton
    recurrence: `d = r` and `c_j = −p_j` for the monic charpoly
    `x^d + Σ_{j<d} p_j x^j`."""
    d = M.rows
    p = _charpoly_coeffs(M)           # p[j] for j = 0..d (monic, p[d]=1)
    c = [-p[j] for j in range(d)]     # x^d = Σ_{j<d} (−p_j) x^j
    return d, c


def _emit_witness() -> None:
    from witness_base import WitnessBuilder
    from q_parameter import Q_50_DIGIT_STR as Qs

    mp.mp.dps = COMPUTE_DPS
    eta0 = mp.log(mp.mpf(Qs))
    tol = mp.mpf(10) ** (-(COMPUTE_DPS - 8))

    # Self-validation: companion matrix of the torus Chebyshev recurrence.
    c1 = 2 * mp.cosh(2 * eta0)
    M = mp.matrix([[0, 1], [-1, c1]])
    d, c = recurrence_kernel(M)
    ok = 1 if (d == 2 and abs(c[0] + 1) < tol and abs(c[1] - c1) < tol) else 0

    w = WitnessBuilder("bring-picard-fuchs-kernel", engine="mpmath")
    w.set_audit_only(
        "docs/workplans/2026-06-05-keystone-prolongation-symbol-derivation.md"
    )
    w.add_parameter("q_0", Qs)
    w.add_data("self_validation_companion", {
        "depth": d,
        "kernel_c": [mp.nstr(x, 12) for x in c],
        "expected_c": ["-1", mp.nstr(c1, 12)],
    })
    w.add_data("bring_M_status",
               "explicit prolongation matrix M for the Bring curve is the open "
               "input (branch-point local monodromy / Picard–Fuchs); "
               "recurrence_kernel(M) yields R the moment M is supplied")
    w.add_assertion(
        "charpoly_recovers_chebyshev_kernel",
        computed=ok, expected=1,
        source="charpoly([[0,1],[-1,2cosh2η₀]]) → kernel [-1, 2cosh(2η₀)]")
    out = w.save()
    print(f"  Witness: {out.name}")


if __name__ == "__main__":
    mp.mp.dps = COMPUTE_DPS
    from q_parameter import Q_50_DIGIT_STR as Qs
    eta0 = mp.log(mp.mpf(Qs))
    c1 = 2 * mp.cosh(2 * eta0)
    M = mp.matrix([[0, 1], [-1, c1]])
    d, c = recurrence_kernel(M)
    print("Identification machinery (PR #1903) — charpoly(M) → kernel")
    print(f"  self-test companion M=[[0,1],[-1,2cosh2η₀]]: depth {d}, "
          f"kernel [{', '.join(mp.nstr(x, 10) for x in c)}]")
    print(f"  expected [-1, 2cosh(2η₀)={mp.nstr(c1, 10)}]")
    print("  Bring M: open input (branch-point monodromy) — supply M ⇒ get R")
    _emit_witness()
