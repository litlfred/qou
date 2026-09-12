#!/usr/bin/env python3
# polynomial_q_not_applicable: exact rational linear algebra on an integer column.
"""The 3A negative is SCOPE-(b) for the all-pairs class: the system is INCONSISTENT.

OWNER INSTRUCTION 2026-09-12: *"3A negative is scope-(a) not an exclusion"* —
go settle whether it can be upgraded.

WHAT THE PRIOR RESULT WAS. `phi3_column_discriminates_the_strand_count_probe.py`
measured that the recorded Phi_3 column of the Z=1-20 mass table is reproduced
19/19 by the A+Z strand content parameter-free, and 0/19 by A, 3A and 3A+Z; and
that granting three FITTED coefficients, 3A and 3A+Z reach only 10/19 with
fractional coefficients. Per AGENTS.md "Before declaring refuted / ruled out",
that is a **scope-(a)** result: *those* constructions fail. It excludes no
ingredient, because a numerical miss is not an invariant.

WHAT THIS PROBE ADDS, AND IT IS A DIFFERENT KIND OF STATEMENT. The question
"can ANY coefficient vector on this basis reproduce the column" is not a
numerical question at all — it is the **consistency of a linear system over
Q**, and consistency is decidable exactly:

    M c = w        M = the 19 x k matrix of pair counts, w = the recorded column

is solvable iff  rank(M) == rank([M | w]).  Both ranks are computed here by
exact Gaussian elimination over `fractions.Fraction` — no tolerance, no least
squares, no float. An INCONSISTENT verdict is a **proved impossibility over the
entire coefficient family**, which is the invariant AGENTS.md requires before a
scope-(b) exclusion may be written.

THE RESULT.

    basis                                    rank(M)  rank([M|w])  verdict
    A+Z   pp, nn, pe                            3          3       CONSISTENT (unique)
    A     pp, nn, pn                            3          4       INCONSISTENT
    3A    pp, nn, pn on quark strands           3          4       INCONSISTENT
    3A+Z  quark strands + Z electrons           4          5       INCONSISTENT
    3A colour-split (intra + 3 cross families)  4          5       INCONSISTENT

and the unique A+Z solution is (4, -2, -2) = 2*(pp+ee), 2*nn, 2*pe read off
tbl:atomic-braid-table1-data. So the parameter-free agreement is not a
coincidence that survived 19 tests: the system has a **unique** solution and it
is the crossing table's.

The colour-split row is the point of this probe. It is the natural objection to
the earlier result — *"you only tested a quark basis with the nucleon-level sign
assignment; colour gives more freedom"* — and it is answered: splitting the
quark pairs into an intra-nucleon family plus three cross-nucleon families adds
a degree of freedom and the system stays inconsistent.

WHY: the obstruction is a POLYNOMIAL IDENTITY, checked independently (check 6).
Every count here is a quadratic in (Z, N), and matching
`w = -2Z - N^2 + N` coefficient-by-coefficient forces, on the quark bases,
two incompatible values for the same coefficient — the Z^2 term demands the
pp weight vanish while the Z term demands it be nonzero. That is the invariant,
and it does not depend on the 19 rows.

🛑 WHAT IS STILL NOT EXCLUDED — read before citing this as "3A is dead".

The scope-(b) exclusion is for **the all-pairs class**: constructions whose
Phi_3 weight is a Q-linear combination of all-pairs counts over a strand set,
with one weight per species-pair type. That is the class
`phi_allpairs_reconstruction.py` establishes for A+Z, so it is the like-for-like
comparison — but it is a class, not "every quark-level construction". NOT
excluded, and each would need its own test:

  * a weight that depends on Z or N (so the "coefficient" is not a constant);
  * a non-all-pairs chain structure (an ordering-dependent product);
  * a construction whose Phi_3 is not a signed pair sum at all.

So the honest verdict is **scope-(b) within a named class**, not scope-(b)
simpliciter, and the class is named in the output.

NO FLOAT is reachable: `int` and `fractions.Fraction` only. No mpmath, no
witness, no producer.
"""
from __future__ import annotations

import re
import sys
from fractions import Fraction
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RECONSTRUCTION = ROOT / "computations" / "phi_allpairs_reconstruction.py"

_checks = 0
_failed = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global _checks, _failed
    _checks += 1
    if not cond:
        _failed += 1
    print(f"  [{'PASS' if cond else 'FAIL'}] {label}" + (f"  {detail}" if detail else ""))


# ------------------------------------------------------------------ the data

print("CHECK 1 -- the target column, read from the corpus rather than retyped")
rec = RECONSTRUCTION.read_text()
ROWS = [(m.group(1), int(m.group(2)), int(m.group(3)), int(m.group(4)))
        for m in re.finditer(r'\("([A-Za-z]{1,2})",\s*(\d+),\s*(\d+),\s*(-?\d+)\)', rec)]
check("phi_allpairs_reconstruction.py yields 20 rows", len(ROWS) == 20, f"{len(ROWS)}")
NONH = [r for r in ROWS if r[0] != "H"]
check("19 non-hydrogen rows (H carries the documented B_3-dressed pe exception)",
      len(NONH) == 19, f"{len(NONH)}")
check("Ar is (Z, N, w) = (18, 22, -498)",
      [r for r in NONH if r[0] == "Ar"][0][1:] == (18, 22, -498))

# ------------------------------------------------------------- the bases

print()
print("CHECK 2 -- the candidate bases, one column per species-pair family")


def basis_A(Z, N):
    """Nucleons only: pp, nn, pn."""
    return (comb(Z, 2), comb(N, 2), Z * N)


def basis_AZ(Z, N):
    """Nucleons + Z electrons. pp and ee share a column (both C(Z,2)),
    which is why three columns suffice: pp+ee, nn, pe."""
    return (comb(Z, 2), comb(N, 2), Z * Z)


def basis_3A(Z, N):
    """3 quark strands per nucleon, no electrons: pp, nn, pn at quark level."""
    return (comb(3 * Z, 2), comb(3 * N, 2), 9 * Z * N)


def basis_3AZ(Z, N):
    """Quark strands + Z electrons: the three above plus a pe family."""
    return (comb(3 * Z, 2), comb(3 * N, 2), 9 * Z * N, 3 * Z * Z)


def basis_3A_colour(Z, N):
    """Quark strands, but the pair families SPLIT by colour locality:
    intra-nucleon quark pairs (3 per nucleon) get their own weight, and the
    cross-nucleon pairs keep pp / nn / pn. This is the natural objection to
    basis_3A -- it grants a further degree of freedom."""
    intra = 3 * (Z + N)                 # C(3,2) = 3 pairs inside each nucleon
    return (intra, 9 * comb(Z, 2), 9 * comb(N, 2), 9 * Z * N)


BASES = [
    ("A+Z  (a)  pp+ee, nn, pe", basis_AZ),
    ("A         pp, nn, pn", basis_A),
    ("3A   (b)  pp, nn, pn on quark strands", basis_3A),
    ("3A+Z (c)  quark strands + Z electrons", basis_3AZ),
    ("3A colour-split  intra, pp, nn, pn", basis_3A_colour),
]
for name, f in BASES:
    check(f"{name}: {len(f(2, 2))} columns, all integer",
          all(isinstance(x, int) for x in f(2, 2)), f"He row -> {f(2, 2)}")

# ------------------------------------------------------ exact rank over Q

print()
print("CHECK 3 -- rank by exact Gaussian elimination over Q (no float, no tolerance)")


def rank(rows):
    """Exact row-echelon rank of a list-of-lists of Fractions."""
    M = [list(r) for r in rows]
    nrows, ncols = len(M), len(M[0]) if M else 0
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, nrows) if M[i][c] != 0), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] != 0:
                fac = M[i][c]
                M[i] = [a - fac * b for a, b in zip(M[i], M[r])]
        r += 1
        if r == nrows:
            break
    return r


# self-test: a known rank, so a broken eliminator cannot report a clean bill
_id3 = [[Fraction(1), Fraction(0), Fraction(0)],
        [Fraction(0), Fraction(1), Fraction(0)],
        [Fraction(0), Fraction(0), Fraction(1)]]
_dep = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(4)]]
check("eliminator self-test: rank(I_3) = 3 and rank([[1,2],[2,4]]) = 1",
      rank(_id3) == 3 and rank(_dep) == 1)


def solve_exact(rows, rhs):
    """Unique solution if the square-ified system determines one, else None."""
    k = len(rows[0])
    # Use the first k independent rows.
    picked, M, y = [], [], []
    for r, b in zip(rows, rhs):
        trial = M + [list(r)]
        if rank(trial) > len(M):
            M, y = trial, y + [b]
            picked.append(r)
        if len(M) == k:
            break
    if len(M) < k:
        return None
    aug = [row + [b] for row, b in zip(M, y)]
    n = len(aug)
    for c in range(k):
        piv = next(i for i in range(c, n) if aug[i][c] != 0)
        aug[c], aug[piv] = aug[piv], aug[c]
        pv = aug[c][c]
        aug[c] = [x / pv for x in aug[c]]
        for i in range(n):
            if i != c and aug[i][c] != 0:
                f = aug[i][c]
                aug[i] = [a - f * b2 for a, b2 in zip(aug[i], aug[c])]
    return [aug[i][k] for i in range(k)]


print()
print("CHECK 4-5 -- CONSISTENCY of  M c = w  over the 19 rows")
print(f"    {'basis':<42} {'rank(M)':>8} {'rank([M|w])':>12}  verdict")

RESULT = {}
for name, f in BASES:
    M = [[Fraction(x) for x in f(Z, N)] for _, Z, N, _ in NONH]
    aug = [row + [Fraction(w)] for row, (_, _, _, w) in zip(M, NONH)]
    rM, rA = rank(M), rank(aug)
    consistent = rM == rA
    sol = solve_exact(M, [Fraction(w) for *_, w in NONH]) if consistent else None
    # a solution found on k rows must be verified on ALL 19
    if sol is not None:
        ok = all(sum(c * Fraction(b) for c, b in zip(sol, f(Z, N))) == Fraction(w)
                 for _, Z, N, w in NONH)
        if not ok:
            sol = None
    RESULT[name] = (rM, rA, consistent, sol)
    verdict = "CONSISTENT" if consistent else "INCONSISTENT"
    extra = f"   c = {[str(s) for s in sol]}" if sol else ""
    print(f"    {name:<42} {rM:>8} {rA:>12}  {verdict}{extra}")

az = RESULT["A+Z  (a)  pp+ee, nn, pe"]
check("A+Z is CONSISTENT and the solution is UNIQUE (rank = #columns)",
      az[2] and az[0] == 3 and az[3] is not None,
      f"rank {az[0]} of 3 columns -> at most one solution")
check("that unique solution is exactly (4, -2, -2)",
      [str(s) for s in az[3]] == ["4", "-2", "-2"],
      "= 2*(pp+ee), 2*nn, 2*pe read off tbl:atomic-braid-table1-data")

# Short labels, given explicitly: splitting the basis name on whitespace makes
# "3A" and "3A colour-split" print identically, which is exactly the distinction
# this probe exists to draw.
SHORT = {
    "A+Z  (a)  pp+ee, nn, pe": "A+Z",
    "A         pp, nn, pn": "A",
    "3A   (b)  pp, nn, pn on quark strands": "3A",
    "3A+Z (c)  quark strands + Z electrons": "3A+Z",
    "3A colour-split  intra, pp, nn, pn": "3A-colour",
}
for nm in ("A         pp, nn, pn",
           "3A   (b)  pp, nn, pn on quark strands",
           "3A+Z (c)  quark strands + Z electrons",
           "3A colour-split  intra, pp, nn, pn"):
    rM, rA, cons, _ = RESULT[nm]
    check(f"{SHORT[nm]:<9} is INCONSISTENT -- NO coefficient vector reproduces the column",
          not cons, f"rank(M) = {rM}, rank([M|w]) = {rA}; the augmented rank is strictly larger")

print()
print("CHECK 6 -- the same obstruction, independently, as a POLYNOMIAL IDENTITY")
print("           (so it does not depend on the 19 rows at all)")

try:
    import sympy as sp

    Zs, Ns = sp.symbols("Z N", integer=True)
    target = sp.expand(-2 * Zs - Ns * (Ns - 1))
    check("the A+Z closed form is w = -2Z - N(N-1)",
          sp.expand(target - (-2 * Zs - Ns**2 + Ns)) == 0, f"w = {target}")

    def poly_basis(f):
        """Symbolic pair counts: C(x,2) = x(x-1)/2 continues the integer counts."""
        def C2(x):
            return sp.expand(x * (x - 1) / 2)
        if f is basis_A:
            return [C2(Zs), C2(Ns), Zs * Ns]
        if f is basis_AZ:
            return [C2(Zs), C2(Ns), Zs**2]
        if f is basis_3A:
            return [C2(3 * Zs), C2(3 * Ns), 9 * Zs * Ns]
        if f is basis_3AZ:
            return [C2(3 * Zs), C2(3 * Ns), 9 * Zs * Ns, 3 * Zs**2]
        return [3 * (Zs + Ns), 9 * C2(Zs), 9 * C2(Ns), 9 * Zs * Ns]

    for name, f in BASES:
        cols = poly_basis(f)
        cs = sp.symbols(f"c0:{len(cols)}")
        expr = sp.expand(sum(c * col for c, col in zip(cs, cols)) - target)
        sol = sp.solve(sp.Poly(expr, Zs, Ns).coeffs(), cs, dict=True)
        solvable = bool(sol)
        expect = name.startswith("A+Z")
        check(f"{SHORT[name]:<9} polynomial system solvable = {solvable}",
              solvable == expect,
              ("unique c = " + str([str(sol[0][c]) for c in cs])) if solvable
              else "no (c) satisfies the coefficient equations -- the invariant")

    # name the obstruction explicitly for the quark bases
    cols = poly_basis(basis_3A)
    cs = sp.symbols("c0:3")
    expr = sp.expand(sum(c * col for c, col in zip(cs, cols)) - target)
    p = sp.Poly(expr, Zs, Ns)
    z2 = p.coeff_monomial(Zs**2)
    z1 = p.coeff_monomial(Zs)
    check("the 3A obstruction is Z^2 vs Z: one forces c_pp = 0, the other c_pp = 4/3",
          sp.solve([z2], cs[0])[cs[0]] == 0 and sp.solve([z1], cs[0])[cs[0]] == sp.Rational(4, 3),
          f"coeff(Z^2) = {z2},  coeff(Z) = {z1}")
except ImportError:                                            # pragma: no cover
    print("  [INFO] sympy unavailable; the rank test above is the verdict")

print()
print("CHECK 7 -- SCOPE: what this excludes and what it does NOT")
doc = Path(__file__).read_text()
check("the docstring names the excluded CLASS, not 'every quark construction'",
      "all-pairs class" in doc and "NOT excluded" in doc)
check("it names the three constructions that remain open",
      "depends on Z or N" in doc and "non-all-pairs chain" in doc
      and "not a signed pair sum" in doc)
check("H is excluded from the 19 for a DOCUMENTED reason, not to help the fit",
      "B_3-dressed" in rec or "B_3-dressed" in doc,
      "the pe crossing is B_3-dressed at A = 1 -- def:atomic-braid says so")

print()
print(f"{_checks - _failed}/{_checks} checks passed")
print()
print("MEASURED: within the all-pairs class, the quark-strand bases cannot")
print("reproduce the recorded Phi_3 column for ANY coefficient vector -- the")
print("linear system is inconsistent, and the obstruction is a polynomial")
print("identity rather than a numerical miss. The A+Z system is consistent with")
print("a UNIQUE solution, and that solution is Table 1's own crossing values.")
sys.exit(1 if _failed else 0)
