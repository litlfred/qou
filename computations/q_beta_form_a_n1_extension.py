#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic Taylor expansion + 50-dps
# numerical evaluation; the symbolic content IS the deliverable.
"""Form A symbolic extension to depth $N = 1$ in the brane tower.

The single-wrap symbolic Q_β prediction
([prop:neutron-qvalue-symbolic](#prop:neutron-qvalue-symbolic)) is

    Q_β^A,N=0  =  m_e · |Δ(net)| · E_0_N=0
              =  m_e · h(2-h)/2 · 1/(q(q-1))

where E_0_N=0 = m_e / (q(q-1)) is the **single-tick** Planck-tick
approximation to the brane-tower energy scale. This script derives
the **N=1 correction** to E_0 from the q-Pochhammer expansion of
Φ_q at depth 1, gives the symbolic closed form of E_0_N=1, and
numerically evaluates the Q_β prediction at 50 dps.

**Strategy.** From `c_k_beta_decay_witness.py` on this branch:
the per-N residual ceiling is

    |R_N| ≤ C(K) · e^{-c(K) · N}
         = ℏ_q^{2(N+1)} / (1 - ℏ_q²)

with c(K) = -2 ln ℏ_q ≈ 4.624, C(K) ≈ 0.00991.

At N=0 the observed residual is 0.168% (1.31 keV), well inside the
ceiling 0.99%. At N=1 the ceiling is 97 ppm — a 100× tightening.

**Symbolic form at N=1.** The single-tick E_0 is the leading term
of the geometric series

    E_0_full  =  E_0_N=0 · Σ_{k=0}^∞ ℏ_q^{2k}
              =  E_0_N=0 / (1 - ℏ_q²)

Truncating at N gives:

    E_0_N  =  E_0_N=0 · Σ_{k=0}^{N} ℏ_q^{2k}
           =  E_0_N=0 · (1 - ℏ_q^{2(N+1)}) / (1 - ℏ_q²)

For N=1:
    E_0_N=1  =  E_0_N=0 · (1 + ℏ_q²)
           =  m_e / (q(q-1)) · (1 + ((q-1)/q)²)

Substituting ℏ_q = (q-1)/q:
    1 + ℏ_q²  =  1 + (q-1)²/q²
              =  (q² + (q-1)²) / q²
              =  (2q² - 2q + 1) / q²

So:
    E_0_N=1  =  m_e · (2q² - 2q + 1) / (q³ · (q - 1))

And:
    Q_β^A,N=1  =  m_e · h(2-h)/2 · (2q² - 2q + 1) / (q³ · (q - 1))

Substituting h = q - q⁻¹ = (q² - 1)/q:
    h(2-h)/2  =  ((q² - 1)/q) · (2 - (q² - 1)/q) / 2
             =  ((q² - 1)/q) · ((2q - q² + 1)/q) / 2
             =  ((q² - 1) · (-(q² - 2q - 1))) / (2q²)
             =  -(q² - 1)(q² - 2q - 1) / (2q²)

Taking |·|:
    |h(2-h)/2|  =  (q + 1)(q - 1) · |q² - 2q - 1| / (2q²)

Combining all terms:

    Q_β^A,N=1  =  m_e · (q+1)(q-1)·|q²-2q-1| / (2q²)
                       · (2q²-2q+1) / (q³(q-1))

              =  m_e · (q+1)·|q²-2q-1|·(2q²-2q+1) / (2 q⁵)

This is the **N=1 symbolic closed form** for Q_β.

Class C (diagnostic / prediction). Pure substrate-derived
(CAL-1 + CAL-2 only); no CAL-3 input.

Output: `q-beta-form-a-n1-extension.witness.json`.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_MP  # noqa: E402 — experimental/proton pin, 50 dps
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    w = WitnessBuilder("q-beta-form-a-n1-extension", engine="mpmath")

    # ── q_0: experimental/proton pin per the 2026-08-07 owner directive ──
    # This producer's manifest entry is physical_proton.  It previously read
    # q-pinning-50-digit.witness.json directly; that witness is MUON-anchored,
    # so it computed at the ideal pin while declaring the experimental one.
    # NOTE the comment this replaces said "Load CAL-2 q_0" — CAL-2 names the
    # CALIBRATION, not the pin.  AGENTS.md: the directive "is about which
    # numerical evaluation code defaults to, not about redefining the 3-CAL
    # triple".  Q_MP is the proton pin at the same 50 dps.
    q_0 = Q_MP

    m_e = M_E_MEV
    q_codata = mp.mpf(str(Q_BETA_MEV))

    # ── Symbolic closed form ───────────────────────────────────
    q = sp.Symbol("q", positive=True)
    me = sp.Symbol("m_e", positive=True)

    h = q - 1/q
    delta_net = h * (2 - h) / 2
    delta_net_abs = sp.Abs(delta_net)

    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0_N0_sym = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    hbar_q_sym = (q - 1) / q
    factor_N1 = 1 + hbar_q_sym**2  # = (2q² - 2q + 1) / q²
    E0_N1_sym = E0_N0_sym * factor_N1

    Q_beta_N0_sym = delta_net_abs * E0_N0_sym
    Q_beta_N1_sym = delta_net_abs * E0_N1_sym

    # Simplify
    Q_beta_N0_simp = sp.simplify(Q_beta_N0_sym)
    Q_beta_N1_simp = sp.simplify(Q_beta_N1_sym)
    factor_N1_simp = sp.simplify(factor_N1)

    print("=" * 78)
    print("Q_β FORM A: SYMBOLIC EXTENSION TO N=1 BRANE-TOWER DEPTH")
    print("=" * 78)
    print()
    print(f"  E_0_N=0 (single tick):")
    print(f"    {E0_N0_sym}")
    print()
    print(f"  N=1 multiplicative correction factor (1 + ℏ_q²):")
    print(f"    {factor_N1_simp}")
    print()
    print(f"  E_0_N=1 = E_0_N=0 · (1 + ℏ_q²):")
    print(f"    {sp.simplify(E0_N1_sym)}")
    print()
    print(f"  Q_β^A,N=0 = m_e · |Δ(net)| · E_0_N=0:")
    print(f"    {Q_beta_N0_simp}")
    print()
    print(f"  Q_β^A,N=1 = m_e · |Δ(net)| · E_0_N=1:")
    print(f"    {Q_beta_N1_simp}")
    print()

    # ── Numerical evaluation at q_0 (50 dps) ───────────────────
    # Note: sp.subs returns a sympy expression; use sp.N to evaluate
    # at 50 dps then cast to mpf.
    def eval_at_q0(expr):
        val = sp.N(expr.subs({q: sp.Rational(str(q_0)), me: sp.Rational(str(m_e))}), 50)
        return mp.mpf(str(val))

    Q_N0 = eval_at_q0(Q_beta_N0_sym)
    Q_N1 = eval_at_q0(Q_beta_N1_sym)
    E0_N0_num = eval_at_q0(E0_N0_sym)
    E0_N1_num = eval_at_q0(E0_N1_sym)
    factor_N1_num = eval_at_q0(factor_N1)
    hbar_q_num = (q_0 - 1) / q_0

    delta_N0_kev = (Q_N0 - q_codata) * 1000
    delta_N1_kev = (Q_N1 - q_codata) * 1000
    delta_N0_pct = (Q_N0 - q_codata) / q_codata * 100
    delta_N1_pct = (Q_N1 - q_codata) / q_codata * 100
    delta_N1_ppm = (Q_N1 - q_codata) / q_codata * 1e6

    # Ceiling at N=1
    ceiling_N1 = hbar_q_num**4 / (1 - hbar_q_num**2)

    print(f"  Numerical values at q_0 = {mp.nstr(q_0, 14)}:")
    print(f"    ℏ_q                = {mp.nstr(hbar_q_num, 10)}")
    print(f"    E_0_N=0 (MeV)      = {mp.nstr(E0_N0_num, 10)}")
    print(f"    E_0_N=1 (MeV)      = {mp.nstr(E0_N1_num, 10)}")
    print(f"    factor (1 + ℏ_q²)  = {mp.nstr(factor_N1_num, 10)}")
    print()
    print(f"    Q_β^A,N=0 (MeV)    = {mp.nstr(Q_N0, 10)}")
    print(f"    Q_β^A,N=1 (MeV)    = {mp.nstr(Q_N1, 10)}")
    print(f"    Q_β CODATA (MeV)   = {q_codata}")
    print()
    print(f"    N=0 residual: {float(delta_N0_kev):+.4f} keV  ({float(delta_N0_pct):+.4f}%)")
    print(f"    N=1 residual: {float(delta_N1_kev):+.4f} keV  ({float(delta_N1_pct):+.4f}% = "
          f"{float(delta_N1_ppm):+.2f} ppm)")
    print()
    print(f"    Per-braid-mass-tower ceiling at N=1: {float(ceiling_N1*100):+.6f}%")
    print(f"    (= ℏ_q^4 / (1 - ℏ_q²) = {mp.nstr(ceiling_N1, 6)})")
    print()
    print(f"    {'✓' if abs(delta_N1_pct) < 100*ceiling_N1 else '✗'} N=1 residual inside per-braid bound")

    # Improvement factor
    if abs(delta_N1_pct) < abs(delta_N0_pct):
        improvement = float(abs(delta_N0_pct) / abs(delta_N1_pct))
        print(f"    Improvement N=0 → N=1: {improvement:.2f}× tighter")
    else:
        excess = float(abs(delta_N1_pct) / abs(delta_N0_pct))
        print(f"    N=1 WORSE than N=0 by {excess:.2f}× — sign of the N=1 correction")
        print(f"    flips the residual direction (predicted by Form A's geometric")
        print(f"    expansion is positive at N=1)")

    w.set_content_block("prop:neutron-qvalue-symbolic")
    w.set_description(
        "Symbolic extension of Form A Q_β to N=1 brane-tower depth. "
        "Derives the N=1 correction factor (1 + ℏ_q²) = (2q²-2q+1)/q² "
        "from the geometric series of E_0_full = E_0_N=0/(1-ℏ_q²). "
        "Closed form: Q_β^A,N=1 = m_e · (q+1) · |q²-2q-1| · (2q²-2q+1) "
        "/ (2 q⁵). Substrate-only (CAL-1 m_e + CAL-2 q_0); no CAL-3 "
        "input. Comparator-only against CODATA Q_β. Class C "
        "(diagnostic / prediction)."
    )
    w.add_parameter("q_0_50dps", str(q_0))
    w.add_parameter("m_e_MeV", str(m_e))
    w.add_parameter("Q_beta_codata_MeV", str(q_codata))
    w.add_data("Q_beta_N0_symbolic", str(Q_beta_N0_simp))
    w.add_data("Q_beta_N1_symbolic", str(Q_beta_N1_simp))
    # Tower-summed full form (N → ∞): E_0^full = E_0_N=0 / (1 - ℏ_q²)
    E0_full_num = E0_N0_num / (1 - hbar_q_num ** 2)
    Q_full_num = abs(eval_at_q0(delta_net)) * E0_full_num
    # CODATA-calibrated cross-check: E_0^(cal) = Q_β / |Δ(net)|
    delta_net_num = eval_at_q0(delta_net)
    E0_cal_num = q_codata / abs(delta_net_num)
    # Bounded symmetric q-dilogarithm closure candidate
    # (conj:alpha-k-categorical-closure):
    #   E_0^{full,Li_2^q} = E_0^{(N=0)} · (1 + (-Li_2^q(-ℏ_q²)))
    # Centralized helper from derived_masses (avoids duplication).
    from derived_masses import li2q_symmetric  # noqa: E402
    x = hbar_q_num ** 2
    li2q_minus_x = li2q_symmetric(-x, q_0)
    E0_full_li2q_num = E0_N0_num * (1 + (-li2q_minus_x))

    w.add_data("E0_N0_MeV_50dps", str(E0_N0_num))
    w.add_data("E0_N1_MeV_50dps", str(E0_N1_num))
    w.add_data("E0_full_MeV_50dps", str(E0_full_num))
    w.add_data("E0_full_li2q_MeV_50dps", str(E0_full_li2q_num))
    w.add_data("E0_calibrated_MeV_50dps", str(E0_cal_num))
    w.add_data("E0_full_vs_calibrated_pct", float((E0_full_num - E0_cal_num) / E0_cal_num * 100))
    w.add_data("E0_full_li2q_vs_calibrated_pct", float((E0_full_li2q_num - E0_cal_num) / E0_cal_num * 100))
    w.add_data("E0_N0_vs_calibrated_pct", float((E0_N0_num - E0_cal_num) / E0_cal_num * 100))
    w.add_data("Q_beta_N0_MeV", str(Q_N0))
    w.add_data("Q_beta_N1_MeV", str(Q_N1))
    w.add_data("Q_beta_full_MeV", str(Q_full_num))
    w.add_data("N0_residual_keV", float(delta_N0_kev))
    w.add_data("N0_residual_pct", float(delta_N0_pct))
    w.add_data("N1_residual_keV", float(delta_N1_kev))
    w.add_data("N1_residual_pct", float(delta_N1_pct))
    w.add_data("N1_residual_ppm", float(delta_N1_ppm))
    w.add_data("per_braid_ceiling_N1_pct", float(ceiling_N1 * 100))
    w.add_data("hbar_q_50dps", str(hbar_q_num))

    # Assertions encode the SUBSTANTIVE NEGATIVE FINDING: the
    # geometric-series N=1 lift overshoots the per-braid bound,
    # confirming that the naive geometric expansion is NOT the
    # correct lift formula. This matches the handoff's "5 naive
    # N=1 lifts all failed" pattern (commit e1b005b2 of PR #637).
    w.add_assertion(
        "geometric_N1_lift_overshoots_per_braid_ceiling",
        computed=(abs(delta_N1_pct) / 100 > float(ceiling_N1)),
        expected=True,
    )
    w.add_assertion(
        "factor_N1_equals_2q_squared_minus_2q_plus_1_over_q_squared",
        computed=factor_N1_num,
        expected=(2*q_0**2 - 2*q_0 + 1) / q_0**2,
        tolerance=1e-40,
    )
    w.add_assertion(
        "geometric_N1_makes_residual_worse_than_N0",
        computed=(abs(delta_N1_pct) > abs(delta_N0_pct)),
        expected=True,
    )
    out = w.save()
    print(f"\n  Wrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
