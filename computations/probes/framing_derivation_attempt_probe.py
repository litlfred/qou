#!/usr/bin/env python3
"""
Probe — attempt to DERIVE the two-nucleon framing f. Honest negative: it fails at nn.

`ribbon_twist_t_selective_probe.py` showed the ribbon twist is T-odd (`theta_lambda
= q^c(lambda)`, `c(lambda') = -c(lambda)`) and so CAN express the required sign
structure, with a threshold `f > 2.7227`, i.e. integer `f >= 3`. It flagged that
`f = 3` is a threshold, not a derivation, and that adopting it because it fits
would be a fit.

This probe tries to derive `f` instead of choosing it. The natural source is the
framing of the braid itself: in a ribbon category the canonical (blackboard)
framing of a braid closure IS its writhe, so `f = w` is the choice with no
freedom in it.

## The framework's own writhes

Exponent sums of `atom_braid_word_3A`, counting each crossing template
`sigma + d` as `e = 1 + 2d/h` (the same interpolation `_bond_type_L` uses for
`de_pn`, so `d=0 -> +1` and `d=-h -> -1`):

    p     +3.000000        pp   +7.000000
    n     +1.000000        pn   +4.000688
                           nn   +1.000000

The interface-only writhes come out exactly as expected — `+1`, `~0`, `-1` —
confirming the intra-nucleon crossings cancel in the free/atom ratio.

## The result: every candidate fails, and always at nn

`mu+` (the `T=1` projector scalar) is channel-INDEPENDENT, so the threshold
`f >= 3` applies to **every** system's `T=1` channel alike.

    candidate                     pp        pn        nn      pp & nn both unbound?
    (a) interface writhe de       f=+1 bnd  f=+0 bnd  f=-1 bnd        NO
    (b) full atom-word writhe     f=+7 UNB  f=+4 UNB  f=+1 bnd        NO
    (c) sum of nucleon writhes    f=+6 UNB  f=+4 UNB  f=+2 bnd        NO

`nn` blocks all three. Its word writhe is `1` (full) or `2` (nucleon sum), and it
needs `>= 3`. The dineutron is the least-twisted two-nucleon word in the
framework and the one most in need of twist.

That is a robust negative rather than a near miss: the gap is not a few percent,
it is a whole unit of an integer-valued quantity, and it points the wrong way in
every candidate.

## What this does and does not establish

**Establishes:** the ribbon-twist route is not closed by a writhe-derived framing.
Three natural derivations of `f` were tried and none reproduces the sign
structure. So the `f >= 3` threshold remains unmet by anything derived, and
`f = 3` remains a fit.

**Does not establish:** that no derivation exists. Framings not tried here
include the Seifert framing of the closed link (rather than the braid-word
exponent sum), a framing fixed by the Markov/Ocneanu normalisation argument that
fixed `(1-h)^((e-n)/2)` with no freedom, and any `lambda`-dependent framing.

## A coincidence, recorded so it is not chased

The proton's word writhe is **exactly 3**, and the threshold is `f > 2.7227`, so
`f = 3` is the smallest admissible integer. That is suggestive and it is **not
evidence**: nothing connects the proton's internal writhe to the framing of a
two-nucleon interface, and the same number 3 would be produced by any
"smallest integer above the threshold" rule with no content. Treated the same
way as the `pi/4` near-miss in `deuteron_one_bond_isolation_probe.py` — recorded,
declined, not built on.

NO WITNESS: exponent sums of the framework's own braid words plus the closed-form
threshold; the tables reproduce it.

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

SYSTEMS = [("p", 1, 0), ("n", 0, 1), ("pp", 2, 0), ("pn", 1, 1), ("nn", 0, 2)]


def main() -> int:
    mp.mp.dps = 50
    q = mp.mpf(str(Q50))
    h = q - 1 / q
    z = q ** 3 / (q ** 2 + 1)
    mup = (z + 1 / q) / (q + 1 / q)

    from mass_at_3A_proper import atom_braid_word_3A
    import pyhecke.gram as G
    # h at 50-dps mpmath, NOT the float64 module constant G.h (which differs
    # from q0 - 1/q0 by 5.0e-17 and would pin this whole probe to double
    # precision). AGENTS.md "PROBES ARE NOT EXEMPT"; bean qou-jtbo.
    hf = G.h_mp()

    def esum(Z, N):
        return mp.fsum([mp.mpf(1) + 2 * mp.mpf(str(d)) / hf
                        for (_c, d, _g) in atom_braid_word_3A(Z, N)])

    E = {lbl: esum(Z, N) for lbl, Z, N in SYSTEMS}

    thr = (mp.log(1 / mup) / mp.log(q))
    print("Can the two-nucleon framing f be DERIVED? Attempt, and honest negative.\n")
    print(f"  threshold: T=1 unbinds iff f > {mp.nstr(thr, 6)}  ->  integer f >= 3")
    print(f"  mu+ = {mp.nstr(mup, 8)} is the T=1 projector scalar, CHANNEL-INDEPENDENT,")
    print("  so the same threshold applies to every system's T=1 channel.\n")

    print("The framework's own braid-word writhes (e = 1 + 2d/h per crossing):\n")
    for lbl, _Z, _N in SYSTEMS:
        print(f"    {lbl:<3}  e = {mp.nstr(E[lbl], 8)}")
    print(f"\n  interface-only:  pp {mp.nstr(E['pp'] - 2*E['p'], 6)}   "
          f"pn {mp.nstr(E['pn'] - E['p'] - E['n'], 6)}   nn {mp.nstr(E['nn'] - 2*E['n'], 6)}")
    print("  (exactly +1 / ~0 / -1 — the intra-nucleon crossings cancel in the ratio)\n")

    cands = {
        "(a) interface writhe de": {
            "pp": E["pp"] - 2 * E["p"], "pn": E["pn"] - E["p"] - E["n"],
            "nn": E["nn"] - 2 * E["n"]},
        "(b) full atom-word writhe": {"pp": E["pp"], "pn": E["pn"], "nn": E["nn"]},
        "(c) sum of nucleon writhes": {
            "pp": 2 * E["p"], "pn": E["p"] + E["n"], "nn": 2 * E["n"]},
    }

    print("CANDIDATE FRAMINGS — need pp and nn BOTH unbound (nature), T=0 bound\n")
    print("| candidate                    | pp        | pn        | nn        | works |")
    print("| ---------------------------- | --------- | --------- | --------- | :---- |")
    any_ok = False
    for name, f in cands.items():
        cells = []
        for s in ("pp", "pn", "nn"):
            e1 = mup * q ** mp.mpf(f[s])
            cells.append(f"{mp.nstr(f[s], 2)} {'UNB' if e1 > 1 else 'bnd'}")
        ok = all(mup * q ** mp.mpf(f[s]) > 1 for s in ("pp", "nn"))
        any_ok = any_ok or ok
        print(f"| {name:<28} | {cells[0]:<9} | {cells[1]:<9} | {cells[2]:<9} "
              f"| {str(ok):<5} |")

    print(f"\n  any candidate reproduces the sign structure: {any_ok}")
    print("\n  nn blocks ALL of them. Its word writhe is 1 (full) or 2 (nucleon sum),")
    print("  against a required >= 3. The dineutron is the least-twisted two-nucleon")
    print("  word in the framework and the one most in need of twist.")
    print("\n  This is a robust negative, not a near miss: the gap is a whole unit of an")
    print("  integer-valued quantity, and it points the wrong way in every candidate.")

    print("\n## Scope\n")
    print("  ESTABLISHES: the f >= 3 threshold is unmet by any writhe-derived framing,")
    print("  so f = 3 remains a FIT and the ribbon-twist route is not yet a derivation.")
    print("  DOES NOT establish that no derivation exists — untried: the Seifert framing")
    print("  of the closed link (not the braid-word exponent sum), a framing fixed by the")
    print("  Markov/Ocneanu argument that fixed (1-h)^((e-n)/2) with no freedom, and any")
    print("  lambda-dependent framing.")

    print("\n## Coincidence recorded and declined\n")
    print(f"  the proton's word writhe is EXACTLY 3 ({mp.nstr(E['p'], 6)}) and the threshold is")
    print(f"  f > {mp.nstr(thr, 6)}, so 3 is the smallest admissible integer. Suggestive, NOT")
    print("  evidence: nothing connects a proton's internal writhe to the framing of a")
    print("  two-nucleon interface, and 'smallest integer above the threshold' produces")
    print("  the same 3 with no content. Declined, as the pi/4 near-miss was.")
    print("\n(no witness by design — exponent sums of the framework's own words.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
