---
# qou-uoal
title: 'SW-7-gen: general dim H_n(q) ≤ n! (spanning, T_w basis) — Coxeter/Matsumoto infra'
status: completed
type: task
priority: normal
created_at: 2026-08-11T00:33:45Z
updated_at: 2026-08-18T16:06:15Z
parent: qou-59vq
---

Spanning half of the Iwahori–Hecke basis theorem dim H_n(q) = n! for general n: H_n(q) is spanned by {T_w : w ∈ S_n} (n! reduced words).

## Mathlib assessment (2026-08-11)
Foundations PRESENT: Mathlib.GroupTheory.Coxeter.{Basic,Length,Inversion,Matrix} — CoxeterSystem, length, IsReduced, inversions/exchange. ABSENT: Matsumoto's theorem (reduced-word independence / T_w well-definedness), any Hecke algebra, the T_w basis.

## Route (multi-day)
1. Symmetric group as CoxeterSystem (check Mathlib instance).
2. Per w ∈ S_n choose reduced word; define T_w ∈ Hecke (product of σ's).
3. Span-closure induction on length: T_s·T_w = T_{sw} (l up) or (q-q⁻¹)T_w + T_{sw} (l down) — the general form of the 12 reductions done concretely at n=3 in HeckeDim3.gen_mul_mem.
4. adjoin{σ_i}=⊤ (as HeckeDim3.adjoin_gens_eq_top) ⇒ span{T_w}=⊤ ⇒ dim ≤ n!.

The lower bound dim ≥ n! (independence) needs ALL irreps = general Hoefsmit (qou-im9l). n=3 fully done (dim=6, PR #4963); this bean is the general-n spanning generalization.



## Mathlib API footing (lean-direct probe, 2026-08-11)
PRESENT in Mathlib.GroupTheory.Coxeter.{Length,Inversion}: CoxeterSystem.wordProd (List B → W), .length (W → ℕ), .IsReduced, .exists_reduced_word (∀ w, ∃ reduced ω, w = wordProd ω). So the reduced-word/length machinery EXISTS given a CoxeterSystem instance.
MISSING: (a) the symmetric group Equiv.Perm (Fin n) wired as a CoxeterSystem instance (not found — likely must be built or use CoxeterMatrix Aₙ + the standard-gen isomorphism); (b) repo-side: a map Coxeter-word → Hecke element (product of σ's) + the span-closure induction on length (T_s·T_w = T_{sw} if l↑ else (q-q⁻¹)T_w + T_{sw}) — the general form of HeckeDim3.gen_mul_mem's 12 concrete reductions. NOTE: the SPANNING bound (dim≤n!) does NOT need Matsumoto/well-definedness — only that ≤|W| generator-products span. Matsumoto is needed only for the exact T_w BASIS (dim=n! both ways).



## Landed on PR #4978 (2026-08-11, sorry-free, generic [CommRing K])
- heckeIncl : Hecke K q qi n →ₐ[K] Hecke K q qi (n+1) (σ_i↦σ_i, Fin.castSucc) + heckeIncl_σ — the tower inclusion (HeckeInclusion.lean).
- adjoin_range_σ_eq_top : Algebra.adjoin K (range σ) = ⊤ for all n (general form of HeckeDim3.adjoin_gens_eq_top).

## Remaining CORE (multi-day, next agent picks up):
1. Coset reps r_k = σ_{n-1}σ_{n-2}⋯σ_k (k=0..n-1) + r_n=1 ⇒ n+1 elements, as a Fin (n+1) → Hecke family.
2. **Coset-spanning lemma** span_K (⋃_r range(heckeIncl)·r) = ⊤ — the crux. Right-mult-closure of the H_{n-1}-module span of {r_k} under each σ_i, via the quadratic + braid 'bubble' argument (moving σ_{n-1} rightward). General form of HeckeDim3.gen_mul_mem.
3. finrank recursion: finrank H_n ≤ (n+1)·finrank H_{n-1} (spanning set = {incl(b)·r_k : b∈basis H_{n-1}, k}) ⇒ finrank H_n(q) ≤ (n+1)! by induction (base n=0: H_0 = K, finrank 1).
Note (n+1)! because Hecke ... n = classical H_{n+1} (n generators, n+1 strands). Lower bound dim≥(n+1)! needs general Hoefsmit (qou-im9l).



## CLOSED (verified 2026-08-18 by the originating session)
finrank_le_factorial : Module.finrank K (Hecke K q qi n) ≤ (n+1)! is SORRY-FREE on main (HeckeCoset.lean, 441 lines). Verified lean-direct exit 0 + #print axioms -> [propext, Classical.choice, Quot.sound] (no sorryAx) for finrank_le_factorial, span_cosetFam_eq_top, span_mul_gen_mem.
KEY: the closure came via RIGHT-multiplication (span_mul_gen_mem + descProd_mul_σ_of_{add_lt,add_eq,add_eq_succ,le_add}) rather than the left-mult framing this bean originally scoped — r_j·σ_i reductions are tractable where σ_i·r_j was not. Child gap qou-j6f9 also completed. The general spanning half of the Iwahori-Hecke basis theorem is DONE.
