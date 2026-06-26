#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic q-rational selection-rule sums + mpmath
# evaluation at q0; falsifiability PROBE (audit-only witness), not a production
# derivation (compute-author §1.3). NO free parameter is tuned to lw.
"""Probe: is the binding period a_D^(n)=lw(n−1) a Bessel-½ FALLING FACTORIAL?

PR #2795 settled the fork: a_D^(n)=lw(n−1) is super-exponential (the √-branch
of the colour cubic gives X^(n) ~ (z−z_k)^{1/2−n}, the falling factorial
(1/2)_n^fall), NOT the depth-2 SL₂ germ. The Hahn–Exton q-Bessel order is ν=1/2
(`BindingQBesselKernel`). The natural follow-up bridge hypothesis is:

    BRIDGE:  lw(n−1) =? scale · |∏_{k=0}^{n-1} [1/2 − k]_q|   (q-Bessel-½ falling factorial)

i.e. lw is the q-deformation of the classical Bessel-½ period, up to one overall
(conventional) scale. This probe TESTS that, decisively, by the constant-ratio
criterion: if `lw / |qfall½|` is constant in n, the bridge closes.

RESULT (this probe): it is NOT constant — the ratio decays monotonically
(≈4.01 → 0.028 over n=2..10, successive ratios ≈0.89 → 0.38, themselves
decreasing). Neither the classical `∏(1/2−k)` nor the q-symmetric `∏[1/2−k]_q`
rescales onto lw. **Scope-(a)**: the Bessel-½ FALLING-FACTORIAL form, alone, does
not reproduce lw — it is NOT a structural exclusion of q-Bessel (the order ν=1/2
is correct and the growth class matches).

STRUCTURAL REASON (decisive, not numerical): `lw(n−1)=(1/n)Σ_{λ⊢n} dim_q` is a
SUM over p(n) partitions; a Bessel-½ falling factorial is a SINGLE product. A sum
of p(n) terms cannot equal one product. Per `prop:sw-period-residue-sum` the
residues are per-block Wedderburn weights, SUMMED — so the Bessel-½ falling
factorial is the PER-BLOCK (per-branch-point) period, and lw is the residue SUM
over blocks. This NARROWS the z2bn kernel target: R(q,x) generates the per-block
period; lw aggregates over the Wedderburn decomposition. (Prunes the
"lw = single falling factorial" shortcut; keeps q-Bessel-per-block alive.)

Output: sw-period-bessel-half-falling-factorial.witness.json (audit-only).
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
    """Selection rule lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q V_λ (canonical q-hook)."""
    n = c + 1
    s = sum((dim_q_via_quantum_hooks(lam, q) for lam in partitions_of(n)), sp.S.Zero)
    return sp.cancel(sp.together(s / n))


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q = sp.Symbol("q", positive=True)
    q0 = sp.Float(Q0, 50)
    q0m = mp.mpf(Q0)

    def num(e: sp.Expr) -> mp.mpf:
        return mp.mpf(str(sp.N(e.subs(q, q0), 50)))

    def qnum(x) -> mp.mpf:
        """Symmetric q-number [x]_q = (q^x − q^{−x})/(q − q^{−1})."""
        return (q0m ** x - q0m ** (-x)) / (q0m - 1 / q0m)

    def qfall_half(n: int) -> mp.mpf:
        r = mp.mpf(1)
        for k in range(n):
            r *= qnum(mp.mpf("0.5") - k)
        return r

    def cfall_half(n: int) -> mp.mpf:
        r = mp.mpf(1)
        for k in range(n):
            r *= mp.mpf("0.5") - k
        return r

    N_MAX = 10
    rows = []
    prev_ratio = None
    succ_ratios = []
    for n in range(2, N_MAX + 1):
        L = num(lw(n - 1, q))
        qf = abs(qfall_half(n))
        cf = abs(cfall_half(n))
        ratio = L / qf
        sr = (ratio / prev_ratio) if prev_ratio is not None else None
        if sr is not None:
            succ_ratios.append(sr)
        prev_ratio = ratio
        rows.append({
            "n": n,
            "lw": mp.nstr(L, 12),
            "qfall_half": mp.nstr(qf, 12),
            "lw_over_qfall": mp.nstr(ratio, 10),
            "succ_ratio": (mp.nstr(sr, 6) if sr is not None else None),
            "lw_over_cfall": mp.nstr(L / cf, 8),
        })

    # Constant-ratio criterion: if lw = scale·|qfall½| then lw/|qfall½| is constant
    # ⇒ all successive ratios = 1. Spread of successive ratios from 1 measures the
    # failure. (They run ≈0.89 → 0.38 — nowhere near constant.)
    max_dev = max(abs(sr - 1) for sr in succ_ratios)
    monotone_decay = all(
        succ_ratios[i] > succ_ratios[i + 1] for i in range(len(succ_ratios) - 1)
    )

    w = WitnessBuilder(
        "sw-period-bessel-half-falling-factorial", engine="python+sympy+mpmath"
    )
    w.set_audit_only("docs/audits/2026-06-26-bessel-half-falling-factorial-bridge-pruned.md")
    w.add_parameter("q_0", Q0)
    w.add_data("bridge_hypothesis",
               "lw(n−1) =? scale · |∏_{k=0}^{n-1} [1/2−k]_q|  (q-Bessel-½ falling factorial)")
    w.add_data("constant_ratio_criterion",
               "lw = scale·|qfall½|  ⟺  lw/|qfall½| constant  ⟺  all succ_ratio = 1")
    w.add_data("table_n2_to_n10", rows)
    w.add_data("max_succ_ratio_deviation_from_1", mp.nstr(max_dev, 6))
    w.add_data("succ_ratio_monotone_decreasing", monotone_decay)
    w.add_data("scope_a_finding",
               "Bessel-½ FALLING-FACTORIAL form alone does not reproduce lw "
               "(ratio non-constant, monotone-decaying). NOT a structural exclusion "
               "of q-Bessel: order ν=1/2 correct, growth class matches.")
    w.add_data("structural_reason",
               "lw(n−1)=(1/n)Σ_{λ⊢n} dim_q is a SUM over p(n) partitions; a Bessel-½ "
               "falling factorial is a SINGLE product. Per prop:sw-period-residue-sum "
               "(residues = per-block Wedderburn weights, summed), the falling factorial "
               "is the PER-BLOCK period; lw is the residue SUM over blocks.")
    w.add_data("z2bn_narrowing",
               "Kernel target R(q,x) generates the PER-BLOCK period (single branch "
               "point); lw aggregates over the Wedderburn decomposition. Prunes the "
               "'lw = single falling factorial' shortcut; q-Bessel-per-block stays open.")

    # Assertion: the bridge does NOT close — lw/|qfall½| is non-constant
    # (the maximal successive-ratio deviation from 1 is far above any tolerance).
    w.add_assertion(
        "bessel_half_falling_factorial_bridge_does_not_close",
        computed=1 if max_dev > mp.mpf("0.01") else 0, expected=1, tolerance=0,
        source=f"max |succ_ratio − 1| = {mp.nstr(max_dev, 6)} ≫ 0.01 over n=2..{N_MAX} "
               f"⇒ lw ≠ scale·|qfall½| (no rescaling closes the falling-factorial bridge).",
    )
    # Assertion: monotone decay (the falling factorial systematically OUTGROWS lw —
    # consistent with lw being a tempered residue-SUM, not a single product).
    w.add_assertion(
        "qfall_half_outgrows_lw_monotonically",
        computed=1 if monotone_decay else 0, expected=1, tolerance=0,
        source="lw/|qfall½| successive ratios strictly decreasing ⇒ the single-product "
               "falling factorial outgrows the partition-sum lw at every step.",
    )
    out = w.save()

    print("=" * 80)
    print(" a_D^(n)=lw(n−1) vs Bessel-½ falling factorial ∏[1/2−k]_q — BRIDGE PROBE")
    print("=" * 80)
    print(f"  {'n':>2} {'lw(n-1)':>14} {'|qfall½|':>14} {'lw/|qfall½|':>14} "
          f"{'succ.ratio':>11} {'lw/|cfall½|':>13}")
    for r in rows:
        print(f"  {r['n']:>2} {r['lw']:>14} {r['qfall_half']:>14} "
              f"{r['lw_over_qfall']:>14} {str(r['succ_ratio']):>11} {r['lw_over_cfall']:>13}")
    print(f"\n  max |succ_ratio − 1| = {mp.nstr(max_dev, 6)}  (≫ 0.01 ⇒ bridge does NOT close)")
    print(f"  succ_ratio monotone-decreasing = {monotone_decay}  (falling factorial outgrows lw)")
    print("  VERDICT (scope-a): lw ≠ scale·Bessel-½ falling factorial. lw is the residue")
    print("  SUM over Wedderburn blocks; the falling factorial is the PER-BLOCK period.")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
