import QOU.SchurWeyl.HeckeStandardBasis
import Mathlib.Algebra.MonoidAlgebra.Basic

/-!
# QOU.SchurWeyl.HeckeMatsumoto — `T_w` does not depend on the reduced word

`HeckeStandardBasis` defines `T_w := stdElt m w` as the product of the generators along one
particular reduced word for `w ∈ S_{m+1}`.  This file proves **Matsumoto's theorem** for the
Iwahori–Hecke algebra: the product along **any** reduced word for `w` is `T_w`
(`prod_σ_of_reduced`), so two reduced words for the same permutation give the same element
(`matsumoto`).

## Proof

The key step is `stdElt_mul_σ_of_ascent`:

```
T_w · σ_i = T_{w s_i}   whenever ninv (w s_i) = ninv w + 1.
```

It is proved on the coset family, by induction on `m`, with the four cases of the coset bubble
(`HeckeCoset.descProd_mul_σ_*`).  For `w = ι(a) · c_j` (with `c_j` the descending coset
representative):

* **far commutation** and **braid**: `c_j s_i = s_k c_j` with `s_k` in the smaller group, so the
  ascent passes to `a` at `k` and the induction hypothesis applies;
* **lengthening**: `c_j s_i = c_{j+1}`, which is again a coset representative;
* **quadratic**: `c_j s_i = c_{j-1}`, which loses an inversion, so this case cannot be an ascent.

The permutation identities needed are obtained from the Hecke ones by **specialising** at
`q = qi = 1`: `Hecke.lift` sends `σ_i ↦ s_i` into the group algebra `ℤ[S_{m+1}]`
(`specialise`), and `MonoidAlgebra.of` is injective.  So nothing about permutations is re-proved
except the braid and commutation relations of the adjacent transpositions.

Then `prod_σ_of_reduced` is induction along the word: a prefix of a reduced word is reduced, and
each appended letter is an ascent.

## Base ring (§7c)

Generic `[CommRing K]`; the specialisation uses `ℤ`, on the permutation side only.

LaTeX label: `thm:hecke-matsumoto`

-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001 (Thm 4.4.6: the `T_w` basis is independent of the reduced word)
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion Equiv

/-! ## Relations of the adjacent transpositions -/

theorem adjT_mul_self {n : ℕ} (i : Fin n) : adjT i * adjT i = 1 := swap_mul_self _ _

/-- Conjugating a transposition by a transposition. -/
theorem swap_conj {n : ℕ} (a b c d : Fin (n + 1)) :
    swap a b * swap c d * swap a b = swap (swap a b c) (swap a b d) := by
  rw [swap_apply_apply, swap_inv]

theorem adjT_braid {n : ℕ} (i : Fin n) (hi : (i : ℕ) + 1 < n) :
    adjT i * adjT (⟨(i : ℕ) + 1, hi⟩ : Fin n) * adjT i
      = adjT (⟨(i : ℕ) + 1, hi⟩ : Fin n) * adjT i * adjT (⟨(i : ℕ) + 1, hi⟩ : Fin n) := by
  simp only [adjT]
  rw [swap_conj, swap_conj]
  have e1 : (⟨(i : ℕ) + 1, hi⟩ : Fin n).castSucc = i.succ := Fin.ext rfl
  have hab : i.castSucc ≠ i.succ :=
    Fin.ne_of_val_ne (by simp only [Fin.coe_castSucc, Fin.val_succ]; omega)
  have hac : i.castSucc ≠ (⟨(i : ℕ) + 1, hi⟩ : Fin n).succ :=
    Fin.ne_of_val_ne (by simp only [Fin.coe_castSucc, Fin.val_succ]; omega)
  have hbc : i.succ ≠ (⟨(i : ℕ) + 1, hi⟩ : Fin n).succ :=
    Fin.ne_of_val_ne (by simp only [Fin.val_succ]; omega)
  rw [e1, swap_apply_right, swap_apply_of_ne_of_ne hac.symm hbc.symm, swap_apply_left,
    swap_apply_of_ne_of_ne hab hac]

theorem adjT_commute {n : ℕ} (i j : Fin n) (h : (j : ℕ) + 2 ≤ (i : ℕ)) :
    adjT i * adjT j = adjT j * adjT i := by
  have h1 : adjT i * adjT j * adjT i = adjT j := by
    simp only [adjT]
    rw [swap_conj, swap_apply_of_ne_of_ne, swap_apply_of_ne_of_ne] <;>
      exact Fin.ne_of_val_ne (by simp only [Fin.coe_castSucc, Fin.val_succ]; omega)
  calc adjT i * adjT j = adjT i * adjT j * (adjT i * adjT i) := by rw [adjT_mul_self, mul_one]
    _ = adjT j * adjT i := by rw [← mul_assoc, h1]

/-! ## Specialisation `q = qi = 1` -/

/-- `σ_i ↦ s_i`, from `H_{n+1}(1)` to the group algebra `ℤ[S_{n+1}]`. -/
noncomputable def specialise (n : ℕ) :
    Hecke ℤ 1 1 n →ₐ[ℤ] MonoidAlgebra ℤ (Perm (Fin (n + 1))) :=
  Hecke.lift ℤ 1 1 n (fun i => MonoidAlgebra.of ℤ _ (adjT i))
    (fun i => by
      rw [← map_mul, adjT_mul_self, map_one, sub_self, zero_smul, zero_add, mul_one, one_smul])
    (fun i hi => by simp only [← map_mul, adjT_braid i hi])
    (fun i j h => by simp only [← map_mul, adjT_commute i j h])

theorem specialise_prod_word (n : ℕ) (u : List (Fin n)) :
    specialise n ((u.map (σ ℤ 1 1 n)).prod) = MonoidAlgebra.of ℤ _ ((u.map adjT).prod) := by
  rw [map_list_prod, map_list_prod, List.map_map, List.map_map]
  congr 1
  refine List.map_congr_left fun i _ => ?_
  simp [specialise]

theorem specialise_descProd (m j : ℕ) :
    specialise (m + 1) (descProd (K := ℤ) (q := 1) (qi := 1) m j)
      = MonoidAlgebra.of ℤ _ (descPerm m j) := by
  rw [descProd_eq_prod_word, specialise_prod_word, descPerm_eq_prod_word]

theorem specialise_σ (n : ℕ) (i : Fin n) :
    specialise n (σ ℤ 1 1 n i) = MonoidAlgebra.of ℤ _ (adjT i) := by
  simp [specialise]

/-- Transfer a Hecke identity `r_j σ_i = x r_k` (`x` a generator) to permutations. -/
theorem of_injective_perm (n : ℕ) {a b : Perm (Fin (n + 1))}
    (h : MonoidAlgebra.of ℤ _ a = MonoidAlgebra.of ℤ _ b) : a = b :=
  MonoidAlgebra.of_injective h

theorem descPerm_mul_adjT_of_add_lt (m : ℕ) (i : Fin (m + 1)) (j : ℕ) (h : (i : ℕ) + j + 1 ≤ m) :
    descPerm m j * adjT i = adjT i * descPerm m j := by
  apply of_injective_perm
  have e := congrArg (specialise (m + 1)) (descProd_mul_σ_of_add_lt (K := ℤ) (q := 1) (qi := 1)
    m i j h)
  rwa [map_mul, map_mul, specialise_descProd, specialise_σ, ← map_mul, ← map_mul] at e

theorem descPerm_mul_adjT_of_add_eq (m j : ℕ) (i : Fin (m + 1)) (h : (i : ℕ) + j = m) :
    descPerm m j * adjT i = descPerm m (j + 1) := by
  apply of_injective_perm
  have e := congrArg (specialise (m + 1))
    (descProd_mul_σ_of_add_eq (K := ℤ) (q := 1) (qi := 1) m j i h)
  rwa [map_mul, specialise_descProd, specialise_σ, specialise_descProd, ← map_mul] at e

theorem descPerm_mul_adjT_of_add_eq_succ (m j : ℕ) (i : Fin (m + 1)) (hj : 1 ≤ j)
    (h : (i : ℕ) + j = m + 1) : descPerm m j * adjT i = descPerm m (j - 1) := by
  apply of_injective_perm
  have e := congrArg (specialise (m + 1))
    (descProd_mul_σ_of_add_eq_succ (K := ℤ) (q := 1) (qi := 1) m j i hj h)
  rw [map_mul, map_add, map_smul, map_smul, specialise_descProd, specialise_σ,
    specialise_descProd, ← map_mul] at e
  simpa using e

theorem descPerm_mul_adjT_of_le_add (m j : ℕ) (i : Fin (m + 1)) (hj : j ≤ m + 1)
    (h : m + 2 ≤ (i : ℕ) + j) :
    descPerm m j * adjT i
      = adjT (⟨(i : ℕ) - 1, by omega⟩ : Fin (m + 1)) * descPerm m j := by
  apply of_injective_perm
  have e := congrArg (specialise (m + 1))
    (descProd_mul_σ_of_le_add (K := ℤ) (q := 1) (qi := 1) m j i hj h)
  rwa [map_mul, map_mul, specialise_descProd, specialise_σ, specialise_σ, ← map_mul,
    ← map_mul] at e

/-! ## The ascent step on the coset family -/

variable {K : Type*} [CommRing K] {q qi : K}

theorem ninv_permOf_succ (m : ℕ) (b : cosetIndex m) (j : Fin (m + 2)) :
    ninv (permOf (m + 1) (b, j)) = ninv (permOf m b) + j.val :=
  ninv_permIncl_mul_descPerm m _ j.val (by have := j.isLt; omega)

/-- **Right multiplication by `σ_i` at an ascent stays in the coset family**, and on the
permutation side it multiplies by `s_i`. -/
theorem cosetFam_mul_σ_of_ascent : ∀ (m : ℕ) (p : cosetIndex m) (i : Fin m),
    ninv (permOf m p * adjT i) = ninv (permOf m p) + 1 →
      ∃ p' : cosetIndex m,
        cosetFam (K := K) (q := q) (qi := qi) m p * σ K q qi m i = cosetFam m p' ∧
          permOf m p' = permOf m p * adjT i
  | 0, _, i, _ => i.elim0
  | (m + 1), (b, j), i, h => by
      have hjlt := j.isLt
      have hilt := i.isLt
      -- the shared "push a letter into the smaller group" case
      have push : ∀ (k : Fin m),
          descProd (K := K) (q := q) (qi := qi) m j.val * σ K q qi (m + 1) i
              = σ K q qi (m + 1) k.castSucc * descProd m j.val →
          descPerm m j.val * adjT i = adjT k.castSucc * descPerm m j.val →
          ∃ p' : cosetIndex (m + 1),
            cosetFam (K := K) (q := q) (qi := qi) (m + 1) (b, j) * σ K q qi (m + 1) i
                = cosetFam (m + 1) p' ∧
              permOf (m + 1) p' = permOf (m + 1) (b, j) * adjT i := by
        intro k hH hP
        have hperm : permOf (m + 1) (b, j) * adjT i
            = permIncl m (permOf m b * adjT k) * descPerm m j.val := by
          rw [permOf_succ, mul_assoc, hP, map_mul, permIncl_adjT, mul_assoc]
        have hb : ninv (permOf m b * adjT k) = ninv (permOf m b) + 1 := by
          have e := h
          rw [hperm, ninv_permIncl_mul_descPerm m _ j.val (by omega), ninv_permOf_succ] at e
          omega
        obtain ⟨b', hb1, hb2⟩ := cosetFam_mul_σ_of_ascent m b k hb
        refine ⟨(b', j), ?_, ?_⟩
        · rw [cosetFam_succ, cosetFam_succ, mul_assoc, hH, ← heckeIncl_σ, ← mul_assoc,
            ← map_mul, hb1]
        · rw [permOf_succ, hb2, ← hperm]
      by_cases h1 : (i : ℕ) + j.val + 1 ≤ m
      · -- far commutation
        have hk : (⟨i, by omega⟩ : Fin m).castSucc = i := Fin.ext rfl
        apply push ⟨i, by omega⟩
        · rw [hk]; exact descProd_mul_σ_of_add_lt m i j.val h1
        · rw [hk]; exact descPerm_mul_adjT_of_add_lt m i j.val h1
      by_cases h2 : (i : ℕ) + j.val = m
      · -- lengthening
        refine ⟨(b, ⟨j.val + 1, by omega⟩), ?_, ?_⟩
        · rw [cosetFam_succ, cosetFam_succ, mul_assoc, descProd_mul_σ_of_add_eq m j.val i h2]
        · rw [permOf_succ, permOf_succ, mul_assoc, descPerm_mul_adjT_of_add_eq m j.val i h2]
      by_cases h3 : (i : ℕ) + j.val = m + 1
      · -- quadratic: not an ascent
        exfalso
        have e := h
        rw [permOf_succ, mul_assoc, descPerm_mul_adjT_of_add_eq_succ m j.val i (by omega) h3,
          ninv_permIncl_mul_descPerm m _ (j.val - 1) (by omega),
          ninv_permIncl_mul_descPerm m _ j.val (by omega)] at e
        omega
      · -- braid
        have h4 : m + 2 ≤ (i : ℕ) + j.val := by omega
        have hk : (⟨(i : ℕ) - 1, by omega⟩ : Fin m).castSucc
            = (⟨(i : ℕ) - 1, by omega⟩ : Fin (m + 1)) := Fin.ext rfl
        apply push ⟨(i : ℕ) - 1, by omega⟩
        · rw [hk]; exact descProd_mul_σ_of_le_add m j.val i (by omega) h4
        · rw [hk]; exact descPerm_mul_adjT_of_le_add m j.val i (by omega) h4

/-- **`T_w σ_i = T_{w s_i}` at an ascent.** -/
theorem stdElt_mul_σ_of_ascent (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : ninv (w * adjT i) = ninv w + 1) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i = stdElt m (w * adjT i) := by
  have hw : permOf m ((permOfEquiv m).symm w) = w := (permOfEquiv m).apply_symm_apply w
  rw [← hw] at h
  obtain ⟨p', h1, h2⟩ := cosetFam_mul_σ_of_ascent (K := K) (q := q) (qi := qi) m _ i h
  rw [hw] at h2
  have hp' : (permOfEquiv m).symm (w * adjT i) = p' :=
    (permOfEquiv m).symm_apply_eq.mpr h2.symm
  rw [stdElt, h1, stdElt, hp']

/-! ## Matsumoto -/

/-- **The product along any reduced word for `w` is `T_w`.** -/
theorem prod_σ_of_reduced (m : ℕ) (u : List (Fin m))
    (hu : u.length = ninv ((u.map adjT).prod)) :
    (u.map (σ K q qi m)).prod = stdElt m ((u.map adjT).prod) := by
  induction u using List.reverseRecOn with
  | nil => simp [stdElt_one]
  | append_singleton u i ih =>
      simp only [List.map_append, List.map_singleton, List.prod_append, List.prod_singleton,
        List.length_append, List.length_singleton] at hu ⊢
      have hle := ninv_le_length u
      have hstep := ninv_mul_adjT_le ((u.map adjT).prod) i
      have hred : u.length = ninv ((u.map adjT).prod) := by omega
      rw [ih hred, stdElt_mul_σ_of_ascent m _ i (by omega)]

/-- **Matsumoto's theorem for `H_{m+1}(q)`**: two reduced words for the same permutation have the
same product. -/
theorem matsumoto (m : ℕ) (u v : List (Fin m))
    (hu : u.length = ninv ((u.map adjT).prod)) (hv : v.length = ninv ((v.map adjT).prod))
    (huv : (u.map adjT).prod = (v.map adjT).prod) :
    (u.map (σ K q qi m)).prod = (v.map (σ K q qi m)).prod := by
  rw [prod_σ_of_reduced m u hu, prod_σ_of_reduced m v hv, huv]

end HeckeCoset
end QOU.SchurWeyl

