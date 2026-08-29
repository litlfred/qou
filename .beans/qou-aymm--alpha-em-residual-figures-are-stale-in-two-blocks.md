---
# qou-aymm
title: 'alpha_EM residual figures are stale in two blocks: open-problems table carries muon-pin order-2 values, hydrogen block cites the wrong prop and quotes an unsourceable 2.1 ppm'
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T05:21:15Z
updated_at: 2026-08-29T05:34:02Z
---

## Finding: one un-propagated proton re-pin, not four wrong numbers

`em-coupling-chern-simons.md` was corrected at some point -- the CS tower was
resummed in closed form and the evaluation moved to the proton pin -- and it
records that correction properly, including its own superseded figures. Three
downstream sites kept the pre-correction numbers.

Every stale figure is a MUON-pin value, correctly computed for the pin and
truncation it belongs to. Sourced exactly, all eight combinations enumerated:

| stale figure | site | exact provenance |
|---|---|---|
| Form A residual -4.0e-7 | open-problems table | muon pin, order-2 -> -399.53 ppb |
| Form B residual +6.7e-9 | open-problems table | muon pin, CODATA-2018 -> 6.672 ppb |
| kappa ~ 1.888 | open-problems table + prose | muon, order-2, CODATA-2022 -> 1.8880423 |
| kappa ~ 1.8878 | chern-simons proof sketch (line 64) | muon, order-2, CODATA-2018 -> 1.8877596 |

So these are STALE, NOT WRONG. I nearly recorded them as errors; computing all
four pin/truncation combinations for kappa is what caught it. This is the
"quantity differing only by normalisation, mistaken for a discrepancy" trap
AGENTS.md names on the c_k banner.

Live values, proton pin, from `alpha_em_form_comparison_probe.py` (the block's
own named reproduction path), independently cross-checked for the bare term at
50 dps with mpmath:

  bare  q[9][10]         136.8232088536    -1552806.0 ppb   derived
  bare + 2/(3pi)         137.0354154444       -4259.7 ppb   derived
  CS tower resummed      137.035935094         -467.6 ppb   conjectural (kappa is a `sorry`)
  45[3](1+d+8qd^2)       137.0359995317            2.6 ppb   RULED OUT (PSLQ-empirical)

  exact closure needs kappa = 1.9153143 vs Witten's 1.7216142 (11.2%)

Note the probe's own remark, which is the honest reading: the SMALLEST residual
belongs to the RULED-OUT form. That is the signature of a fit, not evidence.

## Second defect: hydrogen-knot-structure overstates and mis-cites

`ex:hydrogen-knot-structure` said:

  "Including the Chern-Simons correction from the force-carrier torus knots
   ([EM coupling projection](#prop:em-coupling-projection)) yields
   alpha^-1 ~ 137.036 (2.1 ppm from CODATA)."

Three problems in one sentence:

1. **Wrong citation.** `prop:em-coupling-projection` is 27 lines and contains
   only the bare formula -- no Chern-Simons correction, no 137, no ppm. The CS
   material is in `rem:em-coupling-chern-simons`.
2. **A conjecture stated as a result.** Form A is conjectural and its kappa is
   an unproved Lean `sorry`. With the DERIVED Witten kappa it does not reach
   137.036 -- it reaches 137.035935, still -468 ppb out.
3. **"2.1 ppm" is unsourceable.** I could NOT reproduce it from any form at
   either pin against either CODATA: not -467.6, -478.7, -399.5 or -388.5 ppb,
   not +2.6 or +6.7 ppb, and not 6 ppb (the rounding of "137.036" itself).
   Recorded as unsourced rather than asserted wrong.

## Corpus-grep discipline

alpha_EM is NOT an item I found open. `rem:alpha-em-derivation-open-problems`
already carries it, honestly and in detail: Form A conjectural with kappa a
`sorry`, Form B called "hidden numerology" and "a single-point fit" by the
corpus itself, four closure paths ruled out including a decisive 100-dps PSLQ
scan over a 54-element basis. Bean `qou-pjfu` (completed) is a different
subject -- a Lean `qInt` compile error.

What is new here is only the staleness cascade and the hydrogen block's
overstatement.

## How it was found

By generalising the blind spot behind `qou-a468`: a scan for blocks whose prose
DERIVES a value ("gives"/"yields"/"hence" + a numeric literal + a quantity noun)
that the governing Lean never mentions. v1 required a sibling `.lean` and would
have missed one of the two known positives, so it was widened to resolve Lean
through `interprets`/`uses` -- coverage 890 -> 2458 blocks. Calibrated against
both known positives before being trusted.

Result: 3 candidates in 2458 blocks. Two are false positives and are honest
negative results ("yields +0.145 m_e, MISSING the target -4.35 m_e"; "yields
ONLY a 4-dimensional quadruplet, not a decuplet"). The third is this one.

That is a NEGATIVE worth recording: under this predicate the corpus is close to
clean, and the two quark blocks were outliers rather than a systematic pattern.
The predicate is narrow -- it needs all three signals in one sentence -- so 3 is
a lower bound, not a census.

## Disposition

Fixed on `claude/coulomb-charge-channel-swap-2026-08-29` (PR #5956). Superseded
figures kept and sourced in place, following the precedent the chern-simons
block already set. run-validate 0 issues; three sidecars refreshed; render-QA
battery clean.
