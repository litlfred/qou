#!/usr/bin/env python3
"""Chain walk, step 0: is the genus/chi = -6 step derived, and does its
completeness criterion hold?

CONTEXT.  `docs/audits/2026-09-14-canonical-chain-condition-walk.md` found that
the canonical chain's conditions converge on one — `dim V = 2` — sitting in a
half-declared cycle: `why-b3` derives `G = SU(2)` (hence `dim V = 2`) FROM
`chi = -6`, while `chi-minus-six-chain` step 1 assumes `G = SU(2)` to reach
`chi = -6`.  Breaking that cycle needs a route to the genus that does not
already have SU(2) in hand.  The corpus offers three candidate routes.  This
probe asks, of each, (A) whether it is independent of SU(2), and (B) whether
its own stated criterion is satisfied.

WHAT IS MEASURED HERE IS (B) FOR THE THIRD ROUTE, EXACTLY.  Sections 1-2 are
source quotation and manifest reading (no arithmetic).  Sections 3-5 are exact
symbolic linear algebra over Q(q) -- sympy `Rational`/`Symbol` throughout, no
float anywhere, so there is no precision claim to make and none is made.

The third route (`lem:genus-from-hecke-completeness`) states:

    "At g = 3: 4 evaluations cannot span a 5-dimensional space (rank <= 4).
     At g = 4: 6 evaluations span 5 irreps (verified numerically: the 6 x 5
     matrix has rank 5 for all q > 1, q != root of unity).  Therefore
     g_min = 4."

and `vertex-algebra-relations.md` fixes the matrix:

    "the 6 x 5 character matrix M_ij = chi_{lambda_j}(T_{(r_i, s_i)}) over
     irreps lambda |- r of H_2(R, q) + H_3(R, q) has rank 5".

A torus knot T_{r,s} is the closure of a braid word on **r** strands, so a
row with r_i = 2 has support only in the two H_2 columns and a row with
r_i = 3 only in the three H_3 columns.  The matrix is block-diagonal, and rank
is additive over the blocks.  At g = 4 there are four r = 2 rows (rank <= 2,
two columns) and **two** r = 3 rows (rank <= 2, two rows).  So

    rank(M) <= 2 + 2 = 4 < 5

structurally -- no q, no arithmetic, no numerical verification possible.  This
probe confirms that by exact symbolic rank over Q(q), and checks the same for
every reading of "the matrix" it could find.

WHAT THIS DOES NOT CLAIM.  It does not claim the genus is not 4, and it does
not claim Bring's surface is wrong.  Two of the corpus's three routes to g = 4
are untouched by it.  The claim is narrow and is a scope-(b) structural
exclusion with a named invariant (rank subadditivity over a block
decomposition): *this* route's stated criterion cannot be met at g = 4, so it
cannot be the route that breaks the cycle.

Run:  python3 computations/audits/genus_completeness_rank_probe.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "folio" / "quantum-observable-universe"
BRINGS = CONTENT / "brings-surface"

FAILURES: list[str] = []
CHECKS = 0


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    mark = "ok  " if ok else "FAIL"
    print(f"  [{mark}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


def quote_present(path: Path, needle: str) -> bool:
    """Assert an exact quote is at source.  A quotation that has drifted from
    its source is worse than no quotation, so every quote in the write-up is
    pinned here rather than trusted."""
    if not path.exists():
        return False
    return needle in path.read_text(encoding="utf-8")


# ----------------------------------------------------------------------------
# Section 1.  The three routes, and SU(2) in each one's own words.
# ----------------------------------------------------------------------------

def section1() -> None:
    print("\n=== 1. the three corpus routes to g = 4 / chi = -6 ===\n")

    routes = [
        (
            "chi-minus-six-chain (step 1 assumes the gauge group)",
            BRINGS / "chi-minus-six-chain.md",
            r"We have $(\mathbf{C}, A, \tau)$ with gauge group $G = \mathrm{SU}(2)$",
        ),
        (
            "cohomological-embedding (closing rationale invokes SU_2)",
            BRINGS / "cohomological-embedding.md",
            r"unique minimal environment that supports $\mathrm{SU}_2$ reconstruction",
        ),
        (
            "genus-from-hecke-completeness (opens in Rep(SU_q(2)))",
            BRINGS / "genus-from-hecke-completeness-proof.md",
            r"The braiding on $V_1^{\otimes n}$ in $\mathrm{Rep}(\mathrm{SU}_q(2))$",
        ),
    ]
    for label, path, needle in routes:
        check(quote_present(path, needle), label, f"{path.relative_to(REPO)}")

    # And the direction of the other arrow, which is what closes the cycle.
    check(
        quote_present(
            CONTENT / "braids-and-knots" / "why-b3.md",
            r"The Descartes condition $\chi(A) = -6$ forces the gauge group to be a "
            r"quantum form of $\mathrm{SU}(2)$",
        ),
        "why-b3 derives SU(2) FROM chi = -6 (the return arrow)",
        "so every route above sits inside the cycle rather than breaking it",
    )


# ----------------------------------------------------------------------------
# Section 2.  Route 3 is not even formally independent: it `uses` route 2.
# ----------------------------------------------------------------------------

def section2() -> None:
    print("\n=== 2. route 3 declares route 2 as a dependency ===\n")

    ts = (BRINGS / "genus-from-hecke-completeness.ts").read_text(encoding="utf-8")
    check(
        'uses: ["prop:cohomological-embedding"]' in ts,
        "genus-from-hecke-completeness.ts uses prop:cohomological-embedding",
        "the manifest makes the dependency explicit; route 3 cannot be an\n"
        "independent confirmation of a genus that route 2 already fixed",
    )
    check(
        'validation: "not_checked"' in ts,
        "its Lean carrier is declared validation: not_checked",
    )

    # The "verified numerically" claim has no producer in the corpus.
    #
    # The exclusions are deliberate and are the difference between a measured
    # negative and a sloppy one.  Two `computations/audits/*.witness.json` DO
    # name this lemma -- `i1-no-probe-audit` and `lean-ref-resolution-audit` --
    # but both are corpus-wide INVENTORIES that list every block and every Lean
    # ref in the tree.  Naming a lemma in a census is not computing anything
    # about it; `i1-no-probe-audit` in fact exists to record which blocks have
    # NO probe, so its hit is evidence FOR this check, not against it.
    try:
        hits = [
            h for h in subprocess.run(
                ["grep", "-rl", "genus_from_hecke\\|genus-from-hecke",
                 str(REPO / "computations")],
                capture_output=True, text=True, timeout=120,
            ).stdout.split()
            if Path(h).name != Path(__file__).name
            and not Path(h).match("*/audits/*.witness.json")
        ]
    except Exception:                                    # pragma: no cover
        hits = ["<grep failed>"]
    check(
        not hits,
        "no producer in computations/ computes this lemma's matrix",
        "so \"verified numerically\" in the proof body is unbacked: there is\n"
        "no script and no witness carrying the claimed rank.  Excluded from\n"
        "the search: this probe, and the two corpus-wide audit inventories\n"
        "that name every block in the tree.\n"
        f"remaining hits: {hits}",
    )


# ----------------------------------------------------------------------------
# Section 3.  The H_3 two-dimensional irrep, built and verified from scratch.
# ----------------------------------------------------------------------------

q = sp.Symbol("q", positive=True)


def h3_two_dim_rep() -> tuple[sp.Matrix, sp.Matrix]:
    """The 2-dimensional irrep (2,1) of H_3(q), convention (s - q)(s + 1/q) = 0.

    Built by solving the braid relation rather than transcribed from a table --
    a transcribed rep is a place for a convention slip to hide, and the two
    assertions below are what make this one trustworthy.
    """
    qi = 1 / q
    c = sp.Symbol("c")
    s1 = sp.Matrix([[q, 1], [0, -qi]])
    s2 = sp.Matrix([[-qi, 0], [c, q]])
    sols = sp.solve(
        [sp.simplify(e) for e in (s1 * s2 * s1 - s2 * s1 * s2)], c, dict=True
    )
    assert sols, "no c satisfies the braid relation"
    cval = sols[0][c]
    s2 = s2.subs(c, cval)
    return sp.simplify(s1), sp.simplify(s2)


def section3() -> tuple[sp.Matrix, sp.Matrix]:
    print("\n=== 3. the (2,1) irrep of H_3(q), verified ===\n")
    s1, s2 = h3_two_dim_rep()

    qi = 1 / q
    check(
        sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2, 2),
        "braid relation  s1 s2 s1 = s2 s1 s2",
    )
    for name, s in (("s1", s1), ("s2", s2)):
        hecke = sp.simplify((s - q * sp.eye(2)) * (s + qi * sp.eye(2)))
        check(hecke == sp.zeros(2, 2), f"Hecke relation  ({name} - q)({name} + 1/q) = 0")
    check(
        sp.simplify(sp.trace(s1) - (q - qi)) == 0,
        "trace s1 = q - 1/q   (eigenvalues q, -1/q, as the irrep requires)",
    )
    return s1, s2


# ----------------------------------------------------------------------------
# Section 4.  The 6 x 5 matrix, exactly, and its rank.
# ----------------------------------------------------------------------------

# Torus knots T_{r,s}, gcd(r,s) = 1, s > r.  Seifert genus (r-1)(s-1)/2.
def genus(r: int, s: int) -> Fraction:
    return Fraction((r - 1) * (s - 1), 2)


def embeddable(g: int, rmax: int = 3) -> list[tuple[int, int]]:
    out = []
    for r in range(2, rmax + 1):
        for s in range(r + 1, 200):
            if sp.gcd(r, s) != 1:
                continue
            if genus(r, s) <= g:
                out.append((r, s))
    return sorted(out)


def character_row(r: int, s: int, s1: sp.Matrix, s2: sp.Matrix) -> list[sp.Expr]:
    """Row of M for T_{r,s}, over the 5 columns
    [ (2), (1,1) | (3), (2,1), (1,1,1) ].

    T_{2,s} is the closure of sigma_1^s in B_2 -- a word in H_2, so its H_3
    entries are structurally absent (0), and conversely.  That absence is the
    whole content of this probe and is not a modelling choice: a 2-strand word
    has no image in H_3 without a stabilisation, and stabilising is the other
    reading, handled in section 5.
    """
    qi = 1 / q
    if r == 2:
        # H_2 irreps are both 1-dimensional: sigma_1 |-> q  and  |-> -1/q.
        return [q**s, (-qi) ** s, sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    if r == 3:
        # T_{3,s} closes (sigma_1 sigma_2)^s.
        w2 = (s1 * s2) ** s
        return [
            sp.Integer(0),
            sp.Integer(0),
            sp.simplify(q ** (2 * s)),          # (3):     sigma_i |-> q
            sp.simplify(sp.trace(w2)),          # (2,1):   the 2-dim irrep
            sp.simplify((-qi) ** (2 * s)),      # (1,1,1): sigma_i |-> -1/q
        ]
    raise ValueError(r)


def section4(s1: sp.Matrix, s2: sp.Matrix) -> None:
    print("\n=== 4. the 6 x 5 character matrix at g = 4 ===\n")

    knots = embeddable(4)
    check(
        knots == [(2, 3), (2, 5), (2, 7), (2, 9), (3, 4), (3, 5)],
        "the 6 embeddable torus knots at g = 4 match the proof's table",
        f"{knots}",
    )

    M = sp.Matrix([character_row(r, s, s1, s2) for (r, s) in knots])
    rank = M.rank()
    print(f"    M is {M.shape[0]} x {M.shape[1]}; exact symbolic rank over Q(q) = {rank}\n")

    check(rank == 4, "rank(M) = 4, exactly -- NOT the claimed 5", f"rank = {rank}")

    # The structural reason, measured rather than asserted.
    top = M[:4, :]      # r = 2 rows
    bot = M[4:, :]      # r = 3 rows
    check(
        top[:, 2:] == sp.zeros(4, 3) and bot[:, :2] == sp.zeros(2, 2),
        "M is block-diagonal: r = 2 rows have no H_3 support and conversely",
    )
    check(
        top.rank() == 2 and bot.rank() == 2,
        "block ranks are 2 and 2",
        f"H_2 block (4 x 2) rank {top.rank()}; H_3 block (2 x 3) rank {bot.rank()}",
    )
    check(
        rank == top.rank() + bot.rank(),
        "rank is additive over the blocks (the named invariant)",
        "the H_3 block has only TWO rows at g = 4 (T_{3,4}, T_{3,5}) against\n"
        "THREE H_3 columns, so its rank is <= 2 for any q whatever.  No\n"
        "numerical verification at any q could have returned 5.",
    )

    # The criterion swept across the genus, which is the decisive table.
    #
    # NOTE, because I got this wrong first.  I expected rank 4 at g = 3 too,
    # i.e. that the criterion could not separate g = 3 from g = 4 at all.  It
    # can: the rank is 3 at g = 3 and 4 at g = 4, so the proof's exclusion of
    # g = 3 is correct on its own terms.  What is wrong is only the ACCEPTANCE
    # at g = 4, and the table below is what establishes that -- the criterion
    # is first met at g = 6, and the shortfall at g = 4 is by one.
    print("    rank of M against the stated target, by genus (exact over Q(q)):\n")
    print("      g   knots  (r=2, r=3)   rank   target   met?")
    table: list[tuple[int, int, int, int, int]] = []
    for g in range(1, 8):
        ks = embeddable(g)
        Mg = sp.Matrix([character_row(r, s, s1, s2) for (r, s) in ks])
        n2 = sum(1 for r, _ in ks if r == 2)
        n3 = sum(1 for r, _ in ks if r == 3)
        rk = Mg.rank()
        table.append((g, len(ks), n2, n3, rk))
        print(f"      {g}    {len(ks):2d}      ({n2}, {n3})       {rk}      5      "
              f"{'YES' if rk >= 5 else 'no'}")
    print()

    by_g = {g: rk for (g, _, _, _, rk) in table}
    check(
        by_g[3] == 3,
        "at g = 3 the rank is 3 -- so the proof's exclusion of g = 3 is CORRECT",
        "the criterion does discriminate; the defect is not that it is blind",
    )
    check(
        by_g[4] == 4 and by_g[5] == 4,
        "at g = 4 AND g = 5 the rank is 4: the criterion is NOT met",
        "g = 5 adds T_{2,11} -- a fifth r = 2 row against two H_2 columns, so it\n"
        "adds no rank.  Only a third r = 3 knot can move it.",
    )
    check(
        by_g[6] == 5,
        "the stated criterion is first met at g = 6, not g = 4",
        f"rank by genus: {by_g}",
    )


# ----------------------------------------------------------------------------
# Section 5.  Every other reading of "the matrix" also falls short of 5.
# ----------------------------------------------------------------------------

def section5(s1: sp.Matrix, s2: sp.Matrix) -> None:
    print("\n=== 5. the alternative readings ===\n")

    # Reading B: stabilise every word into H_3 (T_{2,s} as sigma_1^s in B_3).
    # Then the column set is the 3 irreps of H_3 alone and the matrix is 6 x 3.
    qi = 1 / q
    rows_b = []
    for (r, s) in embeddable(4):
        if r == 2:
            w = s1**s
            rows_b.append([q**s, sp.simplify(sp.trace(w)), (-qi) ** s])
        else:
            w2 = (s1 * s2) ** s
            rows_b.append(
                [sp.simplify(q ** (2 * s)), sp.simplify(sp.trace(w2)),
                 sp.simplify((-qi) ** (2 * s))]
            )
    Mb = sp.Matrix(rows_b)
    check(
        Mb.rank() <= 3 < 5,
        "reading B (stabilise into H_3): 6 x 3, rank <= 3",
        f"rank {Mb.rank()}; a 3-column matrix cannot have rank 5 at any g",
    )

    # Reading C: how many r = 3 knots would the stated criterion actually need,
    # and at what genus do they arrive?  Rank 5 needs rank 3 in the H_3 block,
    # hence at least 3 rows with r = 3.
    r3 = [(r, s) for (r, s) in embeddable(60) if r == 3]
    first_three = r3[:3]
    g_needed = max(genus(r, s) for (r, s) in first_three)
    check(
        [(r, s) for (r, s) in first_three] == [(3, 4), (3, 5), (3, 7)]
        and g_needed == 6,
        "reading A taken self-consistently gives g_min = 6, not 4",
        f"the first three r = 3 torus knots are {first_three}, and the third\n"
        f"(T_3,7) has Seifert genus {g_needed} -- so three H_3 rows, the minimum\n"
        "that could give rank 3 in that block, first exist at g = 6",
    )

    # ... and at g = 6 the proof's own restriction to r in {2,3} lapses.
    r4 = [(r, s) for (r, s) in
          [(4, s) for s in range(5, 20) if sp.gcd(4, s) == 1]
          if genus(r, s) <= 6]
    check(
        (4, 5) in r4,
        "and at g = 6 the restriction to r in {2,3} lapses: T_{4,5} embeds",
        f"T_4,5 has genus {genus(4, 5)} <= 6, so H_4 (5 more irreps) enters and\n"
        "the target dimension moves from 5 to 10.  The criterion has no fixed\n"
        "point at 4; pushed self-consistently it escalates rather than closing.",
    )


# ----------------------------------------------------------------------------

def main() -> int:
    print(__doc__.split("Run:")[0].strip()[:0] or "", end="")
    print("genus completeness rank probe")
    print("=" * 72)

    section1()
    section2()
    s1, s2 = section3()
    section4(s1, s2)
    section5(s1, s2)

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
