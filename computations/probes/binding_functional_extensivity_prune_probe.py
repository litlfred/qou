#!/usr/bin/env python3
"""
Probe — extensivity settles qou-y0mc: the channel-measure entropy CANNOT be it.

`binding_law_surprisal_vs_entropy_ambiguity_probe.py` recorded that the binding
law's own interpretation block names two inequivalent objects for the archimedean
functor (step 7 of the canonical chain, the map trace -> MeV):

    S = -sum log(mu)          the IMPLEMENTED sum of bare surprisals
    H = -sum mu_hat log(mu_hat)   the NAMED entropy of the normalized channel
                                  measure y_lambda chi^lambda over Wedderburn blocks

and measured that nature's two-nucleon total sits outside S's range (3.27x) and
inside H's (1.09x). It filed the choice as an ambiguity and explicitly BLOCKED
resolving it by picking whichever fits.

This probe resolves it the other way — by a structural invariant.

## The argument

H is a single entropy of the block measure for the WHOLE nucleus, so it is capped
by the log of the number of accessible blocks. Convention D is Wenzl level 2
(`traceSum_eq_twoRow_of_wenzl`), so `y_lambda = 0` unless `l(lambda) <= 2` and the
accessible blocks for `n = 3A` strands are the <=2-row partitions of `3A`:
exactly `floor(3A/2) + 1` of them. Hence

    B_H <= alpha * log( floor(3A/2) + 1 )   ~  alpha * log A

while binding energy is EXTENSIVE (~ A). S, being a sum over the chain's `A-1`
bonds, is extensive by construction. H is not, and no choice of block measure
can make it so — the bound is on the entropy of ANY measure on that many atoms.

## The measurement

    iso    blocks   alpha*log(blocks)   B_AME      H viable?
    2H          4              5.80      2.22      yes
    4He         7              8.15     28.30      NO   (3.5x short)
    12C        19             12.33     92.16      NO   (7.5x)
    56Fe       85             18.60    492.26      NO   (26x)
    208Pb     313             24.05   1636.44      NO   (68x)

The deficit widens without limit.

## Why this is a prune and not a preference

It goes AGAINST the form that fitted better. H looked 1.09x on the two-nucleon
total where S looked 3.27x; H is nonetheless the excluded one. A resolution that
overrides the better fit is the opposite of the laundering qou-y0mc guarded
against.

The 2H row is the tell: H is viable only where the block count is comparable to
the nucleon count — i.e. the two-nucleon case that motivated it. That is the
signature of a functional form selected on a single data point.

## Consequences

1. **S is confirmed as the step-7 functional.** The two-nucleon floor
   `B(T=1)+B(T=0) >= alpha*log 4` stands as proved, and the 3.27x over-binding is
   REAL, not an artifact of the wrong functional.
2. **R is now well-defined.** `R(A) := B_AME/A - B_chain/A` is a residual against
   `B_chain`, which is whatever step 7 produces — so R's DEFINITION was in doubt
   while y0mc was open. It no longer is. R and y0mc were never independent open
   items; R was downstream.
3. The interpretation block remains self-inconsistent as written and should be
   scoped to say the channel-measure sentence is an analogy, not the functional.

## Scope

**Scope-(b), invariant named:** extensivity of binding energy versus a
logarithmic cap on any entropy over `floor(3A/2)+1` atoms. Excludes H as the
archimedean functor at every `A >= 4`.

**Not excluded:** a functional that is neither S nor H; an A-dependent mixture;
or a reading in which the channel measure is over something other than the
Wedderburn blocks (but the corpus block says Wedderburn blocks explicitly).

NO WITNESS: a counting bound plus AME2020 totals; the table reproduces it.

Bean qou-y0mc; L2 binding axis.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _Path, _bridge

import sys

import mpmath as mp

E0_STR = "4.1859813632944758969"
ROWS = [("2H", 2, "1.1123"), ("4He", 4, "7.0739"), ("12C", 12, "7.6801"),
        ("56Fe", 56, "8.7904"), ("208Pb", 208, "7.8675")]


def main() -> int:
    mp.mp.dps = 25
    E0 = mp.mpf(E0_STR)
    print("Extensivity settles qou-y0mc — the channel-measure entropy cannot be it.\n")
    print("  Convention D is Wenzl level 2, so y_lambda = 0 unless l(lambda) <= 2:")
    print("  the accessible blocks for n = 3A are the <=2-row partitions of 3A,")
    print("  exactly floor(3A/2)+1. Any entropy on them is capped by its log.\n")
    print("|   iso |   A |    n=3A | blocks | a*log(blocks) | B_AME MeV | H viable |")
    print("| ----: | --: | ------: | -----: | ------------: | --------: | :------- |")
    viable = []
    for lab, A, bpn in ROWS:
        n = 3 * A
        blocks = n // 2 + 1
        cap = E0 * mp.log(blocks)
        need = mp.mpf(bpn) * A
        ok = cap >= need
        viable.append((lab, ok, need / cap))
        print(f"| {lab:>5} | {A:3d} | {n:7d} | {blocks:6d} | {float(cap):13.2f} "
              f"| {float(need):9.2f} | {'yes' if ok else 'NO':<8} |")
    print("\n  short by:  " + ",  ".join(f"{l} {mp.nstr(r, 3)}x" for l, ok, r in viable if not ok))
    print("\n  S = sum over A-1 bonds   -> EXTENSIVE, grows like A")
    print("  H <= alpha*log(#blocks)  -> grows like log A")
    print("  Binding energy is extensive. log A is not. The deficit widens without limit.\n")

    print("## Why this is a prune, not a preference\n")
    print("  It goes AGAINST the better fit: H looked 1.09x on the two-nucleon total")
    print("  where S looked 3.27x, and H is the excluded one. A resolution that")
    print("  overrides the better fit is the opposite of what qou-y0mc guarded against.")
    print("\n  The 2H row is the tell — H is viable only where the block count is")
    print("  comparable to the nucleon count, i.e. the case that motivated it. That is")
    print("  the signature of a form selected on one data point.\n")

    print("## Consequences\n")
    print("  1. S is CONFIRMED as the step-7 archimedean functor. The two-nucleon")
    print("     floor stands as proved; the 3.27x over-binding is real.")
    print("  2. R := B_AME/A - B_chain/A is now WELL-DEFINED. Its definition was in")
    print("     doubt while y0mc was open — R was downstream of it, not independent.")
    print("  3. The interpretation block is still self-inconsistent as written and")
    print("     should be scoped: the channel-measure sentence is an analogy, not")
    print("     the functional.\n")
    print("  SCOPE-(b), invariant named: extensivity vs a logarithmic cap on any")
    print("  entropy over floor(3A/2)+1 atoms. Excludes H at every A >= 4.")
    print("  NOT excluded: a functional that is neither S nor H, an A-dependent")
    print("  mixture, or a channel measure over something other than Wedderburn")
    print("  blocks (but the corpus block says Wedderburn blocks explicitly).")
    print("\n(no witness by design — a counting bound plus AME2020 totals.)")

    assert not any(ok for _l, ok, _r in viable[1:]), "H must fail for A >= 4"
    assert viable[0][1], "H should be viable at 2H — that is the tell"
    return 0


if __name__ == "__main__":
    sys.exit(main())
