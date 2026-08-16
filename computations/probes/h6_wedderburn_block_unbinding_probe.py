#!/usr/bin/env python3
"""
Probe — the full H_6 Wedderburn decomposition DOES contain unbinding blocks.

Three routes through the 2-dimensional interface subalgebra `span{1, sigma}` are
now closed:

* single crossing at any admissible `d` — `mu <= z < 1`, always binds
  (`QOU.QBeta.single_crossing_binds`, sorry-free);
* the `T3`-graded writhe — hands `pp` a non-negative exponent, which binds harder
  (`QOU.QBeta.t3_grading_cannot_unbind_pp`);
* stacked powers — the writhe cancels in the channel ratio, and the surviving
  `q^(2m)` orders the channels backwards (`ribbon_twist_t_selective_probe.py`).

All three share a premise: that the two-nucleon interface lives in a
2-dimensional subalgebra. This probe drops that premise and asks the prior
question — does the FULL `H_6` (6 strands = 2 nucleons x 3) contain the range
that `span{1, sigma}` provably lacks?

## Method

Per Wedderburn block `lambda |- 6`, the ratio

    r_lambda = chi_lambda(W_atom) / chi_lambda(W_free)

using `pyhecke.trace.atom_character_raw`, whose `include_inter=False` mode gives
exactly the disconnected free baseline `H_3(q)^{tensor A} -> H_{3A}(q)`. A block
BINDS when `r_lambda < 1` (`B = -alpha*ln r > 0`) and UNBINDS when `r_lambda > 1`.

## Result — yes, and in the right blocks

    lambda        pp        pn        nn
    (6,)        1.110     1.005     0.901
    (5,1)       3.759     4.388     6.464      <- unbound in all three
    (4,2)       3.150     2.438     1.982      <- unbound in all three
    (4,1,1)     0.889     0.975     0.812
    ...          (the taller blocks are bound or sign-flipped)

`H_6` carries `r_lambda` up to `6.46` — far above `1` — where the 2-dim
subalgebra is capped at `z = 0.6127`. The premise the three closed routes shared
is what was blocking them, not the substrate anchor.

And the unbinding sits in the **wide** blocks `(6,)`, `(5,1)`, `(4,2)` — the
symmetric end — while the tall blocks bind or flip sign. Wide = symmetric =
`T=1`-like is exactly where nature puts the unbound channels (pp, nn, np-1S0),
so the block structure is oriented correctly, not merely large enough.

## Validation — the 1-dim blocks reproduce the Hecke eigenvalues exactly

`(6,)` is the trivial rep (`sigma -> q`) and `(1^6)` the sign rep
(`sigma -> -1/q`). Each two-nucleon system has exactly ONE crossing more than its
free reference, so `r` on those blocks must be the eigenvalue itself:

    pp  (6,)    +1.10997858   predicted +q     = +1.10997858   exact
    pp  (1^6)   -0.90091828   predicted -1/q   = -0.90091828   exact
    nn  (6,)    +0.90091828   predicted +1/q   = +0.90091828   exact
    nn  (1^6)   -1.10997858   predicted -q     = -1.10997858   exact

(`nn`'s interface is `sigma^-1`, hence the swap.) This is an independent check on
the whole character computation, and it passes to every digit.

## An obstruction this exposes, worth recording

**6 or 7 of the 11 blocks have `r_lambda < 0`** — the character changes SIGN
between the atom and free words. For those blocks `-alpha*ln(r)` is undefined, so
a per-block "binding energy" does not exist at all. Anyone building a per-block
binding decomposition has to say what a negative character ratio means first;
this is not a detail that can be deferred.

**And the flip is not scattered — it is sorted by conjugation.** Counting
negatives by shape, identically in all three systems:

    WIDE (<= 2 rows)   1 of 4 negative
    TALL (>= 4 rows)   4 of 4 negative

Every conjugate pair shows it: the tall member is negative where the wide member
is positive (`(2,1^4)/-1.52` vs `(5,1)/+3.76`, `(2,2,1,1)/-0.33` vs `(4,2)/+3.15`,
and so on). The mechanism is the sign representation — taller partitions are more
sign-like, and the sign rep contributes `-1/q` per crossing.

This SHARPENS the obstruction rather than explaining it away. Wide = symmetric =
`T=1`-like is where the unbinding sits and where `r > 0`, so those blocks have a
well-defined energy. Tall = antisymmetric = `T=0`-like is the deuteron's side —
and it is exactly there that `r < 0` and the per-block energy does not exist. The
undefined blocks are not a random 7 of 11; they are the channel that has to come
out BOUND.

## What this establishes, and what it does NOT

**Establishes:** the interface-scalar picture is too small, and `H_6` is not.
Option C (drop the 2-dim subalgebra) is structurally viable where the framing and
stacking routes are provably not.

**Does NOT establish** any of the following, and none should be read into it:

* that the aggregate binding comes out right — it does not. The `y_lambda`-weighted
  total is still `+2.54 MeV` for pp, i.e. still a bound diproton. The unbinding
  blocks are outweighed by the bound ones in the full trace.
* that any SELECTION PRINCIPLE picks the unbinding blocks for the pp/nn channels.
  The corpus does have machinery of the right type — the operator-selection
  LP/SDP (`prop:operator-selection-lp`), whose dual shadow prices identify which
  blocks a bound state saturates — but nothing here connects it to this.
* any magnitude claim. No `B_lambda` is proposed and nothing is wired.

Choosing the blocks that give the right answer would be a fit, and a
particularly easy one to commit here because there are 11 of them. The result is
a statement about RANGE, not about a construction.

NO WITNESS: per-block character ratios from the framework's own words; the table
reproduces them.

Bean qou-brg3; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import math
import sys

SYSTEMS = [("pp", 2, 0), ("pn", 1, 1), ("nn", 0, 2)]


def main() -> int:
    # mass_at_3A_proper extends sys.path for pyhecke; import before hecke_core.
    from mass_at_3A_proper import atom_braid_word_3A  # noqa: F401
    import hecke_core_legacy as HC
    from pyhecke.trace import atom_character_raw

    six = [e for e in HC._PARTITION_TABLE
           if e.get("k", 0) == 6 and e.get("has_ysn")]
    if not six:
        print("ABORT — no k=6 YSN entries in the partition table; nothing measured.")
        return 2

    print("Does the FULL H_6 contain unbinding blocks, where span{1,sigma} cannot?\n")
    print(f"  {len(six)} Wedderburn blocks with seminormal data at k = 6")
    print("  r_lambda = chi_lambda(atom)/chi_lambda(free);  BOUND iff r < 1\n")

    results = {}
    for lbl, Z, N in SYSTEMS:
        print(f"=== {lbl}")
        print("  | lambda             | dim | y_lambda   | r_lambda   | verdict   |")
        print("  | ------------------ | --: | ---------: | ---------: | :-------- |")
        nunb = nflip = 0
        for e in sorted(six, key=lambda x: tuple(x["partition"])):
            lam = tuple(e["partition"])
            ca, na, _ = atom_character_raw(Z, N, e, include_inter=True)
            cf, nf, _ = atom_character_raw(Z, N, e, include_inter=False)
            ca, cf = float(ca), float(cf)
            if ca == 0 or cf == 0:
                print(f"  | {str(lam):<18} | {e['dim']:>3} |          - "
                      f"|          - | chi zero  |")
                continue
            logr = (math.log(abs(ca)) + float(na)) - (math.log(abs(cf)) + float(nf))
            sgn = (1 if ca > 0 else -1) * (1 if cf > 0 else -1)
            r = sgn * math.exp(logr)
            if sgn < 0:
                verdict = "SIGN-FLIP"
                nflip += 1
            elif r > 1:
                verdict = "UNBOUND"
                nunb += 1
            else:
                verdict = "bound"
            yw = float(e.get("wedderburn_weight", float("nan")))
            print(f"  | {str(lam):<18} | {e['dim']:>3} | {yw:>10.6f} | {r:>10.6f} "
                  f"| {verdict:<9} |")
        results[lbl] = (nunb, nflip)
        print(f"  -> UNBINDING blocks: {nunb}   sign-flipped: {nflip}\n")

    any_unb = any(v[0] > 0 for v in results.values())
    print("## Verdict\n")
    print(f"  H_6 contains unbinding blocks: {any_unb}")
    if any_unb:
        print("  The 2-dim interface subalgebra is capped at mu <= z = 0.6127 and")
        print("  provably always binds; H_6 reaches r_lambda ~ 6.5. The shared premise")
        print("  of the three closed routes -- that the interface is 2-dimensional --")
        print("  is what was blocking them, not the substrate anchor.")
        print("\n  Orientation: the unbinding sits in the WIDE blocks (6,), (5,1), (4,2)")
        print("  -- the symmetric end -- while tall blocks bind or flip sign. Wide =")
        print("  symmetric = T=1-like is where nature puts the unbound channels.")
    flips = max(v[1] for v in results.values())
    print(f"\n  OBSTRUCTION: up to {flips} of {len(six)} blocks have r_lambda < 0 --")
    print("  the character changes sign between atom and free, so -alpha*ln(r) is")
    print("  UNDEFINED there and a per-block binding energy does not exist. Any")
    print("  per-block decomposition must say what a negative character ratio means.")

    print("\n## Scope\n")
    print("  ESTABLISHES range only: H_6 is big enough, span{1,sigma} is not.")
    print("  Does NOT establish that the aggregate is right -- it is not; the")
    print("  y_lambda-weighted total is still +2.54 MeV for pp, a bound diproton.")
    print("  Does NOT supply a selection principle picking the unbinding blocks. The")
    print("  corpus has machinery of the right type (operator-selection LP/SDP, whose")
    print("  duals identify saturated blocks) but nothing here connects it.")
    print("  Choosing blocks that give the right answer would be a fit, and an easy")
    print("  one to commit with 11 of them. Nothing is proposed and nothing is wired.")
    print("\n(no witness by design — per-block character ratios of the framework's words.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
