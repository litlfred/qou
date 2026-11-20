#!/usr/bin/env python3
"""W1 route 3: is the colour spectral cubic a gauge invariant of a q-difference module?

Wall W1 (bean `qou-d8de`) wants a q-difference prolongation `D_q` built from the colour
spectral curve `Sigma : P(X, z) = 0` with `lambda_SW = X dz`.  Routes 1 and 2 are closed:

  #6695  route 1 in the base coordinate `z`
  #6738  route 1 in the ramified local coordinate `t`, `z = z_c + t^2`
  #6769  route 1 on `Sigma` itself -- no `z -> l*z` with `l != 1` preserves the branch locus
  #7114  route 2's eigenvalue reading -- the fibre monodromy has order exactly 2
  #7185  every BASE automorphism of P^1 preserving the branch locus has order <= 6

The bean's own stated next step is route 3:

    "pick route 3 (import the q-difference D-module framework from the literature)
     before attempting routes 1-2, so `D_q` is built on a real definitional foundation
     rather than an ad-hoc operator."

This probe performs that import and measures whether its obvious instantiation exists.

What route 3 requires, from the sources this corpus holds
---------------------------------------------------------
Ramis-Sauloy-Zhang, *Local analytic classification of q-difference equations*,
Asterisque 355, sec 2.1.1 (`library/arxiv-0903.0853v3`), verbatim:

    "We call difference field a pair (K, sigma), where K is a (commutative) field and
     sigma a field automorphism of K."

Di Vizio-Ramis-Sauloy-Zhang, *Equations aux q-differences* sec 2.5
(`library/equations-aux-q-differences`): a q-difference module is a pair `(M, Phi)` of a
finite-dimensional `K`-space and a `sigma_q`-linear automorphism.  A SYSTEM
`sigma_q X = A X` is read modulo GAUGE, and the gauge law -- DVRSZ eq. (2.4.1), verbatim --
is NOT conjugation:

    "la meme transformation de jauge ramene le systeme (2.3.1) au systeme sigma_q Y = B Y,
     ou (2.4.1)  B = (sigma_q F)^{-1} A F."

In the DIFFERENTIAL / Hitchin case a gauge acts on a Higgs field by conjugation
`Phi -> F Phi F^{-1}`, so `det(X.1 - Phi)` is gauge-invariant and the Seiberg-Witten
spectral curve is well defined.  Eq. (2.4.1) is a twisted action, and that is the whole
question this probe decides.

Sections
--------
  T1  the gauge law (2.4.1) with the monomial gauge `F = z^k . 1`: `B = q^{-k} A`, exact
  T2  a scalar multiple MOVES the characteristic cubic: `det(X.1 - tA) = t^3 det((X/t).1 - A)`
  T3  CONTROL -- the differential/Higgs case: `det(X.1 - F Phi F^{-1}) == det(X.1 - Phi)`,
      so the machinery certifies invariance when invariance is there
  T4  the WEIGHT RELATIONS for a general monic cubic under `X -> tX`, and the consequence:
      for one non-root-of-unity `t` every non-leading coefficient must vanish
  T5  the colour cubic: the only gauge scalar fixing it is `t = 1`
      + CONTROL: the same elimination on the quasi-homogeneous `X^3 + z^3` returns THREE
  T6  JOINT rigidity `P(lX, mz) = n P(X,z)`  =>  `l = m = n = 1`
      + CONTROL: the same elimination on `X^3 + z^3` returns a 1-parameter FAMILY
  T7  the structural reason -- `P` is quasi-homogeneous for the PAIRED action
      (`z^3 P(X/z, 1/z) = P(X,z)`, #7114) but its coefficients are not monomials, so there
      is no weight for an unpaired `X`-motion to absorb
  T8  the substrate: `q_0 > 1`, so every nontrivial monomial gauge scalar `q_0^{-k}` is != 1
  T9  descent to `E_q = C*/q^Z`: the fibre over `z = 0` has root set `{-1, i, -i}`, whose
      ratios are all 4th roots of unity, so `q . B = B` forces `q^4 = 1` -- and `q_0^4 != 1`

Precision discipline (AGENTS.md, NO-FLOAT64; probes are NOT exempt)
------------------------------------------------------------------
Every conclusion-bearing computation is exact `sympy` over `QQ` (or `QQ(i)`).  Exactly one
value is floating and it is `mpmath`, never `float64`: `q_0` in T8/T9, read from the
50-digit proton-pinned string at 60 dps and used only for the comparisons `q_0 > 1` and
`q_0^4 != 1`.  No `float()`, no `statistics`, no `math`.

No witness by design: this probe decides a scope question, it does not record a number.

Run
---
    PYTHONPATH=computations:tools/qou-substrate/python \
      python3 -u computations/probes/w1_route3_qgauge_spectral_rigidity_probe.py
"""

from __future__ import annotations

import sys

import sympy as sp

n_pass = 0
n_tot = 0


def check(name: str, cond: bool, detail: str = "") -> None:
    global n_pass, n_tot
    n_tot += 1
    ok = bool(cond)
    n_pass += ok
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


X, z, q, t, l, m, n = sp.symbols("X z q t l m n")

# The colour spectral cubic, and its branch sextic, exactly as the corpus carries them
# (QOU/Mass/ColorSpectralCubicGeometry.lean, QOU/Mass/PalindromicInvolutionLift.lean).
A2 = z + 1
A1 = z**2 + z + 1
A0 = z**3 + z**2 + z + 1


def color_cubic(x_, z_):
    return x_**3 + (z_ + 1) * x_**2 + (z_**2 + z_ + 1) * x_ + (z_**3 + z_**2 + z_ + 1)


# ---------------------------------------------------------------------------------------
# T1 -- the gauge law, DVRSZ eq. (2.4.1), with the monomial gauge F = z^k . 1.
#
#   sigma_q : f(z) |-> f(qz).   F = z^k . 1  =>  sigma_q F = (qz)^k . 1
#   B = (sigma_q F)^{-1} A F = ((qz)^k)^{-1} . z^k . A = q^{-k} A.
#
# So the scalars a monomial gauge can apply to the system matrix are exactly q^Z.
# ---------------------------------------------------------------------------------------
print("T1  gauge law (DVRSZ 2.4.1) with a monomial gauge")

Asym = sp.Matrix(3, 3, lambda i, j: sp.Symbol(f"a{i}{j}"))

for k in (1, 2, 3):
    F = (z**k) * sp.eye(3)
    sigma_F = ((q * z) ** k) * sp.eye(3)          # sigma_q applied entrywise to F
    B = sigma_F.inv() * Asym * F
    expected = (q ** (-k)) * Asym
    check(
        f"T1.{k}  B = (sigma_q F)^-1 A F = q^-{k} A   (F = z^{k}.1)",
        sp.simplify(B - expected) == sp.zeros(3, 3),
    )

# The same law with a NON-scalar gauge is not conjugation: exhibit one explicit F over
# QQ(z) for which (sigma_q F)^{-1} A F differs from F^{-1} A F.
F2 = sp.Matrix([[1, z, 0], [0, 1, 0], [0, 0, 1]])
sigmaF2 = F2.subs(z, q * z)
twisted = sp.simplify(sigmaF2.inv() * Asym * F2)
conj = sp.simplify(F2.inv() * Asym * F2)
check(
    "T1.4  the twisted action is NOT conjugation for a non-scalar gauge",
    sp.simplify(twisted - conj) != sp.zeros(3, 3),
)

# ---------------------------------------------------------------------------------------
# T2 -- a scalar multiple MOVES the characteristic cubic.
# ---------------------------------------------------------------------------------------
print("T2  a scalar multiple moves the characteristic cubic")

char_A = (X * sp.eye(3) - Asym).det()
char_tA = (X * sp.eye(3) - t * Asym).det()
check(
    "T2.1  det(X.1 - tA) = t^3 . det((X/t).1 - A)   (the roots scale by t)",
    sp.simplify(sp.expand(char_tA - t**3 * char_A.subs(X, X / t))) == 0,
)

# Coefficient weights, read off: the X^(3-k) coefficient of char(tA) carries t^k.
r1, r2, r3 = sp.symbols("r1 r2 r3")
lhs = sp.expand((X - t * r1) * (X - t * r2) * (X - t * r3))
rhs = sp.expand(
    X**3
    - t * (r1 + r2 + r3) * X**2
    + t**2 * (r1 * r2 + r1 * r3 + r2 * r3) * X
    - t**3 * (r1 * r2 * r3)
)
check("T2.2  coefficient of X^(3-k) picks up exactly t^k", sp.expand(lhs - rhs) == 0)

# ---------------------------------------------------------------------------------------
# T3 -- CONTROL.  In the differential / Hitchin case the gauge IS conjugation, and the
# characteristic polynomial is invariant.  Without this the T2 result would not be evidence
# that the q-difference case is special -- it would only show the method finds motion.
# ---------------------------------------------------------------------------------------
print("T3  CONTROL -- the differential/Higgs case: conjugation preserves the char poly")

Fq = sp.Matrix([[2, 1, 0], [1, 1, 0], [0, 3, 1]])          # exact, over QQ, det = 1
check("T3.0  the control gauge is invertible over QQ", sp.Integer(Fq.det()) != 0,
      f"det = {Fq.det()}")
char_conj = (X * sp.eye(3) - Fq * Asym * Fq.inv()).det()
check(
    "T3.1  det(X.1 - F Phi F^-1) == det(X.1 - Phi)  (conjugation: INVARIANT)",
    sp.simplify(sp.expand(char_conj - char_A)) == 0,
)
# ... and the same F used as a q-difference gauge does NOT preserve it.
char_twist = (X * sp.eye(3) - (Fq * Asym * Fq.inv()) * q).det()
check(
    "T3.2  the same matrix scaled by q does NOT preserve it (q generic)",
    sp.simplify(sp.expand(char_twist - char_A)) != 0,
)

# ---------------------------------------------------------------------------------------
# T4 -- the weight relations for a general monic cubic, and their consequence.
# ---------------------------------------------------------------------------------------
print("T4  weight relations for a general monic cubic under X -> tX")

a2, a1, a0 = sp.symbols("a2 a1 a0")
Pc = X**3 + a2 * X**2 + a1 * X + a0
E = sp.expand(Pc.subs(X, t * X) - t**3 * Pc)
# Read the coefficients by degree -- `Poly.all_coeffs()` would silently drop the leading
# slot here, because the `X^3` term cancels and the polynomial is only degree 2.
coeffs = [E.coeff(X, k) for k in (3, 2, 1, 0)]
check("T4.1  the X^3 coefficient cancels identically", sp.simplify(coeffs[0]) == 0)
check("T4.2  X^2 coefficient is a2 . t^2 . (1 - t)",
      sp.simplify(coeffs[1] - a2 * t**2 * (1 - t)) == 0)
check("T4.3  X^1 coefficient is a1 . t . (1 - t^2)",
      sp.simplify(coeffs[2] - a1 * t * (1 - t**2)) == 0)
check("T4.4  X^0 coefficient is a0 . (1 - t^3)",
      sp.simplify(coeffs[3] - a0 * (1 - t**3)) == 0)

# Consequence at one concrete non-root-of-unity scalar, exactly over QQ.
sol = sp.solve([c.subs(t, sp.Integer(2)) for c in coeffs[1:]], [a2, a1, a0], dict=True)
check(
    "T4.5  at t = 2 the ONLY stable monic cubic is X^3 (a2 = a1 = a0 = 0)",
    sol == [{a2: 0, a1: 0, a0: 0}],
    f"solutions = {sol}",
)
# CONTROL: at a root of unity the same elimination does NOT force the coefficients to zero.
w = sp.Rational(-1, 2) + sp.sqrt(3) * sp.I / 2                     # primitive cube root of 1
check("T4.6  CONTROL setup: w^3 = 1, w != 1", sp.simplify(w**3 - 1) == 0 and sp.simplify(w - 1) != 0)
relw = [sp.simplify(c.subs(t, w)) for c in coeffs[1:]]
check(
    "T4.7  CONTROL: at t = w (a cube root of 1) the X^0 relation is VACUOUS",
    sp.simplify(relw[2]) == 0,
    "so a0 is unconstrained -- the method can also say 'not forced'",
)

# ---------------------------------------------------------------------------------------
# T5 -- the colour cubic: which gauge scalars fix it?
# ---------------------------------------------------------------------------------------
print("T5  the colour cubic under the gauge scaling")

gauged = X**3 + t * A2 * X**2 + t**2 * A1 * X + t**3 * A0
Ec = sp.expand(gauged - color_cubic(X, z))
sol_t = sp.solve(sp.Poly(Ec, X, z).coeffs(), t, dict=True)
check("T5.1  the only gauge scalar fixing the colour cubic is t = 1",
      sol_t == [{t: 1}], f"solutions = {sol_t}")

# The fibre over z = 0 alone already decides it: X^3 + X^2 + X + 1, all three non-leading
# coefficients equal to 1, so no weight can be absorbed.
Ez0 = sp.expand(Ec.subs(z, 0))
sol_t0 = sp.solve(sp.Poly(Ez0, X).coeffs(), t, dict=True)
check("T5.2  the fibre over z = 0 alone forces t = 1", sol_t0 == [{t: 1}],
      f"solutions = {sol_t0}")

# CONTROL: a genuinely quasi-homogeneous cubic admits MORE than one gauge scalar, so a
# singleton in T5.1 is evidence and not an artifact of the elimination.
Qh = X**3 + z**3
gauged_Qh = X**3 + t**3 * z**3
sol_ctrl = sp.solve(sp.Poly(sp.expand(gauged_Qh - Qh), X, z).coeffs(), t, dict=True)
check(
    "T5.3  CONTROL: X^3 + z^3 admits THREE gauge scalars (the cube roots of 1)",
    len(sol_ctrl) == 3,
    f"n = {len(sol_ctrl)}",
)

# ---------------------------------------------------------------------------------------
# T6 -- JOINT rigidity: fibre scaling AND base dilation at once.
# ---------------------------------------------------------------------------------------
print("T6  joint rigidity  P(lX, mz) = n P(X,z)")

Ej = sp.expand(color_cubic(l * X, m * z) - n * color_cubic(X, z))
sol_j = sp.solve(sp.Poly(Ej, X, z).coeffs(), [l, m, n], dict=True)
check("T6.1  the unique solution is (l, m, n) = (1, 1, 1)",
      sol_j == [{l: 1, m: 1, n: 1}], f"solutions = {sol_j}")

# CONTROL: the quasi-homogeneous cubic admits a positive-dimensional family.
Ej_ctrl = sp.expand(((l * X) ** 3 + (m * z) ** 3) - n * (X**3 + z**3))
sol_jc = sp.solve(sp.Poly(Ej_ctrl, X, z).coeffs(), [l, m, n], dict=True)
free = sol_jc != [] and any(
    len(s) < 3 or any(v.free_symbols for v in s.values()) for s in sol_jc
)
check(
    "T6.2  CONTROL: X^3 + z^3 admits a 1-parameter FAMILY, not a point",
    free,
    f"solutions = {sol_jc}",
)

# ---------------------------------------------------------------------------------------
# T7 -- the structural reason.  P IS quasi-homogeneous, but only for the PAIRED action.
# ---------------------------------------------------------------------------------------
print("T7  the paired weight exists; the unpaired one does not")

# Re-verify #7114's lift identity (cheap; cited, not re-derived as a result).
lift = sp.simplify(sp.expand(z**3 * color_cubic(X / z, 1 / z) - color_cubic(X, z)))
check("T7.1  z^3 . P(X/z, 1/z) == P(X, z)   (#7114 -- the PAIRED weight)", lift == 0)

# Why no unpaired weight: quasi-homogeneity under (X,z) -> (lX, mz) needs every coefficient
# a_k to be a MONOMIAL in z.  They are truncated geometric sums, so they are not.
for name, ak, want in (("a2", A2, 2), ("a1", A1, 3), ("a0", A0, 4)):
    terms = len(sp.Poly(ak, z).all_coeffs()) - sp.Poly(ak, z).all_coeffs().count(0)
    check(f"T7.{name}  {name} = {ak} has {want} terms, so it is not a monomial in z",
          terms == want, f"terms = {terms}")

# ---------------------------------------------------------------------------------------
# T8 -- the substrate.  The gauge scalars are q^Z and q_0 > 1.
# ---------------------------------------------------------------------------------------
print("T8  the substrate modulus")

import mpmath as mp                                                    # noqa: E402
from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP                     # noqa: E402

mp.mp.dps = 60
q0 = Q_MP
check("T8.1  q_0 > 1 (proton pin, 60 dps)", q0 > 1, f"q_0 = {mp.nstr(q0, 25)}")
powers_ne_one = all(q0**k != 1 for k in range(1, 13))
check("T8.2  q_0^k != 1 for 1 <= k <= 12, so no monomial gauge scalar is trivial",
      powers_ne_one)

# ---------------------------------------------------------------------------------------
# T9 -- descent to the Tate curve E_q = C*/q^Z, at the fibre over z = 0.
#
# For the spectral data to live on E_q the fibre's root set must be q-invariant.  Over
# z = 0 the cubic is (X+1)(X^2+1), roots {-1, i, -i}: all nonzero, and every ratio of two
# of them is a 4th root of unity.  So q . B = B forces q^4 = 1.
# ---------------------------------------------------------------------------------------
print("T9  descent to E_q = C*/q^Z at the fibre over z = 0")

fib = sp.factor(color_cubic(X, 0))
check("T9.1  the fibre over z = 0 factors as (X+1)(X^2+1)",
      sp.simplify(sp.expand(fib - (X + 1) * (X**2 + 1))) == 0, f"{fib}")

roots = sp.Poly(color_cubic(X, 0), X).all_roots()
check("T9.2  three distinct roots, all nonzero",
      len(set(roots)) == 3 and all(sp.simplify(r) != 0 for r in roots),
      f"roots = {roots}")

ratios = {sp.simplify(a / b) for a in roots for b in roots}
all_fourth = all(sp.simplify(sp.expand(rho**4) - 1) == 0 for rho in ratios)
check("T9.3  every ratio of two roots is a 4th root of unity, so q.B = B forces q^4 = 1",
      all_fourth, f"{len(ratios)} distinct ratios")

check("T9.4  q_0^4 != 1, so the z = 0 fibre does NOT descend to E_q",
      q0**4 != 1, f"q_0^4 = {mp.nstr(q0**4, 20)}")

# ---------------------------------------------------------------------------------------
print()
print(f"{n_pass}/{n_tot} checks passed")
print(
    """
SUMMARY
=======
  What route 3 needs.  A difference field `(K, sigma)` (RSZ Asterisque 355 sec 2.1.1) and a
  finite-dimensional `K`-space with a `sigma`-linear automorphism (DVRSZ sec 2.5).  A system
  is read modulo gauge, and the gauge law is `B = (sigma_q F)^{-1} A F` (DVRSZ eq. 2.4.1) --
  a TWISTED action, not conjugation (T1).

  The finding, scope (b), invariant cited.  With the monomial gauge `F = z^k . 1` the law
  reads `A -> q^{-k} A` (T1), and a scalar multiple MOVES the characteristic cubic, its
  `X^(3-k)` coefficient picking up exactly `t^k` (T2).  Stability of a monic cubic under
  `X -> tX` therefore forces `a0(1-t^3) = a1 t(1-t^2) = a2 t^2(1-t) = 0` (T4); at any scalar
  that is not a root of unity -- in particular any real `t > 1`, so every `q_0^{-k}` (T8) --
  every non-leading coefficient must VANISH.  The only gauge-stable monic cubic is `X^3 = 0`.
  This is general; it is not a fact about this Sigma.

  For the colour cubic the fibre over `z = 0` decides it alone: `X^3+X^2+X+1`, all three
  non-leading coefficients `1`, so `t = 1` (T5).  The JOINT move -- fibre scaling together
  with a base dilation -- is equally rigid: `P(lX, mz) = n P(X,z)` forces `l = m = n = 1`
  (T6), which neither #6769 (base only) nor T5 (fibre only) reaches alone.  Read as descent
  to the Tate curve `E_q = C*/q^Z`, the `z = 0` fibre's root ratios are 4th roots of unity,
  so `q . B = B` forces `q^4 = 1`, and `q_0^4 != 1` (T9).

  Why it is structural rather than a coincidence.  `P` IS quasi-homogeneous -- but for the
  PAIRED action `(X, z) -> (X/z, 1/z)`, which is exactly why the palindromic involution lifts
  (#7114, re-verified T7.1).  The gauge asks for an `X`-motion with NO compensating
  `z`-motion, and the coefficients `a_k = 1 + z + ... + z^(3-k)` are not monomials (T7), so
  there is no weight left to absorb it.  This is the same q-freeness of Sigma that forced the
  prolongation to be q-difference in the first place (2026-06-25 z2bn audit) -- the property
  that creates the need is the property that blocks this instantiation.

  CONTROLS.  Three, because a negative from an elimination is only evidence if the same
  elimination can return something else.  T3: conjugation (the differential/Higgs case) IS
  certified invariant by the same determinant computation.  T4.7: at a cube root of unity the
  weight relation on `a0` goes vacuous, so the method can say "not forced".  T5.3/T6.2: the
  quasi-homogeneous `X^3 + z^3` returns three scalars and a 1-parameter family respectively,
  so a singleton answer is not an artifact.

  NOT excluded.  Route 3 is NOT dead: a q-difference module over `(C(z), sigma_q)` is a
  perfectly good object, and this corpus already uses RSZ that way for scalar kernels
  (2026-07-20 qlift route-A audit).  What is excluded is reading Sigma as such a module's
  gauge-invariant characteristic-polynomial curve.  Sigma may still enter route 3 as data
  that is not a char-poly curve -- Newton polygon, slopes, the Birkhoff connection matrix,
  the bundle on `E_q` of RSZ sec 6.3.  One may always FIX a gauge and compute; the objection
  is only that Sigma would then not be an invariant of the module.

  The bridge "the sought `D_q` would have Sigma as its spectral curve" is an ASSUMPTION -- it
  is what `lambda_SW = X dz` sets up and what "a q-difference prolongation of Sigma" means,
  but it is a hypothesis here and in the Lean, never used as a fact.  `D_q` is NOT
  constructed.  Nothing is fitted and nothing is wired.
"""
)

sys.exit(0 if n_pass == n_tot else 1)
