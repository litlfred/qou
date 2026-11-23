#!/usr/bin/env python3
"""
hoefsmit_offdiagonal_exclusion_probe — the off-diagonal of the Hoefsmit
`V_(2,1)` block, the last concrete carrier the bond family cannot reach, ALSO
always binds. Scope (b), and the invariant it needs is already proved
sorry-free. En route it establishes four exact identities showing that the
isospin projectors and the Hoefsmit block are ONE object seen two ways.

Bean `qou-brng`, arc `bk-crossing-mass-binding`. Owner-selected route 2 of 4.

## Why this object

`docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`
closes with a structural note: the bond family and the projectors

    "are the diagonal and off-diagonal data of one 2x2 Hoefsmit V_(2,1) block of
     H_3. The bond family has no access to the off-diagonal, which is exactly
     *why* t is confined to [z-h, z] and the projectors sit outside it on both
     sides."

That names a concrete carrier which is (i) already in the algebra, (ii)
provably unreachable by the family whose every member is now excluded. It was
the cheapest of the four surviving routes, so it went first.

## The block, solved exactly — no fitting, no grid

With `sigma_1 = diag(q, -1/q)` on the two standard tableaux of `(2,1)`, write
`sigma_2 = [[a,b],[c,d]]`. The Hecke quadratic fixes `tr = h` and `det = -1`;
the braid relation `s1 s2 s1 = s2 s1 s2` then forces `a*q - d/q = -1`, giving

    a = -1/(q(q^2+1))        d = h - a        b*c = a*d + 1

**Four identities, each exact to 50 dps (not numerical coincidences):**

    a        = -(z - h)          the LOWER endpoint of the bond range, negated
    d        =   z               the UPPER endpoint
    b*c      =   mu_+            the isospin TRIPLET projector scalar
    z*(z-h)  =   mu_-            the isospin SINGLET projector scalar

So the audit's structural note is an identity: the bond family's interval
`[z-h, z]` **is** the block's diagonal, and `mu_+`, `mu_-` are its off-diagonal
product and its diagonal product. The projectors were never a separate
mechanism from the bond family -- they are the same 2x2 block read the other
way.

## The exclusion

The off-diagonal magnitude in the symmetric (seminormal) normalisation is

    |b| = sqrt(b*c) = sqrt(mu_+) = sqrt(1 - z(z-h)) = 0.867584066965

    B = -alpha*log|b| = -(alpha/2)*log(mu_+) = +0.5945887844 MeV   -> BOUND

and it binds **for every q**, not just at the anchor:

    |b|^2 = mu_+ = 1 - z(z-h),  and  h < z  is  QOU.QBeta.h_lt_markov_z
    (sorry-free, unconditional for q > 0, reducing to q^4 - 1 < q^4).

    h < z  =>  z - h > 0,  and  z > 0,  so  z(z-h) > 0,  so  mu_+ < 1,
    so  |b| < 1,  so  B = -alpha*log|b| > 0.

**Scope (b)** -- a structural exclusion with the invariant named and already
proved, not a search that came up empty. Reaching nature's unbound `T = 1`
channel needs `|b| > 1`, i.e. `z(z-h) < 0`, i.e. `h > z` -- which is the same
condition `SingleCrossingAlwaysBinds` shows fails at the substrate by 24 %.

## What this closes, and what it does not

**Closes:** the off-diagonal as a carrier for the unbound two-nucleon channels.
It was the last *concrete, already-existing* object outside the bond family, and
it fails for the same reason everything else does.

**Does NOT close:** the two remaining owner-selected routes, neither of which is
an object already in the algebra --

  * a **non-separable `(S,L)` coupling** (`qou-vbyi`): the corpus closed the
    space index entering as a FACTOR (`separable_interface_degenerate`,
    axiom-free) and explicitly left the non-factoring coupling live. Nothing
    here touches it; a coupling is precisely not a product of block data.
  * a **non-tracial functional** (the #6399 trilemma).

**And it sharpens why.** Every excluded route -- single crossing, stacked
powers, projector-composed stacking, higher Hecke rank, spin(x)isospin,
separable space factor, and now the off-diagonal -- is a *scalar read off one
block*. The identities above show the projector route and the bond route were
never independent attempts. What has never been tried is an interface that is
not a single scalar at all, which is exactly what routes 1 and 4 propose.

## Scope

Scope **(b)**, invariant cited (`h_lt_markov_z`). Nothing wired, nothing fitted;
no comparison to AME is inverted into a weight.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin. The block is solved in
closed form from the braid relation, not searched.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402

mp.mp.dps = 50
TOL = mp.mpf(10) ** -45


def fmt(x, n=12):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q = mp.mpf(Q_50_DIGIT_STR)
    h = q - 1 / q
    z = q**3 / (q**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    al = _qbeta_e0.order_zero_scaled(me, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    print("hoefsmit_offdiagonal_exclusion_probe")
    print("=" * 78)
    print(f"q = {fmt(q, 17)}   h = {fmt(h)}   z = {fmt(z)}   alpha = {fmt(al)} MeV")
    print()
    print("THE BLOCK, SOLVED IN CLOSED FORM FROM THE BRAID RELATION")
    print("-" * 78)
    print("  sigma_1 = diag(q, -1/q) on the two standard tableaux of (2,1).")
    print("  sigma_2 = [[a,b],[c,d]]:  Hecke quadratic gives tr = h, det = -1;")
    print("  the braid relation s1 s2 s1 = s2 s1 s2 forces  a*q - d/q = -1, so")
    print("      a = -1/(q(q^2+1)),   d = h - a,   b*c = a*d + 1.")
    print()
    a = -1 / (q * (q**2 + 1))
    d = h - a
    bc = a * d + 1
    # verify the braid relation itself, on the constructed matrices
    b = mp.sqrt(bc)
    s1 = mp.matrix([[q, 0], [0, -1 / q]])
    s2 = mp.matrix([[a, b], [b, d]])
    resid = mp.norm(s1 * s2 * s1 - s2 * s1 * s2)
    print(f"  braid-relation residual on the constructed matrices: {fmt(resid, 6)}")
    assert resid < TOL, "the closed-form block must satisfy the braid relation"
    assert abs(mp.det(s2) + 1) < TOL, "det sigma_2 must be -1"
    assert abs((a + d) - h) < TOL, "tr sigma_2 must be h"
    print(f"  det = {fmt(mp.det(s2), 8)}  (must be -1)     "
          f"tr = {fmt(a + d, 8)}  (must be h)")
    print()

    print("FOUR EXACT IDENTITIES — the projectors ARE the block")
    print("-" * 78)
    mu_p = (z + 1 / q) / (q + 1 / q)
    mu_m = (q - z) / (q + 1 / q)
    checks = [
        ("a", a, "-(z - h)", -(z - h), "lower bond endpoint, negated"),
        ("d", d, "z", z, "upper bond endpoint"),
        ("b*c", bc, "mu_+", mu_p, "isospin TRIPLET projector"),
        ("z*(z-h)", z * (z - h), "mu_-", mu_m, "isospin SINGLET projector"),
    ]
    print(f"{'lhs':>10} {'value':>18} {'rhs':>10} {'value':>18}  exact?")
    for ln, lv, rn, rv, _note in checks:
        ok = abs(lv - rv) < TOL
        print(f"{ln:>10} {fmt(lv):>18} {rn:>10} {fmt(rv):>18}  {ok}")
        assert ok, f"{ln} must equal {rn} exactly"
    print()
    print("  => the audit's structural note is an IDENTITY: the bond family's")
    print("     interval [z-h, z] IS the block's diagonal, and mu_+ / mu_- are")
    print("     its off-diagonal product / diagonal product.  The projector route")
    print("     and the bond route were never independent attempts.")
    print()

    print("THE EXCLUSION — scope (b), invariant already proved sorry-free")
    print("-" * 78)
    od = mp.sqrt(bc)
    B = -al * mp.log(od)
    print(f"  |b| = sqrt(mu_+) = sqrt(1 - z(z-h)) = {fmt(od)}")
    print(f"  B   = -(alpha/2)*log(mu_+)          = {fmt(B, 10)} MeV   -> BOUND")
    assert od < 1 and B > 0, "the off-diagonal must bind at the anchor"
    print()
    print("  and it binds for EVERY q, not just at the anchor:")
    print("    |b|^2 = mu_+ = 1 - z(z-h),  and  h < z  is  QOU.QBeta.h_lt_markov_z")
    print("    (sorry-free, unconditional for q > 0; reduces to q^4 - 1 < q^4).")
    print("    h < z  =>  z-h > 0;  z > 0;  so z(z-h) > 0;  so mu_+ < 1;")
    print("    so |b| < 1;  so B > 0.")
    assert h < z, "h < z is the cited invariant"
    assert z * (z - h) > 0 and mu_p < 1, "hence mu_+ < 1"
    print()
    print("  sanity sweep over q (the invariant is not anchor-specific):")
    print(f"{'q':>10} {'h':>12} {'z':>12} {'h<z':>6} {'|b|':>12} {'binds':>6}")
    for qq in ("1.02", "1.10998", "1.25", "1.40", "1.46"):
        Q = mp.mpf(qq)
        H = Q - 1 / Q
        Z = Q**3 / (Q**2 + 1)
        BB = mp.sqrt(1 - Z * (Z - H))
        print(f"{qq:>10} {fmt(H, 8):>12} {fmt(Z, 8):>12} {str(H < Z):>6} "
              f"{fmt(BB, 8):>12} {str(BB < 1):>6}")
        assert H < Z and BB < 1, "must bind across the whole admissible range"
    print()
    print("  Reaching nature's UNBOUND T=1 channel needs |b| > 1, i.e. z(z-h) < 0,")
    print("  i.e. h > z -- the same condition SingleCrossingAlwaysBinds shows")
    print("  fails at the substrate by 24 %.  Same wall, different door.")
    print()

    print("WHAT THIS CLOSES, AND WHAT IT DOES NOT")
    print("-" * 78)
    print("  CLOSES: the off-diagonal as a carrier for the unbound channels --")
    print("    the last CONCRETE, already-existing object outside the bond family.")
    print()
    print("  DOES NOT CLOSE the two remaining owner-selected routes, neither of")
    print("  which is an object already in the algebra:")
    print("    * a NON-SEPARABLE (S,L) coupling (qou-vbyi).  The corpus closed")
    print("      the space index entering as a FACTOR")
    print("      (separable_interface_degenerate, axiom-free) and left the")
    print("      non-factoring coupling explicitly live.  A coupling is precisely")
    print("      NOT a product of block data, so nothing here touches it.")
    print("    * a NON-TRACIAL functional (the #6399 trilemma).")
    print()
    print("  AND IT SHARPENS WHY.  Every excluded route -- single crossing,")
    print("  stacked powers, projector-composed stacking, higher Hecke rank,")
    print("  spin(x)isospin, separable space factor, and now the off-diagonal --")
    print("  is a SCALAR READ OFF ONE BLOCK.  The identities above show two of")
    print("  those were never independent.  What has never been tried is an")
    print("  interface that is not a single scalar at all.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
