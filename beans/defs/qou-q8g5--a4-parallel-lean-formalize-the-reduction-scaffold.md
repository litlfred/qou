---
# qou-q8g5
title: 'A4 (parallel): Lean-formalize the reduction scaffold (tau3=3/n eigenfn, Dirichlet id, Var=|C3|)'
status: completed
type: task
priority: normal
created_at: 2026-07-25T03:30:08Z
updated_at: 2026-07-25T11:32:38Z
parent: qou-v8t7
---

A4 — Lean scaffold: LANDED (2026-07-25). 5 sorry-free theorems in YoungDiagramKernel.lean (lean-direct exit 0; only sorry = the open conjecture): secondMomentKernel_eq_zero_of_le_seven (Σ(f)²ω₃=0 for k≤7 — encodes A5's reframing: kernel = pure dim-tilt k!·Cov(f,ω₃)); kernelValue_base_values (exact k=3..7); kernelValue_nonpos_of_le_seven (conjecture Lean-verified k≤7); contentSq_conj_invariant_of_le_six + omega3_conj_invariant_of_le_six (conjugation-symmetry, U-shape structural obstruction). SCOPE: decide-verified instances; general facts (Var=|C3|, τ3=3/n need char theory; general conj-invariance needs a sorted-List transpose bijection ~150 lines) out of scope for the elementary file and don't advance the kernel. Audit: same as A5.
