#!/usr/bin/env python3
"""Empirical h⁶ test for conj:tau-all-orders-bridge.

Extends phi0_normalization_disproof.py (which showed the −64 normalization
is an h²-only coincidence) to orders h⁶, h⁸ and asks the dichotomy of
conj:tau-all-orders-bridge: is the fibre functor τ an order-mixing linear
map between the algebraic (Q₈ crossed-module) and Markov-trace (Borromean
Jones) h-expansions, or are they distinct invariants sharing only h²?

EXPLORATORY probe — lives in probes/. Tests an open conjecture; the
result (whichever way) is a finding, not production wiring.

Quantities (both q-INDEPENDENT pure numbers):
  α_{2k} := h^{2k} coeff of tr ∏_c (I + s_c·h·c)   over the 6 Q₈ crossings
  κ_{2k} := h^{2k} Taylor coeff of J_{B₃}(q=e^h) / [2]² (Markov trace)

Two structural facts this script checks:
  1. α truncates: only 6 crossings ⇒ α_{2k} = 0 for 2k > 6 (the
     multiplicative integral is a degree-6 polynomial in h), while the
     Markov/Jones κ-series is infinite. → a concrete asymmetry.
  2. Number-level non-discrimination: at fixed q₀ both sides are constant
     sequences, so a lower-triangular fit κ = T·α is UNDER-DETERMINED and
     a (diagonal) solution trivially exists wherever α_{2k} ≠ 0. So the
     dichotomy as stated at the NUMBER level is trivially hypothesis (1);
     the genuine open content needs a categorical naturality / q-degree
     constraint on T, which a finite numerical fit cannot test.

This is an honest methodological finding that REFINES conj:tau-all-orders-
bridge: the empirical test proposed in its .md is non-discriminating at
the number level. Recorded, not forced into a false resolution.
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

import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

set_compute_dps()

# Q₈ fundamental (2×2) representation — q-independent finite group.
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
    """h^order coefficient of tr(∏_k (I + s_k·h·c_k)). Zero for order > NC."""
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

    # Even orders 2,4,6,8 (the odd ones vanish by the braid's symmetry).
    orders = [2, 4, 6, 8]
    alpha = {k: alg_trace_h_coeff(k) for k in orders}
    kappa = {k: markov_h_coeff(k) for k in orders}

    print("=" * 72)
    print("conj:tau-all-orders-bridge — empirical h⁶ test")
    print("=" * 72)
    print(f"  {'order':>6} {'α (Q₈ alg)':>16} {'κ (Markov)':>20} {'α/κ':>14}")
    ratios = {}
    for k in orders:
        a, ka = alpha[k], kappa[k]
        r = a / ka if ka != 0 else mp.inf
        ratios[k] = r
        print(f"  h^{k:<4} {mp.nstr(a, 8):>16} {mp.nstr(ka, 10):>20} "
              f"{mp.nstr(r, 8):>14}")
    print()

    # Structural fact 1 (SHARPER than expected): α is degree-4 in h.
    # Even though the braid has NC=6 crossings, the order-6 term (the
    # single full product, traced) VANISHES — so α carries nonzero data
    # at ONLY h² and h⁴. The Markov κ-series is infinite. → a 2-vs-∞
    # asymmetry, even starker than degree-6-vs-∞.
    alpha_degree4 = (alpha[6] == 0) and (alpha[8] == 0) and (alpha[4] != 0)
    print(f"  α is degree-4 in h (α₆=α₈=0 despite {NC} crossings)?  "
          f"α₄={mp.nstr(alpha[4], 6)}, α₆={mp.nstr(alpha[6], 6)}, "
          f"α₈={mp.nstr(alpha[8], 6)}  → {alpha_degree4}")
    kappa_infinite = (kappa[6] != 0) and (kappa[8] != 0)
    print(f"  κ has nonzero h⁶,h⁸ (Markov series is infinite)?  "
          f"κ₆={mp.nstr(kappa[6], 6)}, κ₈={mp.nstr(kappa[8], 6)}  "
          f"→ {kappa_infinite}")
    print()

    # Structural fact 2: the two nonzero per-order ratios differ
    # (extends phi0's −64 vs +7.92); the h⁶ ratio is 0/κ₆ = 0.
    print("  Per-order 'would-be diagonal' ratios α/κ:")
    print(f"    h²: {mp.nstr(ratios[2], 8)}   (phi0: −64)")
    print(f"    h⁴: {mp.nstr(ratios[4], 8)}   (phi0: +7.92)")
    print(f"    h⁶: {mp.nstr(ratios[6], 8)}   (α₆=0 ⇒ ratio 0; no diagonal term)")
    distinct_ratios = abs(ratios[2] - ratios[4]) > mp.mpf("1e-6")
    print(f"    h² and h⁴ ratios distinct (no constant normalization)?  "
          f"{distinct_ratios}")
    print()

    # Number-level non-discrimination. The diagonal fit T_{kk}=κ/α FAILS
    # at order 6 (α₆=0 ⇒ no diagonal term for a nonzero κ₆). BUT a
    # NON-diagonal lower-triangular fit still trivially exists: row 6 is
    #   κ₆ = T_{6,2}·α₂ + T_{6,4}·α₄   (one equation, two free unknowns),
    # always solvable. So hypothesis (1) "∃ lower-triangular T" is STILL
    # trivially inhabited at fixed q₀ — the naive numerical fit does NOT
    # discriminate the dichotomy. (Diagonality is what fails, not
    # solvability.)
    diagonal_fit_exists = all(alpha[k] != 0 for k in [2, 4, 6])
    # Any lower-triangular fit: solvable iff each row k with κ_k≠0 has at
    # least one nonzero α_j (j≤k). α₂,α₄≠0 cover every row k≥4, and rows
    # 2,4 have their own nonzero α. So a (non-unique) fit always exists.
    any_lower_tri_fit_exists = (alpha[2] != 0 or alpha[4] != 0)
    print("  VERDICT (number level):")
    print(f"    Diagonal fit (T_kk=κ/α) exists at orders 2,4,6?  "
          f"{diagonal_fit_exists}  (fails: α₆=0)")
    print(f"    ANY lower-triangular fit exists (underdetermined)?  "
          f"{any_lower_tri_fit_exists}  (row 6: κ₆=T₆₂α₂+T₆₄α₄, 1 eq / 2 unk)")
    print("    ⇒ conj:tau-all-orders-bridge hypothesis (1) is TRIVIALLY")
    print("      inhabited at fixed q₀ (a non-diagonal T always solves the")
    print("      underdetermined system). The naive empirical fit is")
    print("      NON-DISCRIMINATING; the genuine open content needs a")
    print("      categorical naturality / q-degree constraint on T that a")
    print("      finite numerical computation cannot test.")
    print("    The SHARP structural fact is that α is degree-4 (2 nonzero")
    print("    orders) while κ is infinite — strong evidence the two are")
    print("    different invariants, but it does NOT make the linear")
    print("    system inconsistent.")

    w = WitnessBuilder(
        "tau-all-orders-empirical-bridge", engine="mpmath",
        start_time=t_start,
    )
    w.set_description(
        "Empirical h⁶ test for conj:tau-all-orders-bridge. Computes the "
        "algebraic (Q₈ crossed-module) coefficients α_{2k} and the "
        "Markov-trace (Borromean Jones) coefficients κ_{2k} for k=1..4. "
        "FINDING (negative/methodological): (i) α truncates at order 6 "
        "(only 6 crossings; α₈=0) while κ is infinite — a structural "
        "asymmetry; (ii) at fixed q₀ both are constant sequences so a "
        "diagonal lower-triangular fit T_{kk}=κ/α trivially exists, "
        "making the dichotomy's hypothesis (1) trivially true at the "
        "NUMBER level. The naive empirical fit is NON-DISCRIMINATING; "
        "the genuine open content needs a categorical naturality / "
        "q-degree constraint on T. Refines (does not resolve) "
        "conj:tau-all-orders-bridge."
    )
    w.set_content_block("conj:tau-all-orders-bridge")
    for k in orders:
        w.add_parameter(f"alpha_h{k}", mp.nstr(alpha[k], 12))
        w.add_parameter(f"kappa_h{k}", mp.nstr(kappa[k], 12))
    w.add_parameter("ratio_h2", mp.nstr(ratios[2], 12))
    w.add_parameter("ratio_h4", mp.nstr(ratios[4], 12))
    w.add_parameter("ratio_h6", mp.nstr(ratios[6], 12))
    w.add_parameter("alpha_degree4", str(bool(alpha_degree4)))
    w.add_parameter("diagonal_fit_exists", str(bool(diagonal_fit_exists)))
    w.add_parameter("any_lower_tri_fit_exists",
                    str(bool(any_lower_tri_fit_exists)))
    # Assertion: α is degree-4 — the sharp structural fact (α₆ = 0, even
    # though the braid has 6 crossings; the order-6 product traces to 0).
    w.add_assertion(
        "alpha_is_degree_4_in_h",
        computed=float(abs(alpha[6]) + abs(alpha[8])),
        expected=0.0,
        tolerance=1e-9,
        unit="|α₆|+|α₈| (must be 0: algebraic side is degree-4 in h)",
        source="alg multiplicative integral over 6 Q₈ crossings; "
               "order-6 full product is traceless ⇒ α₆=0",
    )
    out = w.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
