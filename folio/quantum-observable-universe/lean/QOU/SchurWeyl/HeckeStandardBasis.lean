import QOU.SchurWeyl.SymmetrisingTraceZeroParam

/-!
# QOU.SchurWeyl.HeckeStandardBasis — the coset family indexed by permutations, and `τ(T_w) = δ_{w,1}`

`HeckeCoset.cosetFam m : cosetIndex m → Hecke K q qi m` is the coset spanning family of
`H_{m+1}(q)`, indexed abstractly by `cosetIndex m` (`(m+1)!` elements).  This file indexes it by
**permutations** `w ∈ S_{m+1} = Perm (Fin (m+1))`, so that it becomes the standard family `T_w`,
and restates the symmetrising-trace theorem as `τ(T_w) = δ_{w,1}`.

## The dictionary

* `adjT i = (i  i+1)` — the adjacent transposition matching the generator `σ_i`.
* `permIncl m : S_{m+1} →* S_{m+2}` — the inclusion fixing the last point, matching `heckeIncl`
  (`permIncl_adjT`).
* `cosetWord m p : List (Fin m)` — the word of generators whose product is `cosetFam m p`
  (`cosetFam_eq_prod_word`), of length `cosetLen m p` (`cosetWord_length`).
* `permOf m p` — the product of the same word in `S_{m+1}` (`permOf_eq_prod_word`).

`permOf m` is a **bijection** `cosetIndex m ≃ S_{m+1}` (`permOfEquiv`): injective by reading off
`w⁻¹(last)` (which fixes the top coset representative) and cancelling, then bijective by counting.

So `T_w := cosetFam m (permOfEquiv.symm w)` (`stdElt`) is the product of `σ` along a word whose
image in `S_{m+1}` is `w` (`stdElt_eq_prod_word`, `stdWord_prod_eq`).

## The trace

`MarkovTraceFamily.tr_stdElt_of_zero`: a Markov trace with `z = 0` satisfies

```
T.tr m (T_w) = if w = 1 then 1 else 0.
```

## Reduced words

`stdWord m w` is a **reduced** word for `w`: its length is the inversion number `ninv w`
(`stdWord_length`), and every word for `w` has length `≥ ninv w` (`ninv_le_length`), so no word
for `w` is shorter (`stdWord_reduced`).  The ingredients are `ninv (w s_i) = ninv w + 1` at an
ascent (`ninv_mul_adjT_of_lt`), `permIncl` preserving `ninv`, and each coset-representative letter
being an ascent.

## Scope

`T_w` is the product along this particular reduced word.  That every reduced word for `w` gives
the same product (Matsumoto's theorem) is not reproved here; it is not needed for the trace
statement, which is about this family.

## Base ring (§7c)

Generic `[CommRing K]`.

LaTeX label: `thm:hecke-standard-basis-symmetrising`

-- Ref: [mathas1999] https://doi.org/10.1090/ulect/015 (Ch. 1: the `T_w` basis; coset words)
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion Equiv

variable {K : Type*} [CommRing K] {q qi : K}

/-! ## Permutation side -/

/-- The adjacent transposition `(i  i+1)` of `Fin (n+1)`, the image of the generator `σ_i`. -/
def adjT {n : ℕ} (i : Fin n) : Perm (Fin (n + 1)) := swap i.castSucc i.succ

/-- The inclusion `S_{m+1} ↪ S_{m+2}` fixing the last point. -/
def permIncl (m : ℕ) : Perm (Fin (m + 1)) →* Perm (Fin (m + 2)) :=
  Perm.extendDomainHom (finSuccAboveEquiv (Fin.last (m + 1)))

theorem permIncl_injective (m : ℕ) : Function.Injective (permIncl m) :=
  Perm.extendDomainHom_injective _

theorem permIncl_apply_castSucc (m : ℕ) (w : Perm (Fin (m + 1))) (x : Fin (m + 1)) :
    permIncl m w x.castSucc = (w x).castSucc := by
  have h := Perm.extendDomain_apply_image w (finSuccAboveEquiv (Fin.last (m + 1))) x
  simpa [permIncl, finSuccAboveEquiv_apply, Fin.succAbove_last] using h

theorem permIncl_apply_last (m : ℕ) (w : Perm (Fin (m + 1))) :
    permIncl m w (Fin.last (m + 1)) = Fin.last (m + 1) :=
  Perm.extendDomain_apply_not_subtype w _ (by simp)

theorem permIncl_adjT (m : ℕ) (i : Fin m) : permIncl m (adjT i) = adjT i.castSucc := by
  ext x
  refine Fin.lastCases ?_ (fun y => ?_) x
  · rw [permIncl_apply_last, adjT, swap_apply_of_ne_of_ne]
    · rw [Ne, Fin.ext_iff]; simp; omega
    · rw [Ne, Fin.ext_iff]; simp; omega
  · rw [permIncl_apply_castSucc, adjT, adjT, (Fin.castSucc_injective _).map_swap, Fin.succ_castSucc]

/-- The descending cycle `s_m s_{m−1} ⋯ s_{m−j+1}` in `S_{m+2}`, the image of `descProd m j`. -/
def descPerm (m : ℕ) : ℕ → Perm (Fin (m + 2))
  | 0 => 1
  | (j + 1) => descPerm m j * adjT (⟨m - j, by omega⟩ : Fin (m + 1))

/-- `descPerm m j` sends the point `m + 1 − j` to the last point. -/
theorem descPerm_apply (m : ℕ) : ∀ (j : ℕ) (hj : j ≤ m + 1),
    descPerm m j ⟨m + 1 - j, by omega⟩ = Fin.last (m + 1)
  | 0, _ => by
      show (⟨m + 1 - 0, _⟩ : Fin (m + 2)) = Fin.last (m + 1)
      exact Fin.ext (by simp)
  | (j + 1), hj => by
      have h1 : (⟨m + 1 - (j + 1), by omega⟩ : Fin (m + 2))
          = (⟨m - j, by omega⟩ : Fin (m + 1)).castSucc := Fin.ext (by simp)
      have h2 : (⟨m - j, by omega⟩ : Fin (m + 1)).succ = ⟨m + 1 - j, by omega⟩ :=
        Fin.ext (by simp; omega)
      rw [descPerm, Perm.mul_apply, h1, adjT, swap_apply_left, h2]
      exact descPerm_apply m j (by omega)

/-- The permutation indexed by a coset-family index. -/
def permOf : (m : ℕ) → cosetIndex m → Perm (Fin (m + 1))
  | 0, _ => 1
  | (m + 1), p => permIncl m (permOf m p.1) * descPerm m p.2.val

theorem permOf_succ (m : ℕ) (p : cosetIndex (m + 1)) :
    permOf (m + 1) p = permIncl m (permOf m p.1) * descPerm m p.2.val := rfl

/-- `w⁻¹(last)` reads off the top coset representative. -/
theorem permOf_inv_last (m : ℕ) (b : cosetIndex m) (j : Fin (m + 2)) :
    (permOf (m + 1) (b, j))⁻¹ (Fin.last (m + 1)) = ⟨m + 1 - j.val, by omega⟩ := by
  rw [Perm.inv_eq_iff_eq, permOf_succ, Perm.mul_apply, descPerm_apply m j.val (by omega),
    permIncl_apply_last]

theorem permOf_injective : ∀ m : ℕ, Function.Injective (permOf m)
  | 0 => fun _ _ _ => rfl
  | (m + 1) => by
      rintro ⟨a, j⟩ ⟨b, k⟩ h
      have hj := permOf_inv_last m a j
      rw [h, permOf_inv_last m b k] at hj
      have hjk : j = k := by
        have := congrArg Fin.val hj
        simp only at this
        exact Fin.ext (by have := j.isLt; have := k.isLt; omega)
      subst hjk
      rw [permOf_succ, permOf_succ] at h
      have hab := permOf_injective m (permIncl_injective m (mul_right_cancel h))
      simp only at hab
      rw [hab]

theorem permOf_bijective (m : ℕ) : Function.Bijective (permOf m) :=
  (Fintype.bijective_iff_injective_and_card _).mpr
    ⟨permOf_injective m, by rw [card_cosetIndex, Fintype.card_perm, Fintype.card_fin]⟩

/-- **The coset family is indexed by `S_{m+1}`.** -/
noncomputable def permOfEquiv (m : ℕ) : cosetIndex m ≃ Perm (Fin (m + 1)) :=
  Equiv.ofBijective _ (permOf_bijective m)

theorem permOf_cosetOne : ∀ m : ℕ, permOf m (cosetOne m) = 1
  | 0 => rfl
  | (m + 1) => by
      show permIncl m (permOf m (cosetOne m)) * descPerm m 0 = 1
      rw [permOf_cosetOne m, map_one]
      rfl

theorem permOf_eq_one_iff (m : ℕ) (p : cosetIndex m) : permOf m p = 1 ↔ p = cosetOne m := by
  rw [← permOf_cosetOne m]
  exact (permOf_injective m).eq_iff

/-! ## Words -/

/-- The word `[m, m−1, …, m−j+1]` of `descProd m j`. -/
def descWord (m : ℕ) : ℕ → List (Fin (m + 1))
  | 0 => []
  | (j + 1) => descWord m j ++ [⟨m - j, by omega⟩]

/-- The generator word of `cosetFam m p`. -/
def cosetWord : (m : ℕ) → cosetIndex m → List (Fin m)
  | 0, _ => []
  | (m + 1), p => (cosetWord m p.1).map Fin.castSucc ++ descWord m p.2.val

theorem descWord_length (m : ℕ) : ∀ j, (descWord m j).length = j
  | 0 => rfl
  | (j + 1) => by simp [descWord, descWord_length m j]

theorem cosetWord_length : ∀ (m : ℕ) (p : cosetIndex m), (cosetWord m p).length = cosetLen m p
  | 0, _ => rfl
  | (m + 1), p => by
      simp [cosetWord, cosetLen_succ, descWord_length, cosetWord_length m p.1]

theorem descProd_eq_prod_word (m : ℕ) : ∀ j,
    descProd (K := K) (q := q) (qi := qi) m j = ((descWord m j).map (σ K q qi (m + 1))).prod
  | 0 => rfl
  | (j + 1) => by simp [descProd_succ, descWord, descProd_eq_prod_word m j]

theorem descPerm_eq_prod_word (m : ℕ) : ∀ j, descPerm m j = ((descWord m j).map adjT).prod
  | 0 => rfl
  | (j + 1) => by simp [descPerm, descWord, descPerm_eq_prod_word m j]

/-- `cosetFam m p` is the product of the generators along `cosetWord m p`. -/
theorem cosetFam_eq_prod_word : ∀ (m : ℕ) (p : cosetIndex m),
    cosetFam (K := K) (q := q) (qi := qi) m p = ((cosetWord m p).map (σ K q qi m)).prod
  | 0, _ => rfl
  | (m + 1), p => by
      rw [cosetFam_succ, cosetFam_eq_prod_word m p.1, descProd_eq_prod_word, cosetWord,
        List.map_append, List.prod_append, map_list_prod, List.map_map, List.map_map]
      congr 3
      funext i
      simp [heckeIncl_σ]

/-- `permOf m p` is the product of the transpositions along the same word. -/
theorem permOf_eq_prod_word : ∀ (m : ℕ) (p : cosetIndex m),
    permOf m p = ((cosetWord m p).map adjT).prod
  | 0, _ => rfl
  | (m + 1), p => by
      rw [permOf_succ, permOf_eq_prod_word m p.1, descPerm_eq_prod_word, cosetWord,
        List.map_append, List.prod_append, map_list_prod, List.map_map, List.map_map]
      congr 3
      funext i
      simp [permIncl_adjT]

/-! ## The standard family `T_w` and the symmetrising trace -/

/-- The word attached to `w ∈ S_{m+1}`. -/
noncomputable def stdWord (m : ℕ) (w : Perm (Fin (m + 1))) : List (Fin m) :=
  cosetWord m ((permOfEquiv m).symm w)

/-- `T_w`, the product of the generators along `stdWord m w`. -/
noncomputable def stdElt (m : ℕ) (w : Perm (Fin (m + 1))) : Hecke K q qi m :=
  cosetFam m ((permOfEquiv m).symm w)

theorem stdElt_eq_prod_word (m : ℕ) (w : Perm (Fin (m + 1))) :
    stdElt (K := K) (q := q) (qi := qi) m w = ((stdWord m w).map (σ K q qi m)).prod :=
  cosetFam_eq_prod_word m _

/-- The word of `T_w` multiplies out to `w` in `S_{m+1}`. -/
theorem stdWord_prod_eq (m : ℕ) (w : Perm (Fin (m + 1))) : ((stdWord m w).map adjT).prod = w := by
  rw [stdWord, ← permOf_eq_prod_word]
  exact (permOfEquiv m).apply_symm_apply w

theorem stdElt_one (m : ℕ) : stdElt (K := K) (q := q) (qi := qi) m 1 = 1 := by
  have h : (permOfEquiv m).symm 1 = cosetOne m :=
    (permOfEquiv m).symm_apply_eq.mpr (permOf_cosetOne m).symm
  rw [stdElt, h, cosetFam_cosetOne]

/-- **`τ(T_w) = δ_{w,1}`**: a Markov trace with parameter `z = 0` is `1` on `T_1 = 1` and `0` on
every other `T_w`. -/
theorem MarkovTraceFamily.tr_stdElt_of_zero (T : MarkovTraceFamily K q qi 0) (m : ℕ)
    (w : Perm (Fin (m + 1))) :
    T.tr m (stdElt (K := K) (q := q) (qi := qi) m w) = if w = 1 then 1 else 0 := by
  rw [stdElt, T.tr_cosetFam_of_zero]
  refine if_congr ?_ rfl rfl
  rw [cosetLen_eq_zero_iff, ← permOf_eq_one_iff]
  show permOfEquiv m ((permOfEquiv m).symm w) = 1 ↔ w = 1
  rw [(permOfEquiv m).apply_symm_apply]

/-! ## The coset words are reduced -/

/-- The **inversion number** `#{(x, y) : x < y, w y < w x}`. -/
def ninv {n : ℕ} (w : Perm (Fin n)) : ℕ :=
  ((Finset.univ : Finset (Fin n × Fin n)).filter (fun p => p.1 < p.2 ∧ w p.2 < w p.1)).card

theorem ninv_one {n : ℕ} : ninv (1 : Perm (Fin n)) = 0 := by
  rw [ninv, Finset.card_eq_zero, Finset.filter_eq_empty_iff]
  rintro ⟨x, y⟩ _ ⟨h1, h2⟩
  simp only [Perm.one_apply] at h2
  exact absurd (h1.trans h2) (lt_irrefl _)

/-- An adjacent transposition preserves the order of every pair except `{i, i+1}`. -/
theorem adjT_lt_iff {n : ℕ} (i : Fin n) (x y : Fin (n + 1))
    (h1 : ¬(x = i.castSucc ∧ y = i.succ)) (h2 : ¬(x = i.succ ∧ y = i.castSucc)) :
    x < y ↔ adjT i x < adjT i y := by
  simp only [adjT, swap_apply_def]
  simp only [Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ, not_and] at h1 h2
  split_ifs with ha hb hc hd he hf hg hh <;>
    simp only [Fin.lt_iff_val_lt_val, Fin.ext_iff, Fin.coe_castSucc, Fin.val_succ] at * <;> omega

/-- **An ascent adds one inversion**: if `w(i) < w(i+1)` then `ninv (w s_i) = ninv w + 1`. -/
theorem ninv_mul_adjT_of_lt {n : ℕ} (w : Perm (Fin (n + 1))) (i : Fin n)
    (h : w i.castSucc < w i.succ) : ninv (w * adjT i) = ninv w + 1 := by
  set a := i.castSucc
  set b := i.succ
  have hab : a < b := Fin.castSucc_lt_succ i
  have hsa : adjT i a = b := swap_apply_left _ _
  have hsb : adjT i b = a := swap_apply_right _ _
  have hiff : ∀ p : Fin (n + 1) × Fin (n + 1),
      (p.1 < p.2 ∧ (w * adjT i) p.2 < (w * adjT i) p.1)
        ↔ (p = (a, b) ∨ (adjT i p.1 < adjT i p.2 ∧ w (adjT i p.2) < w (adjT i p.1))) := by
    rintro ⟨x, y⟩
    simp only [Perm.mul_apply, Prod.mk.injEq]
    by_cases hxy : x = a ∧ y = b
    · obtain ⟨rfl, rfl⟩ := hxy
      rw [hsa, hsb]
      exact ⟨fun _ => Or.inl ⟨rfl, rfl⟩, fun _ => ⟨hab, h⟩⟩
    by_cases hyx : x = b ∧ y = a
    · obtain ⟨rfl, rfl⟩ := hyx
      rw [hsa, hsb]
      constructor
      · rintro ⟨h', _⟩; exact absurd (h'.trans hab) (lt_irrefl _)
      · rintro (⟨h', _⟩ | ⟨_, h'⟩)
        · exact absurd h' (ne_of_gt hab)
        · exact absurd (h.trans h') (lt_irrefl _)
    rw [adjT_lt_iff i x y hxy hyx]
    exact ⟨fun hh => Or.inr hh, fun hh => hh.resolve_left hxy⟩
  have hnot : (a, b) ∉ (Finset.univ : Finset (Fin (n + 1) × Fin (n + 1))).filter
      (fun p => adjT i p.1 < adjT i p.2 ∧ w (adjT i p.2) < w (adjT i p.1)) := by
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, hsa, hsb, not_and]
    intro h'
    exact absurd (h'.trans hab) (lt_irrefl _)
  have hcard : ((Finset.univ : Finset (Fin (n + 1) × Fin (n + 1))).filter
      (fun p => adjT i p.1 < adjT i p.2 ∧ w (adjT i p.2) < w (adjT i p.1))).card = ninv w := by
    rw [ninv]
    refine Finset.card_bij' (fun p _ => (adjT i p.1, adjT i p.2))
      (fun p _ => (adjT i p.1, adjT i p.2)) ?_ ?_ ?_ ?_
    · intro p hp; simpa using hp
    · intro p hp
      simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hp ⊢
      simpa [adjT, swap_apply_self] using hp
    · intro p _; simp [adjT, swap_apply_self]
    · intro p _; simp [adjT, swap_apply_self]
  rw [ninv, Finset.filter_congr (fun p _ => hiff p), Finset.filter_or, Finset.filter_eq',
    if_pos (Finset.mem_univ _), Finset.singleton_union, Finset.card_insert_of_notMem hnot, hcard]

/-- `ninv (v s_i) ≤ ninv v + 1`. -/
theorem ninv_mul_adjT_le {n : ℕ} (v : Perm (Fin (n + 1))) (i : Fin n) :
    ninv (v * adjT i) ≤ ninv v + 1 := by
  rcases lt_or_gt_of_ne (v.injective.ne (Fin.castSucc_lt_succ i).ne) with h | h
  · exact (ninv_mul_adjT_of_lt v i h).le
  · have h' : (v * adjT i) i.castSucc < (v * adjT i) i.succ := by
      simpa [adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using h
    have e := ninv_mul_adjT_of_lt (v * adjT i) i h'
    have hs : adjT i * adjT i = 1 := swap_mul_self _ _
    rw [mul_assoc, hs, mul_one] at e
    omega

/-- Any word for `w` has length at least `ninv w`. -/
theorem ninv_le_length {n : ℕ} (u : List (Fin n)) :
    ninv ((u.map adjT).prod) ≤ u.length := by
  induction u using List.reverseRecOn with
  | nil => simp [ninv_one]
  | append_singleton u i ih =>
      rw [List.map_append, List.prod_append, List.map_singleton, List.prod_singleton,
        List.length_append, List.length_singleton]
      exact (ninv_mul_adjT_le _ i).trans (by omega)

/-- `permIncl` preserves the inversion number. -/
theorem ninv_permIncl (m : ℕ) (a : Perm (Fin (m + 1))) : ninv (permIncl m a) = ninv a := by
  symm
  rw [ninv, ninv]
  refine Finset.card_bij (fun p _ => (p.1.castSucc, p.2.castSucc)) ?_ ?_ ?_
  · intro p hp
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, permIncl_apply_castSucc,
      Fin.castSucc_lt_castSucc_iff] at hp ⊢
    exact hp
  · intro p _ p' _ h
    simp only [Prod.mk.injEq] at h
    exact Prod.ext (Fin.castSucc_injective _ h.1) (Fin.castSucc_injective _ h.2)
  · rintro ⟨x, y⟩ hp
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hp
    obtain ⟨hxy, hw⟩ := hp
    have hy : y ≠ Fin.last (m + 1) := by
      rintro rfl
      rw [permIncl_apply_last] at hw
      exact absurd hw (not_lt.mpr (Fin.le_last _))
    have hx : x ≠ Fin.last (m + 1) := fun hx => absurd (hx ▸ hxy) (not_lt.mpr (Fin.le_last _))
    obtain ⟨x', rfl⟩ := Fin.exists_castSucc_eq.mpr hx
    obtain ⟨y', rfl⟩ := Fin.exists_castSucc_eq.mpr hy
    refine ⟨(x', y'), ?_, rfl⟩
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, permIncl_apply_castSucc,
      Fin.castSucc_lt_castSucc_iff] at hxy hw ⊢
    exact ⟨hxy, hw⟩

theorem ninv_permIncl_mul_descPerm (m : ℕ) (a : Perm (Fin (m + 1))) :
    ∀ k, k ≤ m + 1 → ninv (permIncl m a * descPerm m k) = ninv a + k
  | 0, _ => by rw [descPerm, mul_one, ninv_permIncl, add_zero]
  | (k + 1), hk => by
      have ih := ninv_permIncl_mul_descPerm m a k (by omega)
      set w := permIncl m a * descPerm m k with hw
      have hlast : w ⟨m + 1 - k, by omega⟩ = Fin.last (m + 1) := by
        rw [hw, Perm.mul_apply, descPerm_apply m k (by omega), permIncl_apply_last]
      have hsucc : (⟨m - k, by omega⟩ : Fin (m + 1)).succ = ⟨m + 1 - k, by omega⟩ :=
        Fin.ext (by simp; omega)
      have hasc : w (⟨m - k, by omega⟩ : Fin (m + 1)).castSucc
          < w (⟨m - k, by omega⟩ : Fin (m + 1)).succ := by
        rw [hsucc, hlast]
        refine lt_of_le_of_ne (Fin.le_last _) fun h => ?_
        rw [← hlast] at h
        have := congrArg Fin.val (w.injective h)
        simp at this
        omega
      show ninv (w * adjT (⟨m - k, by omega⟩ : Fin (m + 1))) = ninv a + (k + 1)
      rw [ninv_mul_adjT_of_lt w _ hasc, ih]
      omega

/-- **The coset word of `p` has length `ninv (permOf p)`.** -/
theorem ninv_permOf : ∀ (m : ℕ) (p : cosetIndex m), ninv (permOf m p) = cosetLen m p
  | 0, _ => ninv_one
  | (m + 1), p => by
      rw [permOf_succ, ninv_permIncl_mul_descPerm m _ p.2.val (by have := p.2.isLt; omega),
        ninv_permOf m p.1, cosetLen_succ]

/-- `stdWord m w` has length `ninv w`. -/
theorem stdWord_length (m : ℕ) (w : Perm (Fin (m + 1))) : (stdWord m w).length = ninv w := by
  rw [stdWord, cosetWord_length, ← ninv_permOf]
  exact congrArg ninv ((permOfEquiv m).apply_symm_apply w)

/-- **`stdWord m w` is a reduced word for `w`**: no word for `w` is shorter. -/
theorem stdWord_reduced (m : ℕ) (w : Perm (Fin (m + 1))) (u : List (Fin m))
    (hu : (u.map adjT).prod = w) : (stdWord m w).length ≤ u.length := by
  rw [stdWord_length, ← hu]
  exact ninv_le_length u

end HeckeCoset
end QOU.SchurWeyl


