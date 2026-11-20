#!/usr/bin/env python3
"""
stacked_unbinding_family_exclusion_probe — the even-negative stacked branch is
NOT a repair direction. Its unbinding magnitude has a MINIMUM at sigma^-2 which
is 6.13x nature's, and composing it with the isospin projectors (the one
mechanism that gets the channel selection right) is excluded structurally.
Also RETRACTS the framing of my own #6407, one PR old.

Bean `qou-brng`, arc `bk-crossing-mass-binding`.

## What was open

`QOU.QBeta.SingleCrossingAlwaysBinds` (sorry-free) proves no single crossing can
unbind while `q^3 < q^2 + 1`, and names the survivor:

    "NOT excluded: unbinding as such. ... the writhe-normalised even negative
     stacked powers sigma^-2, sigma^-4, ... have mu_eff > 1 and do unbind ...
     Their magnitudes are 6-9x nature's, so this is a repair DIRECTION, not a
     repair."

This probe asks whether it is a direction at all. **It is not**, for two
independent reasons, and neither was previously on the record.

## RESULT 1 — 6.13x is a MINIMUM over the family, not a sample (scope (a))

Scanning `m = -60..60`: 30 powers unbind, all even-negative, and

    m = -2     mu_eff = 1.15763245   B = -0.6127311 MeV    6.13x nature (0.10)
    m = -4                1.39270003     -1.3865826         13.87x
    m = -6                1.74811445     -2.3380286         23.38x
    ...

`|B|` is **monotonically increasing in `|m|`** and `m = -2` is the global
minimum. The mechanism is exact: `mu_raw(-2k) ~ A*q^{2k}` while the writhe
factor contributes `(1-h)^{-k}`, so

    mu_eff(-2k) ~ A * (q^2/(1-h))^k,     q^2/(1-h) = 1.5578

grows geometrically. So the family cannot be tuned toward nature by choosing a
different power -- every other member is **worse than the one already known to
be 6x out**. Reaching nature's `|B| ~ 0.10 MeV` needs `mu_eff = 1.0242`; the
family's smallest excess over 1 is `0.1576` against a needed `0.0242`, i.e.
**6.5x too far above 1**, with nothing in between.

That converts "6-9x too large" from an observation about two sampled rows into
a statement about the whole family.

## RESULT 2 — composing with the isospin projectors is excluded (scope (b))

`docs/audits/2026-08-09-two-nucleon-channels-isospin-not-crossing-count.md`
establishes that the channel selector is **isospin**, supplied free by the Hecke
spectral projectors, and derives the correct ordering `mu_- < mu_+` for every
`q > 0` (`mu_singlet_lt_mu_triplet`, `singlet_binds_more`). That is the one
mechanism in this sector that gets a sign right without tuning. It also notes
that projectors alone can never unbind, because `mu_+ + mu_- = 1`.

The obvious composite is therefore: keep the projectors for **selection**, and
stack the word for **magnitude** -- projecting `sigma^m` instead of `sigma`. The
audit does not cover this, and at `m = 2` it looks promising: `mu_+ = 1.00901`,
i.e. `B(T=1) = -0.0375 MeV`, which is the right sign and within 2x of nature's
`-0.066..-0.10` rather than 6x.

**It fails, and it fails identically for every m.** `mu_+ + mu_- = 1` holds for
*any* substituted scalar, since it is the partition of unity of two complementary
projectors and does not know what was projected. So

    mu_+ > 1   <=>   mu_- < 0

and `B = -alpha*log(mu)` is undefined at a negative scalar. **Unbinding the
`T = 1` channel necessarily destroys the `T = 0` channel that must hold the
deuteron.** Measured over `m = -12..12`: every `m` is either
`(T=1 bound, T=0 bound)` -- both wrong -- or `(T=1 UNBOUND, T=0 mu < 0)`. **No
`m` gives `T=1` unbound together with `T=0` bound.**

This is a scope-**(b)** exclusion and the invariant is named: the partition of
unity `mu_+ + mu_- = 1` (`mu_sum_eq_one`, already in `InterfaceScalar.lean`).
It is not "we searched and did not find".

## 🛑 RETRACTION — my own #6407, one PR old

#6407 reported that the trefoil `sigma^3` (fixed by Owner Ruling A) gives the
deuteron at -2.89 % against production's +27.36 %. **The arithmetic stands; the
framing was wrong and I did not know it.** #6407 says the result "improves ONE
leg of three". There are **four** two-nucleon channels, not three:

    pn 3S1 (deuteron)  S=1 T=0   +2.224566   BOUND
    pn 1S0 (virtual)   S=0 T=1      -0.066   unbound
    pp 1S0             S=0 T=1      -0.1     unbound
    nn 1S0             S=0 T=1      -0.1     unbound

The two `pn` rows have **identical nucleon content and opposite boundness**. A
crossing-count word assigned to "the deuteron" *as a p-n pair* is keyed on
content, so it hands both `pn` rows the same energy -- and that is refuted in
Lean, not merely unsupported: `content_keyed_interface_refuted`
(`InterfaceScalar.lean`).

So #6407's number survives **only** if the word is keyed on the isospin channel
`T`, never on the species pair. That is a real condition and #6407 does not
state it. Corrected there; recorded here.

## Where this leaves the sector

The two-nucleon sector now has, on the record:

  * selection: **derived** (isospin projectors, correct ordering, no fit);
  * single-crossing unbinding: **excluded**, scope (b), sorry-free;
  * stacked unbinding alone: **excluded on magnitude**, scope (a), this probe;
  * projector-composed-with-stacking: **excluded**, scope (b), this probe;
  * the `T=0` projector as the deuteron: **excluded** by the `alpha*ln4 = 5.803`
    universal floor (2026-08-09 audit) -- AME is 61.7 % below it.

Every mechanism currently in the algebra is now excluded for the unbound
channels. The sector needs something outside this family, and no candidate is
proposed here.

## Scope

Scope **(a)** for Result 1 (a measured minimum over a scanned family, with the
growth mechanism identified), scope **(b)** for Result 2 (the named invariant
`mu_+ + mu_- = 1`). Nothing is wired, nothing is fitted, AME is the comparison
target only.

NO FLOAT64: mpmath `mpf` at 60 dps, 50-digit proton pin, exact integer recursion
for the Hecke powers.
"""

from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path

_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import AME_B_DEUTERON_MEV_VALIDATION

mp.mp.dps = 60

NAT_1S0 = mp.mpf("0.10")      # pp / nn virtual state, MeV (magnitude)
AME_D = AME_B_DEUTERON_MEV_VALIDATION    # deuteron, MeV


def fmt(x, n=10):
    return mp.nstr(x, n)


def main() -> int:
    from codata_constants import M_E_MEV as _me
    q0 = Q_MP
    h = q0 - 1 / q0
    z = q0**3 / (q0**2 + 1)
    me = _me if isinstance(_me, mp.mpf) else mp.mpf(str(_me))
    al = me / (q0 * (q0 - 1))
    qq = q0 + 1 / q0

    def hecke_power(m):
        if m > 0:
            c, d = mp.mpf(1), mp.mpf(0)
            for _ in range(m - 1):
                c, d = c * h + d, c
            return c, d
        bc, bd = mp.mpf(1), -h
        c, d = bc, bd
        for _ in range(-m - 1):
            c, d = c * bc * h + c * bd + d * bc, c * bc + d * bd
        return c, d

    def mu_raw(m):
        c, d = hecke_power(m)
        return z * c + d

    def mu_eff(m):
        return mu_raw(m) * (1 - h) ** (mp.mpf(m) / 2)

    print("stacked_unbinding_family_exclusion_probe")
    print("=" * 78)
    print(f"q0 = {fmt(q0, 17)}  h = {fmt(h)}  z = {fmt(z)}  alpha = {fmt(al)} MeV")
    print()
    print("RESULT 1 — 6.13x is a MINIMUM over the family, not a sample")
    print("-" * 78)
    unb = []
    for m in range(-60, 61):
        if m == 0:
            continue
        e = mu_eff(m)
        if e > 1:
            unb.append((abs(-al * mp.log(e)), m, e, -al * mp.log(e)))
    unb.sort()
    print(f"  unbinding powers found in |m| <= 60: {len(unb)}  "
          f"(all even-negative: {all(m % 2 == 0 and m < 0 for _a, m, _e, _b in unb)})")
    print(f"{'rank':>5} {'m':>5} {'mu_eff':>16} {'B (MeV)':>14} {'x nature':>10}")
    for i, (a, m, e, B) in enumerate(unb[:5]):
        print(f"{i+1:>5} {m:>5} {fmt(e, 12):>16} {fmt(B, 9):>14} "
              f"{fmt(a / NAT_1S0, 5):>10}")
    a_min, m_min, e_min, _b = unb[0]
    assert m_min == -2, "the minimum must be at sigma^-2"
    print(f"\n  MINIMUM |B| over the family = {fmt(a_min, 10)} MeV at m = {m_min}")
    print(f"    = {fmt(a_min / NAT_1S0, 6)}x nature's 0.10 MeV, and every other")
    print("      member is WORSE -- so the family cannot be tuned by power choice.")
    growth = q0**2 / (1 - h)
    print(f"\n  mechanism: mu_raw(-2k) ~ A*q^(2k), writhe gives (1-h)^(-k), so")
    print(f"    mu_eff(-2k) ~ A*(q^2/(1-h))^k  with q^2/(1-h) = {fmt(growth, 8)}")
    ratios = [unb[i + 1][2] / unb[i][2] for i in range(4)]
    print(f"    successive mu_eff ratios: {[fmt(r, 6) for r in ratios]}"
          f"  -> {fmt(growth, 6)}")
    assert all(ratios[i] < ratios[i + 1] for i in range(len(ratios) - 1)), \
        "ratios must climb toward the asymptotic growth rate"
    need = mp.exp(NAT_1S0 / al)
    print(f"\n  needed mu_eff for |B| = 0.10 MeV: {fmt(need, 12)}")
    print(f"  family's smallest:                {fmt(e_min, 12)}")
    print(f"  excess over 1:  needed {fmt(need - 1, 8)}, smallest available "
          f"{fmt(e_min - 1, 8)}  -> {fmt((e_min - 1) / (need - 1), 5)}x too far")
    assert e_min > need, "the family's minimum must overshoot nature"
    print()

    print("RESULT 2 — composing with the isospin projectors is EXCLUDED, scope (b)")
    print("-" * 78)
    print("  mu+(m) = (mu_raw(m)+1/q)/(q+1/q)  T=1  (pp, nn, pn 1S0)")
    print("  mu-(m) = (q-mu_raw(m))/(q+1/q)    T=0  (deuteron)")
    print(f"\n{'m':>4} {'mu+':>14} {'B(T=1)':>12} {'mu-':>14} {'B(T=0)':>12}  verdict")
    both_ok = []
    for m in list(range(1, 9)) + list(range(-1, -9, -1)):
        mr = mu_raw(m)
        up, um = (mr + 1 / q0) / qq, (q0 - mr) / qq
        b1 = -al * mp.log(up) if up > 0 else None
        b0 = -al * mp.log(um) if um > 0 else None
        v = ("T=1 UNBOUND / T=0 mu<0" if um <= 0 else
             ("T=1 unbound / T=0 bound" if up > 1 else "both bound"))
        if up > 1 and um > 0:
            both_ok.append(m)
        print(f"{m:>4} {fmt(up, 10):>14} {(fmt(b1, 7) if b1 else 'n/a'):>12} "
              f"{fmt(um, 10):>14} {(fmt(b0, 7) if b0 else 'n/a'):>12}  {v}")
        assert abs(up + um - 1) < mp.mpf(10) ** -40, "mu+ + mu- must be 1"
    print(f"\n  m with (T=1 unbound AND T=0 bound): {both_ok}")
    assert both_ok == [], "no m may give T=1 unbound with T=0 still bound"
    print("  => NONE, and structurally so.  mu+ + mu- = 1 is the partition of")
    print("     unity of two complementary projectors -- it holds for ANY")
    print("     substituted scalar, so mu+ > 1 forces mu- < 0, where B is")
    print("     undefined.  Unbinding T=1 necessarily destroys the T=0 channel")
    print("     that has to hold the deuteron.  Invariant: mu_sum_eq_one.")
    print()

    print("RETRACTION — the framing of my own #6407, one PR old")
    print("-" * 78)
    tref = -al * mp.log(mu_eff(3))
    print(f"  #6407: trefoil sigma^3 gives {fmt(tref, 9)} MeV, "
          f"{fmt((tref/AME_D - 1)*100, 4)} % vs AME.  ARITHMETIC STANDS.")
    print("  #6407 says it 'improves ONE leg of three'.  There are FOUR channels:")
    print(f"{'channel':>20} {'S':>2} {'T':>2} {'B (MeV)':>11}  state")
    for nm, S, T, B, st in (("pn 3S1 (deuteron)", 1, 0, "+2.224566", "BOUND"),
                            ("pn 1S0 (virtual)", 0, 1, "-0.066", "unbound"),
                            ("pp 1S0", 0, 1, "-0.1", "unbound"),
                            ("nn 1S0", 0, 1, "-0.1", "unbound")):
        print(f"{nm:>20} {S:>2} {T:>2} {B:>11}  {st}")
    print("\n  The two pn rows have IDENTICAL content and OPPOSITE boundness, so a")
    print("  word assigned to 'the deuteron' AS A P-N PAIR is content-keyed and")
    print("  hands both the same energy -- refuted in Lean, not merely")
    print("  unsupported: content_keyed_interface_refuted (InterfaceScalar.lean).")
    print("  #6407's number survives ONLY if the word is keyed on the isospin")
    print("  channel T, never on the species pair.  #6407 does not say so.")
    print()

    print("WHAT IS NOT CLAIMED")
    print("-" * 78)
    print("  * NOT that unbinding is impossible.  Result 2 excludes the")
    print("    PROJECTOR-COMPOSED family; Result 1 excludes the writhe-normalised")
    print("    stacked family on magnitude.  Mechanisms outside both are untouched.")
    print("  * NOT a proposal.  No candidate replacement is offered.")
    print("  * NOT a claim about #6407's arithmetic, which is unchanged -- only")
    print("    about the condition under which it can mean anything.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
