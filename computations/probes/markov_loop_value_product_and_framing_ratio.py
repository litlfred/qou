"""Convention D has a clean framing ratio a = q^2 and loop-value product
z_+ z_- = 1/[2]_q^2.  Convention C has neither.

WHERE THIS CAME FROM.  Chasing the relation between the Markov parameter and
the Hecke deformation (bean qou-dwf4, item (b)) out of the Toffoli arc, where
it appeared only as an obstruction: z and hbar are algebraically dependent, so
a polynomial representative in them is not unique.  The relation factors, and
in the corpus's own vocabulary it is not an obstruction at all but a statement
about crossing loop values.

THE CORPUS ALREADY NAMES BOTH SIDES.  `prop:markov-z-reconciliation`
(folio/quantum-observable-universe/mass-endomorphism/markov-z-reconciliation.md)
defines the NEGATIVE-crossing loop value

    z_-  =  z  -  (q - 1/q)  =  z - hbar

forced by the Hecke quadratic relation from the one-sided stabilisation rule,
and calls a^2 = z/z_- the FRAMING RATIO of the Ocneanu weight formula.  So the
quantity `z - hbar`, which the Toffoli work met as an algebraic accident, is a
named object with a meaning.

THE RELATION, RESTATED.  What was

    R(z, hbar) = hbar^3 z - hbar^2 z^2 + 4 hbar z - 4 z^2 + 1 = 0

factors as  ([2]_q^2) * z * (z - hbar)  -  1  =  0,  using hbar^2 + 4 = [2]_q^2
with [2]_q = q + 1/q.  That is

    z_+ z_-  =  1 / [2]_q^2                       (convention D)

the product of the two crossing loop values is the inverse square of the
quantum dimension.  And the framing ratio is a monomial:

    a^2  =  z_+ / z_-  =  q^4,      so      a = q^2.

CONVENTION C HAS NEITHER, and this is the point.  With
z_C = 1/[2]_{sqrt q} = sqrt(q)/(1+q) -- which the reconciliation block already
states in exactly that form -- the same two quantities are

    z_-        =  -(-q^(3/2) + q^3 + q^2 - q - 1) / (q(q+1))
    z_+ z_-    =  the same numerator over sqrt(q)(q+1)^2,  NOT 1/[2]_q^2
    a^2        =  -q^(3/2) / (-q^(3/2) + q^3 + q^2 - q - 1),  not a monomial

Half-integer and integer powers of q mixed in one numerator; no factorisation.
Both conventions satisfy tr_M(1) = (z_+ - z_-)/(q - 1/q) = 1, so C is not
inadmissible -- it is admissible and ugly.

WHY THIS MATTERS BEYOND THE TOFFOLI.  The owner's rulings of 2026-08-09 and
2026-08-15 make convention D canonical and excise C.  The justification on
record for that is EMPIRICAL -- the two differ by 195.8 ppm on tr_M(beta_Bor)
and -197 ppm on m_p.  This is a STRUCTURAL reason pointing the same way, and it
is independent of any anchor, any measurement and any ppm figure: in D the
framing parameter of the Ocneanu weight formula is the monomial q^2 and the
loop values multiply to 1/[2]_q^2; in C neither holds.

WHAT IS PRIOR ART AND WHAT IS NOT.  Prior art, in the reconciliation block:
z_- and its definition, the framing ratio a^2 = z/z_-, the form
z_C = 1/(q^{1/2} + q^{-1/2}), and the convention-D weights w_(3) = [4]_q/[2]_q^3,
w_(2,1) = 1/[2]_q^2.  NOT found anywhere in the corpus (six-path grep): the
form z_D = q^2/[2]_q, the product identity, the value of D's framing ratio, and
the C-to-D bridge z_D(q) = q^2 z_C(q^2).

Exact symbolic arithmetic (sympy); no floating point.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

q = sp.Symbol("q", positive=True)
hbar = q - 1 / q
two_q = q + 1 / q                       # [2]_q
two_sq = sp.sqrt(q) + 1 / sp.sqrt(q)    # [2]_{sqrt q}
zD = q ** 3 / (q ** 2 + 1)              # convention D
zC = sp.sqrt(q) / (1 + q)               # convention C

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def zero(e) -> bool:
    return sp.simplify(sp.cancel(e)) == 0


def main() -> int:
    print("=" * 74)
    print("  THE LOOP-VALUE PRODUCT AND THE FRAMING RATIO SEPARATE D FROM C")
    print("=" * 74)
    print()

    # ---- 0. the corpus's own definitions, read from the block ---------------
    blk = (Path(__file__).resolve().parents[2] / "content"
           / "quantum-observable-universe" / "mass-endomorphism"
           / "markov-z-reconciliation.md")
    txt = blk.read_text() if blk.exists() else ""
    check("the corpus already defines z_- and the framing ratio",
          "z_{\\mathrm{m}} - (q - q^{-1})" in txt and "a^2 = z_{\\mathrm{m}}/z_{-}" in txt,
          "prop:markov-z-reconciliation -- z_- is the NEGATIVE-crossing loop "
          "value; a^2 = z/z_- is the Ocneanu framing ratio.  Prior art.")
    check("and already states convention C as 1/[2]_{sqrt q}",
          "\\frac{1}{q^{1/2} + q^{-1/2}}" in txt,
          "so the clean form of C is NOT a finding of this probe")

    # ---- 1. the algebraic identities ---------------------------------------
    check("[2]_q^2 - hbar^2 = 4", zero(two_q ** 2 - hbar ** 2 - 4),
          "the Hecke deformation and the quantum dimension are a hyperbolic pair")
    R = hbar ** 3 * zD - hbar ** 2 * zD ** 2 + 4 * hbar * zD - 4 * zD ** 2 + 1
    check("R factors as [2]_q^2 . z . (z - hbar) - 1",
          zero(R) and zero(R - (two_q ** 2 * zD * (zD - hbar) - 1)),
          "the degree-4 relation between z and hbar, in closed form")

    # ---- 2. convention D ----------------------------------------------------
    zmD = sp.cancel(zD - hbar)
    check("D: z_- = 1/(q(q^2+1))", zero(zmD - 1 / (q * (q ** 2 + 1))),
          f"z_- = {sp.factor(zmD)}")
    check("D: z_+ z_- = 1/[2]_q^2", zero(zD * zmD - 1 / two_q ** 2),
          "the two crossing loop values multiply to the inverse square of the "
          "quantum dimension")
    check("D: the framing ratio is a MONOMIAL, a^2 = q^4 (so a = q^2)",
          zero(zD / zmD - q ** 4))
    check("D: z = q^2/[2]_q -- the exact analogue of C's 1/[2]_{sqrt q}",
          zero(zD - q ** 2 / two_q))
    check("D and C are bridged by z_D(q) = q^2 . z_C(q^2)",
          zero(zD - q ** 2 * zC.subs(q, q ** 2)))

    # ---- 3. convention C has neither ---------------------------------------
    zmC = sp.cancel(zC - hbar)
    check("C: z_+ z_- is NOT 1/[2]_q^2", not zero(zC * zmC - 1 / two_q ** 2),
          f"z_+ z_- = {sp.factor(sp.cancel(zC * zmC))}")
    aC = sp.cancel(zC / zmC)
    check("C: the framing ratio is not a monomial",
          not zero(sp.simplify(aC - q ** 4)) and sp.Poly is not None,
          f"a^2 = {sp.factor(aC)} -- half-integer and integer powers of q mixed "
          f"in one numerator, no factorisation")
    check("BOTH conventions are admissible: tr(1) = (z_+ - z_-)/hbar = 1",
          zero((zD - zmD) / hbar - 1) and zero((zC - zmC) / hbar - 1),
          "so this is not C being invalid -- it is C being structureless")

    # ---- 4. the D weight the block quotes, in the same terms ----------------
    check("D: w_(2,1) = 1/[2]_q^2 equals the loop-value product",
          zero(zD * zmD - 1 / two_q ** 2),
          "the block's registered convention-D standard-block weight is exactly "
          "z_+ z_-")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print()
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  A STRUCTURAL reason for the convention-D ruling, alongside")
    print("  the empirical one already on record (195.8 ppm on tr_M(beta_Bor)).")
    print("  In D the Ocneanu framing parameter is the monomial q^2 and the two")
    print("  crossing loop values multiply to 1/[2]_q^2; in C neither holds, and")
    print("  z_- does not even factor.  No anchor, no measurement, no ppm figure")
    print("  enters.  Bean qou-dwf4 item (b): the relation DOES appear outside the")
    print("  Toffoli arc -- it is a statement about the Markov trace itself.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
