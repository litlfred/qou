#!/usr/bin/env python3
"""Provenance probe for observations/neutron-proton-mass-splitting-proof.md.

That block cites `atom-mass-complete-wedderburn.witness.json` as its witness.
CORRECTED 2026-08-25: an earlier version of this docstring said the witness
"never existed in git history".  THAT IS FALSE -- it was added 2026-04-10 in
commit 1359fe23ac under folio-assistant/computations/ and left with the
platform code in the miga migration.  See docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md.

It remains the WRONG ARTIFACT for this block regardless: it is an ATOMIC-mass
witness carrying 20 atom rows, cited by a QUARK-level computation, and the
recovered file contains no quark Phi values at all.  So the block still has no
usable witness, and the only way to check it is to re-derive its numbers from
its own stated rules.

The block states:
    uu -> sigma            (c=1, d=0)
    dd -> sigma^-1         (c=1, d=-h)
    ud -> (sigma+sigma^-1)/2   (c=1, d=-h/2)
    Phi_p(uud) = -0.8785,  Phi_n(udd) = -1.2261,  |dPhi| = 0.3476
    dm = alpha * |dPhi| = 3.7445 * 0.3476 ~ 1.302 MeV, "an error of 0.63%"

RESULT (measured, this file):

1. THE READING IS IDENTIFIED, BY THE PROTON.  Convention C with the
   suffix-inclusive Phi_1 reproduces Phi_p as -0.8785232973 against the
   published -0.8785 -- exact at the published precision.  Eight readings
   were tried (4 chain readings x 2 conventions) and only this one lands.
   So the reading is pinned, and what follows is not reading ambiguity.

2. THE NEUTRON DOES NOT REPRODUCE.  The same reading gives Phi_n =
   -1.267788822 against the published -1.2261 -- off by 0.0417.

3. SO THE HEADLINE 0.63 % IS NOT REPRODUCIBLE:

       source                        |dPhi|       dm MeV     vs CODATA
       as published                  0.3476       1.3015882    +0.63 %
       reproduced, convention C      0.38926552   1.4576048   +12.7  %
       reproduced, convention D      0.33548346   1.2562178    -2.87 %

4. AND THE BLOCK IS CONVENTION C, which the owner ruling of 2026-08-15
   excised in favour of D.  Under D the block's own claim becomes -2.87 %.

SCOPE (a), not (b): these eight readings do not reproduce the published
Phi_n.  Some further reading might.  What is established is that the
published number cannot be checked -- no witness carries quark Phi values
(the cited one is atomic-mass and carries none) and the reading that pins its
partner does not yield it.  Nothing here proposes a
replacement value or a correction; the numbers are reported as measured.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402
from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

sys.path.insert(0, str(Path(__file__).resolve().parent / "alpha"))
from alpha_blend_tower import Q0, QI  # noqa: E402

H = Q0 - QI
Z_D = Q0 ** 3 / (Q0 ** 2 + 1)                 # convention D (canonical)
Z_C = mp.sqrt(Q0) / (Q0 + 1)                  # convention C (excised 2026-08-09)

# The block's own quark crossing table.
CROSSING = {
    ("u", "u"): (mp.mpf(1), mp.mpf(0)),       # sigma
    ("d", "d"): (mp.mpf(1), -H),              # sigma^-1
    ("u", "d"): (mp.mpf(1), -H / 2),          # (sigma + sigma^-1)/2
}
PUBLISHED = {"uud": mp.mpf("-0.8785"), "udd": mp.mpf("-1.2261")}
ALPHA = mp.mpf("3.7445")          # the block's own alpha = m_e * 8G, as printed
CODATA_SPLIT = mp.mpf("1.2934")


def crossing(a, b):
    return CROSSING[(a, b)] if (a, b) in CROSSING else CROSSING[(b, a)]


def V(chain, z):
    """z*(M)_12 + (M)_22 for the chain word, exactly as Phi_1 consumes it."""
    a, b = mp.mpf(0), mp.mpf(1)
    for c, d in chain:
        a, b = a * (c * H + d) + b * c, a * c + b * d
    return z * a + b


def readings(word):
    s = list(word)
    t = [crossing(s[k], s[k + 1]) for k in range(len(s) - 1)]
    return {
        "suffix-inclusive": [t[i:] for i in range(len(t))],
        "single": [[x] for x in t],
        "prefix": [t[:i + 1] for i in range(len(t))],
        "whole": [t],
    }


def phi(word, z, reading="suffix-inclusive"):
    return mp.fsum(mp.log(abs(V(ch, z))) for ch in readings(word)[reading])


def main() -> int:
    print(f"q0 = {mp.nstr(Q0, 18)}   z_C = {mp.nstr(Z_C, 12)}   "
          f"z_D = {mp.nstr(Z_D, 12)}   h = {mp.nstr(H, 12)}")
    print("\n--- 8 readings vs the two published values ---")
    print(f"{'word':>5} {'conv':>5} {'reading':>17} {'value':>16} "
          f"{'published':>11} {'hit':>5}")
    print("-" * 68)
    hits = []
    for word in ("uud", "udd"):
        for cname, z in (("C", Z_C), ("D", Z_D)):
            for rname in readings(word):
                v = phi(word, z, rname)
                ok = abs(v - PUBLISHED[word]) < mp.mpf("5e-4")   # published to 4 dp
                if ok:
                    hits.append((word, cname, rname, v))
                print(f"{word:>5} {cname:>5} {rname:>17} {mp.nstr(v, 10):>16} "
                      f"{mp.nstr(PUBLISHED[word], 6):>11} "
                      f"{'YES' if ok else '':>5}")
        print()

    print(f"reproduced: {len(hits)} of the 2 published values")
    for word, cname, rname, v in hits:
        print(f"  {word}: convention {cname}, {rname} -> {mp.nstr(v, 10)}")
    missing = [w for w in ("uud", "udd") if w not in {h[0] for h in hits}]
    for w in missing:
        print(f"  {w}: NOT reproduced by any of the 8 readings "
              f"(published {mp.nstr(PUBLISHED[w], 6)})")

    print("\n--- what the block's own claim becomes, per convention ---")
    print(f"{'source':>32} {'|dPhi|':>12} {'dm MeV':>11} {'vs CODATA':>11}")
    print("-" * 70)
    rows = [("as published", abs(PUBLISHED["udd"] - PUBLISHED["uud"]))]
    for cname, z in (("C", Z_C), ("D", Z_D)):
        rows.append((f"reproduced, convention {cname}",
                     abs(phi("udd", z) - phi("uud", z))))
    for name, d in rows:
        dm = ALPHA * d
        print(f"{name:>32} {mp.nstr(d, 8):>12} {mp.nstr(dm, 8):>11} "
              f"{mp.nstr((dm / CODATA_SPLIT - 1) * 100, 4) + ' %':>11}")

    print("\nThe reading is pinned by the proton (exact at 4 dp) and the neutron")
    print("does not follow from it. The published 0.63 % is therefore not")
    print("reproducible, and the block is convention C either way.")
    print("\nSCOPE (a): 8 readings tried, not an exhaustive exclusion. No")
    print("replacement value is proposed here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
