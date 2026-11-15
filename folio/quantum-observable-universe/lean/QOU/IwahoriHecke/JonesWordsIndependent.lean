import QOU.IwahoriHecke.MarkovTransfer
import QOU.SchurWeyl.HeckeRegularRep
import Mathlib.RingTheory.OrzechProperty
import Mathlib.LinearAlgebra.Dimension.StrongRankCondition

/-!
# QOU.IwahoriHecke.JonesWordsIndependent — the Jones normal words are a basis

`QOU.IwahoriHecke.JonesNormalForm` proves that the Jones normal words span (`adjoin_eq_level`)
and that there are at most `(n+1)!` of them (`card_words_le`); it leaves linear independence
open. This file closes it for the presented algebra `Pres N a b` of
`QOU.IwahoriHecke.MarkovTransfer`, for every quadratic relation of the form
`s² = (q − qi)·s + (q·qi)` over any nontrivial commutative ring `R`. That covers the balanced
convention D (`qi = q⁻¹`: `s² = (q − q⁻¹)s + 1`) and the unbalanced one (`qi = 1`:
`s² = (q − 1)s + q`).

* `presEquivHecke` — `Pres N (q − qi) (q·qi) ≃ₐ[R] H_{N+1}(q)` (the `QOU.SchurWeyl.Hecke`
  algebra), generator to generator: both are presented by the same relations.
* `card_words_pres` — the normal words of `Pres N …` at level `N` are exactly `(N+1)!`
  distinct elements (so no two normal words coincide).
* `words_pres_linearIndependent` — they are linearly independent, hence
  (`wordsBasis`) a basis of `Pres N …`. Also at every level `n ≤ N`
  (`words_pres_linearIndependent_of_le`), because the words of level `n` are among those of
  level `N`.

## Proof

`H_{N+1}(q)` is free on the `T_w` over any commutative ring
(`QOU.SchurWeyl.HeckeCoset.stdBasisAny`, the regular representation), so `Pres N …` is free of
rank `(N+1)!`. The words span, so `R^{words} → R^{(N+1)!}` is onto; a nontrivial commutative
ring has the rank condition, so `|words| ≥ (N+1)!`, and with `card_words_le` equality holds.
Then `R^{words} → Pres → R^{(N+1)!} ≅ R^{words}` is a surjective endomorphism of a finite free
module, hence injective (Orzech/Vasconcelos: `OrzechProperty`, which holds for every
commutative ring).

Sorry-free; generic `[CommRing R] [Nontrivial R]` (§7c), nothing archimedean.
-/

namespace QOU.IwahoriHecke.JonesNormalForm

open QOU.SchurWeyl

variable {R : Type*} [CommRing R] (q qi : R) (N : ℕ)

/-- The generators of `H_{N+1}(q)`, ℕ-indexed (`0` from `N` on). -/
noncomputable def hgen (i : ℕ) : Hecke R q qi N :=
  if h : i < N then Hecke.σ R q qi N ⟨i, h⟩ else 0

theorem hgen_of_lt {i : ℕ} (h : i < N) : hgen q qi N i = Hecke.σ R q qi N ⟨i, h⟩ := by
  simp [hgen, h]

theorem hecke_heckeFamily : HeckeFamily N (q - qi) (q * qi) (hgen q qi N) where
  quad i hi := by rw [hgen_of_lt q qi N hi]; exact Hecke.σ_quadratic R q qi N ⟨i, hi⟩
  braid i hi := by
    rw [hgen_of_lt q qi N (show i < N by omega), hgen_of_lt q qi N hi]
    exact Hecke.σ_braid R q qi N ⟨i, by omega⟩ hi
  comm i j hij hj := by
    rw [hgen_of_lt q qi N (show i < N by omega), hgen_of_lt q qi N hj]
    exact (Hecke.σ_commute R q qi N ⟨j, hj⟩ ⟨i, by omega⟩ hij).symm

/-- `H_{N+1}(q) → Pres`, generator to generator. -/
noncomputable def heckeToPres : Hecke R q qi N →ₐ[R] Pres N (q - qi) (q * qi) :=
  Hecke.lift R q qi N (fun i => pgen N (q - qi) (q * qi) i)
    (fun i => (pres_heckeFamily N (q - qi) (q * qi)).quad i i.isLt)
    (fun i hi => (pres_heckeFamily N (q - qi) (q * qi)).braid i hi)
    (fun i j hij => ((pres_heckeFamily N (q - qi) (q * qi)).comm j i hij i.isLt).symm)

theorem heckeToPres_σ (i : Fin N) :
    heckeToPres q qi N (Hecke.σ R q qi N i) = pgen N (q - qi) (q * qi) i := by
  simp [heckeToPres]

/-- **The presented algebra is the Hecke algebra.** -/
noncomputable def presEquivHecke : Pres N (q - qi) (q * qi) ≃ₐ[R] Hecke R q qi N :=
  AlgEquiv.ofAlgHom (lift (hecke_heckeFamily q qi N)) (heckeToPres q qi N)
    (Hecke.hom_ext R q qi N fun i => by
      rw [AlgHom.comp_apply, heckeToPres_σ, lift_pgen _ i.isLt, hgen_of_lt q qi N i.isLt,
        AlgHom.id_apply])
    (AlgHom.ext_of_adjoin_eq_top (adjoin_pgen_eq_top N (q - qi) (q * qi)) (by
      rintro _ ⟨i, hi, rfl⟩
      have hi' : i < N := hi
      rw [AlgHom.comp_apply, lift_pgen _ hi', hgen_of_lt q qi N hi',
        show (⟨i, hi'⟩ : Fin N) = ⟨i, hi'⟩ from rfl, heckeToPres_σ, AlgHom.id_apply]))

theorem presEquivHecke_pgen {i : ℕ} (hi : i < N) :
    presEquivHecke q qi N (pgen N (q - qi) (q * qi) i) = Hecke.σ R q qi N ⟨i, hi⟩ := by
  show lift (hecke_heckeFamily q qi N) _ = _
  rw [lift_pgen _ hi, hgen_of_lt q qi N hi]

/-- `Pres N (q − qi) (q·qi)` is free with a basis indexed by `S_{N+1}`. -/
noncomputable def presBasis :
    Module.Basis (Equiv.Perm (Fin (N + 1))) R (Pres N (q - qi) (q * qi)) :=
  (HeckeCoset.stdBasisAny q qi N).map (presEquivHecke q qi N).toLinearEquiv.symm

/-- The level-`N` normal words. -/
noncomputable abbrev presWords : Finset (Pres N (q - qi) (q * qi)) :=
  words (pgen N (q - qi) (q * qi)) N

theorem span_presWords : Submodule.span R (presWords q qi N : Set (Pres N (q - qi) (q * qi)))
    = ⊤ := by
  have h := adjoin_eq_level (pres_heckeFamily N (q - qi) (q * qi)) (le_refl N)
  rw [adjoin_pgen_eq_top] at h
  rw [← Algebra.top_toSubmodule, h]
  rfl

/-- The coordinate map `R^{words} → Pres`. -/
noncomputable def wordsMap :
    (presWords q qi N → R) →ₗ[R] Pres N (q - qi) (q * qi) :=
  Fintype.linearCombination R (fun w : presWords q qi N => (w : Pres N (q - qi) (q * qi)))

theorem wordsMap_surjective : Function.Surjective (wordsMap q qi N) := by
  rw [← LinearMap.range_eq_top, wordsMap, Fintype.range_linearCombination, Subtype.range_coe_subtype]
  exact span_presWords q qi N

variable [Nontrivial R]

/-- **There are exactly `(N+1)!` distinct normal words.** -/
theorem card_words_pres : (presWords q qi N).card = (N + 1).factorial := by
  refine le_antisymm (card_words_le _ N) ?_
  have h := card_le_of_surjective R
    ((presBasis q qi N).equivFun.toLinearMap ∘ₗ wordsMap q qi N)
    ((presBasis q qi N).equivFun.surjective.comp (wordsMap_surjective q qi N))
  simpa [Fintype.card_perm, Fintype.card_fin] using h

/-- **The Jones normal words are linearly independent** in `Pres N (q − qi) (q·qi)`, over any
nontrivial commutative ring. -/
theorem words_pres_linearIndependent :
    LinearIndependent R (fun w : presWords q qi N => (w : Pres N (q - qi) (q * qi))) := by
  classical
  have hcard : Fintype.card (Equiv.Perm (Fin (N + 1))) = Fintype.card (presWords q qi N) := by
    rw [Fintype.card_perm, Fintype.card_fin, Fintype.card_coe, card_words_pres]
  let e : Equiv.Perm (Fin (N + 1)) ≃ presWords q qi N := Fintype.equivOfCardEq hcard
  let g : (presWords q qi N → R) →ₗ[R] (presWords q qi N → R) :=
    (LinearEquiv.funCongrLeft R R e.symm).toLinearMap ∘ₗ
      (presBasis q qi N).equivFun.toLinearMap ∘ₗ wordsMap q qi N
  have hg : Function.Surjective g :=
    (LinearEquiv.funCongrLeft R R e.symm).surjective.comp
      ((presBasis q qi N).equivFun.surjective.comp (wordsMap_surjective q qi N))
  have hinj : Function.Injective (wordsMap q qi N) := by
    have := OrzechProperty.injective_of_surjective_endomorphism g hg
    exact Function.Injective.of_comp (f := fun x =>
      (LinearEquiv.funCongrLeft R R e.symm) ((presBasis q qi N).equivFun x)) this
  rw [linearIndependent_iff_injective_fintypeLinearCombination]
  exact hinj

/-- **The Jones normal words form a basis** of `Pres N (q − qi) (q·qi)`. -/
noncomputable def wordsBasis : Module.Basis (presWords q qi N) R (Pres N (q - qi) (q * qi)) :=
  Module.Basis.mk (words_pres_linearIndependent q qi N) (by
    convert (span_presWords q qi N).ge using 2
    ext x; simp)

/-- The level-`n` words are among the level-`n+1` words (the empty run `j = n+1`). -/
theorem words_subset_succ {A : Type*} [Ring A] (s : ℕ → A) (n : ℕ) :
    words s n ⊆ words s (n + 1) := by
  classical
  intro x hx
  rw [words]
  refine Finset.mem_image₂.mpr ⟨x, hx, 1, Finset.mem_image.mpr ⟨n + 1, by simp, ?_⟩, mul_one x⟩
  simp

theorem words_subset_of_le {A : Type*} [Ring A] (s : ℕ → A) {n m : ℕ} (h : n ≤ m) :
    words s n ⊆ words s m := by
  induction h with
  | refl => exact Finset.Subset.refl _
  | step _ ih => exact ih.trans (words_subset_succ s _)

/-- **The normal words of every level `n ≤ N` are linearly independent** in `Pres N …`. -/
theorem words_pres_linearIndependent_of_le {n : ℕ} (hn : n ≤ N) :
    LinearIndependent R (fun w : words (pgen N (q - qi) (q * qi)) n =>
      (w : Pres N (q - qi) (q * qi))) := by
  have h := (words_pres_linearIndependent q qi N).comp
    (fun w : words (pgen N (q - qi) (q * qi)) n =>
      (⟨w.1, words_subset_of_le _ hn w.2⟩ : presWords q qi N))
    (fun a b hab => by simpa [Subtype.ext_iff] using hab)
  exact h

end QOU.IwahoriHecke.JonesNormalForm
