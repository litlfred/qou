#!/usr/bin/env python3
"""EXPLORATORY — the non-compact / Faddeev q-hyperbolic binding weight (the one
untested cell after the compact q-heat-kernel weight refuted).

Companion to binding_heat_kernel_weight_probe.py. That probe tested the COMPACT
(Peter–Weyl, SU_q(2)) heat-kernel eigenvalue C_λ = Σ_□[c]_q[c+1]_q as the per-block
binding weight and REFUTED it: at q₀>1 the compact q-integer [c]_q ~ sinh(c·ln q₀)
grows exponentially, so C_λ OVER-grows — A-growth S(⁴He)/S(D) = 34.15 vs the AME
target 12.72; heat-kernel damping e^{−C_λ·τ} for every substrate τ collapses
(0.0–0.21).

This probe tests DERIVED, zero-fit NON-COMPACT / q-hyperbolic weights — slower-
growing objects with a structural pedigree, seeking the ~12.72 growth:

  (baseline) C_q0        = C_λ(q₀)                        [compact, expect ≈34]
  (half)     C_sqrtq0    = C_λ(√q₀)                       [half-monodromy / PION scale
                                                           z=√q; #3487 pion=half-4₁]
  (amp)      sqrt_C      = √C_λ(q₀)                       [amplitude, halves the exponent]
  (intensive) C_over_dim = C_λ(q₀)/Π[h]_q(λ)             [Casimir per q-hook-product]

The genuine modular-dual / reciprocal-tame branch (Faddeev b↔1/b shadow) is NOT
evaluated: the modular dual q̃ of q₀≈1.11 is non-perturbative (e^{±O(400)}), so a
"C_recip via the b↔1/b branch" weight explodes/collapses by construction — the
structural refutation below, not an omission.

DISCIPLINE: every candidate is parameter-free (fixed by q₀); NONE is tuned to AME
(that would be the forbidden 7th Δ_λ ansatz). The probe ASSERTS the refutation
(CI-safe); a genuine slower-growth closure (worst |err| ≤ 5% zero-fit) is surfaced
for promotion + categorical derivation. Touches no production. Full p(3A) partition
sum (no truncation). Reuses the atom-χ / y_λ / Δθ_λ machinery of the sibling probe.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
from mpmath import mpf, fabs, acos, sqrt

sys.path.insert(0, str(Path(__file__).resolve().parent / "substrate"))
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402  (50-digit substrate q₀; NOT the f64 Q)
from codata_constants import (  # noqa: E402
    AME_B_DEUTERON_MEV_VALIDATION, AME_B_HE3_MEV_VALIDATION,
    AME_B_HE4_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION)
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
HERE = Path(__file__).resolve().parent
# q₀ from the 50-digit string (not the f64 Q) so the q0_50dps label is honest.
# workdps + unary `+` force re-rounding at full precision.
with mp.workdps(50):
    q0 = +mpf(Q_50_DIGIT_STR)
    sqrt_q0 = +sqrt(q0)

AME_B = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
         "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}
CHI = {"D": "atom-chi-rust-d.witness.json", "T": "atom-chi-rust-t.witness.json",
       "3He": "atom-chi-rust-3he.witness.json", "4He": "atom-chi-rust-4he.witness.json"}
A_GROWTH_TARGET = float(AME_B["4He"] / AME_B["D"])  # ≈ 12.72


def q_int(m, q):
    if m == 0:
        return mpf(0)
    return (q ** m - q ** (-m)) / (q - 1 / q)


def hooks(lam):
    colh = [0] * (max(lam) if lam else 0)
    for ri in lam:
        for j in range(ri):
            colh[j] += 1
    hs = []
    for i, ri in enumerate(lam):
        for j in range(ri):
            hs.append((ri - j - 1) + (colh[j] - i - 1) + 1)
    return hs


def dim_classical(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= h
    return mp.factorial(sum(lam)) / den


def qhook_prod(lam, q):
    """q-hook product Π_□ [hook]_q (a hook-content proxy for the q-dimension
    scale — NOT the exact Weyl q-dimension). Used only as the intensive
    denominator of the C_over_dim candidate, which collapses regardless."""
    prod = mpf(1)
    for h in hooks(lam):
        prod *= q_int(h, q)
    return prod


def content_casimir(lam, q):
    """C_λ(q) = Σ_□ [c]_q [c+1]_q, c = col − row (compact heat-kernel eigenvalue)."""
    total = mpf(0)
    for i, ri in enumerate(lam):
        for j in range(ri):
            c = j - i
            total += q_int(c, q) * q_int(c + 1, q)
    return total


def main() -> int:
    weights = ["C_q0", "C_sqrtq0", "sqrt_C", "C_over_dim"]
    S = {w: {} for w in weights}

    for name, fname in CHI.items():
        path = HERE / fname
        if not path.exists():
            print(f"⚠ missing chi witness {fname}"); continue
        with open(path, encoding="utf-8") as f:
            raw = json.load(f)
        d = raw["data"] if "data" in raw else raw
        atom = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
                for el in d["atom"]["by_partition"]}
        free = {tuple(el["partition"]): mpf(str(el["chi_lambda"]))
                for el in d["free"]["by_partition"]}
        acc = {w: mpf(0) for w in weights}
        for lam in atom:
            ll = list(lam)
            dl = dim_classical(ll)
            dth = acos(mp.mpc(atom[lam] / dl)) - acos(mp.mpc(free[lam] / dl))
            a = fabs(dth)
            C = content_casimir(ll, q0)
            C_half = content_casimir(ll, sqrt_q0)
            hp = qhook_prod(ll, q0)
            wv = {
                "C_q0": C,                                    # compact baseline (≈34)
                "C_sqrtq0": C_half,                           # half-monodromy / pion scale
                "sqrt_C": sqrt(C) if C >= 0 else mpf(0),      # amplitude (half exponent)
                "C_over_dim": C / hp if hp != 0 else mpf(0),  # intensive (Casimir/q-hook-prod)
            }
            for w in weights:
                acc[w] += wv[w] * a
        for w in weights:
            S[w][name] = acc[w]

    isos = [k for k in CHI if k in S["C_q0"]]
    results = {}
    for w in weights:
        num = mp.fsum(S[w][k] * AME_B[k] for k in isos)
        den = mp.fsum(S[w][k] ** 2 for k in isos)
        scale = num / den if den else mpf(0)
        worst, per = mpf(0), {}
        for k in isos:
            Bp = scale * S[w][k]
            err = (Bp - AME_B[k]) / AME_B[k]
            per[k] = {"B_pred": float(Bp), "err": float(err)}
            worst = max(worst, fabs(err))
        growth = float(S[w]["4He"] / S[w]["D"]) if S[w].get("D") else float("nan")
        results[w] = {"global_scale": float(scale), "worst_err": float(worst),
                      "S_4He_over_S_D": growth, "per_isotope": per}

    print(f"\nq0 = {mp.nstr(q0,8)}   √q0 = {mp.nstr(sqrt_q0,8)}   "
          f"A-growth target S(⁴He)/S(D) ≈ {A_GROWTH_TARGET:.2f}\n")
    print(f"{'weight':<14}{'worst|err|':>11}{'S(⁴He)/S(D)':>13}   pedigree")
    ped = {"C_q0": "compact baseline", "C_sqrtq0": "half-monodromy √q₀ (pion)",
           "sqrt_C": "amplitude √C", "C_over_dim": "Casimir/q-dim (intensive)"}
    any_close = False
    for w in weights:
        r = results[w]
        close = r["worst_err"] <= 0.05
        any_close = any_close or close
        print(f"  {w:<12}{r['worst_err']*100:>9.1f}%{r['S_4He_over_S_D']:>12.2f}   "
              f"{ped[w]}{'   ← CLOSES' if close else ''}")

    verdict = (
        "REFUTED (scope-(a)): no DERIVED non-compact / q-hyperbolic weight closes "
        f"the A≥3 binding zero-fit to 5%. The compact C_λ over-grows (S(⁴He)/S(D)="
        f"{results['C_q0']['S_4He_over_S_D']:.2f} vs target {A_GROWTH_TARGET:.2f}); the "
        f"half-monodromy √q₀ scale gives {results['C_sqrtq0']['S_4He_over_S_D']:.2f}; "
        f"√C gives {results['sqrt_C']['S_4He_over_S_D']:.2f}; Casimir/q-dim gives "
        f"{results['C_over_dim']['S_4He_over_S_D']:.2f}. Structural reason: the binding "
        "sum runs over Young-diagram partitions (compact SU_q(2)/S_n objects); a true "
        "non-compact Faddeev weight has no partition labelling, and the modular dual "
        "q̃ of q₀≈1.11 is non-perturbative (e^{±O(400)}) — explode/collapse, never the "
        "moderate 12.72 regime. The Δ_λ / A≥3 binding closure stays OPEN; no 7th fit "
        "introduced. Touches no production."
        if not any_close else
        "A derived non-compact weight CLOSES A≥3 zero-fit — promote for categorical "
        "derivation (surface, do not wire until derived)."
    )

    wb = WitnessBuilder("binding-qhyperbolic-weight-probe", engine="mpmath",
                        output_dir=HERE)
    wb.set_description(
        "EXPLORATORY: DERIVED non-compact / q-hyperbolic binding weights (C_λ at "
        "√q₀ half-monodromy, √C amplitude, Casimir/q-dim) vs the compact C_λ that "
        "refuted. Seeks the AME A-growth 12.72 zero-fit; asserts refutation if none "
        "closes to 5%. Full p(3A) sum; no τ/AME fit; no production touch.")
    wb.add_parameter("q0_50dps", mp.nstr(q0, 50))
    wb.add_parameter("sqrt_q0_50dps", mp.nstr(sqrt_q0, 50))
    wb.add_parameter("A_growth_target", A_GROWTH_TARGET)
    wb.add_data("weights", results)
    wb.add_data("verdict", verdict)
    wb.add_assertion(
        name="derived_qhyperbolic_weight_closes_or_refutes_A3plus",
        computed=str(int(not any_close)), expected="1", tolerance=0,
        source=(f"worst |err| over {isos} at 1 global scale; growth vs {A_GROWTH_TARGET:.2f}. "
                "1=refuted (no zero-fit closure), 0=closes → promote."))
    out = wb.save()
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
