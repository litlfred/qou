"""Topic 4 probe: Per-pair Wedderburn-block enumeration vs mult(Φ_8).

PR #1649 mirror-pair data shows mult(Φ_8) is NON-MONOTONIC in A:
  A=12 mirror pair has mult=10; A=14 DROPS to 4.
No closed form in A can capture this.

The PR #1625 framing identifies the categorical mechanism: the
level-2 SU(2) Wenzl annihilator at q = ζ_8 forces [4]_q = 0,
which kills partitions of n = 3A with FIRST COLUMN ≥ 4
(equivalently > 3 ROWS in the partition).

The "active" partitions (those that contribute to χ_λ(β_X−β_Y) at
q = ζ_8) are those with first column ≤ 3, equivalently those with
at most 3 rows.

This probe enumerates:
  active(A) := #{ λ ⊢ 3A : λ has ≤ 3 parts }

and correlates with the observed mult(Φ_8) for each mirror pair.

CORPUS CITATIONS (per CLAUDE.md §"Before declaring 'open'"):
  prop:categorical-neutrality-saturated-shells —
    full-twist Δ²_n acts as identity on Φ_n iff n ∈ {2,8,20,28,50,82,126}
    ⇒ Φ_n supported on self-conjugate partitions at magic n
  conj:diagrammatic-double-magic-lr-fusion —
    double-magic (Z, N both magic) ⇒ LR-fusion rigid, single
    self-conjugate Specht module on diagonal
  prop:magic-numbers-from-q —
    magic numbers {2, 8, 20, 28} EMERGE from substrate q₀ via
    Hoefsmit seminormal forms; no empirical magic list used
  MAG-1 audit (2026-05-02-mag1-complete-7-magic-numbers.md) —
    all 7 magic numbers numerically verified

The Φ_8 multiplicity drops at A=6 and A=14 may be the mirror-pair
empirical signature of these existing propositions: when one half
hits a magic shell, that half's Wedderburn support contracts to
self-conjugates (via prop:categorical-neutrality-saturated-shells),
reducing the active partitions in the pair-difference and hence
the Wenzl-annihilator linear-relation count.

This probe is empirical only — it does NOT propose a new closed
form, per CLAUDE.md's "no 7th ansatz" Track A discipline.
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


# Measured mult(Φ_8) from 10 mirror-pair data points (PR #1642, #1649)
MIRROR_DATA = [
    # (pair_label, A, mult_Phi_8, refined_predicted, phi_1, phi_2, magic_structure)
    ("n − p",       1, 0,  0, 1, 1, "Z=0(magic?)/N=1 vs Z=1/N=0"),
    ("³He − ³H",    3, 2,  2, 1, 0, "Z=2 magic ↔ N=2 magic"),
    ("⁵Li − ⁵He",  5, 4,  4, 1, 0, "N=2 magic ↔ Z=2 magic (one extra in 1p)"),
    ("⁶He − ⁶Be",  6, 2,  4, 1, 1, "Z=2 magic ↔ N=2 magic (TWO extra in 1p)"),
    ("⁷Be − ⁷Li",  7, 6,  6, 1, 0, "mid 1p shell"),
    ("⁸B − ⁸Li",   8, 6,  6, 1, 1, "mid 1p shell"),
    ("⁹B − ⁹Be",   9, 8,  8, 1, 0, "mid 1p shell"),
    ("¹⁰C − ¹⁰Be", 10, 8, 8, 1, 1, "1p_{3/2} sub-closure on one side"),
    ("¹²N − ¹²B",  12, 10, 10, 1, 1, "1 hole in 1p shell each"),
    ("¹⁴O − ¹⁴C",  14, 4, 12, 1, 1, "Z=8 magic ↔ N=8 magic (DOUBLY)"),
]


def partitions_with_at_most_k_parts(n: int, k: int) -> int:
    """Count partitions of n into at most k parts.

    Standard recurrence: p(n, k) = p(n-1, k-1) + p(n-k, k) (with
    base cases p(0, k) = 1 for all k ≥ 0; p(n, 0) = 0 for n > 0).
    """
    if n == 0:
        return 1
    if k == 0 or n < 0:
        return 0
    return partitions_with_at_most_k_parts(n - 1, k - 1) + \
        partitions_with_at_most_k_parts(n - k, k)


def partitions_at_most_3_rows_with_content_sum_zero(n: int) -> int:
    """Count partitions of n with ≤ 3 rows AND content sum c(λ) = 0
    (i.e., self-conjugate under transpose-and-flip, satisfying the
    full-twist Δ²_n eigenvalue = q^0 = 1).

    For ≤ 3 rows partitions of n, the self-conjugate condition is
    that λ = λ' on its Young diagram. For partitions with ≤ 3 rows,
    transpose has ≤ 3 columns; self-conjugate means λ has ≤ 3 rows
    AND ≤ 3 columns simultaneously — a 3×3 Young diagram.

    For 3×3 partitions of n: this is the count of partitions of n
    fitting in a 3×3 box, which is non-zero only for 0 ≤ n ≤ 9.
    For n > 9, the count is 0 (no partition fits in 3×3 box).

    This means at A ≥ 4 (n = 3A ≥ 12), the ≤3-rows-AND-≤3-cols
    partition count is zero — so the "Φ_n supported on
    self-conjugates" criterion is much more restrictive than
    just "≤ 3 rows".
    """
    # Partitions of n fitting in a 3x3 box (rows ≤ 3, cols ≤ 3)
    if n > 9 or n < 0:
        return 0
    # Generating function: Σ q^n * count = prod over 3x3 grid (1 - q^k_ij)/...
    # Simpler: enumerate directly
    count = 0
    for a in range(min(3, n) + 1):
        for b in range(min(a, n - a) + 1):
            for c in range(min(b, n - a - b) + 1):
                if a + b + c == n:
                    # Check self-conjugate: λ = (a, b, c) self-conj iff
                    # transpose: row counts = (number with λ_i ≥ 1,
                    # number with λ_i ≥ 2, number with λ_i ≥ 3)
                    # For λ = (a, b, c) with a ≥ b ≥ c:
                    #   λ'_1 = # i : λ_i ≥ 1 = 3 if c ≥ 1 else (2 if b ≥ 1 else 1)
                    #   λ'_2 = # i : λ_i ≥ 2
                    #   λ'_3 = # i : λ_i ≥ 3
                    # Self-conj: λ' = λ, i.e. λ'_1=a, λ'_2=b, λ'_3=c
                    lp1 = sum(1 for x in (a, b, c) if x >= 1)
                    lp2 = sum(1 for x in (a, b, c) if x >= 2)
                    lp3 = sum(1 for x in (a, b, c) if x >= 3)
                    if (lp1, lp2, lp3) == (a, b, c):
                        count += 1
    return count


def main() -> int:
    t0 = time.perf_counter()
    print("=" * 78)
    print(" PER-PAIR WEDDERBURN-BLOCK ENUMERATION")
    print(" (level-2 SU(2) Wenzl 'active' partitions vs mult(Φ_8))")
    print("=" * 78)
    print()

    print(f"{'Pair':<14} {'A':>3} {'n=3A':>5} {'≤3 rows':>9} "
          f"{'3×3 self-conj':>15} {'mult(Φ_8)':>10} {'refined':>8} {'Δ':>5} "
          f"{'magic'}")
    print("─" * 110)

    rows = []
    for label, A, mult_8, refined, phi_1, phi_2, magic_desc in MIRROR_DATA:
        n = 3 * A
        # "Active" partitions at q = ζ_8 (level-2 Wenzl annihilator):
        # those with first column ≤ 3, i.e. ≤ 3 rows
        active_count = partitions_with_at_most_k_parts(n, 3)
        # Self-conjugate partitions with ≤ 3 rows + ≤ 3 cols (fit in 3×3 box)
        self_conj_3x3 = partitions_at_most_3_rows_with_content_sum_zero(n)
        delta = mult_8 - refined
        anomaly = "✗" if mult_8 != refined else "✓"
        row_data = {
            "pair": label, "A": A, "n_eq_3A": n,
            "active_partitions_le_3_rows": active_count,
            "self_conj_partitions_3x3_box": self_conj_3x3,
            "mult_Phi_8_observed": mult_8,
            "refined_predicted": refined,
            "anomaly": anomaly,
            "delta_observed_minus_refined": delta,
            "magic_structure": magic_desc,
        }
        rows.append(row_data)
        print(f"{label:<14} {A:>3} {n:>5} {active_count:>9} "
              f"{self_conj_3x3:>15} {mult_8:>10} {refined:>8} {delta:>+5d} "
              f"{anomaly} {magic_desc[:35]}")

    # ─── Correlation analysis ────────────────────────────────────
    print()
    print("=" * 78)
    print(" CORRELATION ANALYSIS")
    print("=" * 78)
    print()
    print("Per the 'first-column ≤ 3' Wenzl criterion at q = ζ_8:")
    print(f"  active(A) counts grow quickly with A:")
    print(f"    A=1 (n=3):   active = {partitions_with_at_most_k_parts(3, 3)} = 3 (matches expected: (3), (2,1), (1,1,1))")
    print(f"    A=14 (n=42): active = {partitions_with_at_most_k_parts(42, 3)}")
    print()
    print("So the 'active count' alone CANNOT explain mult(Φ_8) — it grows")
    print("monotonically with A while mult(Φ_8) drops at A=6 and A=14.")
    print()
    print("The actual mechanism per prop:categorical-neutrality-saturated-shells:")
    print("  - At a magic shell (Z or N ∈ {2,8,20,28,50,82,126}), the")
    print("    full-twist Δ²_n acts as identity on Φ_n.")
    print("  - This restricts the Wedderburn support to SELF-CONJUGATE")
    print("    partitions (content sum c(λ) = 0).")
    print("  - For pair-differences, ONE HALF hitting magic restricts THAT")
    print("    HALF's support — fewer Wenzl-annihilator linear relations")
    print("    survive in the difference.")
    print()
    print("Anomaly hypothesis (qualitative):")
    print("  A=6 ⁶He(Z=2)/⁶Be(N=2):   Z=2 + N=2 magic on opposite sides")
    print("  A=14 ¹⁴O(Z=8)/¹⁴C(N=8): Z=8 + N=8 magic on opposite sides")
    print("  BOTH have one magic shell per side ⇒ enhanced Wedderburn-block")
    print("  contraction ⇒ FEWER active linear relations ⇒ LOWER mult(Φ_8)")
    print()
    print("Open: empirical quantification requires LR-fused per-block χ_λ")
    print("evaluation at q = ζ_8 for each pair (research-grade compute,")
    print("not done in this probe).")

    elapsed = time.perf_counter() - t0

    payload = {
        "computation": "per-pair-wedderburn-enumeration",
        "description": (
            "Topic 4 probe: enumerate level-2 Wenzl-active partitions "
            "(≤ 3 rows) and self-conjugate-in-3×3-box partitions at "
            "level n = 3A for each mirror pair, correlate with "
            "observed mult(Φ_8). Empirical step — NOT a new closed "
            "form (per CLAUDE.md Track A discipline). Connects "
            "PR #1649 observations to "
            "prop:categorical-neutrality-saturated-shells + "
            "conj:diagrammatic-double-magic-lr-fusion + "
            "prop:magic-numbers-from-q + MAG-1 audit."
        ),
        "reference_blocks": [
            "prop:categorical-neutrality-saturated-shells",
            "conj:diagrammatic-double-magic-lr-fusion",
            "prop:magic-numbers-from-q",
            "conj:homological-shell-condensation",
            "docs/audits/2026-05-02-mag1-complete-7-magic-numbers.md",
            "docs/audits/2026-06-01-qbeta-habiro-a6-refutes-refined-scaling-law.md",
            "PR #1625 (level-2 SU(2) Wenzl)",
            "PR #1642 (mass-table Habiro)",
            "PR #1649 (this branch)",
        ],
        # Wrap rows under a dict-typed `data` slot. A bare top-level list
        # for `data` breaks witness_dependency_drift.py, which does
        # `w.get("data", {}).get("upstream_witness_hashes")` (I6 schema
        # drift). See docs/audits/2026-05-16-stale-witness-infra-gap.md.
        "data": {"rows": rows},
        "key_observations": [
            "Active partition count grows with A — cannot explain "
            "non-monotonic mult(Φ_8).",
            "A=6 ⁶He(Z=2) / ⁶Be(N=2): each half has one magic shell.",
            "A=14 ¹⁴O(Z=8) / ¹⁴C(N=8): each half has Z=8 or N=8 magic.",
            "Both anomalous pairs share: 'one magic shell per half'.",
            "A=3, A=5 ALSO have one magic per half (Z=2 or N=2) but "
            "match the refined formula — suggesting valence-nucleon "
            "parity matters: A=3,5 have ODD valence; A=6,14 have EVEN "
            "valence (= paired nucleons coupling to self-conjugate "
            "block).",
            "The categorical mechanism is prop:categorical-neutrality-"
            "saturated-shells: full-twist Δ²_n acts as identity on "
            "Φ_n at magic n, restricting Wedderburn support to "
            "self-conjugates. For pair-differences, ONE HALF hitting "
            "magic restricts that half's support.",
        ],
        "open_next_steps": [
            "LR-fused per-block χ_λ(β_X − β_Y) at q = ζ_8 for each pair "
            "— directly count Wedderburn partitions with non-zero "
            "χ_λ contribution AND first-column ≤ 3.",
            "Compare directly to mult(Φ_8). If exact match, the "
            "shell-closure ↔ Wedderburn freezing hypothesis is "
            "structurally confirmed at the pair-difference level.",
            "Currently blocked on LR-fused per-block character compute "
            "at A ≥ 2 (Rust LR bridge stub per "
            "markov_trace_via_wenzl_lr.py).",
        ],
    }
    wb = WitnessBuilder.wrap_legacy(
        name="per-pair-wedderburn-enumeration",
        payload=payload,
        script_path=__file__,
        engine="python partition enumeration",
        output_dir=HERE,
    )
    wb.save()
    print()
    print(f"  Elapsed: {elapsed:.2f} s")
    print(f"  Witness: per-pair-wedderburn-enumeration.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
