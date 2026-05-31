# Tier 1.B — intermediate-state memoisation (research)

**Date:** 2026-05-31
**Trigger:** Owner — "do tier 1.b" (the memoisation salvage path flagged as
queued after [#1501](https://github.com/litlfred/qou/pull/1501) merged).
**Builds on:**
[`2026-05-30-tier-1b-orbit-reduction.md`](2026-05-30-tier-1b-orbit-reduction.md)
(the corrected Tier 1.B: no `|orbit|` trace multiplier) and
[`2026-05-30-orbit-trace-identity-proof.md`](2026-05-30-orbit-trace-identity-proof.md)
§"Correction to the roadmap" (lines 76–80, 97–100).

> **Status: research, not engineering.** The prior audits scoped this as
> *unverified* and *research-grade*. This document is the investigation
> log; it states the hypothesis up front and records findings (positive
> or negative) as they land. Do not cite a speedup from this branch until
> the cross-check section below is filled with measured numbers.

## The hypothesis

`tr_M(β_{Z,N}) = tr_M(representative)` — **no `|orbit|` multiplier** (proven,
#1483). The `Z!·N!` orbit size is instead the redundancy of **orbit-equivalent
intermediate reduction states** during `incremental_reduced_element`. Concretely:

- The atomic word for `(Z, N)` is the canonical `p…pn…n` — `A` three-strand
  nucleon blocks, block `k` shifted by `δ = 3k`.
- Folding adjacent same-species blocks `proton@0 ⊗ proton@3` yields a reduced
  intermediate that should be the **shift-by-3 translate** of
  `proton@3 ⊗ proton@6`, etc. The reduce currently recomputes each.
- **Memoise** the reduced intermediate keyed by its *shift-normalised* form
  (via `markov_peel._shift_nf`) and reuse it for every translate. This
  deduplicates the reduction tree — the genuine content of "`Z!·N!`".

This is a layer *above* the existing `pre_register_nucleons` optimisation,
which already caches single-nucleon NFs (`_shifted_nucleon_nf`, `lru_cache`).
The open question is whether the **multi-nucleon** intermediate states are
translate-equivalent in the reduced basis, or whether the inter-nucleon
crossings break the translation symmetry.

## Plan

1. **Profile** the `incremental_reduced_element` fold for ⁵Li/⁶Li — where does
   the wall go, and how many intermediate states recur up to a shift?
2. **Confirm or refute** translate-equivalence of the intermediate states
   (the load-bearing assumption).
3. If confirmed, **implement** the memo and **cross-check** every atom at
   `A ≤ 6` against the full-word path (byte/numeric ≤ 1e-40), per the
   roadmap-correction mandate.
4. **Measure** the speedup honestly; retire the hypothesis if it is illusory
   (as the `|orbit|` multiplier was).

## Known risk — the representation artefact

The identity-proof follow-up (lines 97–100) records that a *naïve
generator-relabelling* block-swap produces a word the Markov-peel recursion
cannot process — a representation artefact, **not** a counterexample. That
blocks the numerical *conjugation test*; this investigation does not depend
on it (the memo keys on shift-normalised reduced states, not on a block-swap
braid). Findings on whether the artefact also obstructs the memo go here.

## Findings

_pending — investigation in progress._

## Cross-check

_pending — table of (atom, full-path tr_M, memo-path tr_M, |Δ|, wall before/after)._
