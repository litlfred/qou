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

## Hypothesis REFUTED, and the measurement gave something better (2026-08-16)

The disconnected-normalisation hypothesis is **wrong**:

    tf(2,0) / tf(1,0)^2 = 1.0000000000     exactly

The free trace is multiplicative with no `z`-power correction, so that is not
where the discrepancy comes from.

What the same run did establish, unasked:

    tr_free / tr_atom  ==  1 / mu       exactly, all three interfaces

| sys | true `tf/ta` | `1/mu` | diff |
|---|---|---|---|
| pp | 1.63215199150517517 | 1.63215199150517517 | 4.9e-31 |
| pn | 1.96761390399082486 | 1.96761390399082486 | 7.2e-31 |
| nn | 2.477530419702766 | 2.477530419702766 | 1.1e-30 |

(`mu = z + d`, the interface scalar. Residuals are the `dps=50` precision floor;
an initial `1e-30` tolerance flagged `nn` spuriously.)

### Three consequences

1. **The trace side is sound**, independently confirmed. The Markov property
   `tr_M(W·sigma) = mu·tr_M(W)` holds exactly for all three interfaces.
2. **The gap is entirely on my per-block side** — not in the corpus's machinery.
   And the reconstruction now has an EXACT target to hit rather than a
   heuristic one.
3. **`SingleCrossingAlwaysBinds` describes the exact trace, not an idealisation.**
   The theorem's content is `mu <= z < 1 => B = -alpha*ln(mu) > 0`. Since the
   measured two-nucleon trace ratio *is* `1/mu` to 1e-30, the scope-(b) exclusion
   applies to the exact object with no approximation in between. That is a
   strengthening of the committed result, obtained by trying to debug something
   else.
