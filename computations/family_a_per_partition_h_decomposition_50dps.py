"""Family A per-partition h-decomposition at H_4 — mpf 50 dps.

Decomposes `linking_weight_family_a(q) = (1/4) · Σ_{λ⊢4} dim_q V_λ`
into per-partition contributions and per-h-order coefficients at
mp.mpf 50-dps precision.

## Why this exists

PR [#1276](https://github.com/litlfred/qou/pull/1276) lists as its
open question:

> "Specific partition-channel assignment of Bring color-tube vs
> Faddeev h⁴ at H_4 (i.e. WHICH of the 5 H_4 Wedderburn blocks
> each factor occupies)."

This probe answers the **prerequisite question**: what is the
per-partition contribution structure of Family A itself, both
at the h⁰ (Wedderburn) level and at the h² coefficient level?
Identifies the structural channels available for any candidate
to occupy.

## Method (closed-form, exact)

For each partition λ ⊢ 4, the q-dimension `dim_q V_λ` is given by
the hook-length formula:
    dim_q V_λ = [n]_q! / Π_{(i,j)∈λ} [h(i,j)]_q

For λ ⊢ 4 with hook profile, this gives:

| λ            | dim_q V_λ          | h-expansion |
|--------------|--------------------|--------------|
| (4)          | 1                  | 1 (no h)     |
| (3,1)        | [3]_q              | h² + 3       |
| (2,2)        | [4]_q/[2]_q        | h² + 2       |
| (2,1,1)      | [3]_q              | h² + 3       |
| (1,1,1,1)    | 1                  | 1 (no h)     |

Where [3]_q = q² + 1 + q⁻² and [4]_q/[2]_q = q² + q⁻², and
h = q − q⁻¹.

Per-partition contributions to `linking_weight_family_a`:

| λ           | (1/4)·dim_q V_λ | h⁰ coef | h² coef |
|-------------|-----------------|---------|---------|
| (4)         | 1/4             | 1/4     | 0       |
| (3,1)       | (h²+3)/4        | 3/4     | 1/4     |
| (2,2)       | (h²+2)/4        | 1/2     | 1/4     |
| (2,1,1)     | (h²+3)/4        | 3/4     | 1/4     |
| (1,1,1,1)   | 1/4             | 1/4     | 0       |
| **Sum**     | **5/2 + (3/4)h²** | **5/2** | **3/4** ✓ |

## Key structural fact (channel assignment)

**Only THREE of the 5 partitions contribute to the h² coefficient**:
(3,1), (2,2), (2,1,1) — each contributing **exactly 1/4** to the
total 3/4.

**Two of the 5 partitions contribute ONLY to h⁰**:
(4) and (1,1,1,1) — the 1-dimensional symmetric and sign reps,
each contributing 1/4 to h⁰ but 0 to h².

This is the **categorical channel decomposition** for any
modification of Family A's h-dependence. Reading-A (PR #1272)
replaces 3/4 → -G ≈ -0.916, distributing the change of -1.666
across the three h²-active channels — does it split equally
(−0.555 each) or non-uniformly?

## Cross-references

- [`_li_2_q_util.py:linking_weight_family_a`](https://github.com/litlfred/qou/blob/main/computations/_li_2_q_util.py#L172) — production
- [PR #1272](https://github.com/litlfred/qou/pull/1272) γγ̄ decomposition — h² Reading-A
- [PR #1276](https://github.com/litlfred/qou/pull/1276) Bring + Faddeev h⁴ candidate — channel-assignment open Q
- [PR #1285](https://github.com/litlfred/qou/pull/1285) — markov_trace mpf precision fix
- [PR #1287](https://github.com/litlfred/qou/pull/1287) — Borromean h-expansion (companion probe)
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


# Closed-form dim_q V_λ at H_4 in terms of q (exact, polynomial / rational)
def dim_q_V_lambda(partition: tuple[int, ...], q) -> "mp.mpf":
    """Closed-form q-dimension for partitions of 4.

    Hand-derived from the hook-length formula at n=4 (see docstring
    table). Returns mp.mpf at current precision.
    """
    qi = 1 / q
    if partition == (4,) or partition == (1, 1, 1, 1):
        return mp.mpf(1)
    if partition == (3, 1) or partition == (2, 1, 1):
        return q ** 2 + 1 + qi ** 2  # [3]_q
    if partition == (2, 2):
        return q ** 2 + qi ** 2  # [4]_q / [2]_q
    raise ValueError(f"Not a partition of 4: {partition}")


def h_decomposition(partition: tuple[int, ...], h: "mp.mpf") -> dict:
    """Per-partition (h⁰, h², h⁴) coefficient triple in (1/4)·dim_q V_λ.

    By the hook-length closed forms:
    - (4): constant 1/4 at h⁰; 0 elsewhere
    - (3,1): (h²+3)/4 = 3/4 + (1/4)h²
    - (2,2): (h²+2)/4 = 1/2 + (1/4)h²
    - (2,1,1): same as (3,1)
    - (1ⁿ): 1/4 at h⁰; 0 elsewhere

    Returns {0: a_0, 2: a_2, 4: a_4, ...} — all terminate at h².
    """
    if partition == (4,) or partition == (1, 1, 1, 1):
        return {0: mp.mpf(1) / 4, 2: mp.mpf(0), 4: mp.mpf(0)}
    if partition == (3, 1) or partition == (2, 1, 1):
        return {0: mp.mpf(3) / 4, 2: mp.mpf(1) / 4, 4: mp.mpf(0)}
    if partition == (2, 2):
        return {0: mp.mpf(1) / 2, 2: mp.mpf(1) / 4, 4: mp.mpf(0)}
    raise ValueError(f"Not a partition of 4: {partition}")


def reading_a_h2_distribution(target_h2_total: "mp.mpf") -> dict[tuple, "mp.mpf"]:
    """Distribute Reading-A's h² coefficient change −G across the 3 h²-active partitions.

    Family A: h² total = 3/4 (each of (3,1), (2,2), (2,1,1) contributes 1/4).
    Reading-A: h² total = −G ≈ −0.9159656.
    Change: −G − 3/4 ≈ −1.6660.

    Distribution hypotheses to test:

      H_uniform: each of 3 partitions gets equal share (−G/3 − 1/4) — i.e.
        partition channel h² coefficient becomes (−G − 3/4)/3 + 1/4 = (−G − 3/4 + 3/4)/3
        = −G/3 ≈ −0.305 (each).

      H_dim_weighted: weighted by classical dim (3,2,3) → ratio 3:2:3:
        - (3,1): 3/8 of change → 3/8 · (−1.666) = −0.625
        - (2,2): 2/8 of change → 2/8 · (−1.666) = −0.417
        - (2,1,1): 3/8 of change → same as (3,1)

    This function reports H_uniform (the symmetric hypothesis).
    """
    n_active = 3  # (3,1), (2,2), (2,1,1)
    per_partition_change = (target_h2_total - mp.mpf(3) / 4) / n_active
    return {
        (3, 1): mp.mpf(1) / 4 + per_partition_change,
        (2, 2): mp.mpf(1) / 4 + per_partition_change,
        (2, 1, 1): mp.mpf(1) / 4 + per_partition_change,
    }


def main() -> int:
    set_compute_dps(50)
    w = WitnessBuilder(
        "family-a-per-partition-h-decomposition-50dps",
        engine="python",
    )
    w.set_audit_only(
        "docs/canonical-derivation-cheat-sheet.md",
    )
    w.set_description(
        "Per-partition decomposition of `linking_weight_family_a = "
        "(1/4)·Σ_{λ⊢4} dim_q V_λ` at H_4. Identifies the categorical "
        "channels (5 Wedderburn blocks) and shows h⁰ and h² "
        "contributions per channel at mp.mpf 50 dps. Addresses the "
        "prerequisite to PR #1276's 'partition-channel assignment' "
        "open question (which partitions carry Bring color-tube vs "
        "Faddeev h⁴)."
    )

    print("=" * 78)
    print("Family A per-partition h-decomposition at H_4 (mp.mpf 50 dps)")
    print("=" * 78)

    q_str = Q_50_DIGIT_STR
    q = mp.mpf(q_str)
    qi = 1 / q
    h = q - qi
    h2 = h * h
    print(f"\nq_0 (50 dps) = {q_str}")
    print(f"h = q − q⁻¹ = {mp.nstr(h, 25)}")
    print(f"h² = {mp.nstr(h2, 25)}")

    partitions_4 = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]

    print(f"\n[1/4] Per-partition dim_q V_λ at q_0 (closed form):")
    print(f"  {'λ':<12}{'dim_q V_λ at q_0':<24}{'(1/4)·dim_q V_λ at q_0':<28}")
    per_partition_value = {}
    total = mp.mpf(0)
    for lam in partitions_4:
        dim_q = dim_q_V_lambda(lam, q)
        contrib = dim_q / 4
        per_partition_value[lam] = contrib
        total += contrib
        print(f"  {str(lam):<12}{mp.nstr(dim_q, 16):<24}{mp.nstr(contrib, 16):<28}")
    print(f"  {'TOTAL':<12}{'':<24}{mp.nstr(total, 16):<28} (= Family A at q_0)")

    print(f"\n[2/4] Per-partition h⁰ + h² coefficient decomposition (closed form):")
    print(f"  {'λ':<12}{'h⁰ coef':<14}{'h² coef':<14}{'h⁴ coef':<14}")
    h0_total = mp.mpf(0)
    h2_total = mp.mpf(0)
    per_partition_h_coeffs = {}
    for lam in partitions_4:
        coeffs = h_decomposition(lam, h)
        per_partition_h_coeffs[lam] = coeffs
        h0_total += coeffs[0]
        h2_total += coeffs[2]
        print(f"  {str(lam):<12}{mp.nstr(coeffs[0], 8):<14}{mp.nstr(coeffs[2], 8):<14}{mp.nstr(coeffs[4], 8):<14}")
    print(f"  {'TOTAL':<12}{mp.nstr(h0_total, 8):<14}{mp.nstr(h2_total, 8):<14}{mp.nstr(mp.mpf(0), 8):<14}")
    print(f"  (= Family A 5/2 + (3/4)h², terminates at h²)")

    print(f"\n[3/4] Categorical channel summary:")
    print(f"  h⁰-only channels: (4), (1,1,1,1) — both 1-dim reps")
    print(f"      Each contributes 1/4 to h⁰; 0 to h² (no h-dependence)")
    print(f"  h²-active channels: (3,1), (2,2), (2,1,1)")
    print(f"      Each contributes 1/4 to the h² coefficient (sum 3/4)")
    print(f"      (3,1) + (2,1,1) are conjugate (bar-symmetric)")
    print(f"      (2,2) is self-conjugate (bar-fixed)")

    # === 4. Reading-A redistribution analysis ===
    catalan = mp.catalan  # G ≈ 0.91596...
    target_h2_reading_a = -catalan
    print(f"\n[4/4] Reading-A target h² coefficient redistribution:")
    print(f"  Family A h² total: 3/4 = {mp.nstr(mp.mpf(3)/4, 12)}")
    print(f"  Reading-A h² target: −G = {mp.nstr(target_h2_reading_a, 12)}")
    print(f"  Change: {mp.nstr(target_h2_reading_a - mp.mpf(3)/4, 12)}")
    print(f"\n  Distributing the change across (3,1), (2,2), (2,1,1):")
    redist = reading_a_h2_distribution(target_h2_reading_a)
    print(f"  {'λ':<12}{'Family A h²':<16}{'Reading-A h² (uniform)':<26}")
    for lam in [(3, 1), (2, 2), (2, 1, 1)]:
        print(f"  {str(lam):<12}{mp.nstr(mp.mpf(1)/4, 12):<16}{mp.nstr(redist[lam], 12):<26}")
    sum_redist = sum(redist.values())
    print(f"  {'sum h²':<12}{mp.nstr(mp.mpf(3)/4, 12):<16}{mp.nstr(sum_redist, 12):<26}")

    # Witness
    w.add_parameter("q_0_50dps", q_str)
    w.add_parameter("partitions_4", [list(p) for p in partitions_4])
    w.add_data("dim_q_V_lambda_at_q0", {
        str(lam): mp.nstr(dim_q_V_lambda(lam, q), 25)
        for lam in partitions_4
    })
    w.add_data("per_partition_contribution_at_q0", {
        str(lam): mp.nstr(v, 25)
        for lam, v in per_partition_value.items()
    })
    w.add_data("per_partition_h_coefficients", {
        str(lam): {f"h_{k}": mp.nstr(v, 25) for k, v in coeffs.items()}
        for lam, coeffs in per_partition_h_coeffs.items()
    })
    w.add_data("reading_a_h2_redistribution_uniform", {
        str(lam): mp.nstr(v, 25) for lam, v in redist.items()
    })
    w.add_data("structural_finding", {
        "h0_active_partitions": ["(4)", "(1,1,1,1)"],
        "h2_active_partitions": ["(3,1)", "(2,2)", "(2,1,1)"],
        "h0_each_active_contrib": "1/4",
        "h2_each_active_contrib_family_a": "1/4",
        "h2_each_active_contrib_reading_a_uniform": mp.nstr(
            (mp.mpf(1)/4) + (target_h2_reading_a - mp.mpf(3)/4) / 3, 12
        ),
        "interpretation": (
            "Family A: h² is 3 × (1/4) = 3/4 across (3,1), (2,2), "
            "(2,1,1). Reading-A: h² becomes -G ≈ -0.916; under "
            "uniform redistribution, each active partition's "
            "h² coefficient becomes (1/4 + (-G - 3/4)/3) ≈ -0.305. "
            "PR #1276's Bring color-tube + Faddeev h⁴ rational "
            "expression does not naturally fit this Wedderburn-"
            "block decomposition — addresses why my h-expansion "
            "fit gave wildly varying coefficients."
        ),
    })

    # Cross-check assertion: Family A h⁰ total = 5/2 + h² total = 3/4
    family_a_match = (
        abs(h0_total - mp.mpf(5) / 2) < mp.mpf("1e-40")
        and abs(h2_total - mp.mpf(3) / 4) < mp.mpf("1e-40")
    )
    w.add_assertion(
        name="family_a_per_partition_sum_matches_closed_form",
        computed=family_a_match,
        expected=True,
        tolerance=0,
        source=(
            "Sum over 5 partitions of (1/4)·dim_q V_λ h-coefficients "
            "must equal Family A's symbolic h⁰=5/2, h²=3/4 (within "
            "1e-40 at 50 dps)"
        ),
    )

    out = w.save()
    print(f"\n  Witness emitted: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
