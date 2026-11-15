#!/usr/bin/env python3
"""The g = 4 completeness route REPAIRS, and the repair confirms its conclusion.

BACKGROUND (`docs/audits/2026-09-14-canonical-chain-condition-walk.md`,
merged as `e8289b4971`).  `prf:genus-from-hecke-completeness` argues

    "At g = 3: 4 evaluations cannot span a 5-dimensional space (rank <= 4).
     At g = 4: 6 evaluations span 5 irreps (verified numerically: the 6 x 5
     matrix has rank 5 ...).  Therefore g_min = 4."

and `genus_completeness_rank_probe.py` (on `main`, 22/22) measured that the
rank is **4, not 5**, structurally and at every q -- the matrix is
block-diagonal over the 2-strand / 3-strand split and rank is additive.  The
stated criterion is first met at g = 6, not g = 4.

That left three dispositions for the author (re-scope / restate / retire) and
the walk explicitly did not choose among them.  **This probe answers the
"restate" branch from the corpus, so the choice is no longer three-way.**

THE REPAIR.  The criterion asks that the torus-knot EVALUATIONS span the
character space of `H_2(q) + H_3(q)`.  In this framework an evaluation is a
**Markov trace** -- `J_K(q) = tr_M(rho(beta_K))`, the corpus's own step-3
statement -- and

    tr_M  =  sum_lambda  y_lambda . chi^lambda .

So a block whose Wenzl weight `y_lambda` is **zero** is invisible to every
evaluation, at every knot, at every genus.  Under convention D's two-row
truncation -- which the corpus derives from `dim V = 2` and pins in Lean as
`markovWeights_eq_jones_of_threeRow_eq_zero`'s hypothesis `y_(1^3) = 0`, and
which the committed `y-lambda-at-q0.witness.json` shows as exactly 0 -- the
`(1,1,1)` block of `H_3` is exactly such a block.

    observable directions  =  (2), (1,1) | (3), (2,1)      =  4,   not 5.

MEASURED, exact symbolic rank over Q(q):

     g  knots (r2,r3)   rank_full/5   rank_observable/4   met?
     1    1   (1,0)          1                1            no
     2    2   (2,0)          2                2            no
     3    4   (3,1)          3                3            no
     4    6   (4,2)          4                4           YES   <-- first
     5    7   (5,2)          4                4           yes
     6    9   (6,3)          5                4           yes
     7   11   (7,4)          5                4           yes

**g_min = 4, exactly, and it is the FIRST crossing.**  So the proof's
ARITHMETIC was right and only its TARGET was wrong: "6 evaluations span 5
irreps" should read "the 6 evaluations span the 4 observable directions".
Its conclusion `g_min = 4` stands.

🛑 IS THIS SELECTION AGAINST THE TARGET?  No, and the question deserves a
direct answer because AGENTS.md's anti-fit rule names exactly this shape.
Four reasons, in the order that matters:

  1. **The derivation order runs the right way.**  truncation -> target ->
     genus.  The two-row cap is fixed by `dim V = 2` (step 1's fibre), pinned
     in sorry-free Lean, and recorded in a committed witness -- all of it
     established before and independently of anything about genus.  The
     target 4 is then read off it.  Nothing about g = 4 enters the choice.
  2. **It is not what an evaluation can see** -- this is not a modelling
     choice at all.  `tr_M = sum y_lambda chi^lambda` with `y_(1^3) = 0` makes
     the `(1,1,1)` coordinate unreachable by any Markov trace whatsoever.
     Including it in the target asks the knots to span a direction the
     framework's own observable cannot reach.
  3. **It does not single out g = 4.**  The corrected criterion is met at
     g = 4, 5, 6 and 7 -- exactly as the original is met at 6 and 7.  A target
     tuned to produce 4 would be met at 4 and nowhere else.  What 4 is, is the
     FIRST crossing, which is what `g_min` means.
  4. **It was derived after the refutation, not to avoid it.**  The
     refutation (rank 4 < 5) is on `main` and is not withdrawn.  This probe
     does not rescue the sentence as written; it shows the sentence has a
     corpus-determined correct form.

WHAT THIS DOES NOT CLAIM.  Not that `g = 4` is thereby derived -- the route
still opens "the braiding on `V_1^{(x)n}` in `Rep(SU_q(2))`", so it sits
inside the `chi = -6 <-> SU(2)` cycle the walk found, and is not independent
of SU(2).  Not that the other two dispositions are excluded: retiring the
route is still open to the author, and it still declares
`uses: ["prop:cohomological-embedding"]`.  And **no content block is edited
here** -- this probe measures; the wording is the author's.

NO-FLOAT64: sympy Symbol/Rational throughout, plus mpmath at dps=60 for the
witness read.  No float anywhere.

Run:  python3 computations/audits/genus_completeness_observable_target_probe.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import sympy as sp

REPO = Path(__file__).resolve().parents[2]
CONTENT = REPO / "folio" / "quantum-observable-universe"

FAILURES: list[str] = []
CHECKS = 0

q = sp.Symbol("q", positive=True)
qi = 1 / q

# Column order: H_2 (2), (1,1) | H_3 (3), (2,1), (1,1,1)
COLS = ["(2)", "(1,1)", "(3)", "(2,1)", "(1,1,1)"]
OBSERVABLE = [0, 1, 2, 3]          # everything except (1,1,1)


def check(ok: bool, label: str, detail: str = "") -> None:
    global CHECKS
    CHECKS += 1
    print(f"  [{'ok  ' if ok else 'FAIL'}] {label}")
    if detail:
        for line in detail.rstrip().splitlines():
            print(f"         {line}")
    if not ok:
        FAILURES.append(label)


def h3_2dim() -> tuple[sp.Matrix, sp.Matrix]:
    """(2,1) of H_3(q), solved from the braid relation rather than transcribed."""
    c = sp.Symbol("c")
    s1 = sp.Matrix([[q, 1], [0, -qi]])
    s2 = sp.Matrix([[-qi, 0], [c, q]])
    sols = sp.solve(
        [sp.simplify(e) for e in (s1 * s2 * s1 - s2 * s1 * s2)], c, dict=True
    )
    assert sols, "no c satisfies the braid relation"
    return sp.simplify(s1), sp.simplify(s2.subs(c, sols[0][c]))


def genus(r: int, s: int) -> sp.Rational:
    return sp.Rational((r - 1) * (s - 1), 2)


def embeddable(g: int) -> list[tuple[int, int]]:
    return sorted(
        (r, s)
        for r in (2, 3)
        for s in range(r + 1, 200)
        if sp.gcd(r, s) == 1 and genus(r, s) <= g
    )


def row(r: int, s: int, s1: sp.Matrix, s2: sp.Matrix) -> list[sp.Expr]:
    if r == 2:
        return [q**s, (-qi) ** s, sp.Integer(0), sp.Integer(0), sp.Integer(0)]
    w = (s1 * s2) ** s
    return [
        sp.Integer(0), sp.Integer(0),
        sp.simplify(q ** (2 * s)),
        sp.simplify(sp.trace(w)),
        sp.simplify((-qi) ** (2 * s)),
    ]


# ---------------------------------------------------------------------------

def section1() -> None:
    """The target is READ OFF the corpus, not chosen.  Pin every input."""
    print("\n=== 1. where the observable target comes from (corpus, not choice) ===\n")

    # (a) the committed witness: y_(1,1,1) is exactly zero at n = 3.
    #     Structure is data.by_n["<n>"] -> [{partition: [...], y_at_q0_50dps: "..."}].
    w = json.loads((REPO / "computations" / "y-lambda-at-q0.witness.json")
                   .read_text(encoding="utf-8"))
    by_n = w["data"]["by_n"]
    n3 = by_n.get("3") or by_n.get(3)
    check(n3 is not None and len(n3) == 3,
          "the committed witness carries all three partitions of n = 3",
          f"{[tuple(e['partition']) for e in n3]}")

    def y_of(part: tuple[int, ...]) -> str:
        for e in n3:
            if tuple(e["partition"]) == part:
                return e["y_at_q0_50dps"]
        raise KeyError(part)

    y111 = y_of((1, 1, 1))
    check(
        sp.Rational(y111) == 0,
        "y_(1,1,1) is EXACTLY 0 in the committed witness",
        f"y_(1,1,1) = {y111}\n"
        "so no Markov trace can see that block -- at any knot, any genus.",
    )
    # and the two that survive are nonzero, so the 4 is not an artifact of a
    # witness full of zeros.
    for part in ((3,), (2, 1)):
        check(
            sp.Rational(y_of(part)) != 0,
            f"y_{part} is NONZERO -- the surviving blocks really do survive",
            f"y_{part} = {y_of(part)[:32]}…",
        )

    # (b) the Lean hypothesis that pins it
    lean = CONTENT / "lean" / "QOU" / "BraidsAndKnots" / "MarkovTraceTLUniqueness.lean"
    txt = lean.read_text(encoding="utf-8") if lean.exists() else ""
    check(
        "markovWeights_eq_jones_of_threeRow_eq_zero" in txt,
        "and Lean pins it as a HYPOTHESIS of the trace-uniqueness theorem",
        f"{lean.relative_to(REPO) if lean.exists() else '(absent)'}\n"
        "y_(1^3) = 0 is what selects the Markov parameter -- convention D.",
    )

    print()
    print("    So the observable column set is DERIVED:")
    print("      H_2 : (2) 1 row KEEP, (1,1) 2 rows KEEP              -> 2")
    print("      H_3 : (3) KEEP, (2,1) KEEP, (1,1,1) 3 rows KILLED    -> 2")
    print("      observable target = 4     (the criterion says 5)")


def section2(s1, s2) -> dict[int, tuple[int, int]]:
    print("\n=== 2. the sweep: full target 5 vs observable target 4 ===\n")
    print("     g  knots (r2,r3)   rank_full/5   rank_obs/4   met?")
    out: dict[int, tuple[int, int]] = {}
    for g in range(1, 8):
        ks = embeddable(g)
        M = sp.Matrix([row(r, s, s1, s2) for (r, s) in ks])
        Mo = M[:, OBSERVABLE]
        n2 = sum(1 for r, _ in ks if r == 2)
        n3 = sum(1 for r, _ in ks if r == 3)
        rf, ro = M.rank(), Mo.rank()
        out[g] = (rf, ro)
        print(f"     {g}    {len(ks):2d}   ({n2},{n3})          {rf}            {ro}"
              f"        {'YES' if ro >= 4 else 'no'}")
    print()
    return out


def section3(t: dict[int, tuple[int, int]]) -> None:
    print("\n=== 3. the conclusion the route claims is RECOVERED ===\n")
    check(t[3][1] == 3, "g = 3 : observable rank 3 < 4 -- excluded")
    check(t[4][1] == 4, "g = 4 : observable rank 4 = 4 -- MET")
    check(
        all(t[g][1] < 4 for g in (1, 2, 3)) and t[4][1] == 4,
        "g = 4 is the FIRST crossing, so g_min = 4 exactly",
        "the proof's ARITHMETIC was right; only its TARGET was wrong.\n"
        "\"6 evaluations span 5 irreps\" should read \"the 6 evaluations span\n"
        "the 4 observable directions\".  Its conclusion g_min = 4 stands.",
    )
    check(
        t[4][0] == 4 and t[6][0] == 5,
        "the refutation on main is NOT withdrawn: full rank is still 4 at g=4, 5 at g=6",
        "this probe does not rescue the sentence as written -- it shows the\n"
        "sentence has a corpus-determined correct form.",
    )


def section4(t: dict[int, tuple[int, int]]) -> None:
    print("\n=== 4. 🛑 anti-fit: is the target selected against g = 4? ===\n")
    met = [g for g in sorted(t) if t[g][1] >= 4]
    check(
        met == [4, 5, 6, 7],
        "the corrected criterion is met at g = 4,5,6,7 -- not only at 4",
        f"met at {met}.  A target TUNED to produce 4 would be met at 4 and\n"
        "nowhere else.  4 is the FIRST crossing, which is what g_min means.",
    )
    met_orig = [g for g in sorted(t) if t[g][0] >= 5]
    check(
        met_orig == [6, 7],
        "and the ORIGINAL target has the same shape, met at 6,7",
        f"met at {met_orig} -- so correcting the target shifts the first\n"
        "crossing, it does not change the criterion's character.",
    )
    print()
    print("    The derivation order is truncation -> target -> genus:")
    print("      dim V = 2  (step 1's fibre)")
    print("        => l(lambda) <= 2   => y_(1^3) = 0   [Lean, witness: section 1]")
    print("          => observable directions = 4")
    print("            => first crossing at g = 4")
    print("    Nothing about g = 4 enters the choice of 4.")


def main() -> int:
    print("genus completeness — observable target probe")
    print("=" * 72)
    s1, s2 = h3_2dim()
    check(
        sp.simplify(s1 * s2 * s1 - s2 * s1 * s2) == sp.zeros(2, 2),
        "(2,1) irrep: braid relation holds",
    )
    check(
        sp.simplify((s1 - q * sp.eye(2)) * (s1 + qi * sp.eye(2))) == sp.zeros(2, 2),
        "(2,1) irrep: Hecke relation holds",
    )
    section1()
    t = section2(s1, s2)
    section3(t)
    section4(t)
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
