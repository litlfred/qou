#!/usr/bin/env python3
"""Defect #5 is a JUDGEMENT, not a corpus-determined fix — and my "one-symbol
fix" characterisation is withdrawn.

BACKGROUND.  The canonical-chain walk (#7362, merged `e8289b4971`) reported as
defect #5 that `\\widehat{\\mathcal{M}}_{\\mathrm{QOU}}` -- the domain on which
`archimedean-realization-functor-interpretation.md` scopes the identification
`R_top = tau_arch` -- "occurs exactly once corpus-wide and is defined nowhere",
while two siblings scope the identical claim to "the algebraic quantum volume",
which resolves to `def:algebraic-quantum-volume`.  I called it "a one-symbol
fix".

**THAT CHARACTERISATION IS WITHDRAWN.**  Defects #1 and #2 turned out to be
corpus-determined (PR #7365).  #5 does not, and asserting the obvious fix would
put something in the corpus the corpus does not say.

WHAT THE MEASUREMENT ACTUALLY SHOWS.

1. The symbol is NOT meaningless.  Its own sentence glosses it: "On **motivic
   QOU inputs**, `R_top` coincides exactly with the archimedean component of
   `tau`".  So a reader is not left without a meaning, only without a formal
   definition block.

2. That gloss HAS a Lean carrier.  The phrase "QOU motivic inputs" appears in
   `mass-theory/archimedean-functor-uniqueness.lean` (the conditional
   uniqueness statement for `tau_arch`), and `QOU/AlgebraicSubstrate/
   MotivicSubstrate.lean` axiomatises "the QOU motivic substrate".

3. **But it is not a defined SUBSET either, and that is the sharp point.**
   `MotivicSubstrate`'s carrier `Mhat` is documented as

       "the dimension-completed localization  Mhat = K_0[L^-1]^"

   i.e. `Mhat` IS `\\widehat{\\mathcal{M}}` -- the whole thing.  The Lean
   carries no proper subobject.  So `\\widehat{\\mathcal{M}}_{\\mathrm{QOU}}
   \\subseteq \\widehat{\\mathcal{M}}` names a RESTRICTION the formalisation
   does not have.

4. **And nothing identifies it with the siblings' scope.**  `vol-through-tau`
   and `vol-as-motivic-period` scope the same coincidence to "the algebraic
   quantum volume [domain]", and `def:algebraic-quantum-volume` defines
   `Vol_alg(W) := tr_M(W)` for `W` in `H_n(q)` -- a TRACE VALUE, a different
   kind of object from a subobject of `Mhat`.  No block connects the two.

VERDICT.  Replacing `\\widehat{\\mathcal{M}}_{\\mathrm{QOU}}` with the siblings'
term would ASSERT an identification the corpus does not make.  So #5 is a
judgement for the author -- and a smaller one than the walk implied, because
the symbol is glossed and its concept is formalised.  The three dispositions
(define the subset; assert the identification and align to the siblings; leave
it as glossed prose) are not equivalent and the corpus does not choose.

🛑 THIS IS A NEGATIVE RESULT, so it is stated with its surface.  I searched:
`content/**` and `docs/**` for the LaTeX symbol and for both prose spellings;
`.beans/`; the Lean tree for the carrier.  What would SEPARATE the readings is
a block -- content or Lean -- that says `Mhat_QOU` is (or is not) the image of
the algebraic quantum volume.  I did not find one; that is different from
proving none can exist.

NO CONTENT IS EDITED HERE.  This measures.  No arithmetic either, so no
precision question arises.

Run:  python3 computations/audits/step9_mqou_scope_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "folio"
PAPER = CONTENT / "quantum-observable-universe"

FAILURES: list[str] = []
CHECKS = 0

SYMBOL = r"\widehat{\mathcal{M}}_{\mathrm{QOU}}"
GLOSSES = ("motivic QOU inputs", "QOU motivic inputs", "QOU motivic")


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


def hits(root: Path, needle: str, suffixes: tuple[str, ...]) -> list[Path]:
    out = []
    for p in root.rglob("*"):
        if p.suffix not in suffixes or not p.is_file():
            continue
        try:
            if needle in p.read_text(encoding="utf-8"):
                out.append(p.relative_to(REPO))
        except Exception:                                   # pragma: no cover
            continue
    return sorted(out)


def main() -> int:
    print("step 9 — the M_QOU scope: judgement, not fix")
    print("=" * 72)

    # 1. the symbol's reach
    print("\n=== 1. the LaTeX symbol ===\n")
    md = hits(CONTENT, SYMBOL, (".md",))
    check(len(md) == 1,
          "the symbol occurs in exactly ONE content .md",
          f"{md[0] if md else '(none)'}")

    # 2. it is glossed in its own sentence
    print("\n=== 2. 🛑 but it is GLOSSED -- not meaningless ===\n")
    rem = PAPER / "mass-theory" / "archimedean-realization-functor-interpretation.md"
    txt = rem.read_text(encoding="utf-8")
    check(
        "On motivic QOU inputs" in txt,
        "its own sentence glosses it: \"On motivic QOU inputs\"",
        "a reader is left without a formal DEFINITION, not without a meaning.\n"
        "My walk's \"defined nowhere\" was true of a definition block and\n"
        "overstated as a description of the reader's position.",
    )

    # 3. the gloss has a Lean carrier
    print("\n=== 3. and the gloss has a LEAN carrier ===\n")
    lean_hits: dict[str, list[Path]] = {}
    for g in GLOSSES:
        lean_hits[g] = hits(CONTENT, g, (".lean",))
    all_lean = sorted({p for v in lean_hits.values() for p in v})
    check(
        len(all_lean) >= 2,
        "\"QOU motivic\" appears in Lean, not only in prose",
        "\n".join(f"  {p}" for p in all_lean),
    )

    ms = PAPER / "lean" / "QOU" / "AlgebraicSubstrate" / "MotivicSubstrate.lean"
    mstxt = ms.read_text(encoding="utf-8") if ms.exists() else ""
    check(
        "axiomatises the QOU motivic" in mstxt,
        "MotivicSubstrate.lean axiomatises \"the QOU motivic substrate\"",
        f"{ms.relative_to(REPO)}",
    )

    # 4. THE SHARP POINT: the Lean carrier is the WHOLE Mhat, not a subset
    print("\n=== 4. 🛑 but the Lean carrier is the WHOLE Mhat ===\n")
    check(
        "dimension-completed localization" in mstxt,
        "its `Mhat` is documented as the dimension-completed localization",
        "`Mhat = K_0[L^-1]^` -- i.e. Mhat IS \\widehat{\\mathcal{M}}, entire.\n"
        "The Lean carries NO proper subobject, so `Mhat_QOU subset Mhat`\n"
        "names a RESTRICTION the formalisation does not have.",
    )

    # 5. nothing identifies it with the siblings' scope
    print("\n=== 5. and nothing identifies it with the siblings' scope ===\n")
    aqv = PAPER / "mass-theory" / "algebraic-quantum-volume.md"
    aqvtxt = aqv.read_text(encoding="utf-8") if aqv.exists() else ""
    check(
        r"\mathrm{tr}_M(W)" in aqvtxt,
        "def:algebraic-quantum-volume defines Vol_alg(W) := tr_M(W)",
        "a TRACE VALUE -- a different KIND of object from a subobject of Mhat.",
    )
    # Is there any block EQUATING them?  Exactly one block mentions both -- the
    # remark itself -- and the sentence that does is an INSTANCE relation, not
    # an identification.  (My first version of this check asserted "no block
    # mentions both" and FAILED on that very sentence; the sharper claim is
    # the one that survives, and it is the one that matters.)
    conn = [p for p in hits(CONTENT, "algebraic quantum volume", (".md",))
            if SYMBOL in (REPO / p).read_text(encoding="utf-8")]
    check(
        conn == [rem.relative_to(REPO)],
        "exactly ONE block mentions both -- the remark itself",
        f"{conn[0] if conn else '(none)'}",
    )
    check(
        "algebraic quantum volume exemplifies this mechanism" in txt,
        "🛑 and it relates them by \"EXEMPLIFIES\" -- an instance, not an equation",
        "\"The Kashaev limit of the algebraic quantum volume exemplifies this\n"
        "mechanism.\"  An example of the chain is not a statement that the\n"
        "chain's DOMAIN is the algebraic quantum volume domain.  So the two\n"
        "scopes are still not equated anywhere in the corpus.",
    )

    # 6. the verdict
    print("\n=== 6. verdict ===\n")
    print("""    Replacing the symbol with the siblings' term would ASSERT an
    identification the corpus does not make.  So defect #5 is a JUDGEMENT,
    not a corpus-determined fix -- unlike #1 and #2 (PR #7365).

    🛑 AND IT IS SMALLER THAN THE WALK IMPLIED.  "occurs once and is defined
    nowhere" is true of a definition BLOCK; the symbol is glossed in its own
    sentence and its concept is formalised in Lean.  **My "one-symbol fix"
    characterisation is withdrawn.**

    Three dispositions, not equivalent, none chosen by the corpus:
      (a) define the subset `Mhat_QOU` (the formalisation has no such object);
      (b) assert the identification and align to the siblings' term;
      (c) leave it -- glossed prose with a Lean carrier for the concept.

    🛑 NEGATIVE RESULT, stated with its surface.  Searched: content/** and
    docs/** for the symbol and both prose spellings; .beans/; the Lean tree.
    What would SEPARATE the readings is a block saying `Mhat_QOU` is (or is
    not) the image of the algebraic quantum volume.  I did not find one --
    which is different from proving none can exist.\n""")

    print("=" * 72)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
