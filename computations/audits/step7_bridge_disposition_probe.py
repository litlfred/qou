#!/usr/bin/env python3
"""Step 7's interior is CLOSED — I re-derived it and the corpus already had it.

🛑 THIS PROBE'S FIRST RESULT IS A NEGATIVE ABOUT MY OWN WORK, and it is stated
first because it is the more useful half.

WHAT I SET OUT TO DO.  The canonical-chain walk (#7362, `e8289b4971`) left
step 7 -- the Gröbner-Shirshov spectral sequence -- as "interior mathematics
to try".  I derived what I believed was a new obstruction:

    Let F_* be any filtration of A = H_n(q) with 1 in F_0, and suppose the
    induced filtration on Z(A) satisfies  Z ∩ F_0 = span{e_λ : δ(λ) = c}.
    Since 1 = Σ_λ e_λ uses EVERY primitive idempotent, linear independence
    forces δ(λ) = c for every λ -- i.e. δ is CONSTANT.

    With δ = gbDepth, `gbDepth_ne_on_H4` then excludes it for every n ≥ 4.

**IT IS ALREADY IN THE CORPUS, PROVED SORRY-FREE, AND IT IS ROUTE A.**
`QOU.BraidKnot.unit_in_degree_zero_forces_constant_grading`
(`GSFiltrationUnitObstruction.lean`, 2026-08-26, bean `qou-09e0`) is the same
argument, formalised better than mine: it keys on the coefficient functionals
`π l u = 1` rather than on a span, so it needs only "the unit has nonzero
coefficient on every block" and never mentions a basis.  Its own docstring
already anticipates the candidate I would have proposed next (the
Jucys-Murphy content filtration) and excludes it by the same route.

So: **nothing in step 7's interior is open to derive.**  Four audits
(2026-08-16 x2, 2026-08-25, 2026-08-26), three sorry-free Lean files, and
three independent exact probes have closed it.  The residue is §3 of the
2026-08-26 audit's stated escape -- a NON-monomial GS-definable filtration
whose unit sits in positive degree -- and that audit argues, as a judgement,
that no rewriting-depth notion has that shape.

🛑 NEGATIVE RESULT, so the surface is named.  Corpus-grep paths run before
this file was written: (0) `corpus_search` MCP -- UNAVAILABLE this session,
the `paper-assistant` server failed to connect, so the structural-expansion
path was NOT exercised and this is a grep-only search; (1) `docs/audits/`;
(2) `content/`; (3) `computations/`; (4) `docs/coordination/`; (5) `library/`
(not reached -- path 1 hit on the first query); (6) `.beans/`.  The hit was
immediate: a grep for `gbDepth.*constant` returned the audit's own §2 line.

WHAT IS LEFT, AND IT IS NOT A DERIVATION.  Every one of those four audits
DELIBERATELY declined to rewrite the consumer sites, three of them giving the
same reason verbatim -- *"mechanical editing across sites whose uses differ is
how this defect got in"*.  That disposition is still undone.  This probe
measures its state, because a walk of the chain is exactly where the cost of
leaving it undone shows up.

THE ONE COMPOSITE FACT THE CORPUS DOES NOT STATE IN ONE PLACE.  Sections 2-5
below chain five things each of which is separately on the record:

  - the chain's `uses[]` graph routes steps 7/8 through
    `prop:jet-prefix-gb-filtration` (measured in #7362, defect #4);
  - that block is the 2026-08-26 audit's **Class B** site;
  - its displayed object is `J^{k-3}(q)/J^{k-2}(q)`, and EVERY candidate
    reading of `J^•` is now excluded;
  - it is stated over `H_{3A}(q)`, so for any atom with A ≥ 2 it sits at
    n ≥ 6 -- inside the regime where the exclusion bites, not at the n ≤ 3
    edge where it is vacuous;
  - and its prose asserts the OPPOSITE ("aligns exactly", "strictly graded"),
    unchanged since before the exclusion landed.

🛑 NOTHING HERE IS A NEW DEFECT REPORT.  In particular the block's §3b-cond
non-compliance is **baselined since 2026-05-01** in three separate audit
witnesses; §5 measures that precisely so nobody re-files it.  What is new is
only the CONJUNCTION, and what the conjunction implies for the author's
decision on defect #4.

NO CONTENT IS EDITED HERE.  Rewriting a consumer site is not covered by
either exemption of AGENTS.md §"ASK THE OWNER BEFORE CHANGING THINGS" -- it
does not increase precision, and the corpus does not fix the wording (the
four audits each declined to choose it).  So this measures and asks.

Arithmetic: integer partition combinatorics only.  No floats anywhere.

Run:  python3 computations/audits/step7_bridge_disposition_probe.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
PAPER = REPO / "content" / "quantum-observable-universe"
LEAN = PAPER / "lean" / "QOU" / "BraidKnot"
AUDITS = REPO / "docs" / "audits"

FAILURES: list[str] = []
CHECKS = 0

BLOCK = PAPER / "mass-theory" / "jet-prefix-gb-filtration"


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


def read(p: Path) -> str:
    return p.read_text(encoding="utf-8") if p.exists() else ""


# ---------------------------------------------------------------- partitions

def partitions(n: int, cap: int | None = None):
    """All partitions of n as weakly-decreasing tuples."""
    if cap is None:
        cap = n
    if n == 0:
        yield ()
        return
    for first in range(min(n, cap), 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def gb_depth(lam: tuple[int, ...]) -> int:
    """gbDepth λ = λ₁ + λ'₁ − 1 (the corner hook).  `QOU.BraidKnot.gbDepth_eq_corner`."""
    return lam[0] + len(lam) - 1


# ------------------------------------------------------------------ sections

def section1() -> None:
    print("\n=== 1. 🛑 my derivation is PRIOR ART — it is Route A ===\n")
    src = read(LEAN / "GSFiltrationUnitObstruction.lean")
    check(
        "theorem unit_in_degree_zero_forces_constant_grading" in src,
        "`unit_in_degree_zero_forces_constant_grading` exists, sorry-free",
        "content/.../lean/QOU/BraidKnot/GSFiltrationUnitObstruction.lean:131\n"
        "the argument I reconstructed independently, formalised better: it keys\n"
        "on `π l u = 1` (the unit's coefficient on every block) rather than on a\n"
        "span, so it never mentions a basis.",
    )
    check(
        "sorry" not in src.replace("sorryAx", ""),
        "and it carries no `sorry`",
    )
    check(
        "Jucys-Murphy" in src or "Jucys–Murphy" in src,
        "🛑 its docstring ALREADY excludes the candidate I would have tried next",
        "the Jucys-Murphy content filtration -- \"whose degree-`0` piece is R·1\".\n"
        "So the obvious fourth filtration was anticipated and closed too.",
    )
    check(
        (AUDITS / "2026-08-26-the-unit-coefficient-excludes-gs-definable-filtrations.md").exists(),
        "and the audit carrying it is on disk",
        "docs/audits/2026-08-26-the-unit-coefficient-excludes-gs-definable-filtrations.md",
    )
    # the three sibling audits, so the reader can see the depth of the prior art
    for name in (
        "2026-08-16-three-gb-filtrations-one-name.md",
        "2026-08-26-no-shift-rescues-the-word-partition-bridge.md",
        "2026-08-25-spectral-sequence-is-a-no-go-not-a-tool.md",
    ):
        check((AUDITS / name).exists(), f"sibling audit present: {name}")


def section2() -> None:
    print("\n=== 2. the chain routes steps 7/8 through the Class-B site ===\n")
    ts = read(BLOCK.with_suffix(".ts"))
    check(
        'label: "prop:jet-prefix-gb-filtration"' in ts,
        "`prop:jet-prefix-gb-filtration` is a live content block",
        f"{BLOCK.with_suffix('.ts').relative_to(REPO)}",
    )
    check(
        "proposition({" in ts,
        "🛑 and its KIND is `proposition` — a provable kind",
        "not `conjecture`.  That matters for §5.",
    )
    audit = read(AUDITS / "2026-08-26-no-shift-rescues-the-word-partition-bridge.md")
    check(
        "Class B" in audit and "prop:jet-prefix-gb-filtration" in audit,
        "the 2026-08-26 audit names it explicitly as a **Class B** site",
        "Class B = \"the site needs genuine compatibility with the word\n"
        "filtration\" -- i.e. it IS the identification, not a labelling.",
    )


def section3() -> tuple[str, dict[int, dict[int, int]]]:
    print("\n=== 3. its displayed object is J^•, and every reading is excluded ===\n")
    md = read(BLOCK.with_suffix(".md"))
    check(
        "J^{k-3}(q) / J^{k-2}(q)" in md.replace("  ", " ") or "J^{k-3}" in md,
        "the block's own display defines β_k^GS in `J^{k-3}(q)/J^{k-2}(q)`",
        "so the object it is built from is exactly the one with three excluded\n"
        "readings (ideal-power = ⊥; Coxeter = wrong induced grading; rewrite\n"
        "depth = identically zero).",
    )
    check(
        "H_{3A}(q)" in md,
        "🛑 and it is stated over `H_{3A}(q)` — so n = 3A",
        "which is where §3's arithmetic below bites.",
    )

    # gbDepth distributions at the n the block actually lives on
    print()
    dists: dict[int, dict[int, int]] = {}
    print("    A   n=3A   gbDepth strata (depth: #partitions)      constant?")
    print("    " + "-" * 64)
    for A in (1, 2, 3, 4):
        n = 3 * A
        d: dict[int, int] = {}
        for lam in partitions(n):
            d[gb_depth(lam)] = d.get(gb_depth(lam), 0) + 1
        dists[n] = d
        const = len(d) == 1
        shown = "{" + ", ".join(f"{k}: {v}" for k, v in sorted(d.items())) + "}"
        print(f"    {A}   {n:>4}   {shown:<42} {'YES' if const else 'no'}")
    print()

    check(
        len(dists[3]) == 1,
        "at A = 1 (n = 3) gbDepth IS constant — the exclusion is VACUOUS there",
        "`QOU.BraidKnot.gbDepth_const_on_H3`.  The single-nucleon case is the\n"
        "one place a GS-definable filtration could exist -- and it is exactly\n"
        "the place the grading carries no information.",
    )
    check(
        all(len(dists[3 * A]) > 1 for A in (2, 3, 4)),
        "🛑 at EVERY A ≥ 2 it is NOT constant — so Route A excludes the site there",
        "any atom past hydrogen sits at n ≥ 6, inside the excluded regime.\n"
        "The block is not used at the edge case that survives.",
    )
    return md, dists


def section4(md: str) -> None:
    print("\n=== 4. 🛑 and its prose asserts the opposite, unchanged ===\n")
    for phrase, gloss in (
        ("aligns exactly with the Hecke-algebraic structure",
         "an alignment Route A excludes for every GS-definable filtration"),
        ("strictly graded construction",
         "the grading whose existence is what was refuted"),
    ):
        check(phrase in md, f"the .md still asserts: \"{phrase}\"", gloss)

    check(
        "conditional" not in md.lower() and "conj:" not in md,
        "and it carries NO conditional banner and names no conjecture",
        f"the whole .md is {len(md.splitlines())} lines.",
    )
    audit = read(AUDITS / "2026-08-26-no-shift-rescues-the-word-partition-bridge.md")
    check(
        "deliberately does not rewrite" in audit,
        "the audit that found this DELIBERATELY did not rewrite the site",
        "\"mechanical editing across sites whose uses differ is how this defect\n"
        "got in\" -- the same reason given by three of the four audits.  So the\n"
        "gap is a deferred decision, not an oversight.",
    )


def section5() -> None:
    print("\n=== 5. 🛑 the §3b-cond gap is BASELINED — do NOT re-file it ===\n")
    found: list[tuple[str, str]] = []
    for name in (
        "2026-05-01-p3-1-conjectural-propagation.witness.json",
        "2026-05-09-conditional-class-banner.witness.json",
        "2026-06-03-conditional-class-banner-baseline.json",
    ):
        p = AUDITS / name
        if not p.exists():
            continue
        blob = json.dumps(json.load(open(p, encoding="utf-8")))
        if "prop:jet-prefix-gb-filtration" in blob:
            found.append((name, "listed"))
    for name, _ in found:
        print(f"    listed in  docs/audits/{name}")
    print()
    check(
        len(found) >= 3,
        "it is listed in THREE separate audit witnesses, earliest 2026-05-01",
        "so \"this proposition is downstream of a conjecture with no conditional\n"
        "banner\" is a KNOWN, baselined item -- four and a half months old.\n"
        "Re-reporting it as a finding would be the re-declaration AGENTS.md's\n"
        "corpus-grep checklist exists to prevent.",
    )
    print("    WHAT HAS CHANGED SINCE THAT BASELINE, and it is the only new thing:")
    print("    in May the conjecture it hangs on was OPEN.  Since 2026-08-26 the")
    print("    route is EXCLUDED for the whole GS-definable class, sorry-free.")
    print("    The 2026-08-26 audit §8 says the Class-B conjecture \"should now")
    print("    record that the route is excluded, not merely candidate-free\".")
    print("    That has not happened.  A banner-gap over an open conjecture and a")
    print("    banner-gap over an excluded construction are different objects.")


def section6() -> None:
    print("\n=== 6. what this probe does NOT claim ===\n")
    print("""    - NOT that any mass or binding NUMBER moves.  `J^•` enters the chain
      as an INDEXING -- which body order an a_D^(n) belongs to -- never as a
      magnitude.  The magnitude is a Seiberg-Witten period and is untouched.
      Unaffected: the Wedderburn decomposition, tr_M, y_λ, the idempotents,
      and gbDepth as a definition.

    - NOT that the identification is false in the abstract.  A filtration
      inducing the gbDepth grading exists -- the Wedderburn-block one, whose
      unit sits in degree n rather than 0.  What is excluded is that anything
      definable from the GS rewriting data is such a filtration.

    - NOT that `prop:curvature-rank-gb-stratification` is false.  It is about
      WORDS and may well be true of words.  What fails is reading a PARTITION
      grading off it.

    - NOT a new defect report.  Every ingredient is on the record; §5 measures
      precisely how long the §3b-cond half has been.

    - NOT a claim that the escape is closed.  A non-monomial GS-definable
      filtration with its unit in positive degree is not excluded by anything
      here; the 2026-08-26 audit argues on judgement, not proof, that no
      rewriting-depth notion has that shape.\n""")


def main() -> int:
    print("step 7 — the bridge disposition, and a negative about my own derivation")
    print("=" * 74)
    section1()
    section2()
    md, _ = section3()
    section4(md)
    section5()
    section6()
    print("=" * 74)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
