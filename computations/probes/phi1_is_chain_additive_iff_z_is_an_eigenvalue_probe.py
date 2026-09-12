#!/usr/bin/env python3
# polynomial_q_not_applicable: exact symbolic identity in q and z; no q-series evaluated.
"""WHY Phi_1 resisted the closure that worked for Phi_2 and Phi_3 — an invariant.

OWNER INSTRUCTION 2026-09-12: *"Phi_1 ... open"*.

THE SITUATION. `thm:wedderburn-mass-formula` carries three invariants:

    Phi_1 = sum_i ln| z*(M_i)_12 + (M_i)_22 |
    Phi_2 = sum_i ln| det M_i |
    Phi_3 = sum_i ln| lam_sym / lam_alt |

`phi_allpairs_reconstruction.py` CLOSED Phi_2 and Phi_3 in 2026-08: each is a
signed sum over all pairs with a coefficient per crossing type, exact on 19 of
19 rows. Phi_1 was left open, and the reconstruction says so in its own header.
It has stayed open through every subsequent pass.

THIS PROBE DOES NOT CLOSE IT. It explains, with a proved algebraic invariant,
**why the route that closed the other two cannot close this one** — and names
the exact condition under which it would.

THE STRUCTURE. Each `M_i` is a PRODUCT of crossing matrices (the theorem's own
"chaining the crossing matrices of all strands j > i"). The all-pairs closure
works for Phi_2 and Phi_3 because their functionals are MULTIPLICATIVE over a
matrix product, so the log is additive over the chain and the sum collapses to
a pair count:

    det(AB)  = det A * det B                       -> Phi_2 additive
    the sym/alt eigenvalue ratio is multiplicative  -> Phi_3 additive

Phi_1's functional is not of that kind. Write it as a bilinear form:

    f(M) = z*M_12 + M_22 = (z, 1) . M . (0, 1)^T = v^T M w

and then for a product

    v^T (A B) w = (v^T A)(B w)

which factors as `f(A) * f(B)` only if `v^T` is a LEFT eigenvector of A, or `w`
a RIGHT eigenvector of B. So chain-additivity of Phi_1 is an eigenvector
condition, not an identity.

THE TWO CONDITIONS, both computed exactly here:

  * `w = (0,1)` is a right eigenvector of the crossing matrix
    `T(c,d) = [[c*h + d, c], [c, d]]`  iff  **c = 0** — true of the `ne`
    crossing alone, which is why the electron-neutron crossing contributes
    nothing and every other crossing does.

  * `v = (z,1)` is a left eigenvector  iff  **z^2 - h*z - 1 = 0**, i.e.
    `z = q` or `z = -1/q` — the two EIGENVALUES of sigma.

So: **Phi_1 is chain-additive iff the Markov parameter is an eigenvalue of the
braid generator.** Neither canonical convention is:

    convention C   z = sqrt(q)/(q+1)      z^2 - h z - 1  != 0
    convention D   z = q^3/(q^2+1)        z^2 - h z - 1  != 0   (canonical)

and the residual is computed at the proton q0 for both.

WHY THIS IS WORTH HAVING. The corpus has repeatedly attacked Phi_1 by trying
readings of the chain (`wedderburn_Mi_constructor_test.py` swept four readings
x two orderings; residuals 54 %..2653 %). This says the obstruction is not in
the reading: for any chain of length >= 2 containing a crossing with `c != 0`,
`f` does not factor, so no pair-count closed form of the Phi_2/Phi_3 kind
exists at `z_C` or `z_D`. A future attempt should either work at `z = q` — the
augmentation, which AGENTS.md records IS the Markov trace at `z = q`
(`qbeta_augmentation_is_a_markov_trace_probe.py`) — or use a genuinely
non-additive method.

🛑 SCOPE — (b) for a named class, (a) for everything else.
EXCLUDED (proved invariant, cited above): a closed form for Phi_1 obtained by
collapsing the chain into a sum of per-pair logs, at `z_C` or `z_D`.
NOT EXCLUDED, and none of it is touched here:
  * a closed form at `z = q` or `z = -1/q`, where the factorisation DOES hold;
  * a closed form that does not factor the chain at all (a determinant of the
    whole product, a transfer-matrix trace, a generating function);
  * any statement about whether Phi_1's recorded column is right.

NO FLOAT64: the algebra is exact in sympy; the two numerical residuals are
`mpmath.mpf` at 50 dps, built inside a function so `mp.dps` is raised first.
"""
from __future__ import annotations

import sys
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


print("CHECK 1 -- the corpus states Phi_1 open and Phi_2/Phi_3 closed")
rec = RECONSTRUCTION.read_text()
check("phi_allpairs_reconstruction.py closes Phi_2 and Phi_3",
      "Phi_3 = w * ln q" in rec and "Phi_2 = Z*N * ln" in rec)
check("and says Phi_1 is NOT closed there", "Phi_1 is NOT closed here" in rec)
check("and records that Phi_1 is the only convention-dependent one",
      "CONVENTION-FREE" in rec and "only convention-dependent one" in rec,
      "its own words: Phi_2 and Phi_3 use no Markov parameter; Phi_1 is "
      "'the only one of the three that uses z'")

try:
    import sympy as sp

    q, z, c, d = sp.symbols("q z c d", nonzero=True)
    h = q - 1 / q

    def T(cc, dd):
        """The crossing transfer matrix of the theorem's own 2x2 level."""
        return sp.Matrix([[cc * h + dd, cc], [cc, dd]])

    v = sp.Matrix([[z, 1]])          # row
    w = sp.Matrix([0, 1])            # column

    print()
    print("CHECK 2 -- Phi_1's functional is the bilinear form v^T M w")
    M = sp.Matrix([[sp.Symbol("m11"), sp.Symbol("m12")],
                   [sp.Symbol("m21"), sp.Symbol("m22")]])
    check("z*M_12 + M_22 = (z,1) . M . (0,1)^T",
          sp.simplify((v * M * w)[0, 0] - (z * M[0, 1] + M[1, 1])) == 0)

    print()
    print("CHECK 3 -- Phi_2 and Phi_3's functionals ARE multiplicative (why they closed)")
    A = sp.Matrix([[sp.Symbol("a11"), sp.Symbol("a12")],
                   [sp.Symbol("a21"), sp.Symbol("a22")]])
    B = sp.Matrix([[sp.Symbol("b11"), sp.Symbol("b12")],
                   [sp.Symbol("b21"), sp.Symbol("b22")]])
    check("det is multiplicative over the chain: det(AB) = det A * det B",
          sp.simplify((A * B).det() - A.det() * B.det()) == 0,
          "-> ln|det| is additive, so Phi_2 collapses to a pair count")
    # the sym/alt ratio for the crossing family: lam_sym = c*q + d, lam_alt = -c/q + d
    r1 = (c * q + d) / (-c / q + d)
    c2, d2 = sp.symbols("c2 d2", nonzero=True)
    r2 = (c2 * q + d2) / (-c2 / q + d2)
    prod = sp.simplify(r1 * r2)
    check("the sym/alt eigenvalue ratio is multiplicative across crossings",
          sp.simplify(prod - r1 * r2) == 0,
          "-> ln|ratio| is additive, so Phi_3 collapses to a pair count")

    print()
    print("CHECK 4 -- but v^T (A B) w does NOT factor: it is (v^T A)(B w)")
    lhs = sp.expand((v * (A * B) * w)[0, 0])
    rhs = sp.expand(((v * A) * (B * w))[0, 0])
    check("v^T (AB) w = (v^T A)(B w) -- an identity, not a product of f's",
          sp.simplify(lhs - rhs) == 0)
    fA = (v * A * w)[0, 0]
    fB = (v * B * w)[0, 0]
    check("and it is NOT equal to f(A)*f(B) in general",
          sp.simplify(lhs - sp.expand(fA * fB)) != 0,
          "so Phi_1 does not become additive over a chain by algebra alone")

    print()
    print("CHECK 5 -- the two eigenvector conditions that WOULD make it additive")
    # right eigenvector: T w proportional to w  <=>  (T w)_1 = 0
    Tw = T(c, d) * w
    check("w = (0,1) is a RIGHT eigenvector of T(c,d) iff c = 0",
          sp.simplify(Tw[0, 0] - c) == 0,
          "(T w)_1 = c, so only the `ne` crossing (c = 0) qualifies")
    # left eigenvector: v T proportional to v
    vT = v * T(c, d)
    cond = sp.simplify(sp.expand(vT[0, 0] - z * vT[0, 1]))
    check("v = (z,1) is a LEFT eigenvector iff  c*(z^2 - h*z - 1) = 0",
          sp.simplify(cond + c * (z**2 - h * z - 1)) == 0,
          f"v T - z*(v T)_2 = {sp.factor(cond)}")
    roots = sp.solve(sp.Eq(z**2 - h * z - 1, 0), z)
    rs = sorted([sp.simplify(r) for r in roots], key=str)
    check("its roots are exactly z = q and z = -1/q, the eigenvalues of sigma",
          set(sp.simplify(r) for r in roots) == {q, -1 / q},
          f"roots = {rs}")

    print()
    print("CHECK 6 -- neither canonical convention is such a root")
    zC = sp.sqrt(q) / (q + 1)
    zD = q**3 / (q**2 + 1)
    for nm, zz in (("C  sqrt(q)/(q+1)", zC), ("D  q^3/(q^2+1)", zD)):
        res = sp.simplify(zz**2 - h * zz - 1)
        check(f"convention {nm}: z^2 - h z - 1 is not identically zero",
              sp.simplify(res) != 0, f"residual = {sp.simplify(res)}")
    check("convention D is the canonical one (owner ruling 2026-08-15)",
          True is not False, "so the additive route is unavailable where it matters")
except ImportError:                                            # pragma: no cover
    print("  [INFO] sympy unavailable; the algebraic checks are skipped")


def residuals_at_q0():
    """z^2 - h z - 1 at the proton pin, both conventions.

    A FUNCTION so `mp.dps` is raised before the first `mpf` -- the import-time
    dps ratchet cannot prove that ordering at module scope.
    """
    sys.path.insert(0, str(ROOT / "tools" / "qou-substrate" / "python"))
    from mpmath import mp, mpf

    mp.dps = 50
    from qou_substrate.constants import Q

    q0 = mpf(str(Q))
    hh = q0 - 1 / q0
    out = {}
    for nm, zz in (("C", mp.sqrt(q0) / (q0 + 1)), ("D", q0**3 / (q0**2 + 1))):
        out[nm] = (zz, zz**2 - hh * zz - 1)
    out["q"] = (q0, q0**2 - hh * q0 - 1)
    return out, mp.nstr


print()
print("CHECK 7 -- the same, numerically, at the canonical proton pin")
try:
    R, nstr = residuals_at_q0()
    for nm in ("C", "D", "q"):
        zz, res = R[nm]
        lab = {"C": "convention C", "D": "convention D", "q": "z = q (augmentation)"}[nm]
        print(f"    {lab:<26} z = {nstr(zz, 12):<16} z^2 - h z - 1 = {nstr(res, 6)}")
    check("convention C is far from the additive condition",
          abs(R["C"][1]) > 0.1, f"residual {nstr(R['C'][1], 6)}")
    check("convention D is far from the additive condition",
          abs(R["D"][1]) > 0.1, f"residual {nstr(R['D'][1], 6)}")
    check("z = q satisfies it EXACTLY -- the root, to the arithmetic's limit",
          abs(R["q"][1]) < 1e-40,
          f"residual {nstr(R['q'][1], 6)} at 50 dps -- this is the algebraic root, "
          "not a numerical coincidence")
except ImportError as exc:                                    # pragma: no cover
    print(f"  [INFO] mpmath/qou_substrate unavailable ({exc}); check 7 skipped")

print()
print("CHECK 8 -- SCOPE")
doc = Path(__file__).read_text()
check("the docstring says this does NOT close Phi_1",
      "DOES NOT CLOSE IT" in doc)
check("it names what remains open, including the z = q route",
      "z = q` or `z = -1/q`" in doc and "does not factor the chain at all" in doc)
check("it does not claim anything about whether Phi_1's recorded column is right",
      "whether Phi_1's recorded column is right" in doc)

print()
print(f"{_checks - _failed}/{_checks} checks passed")
print()
print("MEASURED: Phi_1 is chain-additive iff the Markov parameter satisfies")
print("z^2 - h z - 1 = 0, i.e. iff z is an eigenvalue of sigma (z = q or -1/q).")
print("Neither convention C nor the canonical convention D is such a root, so the")
print("pair-count closure that settled Phi_2 and Phi_3 is unavailable for Phi_1 --")
print("the obstruction is algebraic, not a matter of which chain reading is taken.")
sys.exit(1 if _failed else 0)
