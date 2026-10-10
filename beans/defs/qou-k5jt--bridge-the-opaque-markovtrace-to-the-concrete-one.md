---
# qou-k5jt
title: 'Bridge the opaque markovTrace to the concrete one: make the Hecke interface axioms provable'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-26T03:35:23Z
updated_at: 2026-10-04T15:12:02Z
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
