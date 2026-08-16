---
# qou-jtfo
title: 'GAP: cannot reconstruct tr_M from per-block characters — 5 weight/normalisation variants all fail (recon 2.30 vs true 1.63 at pp)'
status: todo
type: task
created_at: 2026-08-16T12:33:24Z
updated_at: 2026-08-16T12:33:24Z
---


## What fails

`sum_lambda y_lambda chi_lambda` does not reproduce the transfer trace. pp,
`tr_free/tr_atom`, true value **1.63215199**:

| weighting tried | ratio | match |
|---|---:|---|
| `y_l · chi` (correct Markov `y`) | 2.29985924 | no |
| `y_l · chi / dim` | 0.99646096 | no |
| `y_l · dim · chi` | −0.04783518 | no |
| `chi` alone | 5.67975269 | no |
| `chi / dim` | 1.99448863 | no |

Also fails with the Plancherel weight `W_l = d_q^2/[n]_q!` (15.86) — that one is
separately wrong and is recorded on the h6 probe.

## Most likely cause, untested

`atom_character_raw(..., include_inter=False)` builds the free baseline as a
**6-strand disconnected word**, while `tr_m_atom_zn`'s `tf` is plausibly the
product of two separate 3-strand traces. The Markov trace is multiplicative over
disjoint components only up to `z`-power normalisation in the strand count, so
the two differ by a factor the ratio does not cancel. Not verified — stated as
the hypothesis to check first, not as the answer.

## What this does and does not block

**Blocks:** any *weighted* or *aggregate* per-block statement. No magnitude
conclusion may be drawn from a per-block decomposition until this closes.

**Does not block:** the block ratios `r_lambda = chi(atom)/chi(free)`, which are
internal to one block and need no reconstruction — confirmed by the 1-dim blocks
reproducing the Hecke eigenvalues exactly (`+q`, `−1/q`, and swapped for `nn`).
Nor the Wenzl-level-2 vanishing, which comes from the corpus's own live closed
form (`schur_principal_mpmath.y_lambda_at_q0_mpmath`), not from my arithmetic.

Honest note: I do not understand the normalisation well enough to assemble the
trace, and five guesses failed. Recording it as a gap rather than continuing to
try weightings until one lands — that procedure would find a "match" eventually
and it would mean nothing.
