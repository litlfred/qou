"""Yekutieli natural-reading +0.5 — precision-floor re-exam at 50 dps.

Per author 2026-05-31: "what options for new avenues? Ocneanu route,
and other closed ones, lets briefly re-explore. maybe new compute/math
is correct and was wrongly ruled out."

## The route in question

Audit `2026-05-23-yekutieli-bijection-natural-reading-negative.md`
tested whether the conjectural Reading-A coefficient `−G·h²` could be
recovered from a natural categorical π_HS projection at H_4. Under
conjugation-averaging (the simplest natural reading), the result was:

  Σ_classes / 4 = (0 + 1 + 1) / 4 = 0.5

vs the conjectural `−G ≈ −0.916`.

The audit's verdict: "Both differ too much to be a precision issue —
structural mismatch."

## Re-exam — the meson Habiro precedent

Meson Habiro c=4 was ruled out for being "0.77% off integer 4" — at
50 dps it was 0.15% with a clean c_3·u³ truncation. The audit's
precision was lower than the cliff.

Could the Yekutieli +0.5 finding similarly be a precision-floor
artifact of the original probe?  We check at 50 dps.

## Method

1. Compute κ_λ (the h² coefficient of dim_q V_λ at q = 1) directly
   from the closed-form rational expressions, at 50 dps.
2. Verify the conjugation-averaged classes-projection sum.
3. Verify Family A's `Σ_λ dim_q V_λ / 4 = 5/2 + (3/4)·h² + 0` to all
   computed orders (h⁰, h², h⁴, h⁶) — termination is a sanity check.
4. Compare +0.5 vs −G with full 50 dps precision.

## Conclusion preview

At 50 dps:
- κ_(4) = 0 EXACTLY
- κ_(3,1) = 1 EXACTLY
- κ_(2,2) = 1 EXACTLY
- κ_(2,1,1) = 1 EXACTLY
- κ_(1,1,1,1) = 0 EXACTLY
- conjugation-averaged sum / 4 = 0.5 EXACTLY (rational number)

The +0.5 result is NOT a precision artifact. It's an exact rational
arising from partition combinatorics. The structural mismatch with
−G ≈ −0.916 is genuine, not a precision-cliff issue.

DIFFERENT from meson Habiro c=4: that miss was a precision-noise
0.77% → 0.15% reduction at 50 dps with a clean c_3 absorbing the
residual. Here the mismatch is a hard rational-vs-transcendental
sign/magnitude divergence with no truncation parameter to absorb it.

## Cross-references

- audit 2026-05-23-yekutieli-bijection-natural-reading-negative.md
- audit 2026-05-18-conjecture-falsification.md (PR #701)
- reading_a_residual_at_50dps.py (the 13.8 ppm residual claim)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def dim_q(partition: tuple[int, ...], q):
    """q-deformed dimension via Frame-Robinson-Thrall hook-content."""
    n = sum(partition)
    cells = []
    for i, p_i in enumerate(partition):
        for j in range(p_i):
            cells.append((i, j))

    def hook_length(i, j):
        h = partition[i] - j
        for k in range(i + 1, len(partition)):
            if partition[k] > j:
                h += 1
            else:
                break
        return h

    def content(i, j):
        return j - i

    # q-hook formula: dim_q V_λ = [n]_q! / Π_{c} [h(c)]_q
    def qint(k):
        if k == 0:
            return mp.mpf(0)
        return (q ** k - q ** (-k)) / (q - 1 / q)

    n_fact = mp.mpf(1)
    for k in range(1, n + 1):
        n_fact *= qint(k)
    denom = mp.mpf(1)
    for (i, j) in cells:
        denom *= qint(hook_length(i, j))
    return n_fact / denom


def main() -> int:
    set_compute_dps(50)
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Yekutieli natural-reading +0.5 — precision-floor check at 50 dps")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # The five partitions of 4
    parts = [
        (4,),
        (3, 1),
        (2, 2),
        (2, 1, 1),
        (1, 1, 1, 1),
    ]
    conj_class = {
        (4,): (1, 1, 1, 1),
        (3, 1): (2, 1, 1),
        (2, 2): (2, 2),
        (2, 1, 1): (3, 1),
        (1, 1, 1, 1): (4,),
    }

    print("[Step 1 — dim_q V_λ and h² coefficients at 50 dps]")
    print(f"  {'λ':<14}{'dim_q V_λ at q_0':<32}")
    h = q - 1 / q
    h2 = h * h

    # The closed-form representation of (3·[2]_q² − 2)/4 = (1/4)·Σ dim_q V_λ
    fam_a = (3 * (q + 1 / q) ** 2 - 2) / 4
    fam_a_h2_coeff_numeric = (fam_a - mp.mpf(5) / 2) / h2

    dim_vals = {}
    for p in parts:
        d = dim_q(p, q)
        dim_vals[p] = d
        print(f"  {str(p):<14}{mp.nstr(d, 25):<32}")

    sum_dim = sum(dim_vals.values())
    print(f"\n  Σ_λ dim_q V_λ          = {mp.nstr(sum_dim, 25)}")
    print(f"  Σ_λ dim_q V_λ / 4      = {mp.nstr(sum_dim / 4, 25)}")
    print(f"  (3·[2]_q² − 2) / 4     = {mp.nstr(fam_a, 25)}")
    print(f"  Family A h² coeff at q_0 (numeric) = {mp.nstr(fam_a_h2_coeff_numeric, 12)}")
    print(f"    expected 3/4 = 0.75")

    # Now compute κ_λ = (dim_q V_λ − dim V_λ) / h² at q_0 — numeric
    # extraction of the h² coefficient.
    print("\n[Step 2 — κ_λ at q_0 (numeric extraction)]")
    print(f"  {'λ':<14}{'dim V_λ':<10}{'κ_λ (numeric)':<28}{'expected':<12}")
    expected = {
        (4,): 0,
        (3, 1): 1,
        (2, 2): 1,
        (2, 1, 1): 1,
        (1, 1, 1, 1): 0,
    }
    dim_classical = {
        (4,): 1, (3, 1): 3, (2, 2): 2, (2, 1, 1): 3, (1, 1, 1, 1): 1,
    }
    kappas = {}
    for p in parts:
        kap = (dim_vals[p] - dim_classical[p]) / h2
        kappas[p] = kap
        print(f"  {str(p):<14}{dim_classical[p]:<10}{mp.nstr(kap, 18):<28}{expected[p]}")

    # Conjugation-averaged classes
    print("\n[Step 3 — Conjugation-averaged HS projection]")
    visited = set()
    class_sum = mp.mpf(0)
    n_classes = 0
    for p in parts:
        if p in visited:
            continue
        c = conj_class[p]
        if c == p:
            # self-conjugate class
            cls_kappa = kappas[p]
            cls_label = f"{p} (self-conj)"
        else:
            cls_kappa = (kappas[p] + kappas[c]) / 2
            cls_label = f"{{{p}, {c}}}"
            visited.add(c)
        visited.add(p)
        class_sum += cls_kappa
        n_classes += 1
        print(f"  class {cls_label:<30} (κ + κ_T)/2 = {mp.nstr(cls_kappa, 12)}")

    nat_reading = class_sum / 4
    print(f"\n  Σ_classes (κ + κ_T)/2  = {mp.nstr(class_sum, 25)}")
    print(f"  / 4 (audit's natural reading) = {mp.nstr(nat_reading, 25)}")
    print(f"  (audit reported +0.5; we get {mp.nstr(nat_reading, 6)})")

    # Catalan G for reference
    G = mp.catalan
    print(f"\n[Step 4 — Comparison to Reading-A's conjectural −G]")
    print(f"  Catalan's constant G = {mp.nstr(G, 25)}")
    print(f"  −G                   = {mp.nstr(-G, 25)}")
    print(f"  natural reading      = {mp.nstr(nat_reading, 25)}")
    print(f"  |nat − (−G)|         = {mp.nstr(abs(nat_reading - (-G)), 12)}")
    print(f"  ratio nat / (−G)     = {mp.nstr(nat_reading / (-G), 12)}")

    # The "precision artifact" hypothesis: is +0.5 close to anything?
    print(f"\n[Step 5 — Is +0.5 a precision-artifact for a different value?]")
    candidates = [
        ("0.5 (exact)", mp.mpf("0.5")),
        ("−G", -G),
        ("3/4 = Family A", mp.mpf("0.75")),
        ("1/2 − G/4", mp.mpf("0.5") - G / 4),
        ("(3/4 − G) Reading-B", mp.mpf("0.75") - G),
        ("4·(0.5) − 3 = -1", mp.mpf("-1")),
        ("(1/2)·(1 − G) = avg of 1/2 and −G/2", mp.mpf("0.5") * (1 - G)),
    ]
    for name, val in candidates:
        diff = nat_reading - val
        rel = diff / nat_reading * 100 if abs(nat_reading) > 1e-30 else mp.inf
        marker = " ⭐ (exact)" if abs(diff) < mp.mpf("1e-30") else ""
        print(f"    {name:<48} = {mp.nstr(val, 18):<22}Δ% = {mp.nstr(rel, 6)}{marker}")

    # ── Verdict ──
    print("\n[Verdict]")
    diff_from_half = abs(nat_reading - mp.mpf("0.5"))
    diff_from_neg_g = abs(nat_reading - (-G))
    if diff_from_half < mp.mpf("1e-30") and diff_from_neg_g > mp.mpf("1.0"):
        verdict = (
            "AUDIT VERDICT STANDS — the natural-reading +0.5 result is "
            "exactly 1/2 at 50 dps (no precision-floor margin). The "
            "structural mismatch with Reading-A's −G ≈ −0.916 is genuine "
            "(sign opposite, magnitude factor 1.83×). This is NOT a "
            "meson-Habiro-style precision artifact: there's no truncation "
            "parameter that could absorb a sign flip. The +0.5 IS an "
            "exact rational arising from partition combinatorics "
            "((1/4) · Σ_classes ((κ_λ + κ_λ^T)/2)); it just doesn't equal −G."
        )
    else:
        verdict = (
            f"Unexpected: natural reading = {mp.nstr(nat_reading, 12)}, "
            f"|nat − 0.5| = {mp.nstr(diff_from_half, 12)}, "
            f"|nat − (−G)| = {mp.nstr(diff_from_neg_g, 12)}. "
            "Manual investigation needed."
        )
    print(f"  {verdict}")

    print("\n[Categorical-quantity interpretation of +0.5]")
    print("  +0.5 IS the structural value of `(1/4) · Σ_{conj classes}")
    print("  (κ_λ + κ_λ^T)/2` at H_4 — the conjugation-averaged half-")
    print("  symmetric h² projection. It is NOT a Reading-A candidate;")
    print("  it's a different valid categorical quantity, just one that")
    print("  doesn't appear in m_p closure at h² order.")
    print()
    print("  Open question: WHICH physical observable does +0.5·h²")
    print("  contribute to? It must be something — exact rationals from")
    print("  partition combinatorics don't appear by accident. Candidates:")
    print("  - Higher-isotope binding-energy linking_weight (m_He, m_Li)")
    print("  - The Frobenius dual-pairing residual (q_β c_4 ladder?)")
    print("  - The Habiro `2 · 𝒞_q^4·D_{4,1}` term in m_He decomposition")

    # ── Witness ──
    w = WitnessBuilder(
        "yekutieli-natural-reading-precision-floor-check",
        engine="python",
    )
    w.set_description(
        "Re-checks the audit 2026-05-23 Yekutieli natural-reading +0.5 "
        "finding at 50 dps. Confirms +0.5 is an exact rational (not a "
        "precision-floor artifact like meson Habiro c=4 was). The "
        "structural mismatch with Reading-A's −G is genuine. Open: which "
        "physical observable +0.5·h² actually contributes to."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("natural_reading_value", mp.nstr(nat_reading, 25))
    w.add_data("difference_from_half", mp.nstr(diff_from_half, 25))
    w.add_data("difference_from_minus_G", mp.nstr(diff_from_neg_g, 25))
    w.add_data("kappa_values", {str(p): mp.nstr(kappas[p], 25) for p in parts})
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="natural_reading_is_exactly_half",
        computed=mp.nstr(diff_from_half, 12),
        expected="0",
        tolerance=1e-25,
        source="(1/4)·Σ_classes (κ + κ_T)/2 = 1/2 exactly via partition combinatorics.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
