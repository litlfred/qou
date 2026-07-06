"""Reading-A h² redistribution hypotheses across 3 Wedderburn channels.

Companion probe to `family_a_per_partition_h_decomposition_50dps.py`
(same branch, PR #1287). Per author 2026-05-25: investigate the
(3,1) vs (2,2) vs (2,1,1) asymmetry — uniform redistribution is
one hypothesis; non-uniform (dim-weighted, bar-symmetric) are
others.

## The 3 candidate redistribution hypotheses

All preserve the **total** h² coefficient = −G (Reading-A target),
but distribute it differently across the 3 h²-active channels.

### H1 — Uniform

Each of (3,1), (2,2), (2,1,1) gets the same h² coefficient:
  c_λ = −G/3 ≈ −0.305

### H2 — Dim-weighted (classical dimensions 3:2:3)

  c_(3,1)   = 3/8 · (−G) ≈ −0.343
  c_(2,2)   = 2/8 · (−G) ≈ −0.229
  c_(2,1,1) = 3/8 · (−G) ≈ −0.343

(3,1) and (2,1,1) get equal shares by dim-weight = bar-symmetric ✓

### H3 — Bar-symmetric (2-parameter family with one constraint)

By bar-invariance λ ↔ λ^T at q ↔ q⁻¹: c_(3,1) = c_(2,1,1) ≡ a,
and c_(2,2) = b (self-conjugate). Sum: 2a + b = −G.

Sub-hypotheses:
- H3a (a = b): degenerates to uniform H1
- H3b (a = 0, b = −G): (2,2) carries all the change
- H3c (b = 0, 2a = −G): bar-pair carries all, self-conjugate untouched
- H3d (categorical: a/b ratio from Hoefsmit matrix structure)

H3d requires extra categorical input — e.g. the relative
contribution to `tr_M(β_𝓑)` of bar-symmetric vs self-conjugate
channels at H_3 (lifted to H_4 by stabilisation).

## Why this matters

All 3 hypotheses give the **same total h² = −G** and therefore
the **same m_p prediction at h² order**. They differ only at
**h⁴+** if each channel carries its own higher-order correction.

PR #1272's `via_jones` reports h⁴ ≈ −3.03 (total). If H1 is
correct, each active channel contributes h⁴ ≈ −1.01. If H2 or
H3 is correct, the per-channel h⁴ distribution is non-uniform.

**Distinguishing the hypotheses requires per-channel h⁴+ data**,
which is outside this single-session scope.

## Cross-references

- Companion probe: `family_a_per_partition_h_decomposition_50dps.py`
- [PR #1272](https://github.com/litlfred/qou/pull/1272) — γγ̄ decomposition
- [PR #1276](https://github.com/litlfred/qou/pull/1276) — Bring + Faddeev h⁴ candidate
- [PR #1285](https://github.com/litlfred/qou/pull/1285) — markov_trace mpf precision fix
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "reading-a-redistribution-hypotheses-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/canonical-derivation-cheat-sheet.md",
    )
    w.set_description(
        "Comparison of 3 redistribution hypotheses for Reading-A's "
        "h² coefficient (−G) across (3,1), (2,2), (2,1,1) Wedderburn "
        "channels at H_4. All hypotheses preserve total h² = −G; "
        "they differ in per-channel split, distinguishable only by "
        "per-channel h⁴+ data."
    )

    print("=" * 78)
    print("Reading-A h² redistribution hypotheses across 3 Wedderburn")
    print("channels at H_4 (mp.mpf 50 dps)")
    print("=" * 78)

    q_str = Q_50_DIGIT_STR
    q = mp.mpf(q_str)
    h = q - 1 / q
    h2 = h * h
    catalan = mp.catalan
    minus_G = -catalan
    delta_total = minus_G - mp.mpf(3) / 4  # ≈ −1.666

    print(f"\nq_0 (50 dps) = {q_str}")
    print(f"h = {mp.nstr(h, 20)}, h² = {mp.nstr(h2, 20)}")
    print(f"Family A h² coef: 3/4 = {mp.nstr(mp.mpf(3)/4, 12)}")
    print(f"Reading-A target h² coef: −G = {mp.nstr(minus_G, 12)}")
    print(f"Total change: Δh² = {mp.nstr(delta_total, 12)}")

    # === Hypotheses ===
    # H1 — uniform: each gets −G/3
    h1_each = minus_G / 3
    h1 = {
        (3, 1): h1_each,
        (2, 2): h1_each,
        (2, 1, 1): h1_each,
    }

    # H2 — dim-weighted (3:2:3)
    h2_dim_3_1 = mp.mpf(3) / 8 * minus_G
    h2_dim_2_2 = mp.mpf(2) / 8 * minus_G
    h2_hyp = {
        (3, 1): h2_dim_3_1,
        (2, 2): h2_dim_2_2,
        (2, 1, 1): h2_dim_3_1,
    }

    # H3b — self-conjugate carries all: a=0, b=−G
    h3b = {
        (3, 1): mp.mpf(0),
        (2, 2): minus_G,
        (2, 1, 1): mp.mpf(0),
    }

    # H3c — bar-pair carries all: 2a=−G, b=0
    h3c_a = minus_G / 2
    h3c = {
        (3, 1): h3c_a,
        (2, 2): mp.mpf(0),
        (2, 1, 1): h3c_a,
    }

    hypotheses = {
        "H1 (uniform −G/3)": h1,
        "H2 (dim-weighted 3:2:3)": h2_hyp,
        "H3b (self-conj only)": h3b,
        "H3c (bar-pair only)": h3c,
    }

    print(f"\n[1/3] Hypothesis comparison — per-channel h² coefficients:")
    print(f"  {'Hypothesis':<26}{'(3,1) h²':<14}{'(2,2) h²':<14}{'(2,1,1) h²':<14}{'sum':<10}")
    for name, hyp in hypotheses.items():
        s = sum(hyp.values())
        print(f"  {name:<26}{mp.nstr(hyp[(3,1)], 8):<14}{mp.nstr(hyp[(2,2)], 8):<14}{mp.nstr(hyp[(2,1,1)], 8):<14}{mp.nstr(s, 8):<10}")

    print(f"\n[2/3] Linking-weight prediction at q_0 (h² order only):")
    print(f"  All 4 hypotheses give same TOTAL h² contribution.")
    h0_part = mp.mpf(5) / 2  # Family A h⁰ unchanged
    h2_contrib = minus_G * h2
    pred_h2_only = h0_part + h2_contrib
    print(f"  linking_weight (h² order) = 5/2 + (−G)·h² = {mp.nstr(pred_h2_only, 20)}")
    print(f"  Target (= m_p / m_e / Geom_leading) = 2.4599")
    pred_to_target_gap = pred_h2_only - mp.mpf("2.4599")
    print(f"  Residual gap: {mp.nstr(pred_to_target_gap, 12)}")
    print(f"  (The residual ~8% is the h⁴+ tower — distinguishes hypotheses)")

    print(f"\n[3/3] Bar-symmetry constraint analysis:")
    print(f"  AGENTS.md §7b: Type-B folding for bar-invariance — partitions")
    print(f"  paired by λ ↔ λ^T should have IDENTICAL h-coefficients.")
    print(f"  At H_4: (3,1)^T = (2,1,1), and (2,2)^T = (2,2) (self-conj).")
    print(f"  Bar-symmetric hypotheses (a = c_(3,1) = c_(2,1,1)):")
    print(f"    H1 (uniform):           a = b = −G/3      → bar-symmetric ✓")
    print(f"    H2 (dim-weighted):      a = −3G/8, b = −G/4 → bar-symmetric ✓")
    print(f"    H3b (self-conj only):   a = 0, b = −G     → bar-symmetric ✓")
    print(f"    H3c (bar-pair only):    a = −G/2, b = 0   → bar-symmetric ✓")
    print(f"  All 4 hypotheses respect bar-symmetry. The constraint")
    print(f"  is NECESSARY but NOT SUFFICIENT to pick a unique hypothesis.")

    # Witness
    w.add_parameter("q_0_50dps", q_str)
    w.add_parameter("reading_a_h2_target", mp.nstr(minus_G, 25))
    w.add_data("hypotheses", {
        name: {
            str(lam): mp.nstr(v, 25) for lam, v in hyp.items()
        }
        for name, hyp in hypotheses.items()
    })
    w.add_data("structural_constraints", {
        "bar_symmetry_required": "c_(3,1) = c_(2,1,1) at every h-order (by Type-B folding)",
        "bar_symmetry_status": "All 4 hypotheses respect it (necessary but not sufficient)",
        "total_h2_constraint": (
            f"Σ c_λ = −G ≈ {mp.nstr(minus_G, 8)} (Reading-A target)"
        ),
        "distinguishing_data_needed": (
            "Per-channel h⁴+ coefficients (not currently available; would "
            "require Markov-trace computation on H_4 directly with "
            "per-block decomposition, or Hoefsmit-matrix per-channel "
            "contribution to tr_M(β) at each h-order)"
        ),
    })
    w.add_data("pred_h2_order_at_q0", mp.nstr(pred_h2_only, 25))
    w.add_data("residual_gap_h4_plus_tower", mp.nstr(pred_to_target_gap, 25))

    # Sanity assertion: all hypotheses sum to −G
    sums = [sum(hyp.values()) for hyp in hypotheses.values()]
    sums_ok = all(abs(s - minus_G) < mp.mpf("1e-40") for s in sums)
    w.add_assertion(
        name="all_hypotheses_preserve_total_h2_minus_G",
        computed=sums_ok,
        expected=True,
        tolerance=0,
        source=(
            "All 4 redistribution hypotheses must sum to −G "
            "(Reading-A's h² total target), within 1e-40 at 50 dps"
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
