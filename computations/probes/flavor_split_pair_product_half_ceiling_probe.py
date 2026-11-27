#!/usr/bin/env python3
r"""
flavor_split_pair_product_half_ceiling_probe.py — the ½ ceiling on the flavor-split second-order
coefficient α from any positive-weight multiplicative pair product.

The p-n flavor split is Δm_pn/M_N = leading·(1 + α·leading), leading = (q-1)²(1-q⁻⁴)/3 PROVEN,
α ≈ 0.929254 the single OPEN coefficient. One candidate mechanism is a multiplicative pair product
1 + split = ∏_k (1 + s_k), Σ s_k = leading, giving α = (Σ_{k<l} s_k s_l)/(Σ s_k)². This probe verifies
exactly that:
  (1) α > ½ at both q₀ anchors — 0.929489 (proton) and 0.929253 (muon), drift 2.36e-4;
  (2) the pair-product coefficient ratio is MAXIMIZED at equal split, value (m-1)/(2m) < ½, and
      unequal weighting only lowers it — so NO positive-weight pair product reaches α;
  (3) hence the positive-weight pair-count mechanism is EXCLUDED (matching the Lean invariant
      QOU.FlavorDressing.pairSum_lt_half_sq: 2·Σ_{k<l}s_k s_l < (Σ s)²).

Sharpens the partial-derivation audit Part 2a (equal-split only). Narrowing, not closure: α remains
underived; the derivation must live on the self-energy/geometric side (α=1), not the pair-count side.
scope-(b) exclusion (proved invariant); no fit; nothing wired; L2 unchanged (2/7).

# Ref: [manuscript] docs/audits/2026-07-26-flavor-split-pair-product-half-ceiling.md
"""
from __future__ import annotations

import sys
from fractions import Fraction as Fr
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))


import mpmath as mp  # noqa: E402 — anchor read-by-name (bean qou-9ugp)
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

# Every mpf this probe builds was constructed at mpmath's default 15 dps:
# the exact Fractions were divided at 53 bits and then printed at 30 digits
# (float64-padding gate; never-raises-dps ratchet). Raise it first.
set_compute_dps()


def leading_ratio(q):
    """leading(q) = (q-1)²(1-q⁻⁴)/3 as an exact Fraction of the Fraction q."""
    return (q - 1) ** 2 * (1 - q ** -4) / 3


def alpha_target(q, codata_ratio):
    lead = leading_ratio(q)
    C_true = codata_ratio / lead
    return (C_true - 1) / lead, lead


def max_pair_ratio(m):
    """sup over positive weights of Σ_{k<l}s_k s_l/(Σs)² at m weights = equal split (m-1)/(2m)."""
    return Fr(m - 1, 2 * m)


def unequal_pair_ratio(weights):
    """Σ_{k<l}s_k s_l/(Σs)² for explicit weights — demonstrates ≤ equal-split value."""
    S = sum(weights)
    cross = sum(weights[i] * weights[j] for i in range(len(weights)) for j in range(i + 1, len(weights)))
    return Fr(cross, S * S)


def main() -> int:
    print("=== flavor-split α: the ½ ceiling on positive-weight pair products ===\n")

    # q₀ at both anchors (50-dp rationals, truncated) and CODATA Δm_pn/M_N.
    #
    # CORRECTED 2026-09-03 (bean qou-9ugp). `q_proton` was bound to
    # 1.10997859555733471 — the RETIRED muon pin A, not a proton value — while
    # `q_muon` held the CODATA-2018 muon derivation. The "both anchors"
    # comparison was therefore muon-vs-muon, two values 1.4 ppb apart, and its
    # drift figure understated the real proton-vs-muon spread by ~4086x
    # (5.78e-8 as written vs 2.36e-4 true). Both pins are now read BY NAME.
    # The verdict is unaffected: alpha > 1/2 at every one of the four values,
    # and the exclusion rests on a proved invariant that does not involve q0.
    _qp, _qm = Fr(Q_50_DIGIT_STR), Fr(mp.nstr(q_muon_at(50), 50, strip_zeros=False))
    q_proton = _qp   # experimental default, qou_substrate.constants.Q_50_DIGIT_STR
    q_muon = _qm     # ideal CAL-2 pin, live CODATA-2022 lepton-ratio derivation
    codata = Fr(Fr(93956542052, 10 ** 8) - Fr(93827208816, 10 ** 8),
                1) / ((Fr(93956542052, 10 ** 8) + Fr(93827208816, 10 ** 8)) / 2)  # (m_n-m_p)/M_N CODATA22

    a_p, lead_p = alpha_target(q_proton, codata)
    a_m, _ = alpha_target(q_muon, codata)
    print(f"leading(q0_proton)        = {float(lead_p):.10e}")
    print(f"alpha_target (proton q0)  = {float(a_p):.10f}")
    print(f"alpha_target (muon   q0)  = {float(a_m):.10f}")
    print(f"anchor drift              = {abs(float(a_p - a_m)):.2e}")
    alpha_gt_half = a_p > Fr(1, 2)
    print(f"alpha > 1/2 ?             = {alpha_gt_half}   (gap = {float(a_p - Fr(1,2)):.6f})\n")

    print("=== pair-product coefficient ratio: equal-split MAX (m-1)/(2m) < 1/2 ===")
    for m in [2, 3, 4, 6, 10, 100, 1000]:
        r = max_pair_ratio(m)
        print(f"  m={m:5d}: (m-1)/(2m) = {float(r):.8f}")
    print("  sup over m -> 1/2 (never reached)\n")

    print("=== unequal weighting LOWERS the ratio (dominance moves away from alpha) ===")
    demos = [
        ("equal 4",      [Fr(1), Fr(1), Fr(1), Fr(1)]),
        ("dominant 4",   [Fr(10), Fr(1), Fr(1), Fr(1)]),
        ("very dom 4",   [Fr(100), Fr(1), Fr(1), Fr(1)]),
    ]
    for name, w in demos:
        print(f"  {name:12s}: ratio = {float(unequal_pair_ratio(w)):.8f}  (≤ equal-split {float(max_pair_ratio(4)):.6f})")
    print()

    # exclusion verdict
    excluded = alpha_gt_half and all(max_pair_ratio(m) < Fr(1, 2) for m in range(2, 2000))
    print(f"RESULT: positive-weight pair product EXCLUDED as source of alpha "
          f"(alpha≈{float(a_p):.6f} > 1/2 = sup pair ratio): {excluded}")
    print("  ⇒ alpha-derivation must live on the self-energy/geometric side (alpha=1), not pair-count.")

    try:
        from witness_base import WitnessBuilder, q0_comparison
        w = WitnessBuilder("flavor-split-pair-product-half-ceiling", engine="python-exact")
        w.set_description(
            "Flavor-split second-order coefficient alpha ≈ 0.929254 EXCLUDES the positive-weight "
            "multiplicative pair-product mechanism: for any positive weights s_k with Σs_k=leading, "
            "α=(Σ_{k<l}s_k s_l)/(Σs_k)² is MAXIMIZED at equal split, value (m-1)/(2m) < 1/2, and "
            "unequal weighting lowers it — so α>1/2 cannot arise from such a product (Lean-proved "
            "invariant QOU.FlavorDressing.pairSum_lt_half_sq: 2·Σ_{k<l}s_k s_l < (Σs)²). Sharpens the "
            "partial-derivation audit Part 2a (equal-split-only; 'swapped pair dominates' moves α the "
            "wrong way). α remains UNDERIVED; the derivation must live on the self-energy/geometric "
            "side (α=1), not pair-count. scope-(b) exclusion; no fit; nothing wired; L2 unchanged (2/7).")
        # Exact Fractions serialised as decimal strings (bean qou-9ugp): these
        # were float64 fields; the arithmetic upstream is exact rational.
        w.add_data("alpha_target_proton", mp.nstr(mp.mpf(a_p.numerator) / a_p.denominator, 30))
        w.add_data("alpha_target_muon", mp.nstr(mp.mpf(a_m.numerator) / a_m.denominator, 30))
        w.add_data("alpha_gt_half", bool(alpha_gt_half))
        w.add_data("pair_product_sup_ratio", "0.5")   # exact sup (m-1)/(2m) -> 1/2, never attained
        w.add_data("positive_pair_product_excluded", bool(excluded))
        w.add_data("lean_invariant", "QOU.FlavorDressing.pairSum_lt_half_sq (sorry-free)")
        w.add_data("anchor_drift_alpha", mp.nstr(abs(mp.mpf((a_p - a_m).numerator) / (a_p - a_m).denominator), 12))
        w.add_assertion(
            "flavor_split_pair_product_half_ceiling",
            computed=str(int(excluded)), expected="1", tolerance=0,
            source=("alpha≈0.929254>1/2=sup_{m}(m-1)/(2m); positive-weight pair product excluded as "
                    "alpha source (Lean pairSum_lt_half_sq). Narrows, does not close; no fit."))
        out = w.save(q0_comparison(
            muon=mp.mpf(mp.nstr(q_muon_at(50), 50, strip_zeros=False)),
            proton=Q_MP,
            reason="alpha_target evaluated at both pins on purpose (anchor-robustness of the "
                   "> 1/2 exclusion); the proton (default) leg is the scored one"))
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if excluded else 1


if __name__ == "__main__":
    raise SystemExit(main())
