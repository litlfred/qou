#!/usr/bin/env python3
"""W1 route 2, second reading: does the palindromic involution `z -> 1/z` lift to Sigma?

Wall W1 (bean `qou-d8de`) wants a q-difference prolongation `D_q` built from the colour
spectral curve `Sigma : P(X, z) = 0`.  Three prior tranches closed the *dilation* reading:

  #6695  route 1 in the base coordinate `z`
  #6738  route 1 in the ramified local coordinate `t`, `z = z_c + t^2`
  #6769  route 1 on `Sigma` itself  -- no `z -> l*z` with `l != 1` preserves the branch locus
  #7114  route 2's eigenvalue reading -- the fibre monodromy has order exactly 2, so `q = -1`,
         where the C1 carrier's own hypothesis `[k]_q != 0` is FALSE

#7114 left an explicitly-named opening:

    "#6769 closed dilations `z -> l z`; the palindromic symmetry `z -> 1/z` is NOT of that
     form and is not covered by it."

That is what this probe measures.  The corpus already knows `D` is palindromic and uses it at
the COEFFICIENT level -- the substitution `w = z + 1/z` collapsing the sextic to the reciprocal
cubic `16w^3 + 24w^2 - 13w + 2` (docs/audits/2026-05-19-delta-lambda-exploration-findings.md
Sec.H3).  What the corpus does NOT record is whether the involution lifts to the CURVE, and
what automorphism of `Sigma` it gives.

Sections
--------
  T1  the corpus branch sextic, its palindromicity, squarefreeness             (re-verify)
  T2  the colour cubic's coefficient closed form `a_k = 1 + z + ... + z^(3-k)` (re-verify)
  T3  THE LIFT IDENTITY   `z^3 * P(X/z, 1/z) == P(X, z)`   -- exact, in QQ(X, z)
  T4  the lift is an INVOLUTION: applying `(X,z) -> (X/z, 1/z)` twice is the identity
  T5  INVERSION RIGIDITY: `z^6 * D(l/z) == c * D(z)`  forces  `l = 1, c = 1`
      + CONTROL: the same elimination on a deliberately non-palindromic sextic must FAIL
  T6  FIXED POINTS of the lift on Sigma: exactly 4 (three over z=1, one over z=-1)
  T7  Riemann-Hurwitz for the degree-2 quotient: `Sigma / iota ~ P^1`, so the lift is the
      ELLIPTIC involution of the genus-1 curve `Sigma` (genus from #7114)
  T8  the substrate `q_0` has INFINITE order, so it is not supplied by an order-2 symmetry
  T9a the STRUCTURAL bound, exact and symbolic: a Moebius map is determined by three points,
      so `Stab(B)` embeds in `Sym(B) = S_6` and every base automorphism preserving `B` has
      finite order.  This is what the prune rests on; it holds for ANY squarefree sextic.
  T9b the explicit count `Stab(B) = {id, iota} = Z/2`, by cross-ratio at 120 dps.  A sharper
      picture, NOT load-bearing, and reported with its separation margin.

Precision discipline (AGENTS.md, NO-FLOAT64; probes are NOT exempt)
------------------------------------------------------------------
Every conclusion-bearing computation is exact `sympy` over `QQ`.  Two values are floating and
both are `mpmath`, never `float64`:

  * `q_0` (T8), read from the 50-digit proton-pinned string at 60 dps and used only for the
    comparison `q_0 > 1`;
  * the six roots of `D` (T9b) at 120 dps, used for a cross-ratio COUNT.  That count is
    labelled numerical wherever it appears and is not claimed exact; the probe prints the
    largest matching and smallest non-matching gap so the margin is visible rather than
    hidden behind a tolerance, and asserts a separation of >= 60 orders of magnitude.

No `float()`, no `statistics`, no `math`.  No witness by design: this probe decides a scope
question, it does not produce a recorded number.

Run
---
    PYTHONPATH=computations:tools/qou-substrate/python \
      python3 -u computations/probes/w1_palindromic_involution_lifts_probe.py
"""

from __future__ import annotations

import sys

import sympy as sp

CHECKS: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    CHECKS.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


X, Z, R, L, C, W = sp.symbols("X Z R L C W")

# The colour spectral cubic, as carried by
# QOU.Mass.ColorSpectralCubicGeometry (content/.../lean/QOU/Mass/).
P_XZ = X**3 + (Z + 1) * X**2 + (Z**2 + Z + 1) * X + (Z**3 + Z**2 + Z + 1)

# The branch sextic D(z) = -disc_X P.
D_Z = 16 * Z**6 + 24 * Z**5 + 35 * Z**4 + 50 * Z**3 + 35 * Z**2 + 24 * Z + 16


# ---------------------------------------------------------------- T1
print("\nT1  the branch sextic: corpus form, palindromicity, squarefreeness")

disc = sp.factor(sp.discriminant(sp.Poly(P_XZ, X)))
check(
    "D == -disc_X P  (the corpus identity, re-derived)",
    sp.simplify(sp.expand(disc + D_Z)) == 0,
    f"disc + D = {sp.expand(disc + D_Z)}",
)

coeffs = sp.Poly(D_Z, Z).all_coeffs()
check(
    "coefficients are the corpus [16,24,35,50,35,24,16]",
    coeffs == [16, 24, 35, 50, 35, 24, 16],
    str(coeffs),
)
check("D is palindromic (coefficients read the same both ways)", coeffs == coeffs[::-1])

check(
    "z^6 * D(1/z) == D(z)  exactly  (branchSextic_palindromic)",
    sp.simplify(sp.expand(Z**6 * D_Z.subs(Z, 1 / Z)) - D_Z) == 0,
)

g = sp.gcd(sp.Poly(D_Z, Z), sp.Poly(sp.diff(D_Z, Z), Z))
check("D is squarefree  (gcd(D, D') is a unit)", g.total_degree() == 0, f"gcd = {g}")

check("D(0) = 16 != 0, so 0 is NOT a branch point", D_Z.subs(Z, 0) == 16)


# ---------------------------------------------------------------- T2
print("\nT2  the colour cubic's coefficient closed form")

# a_k = sum_{i=0}^{3-k} z^i   for k = 0..3.
closed = sum(sum(Z**i for i in range(3 - k + 1)) * X**k for k in range(4))
check(
    "P(X,z) == sum_k (1 + z + ... + z^(3-k)) X^k",
    sp.simplify(sp.expand(closed - P_XZ)) == 0,
)


# ---------------------------------------------------------------- T3
print("\nT3  THE LIFT IDENTITY  --  z^3 * P(X/z, 1/z) == P(X, z)")

lhs = Z**3 * P_XZ.subs({X: X / Z, Z: 1 / Z}, simultaneous=True)
lift_gap = sp.simplify(sp.cancel(sp.expand(sp.together(lhs - P_XZ))))
check(
    "z^3 * P(X/z, 1/z) - P(X, z) == 0  in QQ(X, z)",
    lift_gap == 0,
    f"residual = {lift_gap}",
)
print("      => the map  iota~ : (X, z) |-> (X/z, 1/z)  carries Sigma to Sigma.")
print("         If P(X0,z0) = 0 and z0 != 0 then P(X0/z0, 1/z0) = z0^-3 P(X0,z0) = 0.")

# The equivalent statement in the form the Lean will carry.
lean_form = sp.simplify(
    sp.expand(sp.together(P_XZ.subs({X: X / Z, Z: 1 / Z}, simultaneous=True) - P_XZ / Z**3))
)
check("equivalently P(X/z, 1/z) == P(X,z) / z^3", lean_form == 0)


# ---------------------------------------------------------------- T4
print("\nT4  the lift is an involution")

x1, z1 = X / Z, 1 / Z
x2, z2 = sp.simplify(x1 / z1), sp.simplify(1 / z1)
check("iota~ applied twice returns (X, z)", (sp.simplify(x2 - X) == 0) and (sp.simplify(z2 - Z) == 0),
      f"({x2}, {z2})")
check("the base involution has order exactly 2 (z -> 1/z is not the identity)",
      sp.simplify(1 / Z - Z) != 0)


# ---------------------------------------------------------------- T5
print("\nT5  INVERSION RIGIDITY  --  which  z -> l/z  preserve the branch locus?")

# Necessary condition: z^6 D(l/z) = c D(z) as polynomials in z.
inv_lhs = sp.expand(Z**6 * D_Z.subs(Z, L / Z))
inv_eqs = sp.Poly(sp.expand(inv_lhs - C * D_Z), Z).all_coeffs()
sol_inv = sp.solve(inv_eqs, [L, C], dict=True)
print(f"      system: {[sp.simplify(e) for e in inv_eqs]}")
print(f"      solutions: {sol_inv}")
check(
    "the ONLY  z -> l/z  preserving B is  l = 1  (with c = 1)",
    sol_inv == [{L: 1, C: 1}],
    str(sol_inv),
)

# Cross-check against #6769's dilation result, using the same machinery.
dil_eqs = sp.Poly(sp.expand(D_Z.subs(Z, L * Z) - C * D_Z), Z).all_coeffs()
sol_dil = sp.solve(dil_eqs, [L, C], dict=True)
check(
    "CROSS-CHECK vs #6769: the only dilation preserving B is l = 1",
    sol_dil == [{L: 1, C: 1}],
    str(sol_dil),
)

# CONTROL.  The method must be able to say "no such l at all" -- otherwise a
# singleton answer above is not evidence.  Perturb D into a non-palindromic sextic.
D_bad = D_Z + Z
bad_eqs = sp.Poly(sp.expand(Z**6 * D_bad.subs(Z, L / Z) - C * D_bad), Z).all_coeffs()
sol_bad = sp.solve(bad_eqs, [L, C], dict=True)
check(
    "CONTROL: a non-palindromic sextic admits NO inversion at all",
    sol_bad == [],
    f"solutions for D+z: {sol_bad}",
)
print("      => the singleton above is a real determination, not a solver artefact.")


# ---------------------------------------------------------------- T6
print("\nT6  FIXED POINTS of the lift on Sigma")

# Fixed points need 1/z = z (so z = +-1) and X/z = X.
check("D(1) = 200 != 0, so the fibre over z=1 is unramified", D_Z.subs(Z, 1) == 200)
check("D(-1) = 4 != 0, so the fibre over z=-1 is unramified", D_Z.subs(Z, -1) == 4)

fib_p1 = sp.factor(P_XZ.subs(Z, 1))
fib_m1 = sp.factor(P_XZ.subs(Z, -1))
print(f"      fibre over z = +1 : {fib_p1}")
print(f"      fibre over z = -1 : {fib_m1}")
check(
    "P(X, 1) = X^3+2X^2+3X+4 is separable (3 distinct points over z=1)",
    sp.discriminant(sp.Poly(P_XZ.subs(Z, 1), X)) != 0,
    f"disc = {sp.discriminant(sp.Poly(P_XZ.subs(Z, 1), X))}",
)
check(
    "over z=+1 the lift acts as X -> X/1 = X, so ALL THREE points are fixed",
    sp.simplify(X / 1 - X) == 0,
)
check(
    "P(X, -1) = X(X^2+1), and over z=-1 the lift acts as X -> -X",
    sp.simplify(sp.expand(P_XZ.subs(Z, -1) - X * (X**2 + 1))) == 0,
)
check("so over z=-1 exactly ONE point (X = 0) is fixed", sp.solve(sp.Eq(-X, X), X) == [0])
check("and (0, -1) really is on Sigma", P_XZ.subs({X: 0, Z: -1}) == 0)

n_fixed = 3 + 1
check("total fixed points on the affine part: 4", n_fixed == 4, f"3 over z=1, 1 over z=-1")

fib_0 = sp.factor(P_XZ.subs(Z, 0))
print(f"      fibre over z = 0  : {fib_0}   (the lift SWAPS z=0 and z=infinity)")
check(
    "the lift swaps the fibres over 0 and infinity, so contributes no fixed point there",
    sp.simplify(sp.expand(P_XZ.subs(Z, 0) - (X + 1) * (X**2 + 1))) == 0,
)


# ---------------------------------------------------------------- T7
print("\nT7  Riemann-Hurwitz for the quotient  Sigma -> Sigma/iota~")

# genus of Sigma, from #7114: degree 3, six SIMPLE finite branch points, unramified at oo.
g_sigma = sp.Rational(3 * (-2) + 6 + 2, 2)
check("genus of Sigma = 1 (carried from #7114: 2g-2 = 3(-2) + 6 = 0)", g_sigma == 1,
      f"g_Sigma = {g_sigma}")

# 2 g_Sigma - 2 = 2 (2 g' - 2) + #fixed
g_quot = sp.solve(sp.Eq(2 * g_sigma - 2, 2 * (2 * W - 2) + n_fixed), W)
check(
    "the quotient has genus 0: Sigma/iota~ ~ P^1",
    g_quot == [0],
    f"2*1-2 = 2(2g'-2) + {n_fixed}  =>  g' = {g_quot}",
)
print("      => an order-2 automorphism of a genus-1 curve with 4 fixed points quotienting")
print("         to P^1 IS the elliptic (hyperelliptic) involution.  Sigma's 4 fixed points")
print("         are its 2-torsion for a suitable choice of origin.")

# The corpus's own w = z + 1/z is the quotient coordinate on the BASE.
recip = sp.simplify(sp.expand(D_Z / (16 * Z**3)))
recip_cubic = sp.expand(16 * (W**3 - 3 * W) + 24 * (W**2 - 2) + 35 * W + 50)
print(f"      corpus reciprocal cubic (2026-05-19 Sec.H3): 16w^3+24w^2-13w+2")
check(
    "the corpus's w = z + 1/z reduction IS the base quotient by iota, re-derived",
    sp.simplify(recip_cubic - (16 * W**3 + 24 * W**2 - 13 * W + 2)) == 0,
    f"pushforward = {sp.expand(recip_cubic)}",
)


# ---------------------------------------------------------------- T8
print("\nT8  the substrate q_0 has infinite order, so no order-2 symmetry supplies it")

try:
    import mpmath as mp
    from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP

    mp.mp.dps = 60
    q0 = Q_MP
    check(
        "|q_0| > 1, so q_0^n != 1 for every n >= 1: q_0 is NOT a root of unity",
        q0 > 1,
        f"q_0 = {mp.nstr(q0, 25)}  (proton pin, 60 dps)",
    )
except Exception as exc:  # pragma: no cover - environment-dependent
    check("q_0 read from the 50-digit proton pin", False, f"unavailable: {exc}")

print("      => the base shift  z -> q_0^2 z  has INFINITE order.  An automorphism of")
print("         order 2 cannot be it, whatever else it is good for.")


# ---------------------------------------------------------------- T9
print("\nT9  the full Moebius stabiliser of B  --  structural bound (exact) + explicit count (120 dps)")

M_A, M_B, M_C, M_D = sp.symbols("M_A M_B M_C M_D")

# (9a) The STRUCTURAL half, exact and symbolic: a Moebius map with three distinct fixed
#      points is the identity.  Fixed points of `(az+b)/(cz+d)` solve `cz^2+(d-a)z-b = 0`,
#      a quadratic; three distinct roots force it to vanish identically.
fixed_pt_quadratic = sp.expand(M_C * Z**2 + (M_D - M_A) * Z - M_B)
check(
    "fixed points of (az+b)/(cz+d) solve  c z^2 + (d-a) z - b = 0",
    sp.simplify(sp.expand(sp.together((M_A * Z + M_B) - Z * (M_C * Z + M_D))) + fixed_pt_quadratic)
    == 0,
    f"{fixed_pt_quadratic}",
)
degenerate = sp.solve([M_C, M_D - M_A, -M_B], [M_B, M_C, M_D], dict=True)
check(
    "three distinct fixed points force b=0, c=0, d=a: the IDENTITY",
    degenerate == [{M_B: 0, M_C: 0, M_D: M_A}],
    str(degenerate),
)
print("      => Stab(B) -> Sym(B) = S_6 is INJECTIVE, so |Stab(B)| divides 720 and EVERY")
print("         base automorphism preserving B has order at most 6.  This holds for any")
print("         squarefree sextic branch locus; it is what makes the prune structural")
print("         rather than a property of this particular D.")

# (9b) The explicit determination.  Enumerate the 6*5*4 = 120 Moebius maps sending the
#      first three roots to an ordered triple of roots, and keep those mapping ALL of B
#      into B.  Realisability is decided by cross-ratio, computed with mpmath at 120 dps
#      -- NOT float64.  The separation between matching and non-matching cross-ratios is
#      reported so the reader can see the margin rather than trust a tolerance.
try:
    import itertools

    import mpmath as mp

    mp.mp.dps = 120
    roots = mp.polyroots([mp.mpf(c) for c in coeffs], maxsteps=200, extraprec=400)
    check("D has 6 roots at 120 dps", len(roots) == 6, f"{len(roots)} roots")

    def crn(p, q, r, s):
        """Cross-ratio `(p,q,r; s)` as a projective pair `(numerator, denominator)`.

        Kept unreduced so that `s == r` (cross-ratio `= infinity`) is representable
        instead of raising: two cross-ratios agree iff `n1*d2 == n2*d1`.
        """
        return ((s - p) * (q - r), (s - r) * (q - p))

    def gap(a, b):
        """Scale-free disagreement of two projective cross-ratios."""
        n1, d1 = a
        n2, d2 = b
        num = abs(n1 * d2 - n2 * d1)
        den = abs(n1 * d2) + abs(n2 * d1)
        return num / den if den != 0 else mp.mpf(0)

    base = (roots[0], roots[1], roots[2])
    matched: list = []
    unmatched: list = []
    realised = 0
    realised_perms = []
    for trip in itertools.permutations(range(6), 3):
        tgt = (roots[trip[0]], roots[trip[1]], roots[trip[2]])
        perm = {0: trip[0], 1: trip[1], 2: trip[2]}
        ok = True
        for i in range(3, 6):
            cr = crn(*base, roots[i])
            best_j, best_d = None, None
            for j in range(6):
                d = gap(cr, crn(*tgt, roots[j]))
                if best_d is None or d < best_d:
                    best_j, best_d = j, d
                if d > mp.mpf(10) ** -80:
                    unmatched.append(d)
            if best_d > mp.mpf(10) ** -80:
                ok = False
                break
            matched.append(best_d)
            perm[i] = best_j
        if ok and len(set(perm.values())) == 6:
            realised += 1
            realised_perms.append(tuple(perm[i] for i in range(6)))

    worst_match = max(matched) if matched else mp.mpf(0)
    best_nonmatch = min(unmatched) if unmatched else mp.mpf(0)
    print(f"      largest  MATCHING cross-ratio gap : {mp.nstr(worst_match, 6)}")
    print(f"      smallest NON-match cross-ratio gap: {mp.nstr(best_nonmatch, 6)}")
    check(
        "the two populations are separated by >= 60 orders of magnitude",
        best_nonmatch > worst_match * mp.mpf(10) ** 60,
        "so the count below does not depend on the tolerance",
    )
    print(f"      realised permutations of B: {sorted(set(realised_perms))}")
    check(
        "exactly 2 Moebius maps preserve B, i.e. Stab(B) = {id, iota} = Z/2",
        realised == 2,
        f"|Stab(B)| = {realised} (120 dps; identity + one fixed-point-free involution)",
    )
except Exception as exc:  # pragma: no cover - environment-dependent
    check("explicit Stab(B) determination", False, f"unavailable: {type(exc).__name__}: {exc}")


# ---------------------------------------------------------------- verdict
print("\n" + "=" * 78)
n_pass = sum(1 for _, ok, _ in CHECKS if ok)
n_tot = len(CHECKS)
print(f"  {n_pass}/{n_tot} checks passed")
for name, ok, detail in CHECKS:
    if not ok:
        print(f"    FAILED: {name}  --  {detail}")
print("=" * 78)
print(
    """
VERDICT

  POSITIVE (new).  The palindromic involution `z -> 1/z` DOES lift to Sigma, by the exact
  identity `z^3 P(X/z, 1/z) = P(X, z)`.  The lift `(X,z) |-> (X/z, 1/z)` is an involution
  with exactly 4 fixed points on the genus-1 curve Sigma, so by Riemann-Hurwitz the quotient
  is P^1 and the lift IS the elliptic involution.  This is the first nontrivial automorphism
  of Sigma the corpus carries; the base quotient coordinate is the `w = z + 1/z` already used
  for the Galois-orbit reduction.

  PRUNE, scope (b).  The load-bearing step is STRUCTURAL and exact (T9a): a Moebius map is
  determined by three points, so the stabiliser of a squarefree sextic's 6-point root set
  embeds in S_6 and every base automorphism preserving B has order at most 6 -- FINITE, for
  any such branch locus, not just this one.  The substrate shift `z -> q_0^2 z` has infinite
  order (T8, |q_0| > 1).  Therefore NO base automorphism of P^1 supplies the W1 q-shift --
  not merely no dilation (#6769), and not merely no order-2 map.

  The explicit count `Stab(B) = {id, iota} = Z/2` (T9b) is a 120-dps NUMERICAL determination
  by cross-ratio, reported with the separation between the matching and non-matching
  populations so the margin is visible.  It sharpens the picture; it is NOT what the prune
  rests on, and it is not claimed as exact.

  NOT excluded.  A q-difference structure that does not come from a base automorphism at all
  (route 3: Ramis-Sauloy-Zhang / Sauloy, now supplied with genus AND an involution); anything
  built from the monodromy REPRESENTATION rather than an automorphism; `D_q` is NOT constructed.
"""
)

sys.exit(0 if n_pass == n_tot else 1)
