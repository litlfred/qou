#!/usr/bin/env python3
"""
Per-atom intrinsic grading bound ℓ(K, q) witness emitter.

L1 (PR #565 audit § 7): emits per-atom ℓ(K, q) — the top non-zero
ℤ-grading degree of an atomic braid's KLR-module lift, equivalent
to the max GS-filtration grade observed during reduction of its
canonical braid word.

Per `prop:jet-prefix-gb-filtration` (main, PR #571):

  ℓ(K, q) := max { ℓ : σ_ℓ(T_w) ≠ 0 in J^ℓ / J^{ℓ+1} }

is the structural grading bound, distinct from the truncation
cutoff k used in jet-prefix prefix construction.  Truncating at
k ≥ ℓ(K, q) is exact; truncating at k < ℓ(K, q) leaves a
homological remainder.

Downstream consumer: #564's P6 (Rust SDP wiring of the
joint-tower-sdp solver) keys variable filtering by this bound,
not by the user-supplied cutoff k.

Atomic braid words used here are the simple-Coxeter forms of
the canonical p/n/D/T/³He/⁴He nuclear braids; they coincide
with the topological braid-group skeleton of the (c, d)-pair
braids in `mass_at_3A_proper.atom_braid_word_3A` once the
energy-coefficient layer is collapsed.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from gb_filtration_jet_tracker import HeckeElement  # noqa: E402


# ── Canonical topological braid words ────────────────────────────────
#
# Each entry: (label, n, word, atom_letter, A, Z, N).
# `word` is a list of ints; positive = T_i, negative = T_i^{-1}.
# Indexing matches gb_filtration_jet_tracker (1-indexed generators).
ATOMS = [
    # Single nucleons (H_3 = 3-strand)
    ("p (proton)",       3, [1,  2, -1],         "p",   1, 1, 0),
    ("n (neutron)",      3, [1, -2,  1],         "n",   1, 0, 1),
    # Disjoint two-nucleon (H_6 = two H_3 clusters)
    ("D (deuteron disj)",  6, [1, 2, -1, 4, -5, 4],  "D", 2, 1, 1),
    # Three-nucleon (H_9): pp ⊗ n  for ³He, p ⊗ nn for ³H
    ("³He disjoint",     9, [1, 2, -1, 4, 5, -4, 7, -8, 7],   "3He", 3, 2, 1),
    ("³H (T) disjoint",  9, [1, 2, -1, 4, -5, 4, 7, -8, 7],   "T",   3, 1, 2),
    # Four-nucleon (H_12): pp ⊗ nn for ⁴He
    ("⁴He disjoint",    12, [1, 2, -1, 4, 5, -4, 7, -8, 7, 10, -11, 10], "4He", 4, 2, 2),
]


def _max_grade(n: int, word: list[int]) -> tuple[int, int]:
    """Return (ℓ(K,q), n_terms_at_ℓ) — top nonzero grade and term count."""
    E = HeckeElement.identity(n)
    for i in word:
        if i > 0:
            E = E.right_mul_T(i)
        else:
            E = E.right_mul_T_inv(-i)
    cert = E.filtration_certificate()
    if not cert:
        return (0, 0)
    grades = sorted(cert.keys())
    top = grades[-1]
    n_terms = len(cert[top])
    return (top, n_terms)


def main() -> int:
    print("Per-atom grading bound ℓ(K, q) — structural max-grade of NF projection\n")
    print(f"  {'atom':<22} {'A':>2} {'n':>2} {'ℓ(K,q)':>7} {'#top-terms':>10}")
    print("  " + "-" * 62)
    rows = []
    for label, n, word, atom, A, Z, N in ATOMS:
        ell, n_top = _max_grade(n, word)
        print(f"  {label:<22} {A:>2} {n:>2} {ell:>7} {n_top:>10}")
        rows.append({
            "atom": atom,
            "label": label,
            "Z": Z, "N": N, "A": A,
            "n_strands": n,
            "topological_word": word,
            "ell_K_q": ell,
            "n_terms_at_top_grade": n_top,
        })
    # Use the fluent WitnessBuilder API (per Gemini review on #581):
    # this is a NEW script, so wrap_legacy is the wrong tool — it's
    # only for migrating existing payload-shaped emitters.
    out = (WitnessBuilder("per-atom-grading-bound", engine="sympy")
        .set_description(
            "Per-atom intrinsic grading bound ℓ(K, q) for the canonical "
            "topological braid words. ℓ(K, q) is the top non-zero "
            "ℤ-grading degree of the KLR-module lift, equivalent to the "
            "max GS-filtration grade observed under "
            "gb_filtration_jet_tracker reduction."
        )
        .add_data("narrative_block", "prop:jet-prefix-gb-filtration")
        .add_data("atoms", rows)
        .add_data("note", (
            "Downstream: #564 P6 (Rust SDP wiring) should key variable "
            "filtering by ell_K_q rather than by a user-supplied cutoff k. "
            "Truncating at k >= ell_K_q is exact; truncating at k < "
            "ell_K_q leaves a homological remainder E(k)."
        ))
        .add_assertion(
            "ell_K_q_proton_eq_3",
            computed=int(rows[0]["ell_K_q"]),
            expected=3,
            tolerance=0,
            source="proton T_1 T_2 T_1^-1: top grade = 3 after Hecke ascent",
        )
        .add_assertion(
            "ell_K_q_monotone_in_A",
            # Per Copilot review: actually test ∀ i,j: A_i ≤ A_j ⟹
            # ℓ_i ≤ ℓ_j. Previous version skipped the neutron row and
            # didn't compare across A levels.
            computed=1.0 if all(
                ri["ell_K_q"] <= rj["ell_K_q"]
                for ri in rows for rj in rows
                if ri["A"] <= rj["A"]
            ) else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="ℓ(K, q) is monotone non-decreasing in atomic mass A",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
