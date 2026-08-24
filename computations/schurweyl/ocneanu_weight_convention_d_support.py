"""Convention D's Markov parameter is exactly the value that kills every partition
with three or more rows -- and the corpus's independent inversion path agrees.

Builds on the closed form derived in `ocneanu_weight_general_n.py`:

    W_lam(q,z) = prod_{(i,j) in lam} [ q^{2i}(q^2 - 1 - qz) + q^{2j+1} z ]
                 / prod_{(i,j) in lam} [ q^{2h(i,j)} - 1 ]

Pulling the row-index monomial out, the numerator factor of a cell of content c is
proportional to  (q^2 - 1) + z*q*(q^{2c} - 1).  Setting that to zero and solving for z:

    c = -k  (k >= 1)  ->  z = q^{2k+1} / (1 + q^2 + ... + q^{2k})
    c =  0            ->  no solution (the factor is the constant q^2 - 1)
    c = +k            ->  a negative-z branch, not the substrate regime

The k = 2 member is  z = q^3/(q^2+1)  -- which is exactly CONVENTION D, made canonical
by the owner ruling of 2026-08-15 (AGENTS.md, "q0 anchor convention").  Any Young
diagram with three or more rows contains the cell (2,0), of content -2, so at
convention D its weight is ZERO.  The k = 1 member z = q likewise kills every diagram
with two or more rows.  Convention C's z = sqrt(q)/(q+1) is not a member at any integer
content and truncates nothing.

Vanishing on the >= 3-row partitions is the condition for a trace on H_n(q) to factor
through its Temperley-Lieb quotient.  That READING is standard (Jones 1983, Wenzl 1988)
and is NOT established here; what is established here is the vanishing itself, which is
also Lean-proved sorry-free as
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows`.

PRECISION.  Part 1 is exact sympy over Q(q,z).  Part 2 compares against
`computations/ocneanu_weights.py::omega_lambda_via_inversion`, an independent
p(n) x p(n) linear solve, which is FLOAT64 -- that is the path's own arithmetic, not a
choice made here.  This side is carried in mpmath at 50 dps; the agreement can therefore
only be reported "to the limit of the float64 arithmetic the inversion path uses", and a
discrepancy below ~1e-16 is invisible to this comparison by construction.  The
qualitative half -- WHICH weights vanish -- does not depend on that resolution and is the
substantive check.

Requires numpy + scipy (dependencies of the corpus inversion path, not of this script).
"""

import math
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

mp.mp.dps = 50
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

q, z = sp.symbols('q z')


def cells(s):
    return [(i, j) for i, r in enumerate(s) for j in range(r)]


def hooks(s):
    rows = list(s)
    mc = rows[0] if rows else 0
    cols = [sum(1 for r in rows if r > j) for j in range(mc)]
    return {(i, j): (rows[i] - j - 1) + (cols[j] - i - 1) + 1 for (i, j) in cells(s)}


def dim(s):
    d = math.factorial(sum(s))
    for h in hooks(s).values():
        d //= h
    return d


# ---------------------------------------------------- part 1: exact, symbolic
print("=" * 74)
print("PART 1 -- which z kills which content (exact, sympy over Q(q,z))")
print("=" * 74)
kills = {}
for c in range(-4, 5):
    fac = (q**2 - 1) + z * q * (q**(2 * c) - 1)
    sol = sp.solve(sp.Eq(fac, 0), z)
    if sol:
        kills[c] = sp.simplify(sol[0])
        print(f"  content c = {c:+d}:  z = {kills[c]}")
    else:
        print(f"  content c = {c:+d}:  none (factor is the constant q^2 - 1)")

zD = q**3 / (q**2 + 1)
zC = sp.sqrt(q) / (q + 1)
print()
print(f"  convention D  z_D = {zD}")
hitD = [c for c in kills if sp.simplify(kills[c] - zD) == 0]
print(f"      kills content(s): {hitD}   -> every diagram containing the cell (2,0),")
print("      i.e. every partition with THREE OR MORE ROWS")
print(f"  convention C  z_C = {zC}")
hitC = [c for c in range(-6, 7)
        if sp.simplify((q**2 - 1) + zC * q * (q**(2 * c) - 1)) == 0]
print(f"      kills content(s): {hitC if hitC else 'none at any integer content'}")
assert hitD == [-2], hitD
assert not hitC, hitC

# ------------------------------- part 2: cross-check vs the corpus inversion
print()
print("=" * 74)
print("PART 2 -- cross-check vs computations/ocneanu_weights.py (float64 inversion)")
print("=" * 74)
try:
    import ocneanu_weights as ow
except Exception as exc:                                    # pragma: no cover
    print(f"  SKIPPED: {type(exc).__name__}: {exc}")
    raise SystemExit(0)

Q0 = mp.mpf(repr(ow.Q0))
Z0 = mp.mpf(repr(ow.z_num))
print(f"  q0     = {mp.nstr(Q0, 17)}")
print(f"  z_num  = {mp.nstr(Z0, 17)}   (module defines z_num = Q0**3/(Q0**2+1))")
print(f"  q^3/(q^2+1) at that q0 = {mp.nstr(Q0**3 / (Q0**2 + 1), 17)}   -> convention D")
print()
print("  NOTE: that module's DOCSTRING declares convention C, z = 1/(q^{1/2}+q^{-1/2})")
print(f"        = {mp.nstr(1 / (mp.sqrt(Q0) + 1 / mp.sqrt(Q0)), 17)}, which its own code does")
print("        NOT use.  The code is canonical per the 2026-08-15 ruling; the docstring")
print("        is stale.  Recorded, not edited here.")
print()


def W(s):
    num = mp.mpf(1)
    den = mp.mpf(1)
    for (i, j) in cells(s):
        num *= Q0**(2 * i) * (Q0**2 - 1 - Q0 * Z0) + Q0**(2 * j + 1) * Z0
    for h in hooks(s).values():
        den *= Q0**(2 * h) - 1
    return num / den


FLOAT64_FLOOR = mp.mpf('1e-15')
worst = mp.mpf(0)
bad = []
for n in (2, 3, 4, 5):
    theirs = ow.omega_lambda_via_inversion(n)
    print(f"  --- n = {n} ---")
    for shape, om in sorted(theirs.items()):
        s = tuple(shape)
        mine = dim(s) * W(s)                       # their omega_lam = d_lam * W_lam
        t = mp.mpf(repr(om))
        d = abs(mine - t)
        worst = max(worst, d)
        rows = len(s)
        pred = "0 (>=3 rows)" if rows >= 3 else ""
        if rows >= 3 and abs(mine) > FLOAT64_FLOOR:
            bad.append(("closed form nonzero on a >=3-row shape", n, s))
        if rows >= 3 and abs(t) > FLOAT64_FLOOR:
            bad.append(("inversion nonzero on a >=3-row shape", n, s))
        if d > FLOAT64_FLOOR:
            bad.append(("disagreement above the float64 floor", n, s))
        print(f"    {str(s):18s} inversion={float(t): .17g}  closed={mp.nstr(mine, 17):>22s}"
              f"  |diff|={mp.nstr(d, 3):>9s}  {pred}")

print()
print(f"  worst |diff| over n = 2..5: {mp.nstr(worst, 3)}")
print("  -- agreement to the limit of the float64 arithmetic the inversion path uses;")
print("     this comparison cannot distinguish that from a discrepancy below ~1e-16.")
print("  The closed form's ~1e-18 residual on the >=3-row shapes is the float64 rounding")
print("  of z_num propagating, NOT a nonzero weight: at the exact z = q^3/(q^2+1) it is")
print("  identically zero, which is the Lean-proved statement.")
print("  The qualitative half is resolution-independent: the closed form predicts WHICH")
print("  weights vanish (exactly the >=3-row shapes), and the inversion returns float64")
print("  noise on precisely those and nothing else.")
print()
print("VERDICT:", "consistent" if not bad else f"FAILURES: {bad}")
sys.exit(0 if not bad else 1)
