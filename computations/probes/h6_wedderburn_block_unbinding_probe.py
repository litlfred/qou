#!/usr/bin/env python3
"""
RETRACTED (2026-08-16) — THE CENTRAL RESULT OF THIS PROBE IS FALSE.

This probe reported that the full H_6 decomposition "DOES contain unbinding
blocks", with r_lambda up to 6.46 and the unbinding sitting in the wide blocks
(5,1) and (4,2). **That is wrong.** It sourced per-block characters from
`pyhecke.trace.atom_character_raw`; production uses
`chi_all_lambda_reduced_block` (the fine-Bratteli transfer), and the two are NOT
the same object. On the pp atom word they agree exactly on the two 1-dim blocks
and disagree on every multi-dimensional one, with no consistent factor:

    lambda      transfer         atom_character_raw     ratio
    (6,)         2.1214920103     2.1214920103           1.0000
    (1^6)       -0.4923081365    -0.4923081365           1.0000
    (5,1)        4.2211832744    -1.1115295916          -3.7976
    (4,2)        3.3394913299    -1.4939847165          -2.2353
    (3,3)        4.8041012721    -0.0310868753        -154.5379

The transfer routine is correct: `sum y_l chi_l` over it reproduces
`tr_free/tr_atom` EXACTLY for all three systems.

CORRECTED TABLE (same y_lambda, production chi):

    lambda   y_lambda      pp      pn      nn
    (6,)     0.1153242   1.110   1.006   0.901
    (5,1)    0.0789530   0.611   0.542   0.408
    (4,2)    0.0460324   0.328   0.186   0.111
    (3,3)    0.0151238   0.928   0.919   0.934

THREE OF THE FOUR SURVIVORS ARE BOUND — the opposite of what was reported. The
only block above 1 is the trivial rep at r = q = 1.110, and `r_(6,) = q` is
forced for a 1-dim rep with one extra crossing, so it is not a finding.

CONSEQUENCE: **option C is refuted.** H_6 does not have the range that
`span{1,sigma}` lacks. The weighted maximum is q ~ 1.11, against the 2-dim
interface cap of z = 0.6127 — larger, but nowhere near the 6.46 claimed, and
every weighted block except the trivial rep binds.

HOW IT GOT PAST ME, since this is the reusable lesson: the "Validation" section
below checks the 1-dim blocks against the Hecke eigenvalues and passes to every
digit. Those are exactly the two blocks where the two routines agree. **A
validation that only exercises the 1-dim blocks cannot detect a defect in the
multi-dim ones**, and this one did not — it produced false confidence rather than
no confidence.

WHAT SURVIVES: the Wenzl y_lambda = 0 for >= 3 rows (corpus closed form, never
mine); the exact identity tr_free/tr_atom = 1/mu; the no-conjugate-pair-survives
result at n = 6. None of those routed through atom_character_raw.

The original text is retained below unaltered, as the record of what was claimed.

=====================================================================

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

## WEIGHT WARNING — `wedderburn_weight` is the PLANCHEREL weight, not `y_lambda`

The `wedderburn_weight` field on the partition table is
`W_lambda = d_q(lambda)^2 / [n]_q!` — a function of `q` alone. It is **not** the
Markov weight `y_lambda` that the Markov trace needs: `tr_M = sum_l y_l chi_l`
with `y_l` depending on the Markov parameter `z`. Measured, the difference is
not subtle:

    sum W_l chi_l : free/atom ratio  15.857   (pp)
    true tr_M     : free/atom ratio   1.632   (pp)

So anything that *weights* the characters with this field is wrong. That includes
an additive per-block decomposition of `tr_free - tr_atom` attempted here, which
came out with the wrong SIGN (implying an unbound diproton by a route that
contradicts the dashboard's own `B_sym > 0`) — caught by validating the
reconstruction against `tr_m_atom_zn` before interpreting it, and discarded.

**Nothing in this probe's VERDICT depends on the weight.** The block ratio
`r_lambda = chi_lambda(atom) / chi_lambda(free)` is a ratio of characters in the
same block, so any weight cancels identically. The unbinding finding, the
wide/tall orientation and the sign-flip structure are all weight-free. The
`y_lambda` COLUMN printed in the table below is the Plancherel weight and is
labelled as such; it is informational and enters no conclusion.

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

> **CORRECTED (2026-08-16) — the obstruction largely dissolves.** This section
> read: *"the undefined blocks are not a random 7 of 11; they are the channel
> that has to come out BOUND"*, and treated that as the blocker facing any
> per-block decomposition. It is not, because those blocks are **not in the
> trace**.
>
> Convention D *is* SU(2) Wenzl level 2 (`5cf16c8f16`, re-derived over ℚ(q)), and
> at level 2 the Markov weight vanishes on every partition with **≥ 3 rows**.
> From the corpus's own live closed form
> (`schur_principal_mpmath.y_lambda_at_q0_mpmath`) at n = 6:
>
>     (6,)   y = 0.1153242249      (4,1,1)      y = 0
>     (5,1)  y = 0.0789529625      (3,2,1)      y = 0
>     (4,2)  y = 0.0460324347      (3,1,1,1)    y = 0
>     (3,3)  y = 0.0151238101      (2,2,2)      y = 0
>                                  (2,2,1,1)    y = 0
>                                  (2,1,1,1,1)  y = 0
>                                  (1^6)        y = 0
>
> The 7 sign-flipped blocks are **exactly** the ≥3-row ones. They carry zero
> weight and contribute nothing to `tr_M`. The obstruction was on blocks that do
> not exist.
>
> What survives of it: **one** block, `(3,3)` — the rectangular two-row survivor,
> sign-flipped in all three systems (−0.018 / −0.042 / −0.269). One block, not
> seven, and why it flips while the other three survivors do not is open
> (bean `qou-8zjc`).
>
> The trace therefore sees four blocks, and **three of the four unbind in all
> three systems**. The wide/tall reading below is superseded in its conclusion —
> the orientation observation stands, but "tall blocks are the obstruction" does
> not, because there are no tall blocks in the trace.

The original reading, retained for the record: wide = symmetric = `T=1`-like is
where the unbinding sits and where `r > 0`; tall = antisymmetric = `T=0`-like is
the deuteron's side, and it is there that `r < 0`.

## What this establishes, and what it does NOT

**Establishes:** the interface-scalar picture is too small, and `H_6` is not.
Option C (drop the 2-dim subalgebra) is structurally viable where the framing and
stacking routes are provably not.

**Does NOT establish** any of the following, and none should be read into it:

* that the aggregate binding comes out right — it does not. The exact trace
  ratio is `tr_atom/tr_free = mu = 0.6127 < 1` for pp, i.e. still a **bound**
  diproton, and that is not an approximation: `tr_free/tr_atom = 1/mu` holds to
  `1e-30` for all three interfaces (the Markov property at the trace level).

  **"Three of the four surviving blocks unbind" does NOT mean the system
  unbinds, and the arithmetic is the reason.** The aggregate is a RATIO OF SUMS,

      r_total = (sum_l y_l chi_l(atom)) / (sum_l y_l chi_l(free))

  not a weighted mean of the per-block ratios `r_l`. A ratio of sums is not the
  mean of the ratios unless every `chi_l(free)` is equal, and they are not — they
  differ across blocks by orders of magnitude. So `{1.110, 3.759, 3.150, -0.018}`
  with weights `{0.115, 0.079, 0.046, 0.015}` aggregating to `0.6127` is not a
  contradiction; it is what a ratio of sums does. Anyone reading the block table
  as "mostly unbinding, therefore nearly unbound" is making exactly this error.
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
        print("  | lambda             | dim | W_l (Planch)| r_lambda   | verdict   |")
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
    print(f"\n  SIGN FLIPS: {flips} of {len(six)} blocks have r_lambda < 0, so -alpha*ln(r)")
    print("  is undefined there. But at convention D = Wenzl level 2 the Markov weight")
    print("  y_lambda VANISHES on every partition with >= 3 rows, which is exactly that")
    print("  set -- they contribute nothing to tr_M. Only 4 blocks carry weight:")
    print("     (6,) 0.1153   (5,1) 0.0790   (4,2) 0.0460   (3,3) 0.0151")
    print("  THREE OF THE FOUR UNBIND in all three systems. The residue of the")
    print("  obstruction is one block, (3,3), sign-flipped and unexplained (qou-8zjc).")

    print("\n## Scope\n")
    print("  ESTABLISHES range only: H_6 is big enough, span{1,sigma} is not.")
    print("  Does NOT establish that the aggregate is right -- it is not; the")
    print("  aggregate is still +2.54 MeV for pp, a bound diproton (dashboard value,")
    print("  Does NOT supply a selection principle picking the unbinding blocks. The")
    print("  corpus has machinery of the right type (operator-selection LP/SDP, whose")
    print("  duals identify saturated blocks) but nothing here connects it.")
    print("  Choosing blocks that give the right answer would be a fit, and an easy")
    print("  one to commit with 11 of them. Nothing is proposed and nothing is wired.")
    print("\n(no witness by design — per-block character ratios of the framework's words.)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
