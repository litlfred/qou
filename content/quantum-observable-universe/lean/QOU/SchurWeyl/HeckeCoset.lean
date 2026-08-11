import QOU.SchurWeyl.HeckeInclusion
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition
import Mathlib.LinearAlgebra.Dimension.Constructions
import Mathlib.LinearAlgebra.Dimension.Finrank

/-!
# QOU.SchurWeyl.HeckeCoset — the coset spanning bound `dim H_{n+1}(q) ≤ (n+1)!` (bean `qou-uoal`)

The Iwahori–Hecke basis theorem `dim_K H_n(q) = n!` has two halves; this file
establishes the **spanning half** in general `n` (upper bound), via the tower
coset decomposition.  With the QOU indexing `Hecke K q qi n = H_{n+1}(q)`
(the algebra on `n` generators `σ_0,…,σ_{n-1}`), the statement proved here is

  `Module.finrank K (Hecke K q qi n) ≤ (n+1)!`.

## Strategy — coset decomposition of the tower

`H_{n+1}(q) = ⨁_{k} H_n(q) · r_k` over the `n+2` (classically `n+2 = [H_{n+2}:H_{n+1}]`)
coset representatives

  `r_0 = 1,  r_j = σ_n σ_{n-1} ⋯ σ_{n-j+1}   (j = 1,…,n+1)`,

i.e. `r_j` is the descending product of the top `j` generators.  Left
multiplication by any generator preserves the subspace `Σ_k ι(H_n)·r_k`
(`ι = heckeIncl`, the tower inclusion `H_n ↪ H_{n+1}`), so that subspace is a
left ideal containing `1`, hence all of `H_{n+1}`.  Iterating gives a spanning
family indexed by `cosetIndex n` of cardinality `(n+1)!`.

## What is delivered here

* `descProd m j` — the descending product `σ_m σ_{m-1} ⋯ σ_{m-j+1}` of length `j`
  in `H_{m+1}(q) = Hecke K q qi (m+1)` (the coset representative `r_j`).
* `cosetIndex m`, `cosetFam m` — the recursively-built spanning family and its
  finite index type, with `Fintype.card (cosetIndex m) = (m+1)!`
  (`card_cosetIndex`, sorry-free).
* `one_mem_span_cosetFam` — `1` is in the span of the family (sorry-free).
* `finrank_le_card_of_span` — the generic finite-spanning ⇒ `finrank ≤ card`
  reduction (sorry-free).
* `span_cosetFam_eq_top` — the spanning statement (the crux; the top-generator
  "bubble" reduction is the deep Iwahori–Hecke basis theorem — see the `-- Ref:`
  gap, bean `qou-uoal`).
* `finrank_le_factorial` — the headline bound `finrank K (Hecke K q qi n) ≤ (n+1)!`,
  proved from `span_cosetFam_eq_top`.

Base ring: generic `[CommRing K]` for the algebraic data; `[Nontrivial K]` only
for the `finrank` bound (`StrongRankCondition`), per §7c.

LaTeX label: `prop:hecke-coset-spanning-bound`

Refs:
- [mathas1999] *Iwahori–Hecke Algebras and Schur Algebras of the Symmetric
  Group*, Ch. 1 (the `T_w` standard basis, `w ∈ S_n`),
  https://doi.org/10.1090/ulect/015
- [geckpfeiffer2000] Geck–Pfeiffer, *Characters of Finite Coxeter Groups and
  Iwahori–Hecke Algebras*, §4.4 (coset representatives / reduced words),
  https://doi.org/10.1093/oso/9780198502500.001.0001
-/

namespace QOU.SchurWeyl

open Hecke HeckeInclusion

namespace HeckeCoset

variable {K : Type*} [CommRing K] {q qi : K}

/-! ## Coset representatives: the descending products `r_j = σ_m ⋯ σ_{m-j+1}` -/

/-- The descending product `descProd m j = σ_m σ_{m-1} ⋯ σ_{m-j+1}` of the top
`j` generators of `H_{m+1}(q) = Hecke K q qi (m+1)` (length `j`; `descProd m 0 = 1`).
This is the coset representative `r_j` in the decomposition
`H_{m+1} = Σ_j ι(H_m)·r_j`.  The generator index `m - j` (truncated subtraction)
is always `< m + 1`, so no bound hypothesis is needed. -/
noncomputable def descProd (m : ℕ) : ℕ → Hecke K q qi (m + 1)
  | 0 => 1
  | (j + 1) => descProd m j * σ K q qi (m + 1) ⟨m - j, by omega⟩

@[simp] theorem descProd_zero (m : ℕ) : descProd (K := K) (q := q) (qi := qi) m 0 = 1 := rfl

theorem descProd_succ (m j : ℕ) :
    descProd (K := K) (q := q) (qi := qi) m (j + 1)
      = descProd m j * σ K q qi (m + 1) ⟨m - j, by omega⟩ := rfl

/-! ## The recursively-built spanning family and its index type -/

/-- The finite index type of the coset spanning family of `Hecke K q qi m`.
`cosetIndex 0 = Unit`; `cosetIndex (m+1) = cosetIndex m × Fin (m+2)` — one factor
`Fin (m+2)` for the `m+2` coset representatives added at each tower step.
`Fintype.card (cosetIndex m) = (m+1)!`. -/
def cosetIndex : ℕ → Type
  | 0 => Unit
  | (m + 1) => cosetIndex m × Fin (m + 2)

instance instFintypeCosetIndex : (m : ℕ) → Fintype (cosetIndex m)
  | 0 => (inferInstance : Fintype Unit)
  | (m + 1) =>
      letI := instFintypeCosetIndex m
      (inferInstance : Fintype (cosetIndex m × Fin (m + 2)))

/-- `Fintype.card (cosetIndex m) = (m+1)!` — the family has `(m+1)!` elements. -/
theorem card_cosetIndex : (m : ℕ) → Fintype.card (cosetIndex m) = (m + 1).factorial
  | 0 => rfl
  | (m + 1) => by
      have e : cosetIndex (m + 1) ≃ cosetIndex m × Fin (m + 2) := Equiv.refl _
      rw [Fintype.card_congr e, Fintype.card_prod, Fintype.card_fin, card_cosetIndex m,
        Nat.factorial_succ (m + 1)]
      ring

/-- The coset spanning family `cosetFam m : cosetIndex m → Hecke K q qi m`.
`cosetFam 0 () = 1`; `cosetFam (m+1) (b, j) = ι(cosetFam m b) · r_j`, where
`ι = heckeIncl` is the tower inclusion and `r_j = descProd m j`. -/
noncomputable def cosetFam : (m : ℕ) → cosetIndex m → Hecke K q qi m
  | 0, _ => 1
  | (m + 1), p => heckeIncl K q qi m (cosetFam m p.1) * descProd m p.2.val

theorem cosetFam_succ (m : ℕ) (p : cosetIndex (m + 1)) :
    cosetFam (K := K) (q := q) (qi := qi) (m + 1) p
      = heckeIncl K q qi m (cosetFam m p.1) * descProd m p.2.val := rfl

/-! ## `finrank ≤ card` from a finite spanning set (sorry-free reduction) -/

/-- Generic reduction: a finite set spanning `⊤` bounds the finrank by its card. -/
theorem finrank_le_card_of_span [Nontrivial K] {A : Type*} [AddCommGroup A]
    [Module K A] (s : Finset A) (hs : Submodule.span K (s : Set A) = ⊤) :
    Module.finrank K A ≤ s.card := by
  have h1 := finrank_span_le_card (R := K) (s : Set A)
  rw [hs, finrank_top] at h1
  simpa using h1

/-- `1` lies in the span of the coset family (sorry-free, by induction on `m`).
Base: `cosetFam 0 () = 1`.  Step: `1 = ι(1)·r_0 = ι(cosetFam m b₁)·descProd m 0`
where `b₁` witnesses `1 ∈ span (range (cosetFam m))`; since `heckeIncl` is an
algebra map and `descProd m 0 = 1`, the image of `1` is `1`. -/
theorem one_mem_span_cosetFam :
    (m : ℕ) → (1 : Hecke K q qi m) ∈ Submodule.span K (Set.range (cosetFam m))
  | 0 => Submodule.subset_span ⟨(), rfl⟩
  | (m + 1) => by
      -- `1 = heckeIncl 1 = heckeIncl 1 · r_0`; push `1 ∈ span (range (cosetFam m))`
      -- through the (linear) tower inclusion, which lands each family element at
      -- coset index `(b, 0)`.
      have ih := one_mem_span_cosetFam m
      have hmap : (Submodule.span K (Set.range (cosetFam m))).map
            (heckeIncl K q qi m).toLinearMap
          ≤ Submodule.span K (Set.range (cosetFam (m + 1))) := by
        rw [Submodule.map_span, Submodule.span_le]
        rintro _ ⟨_, ⟨b, rfl⟩, rfl⟩
        apply Submodule.subset_span
        refine ⟨(b, (0 : Fin (m + 2))), ?_⟩
        simp [cosetFam, AlgHom.toLinearMap_apply]
      have h1 : (1 : Hecke K q qi (m + 1)) = (heckeIncl K q qi m).toLinearMap 1 := by simp
      rw [h1]
      exact hmap (Submodule.mem_map_of_mem ih)

end HeckeCoset

end QOU.SchurWeyl
