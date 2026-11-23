#!/usr/bin/env python3
"""
Probe — the ribbon twist is T-ODD, and that is exactly what the writhe lacks.

The two-nucleon sector needs `T=1` UNBOUND (pp, nn, np-1S0) and `T=0` BOUND (the
deuteron). Three gradings, compared on whether they can even express that:

## 1. Writhe / stacking — IMPOSSIBLE for every m (proved here by ratio)

Under `sigma^m`, the spectral action is `sigma^m P+ = q^m P+` and
`sigma^m P- = (-1/q)^m P-`, so with the writhe normalisation

    mu_eff(T1) = q^m  * mu+ * (1-h)^(m/2)
    mu_eff(T0) = (1/q)^m * mu- * (1-h)^(m/2)      (m even)

The writhe factor is IDENTICAL in both channels, so in the ratio it CANCELS:

    mu_eff(T1) / mu_eff(T0) = q^(2m) * (mu+/mu-)

The writhe is **T-blind**. Only `q^(2m)` orders the channels, and it orders them
the wrong way for negative `m`:

    ratio > 1        <=>  m > -5.334
    T=1 unbound      <=>  m <= -21.978

Incompatible for every `m`. The antisymmetric channel always unbinds FIRST,
because `sigma` acts with `|eigenvalue| = 1/q < 1` on `P-` and `q > 1` on `P+`,
so negative powers AMPLIFY `P-`. This is a structural obstruction, not a
magnitude shortfall.

## 2. Ribbon twist — the structure IS right

The twist acts on the irrep `V_lambda` by `theta_lambda = q^{c(lambda)}`, and the
corpus proves the chirality law `theta_{lambda'} = theta_lambda^{-1}`
(`QOU/BraidKnot/KeystoneModularTwist.lean`). At `n = 2`, `c((2)) = +1` and
`c((1,1)) = -1`, so a framing `f` contributes

    T=1  ->  q^{+f}          T=0  ->  q^{-f}

**opposite** exponents. In the ratio, `q^{2f}` — the twist is **T-odd** where the
writhe is T-blind. This is the property the two-nucleon problem needs, and it is
derived, not chosen: it follows from `c(lambda') = -c(lambda)`.

A threshold follows: both conditions hold simultaneously for `f >= 3`
(`f > 2.723` exactly).

## 3. The numbers at the threshold — and what they are NOT

    f = 3:   B(T=1) = -0.1211 MeV      nature ~ -0.07 MeV (unbound)   1.7x
             B(T=0) = +7.1588 MeV      nature  +2.2246    (deuteron)  3.2x

The sign structure is correct — the first construction on this axis for which
that is true. The `T=1` magnitude is within a factor 1.7. The deuteron is 3.2x
over.

## HONESTY FLAG — `f = 3` is NOT derived, and choosing it would be a fit

`f >= 3` is a *threshold*, and `f = 3` is merely the smallest integer meeting it.
"Smallest framing that unbinds" is a selection principle only if something forces
minimality; nothing here does. **Adopting `f = 3` because it reproduces the data
is a fit** and is blocked by the AGENTS.md anti-fit discipline exactly as the
seven Delta_lambda ansaetze were.

What IS derived and survives regardless of `f`:

* the twist is T-odd (`theta_{lambda'} = theta_lambda^{-1}`), so it CAN express
  the required sign structure;
* the writhe is T-blind, so it CANNOT — for any magnitude, any sign;
* a finite threshold exists.

What is open: whether the framing of the two-nucleon interface is derivable at
all, and if so whether it lands at 3. Note also that a previous keystone result
on this branch forced `f = 0` in the BW-vacuum-row context
(`KeystoneFramingTrivialAtRootsOfUnity.lean`) — a DIFFERENT context (matching the
Hecke side at roots of unity, not framing a two-nucleon interface), but a warning
that framings in this framework are not free to assign.

NO WITNESS: exact spectral algebra at the substrate anchor; the tables reproduce
every number.

Beans qou-brg3 / qou-pjx4; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp
from q_parameter import Q_50_DIGIT_STR as Q50
from _precision import set_compute_dps  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION  # noqa: E402  (AME registry)

E0_STR = "4.1859813632944758969"
NATURE_T1 = -0.07      # 1S0 virtual state, MeV (Machleidt CD-Bonn a<0 channels)
NATURE_T0 = +float(AME_B_DEUTERON_MEV_VALIDATION)  # deuteron, MeV


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q50))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    w = 1 - h
    E0 = mp.mpf(E0_STR)
    mup = (z + 1 / q) / (q + 1 / q)     # T = 1, symmetric
    mum = (q - z) / (q + 1 / q)         # T = 0, antisymmetric

    print("Ribbon twist vs writhe: which grading can express the two-nucleon signs?\n")
    print(f"  q0 = {float(q):.12f}   mu+ (T=1) = {float(mup):.9f}   "
          f"mu- (T=0) = {float(mum):.9f}")
    print(f"  mu+ + mu- = {float(mup + mum):.6f}  (the convex decomposition of 1)\n")
    print("  TARGET:  T=1 UNBOUND (pp, nn, np-1S0)   and   T=0 BOUND (deuteron)\n")

    # ---- 1. writhe / stacking ------------------------------------------------
    print("1. WRITHE / STACKING — the factor cancels in the ratio\n")
    print("   sigma^m P+ = q^m P+ ,  sigma^m P- = (-1/q)^m P-")
    print("   mu_eff(T1)/mu_eff(T0) = q^(2m) * (mu+/mu-)   <- (1-h)^(m/2) GONE\n")
    m_ratio = mp.log(mum / mup) / (2 * mp.log(q))
    m_unb = mp.log(1 / mup) / mp.log(q * mp.sqrt(w))
    print(f"   ratio > 1   (T1 above T0)  <=>  m > {float(m_ratio):.3f}")
    print(f"   T=1 unbound                <=>  m <= {float(m_unb):.3f}")
    feasible_w = float(m_ratio) < float(m_unb)
    print(f"   both simultaneously satisfiable: {feasible_w}")
    print("\n   The writhe is T-BLIND. sigma acts with |eigenvalue| 1/q < 1 on P- and")
    print("   q > 1 on P+, so negative powers AMPLIFY P-: the ANTISYMMETRIC channel")
    print("   unbinds first, which is backwards. Structural, not a magnitude issue.\n")

    # ---- 2. ribbon twist -----------------------------------------------------
    print("2. RIBBON TWIST — theta_lambda = q^c(lambda), theta_{lambda'} = theta_lambda^-1\n")
    print("   n=2:  c((2)) = +1, c((1,1)) = -1   ->   T=1 gets q^+f, T=0 gets q^-f")
    print("   ratio = q^(2f) * (mu+/mu-)  -- OPPOSITE exponents: the twist is T-ODD\n")
    print("   |  f | mu_eff(T=1) | mu_eff(T=0) | T1 unbound | T0 bound | BOTH |")
    print("   | -: | ----------: | ----------: | :--------- | :------- | :--- |")
    hits = []
    for f in range(0, 9):
        e1 = mup * q ** f
        e0 = mum * q ** (-f)
        a = e1 > 1
        b = (e0 > 0) and (e0 < 1)
        if a and b:
            hits.append(f)
        print(f"   | {f:2d} | {float(e1):11.7f} | {float(e0):11.7f} | {str(a):<10} "
              f"| {str(b):<8} | {str(a and b):<4} |")

    thr = mp.log(1 / mup) / mp.log(q)
    print(f"\n   exact threshold: f > {float(thr):.4f}  ->  integer framings f >= 3")
    print(f"   f giving BOTH (f <= 8): {hits}")

    if not hits:
        print("\n   no framing works — the twist route is dead.")
        return 1

    f = hits[0]
    e1 = mup * q ** f
    e0 = mum * q ** (-f)
    b1 = -E0 * mp.log(e1)
    b0 = -E0 * mp.log(e0)
    print(f"\n3. NUMBERS AT THE THRESHOLD f = {f}\n")
    print(f"   B(T=1) = {float(b1):+8.4f} MeV     nature ~ {NATURE_T1:+.4f} "
          f"(1S0 virtual)   ratio {abs(float(b1) / NATURE_T1):.2f}x")
    print(f"   B(T=0) = {float(b0):+8.4f} MeV     nature  {NATURE_T0:+.4f} "
          f"(deuteron)      ratio {float(b0) / NATURE_T0:.2f}x")
    print("\n   The SIGN STRUCTURE is correct -- the first construction on this axis")
    print("   for which that is true. T=1 magnitude within 1.7x; deuteron 3.2x over.")

    print("\n## HONESTY FLAG — f = 3 is NOT derived\n")
    print("   f >= 3 is a THRESHOLD; f = 3 is merely the smallest integer meeting it.")
    print("   'Smallest framing that unbinds' is a selection principle only if")
    print("   something forces minimality, and nothing here does. Adopting f = 3")
    print("   BECAUSE it reproduces the data is a FIT, blocked by the same discipline")
    print("   that blocked the seven Delta_lambda ansaetze. Nothing is wired.")
    print("\n   DERIVED and f-independent:")
    print("     - the twist is T-odd (theta_{lambda'} = theta_lambda^-1), so it CAN")
    print("       express the required sign structure;")
    print("     - the writhe is T-blind, so it CANNOT, at any magnitude or sign;")
    print("     - a finite threshold exists.")
    print("   OPEN: whether the two-nucleon framing is derivable, and whether it is 3.")
    print("\n   Caution from this branch's own keystone work: the framing gate forced")
    print("   f = 0 in the BW-vacuum-row context (KeystoneFramingTrivialAtRootsOfUnity).")
    print("   Different context -- but framings here are not free to assign.")
    print("\n(no witness by design — exact spectral algebra, tables reproduce it.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
