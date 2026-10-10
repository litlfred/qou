---
# qou-q425
title: 'M6: redo rj-canonical-inner-product in convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:58:07Z
updated_at: 2026-10-10T13:58:55Z
parent: qou-d8c7
---

predicted-spectra/rj-canonical-inner-product.md:8 defines tr_M with z = z_C into Q(q^1/2) (4 users). Owner pick 2026-10-10 (M6 Decision 4): bean up and redo in convention D. Work on PR #7562.


2026-10-10: restated in D on PR #7562: tr_M into Q(q), z = q^2/[2]_q, d_lambda = sl2 hook-content dim prod[2+c]/[h], w_lambda = d_lambda/[2]^r (sympy-checked n=3, normalisation 1). Form degenerate: radical = classes with >2 rows. OPEN: part (iii) Rosso-Jones not re-verified (antisymmetric eigenvalue sign -q^-1 missing from omega_lambda = q^c). Uniqueness claim in (ii) restricted to the two-row part.


2026-10-10 (branch claude/rj-inner-product-d-2026-10-10): part (iii) re-verified in exact sympy over Q(q), probe computations/probes/rj_inner_product_conventionD_torus_probe.py. Normalisation: (sigma-q)(sigma+q^-1)=0, [n]=(q^n-q^-n)/(q-q^-1); block's z=q^2/[2] IS z_D=q^3/(q^2+1) symbolically (no rescaling). Ocneanu weights solved from the Markov conditions on Hoefsmit seminormal irreps equal d_lambda/[2]^r for r=2,3,4 (all 3+-row weights 0). Torus braids (sigma_1..sigma_{r-1})^s traced directly: printed form sum_{lambda|-r} d_lambda q^{c s} holds ONLY for r=2, s even (links); 'add the -q^-1 sign' fixes r=2 but fails at r=3 -- the sign was not the only defect (wrong index set: all partitions vs hooks; wrong exponent c*s vs 2cs/r). Verified form, every coprime (r,s) tested at r=2,3,4: [2]^r tr_M(gamma^s) = sum_hooks (-1)^j d theta^{s/r} = [r+1] q^{s(r-1)} - [r-1] q^{s(r-3)}, theta=q^{2c} (full twist checked at s=r). Unknot-normalised [2]^{r-1} q^{-2e} tr_M = Jones at t=q^-2 (trefoil). Block (iii) rewritten to this. (ii): 'every diagonal form compatible with tr_M(1)=1 is a scalar multiple' is FALSE (one free entry per two-row class); restated as form = [2]^r tr_M(p_lambda p_mu), unique because the Markov trace is unique given z. NOT DONE: Lean carrier QOU/Archimedean/rj_canonical_inner_product.lean still has fields claim_unique_up_to_scalar (false as stated) and jonesPoly_eq_eval (old wrong RJ shape) -- a self-assuming context with a false field; needs a Lean follow-up (slv0 is completed and predates this). .qa.json sidecar now stale. Closeable for the .md once merged; the Lean carrier is the remaining work.
