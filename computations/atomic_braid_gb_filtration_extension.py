#!/usr/bin/env python3
"""atomic_braid_gb_filtration_extension.py — v3 #5

**LEGACY CONVENTION.**  The `ATOMIC_BRAIDS` registry below uses the
bare-int format `[1, 2, -1, ...]` (positive = σ_g, negative = σ_g⁻¹)
because `gb_filtration_jet_tracker.reduce_braid` only accepts that
shape.  The canonical operator-valued convention from
`canonical_braid_crossings.atom_canonical_crossings(Z, N)` adds
**averaged** crossings I = σ − (h/2)·1 that the GB-filtration
tracker cannot currently process; migrating this script to canonical
requires extending the tracker to handle averaged crossings (open
research item, see `docs/audits/canonical-convention-migration-plan.md`).

Per `2026-05-09-refocused-1ppb-workplan-v3.md` §3 item #5:

  "gb_filtration_jet_tracker.py extension to H_n for n ≥ 4 — the
   existing infrastructure handles H_3; extending to higher n
   unlocks the 4He / 6Li / etc. atomic-knot canonical forms
   required for the magic-A integration."

The existing `gb_filtration_jet_tracker` test cases stop at n = 3
(electron, proton/neutron body, figure-8, deuteron, tritium, longest
H_3 element). This extension runs the same tracker on the disjoint-
cluster atomic-braid words for D, ³He, ³H, ⁴He at n ∈ {6, 9, 9, 12},
emitting:

- per-atom filtration certificate (grade → list of (perm, coeff))
- per-atom max grade ℓ(K, q)
- per-atom reduction-step count
- structured witness for downstream magic-A integration

This is the multi-nucleon counterpart of the existing H_3 cases.
The tracker class itself is already parameterized by n; this script
only feeds it the canonical disjoint braid words.

Ref: [manuscript] prop:jet-prefix-gb-filtration
Ref: [manuscript] prop:atomic-mass-gb-nf
Ref: [manuscript] thm:wedderburn-mass-formula
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402
from gb_filtration_jet_tracker import (  # noqa: E402
    HeckeElement, perm_to_canonical_word,
)


# ── Canonical disjoint atomic braid words ────────────────────────────
# Each entry: (label, n, word, atom, A, Z, N).
# `word` is a list of ints; positive = T_i, negative = T_i^{-1}.
# Indexing matches the tracker (1-indexed generators).
ATOMIC_BRAIDS = [
    ("deuteron disjoint H_6 (D)",       6,  [1, 2, -1, 4, -5, 4],          "D",   2, 1, 1),
    ("³He disjoint H_9",                9,  [1, 2, -1, 4, 5, -4, 7, -8, 7], "3He", 3, 2, 1),
    ("tritium disjoint H_9 (³H, T)",    9,  [1, 2, -1, 4, -5, 4, 7, -8, 7], "T",   3, 1, 2),
    ("⁴He disjoint H_12",              12,  [1, 2, -1, 4, 5, -4, 7, -8, 7,
                                             10, -11, 10],                 "4He", 4, 2, 2),
]


def _reduce_and_summarize(name: str, n: int, word: list[int]) -> dict:
    """Run tracker on a braid word; return summary dict.

    Per Copilot review on #585: emit the actual filtration certificate
    (grade → list of (perm, canonical_word, coefficient)), not just
    the term counts. Downstream magic-A consumers need the cert.
    """
    E = HeckeElement.identity(n)
    for i in word:
        if i > 0:
            E = E.right_mul_T(i)
        else:
            E = E.right_mul_T_inv(-i)
    cert = E.filtration_certificate()
    grades = sorted(cert.keys())
    top = grades[-1] if grades else 0
    grade_term_counts = {int(g): len(cert[g]) for g in grades}
    # Structured certificate: per-grade list of {perm, canonical_word,
    # coefficient_str}. Coefficients are sympy expressions; stringify
    # for JSON.
    structured_cert = {}
    for g in grades:
        rows = []
        for w, c in sorted(cert[g]):
            cw = perm_to_canonical_word(w)
            rows.append({
                "perm": list(w),
                "canonical_word": list(cw),
                "coefficient": str(c),
            })
        structured_cert[str(int(g))] = rows
    return {
        "name": name,
        "n": n,
        "word": word,
        "ell_K_q": int(top),
        "n_terms_total": sum(grade_term_counts.values()),
        "grade_term_counts": grade_term_counts,
        "filtration_certificate": structured_cert,
        "n_jet_events": len(E.jet_log),
        "n_steps_total": E.step_counter,
    }


def main() -> int:
    print("Atomic-braid GS-filtration extension — H_n for n ∈ {6, 9, 12}\n")
    print(f"  {'atom':<8} {'A':>2} {'n':>2} {'ℓ(K,q)':>7} "
          f"{'#terms':>7} {'#steps':>7} {'#events':>8}")
    print("  " + "-" * 60)
    cases = []
    for label, n, word, atom, A, Z, N in ATOMIC_BRAIDS:
        s = _reduce_and_summarize(label, n, word)
        s["atom"] = atom
        s["A"] = A
        s["Z"] = Z
        s["N"] = N
        cases.append(s)
        print(f"  {atom:<8} {A:>2} {n:>2} {s['ell_K_q']:>7} "
              f"{s['n_terms_total']:>7} {s['n_steps_total']:>7} "
              f"{s['n_jet_events']:>8}")
    out = (WitnessBuilder("atomic-braid-gb-filtration-extension", engine="sympy")
        .set_audit_only("docs/audits/2026-05-09-refocused-1ppb-workplan-v3.md")
        .set_description(
            "v3 #5: gb_filtration_jet_tracker extension to atomic "
            "braid words at n ∈ {6, 9, 12}. Per-atom filtration "
            "certificate + max-grade ℓ(K, q) + reduction-step "
            "counts. Multi-nucleon counterpart of the existing H_3 "
            "test cases on main."
        )
        .add_data("narrative_block", "prop:jet-prefix-gb-filtration")
        .add_data("downstream_consumers", [
            "prop:atomic-mass-gb-nf",
            "thm:wedderburn-mass-formula",
        ])
        .add_data("atoms", cases)
        .add_assertion(
            "ell_K_q_eq_n_strands_disjoint",
            computed=1.0 if all(s["ell_K_q"] == s["n"] for s in cases) else 0.0,
            expected=1.0,
            tolerance=0.0,
            source=("disjoint-cluster braid words satisfy "
                    "ℓ(K, q) = n_strands per crystal-grading "
                    "argument (per_atom_grading_bound observation)"),
        )
        .add_assertion(
            "monotone_steps_in_strictly_larger_A",
            # Compare only across STRICTLY larger A. Equal-A atoms
            # (³He vs T) differ in their braid words and have
            # different step counts; that's not a monotonicity
            # violation, just data spread within an isobar.
            computed=1.0 if all(
                cases[i]["n_steps_total"] <= cases[j]["n_steps_total"]
                for i in range(len(cases)) for j in range(len(cases))
                if cases[i]["A"] < cases[j]["A"]
            ) else 0.0,
            expected=1.0,
            tolerance=0.0,
            source="step count weakly increases when A strictly increases",
        )
        .save())
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
