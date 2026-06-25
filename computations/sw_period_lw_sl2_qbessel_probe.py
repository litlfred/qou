#!/usr/bin/env python3
# polynomial_q_not_applicable: symbolic q-rational selection-rule sums + mpmath
# evaluation at q0; this is a falsifiability PROBE (audit-only witness), not a
# production derivation (compute-author §1.3).
"""Probe: does the binding period a_D^(n) = lw(n−1) (#1765) follow the depth-2 SL₂
recurrence, or a super-exponential q-difference (q-Bessel) kernel?

Reproduces, with the CANONICAL q-hook dim_q (reusing the lw of
`binding_selection_rule_tau_closure.py`), the structural fork settled in PR #2795:

  Layer 1 (depth-2 SL₂, `prop:sl2-prolongation-recurrence`):
      a_{n+2} = τ·a_{n+1} − a_n,   τ = (a²+a⁴)/a³   — GEOMETRIC (ratio → λ₊).
  Layer 2 (#1765, the true global period):
      a_D^(n) = lw(n−1) = (1/n)·Σ_{λ⊢n} dim_q V_λ   — measured here for n = 2..8.

The probe extends lw past the three τ-anchors (c = 1,2,3) to c = 1..7 and asks:
does the depth-2 SL₂ extrapolation (seeded on the anchors) keep tracking the true
lw, or diverge? Per PR #2795 it diverges at n = 6 (SL₂ ratio saturates at λ₊ ≈ 2.18
while the lw ratio grows without bound — the √-branch falling-factorial (1/2)_n).

It also records the Hahn–Exton q-Bessel contiguity coefficients
(`QOU.Mass.BindingQBesselKernel` / `QBesselContiguityRecurrence`, the Lean-formalized
Layer-2 kernel) at the substrate q0, to expose HOW the q-Bessel object relates to the
growing period (the coefficients vs the partial sums) — an honest correspondence
check, NOT a fit (compute-author §1.3; no free parameter is tuned to the lw values).

Output: sw-period-lw-sl2-qbessel-probe.witness.json (audit-only).
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
    """Per-component selection rule lw(c) = (1/(c+1))·Σ_{λ⊢c+1} dim_q V_λ,
    via the CANONICAL q-hook quantum dimension (identical to
    `binding_selection_rule_tau_closure.lw`)."""
    n = c + 1
    s = sum((dim_q_via_quantum_hooks(lam, q) for lam in partitions_of(n)), sp.S.Zero)
    return sp.cancel(sp.together(s / n))


def qbessel_ratio(q: mp.mpf, a: mp.mpf, k: int) -> mp.mpf:
    """Hahn–Exton q-Bessel coefficient ratio r_k = −q^k / [(1−q^{k+1})(1−a q^k)]
    (the Lean `QOU.QBeta.qbesselRatio`; `QBesselContiguityRecurrence`)."""
    return -(q ** k) / ((1 - q ** (k + 1)) * (1 - a * q ** k))


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q = sp.Symbol("q", positive=True)
    q0 = sp.Float(Q0, 50)
    q0m = mp.mpf(Q0)

    def num(e: sp.Expr) -> mp.mpf:
        # decimal-string round-trip (compute-author §1.1) — no float() on the path.
        return mp.mpf(str(sp.N(e.subs(q, q0), 50)))

    # ---- The true period a_D^(n) = lw(n−1), n = 2..8 (c = 1..7) ---------------
    C_MAX = 7
    lw_sym = {c: sp.simplify(lw(c, q)) for c in range(1, C_MAX + 1)}
    # a_D index n ↔ lw(n−1): n = c + 1.
    true_aD = {c + 1: num(lw_sym[c]) for c in range(1, C_MAX + 1)}  # n = 2..8

    # ---- Layer 1: depth-2 SL₂ extrapolation, seeded on the τ-anchors ----------
    # τ from the three anchors a²=lw1, a³=lw2, a⁴=lw3 (the n≤4 effective fit).
    a2, a3, a4 = true_aD[2], true_aD[3], true_aD[4]
    tau = (a2 + a4) / a3
    sl2 = {2: a2, 3: a3}
    for n in range(4, C_MAX + 2):  # generate a⁴..a⁸ from the recurrence
        sl2[n] = tau * sl2[n - 1] - sl2[n - 2]

    # Residual of the SL₂ extrapolation vs the true lw, and growth ratios.
    rows = []
    first_div_n = None
    for n in range(2, C_MAX + 2):
        t = true_aD[n]
        s = sl2[n]
        rel = abs(s - t) / abs(t)
        true_ratio = (true_aD[n] / true_aD[n - 1]) if n > 2 else None
        sl2_ratio = (sl2[n] / sl2[n - 1]) if n > 2 else None
        rows.append({
            "n": n,
            "true_aD_lw": mp.nstr(t, 12),
            "sl2_extrap": mp.nstr(s, 12),
            "rel_resid": mp.nstr(rel, 4),
            "true_ratio": (mp.nstr(true_ratio, 6) if true_ratio is not None else None),
            "sl2_ratio": (mp.nstr(sl2_ratio, 6) if sl2_ratio is not None else None),
        })
        # First n where SL₂ visibly departs from lw (rel > 1e-3).
        if first_div_n is None and n >= 4 and rel > mp.mpf("1e-3"):
            first_div_n = n

    # SL₂ asymptotic ratio = the larger root λ₊ of x² − τx + 1 (det = 1).
    lam_plus = (tau + mp.sqrt(tau * tau - 4)) / 2

    # ---- Layer 2: Hahn–Exton q-Bessel coefficients at q0 (correspondence) -----
    # NOT a fit: a = q0^{ν+1} with ν = 1/2 (the √-branch order from PR #2795,
    # X^(n) ~ (z−z_k)^{1/2−n}); we only RECORD the coefficient behaviour, no
    # parameter is tuned to the lw values (compute-author §1.3).
    nu = mp.mpf("0.5")
    a_param = q0m ** (nu + 1)
    c_qb = [mp.mpf(1)]
    for k in range(0, C_MAX):
        c_qb.append(c_qb[-1] * qbessel_ratio(q0m, a_param, k))
    qb_ratios = [mp.nstr(qbessel_ratio(q0m, a_param, k), 6) for k in range(0, C_MAX)]

    # ---- Witness (audit-only probe) ------------------------------------------
    w = WitnessBuilder("sw-period-lw-sl2-qbessel-probe", engine="python+sympy+mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-25-sw-jet-prolongation-explicit-and-fork.md"
    )
    w.add_parameter("q_0", Q0)
    w.add_data("selection_rule",
               "a_D^(n) = lw(n−1) = (1/n) Σ_{λ⊢n} dim_q V_λ (canonical q-hook dim_q)")
    w.add_data("tau_anchored", mp.nstr(tau, 16))
    w.add_data("sl2_lambda_plus", mp.nstr(lam_plus, 16))
    w.add_data("period_table_n2_to_n8", rows)
    w.add_data("first_sl2_divergence_n",
               (first_div_n if first_div_n is not None else "none ≤ n=8"))
    w.add_data("qbessel_correspondence", {
        "ratio_def": "r_k = −q^k/[(1−q^{k+1})(1−a q^k)], a = q0^{ν+1}, ν = 1/2",
        "coeff_ratios_k0_k6": qb_ratios,
        "note": "Hahn–Exton coefficient ratios at q0 — RECORDED for correspondence, "
                "NOT fit to lw. The q-Bessel coefficients c_k shrink (|r_k|<1) so the "
                "SUPER-EXP growth of a_D^(n)=lw(n−1) lives in the q-Bessel PERIOD / "
                "partial-sum object, not the coefficient sequence — the open z2bn "
                "correspondence (scope-(a): records, does not close).",
    })
    w.add_data("residual_open",
               "a_D^(n)=lw(n−1) geometric↔algebraic identification (#1765) and the "
               "exact q-Bessel⇒period correspondence remain open (bean z2bn).")

    # Assertion 1: the depth-2 SL₂ extrapolation DIVERGES from the true lw by n=6
    # (the fork verdict, reproduced with canonical dim_q).
    diverges = first_div_n is not None and first_div_n <= 6
    w.add_assertion(
        "sl2_depth2_diverges_from_lw_by_n6",
        computed=1 if diverges else 0, expected=1, tolerance=0,
        source=f"|sl2_extrap − lw|/|lw| first exceeds 1e-3 at n={first_div_n} "
               f"(≤6 ⇒ SL₂ is the n≤4 effective fit, not the global period).",
    )
    # Assertion 2: the true lw growth ratio EXCEEDS the SL₂ asymptote λ₊ at the top
    # of the range (super-exp vs geometric).
    top_true_ratio = true_aD[C_MAX + 1] / true_aD[C_MAX]
    lw_super_exp = top_true_ratio > lam_plus
    w.add_assertion(
        "lw_growth_ratio_exceeds_sl2_lambda_plus",
        computed=1 if lw_super_exp else 0, expected=1, tolerance=0,
        source=f"lw ratio at n={C_MAX + 1} = {mp.nstr(top_true_ratio, 8)} > "
               f"λ₊ = {mp.nstr(lam_plus, 8)} (SL₂ geometric cap) — super-exponential.",
    )
    out = w.save()

    print("=" * 84)
    print(" SW period a_D^(n)=lw(n−1): depth-2 SL₂ (n≤4 fit) vs super-exp lw — PROBE")
    print("=" * 84)
    print(f"  τ (anchored) = {mp.nstr(tau, 14)}   λ₊ (SL₂ cap) = {mp.nstr(lam_plus, 10)}")
    print(f"  {'n':>2} {'true a_D=lw(n−1)':>20} {'SL₂ extrap':>16} {'rel.resid':>12} "
          f"{'lw ratio':>10} {'SL₂ ratio':>10}")
    for r in rows:
        print(f"  {r['n']:>2} {r['true_aD_lw']:>20} {r['sl2_extrap']:>16} "
              f"{r['rel_resid']:>12} {str(r['true_ratio']):>10} {str(r['sl2_ratio']):>10}")
    print(f"  first SL₂ divergence (rel>1e-3): n = {first_div_n}")
    print(f"  lw super-exponential (top ratio > λ₊): {lw_super_exp}")
    print(f"\n Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
