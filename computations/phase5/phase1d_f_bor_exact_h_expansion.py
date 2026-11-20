#!/usr/bin/env python3
"""
Phase 1d: exact h-expansion of F_Bor and the substrate identity.

The substrate identity for the proton mass is:
  m_p = 2·m_μ·F_Bor(q₀) − 12·m_e

where F_Bor(q) = |tr_M(β_Bor, q)| · [3]_q! / q³.

Phase 1c proved that |tr_M|'s h² coefficient is EXACTLY ZERO (per-
partition cancellation: 5/128 − 20/128 + 15/128 = 0). This means
F_Bor's h² sensitivity comes entirely from [3]_q! and q³.

This script derives the EXACT rational h-expansion coefficients of
F_Bor analytically (sympy), then computes the per-coefficient
contribution to the m_p residual.

STRUCTURAL RESULT: F_Bor = 6 − 9h + (19/2)h² + ... where all
coefficients are exact rationals derivable from Lean-proved forms.
"""
from __future__ import annotations


# Path bridge (subdirectory refactor — Phase 3, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys
import time
from pathlib import Path

import sympy as sp
from sympy import Symbol, sqrt, Rational, cancel, series, Abs

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder
from _precision import set_compute_dps  # noqa: E402

h = Symbol("h")


def tr_M_lean(hv):
    """Lean-proved Borromean Markov trace in h."""
    return (4 + hv**2 - 3*hv**4 - hv**6) / (hv**2 + 4)


def q_of_h(hv):
    """q = (h + √(h²+4))/2 — positive root of q − 1/q = h."""
    return (hv + sqrt(hv**2 + 4)) / 2


def qfact3_of_h(hv):
    """[3]_q! = (h² + 3)·√(h² + 4) — exact closed form."""
    return (hv**2 + 3) * sqrt(hv**2 + 4)


def q_cubed_of_h(hv):
    """q³ as function of h."""
    return q_of_h(hv)**3


def main():
    t0 = time.time()
    print("=" * 70)
    print("  Phase 1d: exact h-expansion of F_Bor")
    print("=" * 70)
    print()

    order = 10

    # |tr_M(β_Bor)|
    print("  |tr_M(β_Bor, h)| = (4 + h² − 3h⁴ − h⁶)/(h² + 4)")
    tr_ser = series(tr_M_lean(h), h, 0, order + 1)
    print(f"  h-expansion (order {order}):")
    tr_coeffs = {}
    for k in range(order + 1):
        ck = sp.nsimplify(tr_ser.coeff(h, k))
        tr_coeffs[k] = ck
        if ck != 0:
            print(f"    h^{k}: {ck}")
    print()

    # [3]_q!
    print("  [3]_q!(h) = (h² + 3)·√(h² + 4)")
    qf_ser = series(qfact3_of_h(h), h, 0, order + 1)
    print(f"  h-expansion:")
    qf_coeffs = {}
    for k in range(order + 1):
        ck = sp.nsimplify(qf_ser.coeff(h, k))
        qf_coeffs[k] = ck
        if ck != 0:
            print(f"    h^{k}: {ck}")
    print()

    # q³
    print("  q³(h) = ((h + √(h²+4))/2)³")
    q3_ser = series(q_cubed_of_h(h), h, 0, order + 1)
    print(f"  h-expansion:")
    q3_coeffs = {}
    for k in range(order + 1):
        ck = sp.nsimplify(q3_ser.coeff(h, k))
        q3_coeffs[k] = ck
        if ck != 0:
            print(f"    h^{k}: {ck}")
    print()

    # F_Bor = |tr_M| · [3]_q! / q³
    print("  F_Bor(h) = |tr_M|·[3]_q!/q³")
    f_bor = tr_M_lean(h) * qfact3_of_h(h) / q_cubed_of_h(h)
    f_ser = series(f_bor, h, 0, order + 1)
    print(f"  h-expansion:")
    f_coeffs = {}
    for k in range(order + 1):
        ck = sp.nsimplify(f_ser.coeff(h, k))
        f_coeffs[k] = ck
        if ck != 0:
            print(f"    h^{k}: {ck}")
    print()

    # m_p = 2·m_μ·F_Bor − 12·m_e
    # At h₀ = 0.20906...
    print("=" * 70)
    print("  m_p substrate identity h-dependence")
    print("=" * 70)
    import mpmath as mp
    set_compute_dps()
    from q_parameter import Q_50_DIGIT_STR, Q_MP
    from codata_constants import M_E_MEV as m_e, M_MU_MEV_VALIDATION as m_mu  # registry (no literals)
    q0 = Q_MP
    h0 = q0 - 1/q0

    print(f"\n  h₀ = {mp.nstr(h0, 15)}")
    print(f"  h₀² = {mp.nstr(h0**2, 15)}")

    # Evaluate F_Bor via h-series
    f_partial_sums = []
    running = mp.mpf(0)
    for k in range(min(order + 1, 10)):
        ck = f_coeffs.get(k, 0)
        if ck != 0:
            running += mp.mpf(str(float(ck))) * h0**k
        f_partial_sums.append(running)

    # Exact F_Bor
    f_exact = mp.mpf("4.46913859786073375")  # from earlier computation

    print(f"\n  F_Bor convergence of h-series at h₀:")
    for k, ps in enumerate(f_partial_sums):
        err_ppm = abs(ps - f_exact) / f_exact * mp.mpf("1e6")
        print(f"    through h^{k}: F = {mp.nstr(ps, 12)}, err = {mp.nstr(err_ppm, 6)} ppm")

    # Per-coefficient m_p contribution: m_p = 2·m_μ·F_Bor − 12·m_e
    print(f"\n  Per-coefficient m_p contribution (2·m_μ × c_k × h₀^k):")
    for k in range(min(8, order + 1)):
        ck = f_coeffs.get(k, 0)
        if ck != 0:
            contrib = 2 * m_mu * mp.mpf(str(float(ck))) * h0**k
            print(f"    h^{k} (c={ck}): {mp.nstr(contrib, 12)} MeV")

    print(f"\n  −12·m_e = {mp.nstr(-12 * m_e, 12)} MeV")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    # ── Witness ──────────────────────────────────────────────────
    w = WitnessBuilder("phase1d-f-bor-exact-h-expansion", engine="sympy")
    w.set_description(
        "Exact h-expansion of F_Bor(q) = |tr_M(β_Bor)|·[3]_q!/q³ — the "
        "categorical observable in the proton substrate identity "
        "m_p = 2·m_μ·F_Bor − 12·m_e. All coefficients are exact rationals. "
        "Phase 1c proved h²(tr_M) = 0; this shows F_Bor's h² = 19/2 comes "
        "entirely from [3]_q! (11/4) and q³ (9/8) via division."
    )
    w.set_content_block("prop:proton-mass-substrate-identity")
    w.set_audit_only("docs/audits/2026-05-26-phase1d-f-bor-h-expansion.md")

    for label, coeffs in [("tr_M", tr_coeffs), ("qfact3", qf_coeffs),
                           ("q_cubed", q3_coeffs), ("F_Bor", f_coeffs)]:
        w.add_data(f"h_expansion_{label}", {
            str(k): str(v) for k, v in coeffs.items() if v != 0
        })

    w.add_assertion(
        name="tr_M_h2_is_zero",
        computed=int(tr_coeffs.get(2, 0) == 0),
        expected=1,
        tolerance=0,
        source="Phase 1c proved: tr_M h² coefficient = 0 (per-partition cancellation)"
    )
    w.add_assertion(
        name="F_Bor_h2_is_19_over_2",
        computed=int(f_coeffs.get(2, 0) == Rational(19, 2)),
        expected=1,
        tolerance=0,
        source="F_Bor h² = 19/2, derived from [3]_q! (11/4) and q³ (9/8)"
    )

    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
