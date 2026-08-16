---
# qou-cwin
title: 'MIGRATION: express the Q_beta c_k ladder in h = q - 1/q instead of u = b*hbar_q^2'
status: in-progress
type: task
priority: high
created_at: 2026-08-16T12:45:00Z
updated_at: 2026-08-16T12:45:00Z
---

Owner-authorised 2026-08-16: *"bean up and start = express the ladder in h"*.
Parent: `qou-cds1` (S1 of the convention ruling). Evidence for the decision is
on PR #5210.

## Why (the reasons that survived measurement)

- **Analyticity.** `u ~ h^2`, so reverting `u -> h` needs `sqrt(u)` and the
  ladder is non-analytic at `u = 0` (corpus:
  `qbeta_ck_from_operator_markov_trace_probe`). In `h` the same function is a
  genuine power series: measured, `cos(alpha - u/2) = 1 + 0*s - s^2/8 +
  ((1-sqrt3)/8)s^3 + ...` with `s = q-1`, integer powers throughout.
- **Expressiveness.** Odd-order content is half-integer in `u` and therefore
  structurally unrepresentable there. In `h` it is an ordinary rung. Note
  `s^1 = 0` exactly, so the h-frame has no linear rung -- the `u^1` rung
  (`a_1 = -sqrt(3)/12`) is an artifact of expanding in a squared variable.
- **Literature alignment.** The Ohtsuki series is a power series in `q - 1`
  with integral coefficients (Lawrence conj., Rozansky proof); the Habiro ring
  is described as analytic functions at roots of unity.
- **Channel consistency.** alpha_EM's Habiro element is ALREADY written in h:
  `[2]_q * (1 - h^2 * a)`. Q_beta is the odd channel out.

## Why NOT (measured, and it must not be over-sold)

**The reframe does not fix anchor-instability.** Tested at matched
magnification (`h^k` chosen so `h^k ~ u^3`) in
`qbeta_h_vs_u_frame_stability_probe`:

    frame       proton         muon      rel swing
      u^3    -2.069343    -2.020200      2.3748%
      h^9    -1.676039    -1.636236      2.3748%
    residual R                           2.3747%

Identical to five significant figures; the variables' own swings are ~1e-6.
The instability is in the RESIDUAL, not the coordinate. This refuted a
hypothesis I had put in writing (that half-integer leakage drives the drift) --
scope-(a), as the explanation of THIS drift at THESE anchors.

**Cost: ~3x the rungs** for equal precision (7.2 -> 22.1 for 1e-15). It is
3.045x rather than 2x because `u = 0.195 h^2`, and that prefactor costs about
as much as an extra power at these magnitudes.

So this migration is **hygiene and expressiveness, not a fix.** Do not
describe it as one in any PR, witness, or content block.

## Blast radius

Every `c_k`-derived statement is u-frame and becomes a different number:
`c_2`, `c_3`, `c_4...`, `S_leak = c_3 + Vol(4_1)`, `q*_S`,
`c_3^even = -Vol(4_1)`, `[3]_q/25`, `J - hbar^2`. Plus AGENTS.md's truncation
rule `N >= log10(1/eps)/2.07 - 1`, whose `2.07` is `-log10(u)`.

## Ordered plan

**T0 (FIRST, before any number moves) -- make the frame DECLARABLE.**
Add a `ladder_frame: "u" | "h"` field to every c_k-bearing witness and require
it. This is the lesson from the convention C->D campaign, learned the hard
way: PR #5210's own `--impact-vs-main` had to report *"0 of 12 declare
`markov_convention`, so the count is a lower bound."* A migration whose
artifacts do not declare their frame cannot be measured, only guessed at. Do
NOT skip this step to get to the interesting part.

**T1** -- extract the h-frame rungs at both anchors; establish the h-ladder as
a computed object with a witness, alongside (not replacing) the u-ladder.

**T2** -- registry: record the frame on every c_k row; pair with `qou-f09n`'s
`c_2` / `\tilde c_2` naming so a reader can tell which coefficient in which
frame.

**T3** -- re-derive the truncation-order rule in h and correct AGENTS.md
line 1062. Owner sign-off required (STRICT banner, contested channel).

**T4** -- downstream content blocks. NOT started without owner sign-off:
changes published statements.

## Discipline

The anti-fit rules are unchanged. A rung obtained by matching a target is a
fit regardless of which variable it is written in. `alpha` remains un-derived
in both frames and this migration does not change that.
