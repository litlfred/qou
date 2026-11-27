---
# qou-q3dc
title: 'GAP: q-NS Part A needs the q-Clebsch-Gordan triad coefficients or a 3-complex DEC model'
status: todo
type: task
priority: normal
created_at: 2026-11-27T18:40:00Z
updated_at: 2026-11-27T18:40:00Z
parent: qou-pa7n
---

Follow-up to qou-pa7n (PR #9537). Two results show Part A of `conj:regularity-breakdown` is false on every finite or two-dimensional model:
- `partA_fails_on_truncation` (q_ns_modal_triad.lean) covers every finite truncation of the triad model;
- `partA_fails_dec2d` (q_ns_dec_refinement.lean) covers every 2-complex at every resolution, given an enstrophy-skew advection.

**Two routes forward.**

1. **q-CG coefficients.** Compute the coefficients of `μ∘(v⊗∇_q v)` on SU_q(2) Peter–Weyl modes, i.e. the q-Clebsch–Gordan / 6j coefficients times the `∇_q` symbol. Instantiate `TriadCoeff` with them (the conservation field must be proved, not assumed). Then state Part A as a primary conjecture over the infinite-mode system. Note that `∇_q = q⁻¹∇ + (1−q⁻¹)(ι_ξ∇)Θ` is a derivation, so energy conservation should follow from Leibniz and the dagger adjointness. That is to be proved.
2. **3-complex DEC model.** Build `C⁰→C¹→C²→C³` with vortex stretching and state Part A over refining 3-complexes.

Open conjecture: do not close until Part A is proved or refuted. QOU-formalised sources only (owner rule 2026-11-27).
