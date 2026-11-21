#!/usr/bin/env python3
"""
Probe — the two-nucleon TOTAL binding is framing-invariant, and it is floored.

`ribbon_twist_t_selective_probe.py` left the ribbon-twist route open with an
honesty flag: the twist is T-odd so it CAN express the required sign structure,
`f >= 3` reproduces the signs, but `f = 3` is a threshold rather than a
derivation and adopting it would be a fit.
`framing_derivation_attempt_probe.py` then tried three writhe-derived framings
and none reached the threshold.

This probe closes the route WITHOUT deriving `f`, because the framing turns out
not to matter.

## 1. The framing cancels

A T-odd rescaling by `t > 0` sends `(mu+, mu-) -> (mu+ * t, mu- / t)`; the
ribbon twist is `t = q^f`. With `B_T = -alpha * log(mu_T)`,

    B(T=1) + B(T=0) = -alpha * log(mu+ * t) - alpha * log(mu- / t)
                    = -alpha * log(mu+ * mu-)

— the `log t` terms enter with opposite signs and cancel identically. The TOTAL
is a framing invariant. Verified below at `f = 0, 3, 10, -8.297` (that last is
the framing that would reproduce the deuteron on its own): all four agree to 30
digits.

## 2. The total is floored, over every convex pair

`mu+ + mu- = 1` is an exact identity of the projector decomposition (already in
the corpus: `InterfaceScalar.mu_sum_eq_one`, and re-verified here to 30 digits),
so AM-GM caps `mu+ * mu- <= 1/4` and

    B(T=1) + B(T=0) >= alpha * log 4.

This holds for EVERY convex pair, not just the substrate's — no `z`, no
convention, no interface offset, no crossing assignment can go below it.

## 3. The numbers

    floor        alpha * log 4               = 5.8030 MeV
    substrate    -alpha * log(mu+ mu-)       = 7.0377 MeV   (mu+ mu- = 0.186142)
    nature       B(3S1) + B(1S0)             = 2.1510 MeV

The substrate over-binds the two-nucleon total by 3.27x; the FLOOR over-binds it
by 2.70x whatever the projector scalars are. Satisfying the floor at all needs
`alpha <= 2.1510 / log 4 = 1.5516 MeV` against the framework's `E_0 = 4.1860`.

The `1S0` entry is the virtual-state energy `hbar^2/(m_N a^2) = 41.47/23.74^2 =
0.0736 MeV`, negative because unbound. The conclusion barely depends on it: even
setting the `T=1` binding to exactly zero, nature's total is 2.2246 and the floor
still over-binds by 2.61x.

## Scope

**Scope-(b), a proved exclusion** (`QOU/QBeta/TwoChannelTotalBindingFloor.lean`,
sorry-free): no T-odd rescaling of the two isospin channels — ribbon twist at any
framing, or any other `(mu+, mu-) -> (mu+ t, mu- / t)` — reproduces both
two-nucleon channel energies. It cannot change their sum, and the sum is already
wrong. This SUPERSEDES the `f = 3` honesty flag with something stronger: there is
no `f` to find, so the question of deriving one is moot.

**The sub-normalisation escape is closed too, in the OPPOSITE direction.** The
intuitive repair — "the two channels carry only a fraction `s < 1` of the trace
because the colour-only fibre lacks a spin/spatial factor, so the floor drops" —
is backwards: the cap `mu+ mu- <= s^2/4` shrinks with `s`, so a smaller
normalisation binds HARDER. Reaching nature's total forces `s >= 1.5469 > 1`,
which a projector decomposition of a normalised trace cannot supply. More
channels is also the wrong way: for `k` channels the floor is `alpha*k*log k`,
rising with `k`.

**Scope-(a), what genuinely survives.** The floor needs (i) a two-element
decomposition with `mu+ + mu- <= 1` and (ii) one channel-independent `alpha`. The
surviving direction is `alpha`: satisfying the floor needs `alpha <= 1.5516 MeV`
against `E_0 = 4.1860`. So the open question is not whether the colour-only fibre
can host `3S1`/`1S0` — it is that the energy scale attached to the interface is
~2.7x too large. Also untouched: a channel-dependent scale, a binding law other
than `-alpha log mu`, or two-nucleon states that are not spectral projections of
this trace.

NO WITNESS: exact spectral algebra at the substrate anchor plus one AM-GM bound;
the tables reproduce every number.

Bean qou-brg3; L2 binding axis.
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
from mpmath import nstr as _ame_nstr  # noqa: E402  (AME registry, string form)

E0_STR = "4.1859813632944758969"
DEUTERON = _ame_nstr(AME_B_DEUTERON_MEV_VALIDATION, 30)      # 3S1, MeV, bound
S0_VIRTUAL = "0.0736"       # 1S0 virtual-state energy hbar^2/(m_N a^2), MeV, UNbound


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q50))
    z = q ** 3 / (q ** 2 + 1)
    E0 = mp.mpf(E0_STR)
    mup = (z + 1 / q) / (q + 1 / q)      # T = 1, symmetric
    mum = (q - z) / (q + 1 / q)          # T = 0, antisymmetric
    D = mp.mpf(DEUTERON)
    V = mp.mpf(S0_VIRTUAL)
    nature = D - V

    print("The two-nucleon TOTAL binding: framing-invariant, and floored.\n")
    print(f"  q0    = {mp.nstr(q, 12)}    alpha = E_0 = {mp.nstr(E0, 8)} MeV")
    print(f"  mu+   = {mp.nstr(mup, 12)}   (T=1, symmetric)")
    print(f"  mu-   = {mp.nstr(mum, 12)}   (T=0, antisymmetric)")
    print(f"  mu+ + mu- = {mp.nstr(mup + mum, 30)}   <- EXACTLY 1, identically in q,z")
    print(f"  mu+ * mu- = {mp.nstr(mup * mum, 12)}\n")

    # ---- 1. the framing cancels ------------------------------------------
    print("1. THE FRAMING CANCELS — B(T=1)+B(T=0) is a T-odd invariant\n")
    print("   (mu+, mu-) -> (mu+ t, mu- / t)  gives  -a log(mu+ t) - a log(mu- / t)")
    print("                                        = -a log(mu+ mu-)   [log t cancels]\n")
    f_deut = -mp.log(mp.exp(-D / E0) / mum) / mp.log(q)
    print("   |          f | B(T=1)      | B(T=0)      | TOTAL                          |")
    print("   | ---------: | ----------: | ----------: | :----------------------------- |")
    totals = []
    for lab, f in (("0", mp.mpf(0)), ("3", mp.mpf(3)), ("10", mp.mpf(10)),
                   (f"{mp.nstr(f_deut, 5)}", f_deut)):
        e1 = mup * q ** f
        e0 = mum * q ** (-f)
        b1 = -E0 * mp.log(e1)
        b0 = -E0 * mp.log(e0)
        totals.append(b1 + b0)
        print(f"   | {lab:>10} | {mp.nstr(b1, 6)} | {mp.nstr(b0, 6)} "
              f"| {mp.nstr(b1 + b0, 22):<30} |")
    spread = max(totals) - min(totals)
    print(f"\n   spread across all four framings: {mp.nstr(spread, 6)}  -> invariant")
    print(f"   (the last row is the f that reproduces the deuteron ALONE: "
          f"{mp.nstr(f_deut, 5)},")
    print("    on the wrong side of the f > 2.7227 unbinding threshold by 11 units)\n")

    # ---- 2. the floor ------------------------------------------------------
    print("2. THE FLOOR — mu+ + mu- = 1 caps the product at 1/4 (AM-GM)\n")
    floor = E0 * mp.log(4)
    subst = -E0 * mp.log(mup * mum)
    print(f"   floor      alpha * log 4         = {mp.nstr(floor, 6)} MeV"
          "   (any convex pair)")
    print(f"   substrate  -alpha * log(mu+ mu-) = {mp.nstr(subst, 6)} MeV"
          f"   (mu+ mu- = {mp.nstr(mup*mum, 8)})")
    print(f"   nature     B(3S1) + B(1S0)       = {mp.nstr(nature, 6)} MeV"
          f"   ({mp.nstr(D, 6)} {mp.nstr(-V, 6)})\n")
    print(f"   substrate over-binds by {mp.nstr(subst / nature, 4)}x")
    print(f"   the FLOOR over-binds by {mp.nstr(floor / nature, 4)}x "
          "— whatever the projector scalars are")
    print(f"   satisfying the floor needs alpha <= {mp.nstr(nature / mp.log(4), 6)} MeV"
          f"  (framework has {mp.nstr(E0, 6)})\n")
    print("   robustness: even taking B(T=1) = 0 exactly, nature's total is "
          f"{mp.nstr(D, 6)}")
    print(f"   and the floor still over-binds by {mp.nstr(floor / D, 4)}x. The"
          " conclusion does not")
    print("   rest on the virtual-state number.\n")

    # ---- 3. the obvious escape, and why it points the wrong way -----------
    print("3. THE SUB-NORMALISATION ESCAPE IS CLOSED — in the OPPOSITE direction\n")
    s_req = 2 * mp.sqrt(mp.exp(-nature / E0))
    print("   The intuitive repair: 'the two isospin channels carry only a fraction")
    print("   s < 1 of the trace (the colour-only fibre lacks a spin/spatial factor),")
    print("   so the floor drops.' IT DOES NOT DROP — IT RISES.\n")
    print("   Under mu+ + mu- = s the cap is mu+ mu- <= s^2/4, which SHRINKS with s,")
    print("   so a smaller normalisation makes the product smaller and the binding")
    print("   LARGER. Reaching nature's total needs\n")
    print(f"       s >= 2*exp(-total/(2*alpha)) = {mp.nstr(s_req, 6)}   > 1\n")
    print("   and a projector decomposition of a single normalised trace cannot")
    print("   exceed 1. Tabulated:\n")
    print("   |    s | max mu+ mu- = s^2/4 | floor = -a log(s^2/4) | vs nature |")
    print("   | ---: | ------------------: | --------------------: | --------: |")
    for s in (mp.mpf("0.5"), mp.mpf("0.75"), mp.mpf(1), s_req):
        cap = s ** 2 / 4
        fl = -E0 * mp.log(cap)
        print(f"   | {mp.nstr(s, 4)} | {mp.nstr(cap, 8)} | {mp.nstr(fl, 6)} "
              f"| {mp.nstr(fl / nature, 4)}x |")
    print("\n   More channels does not help either: for k channels sharing the unit")
    print("   normalisation the cap is prod <= k^-k and the floor is a*k*log k,")
    print("   which RISES with k (k=2: 5.803, k=3: 13.80, k=4: 23.21 MeV).")
    print("\n   So the surviving direction is ALPHA, not the interface. The issue is")
    print("   not that the colour-only fibre is too small to host 3S1/1S0 — it is")
    print("   that the energy scale attached to the interface is ~2.7x too large.")
    print("   Proved: reaching_target_forces_over_unit_sum.\n")

    print("## Scope\n")
    print("   SCOPE-(b), proved (TwoChannelTotalBindingFloor.lean, sorry-free):")
    print("   no T-odd rescaling reproduces both channel energies. This SUPERSEDES")
    print("   the 'f = 3 is a fit' flag with something stronger — there is no f to")
    print("   find, so deriving one is moot. The ribbon-twist route is closed.")
    print("\n   SCOPE-(a), what survives: the ALPHA direction. A channel-dependent or")
    print("   non-E_0 scale, a binding law other than -alpha log mu, or two-nucleon")
    print("   states that are not spectral projections of this trace.")
    print("\n(no witness by design — exact spectral algebra + one AM-GM bound.)")

    # guard: the identity the whole argument rests on
    assert abs(mup + mum - 1) < mp.mpf("1e-45"), "mu+ + mu- != 1"
    assert spread < mp.mpf("1e-40"), "total is not framing-invariant"
    assert subst >= floor, "substrate below the AM-GM floor"
    return 0


if __name__ == "__main__":
    sys.exit(main())
