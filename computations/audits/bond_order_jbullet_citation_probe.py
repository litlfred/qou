#!/usr/bin/env python3
"""`conj:bond-order-eq-jet-degree` names one filtration and cites a block that names another.

Bean `qou-5jqv`.  One hop downstream of `qou-sw8n` (2026-09-14), which
established that `prop:gb-spectral-sequence` names a FOURTH reading of the
symbol `J^•` -- the energy-indexed confinement filtration of
`def:confinement-level`, alongside the three that `2026-08-16-three-gb-
filtrations-one-name.md` tabulated.  This probe identifies that block's first
CONSUMER, and measures that the consumer reads `J^•` the other way.

WHAT IS MEASURED, in one sentence.  `conj:bond-order-eq-jet-degree` opens by
equipping `H_{3A}(q)` with "the Gröbner--Shirshov filtration by Coxeter length
ℓ(w)" and attributes that to `prop:gb-spectral-sequence`; that proposition's
own text says the filtration is "the confinement filtration J^•(q)" and never
mentions Coxeter length, indexing its strata `J^ℓ` by PARTITION ENERGIES
`E_ℓ(q₀)` instead.  Same glyph `ℓ`, two different things -- a Coxeter length in
the citing block, a partition index in the cited one.

🛑 WHY THIS IS NOT A ONE-LINE DOC FIX, and the reason is the Lean.  The
formalisation sides with the CITING block.  `QOU.Knot.BodyOrderExpansion`
(sorry-free) states in its own words that applying its factorisation to the
atomic braid "needs the index set of `H_{3A}`'s normal forms to BE such a
product -- i.e. that Coxeter length is additive over the Young subgroup
`S_3 × ⋯ × S_3`", and discharges exactly that via
`QOU.Knot.BlockLengthAdditive`.  So the Coxeter reading is not a stray link in
one sentence of prose: it is the reading the whole Lean cone is built on.
Retargeting the citation would put the prose in agreement with the cited
proposition and in DISAGREEMENT with the Lean.  Which of the two moves is
correct is a decision with real blast radius and is NOT taken here.

🛑 THE PRIOR RECORD ASSERTS THE OPPOSITE, which is the part worth reading.
`docs/audits/2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md` §4 draws
this exact dependency edge and then concludes the identification "is stated in
terms of the SAME J^• that has three excluded readings".  `same` is precisely
what is measured here to be false.  So this is not a gap in the record; it is
a claim in the record pointing the wrong way, which is why a topic-grep for
prior art comes back reassuring.

WHY EVERY EXISTING DETECTOR MISSED IT.  Three independent reasons, all
measured below, and none of them is "nobody looked":

  1. The `da-citation-misuse` criterion -- the one built for exactly this --
     RAN on this block and returned `pass` with ZERO findings.  Its note is
     content-free filler and is stamped `[EXPIRED-NO-FIELD-HASH]`.
  2. The whole `wpdb` / 08-16 / 08-26 audit arc is keyed on
     `prop:curvature-rank-gb-stratification`.  This block's `uses[]` does not
     contain it, so the arc passes over the block transitively and never names
     it.  `grep -c bond` on the 08-26 audit is 0.
  3. The 08-16 audit's own "Search performed" section asserts there is no
     fourth reading.  It walked `mass-theory/`; the fourth lives in
     `knots-particles-confinement/`.

🛑 AND THE CORPUS ALREADY KNOWS, IN ONE PLACE.  §6 classifies the blocks that
carry the word-length rule for a named filtration -- and one of the three is
not a carrier of the conflation at all.  `phi-q-categorical-truncation-
interpretation.md` opens: "The parameter `k_max` recorded in witness data
represents the Coxeter-length filtration.  This strictly differs from the
structural GB-depth `k_*(T_w)`."  So the distinction is stated in `content/`
and simply never propagated to the blocks downstream of it.  That makes this a
CONSISTENCY defect rather than an open question, and it is why the repair is a
decision about which reading to keep, not a discovery to be made.  (An earlier
unclassified version of §6 lumped that block in with the two that conflate and
reported "3 carriers" -- counting a witness AGAINST the conflation as evidence
FOR it.  Classify before counting.)

WHAT THIS DOES NOT CLAIM.  Not that the lemma is false, not that the Lean is
wrong, not that either filtration is the right one.  `qou-sw8n`'s question --
WHICH `J^•` step 7 means -- stays open, and its own exclusion is scope-(a)
(a generic-`q` strata mismatch, ties permitted at a single `q₀`).  This is a
citation-integrity measurement, not a refutation, so no (a)/(b) scope is owed.

No arithmetic: every check is a string/AST measurement over committed files.
No witness written, no producer re-run, nothing recomputed.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# `content/` was renamed to `folio/` in the 2026-10-04 reorg. This probe
# predates it; left unrepathed it resolves a directory that does not exist,
# `read()` returns "" for every block and `rglob` yields nothing -- measured
# 21 of its 31 checks fail for that reason alone, with nothing wrong in the
# corpus. The salvage is this one line.
CONTENT = ROOT / "folio" / "quantum-observable-universe"
AUDITS = ROOT / "docs" / "audits"
COORD = ROOT / "docs" / "coordination"
LEAN = CONTENT / "lean" / "QOU"

CITER = CONTENT / "mass-theory" / "bond-order-eq-jet-degree.md"
CITED = CONTENT / "mass-endomorphism" / "gb-spectral-sequence.md"

_passed = 0
_failed = 0


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


def check(cond: bool, label: str, detail: str = "") -> None:
    global _passed, _failed
    mark = "✓" if cond else "✗"
    if cond:
        _passed += 1
    else:
        _failed += 1
    print(f"  {mark} {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"      {line}")


def section1() -> None:
    print("\n=== 1. the citing block names COXETER LENGTH and cites the other one ===\n")
    md = read(CITER)
    check(bool(md), f"{CITER.relative_to(ROOT)} exists", f"{len(md.splitlines())} lines")
    check(
        "Coxeter length" in md and r"\ell(w)" in md,
        "it says the filtration is by Coxeter length ℓ(w)",
        'verbatim: "equip $H_{3A}(q)$ with the Gröbner--Shirshov\n'
        'filtration by Coxeter length $\\ell(w)$"',
    )
    check(
        "prop:gb-spectral-sequence" in md,
        "and it attributes that to `prop:gb-spectral-sequence`",
        "the citation sits in the same sentence as the Coxeter claim, so it is\n"
        "read as the SOURCE of the Coxeter reading, not as a neighbouring fact.",
    )
    ts = read(CITER.with_suffix(".ts"))
    check(
        "prop:gb-spectral-sequence" in ts,
        "the .ts `uses[]` carries the edge too (not only the prose)",
        "so the dependency graph routes through it as well.",
    )
    check(
        "prop:curvature-rank-gb-stratification" not in ts,
        "🛑 but `uses[]` does NOT contain `prop:curvature-rank-gb-stratification`",
        "which is the proposition the whole wpdb / 08-16 / 08-26 audit arc is\n"
        "keyed on.  That is detector-miss reason 2: the arc reaches this block\n"
        "only transitively and never names it.",
    )


def section2() -> None:
    print("\n=== 2. the CITED block names the CONFINEMENT filtration, and never Coxeter ===\n")
    md = read(CITED)
    check(bool(md), f"{CITED.relative_to(ROOT)} exists", f"{len(md.splitlines())} lines")
    check(
        "confinement filtration" in md,
        "it says the filtration is the *confinement* filtration J^•(q)",
        'verbatim line 2: "The Hecke algebra $H_n(R, q)$ with the confinement\n'
        'filtration $J^\\bullet(q)$ ([confinement level](#def:confinement-level))"',
    )
    check(
        "def:confinement-level" in md,
        "and points at `def:confinement-level` as its definition",
    )
    check(
        "Coxeter" not in md,
        "🛑 the string 'Coxeter' does NOT occur in it at all",
        "so the citing block attributes to it a reading it does not carry.",
    )
    check(
        "Partition energies" in md or "partition energies" in md.lower(),
        "its strata are indexed by PARTITION ENERGIES E_ℓ(q₀), not word lengths",
        "so the shared glyph `ℓ` is a partition index there and a Coxeter\n"
        "length in the citer -- the collision that makes the mis-citation\n"
        "invisible to a reader skimming either block alone.",
    )


def section3() -> None:
    print("\n=== 3. 🛑 the LEAN sides with the CITER — so this is not a doc fix ===\n")
    f = LEAN / "Knot" / "BodyOrderExpansion.lean"
    src = read(f)
    check(bool(src), f"{f.relative_to(ROOT)} exists", f"{len(src.splitlines())} lines")
    check(
        "Coxeter length is additive" in src,
        "it states it needs Coxeter-length additivity over S_3 × ⋯ × S_3",
        'verbatim: "needs the index set of `H_{3A}`\'s normal forms to BE such a\n'
        'product -- i.e. that Coxeter length is additive over the Young subgroup"',
    )
    check(
        "BlockLengthAdditive" in src,
        "and discharges it via `QOU.Knot.BlockLengthAdditive`",
        "the parabolic length formula -- a real proof, not an assumption.",
    )
    for name in ("BodyOrderExpansion", "BlockLengthAdditive"):
        g = LEAN / "Knot" / f"{name}.lean"
        s = read(g)
        bare = len(re.findall(r"(?<![-\w])sorry(?![-\w])", s))
        check(
            bool(s) and bare == 0,
            f"{name}.lean is sorry-free ({bare} bare `sorry`)",
        )
    carrier = read(CITER.with_suffix(".lean"))
    check(
        bool(carrier) and "gradedTerm" in carrier,
        "the block's OWN .lean is filtration-agnostic (`gradedTerm : ℕ → ℝ`)",
        "no Hecke algebra, no J^•, no ℓ(w) -- a §3b-cond structure whose\n"
        "`body_eq_graded` is a hypothesis FIELD.  So the carrier itself cannot\n"
        "adjudicate which filtration is meant; only the cone above it does.",
    )


def section4() -> None:
    print("\n=== 4. 🛑 the prior record asserts these are the SAME object ===\n")
    a = read(AUDITS / "2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md")
    check(bool(a), "2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md exists")
    check(
        "bond-order-eq-jet-degree" in a,
        "it draws the dependency edge through `conj:bond-order-eq-jet-degree`",
    )
    # Whitespace-tolerant: the phrase is WRAPPED across a line break in the
    # source ("...the same\n$J^\bullet$ that has..."), so a single-line literal
    # match returns False on text that is plainly there.  This probe's first
    # run failed exactly that way -- recorded because it is the same
    # detector-blindness class the rest of the file is about, committed by the
    # file itself.
    same_j = re.search(r"the\s+same\s+\$J\^\\bullet\$", a)
    check(
        same_j is not None,
        "🛑 and concludes the identification is stated in terms of THE SAME J^•",
        'verbatim: "is stated in terms of the same $J^\\bullet$ that has three\n'
        'excluded readings."  That identification is what §1+§2 measure to be\n'
        "false.  A topic-grep for prior art therefore returns a confident\n"
        "statement pointing the WRONG way -- the most expensive kind of miss.",
    )
    b = read(AUDITS / "2026-08-26-no-shift-rescues-the-word-partition-bridge.md")
    check(
        bool(b) and "bond" not in b,
        "the 08-26 audit never mentions the block (`bond` count = 0)",
        "detector-miss reason 2, measured on the audit that would have caught it.",
    )


def section5() -> None:
    print("\n=== 5. 🛑 the criterion built for this RAN and passed with 0 findings ===\n")
    p = CITER.with_suffix(".qa.json")
    d = json.loads(read(p) or "{}")
    crit = d.get("criteria", {})
    entry = (crit.get("da-citation-misuse") or [{}])[-1]
    check(
        entry.get("result") == "pass",
        "`da-citation-misuse` ran on this block and returned `pass`",
        f"findings: {len(entry.get('findings') or [])}",
    )
    notes = str(entry.get("notes", ""))
    check(
        "EXPIRED" in notes,
        "its verdict is stamped [EXPIRED-NO-FIELD-HASH]",
        f"reviewed_at: {entry.get('reviewed_at')}\n"
        f"reviewer:    {(entry.get('reviewer') or {}).get('agent_model')}",
    )
    check(
        "Sound conceptual formulation" in notes,
        "and its note is content-free filler, not a finding",
        f'verbatim: "{notes[:120]}..."\n'
        "A `pass` from a criterion whose note says nothing specific is not\n"
        "evidence the block was examined.  This is the same shape already on\n"
        "record for `curvature-rank-gb-stratification-proof`, where four `da-*`\n"
        "criteria returned zero findings on a proof its own Step 1 refutes.",
    )


def section6() -> None:
    print("\n=== 6. how many content blocks DEFINE the filtration by Coxeter length ===\n")
    # Measured, not asserted: a block DEFINES the GB/GS filtration by word
    # length only if it (i) names a Gröbner-Shirshov / GB / GS / jet filtration
    # AND (ii) gives the word-length rule in the same block.  Merely *using*
    # ell(w) for something else does not count -- a looser grep on "Coxeter
    # length" alone matches ~10 files and answers a different question.
    rule = re.compile(r"\\ell\(w\)\s*\\leq|with\s+\\ell\(w\)|by Coxeter length|Coxeter-length filtration")
    names = re.compile(r"Gr[oö]bner|Gr\\\"obner|\bGS filtration|\bGB filtration|jet filtration|filtration")
    # A block that carries the word-length rule may be doing one of two
    # OPPOSITE things, and lumping them is the error this probe is about.
    # A block that says the Coxeter filtration DIFFERS from the GB depth is a
    # witness FOR the distinction, not a carrier of the conflation.
    distinguishes = re.compile(
        r"strictly differs|differs from the structural|not the same as the GB|"
        r"distinct from the GB|is not the GB[- ]depth",
        re.IGNORECASE,
    )
    conflate, distinct = [], []
    for f in sorted(CONTENT.rglob("*.md")):
        s = read(f)
        if rule.search(s) and names.search(s):
            (distinct if distinguishes.search(s) else conflate).append(f.relative_to(ROOT))
    print(f"    blocks carrying the word-length rule for a named filtration: "
          f"{len(conflate) + len(distinct)}")
    print(f"    -- of which CONFLATE (state it as the GB/GS filtration): {len(conflate)}")
    for h in conflate:
        print(f"         {h}")
    print(f"    -- of which DISTINGUISH (say it differs from GB depth): {len(distinct)}")
    for h in distinct:
        print(f"         {h}")
    check(
        len(conflate) >= 2,
        "at least two blocks state the word-length rule AS the GB/GS filtration",
        "the count is printed rather than asserted.  A looser grep on 'Coxeter\n"
        "length' alone matches ~10 files and answers a different question; an\n"
        "unclassified one lumps in a block that explicitly DISTINGUISHES the\n"
        "two, which is evidence against the conflation, not for it.\n"
        "Re-measure here rather than quoting any number from prose.",
    )
    check(
        any("bond-order-eq-jet-degree" in str(h) for h in conflate),
        "`bond-order-eq-jet-degree.md` is one of the conflating blocks",
    )
    check(
        any("mba-step07-gb-filtration" in str(h) for h in conflate),
        "as is `alg:mba-step07-gb-filtration` — the APPENDIX MAINTENANCE CONTRACT",
        "AGENTS.md declares that appendix a sync contract for the compute.  So\n"
        "the Coxeter reading is carried by the block that is supposed to keep\n"
        "step 7's prose and its Python in agreement.",
    )
    check(
        len(distinct) >= 1,
        "🛑 and at least one block ALREADY DISTINGUISHES them — the corpus knows",
        "`phi-q-categorical-truncation-interpretation.md` line 1: \"The parameter\n"
        "$k_{\\max}$ recorded in witness data represents the Coxeter-length\n"
        "filtration. This strictly differs from the structural GB-depth\n"
        "$k_\\star(T_w)$.\"  So the distinction is stated somewhere in `content/`\n"
        "and is simply not propagated to the blocks that depend on it.  That\n"
        "makes this a consistency defect rather than an unknown, and it is why\n"
        "the repair is a decision about WHICH reading, not a discovery.",
    )


def section7() -> None:
    print("\n=== 7. two coordination ledgers still propagate the Coxeter reading ===\n")
    for name, frag in (
        ("2026-05-30-alpha-em-canonical-chain-walkthrough.md", "Coxeter length"),
        ("2026-05-23-algebraic-geometric-observable-consistency.md", "Coxeter length"),
    ):
        s = read(COORD / name)
        check(
            frag in s,
            f"{name} still states the step-7 filtration is by Coxeter length",
        )
    cs = read(ROOT / "docs" / "canonical-derivation-cheat-sheet.md")
    check(
        "qou-sw8n" in cs,
        "the cheat-sheet row WAS corrected today and points at `qou-sw8n`",
        "so the ledgers are behind the cheat sheet, not ahead of it -- they are\n"
        "the source shape the cheat-sheet row was corrected away from.",
    )
    # Test the LABEL, not the substring.  `grep -c bond` on the cheat sheet is
    # NOT zero -- it matches "bond-count", "bonded pairs" and "bond-word" in
    # the step-9b binding row, which are unrelated.  A substring test here
    # would report a false clean and, run the other way, a false alarm.
    check(
        "bond-order-eq-jet-degree" not in cs,
        "but the cheat sheet never names this consumer by label",
        "the correction was made at the row, not at the blocks downstream of it.",
    )


def section8() -> None:
    print("\n=== 8. what is NOT claimed ===\n")
    print(
        """    NOT claimed: that `conj:bond-order-eq-jet-degree` is false.  Its own Lean
    carrier is a legitimate §3b-cond conditional whose `body_eq_graded` is a
    hypothesis field; nothing here touches its truth.

    NOT claimed: that the Lean is wrong.  `BlockLengthAdditive` proves the
    parabolic length formula and is sorry-free.  The Coxeter reading is
    well-defined; the question is whether it is the one step 7 means.

    NOT claimed: that either filtration is canonical.  That is `qou-sw8n`,
    which stays OPEN -- and whose own exclusion of the confinement reading is
    scope-(a) (a generic-`q` strata mismatch; ties are permitted at a single
    `q₀`, and the decisive test needs the step-10 confinement LP, not run).

    NOT claimed: that retargeting the citation is the fix.  §3 measures that
    the Lean cone is built on the Coxeter reading, so pointing the prose at
    `prop:gb-spectral-sequence`'s confinement filtration would align it with
    the cited block and MISALIGN it with the formalisation.  There are at
    least three repairs and they have different blast radii; choosing among
    them is an owner decision and is deliberately not taken here.

    WHAT IS claimed: one citation names a source that says something else, the
    prior record says the two are the same object, and the criterion built to
    catch exactly this passed it with an expired content-free note."""
    )


def main() -> int:
    print("=" * 72)
    print("bond-order-eq-jet-degree cites a block that names a different filtration")
    print("=" * 72)
    for s in (section1, section2, section3, section4, section5, section6, section7):
        s()
    section8()
    print()
    print("=" * 72)
    if _failed:
        print(f"{_failed} check(s) FAILED, {_passed} passed")
        return 1
    print(f"all {_passed} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
