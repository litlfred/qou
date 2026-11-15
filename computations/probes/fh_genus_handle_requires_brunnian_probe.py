#!/usr/bin/env python3
# polynomial_q_not_applicable: integer linking numbers and a literal source-text
# check; no q enters anywhere.
"""The Freedman-He complement-genus handle is stated FOR BORROMEAN LINKS.

Bean qou-768r, route 2. The Freedman-He link bound as Komendarczyk states it
(arXiv:0808.1533v1 eq. (43), p. 26) is

    E_{3/2}(X) >= (pi/16)^{1/4} (sum_k ac(L_k, L)|Flux(X_k)|) * min_k |Flux(X_k)|

`ac(L_k, L)` is an INFIMUM OVER HOMOTOPIES and so is not directly computable. The
corpus's only route to a number has been the sentence immediately after, which
bounds it below by a smallest genus among surfaces in the complement of the other
components.

THE CORPUS DROPS THAT SENTENCE'S QUALIFIER, AND I DROPPED IT TOO. The source reads

    "the asymptotic crossing numbers ac(Lk, L) FOR BORROMEAN LINKS can be
     estimated below by a smallest genus among surfaces in R^3 \\ {L1 u ... u
     ^Lk u ... u Ln} with a single boundary component"

Beans qou-a9li and qou-b5yi, both completed 2026-09-02, quote the genus clause
without "for borromean links". The literature ledger committed earlier in THIS
tranche (5fadc01398) repeated the elision and then drew the opposite conclusion --
that nonzero linking makes the bound EASIER. It does not; it makes it inapplicable.

WHY THE QUALIFIER MUST BE THERE. A compact oriented surface S in R^3 \\ L_j with
boundary L_k forces lk(L_k, L_j) = 0, since [L_k] = [dS] = 0 in H_1(R^3 \\ L_j) = Z
and that class IS the linking number. So where some lk != 0 the surfaces being
minimised over do not exist: off the Brunnian class the estimate is ill-posed --
an infimum over the empty set -- rather than merely weaker.

WHAT THIS PROBE MEASURES. For the derived carrier -- the closure of the canonical
atom braid word -- how many components have ALL their pairwise linking numbers
vanishing, i.e. satisfy the hypothesis the handle needs. The answer is ZERO, on
every isotope tested and in BOTH crossing-resolution branches.

Hence the handle is available at no component of the derived carrier, while the one
carrier in this arc where it IS available is the Borromean L6a4 -- the census
assignment that owner ruling 2026-08-29 retired as a fit.

Two things this does NOT establish, stated so no restatement drifts stronger:
eq. (43) is untouched and remains a true lower bound; and `ac(L_k, L)` itself is
untouched -- nothing here says it is small or zero, only that this particular
handle on it is unavailable here.

Companion Lean: QOU/Mass/FreedmanHeGenusHandleNeedsVanishingLinking.lean
(lean-direct exit 0, sorry-free). EXPLORATORY; nothing wired.
"""

from __future__ import annotations

import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401,E402
from witness_base import WitnessBuilder  # noqa: E402

# Reuses the sibling probe's `linking`, rather than reimplementing it. Stated
# because a probe depending on a probe is worth noticing: the alternative is a
# second copy of the closure/permutation logic, and two copies drifting apart is
# the more expensive failure. That module runs nothing at import.
from atom_closure_milnor_indeterminacy_probe import linking  # noqa: E402

SOURCE = (REPO / "library" / "arxiv-0808.1533v1" / "sections"
          / "sec-001-energy-bound.md")

ISOTOPES = [(1, 1, "2H"), (1, 2, "3H"), (2, 1, "3He"),
            (2, 2, "4He"), (3, 3, "6Li"), (4, 4, "8Be")]

# +1 resolves every averaged letter to sigma, -1 to sigma^-1. Both are checked:
# `lk` is branch-dependent (unlike the component count), so a result read off one
# branch would not be a result about the carrier.
BRANCHES = [(+1, "sigma"), (-1, "sigma^-1")]


def qualifier_is_in_the_source() -> dict:
    """Live check that the genus sentence carries 'borromean'.

    Asserted from the file rather than quoted from memory, so that if the held
    text is ever re-ingested differently the assertion fails loudly instead of
    this probe resting on a remembered reading.
    """
    text = SOURCE.read_text(errors="ignore")
    # The sentence runs across OCR line breaks; normalise whitespace first.
    flat = re.sub(r"\s+", " ", text)
    m = re.search(r"asymptotic crossing numbers.{0,120}?estimated below", flat,
                  re.IGNORECASE | re.DOTALL)
    sentence = m.group(0) if m else ""
    return {
        "found": bool(m),
        "sentence": sentence,
        "has_borromean_qualifier": "borromean" in sentence.lower(),
    }


def brunnian_components(Z: int, N: int, avg_sign: int) -> tuple[int, int, int]:
    """(components, components whose pairwise linking ALL vanishes, linked pairs)."""
    mu, lk = linking(Z, N, avg_sign)
    unlinked = 0
    for k in range(mu):
        total = sum(abs(lk.get(tuple(sorted((k, j))), 0))
                    for j in range(mu) if j != k)
        if total == 0:
            unlinked += 1
    linked_pairs = sum(1 for v in lk.values() if v != 0)
    return mu, unlinked, linked_pairs


def main() -> int:
    q = qualifier_is_in_the_source()

    rows = []
    total_components = 0
    total_unlinked = 0
    for (Z, N, name) in ISOTOPES:
        for sign, tag in BRANCHES:
            mu, unlinked, linked_pairs = brunnian_components(Z, N, sign)
            total_components += mu
            total_unlinked += unlinked
            rows.append({
                "isotope": name, "A": Z + N, "branch": tag,
                "components_mu": mu,
                "components_with_all_linking_zero": unlinked,
                "linked_pairs": linked_pairs,
            })

    b = WitnessBuilder(
        name="fh-genus-handle-requires-brunnian",
        _script_path=pathlib.Path(__file__),
        output_dir=HERE,
    )
    b.set_audit_only("docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md")
    b.set_description(
        "EXPLORATORY. The Freedman-He complement-genus lower bound on ac(L_k, L) is "
        "stated in Komendarczyk (arXiv:0808.1533v1, sec-001-energy-bound.md:216-217) "
        "FOR BORROMEAN LINKS -- a qualifier the corpus drops (qou-a9li, qou-b5yi) and "
        "which this tranche's own earlier literature ledger dropped before drawing the "
        "OPPOSITE conclusion. It is load-bearing: a surface in the complement bounding "
        "L_k forces lk(L_k, L_j) = 0 by complement homology, so off the Brunnian class "
        "the infimum is over an EMPTY set and the estimate is ill-posed, not merely "
        "weaker. Measured on the derived carrier (the canonical atom-word closure): "
        "ZERO of its components have all-vanishing pairwise linking, on every isotope "
        "and in BOTH crossing-resolution branches. So the handle applies at no "
        "component here -- while the one carrier where it does apply is the Borromean "
        "L6a4, the census assignment retired as a fit by the 2026-08-29 owner ruling. "
        "Scope (b) on the HANDLE, with the invariant cited; eq. (43) and ac(L_k, L) "
        "themselves are untouched. Nothing wired."
    )

    b.add_data("the_dropped_qualifier", {
        "source": "library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md:216-217",
        "sentence_as_held": q["sentence"],
        "corpus_records_that_drop_it": ["qou-a9li", "qou-b5yi",
                                        "docs/audits/2026-09-04-carrier-derivation-held-literature-ledger.md (this tranche, corrected)"],
        "why_it_is_load_bearing": (
            "a compact oriented S in R^3 \\ L_j with dS = L_k forces lk(L_k,L_j) = 0, "
            "since [L_k] = [dS] = 0 in H_1(R^3 \\ L_j) = Z and that class IS the "
            "linking number. Where some lk != 0 the minimised-over set is EMPTY."),
    })
    b.add_data("measured_on_the_derived_carrier", {
        "carrier": ("closure of the canonical atom braid word; a connected sum of "
                    "(2,k) torus links, verified 32/32 in SnapPy "
                    "(docs/audits/2026-08-25-atom-word-closures-are-not-hyperbolic.md)"),
        "rows": rows,
        "totals": {"components": total_components,
                   "components_with_all_linking_zero": total_unlinked},
        "reading": ("not one component anywhere satisfies the handle's hypothesis, and "
                    "this holds in both branches -- so it is not an artifact of how the "
                    "superposition letters were resolved"),
    })
    b.add_data("the_inversion", {
        "handle_applies_to": "Borromean links -- in this arc, L6a4 (the A=3 carrier)",
        "L6a4_provenance": ("the CENSUS assignment, admitted AME-driven "
                            "(jsj_verification.py), retired by owner ruling 2026-08-29"),
        "handle_applies_to_derived_carrier": False,
        "consequence": ("the only carrier on which route 2's computable handle works is "
                        "the one that was retired as a fit; on the derived carrier it "
                        "does not apply at all"),
    })
    b.add_data("what_this_does_NOT_establish", {
        "eq_43": "untouched -- it remains a true lower bound",
        "ac_itself": ("untouched -- nothing here says ac(L_k, L) is small or zero, only "
                      "that the complement-genus handle on it is unavailable here"),
        "other_handles": ("a different lower bound on ac, not routed through a "
                          "complement genus, is not excluded and is not examined"),
        "scope": "(b) on the handle, invariant cited (complement homology)",
    })

    b.add_assertion(
        name="source_sentence_carries_the_borromean_qualifier",
        computed="1" if (q["found"] and q["has_borromean_qualifier"]) else "0",
        expected="1", tolerance="0", unit="bool",
        source=("live read of the held text, so a re-ingestion that changed the sentence "
                "would fail this rather than leave the probe resting on a remembered "
                "reading"),
    )
    b.add_assertion(
        name="components_of_the_derived_carrier_satisfying_the_handles_hypothesis",
        computed=str(total_unlinked), expected="0", tolerance="0", unit="components",
        source=("THE RESULT. Summed over 6 isotopes x 2 branches = "
                f"{total_components} components. Not one has all its pairwise linking "
                "numbers vanishing, so the Borromean hypothesis fails everywhere."),
    )
    b.add_assertion(
        name="result_holds_in_both_crossing_resolution_branches",
        computed=str(sum(1 for r in rows
                         if r["components_with_all_linking_zero"] == 0)),
        expected=str(len(rows)), tolerance="0", unit="rows",
        source=("lk is branch-DEPENDENT (unlike the component count), so a figure read "
                "off one branch would not be a statement about the carrier. Checked in "
                "both."),
    )
    b.add_assertion(
        name="every_isotope_has_exactly_A_linked_pairs",
        computed=str(sum(1 for r in rows if r["linked_pairs"] == r["A"])),
        expected=str(len(rows)), tolerance="0", unit="rows",
        source=("cross-check that the carrier really is the measured path: mu - 1 = A "
                "linked consecutive pairs. If this ever fails the shape assumption "
                "behind the Lean's PathLinking has changed and the result needs re-deriving."),
    )

    # `independent`, with a reason rather than a bare token: this probe reads no
    # q₀ on any path. Its inputs are integer linking numbers of a braid closure
    # (permutation + crossing-sign arithmetic) and a literal string search of a
    # held source file. Nothing in the import cone evaluates a substrate pin, so
    # there is no `q0Value` to record and recording one would be a contradiction.
    #
    # Declared because the q0-anchor refill ratchet counts an undeclared witness
    # as NEW-unstamped, and an undeclared one is indistinguishable from a
    # producer that simply forgot. Measured: with this omitted the ratchet's
    # "NEW (not in baseline)" went 40 -> 41 on this branch, which is how the
    # omission was caught -- by A/B-ing the gate with the file removed, NOT by
    # grepping the log for the filename, which reports only a `skipped:` line
    # and misses it entirely.
    out = b.save({
        "q0Anchor": "independent",
        "q0AnchorReason": (
            "reads no q0 anywhere. Inputs are integer linking numbers of the "
            "canonical atom-word closure (permutation and crossing-sign "
            "arithmetic, exact integers) and a literal text search of "
            "library/arxiv-0808.1533v1/sections/sec-005-energy-bound.md. No "
            "substrate pin is evaluated on any path, so no q0Value exists."
        ),
    })
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
