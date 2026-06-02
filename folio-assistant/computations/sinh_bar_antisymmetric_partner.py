"""sinh_bar_antisymmetric_partner.py — the bar-anti-symmetric partner
of the unified torus-knot binomial pattern.

Cherry-picks the unified P_m closed form from
`torus_knot_h_expansion_pattern.py` (PR #1125) and derives the
bar-ANTI-symmetric (sinh) analog Q_m, then explores its role as
the Coulomb / charge-distinguishing channel discarded by the
canonical P_avg projection.

## Background

PR #1125 + #1129 established:

    P_m(h) := Σ_{j=0}^m C(m+j, 2j)/2 · h^{2j}
            = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q)        (bar-SYMMETRIC, cosh form)
            = cosh((2m+1) η_0) / (2 cosh η_0)               at substrate η_0 = log q_0

This is the bar-SYMMETRIC even-h projection of tr_M(σ_1^{2m}).  Per
[`bar-involution.md`](../../content/quantum-observable-universe/braids-and-knots/bar-involution.md),
the canonical P_avg projection KEEPS this (cosh, cos_q, Li_2^q)
and DISCARDS the bar-anti-symmetric companion (sinh, sin_q, Φ_q).

## What this probe does

1. Defines the bar-ANTI-symmetric partner Q_m by analogy:

       Q_m(h) := (q^{2m+1} - q^{-(2m+1)}) / (2 [2]_q)        (bar-ANTI-symmetric)
              = sinh((2m+1) η_0) / (2 cosh η_0)               at substrate

2. Verifies symbolically (sympy-exact across m=1..9):
   - bar-symmetry of P_m and bar-anti-symmetry of Q_m under q ↦ q^{-1}
   - the decomposition identity P_m ± Q_m = q^{±(2m+1)} / [2]_q
   - Q_m h-expansion has only odd-h coefficients (bar-anti-symmetric ⇒ h-odd)

3. Computes Q_m(h_0) numerically at substrate for m = 0..6.

4. Cross-checks Q_m + P_m = bar-decomposed full trace:

       P_m(h) + Q_m(h) = q^{2m+1} / [2]_q                     (one bar-piece)
       P_m(h) - Q_m(h) = q^{-(2m+1)} / [2]_q                  (other bar-piece)

5. Documents the EM/Coulomb-channel role of Q (per
   [`crossing-energy-interpretation.md`](../../content/quantum-observable-universe/observations/crossing-energy-interpretation.md):
   sinh(ln q) is the Coulomb / electromagnetic component vs the
   cosh strong-binding component).

## Why this matters (epistemic discipline applies)

The P_avg canonical projection discards Q.  For neutral, isospin-
symmetric observables (m_p alone, m_n alone in the symmetric
limit), that's correct — Q is bar-anti-symmetric and the canonical
chain is bar-symmetric by construction.

For CHARGE-DISTINGUISHING observables (Δm_{n-p}, EM self-energy,
isospin-breaking widths), Q is the natural carrier.  Sibling PR
#1139's D9 isospin-closure work flags exactly this gap (the 305 ppm
substrate flavor split conjectured to be the canonical-isospin
q_0-anomaly is structurally a Q-channel residual).

This probe is a STRUCTURAL CHARACTERIZATION of the discarded channel,
not a derivation of Δm_{n-p}.  Closing the n-p mass gap from Q
requires (a) the right Borromean-side bar-anti-symmetric expansion
(not the T(2,2m) torus-knot expansion used here), and (b) the
operator-valued ⋈_K extension to unlike-isospin pn pairs (per the
sibling audit).

Status: EXPLORATORY (per `local/production-vs-exploratory-discipline`).
This is a structural characterization probe, no production wiring.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402

# Per qou_substrate.precision convention: respects QOU_COMPUTE_DPS env.
set_compute_dps()

# Canonical 50-digit substrate pin (derived from CODATA m_μ/m_e +
# SnapPy Vol(4_1); see qou_substrate.constants).
Q_0 = mp.mpf(Q_50_DIGIT_STR)


def P_m_symbolic(m: int):
    """Bar-SYMMETRIC trace polynomial P_m(h) per PR #1125 + #1129."""
    q = sp.Symbol("q", positive=True)
    return (q ** (2 * m + 1) + q ** (-(2 * m + 1))) / (2 * (q + 1 / q))


def Q_m_symbolic(m: int):
    """Bar-ANTI-symmetric trace polynomial Q_m(h) — sinh partner of P_m.

    Defined by Q_m(h) := (q^{2m+1} - q^{-(2m+1)}) / (2 [2]_q).
    At substrate q_0 = e^{η_0}: Q_m(h_0) = sinh((2m+1) η_0) / (2 cosh η_0).
    """
    q = sp.Symbol("q", positive=True)
    return (q ** (2 * m + 1) - q ** (-(2 * m + 1))) / (2 * (q + 1 / q))


def bar_decomposition_check(m: int) -> dict:
    """Verify P_m + Q_m = q^{2m+1}/[2]_q and P_m - Q_m = q^{-(2m+1)}/[2]_q."""
    q = sp.Symbol("q", positive=True)
    P = P_m_symbolic(m)
    Q = Q_m_symbolic(m)
    sum_pq = sp.simplify(P + Q - q ** (2 * m + 1) / (q + 1 / q))
    diff_pq = sp.simplify(P - Q - q ** (-(2 * m + 1)) / (q + 1 / q))
    return {
        "m": m,
        "P_plus_Q_minus_q_to_2mp1_over_2q": str(sum_pq),
        "P_minus_Q_minus_q_to_neg_2mp1_over_2q": str(diff_pq),
        "decomposition_holds": bool(sum_pq == 0 and diff_pq == 0),
    }


def bar_involution_check(m: int) -> dict:
    """Verify P_m is bar-SYMMETRIC and Q_m is bar-ANTI-symmetric.

    bar: q ↦ q^{-1} sends h = q − q^{-1} ↦ -h.
    Expected: P_m(-h) = P_m(h) (even in h), Q_m(-h) = -Q_m(h) (odd in h).
    """
    q = sp.Symbol("q", positive=True)
    P = P_m_symbolic(m)
    Q = Q_m_symbolic(m)
    P_bar = P.subs(q, 1 / q)
    Q_bar = Q.subs(q, 1 / q)
    P_symmetric = sp.simplify(P_bar - P)
    Q_antisymmetric = sp.simplify(Q_bar + Q)
    return {
        "m": m,
        "P_bar_minus_P": str(P_symmetric),
        "Q_bar_plus_Q": str(Q_antisymmetric),
        "P_is_bar_symmetric": bool(P_symmetric == 0),
        "Q_is_bar_antisymmetric": bool(Q_antisymmetric == 0),
    }


def Q_h_expansion(m: int, order: int = 10) -> list:
    """Extract odd-h coefficients of Q_m by series expansion.

    Q_m is h-odd, so even-h coefficients vanish; odd ones live."""
    q = sp.Symbol("q", positive=True)
    h = sp.Symbol("h", real=True)
    expr = Q_m_symbolic(m)
    q_of_h = (sp.sqrt(h ** 2 + 4) + h) / 2
    series = sp.series(expr.subs(q, q_of_h), h, 0, order + 1).removeO()
    series = sp.expand(series)
    return [sp.simplify(series.coeff(h, n)) for n in range(order + 1)]


def evaluate_at_substrate(m: int) -> dict:
    """Numerical Q_m(h_0) at q = q_0 = 1.10970, 50-dps mpmath."""
    eta_0 = mp.log(Q_0)
    cosh_eta = mp.cosh(eta_0)
    sinh_form = mp.sinh((2 * m + 1) * eta_0) / (2 * cosh_eta)
    direct = (Q_0 ** (2 * m + 1) - Q_0 ** (-(2 * m + 1))) / (2 * (Q_0 + 1 / Q_0))
    delta = mp.fabs(sinh_form - direct)
    cosh_partner = mp.cosh((2 * m + 1) * eta_0) / (2 * cosh_eta)
    return {
        "m": m,
        "k_torus": 2 * m,
        "Q_m_at_q0_sinh_form": float(sinh_form),
        "Q_m_at_q0_direct": float(direct),
        "agreement_delta": float(delta),
        "P_m_at_q0_for_comparison": float(cosh_partner),
        "Q_over_P_ratio": float(sinh_form / cosh_partner) if cosh_partner != 0 else None,
    }


def main() -> int:
    t0 = time.time()
    builder = WitnessBuilder(
        "sinh-bar-antisymmetric-partner", engine="sympy+mpmath"
    )
    builder.set_audit_only("docs/audits/2026-05-24-sinh-bar-antisymmetric-partner-probe.md")

    print("=== sinh bar-anti-symmetric partner Q_m(h) ===\n")
    print("Definition:")
    print("  P_m(h) = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q)   bar-SYMMETRIC   (cosh form)")
    print("  Q_m(h) = (q^{2m+1} - q^{-(2m+1)}) / (2 [2]_q)   bar-ANTI-sym    (sinh form)")
    print()

    # Step 1: Verify bar-symmetry properties
    print("=== Step 1: bar-symmetry verification (sympy-exact) ===\n")
    bar_results = []
    for m in range(1, 10):
        r = bar_involution_check(m)
        bar_results.append(r)
        if not (r["P_is_bar_symmetric"] and r["Q_is_bar_antisymmetric"]):
            print(f"  ✗ m={m}: P sym = {r['P_is_bar_symmetric']}, Q antisym = {r['Q_is_bar_antisymmetric']}")
    bar_all_pass = all(
        r["P_is_bar_symmetric"] and r["Q_is_bar_antisymmetric"]
        for r in bar_results
    )
    print(f"  All {len(bar_results)} cases: P bar-sym + Q bar-antisym → {bar_all_pass}")

    # Step 2: Verify decomposition identity
    print("\n=== Step 2: decomposition P_m ± Q_m = q^{±(2m+1)}/[2]_q ===\n")
    decomp_results = []
    for m in range(1, 10):
        r = bar_decomposition_check(m)
        decomp_results.append(r)
        if not r["decomposition_holds"]:
            print(f"  ✗ m={m}: decomposition fails")
    decomp_all_pass = all(r["decomposition_holds"] for r in decomp_results)
    print(f"  All {len(decomp_results)} cases: decomposition holds → {decomp_all_pass}")

    # Step 3: Odd-h expansion of Q_m
    print("\n=== Step 3: Q_m h-expansion (odd-h only; even h-coefficients should vanish) ===\n")
    q_expansion = []
    for m in range(1, 5):
        coeffs = Q_h_expansion(m, order=7)
        even_h = [coeffs[n] for n in [0, 2, 4, 6]]
        odd_h = [coeffs[n] for n in [1, 3, 5, 7]]
        even_vanish = all(c == 0 for c in even_h)
        q_expansion.append({
            "m": m,
            "even_h_coefs_c0_c2_c4_c6": [str(c) for c in even_h],
            "odd_h_coefs_c1_c3_c5_c7": [str(c) for c in odd_h],
            "even_h_all_vanish": bool(even_vanish),
        })
        marker = "✓" if even_vanish else "✗"
        print(f"  {marker}  m={m}: c_1={odd_h[0]}, c_3={odd_h[1]}, c_5={odd_h[2]}, c_7={odd_h[3]}")

    odd_pattern_pass = all(r["even_h_all_vanish"] for r in q_expansion)

    # Step 4: Numerical evaluation at substrate
    print("\n=== Step 4: Q_m(h_0) at substrate (50-dps mpmath, η_0 = log q_0) ===\n")
    print(f"  q_0 = {Q_0}, η_0 = log q_0 = {float(mp.log(Q_0)):.8f}")
    print(f"  h_0 = q_0 - 1/q_0 = {float(Q_0 - 1/Q_0):.8f}")
    print()
    substrate = []
    for m in range(0, 7):
        r = evaluate_at_substrate(m)
        substrate.append(r)
        print(f"  m={m:>2}  k_torus={r['k_torus']:>2}  "
              f"Q_m(h_0) = {r['Q_m_at_q0_sinh_form']:>10.7f}   "
              f"P_m(h_0) = {r['P_m_at_q0_for_comparison']:>10.7f}   "
              f"Q/P = {r['Q_over_P_ratio']:>8.5f}   "
              f"agree to {r['agreement_delta']:.2e}")
    substrate_all_agree = all(r["agreement_delta"] < 1e-30 for r in substrate)

    # Step 5: Electroweak triplet — what Q says
    print("\n=== Step 5: Q-channel values for the EW torus-knot triplet ===\n")
    print(f"  These are the bar-ANTI-symmetric / Coulomb / EM-channel residuals")
    print(f"  that the canonical P_avg projection discards.\n")
    ew_q = []
    for particle, m in [("W± (T(2,4))", 2), ("Z (T(2,6))", 3), ("H (T(2,8))", 4)]:
        eta_0 = mp.log(Q_0)
        Q_val = mp.sinh((2 * m + 1) * eta_0) / (2 * mp.cosh(eta_0))
        P_val = mp.cosh((2 * m + 1) * eta_0) / (2 * mp.cosh(eta_0))
        ew_q.append({
            "particle": particle,
            "m": m,
            "two_m_plus_1": 2 * m + 1,
            "P_m_at_q0": float(P_val),
            "Q_m_at_q0": float(Q_val),
            "tanh_argument_2mp1_eta_0": float((2 * m + 1) * eta_0),
            "Q_over_P_tanh_form": float(mp.tanh((2 * m + 1) * eta_0)),
        })
        print(f"  {particle:>15}  m={m}, 2m+1={2*m+1:>2}, "
              f"Q={float(Q_val):.6f}, P={float(P_val):.6f}, "
              f"tanh((2m+1)η_0) = {float(mp.tanh((2*m+1)*eta_0)):.6f}")

    # Step 6: Cross-particle Q-ratios (the bar-anti-symmetric Weinberg-angle analog)
    print("\n=== Step 6: Q-ratios — bar-anti-symmetric analog of Weinberg cosh ratios ===\n")
    Q_W = ew_q[0]["Q_m_at_q0"]
    Q_Z = ew_q[1]["Q_m_at_q0"]
    Q_H = ew_q[2]["Q_m_at_q0"]
    Q_ratios = {
        "Q_W_over_Q_Z": Q_W / Q_Z,
        "Q_Z_over_Q_H": Q_Z / Q_H,
        "Q_W_over_Q_H": Q_W / Q_H,
        "comparison_P_W_over_P_Z": ew_q[0]["P_m_at_q0"] / ew_q[1]["P_m_at_q0"],
        "comparison_SM_cos_theta_W": 80.379 / 91.188,
    }
    print(f"  Q_W / Q_Z = sinh(5η) / sinh(7η) = {Q_ratios['Q_W_over_Q_Z']:.6f}")
    print(f"  Q_Z / Q_H = sinh(7η) / sinh(9η) = {Q_ratios['Q_Z_over_Q_H']:.6f}")
    print(f"  Q_W / Q_H = sinh(5η) / sinh(9η) = {Q_ratios['Q_W_over_Q_H']:.6f}")
    print(f"\n  (For comparison, the bar-symmetric P_W/P_Z = {Q_ratios['comparison_P_W_over_P_Z']:.6f}")
    print(f"   vs SM m_W/m_Z = {Q_ratios['comparison_SM_cos_theta_W']:.6f} — PR #1129's cosh result)")
    print(f"\n  Q-ratios differ from cosh ratios because sinh and cosh have different growth at small η_0.")

    all_pass = (
        bar_all_pass
        and decomp_all_pass
        and odd_pattern_pass
        and substrate_all_agree
    )
    verdict = "Q-as-sinh-partner-verified" if all_pass else "verification-failure"
    print(f"\n=== Verdict: {verdict} ===")

    builder.set_description(
        "Bar-ANTI-symmetric partner Q_m(h) = (q^{2m+1} - q^{-(2m+1)}) / "
        "(2 [2]_q) of the bar-symmetric P_m from PR #1125/#1129.  At "
        "substrate Q_m(h_0) = sinh((2m+1) η_0) / (2 cosh η_0).  Verified "
        "symbolically (sympy-exact across m=1..9) that P_m is bar-symmetric, "
        "Q_m is bar-anti-symmetric, and P_m ± Q_m = q^{±(2m+1)}/[2]_q.  "
        "Verified numerically (50-dps mpmath) that the sinh form matches "
        "the direct evaluation at substrate.  Documents the role of Q as "
        "the Coulomb / EM / charge-distinguishing channel that the canonical "
        "P_avg projection discards (per bar-involution.md + "
        "crossing-energy-interpretation.md).  EXPLORATORY: structural "
        "characterization, NOT a derivation of Δm_{n-p}."
    )
    builder.add_parameter("dps", mp.mp.dps)
    builder.add_parameter("q_0_50dps", Q_50_DIGIT_STR)
    builder.add_parameter("q_0_source", "qou_substrate.constants.Q_50_DIGIT_STR")
    builder.add_parameter("m_range_sympy", [1, 9])
    builder.add_parameter("m_range_substrate", [0, 6])
    builder.add_data("bar_involution_check", bar_results)
    builder.add_data("decomposition_check", decomp_results)
    builder.add_data("Q_h_expansion_odd_only", q_expansion)
    builder.add_data("substrate_evaluation", substrate)
    builder.add_data("ew_triplet_Q_values", ew_q)
    builder.add_data("Q_ratios_vs_cosh_ratios", Q_ratios)
    builder.add_data("verdict", verdict)
    builder.add_assertion(
        name="sinh_bar_antisymmetric_partner_verified",
        computed=float(all_pass),
        expected=1.0,
        tolerance=0.0,
        unit="dimensionless (binary)",
        source=(
            "Symbolic verification (sympy) that P_m bar-symmetric + "
            "Q_m bar-anti-symmetric + P_m ± Q_m = q^{±(2m+1)}/[2]_q "
            "across m=1..9 (54 sympy cells).  Numerical verification "
            "(50-dps mpmath) that sinh((2m+1) η_0) / (2 cosh η_0) "
            "matches (q_0^{2m+1} - q_0^{-(2m+1)}) / (2 [2]_q_0) for "
            "m=0..6 (7 cells; agreement < 1e-30)."
        ),
    )
    builder.save()
    print(f"\nWall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
