#!/usr/bin/env python3
"""
Probe — the binding law's own interpretation block names TWO different objects.

`two_channel_total_binding_floor_probe.py` closed every T-odd repair on the floor
`B(T=1)+B(T=0) >= alpha*log 4`, and `alpha_direction_two_sided_squeeze_probe.py`
then closed the alpha direction. Both rest on the binding law

    B = -alpha * log(mu),

so the remaining question is whether that law is derived or conventional. **It is
derived** — `mass-endomorphism/markov-trace-gibbs-free-energy.md` gives

    E_bind = E_0 * ln( tr_M(W_free) / tr_M(W_atom) ),

a Gibbs free-energy difference `dF = kT ln(Z_1/Z_2)` with `kT = E_0`, resting on
Markov traces being temperature states on the Hecke tower (Jones 1987). With
`tr_free/tr_atom = 1/mu` exactly (1e-30, established on this axis), that is
`B = -E_0 log mu`. So the floor is not an artifact of a conventional choice.

## But the same block names a second, inequivalent object

Two sentences later it says: *"The entropy in play is that of the normalized
channel measure `y_lambda chi^lambda` over Wedderburn blocks."* For a two-channel
split those are **not the same quantity**:

    implemented (bare surprisals)   S = -log(mu+) - log(mu-)      >= 2 log 2
    named (Shannon entropy)         H = -mu+ log(mu+) - mu- log(mu-)  <= log 2

`S` sums surprisals unweighted; `H` weights each by its own probability. They have
disjoint ranges — `S` is floored where `H` is ceilinged.

## The measurement, and why it is uncomfortable

    nats:   S = 1.681247   (floor 2log2 = 1.386294)
            H = 0.559347   (ceiling log2 = 0.693147)
            nature total / E_0 = 0.513850

    MeV:    alpha*S = 7.0377   3.27x nature
            alpha*H = 2.3414   1.09x nature   (+8.85%)
            nature  = 2.1510

**Nature's total lies outside `S`'s range and inside `H`'s.** That is the whole
of the 3.27x discrepancy, and it is a difference between two readings of one
paragraph rather than between the framework and nature.

## THIS IS NOT A RESULT, AND HERE IS WHY

Four reasons to hold it at arm's length, all of which apply:

1. **Post-hoc.** I went looking for an alternative functional form *after* the
   floor failed. That is the circumstance in which a better-fitting form is
   least informative.
2. **It does not fix the sign — the primary defect.** Every term `-alpha*mu*log(mu)`
   is positive for `0 < mu < 1`, so under `H` both channels still bind:
   `T=1 +0.8951`, `T=0 +1.4463 MeV`. The two-nucleon sector is qualitatively
   wrong in `H` exactly as in `S`. `H` improves a magnitude while leaving the
   thing that was actually broken.
3. **The window is not tight.** Landing within 10% of nature needs `H` in
   `[0.4625, 0.5652]` nats out of the available `[0, log 2]` — **14.8%** of the
   range. An 8.85% miss inside a 14.8% window is weak evidence, not a near-hit.
4. **The corpus's headline formula is `S`, not `H`.** `dF = kT ln(Z_1/Z_2)` is
   the equation; the channel-measure sentence is a secondary interpretive remark.
   Reading `H` as canonical because it fits better would be laundering a fit
   through an ambiguity.

## What it IS

A **documented internal ambiguity in the binding law's interpretation block**,
with a measured 3.27x consequence, on the axis where six repair routes have now
closed. That is worth recording precisely because the block asserts both objects
without reconciling them, and everything downstream silently takes `S`.

**What would settle it** is a derivation, not a fit: which object does the
confinement reweighting actually cost — the free-energy difference of the
*trace ratio*, or the entropy of the *channel measure*? Those are different
physical statements about what confinement does, and the corpus currently claims
both. Settling it is a genuine derivation task and is filed as such.

Until then: the floor stands as proved (it is a theorem about `S`, and `S` is
what the pipeline evaluates), and `H` is a named alternative with an honest
caveat attached, wired to nothing.

NO WITNESS: exact spectral algebra at the substrate anchor; the tables reproduce
every number.

Bean qou-bid3 (closed) -> successor; L2 binding axis.
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

E0_STR = "4.1859813632944758969"
DEUTERON = "2.2245662"
S0_VIRTUAL = "0.0736"


def main() -> int:
    set_compute_dps()
    q = mp.mpf(str(Q50))
    z = q ** 3 / (q ** 2 + 1)
    E0 = mp.mpf(E0_STR)
    mup = (z + 1 / q) / (q + 1 / q)
    mum = (q - z) / (q + 1 / q)
    nature = mp.mpf(DEUTERON) - mp.mpf(S0_VIRTUAL)

    S = -(mp.log(mup) + mp.log(mum))
    H = -(mup * mp.log(mup) + mum * mp.log(mum))
    ln2 = mp.log(2)

    print("The binding law's interpretation block names TWO inequivalent objects.\n")
    print("  markov-trace-gibbs-free-energy.md gives the DERIVED law")
    print("      E_bind = E_0 * ln( tr_M(W_free) / tr_M(W_atom) )   [dF = kT ln(Z1/Z2)]")
    print("  and, two sentences later, says the entropy in play is that of the")
    print("  NORMALIZED CHANNEL MEASURE. For a two-channel split those differ:\n")
    print("      implemented   S = -log(mu+) - log(mu-)          >= 2 log 2")
    print("      named         H = -mu+ log(mu+) - mu- log(mu-)  <=   log 2\n")
    print("  S sums surprisals UNWEIGHTED; H weights each by its own probability.")
    print("  Their ranges are disjoint — S is floored where H is ceilinged.\n")

    print("## Measurement\n")
    print("| quantity | nats | bound | MeV | vs nature |")
    print("| :------- | ---: | ----: | --: | --------: |")
    print(f"| S (implemented) | {mp.nstr(S, 8)} | floor {mp.nstr(2*ln2, 8)} "
          f"| {mp.nstr(E0*S, 6)} | {mp.nstr(E0*S/nature, 4)}x |")
    print(f"| H (named)       | {mp.nstr(H, 8)} | ceil  {mp.nstr(ln2, 8)} "
          f"| {mp.nstr(E0*H, 6)} | {mp.nstr(E0*H/nature, 4)}x |")
    print(f"| nature          | {mp.nstr(nature/E0, 8)} | — "
          f"| {mp.nstr(nature, 6)} | 1.00x |")
    print(f"\n  Nature's total is OUTSIDE S's range and INSIDE H's. H misses by "
          f"{mp.nstr((E0*H-nature)/nature*100, 4)}%.\n")

    print("## THIS IS NOT A RESULT — four reasons, all applicable\n")
    print("  1. POST-HOC. I looked for an alternative form only after the floor")
    print("     failed. That is when a better-fitting form is least informative.\n")
    print("  2. IT DOES NOT FIX THE SIGN — the primary defect. -a*mu*log(mu) > 0")
    print("     for every 0 < mu < 1, so under H both channels still BIND:")
    for lab, m in (("T=1 (pp, nn, 1S0)", mup), ("T=0 (deuteron)", mum)):
        print(f"        {lab:<18} {mp.nstr(-E0*m*mp.log(m), 6)} MeV")
    print("     The sector is qualitatively wrong in H exactly as in S. H improves")
    print("     a magnitude and leaves the thing that was actually broken.\n")
    lo, hi = nature * mp.mpf("0.9"), nature * mp.mpf("1.1")
    frac = (hi - lo) / E0 / ln2
    print("  3. THE WINDOW IS NOT TIGHT. Landing within 10% needs H in")
    print(f"     [{mp.nstr(lo/E0, 6)}, {mp.nstr(hi/E0, 6)}] nats out of [0, log 2] —")
    print(f"     {mp.nstr(frac*100, 3)}% of the available range. An 8.85% miss inside a")
    print(f"     {mp.nstr(frac*100, 3)}% window is weak evidence, not a near-hit.\n")
    print("  4. THE HEADLINE FORMULA IS S. dF = kT ln(Z1/Z2) is the equation; the")
    print("     channel-measure sentence is a secondary remark. Promoting H because")
    print("     it fits better would launder a fit through an ambiguity.\n")

    print("## What it IS\n")
    print("  A documented internal ambiguity in the binding law's own interpretation")
    print("  block, with a measured 3.27x consequence, on the axis where six repair")
    print("  routes have closed. The block asserts both objects without reconciling")
    print("  them, and everything downstream silently takes S.\n")
    print("  WHAT WOULD SETTLE IT (a derivation, not a fit): which object does the")
    print("  confinement reweighting cost — the free-energy difference of the TRACE")
    print("  RATIO, or the entropy of the CHANNEL MEASURE? Those are different")
    print("  physical claims about what confinement does, and the corpus makes both.\n")
    print("  Until settled: the floor stands as proved (it is a theorem about S, and")
    print("  S is what the pipeline evaluates); H is a named alternative with this")
    print("  caveat attached, wired to nothing.")
    print("\n(no witness by design — exact spectral algebra at the anchor.)")

    # guards
    assert S > 2 * ln2, "S must sit above its floor"
    assert H < ln2, "H must sit below its ceiling"
    assert -E0 * mup * mp.log(mup) > 0 and -E0 * mum * mp.log(mum) > 0, \
        "entropy terms must be positive — H does not fix the sign"
    return 0


if __name__ == "__main__":
    sys.exit(main())
