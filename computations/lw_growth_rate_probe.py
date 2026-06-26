#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic q-rational selection-rule sums evaluated
# numerically at q0; falsifiability PROBE (audit-only witness), not production
# (compute-author §1.3 — no parameter is fit to experiment).
"""Probe: characterise the super-exponential growth law of a_D^(n) = lw(n−1).

Sibling PR #2795 settled that a_D^(n) = lw(n−1) is super-exponential and attributed
it to the √-branch of the color cubic: X^(n) ~ (z−z_k)^{1/2−n}, whose period
coefficient is the falling factorial (1/2)_n with consecutive-ratio (n−1/2).

#2808 measured the lw ratios at q0 to n=8 (1.89 → 3.10). Those are *smaller* than
the bare (n−1/2) = 3.5, 4.5, … — so the √-branch is the qualitative magnitude
mechanism, but the q0-evaluated period ratio is modulated (the dim_q weights at the
substrate q0). This probe extends lw to n=13 and quantifies the actual growth law:
ratio vs n, against three reference models — (n−1/2) [verdict], the SL₂ geometric
cap λ₊ [depth-2 fit], and a linear-in-n ratio (the factorial-class signature). It
records, it does not close (the exact a_D⇔lw⇔q-Bessel correspondence is open, z2bn).

Output: lw-growth-rate-probe.witness.json (audit-only).
"""
from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE / "phase5"))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _precision import COMPUTE_DPS  # noqa: E402
from q_parameter import Q_50_DIGIT_STR as Q0  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from phase5_n8_dim_q_table import dim_q_via_quantum_hooks, partitions_of  # noqa: E402


def lw(c: int, q: sp.Symbol) -> sp.Expr:
    """lw(c) = (1/(c+1)) Σ_{λ⊢c+1} dim_q V_λ (canonical q-hook dim_q)."""
    n = c + 1
    s = sum((dim_q_via_quantum_hooks(lam, q) for lam in partitions_of(n)), sp.S.Zero)
    return sp.cancel(sp.together(s / n))


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q = sp.Symbol("q", positive=True)
    q0 = sp.Float(Q0, 50)
    q0m = mp.mpf(Q0)

    C_MAX = 12  # a_D up to n = C_MAX + 1 = 13
    print(f"computing lw(c), c=1..{C_MAX} (a_D^(n), n=2..{C_MAX + 1}) at q0 …")
    aD = {}
    for c in range(1, C_MAX + 1):
        val = mp.mpf(str(sp.N(lw(c, q).subs(q, q0), 50)))
        aD[c + 1] = val  # a_D^(n) = lw(n−1), n = c+1
        print(f"  n={c + 1:>2}  a_D=lw({c}) = {mp.nstr(val, 12)}")

    # SL₂ geometric cap λ₊ from the depth-2 anchored τ (n≤4 fit).
    tau = (aD[2] + aD[4]) / aD[3]
    lam_plus = (tau + mp.sqrt(tau * tau - 4)) / 2

    rows = []
    ratios = []
    for n in range(3, C_MAX + 2):
        r = aD[n] / aD[n - 1]
        ratios.append((n, r))
        rows.append({
            "n": n,
            "aD_lw": mp.nstr(aD[n], 12),
            "ratio": mp.nstr(r, 8),
            "n_minus_half": mp.nstr(mp.mpf(n) - mp.mpf("0.5"), 6),  # verdict √-branch
            "lambda_plus": mp.nstr(lam_plus, 6),                     # SL₂ geometric cap
        })

    # Empirical growth characterisation (no experimental fit — pure math rates):
    #  (i) does the ratio keep climbing (super-exp) past the SL₂ cap?
    top_ratio = ratios[-1][1]
    super_exp = top_ratio > lam_plus
    #  (ii) least-squares slope of ratio-vs-n (a positive slope ⇒ factorial-class,
    #       the ratio not saturating; the magnitude of the slope vs 1.0 says how it
    #       compares to the bare (n−1/2) slope of exactly 1).
    ns = mp.matrix([r[0] for r in ratios])
    rs = mp.matrix([r[1] for r in ratios])
    k = len(ratios)
    mean_n = mp.fsum(ns) / k
    mean_r = mp.fsum(rs) / k
    num = mp.fsum([(ns[i] - mean_n) * (rs[i] - mean_r) for i in range(k)])
    den = mp.fsum([(ns[i] - mean_n) ** 2 for i in range(k)])
    slope = num / den  # d(ratio)/dn
    intercept = mean_r - slope * mean_n

    w = WitnessBuilder("lw-growth-rate-probe", engine="python+sympy+mpmath")
    w.set_audit_only("docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md")
    w.add_parameter("q_0", Q0)
    w.add_data("aD_eq_lw", "a_D^(n) = lw(n−1) = (1/n) Σ_{λ⊢n} dim_q V_λ (canonical q-hook)")
    w.add_data("sl2_lambda_plus", mp.nstr(lam_plus, 12))
    w.add_data("ratio_table", rows)
    w.add_data("ratio_vs_n_linear_fit", {
        "slope": mp.nstr(slope, 8),
        "intercept": mp.nstr(intercept, 8),
        "interpretation": "ratio(n) ≈ slope·n + intercept. slope > 0 ⇒ ratio does NOT "
                          "saturate (super-exp, factorial-class). The bare √-branch "
                          "(n−1/2) has slope exactly 1; the measured slope is the q0 "
                          "modulation of that mechanism.",
    })
    w.add_data("vs_verdict_n_minus_half",
               "the q0-evaluated lw ratio is SMALLER than the bare (n−1/2) and climbs "
               "with slope ≈ %s (not 1): the √-branch sets the super-exp CLASS, the "
               "dim_q(q0) weights set the RATE — recorded, correspondence open (z2bn)."
               % mp.nstr(slope, 4))

    # Assertion 1: lw is super-exponential — ratio exceeds the SL₂ geometric cap at the top.
    w.add_assertion(
        "lw_ratio_exceeds_sl2_cap_at_top", computed=1 if super_exp else 0,
        expected=1, tolerance=0,
        source=f"ratio(n={C_MAX + 1}) = {mp.nstr(top_ratio, 8)} > λ₊ = "
               f"{mp.nstr(lam_plus, 8)}.")
    # Assertion 2: the ratio does NOT saturate — positive linear slope ⇒ factorial-class
    # (a geometric/C-finite sequence would have slope 0, a flat ratio).
    w.add_assertion(
        "lw_ratio_nonsaturating_slope_positive", computed=1 if slope > 0 else 0,
        expected=1, tolerance=0,
        source=f"d(ratio)/dn ≈ {mp.nstr(slope, 6)} > 0 over n=3..{C_MAX + 1} "
               f"(geometric ⇒ 0; bare (n−1/2) ⇒ 1).")
    out = w.save()

    print("=" * 80)
    print(" lw(n−1) growth law at q0 — PROBE (super-exp class, q0-modulated rate)")
    print("=" * 80)
    print(f"  SL₂ geometric cap λ₊ = {mp.nstr(lam_plus, 10)}")
    print(f"  {'n':>2} {'a_D=lw(n−1)':>16} {'ratio':>10} {'(n−1/2)':>9} {'λ₊':>8}")
    for r in rows:
        print(f"  {r['n']:>2} {r['aD_lw']:>16} {r['ratio']:>10} "
              f"{r['n_minus_half']:>9} {r['lambda_plus']:>8}")
    print(f"  ratio-vs-n linear slope = {mp.nstr(slope, 6)}  (geometric→0, √-branch→1)")
    print(f"  super-exp (ratio > λ₊ at top): {super_exp}")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
