#!/usr/bin/env python3
"""W1 route 2 — which root of unity can the fibre monodromy supply?

Bean `qou-hmrm`. Follows the route-1 closure across all three charts:
#6695 (base coordinate), #6738 (ramified local coordinate), #6769 (Sigma itself).

Route 2 of `qou-d8de` reads, verbatim:

    Root-of-unity fibre monodromy. The fibre singularity is a root of unity; a
    q-difference connection may arise naturally from its local monodromy.

This probe measures WHICH root of unity that datum supplies, before anything is
constructed. The chain:

  S1  the branch sextic D(z) = -disc_X P is squarefree  (6 distinct roots)
  S2  the colour cubic has NO triple root, for any z    (=> no TOTAL branch point)
  S3  therefore every branch point is SIMPLE            (order of vanishing 1)
  S4  the cover is unramified over z = infinity
  S5  Riemann-Hurwitz => genus of Sigma
  S6  CONTROL: the same machinery on a curve that DOES have a total branch point
  S7  the quantum integers at q = -1 collapse to {0, 1}
  S8  the substrate q0 is not a root of unity at all (|q0| != 1)

S2 is the exact counterpart of the Lean theorem
`QOU.Mass.FibreMonodromyOrderTwo.colorCubic_no_triple_root`; S6 is what makes S2
mean something, exactly as the `z^6 - 1` control did for #6769.

Arithmetic: exact sympy over QQ throughout. The single numeric read-out (S8) is
mpmath at 60 dps off the canonical proton-pinned q0 string. No float64 anywhere;
no `float(`, no `statistics`/`math` aggregation. No witness by design -- this
probe removes a reading of a route, it does not produce a recorded value.

Run:
    PYTHONPATH=computations:tools/qou-substrate/python \\
      python3 -u computations/probes/w1_fibre_monodromy_order_probe.py
"""

from __future__ import annotations

import sys

import sympy as sp

CHECKS: list[tuple[str, bool]] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((label, bool(ok)))
    mark = "ok " if ok else "FAIL"
    print(f"  [{mark}] {label}" + (f"  --  {detail}" if detail else ""))


X, Z, R, W = sp.symbols("X Z R W")

# The colour spectral cubic (canonical; see QOU/Mass/ColorSpectralCubicGeometry.lean).
P = X**3 + (Z + 1) * X**2 + (Z**2 + Z + 1) * X + (Z**3 + Z**2 + Z + 1)


def banner(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


# ---------------------------------------------------------------- S1
banner("S1  the branch sextic is squarefree")

disc = sp.factor(sp.discriminant(P, X))
D = sp.expand(-disc)
D_poly = sp.Poly(D, Z)
print(f"  D(z) = {sp.expand(D)}")

expected = [16, 24, 35, 50, 35, 24, 16]
check(
    "D matches the corpus branchSextic coefficients",
    D_poly.all_coeffs() == expected,
    f"{D_poly.all_coeffs()}",
)
check("D = -disc_X P", sp.simplify(D + disc) == 0)

sqf = sp.gcd(D_poly, D_poly.diff(Z))
check(
    "D is squarefree (gcd(D, D') is a unit)",
    sp.Poly(sqf, Z).degree() == 0,
    f"gcd degree {sp.Poly(sqf, Z).degree()}",
)
check("deg D = 6", D_poly.degree() == 6)
check("D(0) = 16 != 0 (z=0 is not a branch point)", D_poly.eval(0) == 16)

# Squarefree over QQ is not yet "6 distinct roots in the algebraic closure" unless
# we say so; gcd(D, D') = 1 gives exactly that, but state the count explicitly.
roots = sp.Poly(D, Z).all_roots()
check("D has 6 roots, all distinct", len(roots) == 6 and len(set(roots)) == 6)

# ---------------------------------------------------------------- S2
banner("S2  the colour cubic has NO triple root, for any z  (no TOTAL branch point)")

# A triple root means P(X, z) = (X - r)^3 identically in X, i.e. the three
# coefficient equations below. These are the Lean hypotheses hc2 / hc1 / hc0.
triple = sp.expand(P - (X - R) ** 3)
coeff_eqs = [sp.expand(sp.Poly(triple, X).coeff_monomial(X**k)) for k in (2, 1, 0)]
for k, e in zip((2, 1, 0), coeff_eqs):
    print(f"  X^{k}:  {e} = 0")

sol = sp.solve(coeff_eqs, [Z, R], dict=True)
check(
    "the triple-root system (z, r) has NO solution",
    sol == [],
    f"sympy.solve -> {sol}",
)

# The two eliminations, matching the Lean proof step for step.
elimA = sp.expand(3 * coeff_eqs[1] - (Z + 1 - 3 * R) * coeff_eqs[0])
elimB = sp.expand(27 * coeff_eqs[2] - ((Z + 1) ** 2 - 3 * R * (Z + 1) + 9 * R**2) * coeff_eqs[0])
print(f"  eliminate r (quadratic vs linear):  {elimA} = 0")
print(f"  eliminate r (constant  vs linear):  {elimB} = 0")
check("elimination A is exactly 2z^2 + z + 2", sp.expand(elimA - (2 * Z**2 + Z + 2)) == 0)
check(
    "elimination B is exactly 26z^3 + 24z^2 + 24z + 26",
    sp.expand(elimB - (26 * Z**3 + 24 * Z**2 + 24 * Z + 26)) == 0,
)
g_elim = sp.gcd(sp.Poly(elimA, Z), sp.Poly(elimB, Z))
check(
    "the two eliminations have NO common root",
    sp.Poly(g_elim, Z).degree() == 0,
    f"gcd = {sp.factor(g_elim)}",
)

# ---------------------------------------------------------------- S3
banner("S3  every branch point is SIMPLE (vanishing order 1, two sheets collide)")

# Squarefree D already gives order 1 at every root; verify per root symbolically
# via the multiplicity recorded by sympy's factor list.
mults = [m for _, m in sp.Poly(D, Z).factor_list()[1]]
check(
    "every irreducible factor of D has multiplicity 1",
    all(m == 1 for m in mults),
    f"multiplicities {mults}",
)
# At a branch point the fibre cubic has a repeated root; S2 says it is never triple,
# so it is exactly a double root: precisely two sheets meet.
check(
    "so each branch point is a DOUBLE root of the fibre cubic, never a triple",
    sol == [] and all(m == 1 for m in mults),
    "local monodromy is a transposition -> order exactly 2",
)

# ---------------------------------------------------------------- S4
banner("S4  the cover is unramified over z = infinity")

# Put z = 1/w and rescale X = Y/w; the leading fibre as w -> 0.
Y = sp.symbols("Y")
P_inf = sp.expand(sp.simplify(P.subs({X: Y / W, Z: 1 / W}) * W**3))
fibre_inf = sp.expand(P_inf.subs(W, 0))
print(f"  leading fibre at infinity:  {sp.factor(fibre_inf)} = 0")
disc_inf = sp.discriminant(sp.Poly(fibre_inf, Y), Y)
check(
    "the fibre at infinity has 3 DISTINCT roots (disc != 0)",
    disc_inf != 0,
    f"disc = {disc_inf}",
)
fibre_zero = sp.factor(P.subs(Z, 0))
check(
    "and it coincides with the fibre at z = 0  (the palindromic z -> 1/z symmetry)",
    sp.expand(fibre_inf - P.subs({Z: 0, X: Y})) == 0,
    f"P(X,0) = {fibre_zero}",
)

# ---------------------------------------------------------------- S5
banner("S5  Riemann-Hurwitz: the genus of Sigma")

deg = 3
n_branch = 6                      # S1: six distinct finite branch points
ram_excess = n_branch * 1         # S3: each simple, so (e - 1) = 1 apiece
# 2g - 2 = deg * (2*0 - 2) + ram_excess          (base P^1 has genus 0)
two_g_minus_2 = deg * (-2) + ram_excess
genus = sp.Rational(two_g_minus_2 + 2, 2)
print(f"  2g - 2 = {deg}*(-2) + {ram_excess} = {two_g_minus_2}   =>   g = {genus}")
check("the genus is an integer", genus.is_integer, f"g = {genus}")
check("Sigma is an ELLIPTIC curve (g = 1)", genus == 1)

# ---------------------------------------------------------------- S6
banner("S6  CONTROL -- the same machinery on a curve that DOES have a total branch")

# X^3 - z has a total branch point at z = 0: all three sheets collide there.
P_ctl = X**3 - Z
triple_ctl = sp.expand(P_ctl - (X - R) ** 3)
eqs_ctl = [sp.expand(sp.Poly(triple_ctl, X).coeff_monomial(X**k)) for k in (2, 1, 0)]
sol_ctl = sp.solve(eqs_ctl, [Z, R], dict=True)
check(
    "the control DOES have a triple root (so the S2 method can answer 'yes')",
    sol_ctl != [],
    f"solutions {sol_ctl}",
)
disc_ctl = sp.expand(sp.discriminant(P_ctl, X))
mult_ctl = sp.Poly(disc_ctl, Z).factor_list()[1]
check(
    "and its discriminant vanishes to order 2, not 1",
    any(m == 2 for _, m in mult_ctl),
    f"disc = {sp.factor(disc_ctl)}, multiplicities {[m for _, m in mult_ctl]}",
)

# ---------------------------------------------------------------- S7
banner("S7  the quantum integers collapse at q = -1")

qm1 = sp.Integer(-1)
qints = [sp.expand(sum(qm1**i for i in range(n))) for n in range(0, 11)]
print("  [n]_{-1} for n = 0..10:  " + ", ".join(str(v) for v in qints))
check(
    "even quantum integers vanish at q = -1",
    all(qints[n] == 0 for n in range(0, 11, 2)),
)
check(
    "odd quantum integers are 1 at q = -1",
    all(qints[n] == 1 for n in range(1, 11, 2)),
)
check(
    "in particular [2]_{-1} = 0, falsifying the C1 carrier's standing hypothesis",
    qints[2] == 0,
    "qlift_normalized_kernel_exists assumes forall k >= 1, [k]_q != 0",
)

# ---------------------------------------------------------------- S8
banner("S8  the substrate q0 is not a root of unity at all")

try:
    from mpmath import mp  # type: ignore

    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # type: ignore

    mp.dps = 60
    q0 = Q_MP
    print(f"  q0 (proton pin, 25 sf) = {mp.nstr(q0, 25)}")
    # A root of unity has modulus exactly 1; q0 is real and > 1.
    check("q0 > 1, so |q0| != 1: q0 is not a root of unity", q0 > 1,
          f"q0 - 1 = {mp.nstr(q0 - 1, 12)}")
    check("q0 != -1 (the value the fibre monodromy supplies)", q0 != -1)
except Exception as exc:  # pragma: no cover - substrate package optional
    print(f"  (substrate read-out unavailable: {exc})")
    check("substrate read-out available", False, "qou_substrate not importable")

# ---------------------------------------------------------------- verdict
banner("VERDICT")

print("""  Route 2's fibre datum supplies the root of unity q = -1 and NOTHING ELSE:
  the branch sextic is squarefree (S1) and the colour cubic never has a triple
  root (S2), so every branch point is simple (S3) and its local monodromy is a
  transposition of order exactly 2. At q = -1 the quantum integers collapse to
  {0, 1} (S7), which FALSIFIES the standing hypothesis of the C1 carrier
  `qlift_normalized_kernel_exists` -- so that carrier does not apply there, and
  on every even index the recurrence determines nothing.

  SCOPE (b), invariant cited, for exactly one identification: q = the eigenvalue
  of the local fibre monodromy. Every looser reading of route 2 stays open at
  scope (a) at most -- a structure using the monodromy REPRESENTATION without
  setting q to an eigenvalue, one built at z = infinity, or one from the global
  S_3 rather than a local generator. Route 3 (Ramis-Sauloy-Zhang / Sauloy) is
  untouched.

  Carried forward for route 3: Sigma is an ELLIPTIC curve, g = 1 (S4 + S5) --
  six simple finite branch points, unramified at infinity. Which q-difference
  structures a genus-1 curve admits is exactly the input route 3 needs.

  D_q is NOT constructed. This removes a reading of a route.""")

n_ok = sum(1 for _, ok in CHECKS if ok)
n_all = len(CHECKS)
print()
print(f"  ALL CHECKS PASS: {n_ok == n_all}   ({n_ok}/{n_all})")
if n_ok != n_all:
    for label, ok in CHECKS:
        if not ok:
            print(f"    FAILED: {label}")
    sys.exit(1)
