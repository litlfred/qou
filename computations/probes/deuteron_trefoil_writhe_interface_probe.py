#!/usr/bin/env python3
"""
deuteron_trefoil_writhe_interface_probe — the deuteron knot that Owner Ruling A
already fixed (the trefoil, sigma^3) gives a binding 9.45x closer to AME than
production's single crossing, at -2.89 % instead of +27.36 %. It is NOT a
solution and the look-elsewhere cost is ~12 %, both stated below.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## What connects two things the corpus already holds separately

**(i)** Owner Ruling A, 2026-08-29
(`docs/audits/2026-08-29-deuteron-knot-owner-decision.md`): *"the deuteron knot
is the canonical braid closure (trefoil / Hopf, Vol = 0)"*, whose own table
labels the trefoil `T(2,3)` the **canonical-for-Delta_lambda** route and the
Hopf `L2a1` the **linear-chain** route. That ruling was about the **volume**
(it proved the Bloch-volume leg is 0); it says nothing about binding magnitude.

**(ii)** `stacked_interface_writhe_normalised_probe.py` already tabulates the
writhe-normalised interface scalar `mu_eff = mu * (1-h)^(e/2)` for `sigma^m`,
`m = -8 .. +8`. Its own conclusion discusses only the UNBOUND channels
(`sigma^-2` at -0.613 MeV, 6-9x nature's) and never reads off the bound side.

Nobody had put (i) into (ii). `T(2,3)` is the closure of `sigma^3` in `B_2`, so
the ruling fixes `m = 3` -- and the `m = 3` row was sitting in that table.

## The measurement

    word            e     mu_eff        B (MeV)      vs AME 2.224566
    sigma^1         1     0.5448928     2.5415862     +14.25 %
    sigma^2  Hopf   2     0.8922502     0.4772384     -78.55 %
    sigma^3  tref   3     0.5968711     2.1601931      -2.89 %

    production (single crossing, `_bond_type_L`)  2.8331626    +27.36 %

    |error_production| / |error_trefoil| = 9.454

So the knot the owner already ruled for gives the deuteron to **-2.89 %**, where
the production single-crossing bond is **+27.36 %** out.

**The Hopf leg is the reason this is not simply a curve-fit.** The ruling names
two closures; only the one its own table calls canonical works. `sigma^2` (Hopf)
lands at **-78.5 %**. A fit would have taken whichever matched.

## 🛑 Three reasons this is SUGGESTIVE and not a result

1. **The look-elsewhere cost is ~12 %, computed below, not hand-waved.** The
   table offers 11 positive `B_eff` values spread over ~0.48 .. 12.2 MeV, so the
   typical gap near 2.2 MeV is ~10 %. A 2.89 % hit is ~3x better than that
   spacing -- mildly lucky, not compelling. Under a uniform look-elsewhere over
   the tabulated candidates the probability of landing this close by chance is
   ~0.12. **That is not a small number and it is the honest headline caveat.**
2. **`mu_eff` is a property of the braid WORD, not of the link** -- the source
   probe says so itself, and it would change under Markov move II. `T(2,3)` as
   `sigma^3` in `B_2` has `e = 3`; the same knot in `B_3` does not. So the result
   is conditional on the canonical presentation being the `B_2` one. The ruling
   says "canonical braid closure", which for `T(2,3)` is standard -- but this is
   a real dependency, not a formality.
3. **It fixes ONE leg and leaves the sector's actual failure untouched.** The
   two-nucleon sector's headline defect is a SIGN error: the framework binds the
   diproton (+2.5416) and the dineutron (+3.3069) where nature has no bound
   state (`qou-0pzi`), and `QOU.QBeta.single_crossing_binds` proves sorry-free
   that NO single crossing at any admissible `d` can unbind while `q^3 < q^2+1`.
   Nothing here touches that. A trefoil assignment for `pp`/`nn` would bind them
   too.

## What this is NOT

  * NOT a closure of the deuteron leg. -2.89 % is roughly four orders of
    magnitude from the L2 100x target on this observable.
  * NOT a proposal to rewire `_bond_type_L`. Nothing is wired.
  * NOT a claim that `m = 3` is derived. It is *ruled* (Owner Ruling A) and
    therefore not chosen against this data -- which is weaker than derived and
    stronger than fitted.
  * NOT an argument that the writhe normalisation is correct. It is the one the
    source probe applies, carried over unchanged so the comparison is like-for-
    like.

Scope **(a)**: a measurement joining two existing corpus facts. AME is the
comparison target only, never inverted into a weight.

NO FLOAT64: mpmath `mpf` at 50 dps, 50-digit proton pin, exact integer recursion
for the Hecke powers.
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

AME_DEUTERON = AME_B_DEUTERON_MEV_VALIDATION   # AME2020, MeV


def fmt(x, n=10):
    return mp.nstr(x, n)


def hecke_power(m: int, h):
    """T^m = c*T + d in H_2(q) with T^2 = h*T + 1.  Exact recursion, no float."""
    if m == 0:
        return mp.mpf(0), mp.mpf(1)
    if m > 0:
        c, d = mp.mpf(1), mp.mpf(0)                      # T^1
        for _ in range(m - 1):
            c, d = c * h + d, c                          # (cT+d)*T
        return c, d
    # T^-1 = T - h  (from T^2 = hT + 1)
    bc, bd = mp.mpf(1), -h
    c, d = bc, bd
    for _ in range(-m - 1):
        c, d = c * bc * h + c * bd + d * bc, c * bc + d * bd
    return c, d


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q0 = Q_MP
    h = q0 - 1 / q0
    z = q0**3 / (q0**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    al = _qbeta_e0.order_zero_scaled(me, q0)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)

    def mu_raw(m):
        c, d = hecke_power(m, h)
        return z * c + d

    def b_eff(m):
        mu = mu_raw(m) * (1 - h) ** (mp.mpf(m) / 2)
        return (-al * mp.log(mu)) if mu > 0 else None

    print("deuteron_trefoil_writhe_interface_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 17)}   h = {fmt(h)}   z = {fmt(z)}")
    print(f"alpha = m_e/(q0(q0-1)) = {fmt(al)} MeV     AME(2H) = {AME_DEUTERON}")
    print()
    print("THE TWO CORPUS FACTS BEING JOINED")
    print("-" * 78)
    print("  (i)  Owner Ruling A (2026-08-29): the deuteron knot IS the canonical")
    print("       braid closure, trefoil T(2,3).  That ruling was about VOLUME")
    print("       (Bloch leg proved 0); it says nothing about binding magnitude.")
    print("  (ii) stacked_interface_writhe_normalised_probe tabulates")
    print("       mu_eff = mu*(1-h)^(e/2) for sigma^m -- and its conclusion reads")
    print("       only the UNBOUND rows, never the bound side.")
    print("  T(2,3) is the closure of sigma^3 in B_2, so (i) fixes m = 3.")
    print()

    print(f"{'word':>14} {'e':>3} {'mu_eff':>15} {'B (MeV)':>15} {'vs AME':>12}")
    rows = {}
    for m, label in ((1, "sigma"), (2, "sigma^2 Hopf"), (3, "sigma^3 tref")):
        B = b_eff(m)
        rows[m] = B
        print(f"{label:>14} {m:>3} "
              f"{fmt(mu_raw(m) * (1 - h)**(mp.mpf(m)/2), 9):>15} "
              f"{fmt(B, 10):>15} {fmt((B / AME_DEUTERON - 1) * 100, 5) + ' %':>12}")

    dlt = flavor_split_leading(q0)
    e_pn = 2 * (mp.mpf(1) / 2 - dlt / 4) - 1   # production de['pn'] = -delta/2
    B_prod = al * (-mp.log(z - h * (mp.mpf(1) / 2 - dlt / 4))
                   - e_pn / 2 * mp.log(1 - h))
    e_prod = (B_prod / AME_DEUTERON - 1) * 100
    e_tref = (rows[3] / AME_DEUTERON - 1) * 100
    print(f"{'production':>14} {'--':>3} {'--':>15} {fmt(B_prod, 10):>15} "
          f"{fmt(e_prod, 5) + ' %':>12}")
    print()
    ratio = abs(e_prod) / abs(e_tref)
    print(f"  |error_production| / |error_trefoil| = {fmt(ratio, 6)}")
    assert ratio > 9, "the trefoil row must beat production by ~9x"
    assert abs(e_tref) < 3, "trefoil must land inside 3 %"
    print()
    print("  The Hopf leg is why this is not simply a curve-fit: the ruling names")
    print("  TWO closures and only the one its own table calls canonical works.")
    print(f"  sigma^2 (Hopf) lands at {fmt((rows[2]/AME_DEUTERON - 1)*100, 5)} %.")
    print("  A fit would have taken whichever matched.")
    assert rows[2] / AME_DEUTERON - 1 < mp.mpf("-0.5"), "Hopf must be far off"
    print()

    print("LOOK-ELSEWHERE COST — computed, not hand-waved")
    print("-" * 78)
    cands = [b_eff(m) for m in list(range(1, 9)) + list(range(-1, -9, -1))]
    pos = sorted(b for b in cands if b is not None and b > 0)
    lo, hi = pos[0], pos[-1]
    tol = abs(e_tref) / 100
    win = 2 * tol * AME_DEUTERON
    p = len(pos) * win / (hi - lo)
    print(f"  positive B candidates in the table: {len(pos)}")
    print(f"  spread: {fmt(lo, 6)} .. {fmt(hi, 6)} MeV")
    print(f"  window for a {fmt(abs(e_tref), 4)} % hit: +-{fmt(tol*AME_DEUTERON, 5)}"
          f" MeV, width {fmt(win, 5)}")
    print(f"  crude uniform look-elsewhere probability p ~ {fmt(p, 4)}")
    n_in = sum(1 for b in pos if abs(b / AME_DEUTERON - 1) <= tol)
    print(f"  candidates actually within that window: {n_in}")
    assert n_in == 1, "exactly one candidate should sit in the window"
    print()
    print(f"  p ~ {fmt(p, 3)} IS NOT A SMALL NUMBER.  Roughly one chance in eight")
    print("  of landing this close by accident.  That is the honest headline")
    print("  caveat and it is why this is reported as SUGGESTIVE, not as a result.")
    print()

    print("WHAT IT DOES NOT TOUCH — the sector's actual failure")
    print("-" * 78)
    print("  The two-nucleon defect is a SIGN error, not a magnitude one:")
    print("  the framework binds the diproton (+2.5416) and dineutron (+3.3069)")
    print("  where nature has NO bound state (bean qou-0pzi), and")
    print("  QOU.QBeta.single_crossing_binds proves sorry-free that no single")
    print("  crossing at any admissible d can unbind while q^3 < q^2 + 1.")
    print("  Nothing here touches that.  A trefoil word for pp/nn would bind")
    print("  them too -- this improves ONE leg of three.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT a closure.  -2.89 % is ~4 orders from the L2 100x target.")
    print("  * NOT a rewiring of _bond_type_L.  Nothing is wired.")
    print("  * NOT that m = 3 is DERIVED.  It is RULED, hence not chosen against")
    print("    this data -- weaker than derived, stronger than fitted.")
    print("  * NOT that the writhe normalisation is correct; it is carried over")
    print("    unchanged from the source probe so the comparison is like-for-like.")
    print("  * mu_eff is a braid-WORD property, not a link invariant.  This is")
    print("    conditional on the canonical presentation being sigma^3 in B_2.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
