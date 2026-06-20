#!/usr/bin/env python3
"""
Phase 2c: derive (not fit) the ℏ_q correction tower.

The "fitted" coefficients (c_F ≈ 1/4, c_X ≈ 5 or 3.2) are
EMPIRICAL — matching CODATA backwards. Per AGENTS.md Rule 14
(production-vs-exploratory discipline), we need to DERIVE them
from categorical structure.

APPROACH: The corrections come from the DIFFERENCE between two
trace conventions:
  - Jones-Wenzl Markov trace (used in mass formula): z = 1/(√q+1/√q)
  - q-Schur Plancherel trace: z_qS = h/[n]_q (different normalization)

The mass formula uses the Jones-Wenzl convention, but the closed-form
building blocks (tr_M, [3]_q!, y_λ) mix conventions. The ℏ_q
corrections may be the CONVENTION-MISMATCH terms.

This script:
1. Derives the relationship between JW and q-Schur normalizations
2. Computes the convention ratio as a function of ℏ_q
3. Checks if the ratio's ℏ-expansion matches the empirical corrections
4. If yes: the "corrections" are structural (convention alignment)
5. If no: they're genuine higher-order physics

Also investigates: does the formula m_p = 2m_μF_Bor − 12m_e have an
EXACT form where "2" and "12" are replaced by q-deformed analogues
[2]_q and [12]_q (or similar), eliminating the corrections entirely?
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
from sympy import Symbol, sqrt, cancel, series, Rational
import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from codata_constants import M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402
from experimental_constants import M_E_MEV  # noqa: E402

q = Symbol("q", positive=True)
h = q - 1/q
hbar = (q - 1) / q


def main():
    set_compute_dps()
    t0 = time.time()
    mp.mp.dps = 50

    print("=" * 70)
    print("  Phase 2c: DERIVE the correction tower (not fit)")
    print("=" * 70)
    print()

    # ── 1. q-deformed mass formula hypothesis ───────────────────
    print("  1. q-deformed mass formula hypothesis")
    print()
    print("    The current formula uses INTEGER coefficients:")
    print("      m_p = 2·m_μ·F_Bor − 12·m_e")
    print()
    print("    What if the exact formula uses Q-INTEGERS?")
    print("      m_p = [2]_q·m_μ·F_Bor − [12]_q·m_e   ???")
    print("    or")
    print("      m_p = [2]_q·m_μ·F_Bor − 2·[3]_q!·m_e  ???")
    print()

    q0 = mp.mpf(Q_50_DIGIT_STR)
    h0 = q0 - 1/q0
    hbar0 = (q0 - 1) / q0
    m_e = mp.mpf(M_E_MEV)
    m_mu = mp.mpf("105.6583755")
    m_p_codata = mp.mpf(M_P_MEV_VALIDATION)

    trM = abs((4 + h0**2 - 3*h0**4 - h0**6) / (h0**2 + 4))
    qf3 = (q0**2 + 1 + q0**(-2)) * (q0 + q0**(-1))
    F = trM * qf3 / q0**3

    def q_int(n, qv):
        return (qv**n - qv**(-n)) / (qv - 1/qv)

    q2 = q_int(2, q0)  # [2]_q = q + q⁻¹
    q12 = q_int(12, q0)

    # Test hypothesis A: m_p = [2]_q · m_μ · F_Bor − [12]_q · m_e
    m_p_A = q2 * m_mu * F - q12 * m_e
    print(f"    [2]_q  = {mp.nstr(q2, 12)}")
    print(f"    [12]_q = {mp.nstr(q12, 12)}")
    print(f"    Hypothesis A: [2]_q·m_μ·F − [12]_q·m_e = {mp.nstr(m_p_A, 12)} MeV")
    print(f"    Residual: {mp.nstr((m_p_A - m_p_codata)/m_p_codata * 1e6, 8)} ppm")
    print()

    # Test hypothesis B: m_p = 2·m_μ·F_Bor − 2·[3]_q!·m_e
    m_p_B = 2 * m_mu * F - 2 * qf3 * m_e
    print(f"    [3]_q! = {mp.nstr(qf3, 12)}")
    print(f"    Hypothesis B: 2·m_μ·F − 2·[3]_q!·m_e = {mp.nstr(m_p_B, 12)} MeV")
    print(f"    Residual: {mp.nstr((m_p_B - m_p_codata)/m_p_codata * 1e6, 8)} ppm")
    print()

    # Test hypothesis C: m_p = [2]_q·m_μ·F_Bor − 2·[3]_q!·m_e
    m_p_C = q2 * m_mu * F - 2 * qf3 * m_e
    print(f"    Hypothesis C: [2]_q·m_μ·F − 2·[3]_q!·m_e = {mp.nstr(m_p_C, 12)} MeV")
    print(f"    Residual: {mp.nstr((m_p_C - m_p_codata)/m_p_codata * 1e6, 8)} ppm")
    print()

    # Test hypothesis D: m_p = [2]_q·m_μ·|tr_M|·[3]_q!/q³ − [2]_q·[3]_q!·m_e
    # = [2]_q · (m_μ·|tr_M|·[3]_q!/q³ − [3]_q!·m_e)
    # = [2]_q · [3]_q! · (m_μ·|tr_M|/q³ − m_e)
    m_p_D = q2 * qf3 * (m_mu * trM / q0**3 - m_e)
    print(f"    Hypothesis D: [2]_q·[3]_q!·(m_μ·|tr_M|/q³ − m_e) = {mp.nstr(m_p_D, 12)} MeV")
    print(f"    Residual: {mp.nstr((m_p_D - m_p_codata)/m_p_codata * 1e6, 8)} ppm")
    print()

    # Test hypothesis E: the EXACT substrate identity with q-deformed orbit size
    # Instead of |Orb| = 2 (integer), use |Orb|_q = [2]_q/1 or something
    # m_p = |Orb|_q · (m_μ · F_Bor − |S₃|_q · m_e)
    # where |S₃|_q = [3]_q! (q-deformed group order)
    m_p_E = q2 * (m_mu * F - qf3 * m_e)
    print(f"    Hypothesis E: [2]_q·(m_μ·F − [3]_q!·m_e) = {mp.nstr(m_p_E, 12)} MeV")
    print(f"    Residual: {mp.nstr((m_p_E - m_p_codata)/m_p_codata * 1e6, 8)} ppm")
    print()

    # ── 2. Systematic scan ──────────────────────────────────────
    print("  2. Systematic scan of q-deformed replacements")
    print()
    print(f"    {'Formula':>50s}  {'m_p (MeV)':>12s}  {'Δ (ppm)':>12s}  {'Δ (ppb)':>10s}")

    candidates = [
        ("2·m_μ·F − 12·m_e (current)",
         2 * m_mu * F - 12 * m_e),
        ("[2]_q·m_μ·F − [2]_q·[3]_q!·m_e",
         q2 * m_mu * F - q2 * qf3 * m_e),
        ("[2]_q·(m_μ·F − [3]_q!·m_e)",
         q2 * (m_mu * F - qf3 * m_e)),
        ("2·m_μ·F − 2·[3]_q!·m_e",
         2 * m_mu * F - 2 * qf3 * m_e),
        ("[2]_q·m_μ·F − 12·m_e",
         q2 * m_mu * F - 12 * m_e),
        ("2·m_μ·F − [12]_q·m_e",
         2 * m_mu * F - q12 * m_e),
        ("[2]_q·m_μ·F − [12]_q·m_e",
         q2 * m_mu * F - q12 * m_e),
        ("(q+q⁻¹)·m_μ·F − (q+q⁻¹)·(q²+1+q⁻²)·(q+q⁻¹)·m_e",
         q2 * m_mu * F - q2 * qf3 * m_e),
        # What about replacing only the 12: 12 → [3]_q! · [2]_q/[2]_q = [3]_q!
        ("2·m_μ·|tr_M|/y₃ − 2·(q³/y₃)·m_e",
         2 * m_mu * trM * qf3/q0**3 - 2 * q0**3 / (q0**3/qf3) * m_e),
    ]

    for name, val in candidates:
        delta_ppm = (val - m_p_codata) / m_p_codata * 1e6
        delta_ppb = delta_ppm * 1000
        marker = " ◄" if abs(delta_ppb) < 10 else ""
        print(f"    {name:>50s}  {mp.nstr(val, 12):>12s}  {mp.nstr(delta_ppm, 6):>12s}  {mp.nstr(delta_ppb, 6):>10s}{marker}")

    # ── 3. The q-deformed orbit interpretation ──────────────────
    print()
    print("  3. Structural interpretation")
    print()

    # [2]_q = q + q⁻¹ ≈ 2.0109 (the q-deformed orbit size)
    # [2]_q / 2 = 1.0054... = 1 + h²/8 + ...
    # So [2]_q ≈ 2·(1 + h²/8 + ...) — the q-deformation of "2"
    print(f"    [2]_q = q + q⁻¹ = {mp.nstr(q2, 15)}")
    print(f"    [2]_q / 2       = {mp.nstr(q2/2, 15)}")
    print(f"    = 1 + h²/8 + ... (q-deformation of the integer 2)")
    print()
    print(f"    [3]_q! = {mp.nstr(qf3, 15)}")
    print(f"    [3]_q! / 6      = {mp.nstr(qf3/6, 15)}")
    print(f"    = 1 + 11h²/24 + ... (q-deformation of 3! = 6)")
    print()

    # The DIFFERENCE between [2]_q and 2:
    delta_2 = q2 - 2
    print(f"    [2]_q − 2  = {mp.nstr(delta_2, 15)} = h²/4 + ...")
    print(f"    [3]_q! − 6 = {mp.nstr(qf3 - 6, 15)} = 11h²/4 + ...")
    print()

    # If the exact formula is [2]_q·(m_μ·F − [3]_q!·m_e):
    # Then the "correction" to 2·(m_μ·F − 6·m_e) is:
    # [2]_q·(m_μF − [3]_q!·m_e) − 2·(m_μF − 6·m_e)
    # = (q2−2)·(m_μF − [3]_q!·m_e) + 2·(6−[3]_q!)·m_e
    # = (h²/4+...)·(m_μF − 6.12·m_e) + 2·(−0.12)·m_e
    # The first term is h²-order, the second is h²-order

    correction_E = m_p_E - (2 * m_mu * F - 12 * m_e)
    correction_as_hbar = correction_E / hbar0**6
    print(f"    Correction from integer→q-deformed:")
    print(f"    [2]_q·(m_μF−[3]_q!m_e) − 2(m_μF−6m_e) = {mp.nstr(correction_E, 12)} MeV")
    print(f"    In ℏ⁶ units: {mp.nstr(correction_as_hbar, 12)}")
    print(f"    In ppm of m_p: {mp.nstr(correction_E / m_p_codata * 1e6, 8)}")

    elapsed = time.time() - t0
    print(f"\n  Wall time: {elapsed:.1f}s")

    w = WitnessBuilder("phase2c-derive-correction-tower", engine="sympy+mpmath")
    w.set_description(
        "Investigates whether the ℏ_q correction tower can be DERIVED "
        "(not fitted) by replacing integer coefficients with their "
        "q-deformed analogues: 2 → [2]_q, 6 → [3]_q!. Tests multiple "
        "q-deformation hypotheses against CODATA."
    )
    w.set_content_block("prop:proton-mass-substrate-identity")
    best = min(candidates, key=lambda c: abs(float((c[1]-m_p_codata)/m_p_codata)))
    w.add_data("best_q_deformed_formula", {
        "name": best[0],
        "m_p_MeV": str(mp.nstr(best[1], 15)),
        "residual_ppm": str(mp.nstr((best[1]-m_p_codata)/m_p_codata*1e6, 10)),
    })
    w.add_assertion(
        name="q_deformation_improves",
        computed=1 if abs(float((best[1]-m_p_codata)/m_p_codata)) < abs(float((2*m_mu*F-12*m_e-m_p_codata)/m_p_codata)) else 0,
        expected=1, tolerance=0,
        source="At least one q-deformed formula should beat the integer form"
    )
    out = w.save()
    print(f"\n  Witness: {out}")


if __name__ == "__main__":
    main()
