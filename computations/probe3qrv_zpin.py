"""Bean qou-3qrv, part 3: does the TL condition y_(1^3)=0 pin z UNIQUELY?

A normalised Markov trace on H_3(q) is determined by its Ocneanu parameter
z via its values on the three class representatives:

    tr(1) = 1,      tr(sigma_1) = z,      tr(sigma_1 sigma_2) = z^2.

Writing tr = sum_lambda y_lambda chi^lambda and solving the resulting 3x3
linear system gives y_lambda(z) explicitly. Then:

    y_(1^3)(z) = 0     <-- the Temperley-Lieb condition (3-row block dies)

is ONE equation in ONE unknown. If it has a unique solution z_D, and the
weight vector at z_D equals the Jones-closure vector, then convention D is
FORCED by the TL condition -- no residual freedom, no fit.
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401
import sympy as sp

HERE = Path(__file__).resolve().parent
for sub in ("markov", "substrate", "hecke"):
    sys.path.insert(0, str(HERE / sub))

from hecke_character_symbolic import q_character_on_braid_word
from q_parameter import Q as Q0

qs = sp.symbols("q", positive=True)
z = sp.symbols("z")
q0 = sp.Float(str(Q0), 50)

PARTS = [(3,), (2, 1), (1, 1, 1)]
# class representatives as (generator, kind) crossing lists
CLASSES = {
    "1":            [],
    "s0":           [(0, "sigma")],
    "s0s1":         [(0, "sigma"), (1, "sigma")],
}
TARGET = {"1": sp.Integer(1), "s0": z, "s0s1": z**2}

print("Characters chi^lambda on the three H_3 class representatives:")
M, rhs = [], []
for cname, word in CLASSES.items():
    row = []
    for lam in PARTS:
        c = sp.cancel(sp.together(sp.sympify(
            q_character_on_braid_word(lam, word, qs))))
        row.append(c)
    M.append(row)
    rhs.append(TARGET[cname])
    print("  %-6s : %s" % (cname, [sp.simplify(x) for x in row]))

A = sp.Matrix(M)
b = sp.Matrix(rhs)
sol = A.solve(b)
y = {lam: sp.cancel(sp.together(sol[i])) for i, lam in enumerate(PARTS)}

print("\nWeights as functions of the Ocneanu parameter z:")
for lam in PARTS:
    print("  y_%-9s = %s" % (str(lam), sp.simplify(y[lam])))

print("\nSolve the Temperley-Lieb condition  y_(1^3)(z) = 0 :")
roots = sp.solve(sp.numer(sp.together(y[(1, 1, 1)])), z)
print("  roots in z: %s" % [sp.simplify(r) for r in roots])
print("  number of roots: %d" % len(roots))

# Convention C is EXCISED (owner ruling 2026-08-09, re-affirmed 2026-08-15).
# Printed beside the solved root because the POINT of this probe is that z_C is
# NOT a root of y_(1^3) = 0 while z_D is -- i.e. the two-row forcing selects D.
# The comparison needs the excised value present to be a comparison at all.
z_C = 1/(sp.sqrt(qs) + 1/sp.sqrt(qs))
print("\n  z_C (Wenzl/Ocneanu convention C, EXCISED 2026-08-09/15) = %s   -> at q0: %s"
      % (z_C, sp.N(z_C.subs(qs, q0), 20)))
for r in roots:
    rs = sp.simplify(r)
    print("  z_D root                         = %s   -> at q0: %s"
          % (rs, sp.N(rs.subs(qs, q0), 20)))

print("\nWeight vector at each TL root, vs the Jones-closure vector:")
b2 = (qs**2 - qs**-2)/(qs - qs**-1)
b4 = (qs**4 - qs**-4)/(qs - qs**-1)
yJ = {(3,): sp.cancel(b4/b2**3), (2, 1): sp.cancel(1/b2**2),
      (1, 1, 1): sp.Integer(0)}
for r in roots:
    print("  at z = %s :" % sp.simplify(r))
    ok = True
    for lam in PARTS:
        got = sp.cancel(sp.together(y[lam].subs(z, r)))
        want = yJ[lam]
        d = sp.simplify(sp.cancel(sp.together(got - want)))
        ok = ok and (d == 0)
        print("    y_%-9s = %-22s  (matches Jones-closure: %s)"
              % (str(lam), sp.N(got.subs(qs, q0), 18), d == 0))
    print("    ==> weight vector equals the Jones-closure vector: %s" % ok)
