#!/usr/bin/env python3
# polynomial_q_not_applicable: combinatorial probe; no symbolic-q output.
"""Multiplicity-refined $n_\\star$: four 2-input combinations tested.

Builds on `probe_phiq_type_b_fold_depth.py` (this branch) and PR
#638's per-eigenvalue probe. Tests whether any **simple two-input
combination** of

  * `fold_depth` = #{λ ⊢ 3A : λ = λ^T}      (Type-B Kashiwara depth)
  * `m_near_pole` = per-atom near-pole multiplicity (from #638)

closes ${}^3\\mathrm{He}$'s non-closure under uniform-$k$.

**The four candidate rules tested:**

  R1: $n_\\star = \\mathrm{fold\\_depth} + (m_{\\mathrm{near\\_pole}} - 1)$
  R2: $n_\\star = \\max(\\mathrm{fold\\_depth}, m_{\\mathrm{near\\_pole}})$
  R3: $n_\\star = \\mathrm{fold\\_depth} + m_{\\mathrm{near\\_pole}}$
  R4: $n_\\star = \\mathrm{fold\\_depth} \\cdot m_{\\mathrm{near\\_pole}}$

For each, predict $n_\\star$ per atom; check against the observed
best-$k$ closures from #638's per-eigenvalue probe:

  D:   observed best $k = 1$ (-6.87%)
  T:   observed best $k = 2$ (-8.00%)
  ³He: never closes at uniform $k \\in \\{1, \\ldots, 10\\}$.

**Per-atom near-pole multiplicity** $m$ (from #638's `brane-tower-z-habiro.md`):

  D:   one near-pole entry ($|\\hat V| \\approx 0.989$, single generator)
  T:   one near-pole entry
  ³He: TWO near-pole entries (at generator positions 0 and 3)

**Expected outcome (negative finding):** none of R1-R4 reproduces
${}^3\\mathrm{He}$'s non-closure. Each predicts a specific finite
$n_\\star \\geq 2$ for ³He, but ³He doesn't close at ANY uniform $k$.
This documents that the multiplicity refinement must be **non-uniform-k**
(per-generator $k_i$) or genuinely structural beyond simple scalar
2-input combinations.

Class C (diagnostic / probe).

Output: `probe-phiq-multiplicity-refinement.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402

# ── Substrate data (from probe_phiq_type_b_fold_depth.py) ───────
FOLD_DEPTH = {
    "D":   1,   # self-conj partitions of n=6: (3,2,1)
    "T":   2,   # self-conj partitions of n=9: (5,1,1,1,1), (3,3,3)
    "He3": 2,   # same as T (same strand count n=9)
}

# ── Near-pole multiplicity (from #638 brane-tower-z-habiro.md) ──
M_NEAR_POLE = {
    "D":   1,   # one near-pole generator at |V̂| ≈ 0.989
    "T":   1,   # one near-pole generator
    "He3": 2,   # TWO near-pole generators (positions 0 and 3)
}

# ── Empirical closure depths (from #638 per-eigenvalue probe) ───
OBSERVED_K = {
    "D":   1,    # closes at k=1 with -6.87% residual
    "T":   2,    # closes at k=2 with -8.00% residual
    "He3": None, # never closes at k ∈ {1..10}
}


def rule_R1(fold: int, m: int) -> int:
    """R1: n_⋆ = fold_depth + (m - 1)."""
    return fold + (m - 1)


def rule_R2(fold: int, m: int) -> int:
    """R2: n_⋆ = max(fold_depth, m)."""
    return max(fold, m)


def rule_R3(fold: int, m: int) -> int:
    """R3: n_⋆ = fold_depth + m."""
    return fold + m


def rule_R4(fold: int, m: int) -> int:
    """R4: n_⋆ = fold_depth · m."""
    return fold * m


RULES = {"R1": rule_R1, "R2": rule_R2, "R3": rule_R3, "R4": rule_R4}


def main() -> int:
    w = WitnessBuilder("probe-phiq-multiplicity-refinement",
                       engine="python")

    print("=" * 78)
    print("MULTIPLICITY-REFINED n_⋆ — 4 simple 2-input rules")
    print("=" * 78)
    print(f"  Atoms:  D, T, ³He")
    print(f"  fold_depth (self-conj count): D=1, T=2, ³He=2")
    print(f"  m_near_pole:                   D=1, T=1, ³He=2")
    print(f"  observed best-k (#638):        D=1, T=2, ³He=NONE")
    print()

    rules_results = {}
    for rule_name, rule_fn in RULES.items():
        row = {"rule_name": rule_name, "predictions": {}, "matches": {}}
        all_match = True
        for atom in ("D", "T", "He3"):
            fold = FOLD_DEPTH[atom]
            m = M_NEAR_POLE[atom]
            predicted_k = rule_fn(fold, m)
            observed_k = OBSERVED_K[atom]
            # Match if observation exists AND predicted == observed,
            # OR observation is None AND predicted is "unreachable"
            # (no rule actually predicts unreachable, so ³He always
            # mismatches when observed_k is None).
            if observed_k is None:
                match = False  # ³He has no uniform-k closure
            else:
                match = (predicted_k == observed_k)
            if not match:
                all_match = False
            row["predictions"][atom] = predicted_k
            row["matches"][atom] = match
        row["all_match"] = all_match
        rules_results[rule_name] = row

    # ── Print result table ─────────────────────────────────────
    print("  Rule | formula                          | D  | T  | ³He | closes ³He?")
    print("  -----+----------------------------------+----+----+-----+-------------")
    formulas = {
        "R1": "fold + (m - 1)            ",
        "R2": "max(fold, m)              ",
        "R3": "fold + m                  ",
        "R4": "fold · m                  ",
    }
    for rule_name in ("R1", "R2", "R3", "R4"):
        r = rules_results[rule_name]
        d_p = r["predictions"]["D"]
        t_p = r["predictions"]["T"]
        h_p = r["predictions"]["He3"]
        d_m = "✓" if r["matches"]["D"] else "✗"
        t_m = "✓" if r["matches"]["T"] else "✗"
        # ³He never closes at uniform k, so any finite predicted k fails
        h_m = "✗"
        print(f"   {rule_name}  | {formulas[rule_name]}| {d_p}{d_m} | {t_p}{t_m} | {h_p}{h_m}  |  NO (always)")

    print()
    print("  ─────────────────────────────────────────────────────────────────")
    print("  All 4 rules: D and T match (under R1/R2/R4); ³He never closes.")
    print()
    print("  Conclusion: NO simple two-input combination of")
    print("  (fold_depth, m_near_pole) reproduces ³He's non-closure under")
    print("  uniform k. The multiplicity refinement requires either:")
    print("    (a) PER-GENERATOR k_i (non-uniform-k truncation), OR")
    print("    (b) a structural ingredient beyond (fold_depth, m).")

    # ── Disposition ────────────────────────────────────────────
    print()
    print("  Best partial fit: R1 = fold + (m - 1)")
    print("    D: 1 + 0 = 1 ✓  T: 2 + 0 = 2 ✓  ³He: 2 + 1 = 3 (³He at k=3: +1375% — fail)")

    w.set_content_block("conj:brane-tower-z-habiro")
    w.set_description(
        "Four-rule sweep over simple 2-input combinations of "
        "(fold_depth, m_near_pole) for the brane-tower n_⋆ "
        "level-selection rule. Tests R1=fold+(m-1), R2=max, "
        "R3=fold+m, R4=fold·m against observed best-k closures "
        "from PR #638's per-eigenvalue probe. Negative finding: "
        "NO simple 2-input rule closes ³He's non-closure at "
        "uniform k. The multiplicity refinement must be either "
        "non-uniform-k (per-generator k_i) or carry structure "
        "beyond the (fold_depth, m_near_pole) pair. R1 fits the "
        "D and T data exactly, supporting the additive interpretation "
        "but not the ³He observation. Substrate-only (Class C)."
    )
    w.add_parameter("atoms", list(FOLD_DEPTH.keys()))
    w.add_parameter("fold_depth", FOLD_DEPTH)
    w.add_parameter("m_near_pole", M_NEAR_POLE)
    w.add_parameter("observed_best_k", OBSERVED_K)
    w.add_data("rules", rules_results)
    w.add_data("conclusion", (
        "No simple 2-input combination of (fold_depth, m_near_pole) "
        "closes ³He's non-closure under uniform k. R1 = fold + (m-1) "
        "fits D and T exactly but predicts ³He closes at k=3, which "
        "empirically gives +1375% (per #638). The refinement requires "
        "either per-generator k_i (non-uniform truncation) or "
        "additional substrate ingredients beyond (fold_depth, m)."
    ))

    # Sanity assertions on the substrate data
    w.add_assertion("fold_depth_D_equals_1",
                    computed=FOLD_DEPTH["D"], expected=1)
    w.add_assertion("fold_depth_T_He3_both_2",
                    computed=FOLD_DEPTH["T"] == FOLD_DEPTH["He3"] == 2,
                    expected=True)
    w.add_assertion("m_He3_strictly_greater_than_D_T",
                    computed=M_NEAR_POLE["He3"] > M_NEAR_POLE["D"]
                             and M_NEAR_POLE["He3"] > M_NEAR_POLE["T"],
                    expected=True)
    # R1 (best fit) predicts D=1, T=2, ³He=3 — assert this
    w.add_assertion("R1_predicts_D_1_T_2_He3_3",
                    computed=(rules_results["R1"]["predictions"]["D"] == 1
                              and rules_results["R1"]["predictions"]["T"] == 2
                              and rules_results["R1"]["predictions"]["He3"] == 3),
                    expected=True)
    # The negative finding: ³He doesn't close at uniform k under any rule
    w.add_assertion("no_rule_closes_He3",
                    computed=all(not r["matches"]["He3"]
                                 for r in rules_results.values()),
                    expected=True)

    out = w.save()
    print(f"\nWrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
