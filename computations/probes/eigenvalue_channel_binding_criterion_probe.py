#!/usr/bin/env python3
"""
eigenvalue_channel_binding_criterion_probe — leaving the scalar space for the
OPERATOR gives, first, a mirror theorem (the spectral radius unbinds everything
exactly as the scalar binds everything), and then the first mechanism in this
sector to get all FOUR two-nucleon signs right with no parameter: read the
binding off the Hecke EIGENVALUE of the isospin channel, not off a scalar.

It is **not** a solution. The magnitudes are 4-6x out and, worse, exactly
antisymmetric where nature is 22:1 asymmetric. That falsification is the
sharpest thing here.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Owner-selected route 1 of 4,
worked in operator space at the owner's direction ("make sure you're not in the
scalars space ... particularly transfer matrices for the knot operators").

## 1. The mirror theorem — the naive operator reading fails as hard, oppositely

The corpus's transfer matrix (appendix `tm-general-form`) is

    T(c,d) = [[c*h + d, c], [c, d]]        acting on  a*sigma + b

and the scalar `mu = z + d` that the whole sector has been failing on is a
NUMBER READ OFF THIS OPERATOR. So the obvious operator invariant is the
spectral radius. Measured across the admissible range `d = -s`, `s in [0,h]`:

    det T(1,-s) = -s(h-s) - 1     =>     |det| = 1 + s(h-s) >= 1

with equality only at the endpoints (`sigma`, `sigma^-1`). Since for a 2x2
`|lambda_1 * lambda_2| = |det|`, we get `rho >= sqrt(|det|) >= 1` for EVERY
admissible `d`. Hence `B_oper = -alpha*log(rho) <= 0` always.

**So the operator reading UNBINDS EVERYTHING, exactly as the scalar reading
BINDS EVERYTHING** (`single_crossing_binds`, sorry-free: `mu` in `(0,1)`).
Neither can produce a MIX, and nature needs a mix. Two saturated readings of
one relation.

**And this kills the flattering surface reading.** The spectral radius "gets pp
and nn right" (both unbound) -- but `rho = q` is forced by the Hecke quadratic
for ANY braid generator at ANY `q > 1`, and says the same about the deuteron.
Right for a reason that cannot distinguish the channels. Not a finding.

## 2. What the mirror theorem points at

`|det| = 1` pins the GEOMETRIC MEAN of the two eigenvalues at 1. So they cannot
both be under 1, nor both over -- **they straddle it**:

    lambda_+ =  q      = 1.1099785828     |lambda| > 1
    lambda_- = -1/q    = -0.90091828396   |lambda| < 1

The mix the sector needs is *inside a single crossing*, and it is exactly
two-valued -- which is the shape of the problem (two isospin channels).

## 3. The criterion, and every link in it is forced

The spectral projectors are the isospin channels
(`docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`,
`mu_singlet_lt_mu_triplet`), and each projects onto one eigenvalue:

    P_+ = (sigma + 1/q)/(q + 1/q)   projects onto lambda_+ = q     <-> T = 1
    P_- = (q - sigma)/(q + 1/q)     projects onto lambda_- = -1/q  <-> T = 0

(`sigma * P_+ = q * P_+` is checked below, not asserted.) Reading the binding
off the channel's own eigenvalue, `B_T = -alpha*log|lambda_T|`:

    channel      nature                    |lambda|      B (MeV)     sign
    T=1  pp      UNBOUND                   1.10998       -0.43677    correct
    T=1  nn      UNBOUND                   1.10998       -0.43677    correct
    T=1  pn 1S0  UNBOUND (-0.066)          1.10998       -0.43677    correct
    T=0  pn 3S1  BOUND   (+2.224566)       0.90092       +0.43677    correct

**4 of 4 signs, with no parameter anywhere.** Nothing else in this sector has
managed that: the scalar reading is 1/4 (it binds all four), the spectral
radius is 3/4 but for a reason that cannot see the channels.

## 4. Is it vacuous? The falsification check says no

Every braid generator has eigenvalues `{q, -1/q}`, so the VALUES carry no
channel information. All the content is in the PAIRING, and the pairing is
derived (spectral projector = isospin channel), not chosen. The test is whether
the other pairing would also have "worked":

    T=1 <-> lambda_-  and  T=0 <-> lambda_+   gives   0 of 4 signs correct.

So the criterion is falsifiable and the derived pairing is the one that passes.
That is the whole evidential content and it is checked below.

## 5. 🛑 Where it fails, and the failure is sharp

    channel   B_model      nature        ratio
    T = 1     -0.43677     -0.066..-0.1  4.4x .. 6.6x too large
    T = 0     +0.43677     +2.224566     5.1x too small

Signs right, magnitudes wrong in OPPOSITE directions. And the structural
signature is worse than the sizes: the model predicts

    B(T=1) = -B(T=0) = -alpha*log q      EXACTLY antisymmetric

because `|lambda_+| * |lambda_-| = 1` -- the bar involution `q <-> 1/q`. Nature
is **22:1 asymmetric** (`2.2246` against `~0.1`). So this is a falsified
quantitative account, and it falsifies in a way that names the missing
structure: **whatever is absent breaks the bar symmetry between the channels.**

## What is and is not claimed

  * NOT a solution, not a closure, and nothing is wired or fitted.
  * NOT that the eigenvalue criterion is derived. It is *proposed* here; what
    is derived is each link (projector = channel, projector -> eigenvalue).
    Whether `B = -alpha*log|lambda|` is the right functional is open.
  * NOT that 4/4 signs is strong evidence on its own -- with two outcomes and
    a forced pairing it is one binary choice, not four independent ones. The
    honest weight is: it is the first mechanism whose sign structure is not
    wrong, and it is cheap to falsify further.
  * The magnitude failure is REPORTED, not explained away.

Scope **(a)**: a measurement plus a proposed criterion, with its own
falsification test run. AME/PDG are comparison targets only.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from _li_2_q_util import flavor_split_leading  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 50
TOL = mp.mpf(10) ** -40

# (label, T, nature is bound?, nature's |B| MeV or None)
CHANNELS = [
    ("pp  1S0", 1, False, mp.mpf("0.10")),
    ("nn  1S0", 1, False, mp.mpf("0.10")),
    ("pn  1S0", 1, False, mp.mpf("0.066")),
    ("pn  3S1", 0, True, AME_B_DEUTERON_MEV_VALIDATION),
]


def fmt(x, n=11):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q = Q_MP
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    al = me / (q * (q - 1))
    _d = flavor_split_leading(q)

    print("eigenvalue_channel_binding_criterion_probe")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}  h = {fmt(h)}  z = {fmt(z)}  alpha = {fmt(al)} MeV")
    print()

    print("1. MIRROR THEOREM — the naive operator reading fails, oppositely")
    print("-" * 78)
    print("  T(1,d) = [[h+d, 1],[1, d]];  det = (h+d)d - 1.  With d = -s:")
    print("     |det| = 1 + s(h-s) >= 1   for all s in [0,h]")
    print("  and |lambda_1 lambda_2| = |det|, so rho >= sqrt(|det|) >= 1 ALWAYS.")
    print()
    print(f"{'s':>12} {'|det|':>13} {'rho':>13} {'B_oper':>12} {'unbinds?':>9}")
    rho_min = None
    for k in range(0, 11):
        s = h * mp.mpf(k) / 10
        M = mp.matrix([[h - s, 1], [1, -s]])
        det = M[0, 0] * M[1, 1] - 1
        tr = M[0, 0] + M[1, 1]
        r = mp.sqrt(tr * tr - 4 * det)
        rho = max(abs((tr + r) / 2), abs((tr - r) / 2))
        assert abs(det) >= 1 - TOL, "|det| must be >= 1"
        assert rho >= 1 - TOL, "rho must be >= 1"
        if rho_min is None or rho < rho_min[0]:
            rho_min = (rho, s)
        if k % 2 == 0:
            print(f"{fmt(s, 8):>12} {fmt(abs(det), 9):>13} {fmt(rho, 9):>13} "
                  f"{fmt(-al * mp.log(rho), 8):>12} {str(rho > 1):>9}")
    print(f"\n  minimum rho over the range: {fmt(rho_min[0], 12)} at s = "
          f"{fmt(rho_min[1], 6)} (= h/2, the colour-weighted midpoint)")
    print("  => the OPERATOR reading unbinds EVERYTHING, as the SCALAR reading")
    print("     binds everything.  Neither can mix; nature needs a mix.")
    print()
    print("  And 'rho gets pp and nn right' is NOT a finding: rho = q is forced")
    print("  for any braid generator at any q > 1, and says the same about the")
    print("  deuteron.  Right for a reason that cannot see the channels.")
    print()

    print("2. WHAT IT POINTS AT — |det| = 1 makes the eigenvalues STRADDLE 1")
    print("-" * 78)
    lp, lm = q, -1 / q
    print(f"  lambda_+ = q    = {fmt(lp)}   |.| = {fmt(abs(lp))}  > 1")
    print(f"  lambda_- = -1/q = {fmt(lm)}   |.| = {fmt(abs(lm))}  < 1")
    print(f"  product of moduli = {fmt(abs(lp * lm))}  (the bar involution)")
    assert abs(abs(lp * lm) - 1) < TOL, "moduli must multiply to 1"
    print()

    print("3. THE PROJECTOR->EIGENVALUE PAIRING, CHECKED not asserted")
    print("-" * 78)
    # sigma in the 2-dim rep spanned by {sigma, 1}: matrix of left-mult by sigma
    S = mp.matrix([[h, 1], [1, 0]])
    I = mp.matrix([[1, 0], [0, 1]])
    Pp = (S + I / q) / (q + 1 / q)
    Pm = (I * q - S) / (q + 1 / q)
    print(f"  P+ + P- = I ?   {mp.norm(Pp + Pm - I) < TOL}")
    print(f"  P+ P-   = 0 ?   {mp.norm(Pp * Pm) < TOL}")
    print(f"  sigma P+ = q P+ ?      {mp.norm(S * Pp - q * Pp) < TOL}")
    print(f"  sigma P- = (-1/q) P- ? {mp.norm(S * Pm + Pm / q) < TOL}")
    for chk, nm in ((mp.norm(Pp + Pm - I), "P+ + P- = I"),
                    (mp.norm(Pp * Pm), "P+ P- = 0"),
                    (mp.norm(S * Pp - q * Pp), "sigma P+ = q P+"),
                    (mp.norm(S * Pm + Pm / q), "sigma P- = -P-/q")):
        assert chk < TOL, f"{nm} must hold"
    print("  => P+ is the lambda_+ = q eigenprojector, P- the lambda_- = -1/q one.")
    print("     The audit identifies P+ with T=1 and P- with T=0, so the pairing")
    print("     T=1 <-> q, T=0 <-> -1/q is DERIVED, not chosen.")
    print()

    print("4. THE CRITERION — B_T = -alpha*log|lambda_T|")
    print("-" * 78)
    print(f"{'channel':>10} {'T':>2} {'nature':>10} {'|lambda|':>12} "
          f"{'B (MeV)':>11} {'sign':>8}")
    n_ok = 0
    for nm, T, is_bound, natB in CHANNELS:
        lam = lp if T == 1 else lm
        B = -al * mp.log(abs(lam))
        ok = (B > 0) == is_bound
        n_ok += ok
        print(f"{nm:>10} {T:>2} {('BOUND' if is_bound else 'unbound'):>10} "
              f"{fmt(abs(lam), 8):>12} {fmt(B, 8):>11} "
              f"{('correct' if ok else 'WRONG'):>8}")
    print(f"\n  signs correct: {n_ok} of {len(CHANNELS)}")
    assert n_ok == 4, "the derived pairing must get all four signs"
    print()

    print("5. IS IT VACUOUS?  The other pairing is the falsification test")
    print("-" * 78)
    n_bad = sum(((-al * mp.log(abs(lm if T == 1 else lp))) > 0) == is_bound
                for _nm, T, is_bound, _b in CHANNELS)
    print(f"  swapped pairing (T=1 <-> -1/q, T=0 <-> q): {n_bad} of 4 correct")
    assert n_bad == 0, "the swapped pairing must fail all four"
    print("  => 0 of 4.  The criterion IS falsifiable and the DERIVED pairing is")
    print("     the one that passes.  The eigenvalue VALUES carry no channel")
    print("     information (every braid generator has {q,-1/q}); all the content")
    print("     is in the pairing, and the pairing is derived.")
    print()

    print("6. WHERE IT FAILS — sharply, and the failure names the gap")
    print("-" * 78)
    print(f"{'channel':>10} {'B_model':>11} {'nature':>11} {'ratio':>10}")
    for nm, T, _ib, natB in CHANNELS:
        B = -al * mp.log(abs(lp if T == 1 else lm))
        print(f"{nm:>10} {fmt(B, 8):>11} "
              f"{fmt(natB if T == 0 else -natB, 8):>11} "
              f"{fmt(abs(B) / natB, 5):>10}")
    B1 = -al * mp.log(q)
    B0 = -al * mp.log(1 / q)
    print(f"\n  B(T=1) = {fmt(B1, 9)}   B(T=0) = {fmt(B0, 9)}")
    print(f"  EXACTLY antisymmetric: B(T=1) + B(T=0) = {fmt(B1 + B0, 6)}")
    assert abs(B1 + B0) < TOL, "the model's two channels must be antisymmetric"
    print("  because |lambda_+||lambda_-| = 1 -- the bar involution q <-> 1/q.")
    nat_ratio = AME_B_DEUTERON_MEV_VALIDATION / mp.mpf("0.10")
    print(f"\n  nature's asymmetry: {fmt(nat_ratio, 6)} : 1   model's: 1 : 1")
    print("  So the account is FALSIFIED quantitatively, and it falsifies in a")
    print("  way that names the missing structure: whatever is absent BREAKS THE")
    print("  BAR SYMMETRY between the two channels.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT a solution or a closure.  Nothing wired, nothing fitted.")
    print("  * NOT that B = -alpha*log|lambda| is DERIVED.  Each LINK is derived")
    print("    (projector = channel; projector -> eigenvalue); the functional is")
    print("    proposed.")
    print("  * NOT that 4/4 is strong on its own -- with a forced pairing it is")
    print("    ONE binary choice, not four independent ones.  The honest weight:")
    print("    the first mechanism here whose sign structure is not wrong.")
    print("  * The magnitude failure is reported, not explained away.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
