---
# qou-mex9
title: LinearMap.trace packaging over the Pi tensor power — Free/Finite instances + trace = (card k)^orbitCount
status: completed
type: task
priority: normal
created_at: 2026-09-05T07:27:46Z
updated_at: 2026-09-05T07:34:57Z
---

DONE 2026-09-05, sorry-free, lean-direct exit 0 (3.4 s), zero warnings, #print axioms
clean on all five public results.

    LinearMap.trace R (⨂[R] _ : α, (κ → R)) (tensorPerm σ) = (card κ) ^ orbitCount σ

plus trace_tensorPerm_two, the card κ = 2 case: the 2^c(σ) ClassicalTraceFloor states
as its step-1 hypothesis, now over the real object with the real trace.

THE INSTANCES ARE NOT BOOKKEEPING. LinearMap.trace is defined on ANY module but is
junk without a basis, so without Module.Free/Module.Finite the headline statement
would have been VACUOUS rather than false. They are transported along monoEquiv
(Module.Free.of_equiv, Module.Finite.equiv) -- which is why constructing monoEquiv in
qou-uinl was the load-bearing step, not a detour.

MECHANISM: monoEquiv_comp_tensorPerm (permuting FACTORS is conjugate to precomposition
on index tuples by indexPerm σ⁻¹) + LinearMap.trace_comp_comm' to move the trace
across the conjugation + orbitCount_inv to absorb the σ⁻¹ (orbits are
inversion-invariant: support_inv, cycleType_inv).

SANDBOX: three more Mathlib oleans absent from the restore and built from source --
LinearAlgebra.FreeModule.Basic, LinearAlgebra.Matrix.ToLin, LinearAlgebra.Trace. With
the earlier two (Multilinear.TensorProduct, PiTensorProduct) that is five. The cache
is PARTIAL, not broken; all five build in minutes.

STALE-CLAIM SWEEP: both predecessor files said this packaging 'is not done'. Both
corrected in the same commit rather than left contradicting the file that does it.

STILL OPEN, unchanged and a different order of problem: quantum Schur-Weyl at q != 1
(qou-mpq5, multi-week: Jimbo double-centralizer + Hoefsmit matrix units). Nothing in
this arc bears on it.
