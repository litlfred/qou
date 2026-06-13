#!/usr/bin/env python3
"""GAP-A-4 T16 probe — combinatorial-coincidence observations on (2, 0, −3, −1).

Follow-up to the merged T15 polynomial closed form
χ^{(2,1)}(β_Bor) = 2 − 3·h⁴ − h⁶ (PR #1927).

T16 enumerates a small set of natural counting candidates on the (2,1)
Young diagram and the Borromean braid structure, checks which match the
T15 coefficient 4-tuple (h⁰, h², h⁴, h⁶) = (2, 0, −3, −1), and records
the matches as STRUCTURAL OBSERVATIONS — explicitly NOT as a derivation
attempt.  Per CLAUDE.md `no-7th-ansatz` / formalize-first discipline,
the probe enumerates candidates and reports their matches without
proposing any single one as the answer.

Candidate counts checked at each h-order:

  h⁰ = +2  candidates:
    - d_{(2,1)} (dim of standard S_3 irrep)     = 2  ← already T15
    - #SYT of (2,1)                              = 2
    - #corners of (2,1)                          = 2
    - #removable corners (Young branching)      = 2

  h² = 0  candidates:
    - #non-rim-hooks of size 2 in (2,1)         = ? (computed)
    - #cycle-type contributions from S_3 ∖ id    = ? (sum over non-id)

  h⁴ = −3  candidates:
    - −(#cells of (2,1))                         = −3
    - −(product of hook lengths)                  = −(3·1·1) = −3
    - −(2·#corners − 1)                           = −3
    - −(#components of Borromean rings)           = −3

  h⁶ = −1  candidates:
    - −(#non-trivial hooks > 1)                  = −1 (just the 3)
    - −(1) generic                                = −1
    - content_sum signed (Σ (j − i) over cells of (2,1))

MULTIPLE candidates match — this is INFORMATIVE about the structural
richness of the (2,1) data, but per formalize-first discipline, NO
single combinatorial bijection is proposed as THE derivation.  The
probe records observations as open data; a future probe (T17 or later)
would need to derive WHICH candidate is structural by independent means
(e.g. category-theoretic / topological).

EXPLORATORY — no production code, content blocks, or production
witnesses changed.  Emits `gap-a4-T16-coefficient-counting-probe.witness.json`.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401
del _sys, _Path, _bridge

import mpmath as mp  # noqa: E402,F401 — used for set_compute_dps engine state + assertion floats

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()

from witness_base import WitnessBuilder  # noqa: E402
from _gap_a4_qsafe import Q_0_50DPS  # noqa: E402
from partition_utils import hook_lengths  # noqa: E402

from pathlib import Path  # noqa: E402
from math import factorial as _fact, prod  # noqa: E402

HERE = Path(__file__).resolve().parent


# ── Combinatorial data on (2,1) ───────────────────────────────────


TWO_ONE = (2, 1)


def num_corners(lam: tuple) -> int:
    """Number of corner cells of λ (the cells whose removal yields a
    Young diagram)."""
    rows = list(lam)
    n = len(rows)
    count = 0
    for i in range(n):
        below = rows[i + 1] if i + 1 < n else 0
        if rows[i] > below:
            count += 1
    return count


def num_syt(lam: tuple) -> int:
    """Standard Young Tableaux count = n! / Π hook lengths (hook-length
    formula, Frame-Robinson-Thrall 1954).  Equivalent to d_lambda from
    the murnaghan_nakayama family but kept local since no canonical
    `d_lambda` export exists in the repo's utility modules (Gemini
    review suggested the import; the canonical location does not yet
    provide it)."""
    return _fact(sum(lam)) // prod(hook_lengths(list(lam)))


def content_sum_signed(lam: tuple) -> int:
    """Σ (j − i) over cells (i, j) of λ (1-indexed).  Closed-form O(len(λ))
    via Σ_i λ_i(λ_i − 2i + 1)/2 (Gemini review #1932 optimisation)."""
    return sum(
        row_len * (row_len - 2 * i + 1) // 2
        for i, row_len in enumerate(lam, start=1)
    )


# ── Tests ─────────────────────────────────────────────────────────


def check_h0_candidates() -> dict:
    print("=" * 78)
    print("T16a — h⁰ candidates (target +2)")
    print("=" * 78)
    d_lam = num_syt(TWO_ONE)  # also equals dim_(2,1) = 2
    n_corners = num_corners(TWO_ONE)
    candidates = {
        "d_(2,1) / num_syt": d_lam,
        "num_corners": n_corners,
        "num_removable_corners (= num_corners)": n_corners,
    }
    target = 2
    matches = []
    for name, val in candidates.items():
        match = val == target
        marker = "✓" if match else " "
        print(f"  [{marker}] {name:<40} = {val} (target {target})")
        if match:
            matches.append(name)
    print(f"  {len(matches)} of {len(candidates)} candidates match.")
    return {
        "target": target,
        "candidates": candidates,
        "matching_candidates": matches,
    }


def check_h2_candidates() -> dict:
    print()
    print("=" * 78)
    print("T16b — h² candidates (target 0)")
    print("=" * 78)
    # No h² character correction for (2,1) on β_Bor; T15 established this.
    # Look for counts that vanish.
    candidates = {
        "writhe_of_beta_Bor": 0,  # 3 positive − 3 negative crossings
        "linking_number_components": 0,  # Borromean rings have ln = 0
        "image_in_S_3 minus id": 0,  # β_Bor → id ∈ S_3
    }
    target = 0
    matches = []
    for name, val in candidates.items():
        match = val == target
        marker = "✓" if match else " "
        print(f"  [{marker}] {name:<40} = {val} (target {target})")
        if match:
            matches.append(name)
    print(f"  {len(matches)} of {len(candidates)} candidates match.")
    print(f"  (h² = 0 is over-determined — multiple natural sources)")
    return {
        "target": target,
        "candidates": candidates,
        "matching_candidates": matches,
    }


def check_h4_candidates() -> dict:
    print()
    print("=" * 78)
    print("T16c — h⁴ candidates (target −3)")
    print("=" * 78)
    n_cells = sum(TWO_ONE)
    hook_product = prod(hook_lengths(list(TWO_ONE)))
    n_corners = num_corners(TWO_ONE)
    n_borromean_components = 3
    candidates = {
        "−num_cells_of_(2,1)": -n_cells,
        "−hook_product_of_(2,1)": -hook_product,
        "−(2·num_corners − 1)": -(2 * n_corners - 1),
        "−num_components_of_Borromean": -n_borromean_components,
    }
    target = -3
    matches = []
    for name, val in candidates.items():
        match = val == target
        marker = "✓" if match else " "
        print(f"  [{marker}] {name:<40} = {val} (target {target})")
        if match:
            matches.append(name)
    print(f"  {len(matches)} of {len(candidates)} candidates match.")
    print(f"  (h⁴ = −3 has MULTIPLE coincidence-level matches — informative")
    print(f"  but NOT proposed as a derivation per no-7th-ansatz discipline.)")
    return {
        "target": target,
        "candidates": candidates,
        "matching_candidates": matches,
    }


def check_h6_candidates() -> dict:
    print()
    print("=" * 78)
    print("T16d — h⁶ candidates (target −1)")
    print("=" * 78)
    hooks = hook_lengths(list(TWO_ONE))
    n_non_trivial_hooks = sum(1 for h in hooks if h > 1)
    content_sum = content_sum_signed(TWO_ONE)
    candidates = {
        "−num_non_trivial_hooks (h > 1)": -n_non_trivial_hooks,
        "content_sum_signed": content_sum,
        "−1 generic": -1,
    }
    target = -1
    matches = []
    for name, val in candidates.items():
        match = val == target
        marker = "✓" if match else " "
        print(f"  [{marker}] {name:<40} = {val} (target {target})")
        if match:
            matches.append(name)
    print(f"  {len(matches)} of {len(candidates)} candidates match.")
    return {
        "target": target,
        "candidates": candidates,
        "matching_candidates": matches,
    }


# ── main ─────────────────────────────────────────────────────────


def main():
    w = WitnessBuilder("gap-a4-T16-coefficient-counting-probe",
                       engine="mpmath")
    w.set_audit_only(
        "docs/audits/2026-06-06-gap-a4-T9-T14-followup-retrospective.md"
    )
    w.set_description(
        "GAP-A-4 T16 — enumerate combinatorial counting candidates on "
        "the (2,1) Young diagram + Borromean braid that match the T15 "
        "coefficient 4-tuple (h⁰, h², h⁴, h⁶) = (2, 0, −3, −1). "
        "Records matches as OBSERVATIONS — no derivation claimed per "
        "no-7th-ansatz discipline."
    )

    w.add_parameter("q_0_50dps", Q_0_50DPS)
    w.add_data("discipline", "EXPLORATORY-OBSERVATIONS")
    w.add_data("production_wired", False)

    h0 = check_h0_candidates()
    h2 = check_h2_candidates()
    h4 = check_h4_candidates()
    h6 = check_h6_candidates()

    w.add_data("h0_candidates", h0)
    w.add_data("h2_candidates", h2)
    w.add_data("h4_candidates", h4)
    w.add_data("h6_candidates", h6)

    # Sanity assertions
    w.add_assertion(
        "num_syt_of_2_1_equals_dim",
        computed=float(num_syt(TWO_ONE)),
        expected=2.0,
        tolerance=0.0,
        source=(
            "Standard Young Tableaux of shape (2,1): there are exactly 2 "
            "(filling the 3 cells with 1, 2, 3 such that rows + columns "
            "increase).  Equals dim of (2,1) irrep of S_3 by hook-length "
            "formula 3!/3·1·1 = 2."
        ),
    )
    w.add_assertion(
        "num_corners_of_2_1_equals_2",
        computed=float(num_corners(TWO_ONE)),
        expected=2.0,
        tolerance=0.0,
        source=(
            "Corners of (2,1): cells (1,2) and (2,1) are both removable "
            "(removing either yields a valid Young diagram)."
        ),
    )
    w.add_assertion(
        "hook_product_equals_3",
        computed=float(prod(hook_lengths(list(TWO_ONE)))),
        expected=3.0,
        tolerance=0.0,
        source=(
            "Hook lengths of (2,1): {3, 1, 1}; product = 3·1·1 = 3."
        ),
    )

    total_matches = (
        len(h0["matching_candidates"])
        + len(h2["matching_candidates"])
        + len(h4["matching_candidates"])
        + len(h6["matching_candidates"])
    )

    synthesis = (
        "T16 enumerates natural combinatorial counts on the (2,1) Young "
        "diagram and the Borromean braid that match the T15 coefficient "
        "triple (2, 0, −3, −1).  Multiple candidates match at each "
        "h-order: "
        f"{len(h0['matching_candidates'])} at h⁰, "
        f"{len(h2['matching_candidates'])} at h², "
        f"{len(h4['matching_candidates'])} at h⁴, "
        f"{len(h6['matching_candidates'])} at h⁶ "
        f"(total {total_matches} match events).  The over-determination "
        "at each order is STRUCTURALLY INFORMATIVE — the coefficient "
        "triple sits at the intersection of multiple natural counting "
        "principles (dim/SYT, corner count, hook product, Borromean "
        "component count, writhe).  This is EXPECTED for a combinatorially "
        "rich object; it does NOT distinguish which candidate is the "
        "structural derivation.  Per no-7th-ansatz discipline, NO single "
        "combinatorial bijection is proposed as THE derivation — the "
        "probe records the candidates as open observations for a future "
        "category-theoretic / topological distinguisher to select among "
        "(e.g. via the Schur-Weyl projector in V_{1/2}^⊗3, the Kauffman "
        "bracket state-sum on β_Bor, or a topological-quantum-field-theory "
        "interpretation).  The Borromean h⁴ = −3/4 obstruction stays OPEN."
    )
    w.add_data("synthesis_verdict", synthesis)
    w.add_data("total_match_events", total_matches)

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
