---
# qou-k5jt
title: 'Bridge the opaque markovTrace to the concrete one: make the Hecke interface axioms provable'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T03:35:23Z
updated_at: 2026-11-16T19:05:00Z
parent: qou-rtxm
---

MarkovTrace_cyclic: my characterization was wrong on all three counts.

Claimed: 'the genuine remaining axiom, blocked on heckeMul being opaque, a formalization project rather than a cleanup.'

Measured:
  * NOT blocked in any load-bearing sense -- ZERO consumers corpus-wide.
  * NOT a formalization project -- cyclicity is already PROVED concretely
    (MathlibExt.character_append_comm) and proved conditionally over a generic
    algebra (Machinery/MarkovInductiveCyclicity, 0 sorry/0 axiom).
  * It WAS a cleanup, which is the opposite of what I said.

Removed the axiom (kept opaque heckeMul, which is a datum not an axiom, and is needed by markov_axioms_vacuous_of_weight_zero). Surface 22 -> 21 library, 198 -> 197 corpus.

Measurement note: my first 'zero consumers' grep excluded the declaring files and so hid an in-file consumer -- my own degeneracy lemma. The build caught it. Filter-hides-the-answer, again.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — Concrete Wedderburn Character Bridge for Hecke Trace Axioms (PR #8157)
- Formalized `TwoBlockWedderburnTrace`, `concrete_wedderburn_trace_add`, `concrete_wedderburn_trace_cyclic`, `concrete_wedderburn_trace_one`, and the explicit `H₂(q)` 2-block witness `h2_concrete_trace_nonvacuity` in `folio/quantum-observable-universe/lean/QOU/Foundations/FrobeniusHopfMarkovBridge.lean` (wired into `QOU.lean`, 0 `sorry`, 0 `axiom`, generic `CommRingOps R` per §7c).
- PR: https://github.com/litlfred/qou/pull/8157 (commit `16f8c01498462170d1ad98f5b5426233d3feea7d`). Status kept `in-progress`.
