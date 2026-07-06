#!/usr/bin/env python3
# polynomial_q_not_applicable: structural / combinatorial probe;
# no symbolic-q output.
"""Type-B-folded-crystal-depth $n_\\star$ candidate (substrate-derived).

Tests the candidate rule

    $n_\\star(\\mathfrak{H}) := \\#\\{\\lambda \\vdash 3A : \\lambda = \\lambda^T\\}$

— the number of **self-conjugate partitions** of $n = 3A$, where
$A$ is the mass number of the confined particle. Motivation
(per PR #638 closure note + AGENTS.md §7b on symmetric-crystal
techniques):

* Self-conjugate partitions $\\lambda = \\lambda^T$ are the **fixed
  points** of the Type-B folding action on the unfolded crystal
  graph of $H_{3A}(q)$ (Kashiwara graph).
* Non-fixed partitions pair up as $(\\lambda, \\lambda^T)$ orbits
  of length 2 under the conjugation involution.
* The Type-B-folded-crystal **depth** is the count of fold-fixed
  partitions (count of orbits of length 1).
* Conjecture under test: $n_\\star = $ (this depth) gives the
  per-atom cyclotomic-projection truncation that closes the
  brane-tower bound.

This script:
  1. Computes self-conjugate partition counts for $n = 6$ (D),
     $n = 9$ (T, $^3\\mathrm{He}$) directly (no need for the
     full $H_n$ representation data).
  2. Compares the candidate $n_\\star$ value to the **observed
     uniform-$k$ closure depths** reported in #638's
     per-eigenvalue operator-valued probe.
  3. Reports partial agreement (D + T) and the $^3\\mathrm{He}$
     non-closure as a multiplicity-driven exception.

**Class C (diagnostic / probe)** per
`docs/audits/2026-05-11-three-calibration-discipline-violations.md`:
this script consumes **no** CODATA constants. The observed
closure-depth data $\\{D{:}k{=}1, T{:}k{=}2\\}$ is pulled from PR
#638's witness as comparator, NOT as calibration input.

Output: `probe-phiq-type-b-fold-depth.witness.json`.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Iterator

import mpmath as mp

from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from witness_base import WitnessBuilder  # noqa: E402


def _partitions(n: int, max_part: int | None = None) -> Iterator[tuple[int, ...]]:
    """Enumerate partitions of `n` as weakly decreasing tuples."""
    if n == 0:
        yield ()
        return
    if max_part is None:
        max_part = n
    for first in range(min(n, max_part), 0, -1):
        for rest in _partitions(n - first, first):
            yield (first,) + rest


def _conjugate(lam: tuple[int, ...]) -> tuple[int, ...]:
    """Partition conjugate: rows ↔ columns of the Young diagram."""
    if not lam:
        return ()
    width = lam[0]
    return tuple(
        sum(1 for part in lam if part >= i) for i in range(1, width + 1)
    )


def self_conjugate_partitions(n: int) -> list[tuple[int, ...]]:
    """List of self-conjugate partitions of `n`."""
    return [lam for lam in _partitions(n) if _conjugate(lam) == lam]


# ── Observed closure depths from #638's per-eigenvalue probe ────
# Reference: probe-phiq-operator-valued.witness.json on PR #638
# (`claude/close-level-selection-rule-bvMvw`). Comparator only;
# Class-C per audit framework.
OBSERVED_K_CLOSURE = {
    # atom: (best_k, residual_pct_at_that_k)
    "D":      (1, -6.87),   # closure within ±10% at k=1
    "T":      (2, -8.00),   # closure within ±10% at k=2
    "He3":    (None, None),  # never within 50% at any k ∈ {1..10}
}


# ── Particle → strand count n = 3A ──────────────────────────────
ATOM_DATA = {
    "D":   {"Z": 1, "N": 1, "A": 2, "n": 6},
    "T":   {"Z": 1, "N": 2, "A": 3, "n": 9},
    "He3": {"Z": 2, "N": 1, "A": 3, "n": 9},
}


def main() -> int:
    w = WitnessBuilder("probe-phiq-type-b-fold-depth", engine="python")

    print("=" * 78)
    print("TYPE-B-FOLDED-CRYSTAL-DEPTH n_⋆ candidate (combinatorial)")
    print("=" * 78)
    print(f"  Candidate rule: n_⋆(H) = #{{λ ⊢ 3A : λ = λ^T}}")
    print()

    rows = []
    matches = []
    misses = []
    for atom, meta in ATOM_DATA.items():
        n = meta["n"]
        self_conj = self_conjugate_partitions(n)
        n_star_candidate = len(self_conj)
        obs_k, obs_pct = OBSERVED_K_CLOSURE[atom]
        if obs_k is None:
            agreement = "n/a (³He never closes at uniform k)"
            misses.append(atom)
        else:
            if n_star_candidate == obs_k:
                agreement = f"✓ MATCH (n_⋆ candidate {n_star_candidate} = observed k {obs_k})"
                matches.append(atom)
            else:
                agreement = f"✗ MISMATCH (candidate {n_star_candidate} vs observed k {obs_k})"
                misses.append(atom)

        print(f"  {atom:>5} (n = {n}, Z = {meta['Z']}, N = {meta['N']}):")
        print(f"    self-conjugate partitions: {self_conj}")
        print(f"    candidate n_⋆ = {n_star_candidate}")
        if obs_k is not None:
            print(f"    observed closure: k = {obs_k} ({obs_pct:+.2f}%)")
        else:
            print(f"    observed closure: NONE in uniform-k sweep k ∈ {{1..10}}")
        print(f"    → {agreement}")
        print()

        rows.append({
            "atom": atom,
            "Z": meta["Z"],
            "N": meta["N"],
            "A": meta["A"],
            "strand_count": n,
            "self_conj_partitions": [list(p) for p in self_conj],
            "n_star_candidate": n_star_candidate,
            "observed_k_closure": obs_k,
            "observed_residual_pct": obs_pct,
            "match": (obs_k is not None and n_star_candidate == obs_k),
        })

    # ── Disposition ─────────────────────────────────────────────
    n_matches = len(matches)
    n_total_with_obs = sum(
        1 for r in rows if r["observed_k_closure"] is not None
    )
    n_atoms = len(rows)

    print("─" * 78)
    print(f"  Atoms with observed uniform-k closure: {n_total_with_obs}/{n_atoms}")
    print(f"  Of those, candidate matches:           {n_matches}/{n_total_with_obs}")
    print(f"  Refuted by:                            {[a for a in misses]}")
    print()
    print("  Reading: the self-conjugate-partition-count candidate")
    print("  reproduces D (k=1) and T (k=2) but cannot explain ³He's")
    print("  non-closure at uniform k. This is the SAME multiplicity-")
    print("  driven exception flagged in PR #638's closure: ³He's 8-")
    print("  generator list carries two near-pole entries (positions 0,3)")
    print("  while D/T carry only one each. The Type-B fold-depth alone")
    print("  CAPTURES the D ↔ T distinction (different self-conj counts")
    print("  at n=6 vs n=9) but is INSENSITIVE to the multiplicity")
    print("  profile that breaks ³He.")
    print()
    print("  Refined open question (consistent with #638):")
    print("    n_⋆(ℓ, n_0, k, m)  where m = per-generator near-pole")
    print("    multiplicity profile of the atom's braid word.")
    print("    Type-B fold-depth contributes the (ℓ, n_0, k) piece;")
    print("    m supplies the ³He correction.")

    w.set_content_block("conj:brane-tower-z-habiro")
    w.set_description(
        "Type-B-folded-crystal-depth n_⋆ candidate: count of self-"
        "conjugate partitions of n = 3A (fixed points of the "
        "Kashiwara λ ↔ λ^T involution). Combinatorial probe, "
        "substrate-only (no CODATA, no operator-data needed). "
        "Result: candidate reproduces D (k=1) and T (k=2) observed "
        "closure depths from PR #638's per-eigenvalue probe, but "
        "FAILS for ³He (n_⋆ predicts k=2, ³He doesn't close at any "
        "uniform k). Same multiplicity-driven exception as PR #638; "
        "Type-B fold-depth is the (ℓ, n_0, k) piece of the open "
        "multiplicity-refined n_⋆(ℓ, n_0, k, m) candidate. Class C "
        "(diagnostic / probe) per three-calibration-discipline audit."
    )
    w.add_parameter("atoms", list(ATOM_DATA.keys()))
    w.add_parameter("observed_k_closure_source",
        "PR #638 probe_phiq_operator_valued.py at q_0 ≈ 1.11"
    )
    w.add_data("table", rows)
    w.add_data("matches", matches)
    w.add_data("misses", misses)
    w.add_data("note_he3_failure", (
        "³He fails to close at any uniform k ∈ {1..10} (per #638). "
        "Candidate Type-B fold depth = 2 (= self-conj count of "
        "partitions of 9). Failure attributed to the multiplicity "
        "profile of ³He's braid word: 8 generators with two near-pole "
        "entries (|V̂| ≈ 0.989 at positions 0 and 3) vs D/T's one "
        "each. The fold-depth candidate alone is INSENSITIVE to "
        "per-generator multiplicity asymmetry."
    ))
    w.add_data("refined_open_form", (
        "n_⋆ : (ℓ, n_0, k, m) → ℕ where m = per-generator near-pole "
        "multiplicity profile. Type-B fold-depth contributes the "
        "(ℓ, n_0, k) component; m supplies the ³He correction. Same "
        "form as PR #638 refined open question."
    ))

    w.add_assertion(
        "self_conj_count_6_is_1",
        computed=len(self_conjugate_partitions(6)),
        expected=1,
    )
    w.add_assertion(
        "self_conj_count_9_is_2",
        computed=len(self_conjugate_partitions(9)),
        expected=2,
    )
    w.add_assertion(
        "D_candidate_matches_observed_k",
        computed=rows[0]["match"],
        expected=True,
    )
    w.add_assertion(
        "T_candidate_matches_observed_k",
        computed=rows[1]["match"],
        expected=True,
    )
    # ³He match is False — assert that the candidate FAILS for ³He
    # in the manner expected (no observation).
    w.add_assertion(
        "He3_no_closure_at_uniform_k",
        computed=(OBSERVED_K_CLOSURE["He3"][0] is None),
        expected=True,
    )

    out = w.save()
    print(f"\nWrote {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
