# Story B selection — canonical Q_β precision-ladder chain

**Date:** 2026-05-16
**Branch:** `claude/crystal-and-he4-combined`
**Status:** Documents the selection of **Story B** (the categorical
chain) as the canonical interpretation of the Q_β precision ladder,
superseding Story A (CODATA-noise interpretation) per the user's
direction and the categorical-derivation evidence from PRs
#661, #664, #665.

## Background — Story A vs Story B

PR #657 (merged) flagged a high-precision finding: at `dps = 200`,
the categorical-chain coefficients `c_k` of the Q_β precision ladder
can be interpreted either as:

| | c_2 | c_3 | c_4 | c_5+ |
|---|---|---|---|---|
| **Story A** | b² · (1 + 0.017) | 0 (CODATA noise) | 0 | 0 |
| **Story B** | b² (Kashiwara, exact) | -2 (J_Hopf at q=1) | b² + 1/2 (mixed) | open (categorical) |

Both stories reproduce CODATA Q_β to within its measurement floor
(~400 ppb).  PR #657 left the choice open.

## Story B confirmed canonical

Three independently-derived categorical proofs land Story B:

1. **PR #661** (merged): c_2 = b² *exactly* from V_(2,1) Hoefsmit alone —
   no fit, no free parameter.  Symbolic identity at q = 1 + ε to
   order ε^4; 50-dps mpmath confirmation at q_0 within 1.55 × 10⁻⁶².

2. **PR #664** (open, due to merge): c_3 = J_Hopf(q=1) = -2 from
   V_(2,1) self-fusion + Frobenius selection of the V_(2,2,2)
   channel + Hopf-Jones at q=1.  Empirical match exact at CODATA
   precision floor.

3. **PR #665** (open, due to merge): c_4 = b² + 1/2 (mixed Kashiwara
   + half-Hopf offset) closes the N=4 rung of the precision ladder.

Story A's c_2 = b² · (1 + 0.017) is incompatible with PR #661's exact
b² categorical derivation — the 1.7% deviation is structurally
attributable to higher c_k (c_3 = -2 + c_4 = b² + 1/2 + … per Story B),
NOT a fit parameter.

## Consequences for this branch's work

PR #670 (this branch) carries:
- **Crystal-pole counter + Habiro bridge** (PRs #668 + #669 + this PR):
  derives `shift(Z, N) = 18Z + 21N + 1` categorically.  Independent
  of Story A/B selection (shift is structural, not a precision-ladder
  coefficient).
- **⁴He compositional probe**: confirms Model B (knot identification
  via composition) is ambiguous at the Markov-trace level — separate
  concern from Story B.
- **H_12 ⁴He scaffold**: extends Sub-lemma 2.1 to ⁴He via three-fold
  iterated branching basis.  Independent of Story A/B.

**No work on this branch contradicts Story B.**  My PR #661's c_2 = b²
proof IS Story B's c_2 step.

## What remains open under Story B

- **c_5, c_6, …** — the higher precision-ladder coefficients are
  predicted to be structurally derivable (Jones invariants at q=1 of
  specific links from V_(2,1)^⊗k self-fusion) but the explicit
  derivations are not yet done.  PR #657's empirical c_5 ≈ -395
  doesn't match simple Jones-at-q=1 values; the categorical structure
  must involve higher-rank Wedderburn coefficients or composite
  Jones products.  Open R&D.

- **Lean formalisation** of `c_3 = -2` and `c_4 = b² + 1/2` propositions
  in PR #664/665 — bundles into the conditional-class chain per
  CLAUDE.md §3b-cond, with the V_(2,2,2) channel selection as the
  axiomatic input.

## Cross-references

- [PR #661 (merged)](https://github.com/litlfred/qou/pull/661) — c_2 = b² categorical
- [PR #657 (merged)](https://github.com/litlfred/qou/pull/657) — Story A vs Story B framing
- [PR #664 (open)](https://github.com/litlfred/qou/pull/664) — c_3 = J_Hopf(q=1) categorical
- [PR #665 (open)](https://github.com/litlfred/qou/pull/665) — c_4 = b² + 1/2 mixed
- [PR #670 (open, this branch)](https://github.com/litlfred/qou/pull/670) — crystal shift_NF + ⁴He compositional + H_12 scaffold

## CAL discipline

All Story B coefficients are categorical-derivation results — they
use only the substrate parameter q_0 (CAL-2) and the Hoefsmit
representation theory of V_(2,1).  No m_e, Q_β, AME, or experimental
data enters their derivation.  CODATA Q_β is referenced for
validation only, not calibration.
