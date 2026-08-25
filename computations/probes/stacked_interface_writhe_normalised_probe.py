#!/usr/bin/env python3
"""
Probe — which stacked crossings unbind, once the framing normalisation is applied.

`QOU/QBeta/InterfaceScalar.lean::stacked_crossing_gt_one` records that the
stacked crossing sigma^2 has interface scalar `mu = h*z + 1 > 1`, and the
two-nucleon audit reads that as the corpus's mechanism for an UNBOUND channel:
projectors give `mu < 1` (always bound), so unbinding needs leaving the convex
decomposition of 1, and sigma^2 does it.

That reading uses the RAW `mu`. But `_bond_type_L` — the production path — does
not: it applies the Lean-proved writhe normalisation

    L  ->  L - (delta_e / 2) * ln(1 - h)        (QOU/QBeta/WritheNormalisation.lean,
                                                 `writhe_factor_sq`, unique up to sign)

which is equivalent to grading the interface scalar to

    mu_eff = mu * (1 - h)^(e/2),    e = exponent sum of the stacked word.

The normalisation exists to make the invariant Markov-invariant, i.e.
framing-INDEPENDENT. So an unbinding claim that holds for `mu` but not for
`mu_eff` is a statement about a braid WORD, not about a link — it would change
under a Markov move, and a physical binding energy cannot.

This probe evaluates the whole family `sigma^m` and `sigma^-m` both ways.

## What it finds

Unbinding does **not** disappear under the normalisation — it MOVES.

* every POSITIVE power `sigma^m` has `mu_eff < 1` (bound), including `m = 2`,
  where the raw `mu = 1.128 > 1` flips to `mu_eff = 0.892 < 1`;
* the EVEN NEGATIVE powers `sigma^-2, -4, -6, -8` have `mu_eff > 1` (unbound),
  though their raw `mu < 1` would read as bound.

So the sign of the crossing that unbinds is OPPOSITE to the corpus's reading,
and the effect is a relocation within the same family rather than a loss of the
mechanism.

## Scope (STRICT)

**Scope-(a).** Nothing structural is excluded. Specifically NOT claimed:

* that `stacked_crossing_gt_one` is wrong — it states `1 < h*z + 1` for
  `0 < z, 0 < h`, pure arithmetic, and is untouched by anything here;
* that unbinding is unavailable — it is available, at even negative powers;
* that even-negative stacking is the physical two-nucleon interface. The
  magnitudes are still wrong: `sigma^-2` gives `B_eff = -0.613 MeV` against
  nature's `pp ~ -0.1`, `nn ~ -0.1`, `pn 1S0 ~ -0.066` — right sign, 6-9x too
  large, the same magnitude problem the rest of this axis has.

What IS claimed: the identification of `sigma^2` as *the* unbinding mechanism is
framing-dependent, and the production path already normalises that framing away.

## An oddity worth recording

`sigma^-7` gives `mu = -0.1508 < 0`. A negative interface scalar has no reading
as a suppression factor (`B = -alpha*ln(mu)` is undefined), so the family is not
uniformly interpretable and odd negative powers past -5 should not be used
without deciding what a negative trace ratio means.

## Method note

The 2-dimensional subalgebra `span{1, sigma}` is closed under multiplication via
`sigma^2 = h*sigma + 1`, so powers are computed by repeated multiplication

    (a s + b)(c s + d) = (a c h + a d + b c) s + (a c + b d)

rather than by a hand-derived recurrence. An earlier cut of this probe used a
hand-derived recurrence for the NEGATIVE powers and got it wrong (it reported
`mu(-2) = 0.7438`; the correct value is `0.9156`, since
`sigma^-2 = (sigma - h)^2 = -h*sigma + 1 + h^2`), which produced a spurious
"unbinding at -4 only" pattern. The `sigma * sigma^-1 = 1` assertion below is
the guard that catches that class of error; it is checked, not assumed.

NO WITNESS: exact algebra in the 2-dim interface subalgebra at the substrate
anchor; the printed table reproduces every number.

Bean qou-x66y follow-on; L2 binding axis.
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

MAXPOW = 8


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q50))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)          # convention D
    E0 = mp.mpf("4.1859813632944758969")
    w = 1 - h

    def mul(x, y):
        a, b = x
        c, d = y
        return (a * c * h + a * d + b * c, a * c + b * d)

    def power(base, m):
        r = (mp.mpf(0), mp.mpf(1))
        for _ in range(m):
            r = mul(r, base)
        return r

    S = (mp.mpf(1), mp.mpf(0))         # sigma
    Si = (mp.mpf(1), -h)               # sigma^-1 = sigma - h

    chk = mul(S, Si)
    tol = mp.mpf("1e-40")
    if abs(chk[0]) > tol or abs(chk[1] - 1) > tol:
        print(f"ABORT — sigma * sigma^-1 != 1 (got {chk}); the algebra is wrong.")
        return 1

    print("Stacked interface scalars, raw vs writhe-normalised\n")
    print(f"  q0 = {q!s:.14}  h = {float(h):.10f}  z = {float(z):.10f}  "
          f"(1-h) = {float(w):.10f}")
    print(f"  writhe grading: mu_eff = mu * (1-h)^(e/2), e = exponent sum\n")
    print("|   m | mu_raw       | mu_eff       | B_raw    | B_eff    | unbound raw | unbound eff |")
    print("| --: | -----------: | -----------: | -------: | -------: | :---------- | :---------- |")

    flips = []
    for sgn, base in ((+1, S), (-1, Si)):
        for m in range(1, MAXPOW + 1):
            a, b = power(base, m)
            mu = a * z + b
            e = sgn * m
            eff = mu * w ** (mp.mpf(e) / 2)
            braw = f"{float(-E0 * mp.log(mu)):+8.4f}" if mu > 0 else "     n/a"
            beff = f"{float(-E0 * mp.log(eff)):+8.4f}" if eff > 0 else "     n/a"
            ur, ue = mu > 1, eff > 1
            if ur != ue:
                flips.append((e, float(mu), float(eff)))
            print(f"| {e:+3d} | {float(mu):12.9f} | {float(eff):12.9f} | {braw} | {beff} "
                  f"| {str(ur):<11} | {str(ue):<11} |")

    pos_any = any((power(S, m)[0] * z + power(S, m)[1]) * w ** (mp.mpf(m) / 2) > 1
                  for m in range(1, MAXPOW + 1))
    neg_unbound = [m for m in range(1, MAXPOW + 1)
                   if (power(Si, m)[0] * z + power(Si, m)[1]) * w ** (-mp.mpf(m) / 2) > 1]

    print("\n## What changed\n")
    print(f"  positive powers with mu_eff > 1 (unbound after normalisation): {pos_any}")
    print(f"  negative powers with mu_eff > 1: {[-m for m in neg_unbound]}")
    print(f"  verdicts that FLIP under the normalisation: {len(flips)} of {2*MAXPOW}")
    print("\n  So unbinding is not lost — it MOVES to the even NEGATIVE powers, and the")
    print("  sign of the unbinding crossing is opposite to the corpus's sigma^2 reading.")
    print("  That reading uses the raw mu; the production path (_bond_type_L) already")
    print("  normalises the framing away, and a binding energy that depends on the")
    print("  framing is a property of the braid WORD, not of the link.")

    print("\n## Magnitudes — still wrong, stated plainly\n")
    a, b = power(Si, 2)
    mu2 = a * z + b
    eff2 = mu2 * w ** mp.mpf(-1)
    print(f"  sigma^-2:  B_eff = {float(-E0*mp.log(eff2)):+.4f} MeV")
    print("  nature:    pp ~ -0.1, nn ~ -0.1, pn 1S0 ~ -0.066 MeV")
    print("  -> right sign, 6-9x too large. No candidate is proposed here.")

    print("\n## Scope\n")
    print("  Scope-(a). `stacked_crossing_gt_one` (1 < h*z+1) is arithmetic and stands.")
    print("  Unbinding is NOT excluded; it is relocated. Even-negative stacking is NOT")
    print("  proposed as the physical interface. Nothing is fitted and nothing is wired.")
    print("\n(no witness by design — exact algebra, reproduced by the table.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
