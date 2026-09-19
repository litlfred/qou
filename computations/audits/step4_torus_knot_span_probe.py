#!/usr/bin/env python3
"""Chain walk, step 4: do the six embeddable torus knots span H_3(q)?

CONTEXT.  The canonical-derivation cheat sheet renders step 4 as

    step 4. Bring chi = -6  ->  6 basis elements <-> 6 torus knots <-> particle content

and its step table gives the arithmetic: "dim H_3(q) = 6 = # embeddable torus
knots in Sigma_4".  Two sixes are being set against each other, and the "<->"
is doing real work in the chain: it is what carries the genus into the
particle content.

🛑 READ SECTION 2b BEFORE QUOTING SECTIONS 2 OR 3.  Sections 1-3 were written
before I had read cheat-sheet §9.5, and §9.5 answers most of what they raise.
Its text is on disk and was one grep away; I ran topic-scoped greps instead.

WHAT §9.5 SAYS, and it is the thing to know.  The diagram's six basis elements
are `{1, s1, s2, s1s2, s2s1, s1s2s1}` -- the GB basis of H_3 -- and §9.5 exists
precisely to correct "a recurrent agent confusion ... reading '6 basis
elements' as 6 independent SM-equivalent operators".  It calls them
**GENERATORS** whose multiplicative closure climbs the GB/jet tower.

So the right question is not what the six knots SPAN but what they GENERATE.
Measured in section 2b: **they generate all of H_3(q), 6 of 6, by products
alone.**  Section 2's framing -- "a coincidence of counts, not a
linear-algebraic identification" -- is therefore WITHDRAWN: there is a correct
algebraic sense in which the six knots answer to the six-element basis, and it
is the sense §9.5 tells readers to use.

WHAT SURVIVES.  The span measurement (4 of 6) refutes the BASIS reading, which
is the same reading §9.5 refutes at greater length.  So sections 1-3
CORROBORATE the corpus rather than finding a defect in it.  The one narrow
residue: the §1 diagram's bare "<->" still invites the basis reading, and §9.5
sits ~700 lines below it.

Section 3's `{ gamma, sigma_0, sigma_1, L_+, L_-, e^- }` is a THIRD six, from a
different appendix, and is not what the diagram means.  Kept because the
arithmetic is still correct and the three-sixes picture is worth having.

WHAT IS MEASURED.  The one linear-algebraic content the identification could
have: do the six torus-knot braid words span H_3(q)?  They do not.  Exact
symbolic rank over Q(q) via the faithful representation
(3) + (2,1) + (1,1,1) -- 1 + 4 + 1 = 6 matrix coordinates, so the span of
the six image vectors IS the span of the six words in the 6-dimensional
algebra.  sympy Symbol/Rational throughout; no float anywhere, so no
precision claim arises and none is made.

The answer is 4, and the reason is structural rather than numerical, so it
holds at every q:

  - Four of the six are 2-STRAND words, T_{2,s} = closure of sigma_1^s.  The
    Hecke relation collapses every power of one generator into
    span{1, sigma_1}, so those four span at most 2 dimensions however many
    of them there are.  Adding T_{2,11} at g = 5 adds nothing.
  - The other two are T_{3,4} and T_{3,5} = (sigma_1 sigma_2)^s.  Two words
    span at most 2.

  => rank <= 2 + 2 = 4 < 6.

This is the same invariant as the genus probe one level up (rank
subadditivity over a decomposition), and it is worth stating because it is
the *cheap structural argument that prunes the class* -- AGENTS.md
formalize-first -- rather than a numerical search.

WHAT THIS DOES NOT CLAIM.  Not that step 4 is wrong, and not that the
particle-content assignment fails.  Scope (b) applies ONLY to the narrow
arithmetic -- the six knot words span 4 of 6, at no q rather than at some q,
by the invariant named above.  It does NOT apply to any reading of the
diagram, per section 2b.

Run:  python3 computations/audits/step4_torus_knot_span_probe.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "content" / "quantum-observable-universe"

FAILURES: list[str] = []
CHECKS = 0

q = sp.Symbol("q", positive=True)
qi = 1 / q


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


# ---------------------------------------------------------------------------
# The three irreps of H_3(q), convention (sigma - q)(sigma + 1/q) = 0.
# ---------------------------------------------------------------------------

def h3_irreps() -> dict[str, tuple[sp.Matrix, sp.Matrix]]:
    """(sigma_1, sigma_2) in each of the three irreps of H_3(q).

    The 2-dimensional one is SOLVED from the braid relation rather than
    transcribed -- a transcribed rep is a place for a convention slip to
    hide, and the assertions below are what make this one trustworthy.
    """
    one = sp.Matrix([[1]])
    c = sp.Symbol("c")
    s1 = sp.Matrix([[q, 1], [0, -qi]])
    s2 = sp.Matrix([[-qi, 0], [c, q]])
    sols = sp.solve(
        [sp.simplify(e) for e in (s1 * s2 * s1 - s2 * s1 * s2)], c, dict=True
    )
    assert sols, "no c satisfies the braid relation"
    s2 = s2.subs(c, sols[0][c])
    return {
        "(3)": (sp.Matrix([[q]]), sp.Matrix([[q]])),
        "(2,1)": (sp.simplify(s1), sp.simplify(s2)),
        "(1,1,1)": (sp.Matrix([[-qi]]), sp.Matrix([[-qi]])),
        "_one": (one, one),
    }


def section1(irr) -> None:
    print("\n=== 1. the three irreps, verified ===\n")
    for name in ("(3)", "(2,1)", "(1,1,1)"):
        a, b = irr[name]
        n = a.shape[0]
        check(
            sp.simplify(a * b * a - b * a * b) == sp.zeros(n, n),
            f"{name:8s} braid relation  s1 s2 s1 = s2 s1 s2",
        )
        for lbl, s in (("s1", a), ("s2", b)):
            check(
                sp.simplify((s - q * sp.eye(n)) * (s + qi * sp.eye(n))) == sp.zeros(n, n),
                f"{name:8s} Hecke relation on {lbl}",
            )
    check(
        sum(irr[n][0].shape[0] ** 2 for n in ("(3)", "(2,1)", "(1,1,1)")) == 6,
        "dim H_3(q) = 1 + 4 + 1 = 6  (the cheat sheet's first six)",
    )


# ---------------------------------------------------------------------------

def word_vector(r: int, s: int, irr) -> list[sp.Expr]:
    """The image of beta(T_{r,s}) in (3) + (2,1) + (1,1,1), flattened.

    Six coordinates, and the map is FAITHFUL (Wedderburn: H_3 is the direct
    sum of its three matrix blocks), so the span of these vectors equals the
    span of the words in H_3(q) itself -- not merely of their characters.
    """
    out: list[sp.Expr] = []
    for name in ("(3)", "(2,1)", "(1,1,1)"):
        s1, s2 = irr[name]
        w = (s1**s) if r == 2 else ((s1 * s2) ** s)
        out.extend(sp.simplify(e) for e in w)
    return out


def section2(irr) -> None:
    print("\n=== 2. the span of the six torus-knot words in H_3(q) ===\n")

    knots = [(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)]
    M = sp.Matrix([word_vector(r, s, irr) for (r, s) in knots])
    rank = M.rank()
    print(f"    M is {M.shape[0]} x {M.shape[1]} (6 words x 6 algebra coordinates)")
    print(f"    exact symbolic rank over Q(q) = {rank}\n")

    check(rank == 4, "the six words span a 4-dimensional subspace, not 6",
          f"rank = {rank}; dim H_3(q) = 6")

    # The two structural reasons, measured separately.
    two_strand = sp.Matrix([word_vector(2, s, irr) for s in (3, 5, 7, 9)])
    check(
        two_strand.rank() == 2,
        "the FOUR 2-strand words span only 2 dimensions",
        "sigma_1^s collapses into span{1, sigma_1} by the Hecke relation, so\n"
        "any number of T_{2,s} spans at most 2 -- T_{2,11} at g = 5 adds none",
    )
    three_strand = sp.Matrix([word_vector(3, s, irr) for s in (4, 5)])
    check(
        three_strand.rank() == 2,
        "the TWO 3-strand words span 2 dimensions",
    )
    check(
        rank == two_strand.rank() + three_strand.rank(),
        "rank is additive here (the named invariant: rank subadditivity)",
        "2 + 2 = 4 < 6, at every q -- structural, not a numerical accident",
    )

    # Would MORE 2-strand knots help?  No -- that is the point.
    more2 = sp.Matrix([word_vector(2, s, irr) for s in (3, 5, 7, 9, 11, 13, 15)])
    check(
        more2.rank() == 2,
        "seven 2-strand words still span 2 -- the cap is the Hecke relation",
        f"rank {more2.rank()} for s in 3,5,7,9,11,13,15",
    )


# ---------------------------------------------------------------------------

def section2b(irr) -> None:
    """🛑 THE CORRECTION.  Span is not the right test, and the cheat sheet says so.

    Added after reading cheat-sheet §9.5, which I had not read when sections 1-2
    were written.  That section states the six as
    `{1, s1, s2, s1s2, s2s1, s1s2s1}` -- the GB basis of H_3 -- and exists
    precisely to correct "a recurrent agent confusion ... reading '6 basis
    elements' as 6 independent SM-equivalent operators".  It calls them
    **GENERATORS** whose multiplicative closure climbs the GB/jet tower.

    Under THAT reading the right question is not what the six knots SPAN but
    what they GENERATE -- and measured below, they generate all of H_3(q), by
    products alone, no inverses needed.
    """
    print("\n=== 2b. 🛑 CORRECTION: they SPAN 4, but they GENERATE all 6 ===\n")

    knots = [(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)]
    gens = [
        (
            (sp.Matrix([[q**s]]), irr["(2,1)"][0] ** s, sp.Matrix([[(-qi) ** s]]))
            if r == 2 else
            (sp.Matrix([[q ** (2 * s)]]),
             (irr["(2,1)"][0] * irr["(2,1)"][1]) ** s,
             sp.Matrix([[(-qi) ** (2 * s)]]))
        )
        for (r, s) in knots
    ]

    def flat(t):
        return list(t[0]) + list(t[1]) + list(t[2])

    ident = (sp.Matrix([[1]]), sp.eye(2), sp.Matrix([[1]]))
    seen = sp.Matrix([flat(ident)])
    cur = [ident]
    for _ in range(6):
        new = []
        for a in cur:
            for g in gens:
                p = (sp.simplify(a[0] * g[0]),
                     sp.simplify(a[1] * g[1]),
                     sp.simplify(a[2] * g[2]))
                cand = seen.col_join(sp.Matrix([flat(p)]))
                if cand.rank() > seen.rank():
                    seen = cand
                    new.append(p)
        if not new:
            break
        cur = new

    check(
        seen.rank() == 6,
        "the six torus knots GENERATE all of H_3(q) -- 6 of 6",
        "by products alone; no inverses needed.\n"
        "\n"
        "SO SECTION 2's FRAMING WAS TOO STRONG AND IS WITHDRAWN.  I wrote that\n"
        "the '6 <-> 6' is 'a coincidence of counts, not a linear-algebraic\n"
        "identification'.  There IS a correct algebraic sense in which the six\n"
        "knots answer to the six-element basis: they generate the same algebra,\n"
        "and generation is exactly the reading cheat-sheet §9.5 tells readers to\n"
        "use.  My span measurement does not refute that reading; it refutes the\n"
        "BASIS reading -- which §9.5 already refutes, in more detail, and which\n"
        "it calls a 'recurrent agent confusion'.\n"
        "\n"
        "So section 2 CORROBORATES the corpus rather than finding a defect in it.\n"
        "What is left is narrow: the §1 DIAGRAM's bare '<->' still invites the\n"
        "basis reading that §9.5 spends a section correcting, and §9.5 is 700\n"
        "lines below the diagram.",
    )


def section3() -> None:
    print("\n=== 3. a THIRD six, in a different appendix ===\n")

    p = CONTENT / "appendix-knot-operations" / "knot-operator-basis-table.md"
    txt = p.read_text(encoding="utf-8") if p.exists() else ""
    check(
        r"\{\ \gamma,\ \sigma_0,\ \sigma_1,\ L_+,\ L_-,\ e^-\ \}" in txt,
        "the NF basis is {gamma, sigma_0, sigma_1, L_+, L_-, e^-}",
        f"{p.relative_to(REPO)}",
    )
    check(
        r"b_i \cdot \beta(T_{m,n}) \cdot b_j" in txt,
        "and the torus knots appear as OPERATORS on that basis, not as it",
        "the block tabulates b_i . beta(T_{m,n}) . b_j for every basis pair\n"
        "and every knot.\n"
        "\n"
        "NOTE this is a THIRD six, not the one the diagram means.  Cheat-sheet\n"
        "§9.5 names the diagram's six explicitly as the GB basis of H_3,\n"
        "{1, s1, s2, s1s2, s2s1, s1s2s1}.  Section 2 was written reaching for\n"
        "the wrong second six; that does not change its arithmetic, but it does\n"
        "change what the arithmetic is ABOUT.  See section 2b.",
    )

    # And pin §9.5 itself, so this correction cannot go stale silently.
    cs = (REPO / "docs" / "canonical-derivation-cheat-sheet.md").read_text(encoding="utf-8")
    check(
        "A recurrent agent confusion is reading \"6 basis elements\" as **6 independent" in cs,
        "cheat-sheet §9.5 already warns against the basis reading",
        "it calls them GENERATORS and describes the multiplicative closure\n"
        "climbing the GB/jet tower -- which section 2b measures and confirms.",
    )


def main() -> int:
    print("step 4 torus-knot span probe")
    print("=" * 72)
    irr = h3_irreps()
    section1(irr)
    section2(irr)
    section2b(irr)
    section3()
    print("\n" + "=" * 72)
    if FAILURES:
        print(f"FAILED {len(FAILURES)}/{CHECKS}")
        for f in FAILURES:
            print(f"  - {f}")
        return 1
    print(f"all {CHECKS} checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
