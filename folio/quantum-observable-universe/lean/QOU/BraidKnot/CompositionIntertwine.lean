import QOU.BraidKnot.CompositionMinimal
import QOU.BraidKnot.CompositionMurphy

/-!
# The intertwining `T_d · x_μ = x_ν · T_d`

Mathas' Lemma 3.9 turns `m_{st}` for a composition `μ` into a combination of terms for
its reordering `ν`.  The engine is this identity: the Murphy element of one composition,
conjugated across by `d`, is the Murphy element of the other.

Every input is now proved rather than assumed:

* `CompositionYoung.youngOfComp_conj_of_blockMatch` — `S_ν = d⁻¹ S_μ d`, so the two
  index sets correspond;
* `CompositionMinimal.length_mul_sortPerm_eq_add` and `length_sortPerm_mul_eq_add` — the
  length hypothesis `Tw_mul_Tw` needs, on **both** sides, because that lemma is handed;
* `TwBasis.Tw_mul_Tw` — `T_v · T_w = T_{w·v}` when the lengths add.

What is left is the reindexing, and the bijection is conjugation by `d`.
-/

namespace QOU.BraidKnot.CompositionIntertwine

open QOU.BraidKnot.CompositionYoung QOU.BraidKnot.CompositionMinimal
open QOU.BraidKnot.CompositionMurphy QOU.BraidKnot.HeckeMurphy Equiv
open QOU.Hecke.TwBasis

variable (K : Type*) [Field K] (q : K) {n : ℕ}

/-- Conjugation by `d` carries `c`'s Young subgroup into `c'`'s.  This is
`youngOfComp_conj_of_blockMatch` read elementwise. -/
theorem conj_mem_youngOfComp {c c' : Composition (n + 1)} (m : BlockMatch c c')
    {v : Perm (Fin (n + 1))} (hv : v ∈ youngOfComp c) :
    (sortPerm m)⁻¹ * v * sortPerm m ∈ youngOfComp c' := by
  rw [youngOfComp_conj_of_blockMatch m]
  refine ⟨v, hv, ?_⟩
  simp [MulAut.conj, mul_assoc]

/-- …and conjugation by `d⁻¹` carries them back. -/
theorem conj_inv_mem_youngOfComp {c c' : Composition (n + 1)} (m : BlockMatch c c')
    {w : Perm (Fin (n + 1))} (hw : w ∈ youngOfComp c') :
    sortPerm m * w * (sortPerm m)⁻¹ ∈ youngOfComp c := by
  rw [youngOfComp_conj_of_blockMatch m] at hw
  obtain ⟨v, hv, hvw⟩ := hw
  have : w = (sortPerm m)⁻¹ * v * sortPerm m := by
    rw [← hvw]; simp [MulAut.conj, mul_assoc]
  subst this
  simpa [mul_assoc] using hv

/-- **The intertwining.**  `T_d · x_μ = x_ν · T_d`.

Both sides are the same sum of basis elements, indexed once by `S_μ` and once by
`S_ν`; the bijection is conjugation by `d`, and the two length identities are what let
each product collapse to a single `T`. -/
theorem Tw_sortPerm_mul_xComp {c c' : Composition (n + 1)} (m : BlockMatch c c')
    [DecidablePred (· ∈ youngOfComp c)] [DecidablePred (· ∈ youngOfComp c')] :
    Tw K q n (sortPerm m) * xComp K q c = xComp K q c' * Tw K q n (sortPerm m) := by
  classical
  rw [xComp, xComp, murphySum, murphySum, Finset.mul_sum, Finset.sum_mul]
  refine Finset.sum_nbij' (fun v => (sortPerm m)⁻¹ * v * sortPerm m)
    (fun w => sortPerm m * w * (sortPerm m)⁻¹) ?_ ?_ ?_ ?_ ?_
  · intro v hv
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hv ⊢
    exact conj_mem_youngOfComp m hv
  · intro w hw
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hw ⊢
    exact conj_inv_mem_youngOfComp m hw
  · intro v _; group
  · intro w _; group
  · intro v hv
    simp only [Finset.mem_filter, Finset.mem_univ, true_and] at hv
    -- left side: `T_d · T_v = T_{v·d}`
    have hL : Tw K q n (sortPerm m) * Tw K q n v = Tw K q n (v * sortPerm m) :=
      Tw_mul_Tw K q n (sortPerm m) v (length_mul_sortPerm_eq_add m hv)
    -- right side: `T_{d⁻¹vd} · T_d = T_{d·(d⁻¹vd)}`, and that element is `v·d`
    have hR : Tw K q n ((sortPerm m)⁻¹ * v * sortPerm m) * Tw K q n (sortPerm m)
        = Tw K q n (sortPerm m * ((sortPerm m)⁻¹ * v * sortPerm m)) :=
      Tw_mul_Tw K q n _ (sortPerm m)
        (length_sortPerm_mul_eq_add m (conj_mem_youngOfComp m hv))
    rw [hL, hR]
    congr 1
    group

/-- Subtracting the right-intertwined product from the left-intertwined product cancels to zero (`qou-i2ed`). -/
theorem Tw_sortPerm_mul_xComp_sub_eq_zero {c c' : Composition (n + 1)} (m : BlockMatch c c')
    [DecidablePred (· ∈ youngOfComp c)] [DecidablePred (· ∈ youngOfComp c')] :
    Tw K q n (sortPerm m) * xComp K q c - xComp K q c' * Tw K q n (sortPerm m) = 0 := by
  rw [Tw_sortPerm_mul_xComp K q m, sub_self]

end QOU.BraidKnot.CompositionIntertwine
