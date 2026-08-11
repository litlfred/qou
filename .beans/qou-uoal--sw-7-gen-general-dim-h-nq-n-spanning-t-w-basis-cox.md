---
# qou-uoal
title: 'SW-7-gen: general dim H_n(q) ≤ n! (spanning, T_w basis) — Coxeter/Matsumoto infra'
status: in-progress
type: task
priority: normal
created_at: 2026-08-11T00:33:45Z
updated_at: 2026-08-11T10:38:46Z
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



## Attempt findings (2026-08-11, end of long session — honest handoff)
Tried the coset-rep definition; two concrete lessons for the next (fresh) attempt:
1. **Do NOT define reps with modular indexing** (`σ ⟨(top-j)%(n+1), _⟩`) — the % hack compiles but makes the spanning proof unmanageable. Define r_k via clean Fin arithmetic or a `List.ofFn`/`Fin.foldr` over the descending generator indices, keeping the index bounds as real hypotheses, not mod.
2. **finrank bound is self-contained from spanning** — no separate Module.Finite lemma needed: an explicit finite spanning set S with span=⊤ gives `finrank K A ≤ S.card` via `finrank_span_le_card` + `finrank_top`. So the whole theorem reduces to the ONE spanning lemma + the arithmetic induction (n+1)·n!=(n+1)!.
3. Companion `Module.Finite K (Hecke K q qi n)` is a clean general result IF wanted: generators are integral (monic quadratic σ²−(q−qi)σ−qqi=0), finitely many ⇒ module-finite. BLOCKED this session only by the firewalled Mathlib search (leansearch/loogle 403) needed to name the 'finite-type + integral ⇒ Module.Finite' bridge lemma; a session with LSP exact? (or network) closes it fast.
Core spanning closure (σ-top bubble: σ_n·(H_n·r_k) ⊆ Σ H_n·r_k via quadratic+braid) remains the multi-day piece — the general form of HeckeDim3.gen_mul_mem.
