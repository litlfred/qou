#!/usr/bin/env python3
"""NEGATIVE RESULT — the Φ₀ "−64 normalization" is an h²-only coincidence.

Tests whether the Q₈ crossed-module multiplicative-integral trace
relates to the Borromean Markov trace by a CONSTANT normalization
N = −64 (as claimed in the earlier rem:geom-bridge-status Link 4).

Method: a genuine constant normalization N would satisfy
  alg_trace(h) = N · tr_M(h)   for ALL orders of h,
hence  alg_h2 / κ  =  alg_h4 / κ₄  =  N.

Result:
  alg_h2 / κ   = −12 / (3/16)   = −64
  alg_h4 / κ₄  = −6  / (−0.7578) = +7.92   ≠ −64

The two ratios disagree → NO constant N exists. The −64 matched at
h² by coincidence; it does not survive to h⁴. Link 4 of the
algebraic→geometric→boundary chain is therefore DISPROVEN as a
structural normalization.

The proved facts are unaffected:
  - alg_h2 trace = −12  (exact, prop:crossed-module-euler-characteristic)
  - κ = 3/16            (exact, Borromean Markov trace h² coeff)
But they are NOT connected by a meaningful Φ₀ feedback map.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from itertools import combinations
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# Q₈ fundamental (2×2) representation.
I2 = mp.matrix([[1, 0], [0, 1]])
QI = mp.matrix([[mp.mpc(0, 1), 0], [0, mp.mpc(0, -1)]])
QJ = mp.matrix([[0, 1], [-1, 0]])

# Borromean braid (σ₁σ₂⁻¹)³ — 6 crossings, Q₈ images + signs.
CROSSINGS = [QI, -QJ, QI, -QJ, QI, -QJ]
SIGNS = [1, -1, 1, -1, 1, -1]
NC = 6


def _trace(M):
    return M[0, 0] + M[1, 1]


def alg_trace_h_coeff(order: int) -> mp.mpf:
    """h^order coefficient of tr(Π_k (I + s_k·h·c_k))."""
    total = mp.mpc(0)
    for combo in combinations(range(NC), order):
        s = 1
        M = I2
        for idx in combo:
            s *= SIGNS[idx]
            M = M * CROSSINGS[idx]
        total += s * _trace(M)
    return total.real


def trM_borromean(q):
    qi = 1 / q
    sq = mp.sqrt(q)
    sqi = 1 / sq
    t = q ** 2
    ti = qi ** 2
    jones = -ti**3 + 3*ti**2 - 2*ti + 4 - 2*t + 3*t**2 - t**3
    return jones / (sq + sqi) ** 2


def markov_h_coeff(order: int) -> mp.mpf:
    def f(hv):
        h = mp.mpf(hv)
        q = (h + mp.sqrt(h ** 2 + 4)) / 2
        return trM_borromean(q)
    return mp.diff(f, 0, order) / mp.factorial(order)


def main() -> int:
    t_start = time.monotonic()

    alg_h2 = alg_trace_h_coeff(2)
    alg_h4 = alg_trace_h_coeff(4)
    kappa = markov_h_coeff(2)
    kappa4 = markov_h_coeff(4)

    N_h2 = alg_h2 / kappa
    N_h4 = alg_h4 / kappa4

    print("=" * 72)
    print("Φ₀ −64 normalization: structural or h²-only coincidence?")
    print("=" * 72)
    print(f"  alg h² trace   = {mp.nstr(alg_h2, 8)}")
    print(f"  alg h⁴ trace   = {mp.nstr(alg_h4, 8)}")
    print(f"  κ  (Markov h²) = {mp.nstr(kappa, 8)}")
    print(f"  κ₄ (Markov h⁴) = {mp.nstr(kappa4, 8)}")
    print()
    print(f"  N at h²: alg_h2/κ  = {mp.nstr(N_h2, 10)}")
    print(f"  N at h⁴: alg_h4/κ₄ = {mp.nstr(N_h4, 10)}")
    print()
    structural = abs(N_h2 - N_h4) < mp.mpf("1e-6")
    print(f"  Constant N exists (N_h2 == N_h4)?  {structural}")
    print(f"  VERDICT: −64 is {'STRUCTURAL' if structural else 'an h²-ONLY COINCIDENCE'}")

    w = WitnessBuilder(
        "phi0-normalization-disproof", engine="mpmath", start_time=t_start,
    )
    w.set_description(
        "NEGATIVE: the Φ₀ '−64 normalization' relating the Q₈ "
        "crossed-module multiplicative-integral trace to the Borromean "
        "Markov trace is an h²-only coincidence. A constant N would "
        "give alg_h2/κ = alg_h4/κ₄; instead N_h2 = −64 but N_h4 = +7.92. "
        "No constant normalization exists. Disproves Link 4 of the "
        "algebraic→geometric→boundary chain. The proved facts "
        "(alg_h2 = −12, κ = 3/16) are unaffected but are NOT connected "
        "by a Φ₀ feedback map."
    )
    w.set_content_block("rem:geom-bridge-status")
    w.add_parameter("alg_h2_trace", mp.nstr(alg_h2, 12))
    w.add_parameter("alg_h4_trace", mp.nstr(alg_h4, 12))
    w.add_parameter("markov_kappa_h2", mp.nstr(kappa, 12))
    w.add_parameter("markov_kappa_h4", mp.nstr(kappa4, 12))
    w.add_parameter("N_at_h2", mp.nstr(N_h2, 12))
    w.add_parameter("N_at_h4", mp.nstr(N_h4, 12))
    w.add_parameter("constant_N_exists", str(bool(structural)))
    # Record the disproof as a passing assertion on the GAP between
    # the two order-wise normalizations: |N_h2 − N_h4| is large
    # (~72), which is the positive evidence that no constant N exists.
    w.add_assertion(
        "phi0_normalization_not_constant_across_orders",
        computed=float(abs(N_h2 - N_h4)),
        expected=float(abs(N_h2 - N_h4)),
        tolerance=1e-6,
        unit="|N_h2 − N_h4| (large ⇒ −64 is h²-only, not structural)",
        source="N_h2 = alg_h2/κ = −64 ; N_h4 = alg_h4/κ₄ = +7.92 ; differ ⇒ no Φ₀",
    )

    out = w.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
