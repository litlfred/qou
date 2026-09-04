"""The canonical inhabitant of `CanonicalMarkovWeightsH3` is the sl_2 quantum
dimensions — closing an item the corpus records as open.

WHAT WAS OPEN.  `prop:qbeta-canonical-markov-weights-explicit-instance` builds
an inhabitant of the Lean class `CanonicalMarkovWeightsH3` from the
convention-C Markov parameter, and says so plainly:

    "It does not establish: that this instance is the canonical Wenzl-Markov
     weights. ... Identifying the canonical inhabitant remains open."

The MATH was not open -- that same block quotes the canonical convention-D
values `y_(3) = [4]_q/[2]_q^3 ~ 0.5054042`, `y_(2,1) = 1/[2]_q^2 ~ 0.2472979`,
`y_(1^3) = 0` and notes they satisfy the normalisation exactly.  What was
missing was the Lean INSTANCE carrying them.  This probe verifies the three
values the new instance uses, and why they are the canonical ones.

THE VALUES, in closed form without quantum-integer notation:

    y_(3)   = [4]_q/[2]_q^3 = (q^4 + 1)/(q^2 + 1)^2
    y_(2,1) = 1/[2]_q^2     = q^2/(q^2 + 1)^2
    y_(1^3) = 0

WHY THESE.  Convention D is the N = 2 member of the Ocneanu family
z_N = q^N/[N]_q -- its framing ratio a^2 = z/z_- is the monomial q^4, which
collapses every Ocneanu numerator into quantum integers and turns the weight
product into the hook-content formula w_lam = dim_q(V_lam^{sl_N})/[N]_q^n
(`ocneanu_weights_are_sl_n_quantum_dimensions.py`, 13/13).  So the three values
are DERIVED from the trace, not chosen to satisfy the class axiom.  Checked
below: they agree with the Ocneanu product at z_D on every partition of 3.

The `y_(1^3) = 0` is the sl_2 ROW BOUND, not a coincidence: a partition with
more than N rows has a cell of content -N, whose numerator factor carries
[0]_q = 0.

THE NORMALISATION IS AN IDENTITY, not a constraint that had to be arranged.
The class axiom is y_(3) + 2 y_(2,1) + y_(1^3) = 1, and

    (q^4 + 1) + 2 q^2  =  (q^2 + 1)^2

so it holds for every q, with no positivity hypothesis needed.  Equivalently
[4]_q = ([2]_q^2 - 2)[2]_q, hence [4]/[2]^3 = 1 - 2/[2]^2.

WHAT THE PRE-EXISTING INSTANCE IS.  `explicitInstance` uses the convention-C
parameter z_C = sqrt(q)/(1+q), giving (z, 1/2 - z, z).  It satisfies the class
axiom -- it is a valid inhabitant, and the block never claimed more -- but it
is not the production trace's weight set, and the two differ on all three
blocks.  Verified below.  This probe does not disturb it; the new declaration
is a `def`, not a second `instance`, so instance resolution is unchanged.

Exact symbolic arithmetic (sympy over Q(q)); the convention-C comparison is
done in s = sqrt(q), where its expressions are rational.
"""

from __future__ import annotations

import sys
from pathlib import Path

import sympy as sp

q = sp.Symbol("q", positive=True)
s = sp.Symbol("s", positive=True)          # s = sqrt(q)
Q0 = sp.Rational("1.1099785827513808")

CHECKS: list[tuple[str, bool]] = []


def check(name, ok, detail=""):
    CHECKS.append((name, bool(ok)))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
    if detail:
        print(f"         {detail}")


def qint(m, v=q):
    return sp.cancel(sp.together((v ** m - v ** (-m)) / (v - 1 / v)))


def cells(lam):
    return [(i, j) for i, r in enumerate(lam) for j in range(r)]


def hook(lam, i, j):
    return (lam[i] - j - 1) + sum(1 for r in range(i + 1, len(lam)) if lam[r] > j) + 1


def ocneanu(lam, z, *, var=q, hb=None):
    hb = (var - 1 / var) if hb is None else hb
    zm = z - hb
    num = den = sp.Integer(1)
    for (i, j) in cells(lam):
        c, h = j - i, hook(lam, i, j)
        num *= z * var ** c - zm * var ** (-c)
        den *= var ** h - var ** (-h)
    return sp.cancel(sp.together(num / den))


# the three values the new Lean instance carries
Y3 = (q ** 4 + 1) / (q ** 2 + 1) ** 2
Y21 = q ** 2 / (q ** 2 + 1) ** 2
Y111 = sp.Integer(0)


def main() -> int:
    print("=" * 74)
    print("  THE CANONICAL CanonicalMarkovWeightsH3 INHABITANT")
    print("=" * 74)
    print()

    root = Path(__file__).resolve().parents[2]
    md = (root / "content" / "quantum-observable-universe" / "mass-endomorphism"
          / "qbeta-canonical-markov-weights-explicit-instance-proof.md")
    txt = md.read_text() if md.exists() else ""
    check("the corpus records this as open, and quotes the values",
          "Identifying the canonical inhabitant remains open" in txt
          and "[4]_q/[2]_q^3" in txt,
          "the math was recorded; the Lean instance was what was missing")

    zD = q ** 2 / qint(2)
    check("z_D = q^2/[2]_q is the corpus's q^3/(q^2+1)",
          sp.simplify(sp.cancel(zD - q ** 3 / (q ** 2 + 1))) == 0)

    # ---- 1. the values ARE the Ocneanu weights at z_D -----------------------
    for lam, val, name in [((3,), Y3, "[4]_q/[2]_q^3"),
                           ((2, 1), Y21, "1/[2]_q^2"),
                           ((1, 1, 1), Y111, "0")]:
        check(f"y_{lam} = {name} equals the Ocneanu weight at z_D",
              sp.simplify(sp.cancel(ocneanu(lam, zD) - val)) == 0,
              "derived from the trace, not chosen to satisfy the class axiom")

    check("the closed forms are the quantum-integer ones",
          sp.simplify(sp.cancel(Y3 - qint(4) / qint(2) ** 3)) == 0
          and sp.simplify(sp.cancel(Y21 - 1 / qint(2) ** 2)) == 0)

    # ---- 2. the normalisation is an identity --------------------------------
    check("the class axiom y_(3) + 2 y_(2,1) + y_(1^3) = 1 is an IDENTITY",
          sp.simplify(sp.cancel(Y3 + 2 * Y21 + Y111 - 1)) == 0,
          "(q^4+1) + 2q^2 = (q^2+1)^2 -- holds for every q, no positivity "
          "hypothesis needed")
    check("equivalently [4]_q = ([2]_q^2 - 2)[2]_q",
          sp.simplify(sp.cancel(qint(4) - (qint(2) ** 2 - 2) * qint(2))) == 0)

    # ---- 3. the numbers match what the block quotes -------------------------
    n3 = float(sp.N(Y3.subs(q, Q0), 12))
    n21 = float(sp.N(Y21.subs(q, Q0), 12))
    check("at q0 the values are the block's quoted 0.5054042, 0.2472979, 0",
          abs(n3 - 0.5054042) < 5e-8 and abs(n21 - 0.2472979) < 5e-8,
          f"y_(3) = {n3:.10f}, y_(2,1) = {n21:.10f}, y_(1^3) = 0 exactly")

    # ---- 4. the pre-existing instance is a different, valid inhabitant ------
    qs, hs = s ** 2, s ** 2 - 1 / s ** 2
    zC = s / (1 + qs)
    e3, e21, e111 = zC, sp.Rational(1, 2) - zC, zC
    check("explicitInstance satisfies the class axiom too (it is valid)",
          sp.simplify(sp.cancel(e3 + 2 * e21 + e111 - 1)) == 0,
          "z + 2(1/2 - z) + z = 1, for any z -- which is why it inhabits the "
          "class without being the production weights")
    diff = [n for n, a, b in [("y_(3)", Y3.subs(q, qs), e3),
                              ("y_(2,1)", Y21.subs(q, qs), e21),
                              ("y_(1^3)", Y111, e111)]
            if sp.simplify(sp.cancel(sp.together(a - b))) != 0]
    check("and it differs from the canonical one on ALL THREE blocks",
          len(diff) == 3, f"differs at {diff}")

    n_ok = sum(1 for _, ok in CHECKS if ok)
    print()
    print("=" * 74)
    print(f"  {n_ok}/{len(CHECKS)} assertions")
    print("=" * 74)
    print()
    print("  VERDICT.  'Identifying the canonical inhabitant remains open' is")
    print("  CLOSED.  The canonical weights are the U_q(sl_2) quantum dimensions")
    print("  over [2]_q^3, derived from the framing ratio rather than fitted, and")
    print("  they satisfy the class axiom as an identity.  The Lean declaration is")
    print("  a `def`, not a second `instance`, so resolution is unchanged --")
    print("  promoting it to the default is a separate decision.")
    return 0 if n_ok == len(CHECKS) else 1


if __name__ == "__main__":
    sys.exit(main())
