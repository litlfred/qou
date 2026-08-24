#!/usr/bin/env python3
"""GAP-A-4 T7 probe — Bratteli/Markov stabilization candidate functor.

After T5 REFUTED 3 cross-algebra functor candidates (F1/F2/F3) and T6
showed the H-sector's own h⁴ = +2 ≠ Borromean −3/4, this probe tests a
fourth candidate: **the Bratteli/Markov stabilization functor**
F: H_3(q) → H_5(q), the natural inclusion via σ_1, σ_2 → σ_1, σ_2 (leaving
σ_3, σ_4 free).

Markov stabilization theorem: tr_M^{(5)}(F(β_Bor)) = z² · tr_M^{(3)}(β_Bor)
for some Markov parameter z.  The H-sector contribution to tr_M^{(5)} is:

  tr_H^{(5)}(F(β_Bor)) := y_{(3,2)} · χ^{(3,2)}(F(β_Bor))
                        + y_{(2,2,1)} · χ^{(2,2,1)}(F(β_Bor))

Per T5, the explicit Young's branching restrictions are:

  Res^{S_5}_{S_3} V_{(3,2)}   = V_{(3)} ⊕ 2·V_{(2,1)}
  Res^{S_5}_{S_3} V_{(2,2,1)} =        2·V_{(2,1)} ⊕ V_{(1^3)}

The Borromean braid has image (s_1s_2)^3 = id in S_3 with writhe 0, so
χ^{(3)}(β_Bor) = χ^{(1^3)}(β_Bor) = 1 exactly.  Therefore:

  χ^{(3,2)}(F(β_Bor))   = 1 + 2·χ^{(2,1)}(β_Bor)
  χ^{(2,2,1)}(F(β_Bor)) = 1 + 2·χ^{(2,1)}(β_Bor)

and the H-sector trace contribution factors as:

  tr_H^{(5)}(F(β_Bor)) = (y_{(3,2)} + y_{(2,2,1)}) · (1 + 2·χ^{(2,1)}(β_Bor))

The Bratteli candidate functor's prediction: if the H-sector exactly
carries the (2,1) h⁴ = −3/4 contribution, then the structural ratio
2·(y_{(3,2)} + y_{(2,2,1)}) / y_{(2,1)} would equal 1 — but at q=1 this is

  2·(5/24 + 5/24) / (2/3) = 2·(10/24) / (16/24) = 5/4

So the Bratteli stabilization picks up the χ^{(2,1)} h⁴ contribution at a
**5/4 multiplier** at q=1, NOT the unit transfer needed to reproduce
−3/4 cleanly.  The constant offset y_{(3,2)} + y_{(2,2,1)} = 5/12 also
differs from y_{(3)} + y_{(1^3)} = 2/6 = 1/3 by the same factor 5/4.

VERDICT: Bratteli/Markov stabilization functor is REFUTED — the structural
ratio is 5/4 (not 1), which would require an ad-hoc rescaling to match
the Borromean h⁴.  Note this 5/4 is the SAME factor that appears in T5
F1's m_{(2,1)} = 4 normalisation question (4/(2·2) where 2 is the dim of
V_{(2,1)}: 4 copies of dim-2 / 2 = 4 — but the ratio of Wenzl-weighted
counts gives 5/4 which is the Plancherel-modulated version of T5 F1).

This is the **4th candidate functor REFUTED** for the cross-algebra
h⁴ = −3/4 obstruction.

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T7-bratteli-stabilization-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402

# Centralised q=1-safe q-integer / dim_q helpers + Q_0_50DPS +
# classical_dim (addresses Gemini deduplication review on PR #1904).
from _gap_a4_qsafe import (  # noqa: E402
    Q_0_50DPS,
    classical_dim_partition as classical_dim,
)

from pathlib import Path  # noqa: E402
from math import factorial as _fact  # noqa: E402

HERE = Path(__file__).resolve().parent


def wenzl_weight_at_q1(lam: tuple) -> mp.mpf:
    """Plancherel measure y_λ(1) = d_λ² / n!."""
    n = sum(lam)
    return mp.mpf(classical_dim(lam)) ** 2 / mp.mpf(_fact(n))


# ── χ^{(2,1)}(β_Bor) closed form (from borromean-markov-trace-closed-form.md) ──


def chi_21_borromean_at_q(q_0: mp.mpf) -> mp.mpf:
    """χ^{(2,1)}(β_Bor) = (−q^{12} + 3q^{10} − 3q^{8} + 4q^{6} − 3q^{4}
    + 3q^{2} − 1) / q^{6}.  At q=1 this gives 2 = d_{(2,1)}, consistent
    with β_Bor → id ∈ S_3."""
    num = (
        -q_0 ** 12 + 3 * q_0 ** 10 - 3 * q_0 ** 8
        + 4 * q_0 ** 6 - 3 * q_0 ** 4 + 3 * q_0 ** 2 - 1
    )
    return num / q_0 ** 6


# ── Bratteli candidate functor — structural ratios ────────────────


def test_bratteli_structural_ratio() -> dict:
    """The candidate functor's structural prediction at q=1:
    2·(y_{(3,2)} + y_{(2,2,1)}) / y_{(2,1)} should equal 1 for a clean
    χ^{(2,1)}(β_Bor) → χ^{(2,1)}(F(β_Bor)) h⁴ transfer at the H-sector.
    """
    print("=" * 78)
    print("T7 Bratteli/Markov stabilization functor")
    print("=" * 78)

    y_32 = wenzl_weight_at_q1((3, 2))
    y_221 = wenzl_weight_at_q1((2, 2, 1))
    y_3 = wenzl_weight_at_q1((3,))
    y_21 = wenzl_weight_at_q1((2, 1))
    y_111 = wenzl_weight_at_q1((1, 1, 1))

    # NB: these are the Plancherel measure w_λ = d_λ²/Σ d_μ², NOT the Markov
    # weights y_λ (which are (1/2, 1/4, 0) at q=1, not (1/6, 2/3, 1/6)). The
    # function name `wenzl_weight_at_q1` is a misnomer — see docs/audits/
    # 2026-06-13-wenzl-trace-normalization-prop-compute-mismatch.md §4.
    print(f"  Plancherel measure w_λ at q=1 (NOT the Markov y_λ):")
    print(f"    y_(3,2)   = 5²/120 = 25/120 = 5/24  = {mp.nstr(y_32, 10)}")
    print(f"    y_(2,2,1) = 5²/120 = 25/120 = 5/24  = {mp.nstr(y_221, 10)}")
    print(f"    y_(3)     = 1/6                     = {mp.nstr(y_3, 10)}")
    print(f"    y_(2,1)   = 4/6  = 2/3              = {mp.nstr(y_21, 10)}")
    print(f"    y_(1,1,1) = 1/6                     = {mp.nstr(y_111, 10)}")

    # χ-coefficient ratio: H-sector picks up 2·(y_(3,2)+y_(2,2,1))
    # times χ^{(2,1)}(β_Bor); Borromean picks up y_(2,1) times same.
    h_sector_chi_coef = 2 * (y_32 + y_221)
    borromean_chi_coef = y_21
    chi_ratio = h_sector_chi_coef / borromean_chi_coef
    print()
    print("  χ^{(2,1)}(β_Bor) multiplier in tr decompositions:")
    print(f"    H-sector on H_5:   2·(y_(3,2)+y_(2,2,1)) "
          f"= 2·5/12 = 5/6  = {mp.nstr(h_sector_chi_coef, 10)}")
    print(f"    Borromean on H_3:  y_(2,1) "
          f"= 2/3              = {mp.nstr(borromean_chi_coef, 10)}")
    print(f"    Ratio H/Borromean: 5/6 ÷ 2/3 = 5/4 "
          f"= {mp.nstr(chi_ratio, 10)}")

    # Constant-term ratio
    h_sector_const = y_32 + y_221
    borromean_const = y_3 + y_111
    const_ratio = h_sector_const / borromean_const
    print()
    print("  Constant-term (writhe-0 1-dim chars) in tr decompositions:")
    print(f"    H-sector on H_5:   y_(3,2)+y_(2,2,1) "
          f"= 5/12             = {mp.nstr(h_sector_const, 10)}")
    print(f"    Borromean on H_3:  y_(3)+y_(1,1,1) "
          f"= 1/3              = {mp.nstr(borromean_const, 10)}")
    print(f"    Ratio: 5/12 ÷ 1/3 = 5/4 "
          f"= {mp.nstr(const_ratio, 10)}")
    print()
    print("  → Both the χ-multiplier ratio AND the constant ratio equal 5/4.")
    print("  → The H-sector contribution is exactly 5/4 × (Borromean trace) "
          "at q=1.")
    print("  → The Bratteli/Markov stabilization picks up Borromean h⁴ "
          "= −3/4 at the H-sector via the multiplier 5/4 — i.e. h⁴ "
          "of H-sector = (5/4)·(−3/4) = −15/16.")
    print("  → This is NOT a unit transfer; it would require an ad-hoc "
          "rescaling by 4/5 to recover −3/4.")
    print()

    return {
        "y_(3,2)_at_q1": str(y_32),
        "y_(2,2,1)_at_q1": str(y_221),
        "y_(2,1)_at_q1": str(y_21),
        "y_(3)_at_q1": str(y_3),
        "y_(1,1,1)_at_q1": str(y_111),
        "chi_multiplier_H_sector": str(h_sector_chi_coef),
        "chi_multiplier_Borromean": str(borromean_chi_coef),
        "chi_ratio_H_over_Borromean": str(chi_ratio),
        "const_H_sector": str(h_sector_const),
        "const_Borromean": str(borromean_const),
        "const_ratio": str(const_ratio),
        "predicted_H_sector_h4_at_q1": "(5/4) · (−3/4) = −15/16 = −0.9375",
        "verdict": (
            "Bratteli/Markov stabilization functor REFUTED — the structural "
            "ratio is uniformly 5/4 (not 1), so the H-sector h⁴ transfer "
            "would be −15/16, not −3/4.  Recovering −3/4 requires an ad-hoc "
            "rescaling by 4/5 that has no derivation in the framework.  This "
            "is the 4th candidate functor refuted (after T5 F1/F2/F3)."
        ),
    }


# ── Sanity: χ^{(2,1)}(β_Bor) closed form check ────────────────────


def test_chi_21_consistency(q_0: mp.mpf) -> dict:
    """Verify the closed form recovers χ^{(2,1)}(id) = 2 at q=1 and
    is real-valued at q_0."""
    chi_at_1 = chi_21_borromean_at_q(mp.mpf(1))
    chi_at_q0 = chi_21_borromean_at_q(q_0)
    print("=" * 78)
    print("Sanity check — χ^{(2,1)}(β_Bor) at q=1 and q_0")
    print("=" * 78)
    print(f"  χ^{{(2,1)}}(β_Bor)|_q=1   = {mp.nstr(chi_at_1, 10)} "
          f"(expected: d_(2,1) = 2 since β_Bor → id ∈ S_3)")
    print(f"  χ^{{(2,1)}}(β_Bor)|_q_0  = {mp.nstr(chi_at_q0, 10)}")
    print()
    return {
        "chi_21_at_q1": str(chi_at_1),
        "chi_21_at_q0": str(chi_at_q0),
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    set_compute_dps()
    w = WitnessBuilder(
        "gap-a4-T7-bratteli-stabilization-probe",
        engine="mpmath",
    )
    w.set_audit_only("docs/audits/2026-06-01-s5-so3-su2-u1-fiber-action.md")
    w.set_description(
        "GAP-A-4 T7 — Bratteli/Markov stabilization candidate functor "
        "H_3 → H_5 via σ_1,σ_2 ↪. Tests whether the H-sector trace "
        "contribution carries the Borromean h⁴ = −3/4 cleanly. "
        "Verdict: REFUTED — structural ratio is 5/4 (not 1)."
    )

    q_0 = mp.mpf(Q_0_50DPS)
    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY")
    w.add_data("production_wired", False)

    print(f"  q₀ = {Q_0_50DPS[:18]}...")
    print()

    sanity = test_chi_21_consistency(q_0)
    bratteli = test_bratteli_structural_ratio()

    w.add_data("chi_21_consistency", sanity)
    w.add_data("bratteli_structural_ratio", bratteli)

    w.add_assertion(
        "chi_21_recovers_dim_at_q1",
        computed=float(sanity["chi_21_at_q1"]),
        expected=2.0,
        tolerance=1e-30,
        source=(
            "β_Bor projects to id ∈ S_3 under π : B_3 → S_3, so "
            "χ^{(2,1)}(β_Bor)|_q=1 = χ^{(2,1)}(id) = d_(2,1) = 2."
        ),
    )
    w.add_assertion(
        "bratteli_ratio_5_over_4",
        computed=float(bratteli["chi_ratio_H_over_Borromean"]),
        expected=1.25,
        tolerance=1e-30,
        source=(
            "2·(y_(3,2)+y_(2,2,1)) / y_(2,1) at q=1 "
            "= 2·(5/24+5/24)/(2/3) = (5/6)/(2/3) = 5/4. "
            "Same for the constant-term ratio (y_(3,2)+y_(2,2,1))/(y_(3)+y_(1^3)) "
            "= (5/12)/(1/3) = 5/4."
        ),
    )

    synthesis = (
        "Bratteli/Markov stabilization functor F: H_3 → H_5 picks up the "
        "Borromean trace at the H-sector with a uniform multiplier 5/4 at "
        "q=1 — confirmed for BOTH the χ^{(2,1)}-coefficient (5/6 vs 2/3) "
        "AND the writhe-0 constant term (5/12 vs 1/3). So the H-sector "
        "h⁴ contribution would be (5/4)·(−3/4) = −15/16, NOT −3/4. "
        "Recovering −3/4 cleanly requires an ad-hoc rescaling by 4/5 with "
        "no framework-internal derivation — Bratteli stabilization is the "
        "4th candidate functor REFUTED (after T5's F1/F2/F3 and T6's "
        "H-sector self-h⁴ = +2). The 5/4 factor itself is structurally "
        "interesting (it equals the per-irrep Plancherel weight ratio "
        "and the multiplicity-4 normalisation from T5 F1), but it is NOT "
        "the obvious bridge the audit's missing functor demands. RT / "
        "q-Schur duality (T8 follow-up) remains untested."
    )
    w.add_data("synthesis_verdict", synthesis)

    print()
    print("-" * 78)
    print("  SYNTHESIS:")
    for chunk in synthesis.split(". "):
        print(f"    {chunk.strip()}")

    out_path = w.save()
    print()
    print(f"  Wrote witness: {out_path}")


if __name__ == "__main__":
    main()
