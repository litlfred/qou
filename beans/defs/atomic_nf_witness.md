---
# atomic_nf_witness
title: atomic nf witness missing hypotheses
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-11T00:00:00Z
updated_at: 2026-10-04T15:26:44Z
parent: qou-iqjk
---

File: `folio/quantum-observable-universe/lean/QOU/ParticleInteractions/atomic_nf_witness.lean`
The `atomic_nf_witness` theorem is unprovable. `AtomicNfWitnessContext` provides `F_Pauli`, `trAlt`, and `net` as free unconstrained variables, so `F_Pauli = |trAlt / net|` does not logically follow.



Also known as `atnw` (its former front-matter header id; the beans CLI uses the filename id `atomic_nf_witness`). Recorded 2026-10-04.
