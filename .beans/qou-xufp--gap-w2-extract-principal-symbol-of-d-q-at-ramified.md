---
# qou-xufp
title: 'GAP W2: extract principal symbol of D_q at ramified pole (Ramis-Sauloy-Zhang local q-difference classification)'
status: todo
type: task
created_at: 2026-08-01T01:47:27Z
updated_at: 2026-08-01T01:47:27Z
---


## The wall (W2 / G2 of the C1↔SW leg)

Parent: `qou-3cgi`; downstream of `qou-d8de` (W1, construct `D_q`). **Conditional on
W1** — cannot start until a q-difference prolongation `D_q` exists.

Given `D_q : Jⁿ E → Jⁿ⁺¹ E` on Σ, extract its **principal symbol at a ramification
point**. At a simple branch `z = z_c + t²` (local coord `t`) the jets acquire poles
(`X⁽¹⁾ = (dX/dt)/(2t)`, order rising by 2 per jet), so the symbol is the leading
Laurent coefficient / connection-matrix datum on the `t`-punctured disk.

**Missing framework:** the Ramis–Sauloy–Zhang **local classification of q-difference
modules** (Newton polygon of a q-difference module, slopes, the Stokes/`q`-Gevrey
structure at an irregular/ramified singularity). Not in Mathlib; not in the corpus.
This is what turns `D_q` into a symbol datum comparable to C1's `{½,½}` isoclinic
slopes (`ThetaSlopeArithmetic`, on main).

**Next step:** import the q-difference local-classification framework (Sauloy,
*Systèmes aux q-différences singuliers réguliers*; Ramis–Sauloy–Zhang, *Local
analytic classification of q-difference equations*) before attempting extraction.
