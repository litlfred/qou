import QOU.Hecke.TwBasisField

/-!
# QOU.Hecke.TwMul — `T_v · T_w = T_{wv}` when the lengths add

Second brick of bean `qou-0y6h`.  The Gram matrix landed in
`QOU.Hecke.TwGram` is `τ`-shaped only once one knows how the basis multiplies,
and that is this file.

## The rule, and why the indices reverse

`orbitMap` is built from `toEnd`, an algebra map into `Module.End` whose
product is composition, so `orbitMap (a * b) = toEnd a (orbitMap b)` — the
right factor acts first.  `T_w` is in turn the product of the `σ` along a
reduced word read the same way.  The composite effect is that the group element
reached by `T_v · T_w` is `w · v`, not `v · w`.  That is a fact about this
representation's handedness, not a typo; `Tw_mul_Tw` states it explicitly.

## What is proved

* `orbitMap_mul` — `orbitMap (a * b) = toEnd a (orbitMap b)`.
* `toEnd_TwOf` — `T_ω` acts as the word `ω` acts.
* `Tw_mul_Tw` — **`T_v · T_w = T_{wv}` whenever `ℓ(wv) = ℓ(w) + ℓ(v)`**.
* `Tw_one` — `T_1 = 1`.

Injectivity of `orbitMap` is what makes this provable: the identity is checked
in the free module, where `applyWord_single` already says the operators walk the
basis, and then pulled back.  Over a field, so `[Field K]` throughout.

## What is NOT here

The **down** case — `T_v · T_s` when the length drops — which is where the
`(q-1)` and `q` coefficients appear, and which the Gram determinant needs.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.SymmetricCoxeter
open QOU.Hecke.IwahoriHecke (σ)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- `orbitMap` turns a product into the left factor acting on the right
    factor's orbit — the right factor acts first. -/
theorem orbitMap_mul (a b : QOU.Hecke.IwahoriHecke K q n) :
    orbitMap K q n (a * b) = toEnd K q n a (orbitMap K q n b) := by
  simp [map_mul, Module.End.mul_apply]

/-- The word product acts as the word acts, on any vector. -/
theorem toEnd_foldl (ω : List (Fin n)) (h : QOU.Hecke.IwahoriHecke K q n)
    (x : Equiv.Perm (Fin (n + 1)) →₀ K) :
    toEnd K q n (ω.foldl (fun a i => σ K q n i * a) h) x
      = applyWord (permCoxeterSystem n) q ω (toEnd K q n h x) := by
  induction ω generalizing h with
  | nil => simp
  | cons i ω ih =>
      have hstep : toEnd K q n (σ K q n i * h) x
          = Rs (permCoxeterSystem n) q i (toEnd K q n h x) := by
        simp [map_mul, Module.End.mul_apply]
      rw [List.foldl_cons, ih, hstep, applyWord_cons]

@[simp] theorem toEnd_TwOf (ω : List (Fin n)) (x : Equiv.Perm (Fin (n + 1)) →₀ K) :
    toEnd K q n (TwOf K q n ω) x = applyWord (permCoxeterSystem n) q ω x := by
  rw [TwOf, toEnd_foldl]
  simp

/-- **`T_1 = 1`.**  The chosen reduced word for the identity is forced to be
    empty, since a reduced word has the length of its product. -/
@[simp] theorem Tw_one : Tw K q n 1 = 1 := by
  have hlen : (reducedWord n 1).length = 0 := by
    have h := reducedWord_isReduced n (1 : Equiv.Perm (Fin (n + 1)))
    rw [CoxeterSystem.IsReduced, wordProd_reducedWord] at h
    simpa using h.symm
  rw [Tw, TwOf, List.eq_nil_of_length_eq_zero hlen]
  simp

/-- **The multiplication rule for the basis.**  When the lengths add,
    `T_v · T_w = T_{wv}` — note the order, forced by the handedness of
    `orbitMap` (see the module docstring). -/
theorem Tw_mul_Tw (v w : Equiv.Perm (Fin (n + 1)))
    (h : (permCoxeterSystem n).length (w * v)
        = (permCoxeterSystem n).length w + (permCoxeterSystem n).length v) :
    Tw K q n v * Tw K q n w = Tw K q n (w * v) := by
  refine orbitMap_injective K q n ?_
  have hlen : (reducedWord n v).length = (permCoxeterSystem n).length v := by
    have hred := reducedWord_isReduced n v
    rw [CoxeterSystem.IsReduced, wordProd_reducedWord] at hred
    exact hred.symm
  have hstep : applyWord (permCoxeterSystem n) q (reducedWord n v)
      (Finsupp.single w (1 : K)) = Finsupp.single (w * v) 1 := by
    rw [applyWord_single (permCoxeterSystem n) q _ w
      (by rw [wordProd_reducedWord, h, hlen]), wordProd_reducedWord]
  rw [orbitMap_mul, orbitMap_Tw, Tw, toEnd_TwOf, hstep, orbitMap_Tw]

/-- **The multiplication table of `H_n(q)` on its own basis.**  Left
    multiplication by a generator is exactly the operator `Rs i` that built the
    basis in the first place — so the *down* case, where the `(q-1)` and `q`
    coefficients appear, comes for free from `rsFun`.

    This is the statement the Gram determinant needs: it is the whole structure
    constant table, up and down cases together, in one identity. -/
theorem σ_mul_Tw (i : Fin n) (v : Equiv.Perm (Fin (n + 1))) :
    σ K q n i * Tw K q n v
      = if v i.castSucc < v i.succ then
          Tw K q n (v * Equiv.swap i.castSucc i.succ)
        else (q - 1) • Tw K q n v
               + q • Tw K q n (v * Equiv.swap i.castSucc i.succ) := by
  refine orbitMap_injective K q n ?_
  rw [orbitMap_mul, orbitMap_Tw, toEnd_σ, Rs_single_perm]
  by_cases h : v i.castSucc < v i.succ
  · rw [if_pos h, if_pos h, orbitMap_Tw]
  · rw [if_neg h, if_neg h, map_add, map_smul, map_smul, orbitMap_Tw, orbitMap_Tw]

/-- The **up** case on its own: when the length goes up, no coefficients. -/
theorem σ_mul_Tw_of_lt (i : Fin n) (v : Equiv.Perm (Fin (n + 1)))
    (h : v i.castSucc < v i.succ) :
    σ K q n i * Tw K q n v = Tw K q n (v * Equiv.swap i.castSucc i.succ) := by
  rw [σ_mul_Tw, if_pos h]

/-- The **down** case on its own: when the length drops, the quadratic
    relation's coefficients appear. -/
theorem σ_mul_Tw_of_not_lt (i : Fin n) (v : Equiv.Perm (Fin (n + 1)))
    (h : ¬ v i.castSucc < v i.succ) :
    σ K q n i * Tw K q n v
      = (q - 1) • Tw K q n v + q • Tw K q n (v * Equiv.swap i.castSucc i.succ) := by
  rw [σ_mul_Tw, if_neg h]

end QOU.Hecke.TwBasis
