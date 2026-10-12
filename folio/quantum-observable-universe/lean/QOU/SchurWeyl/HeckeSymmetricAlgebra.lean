import QOU.SchurWeyl.HeckeRegularRep

/-!
# QOU.SchurWeyl.HeckeSymmetricAlgebra — `H_{m+1}(q)` is a symmetric algebra over any ring

Over an arbitrary commutative ring `K`, with `q, qi : K` free, let `τ = symTrace` be the
coefficient of `T_1` in the basis `{T_w}` (`stdBasisAny`).  Then

* `τ(T_w T_v) = (q·qi)^{ℓ(w)}` if `v = w⁻¹`, and `0` otherwise (`symTrace_stdElt_mul_stdElt`);
* `τ(x y) = τ(y x)` (`symTrace_mul_comm`);
* when `q·qi` is a unit, the form `(x, y) ↦ τ(x y)` is nondegenerate
  (`eq_zero_of_symTrace_mul_eq_zero`), so `H_{m+1}(q)` is a symmetric algebra, with dual basis
  `(q·qi)^{-ℓ(w)} T_{w⁻¹}`;
* every Markov trace with parameter `z = 0` equals `τ` (`MarkovTraceFamily.tr_eq_symTrace`).

## Proof of the product formula

Induct along a reduced word `u` for `w`, peeling the last letter: `w = w' s_i` with
`ℓ(w) = ℓ(w') + 1`, so `T_w = T_{w'} σ_i`, and expand `σ_i T_v` by the left rule.

* If `v⁻¹(i) < v⁻¹(i+1)` then `σ_i T_v = T_{s_i v}` and `ℓ(s_i v) = ℓ(v) + 1`.  Both sides
  vanish: `v = w⁻¹` would give `s_i v = w'⁻¹`, of length `ℓ(w) − 1 = ℓ(v) − 1`.
* Otherwise `σ_i T_v = (q − qi) T_v + q·qi T_{s_i v}`.  The first term vanishes, since `v = w'⁻¹`
  would make `i` a right descent of `w'`, contradicting `ℓ(w' s_i) = ℓ(w') + 1`.  The second is
  `q·qi · (q·qi)^{ℓ(w')}` exactly when `s_i v = w'⁻¹`, i.e. `v = w⁻¹`.

## Base ring (§7c)

Generic `[CommRing K]`, no hypotheses on `q, qi` except `IsUnit (q * qi)` for nondegeneracy.
Nothing archimedean.

LaTeX label: `thm:hecke-symmetric-algebra`

-- Ref: [geckpfeiffer2000] https://global.oup.com/academic/product/9780198502500 (Prop. 8.1.1: the symmetrising trace of the generic Iwahori–Hecke algebra)
-/

namespace QOU.SchurWeyl.HeckeCoset

open Hecke Equiv

variable {K : Type*} [CommRing K] (q qi : K)

/-- **The symmetrising trace** `τ`: the coefficient of `T_1` in the basis `{T_w}`. -/
noncomputable def symTrace (m : ℕ) : Hecke K q qi m →ₗ[K] K :=
  (stdBasisAny q qi m).coord 1

theorem symTrace_stdElt (m : ℕ) (v : Perm (Fin (m + 1))) :
    symTrace q qi m (stdElt (K := K) (q := q) (qi := qi) m v) = if v = 1 then 1 else 0 := by
  rw [symTrace, ← stdBasisAny_apply q qi m v, Module.Basis.coord_apply, Module.Basis.repr_self,
    Finsupp.single_apply]

theorem symTrace_one (m : ℕ) : symTrace q qi m 1 = 1 := by
  rw [← stdElt_one (K := K) (q := q) (qi := qi) m, symTrace_stdElt, if_pos rfl]

/-- The key step: the formula along a reduced word. -/
theorem symTrace_word_mul_stdElt (m : ℕ) (u : List (Fin m))
    (hu : u.length = ninv ((u.map adjT).prod)) (v : Perm (Fin (m + 1))) :
    symTrace q qi m ((u.map (σ K q qi m)).prod * stdElt m v)
      = if v = ((u.map adjT).prod)⁻¹ then (q * qi) ^ u.length else 0 := by
  induction u using List.reverseRecOn generalizing v with
  | nil => simp [symTrace_stdElt]
  | append_singleton u i ih =>
    simp only [List.map_append, List.prod_append, List.map_singleton, List.prod_singleton,
      List.length_append, List.length_singleton] at hu ⊢
    set w' := (u.map adjT).prod with hw'
    have hle := ninv_mul_adjT_le w' i
    have hlen := ninv_le_length u
    rw [← hw'] at hlen
    have hred : u.length = ninv w' := by omega
    have hw : ninv (w' * adjT i) = ninv w' + 1 := by omega
    have hs : adjT i * adjT i = 1 := adjT_mul_self i
    have hsi : (adjT i)⁻¹ = adjT i := adjT_inv i
    -- `v = (w' s)⁻¹ ↔ s v = w'⁻¹`
    have hiff : ∀ x : Perm (Fin (m + 1)), x = (w' * adjT i)⁻¹ ↔ adjT i * x = w'⁻¹ := by
      intro x
      rw [mul_inv_rev, hsi]
      constructor
      · rintro rfl; rw [← mul_assoc, hs, one_mul]
      · intro h; rw [← h, ← mul_assoc, hs, one_mul]
    rw [mul_assoc, σ_mul_stdElt]
    by_cases hv : v⁻¹ i.castSucc < v⁻¹ i.succ
    · -- ascent of `v⁻¹`: both sides vanish
      have hnv : ninv (adjT i * v) = ninv v + 1 := ninv_adjT_mul_of_lt v i hv
      rw [if_pos hv, ih hred, if_neg, if_neg]
      · intro h
        have h3 : ninv v = ninv w' + 1 := by rw [h, ninv_inv]; exact hw
        have h2 : ninv (adjT i * v) = ninv w' := by rw [(hiff v).1 h, ninv_inv]
        omega
      · intro h
        have h3 : ninv v = ninv w' + 1 := by rw [(hiff v).2 h, ninv_inv]; exact hw
        have h2 : ninv (adjT i * v) = ninv w' := by rw [h, ninv_inv]
        omega
    · -- descent of `v⁻¹`
      have hne : v ≠ w'⁻¹ := by
        intro h
        -- `v = w'⁻¹` makes `i` a descent of `w'`
        have hd : w' i.succ < w' i.castSucc := by
          have hv' : ¬ w' i.castSucc < w' i.succ := by rw [h, inv_inv] at hv; exact hv
          exact lt_of_le_of_ne (not_lt.mp hv') (w'.injective.ne (Fin.castSucc_lt_succ i).ne')
        have h' : (w' * adjT i) i.castSucc < (w' * adjT i) i.succ := by
          simpa [adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using hd
        have e := ninv_mul_adjT_of_lt (w' * adjT i) i h'
        rw [mul_assoc, hs, mul_one] at e
        omega
      rw [if_neg hv, mul_add, mul_smul_comm, mul_smul_comm, map_add, map_smul, map_smul, ih hred,
        ih hred, if_neg hne, smul_eq_mul, smul_eq_mul, mul_zero, zero_add]
      by_cases h : v = (w' * adjT i)⁻¹
      · rw [if_pos h, if_pos ((hiff v).1 h), pow_succ]; ring
      · rw [if_neg h, if_neg (fun h' => h ((hiff v).2 h')), mul_zero]

/-- **The product formula**: `τ(T_w T_v) = (q·qi)^{ℓ(w)} δ_{v,w⁻¹}`. -/
theorem symTrace_stdElt_mul_stdElt (m : ℕ) (w v : Perm (Fin (m + 1))) :
    symTrace q qi m (stdElt (K := K) (q := q) (qi := qi) m w * stdElt m v)
      = if v = w⁻¹ then (q * qi) ^ ninv w else 0 := by
  have h := symTrace_word_mul_stdElt q qi m (stdWord m w)
    (by rw [stdWord_length, stdWord_prod_eq]) v
  rw [stdWord_prod_eq, stdWord_length, ← stdElt_eq_prod_word] at h
  exact h

/-- **`τ` is a trace**: `τ(x y) = τ(y x)`. -/
theorem symTrace_mul_comm (m : ℕ) (x y : Hecke K q qi m) :
    symTrace q qi m (x * y) = symTrace q qi m (y * x) := by
  let F : Hecke K q qi m →ₗ[K] Hecke K q qi m →ₗ[K] K :=
    (LinearMap.mul K (Hecke K q qi m)).compr₂ (symTrace q qi m)
  let G : Hecke K q qi m →ₗ[K] Hecke K q qi m →ₗ[K] K := F.flip
  have hFG : F = G := by
    refine (stdBasisAny q qi m).ext fun w => (stdBasisAny q qi m).ext fun v => ?_
    simp only [F, G, LinearMap.flip_apply, LinearMap.compr₂_apply, LinearMap.mul_apply',
      stdBasisAny_apply, symTrace_stdElt_mul_stdElt]
    by_cases h : v = w⁻¹
    · subst h; rw [if_pos rfl, if_pos (inv_inv w).symm, ninv_inv]
    · rw [if_neg h, if_neg]
      rintro rfl; exact h (inv_inv v).symm
  exact congrArg (fun f : Hecke K q qi m →ₗ[K] Hecke K q qi m →ₗ[K] K => f x y) hFG

/-- `τ(x T_{w⁻¹}) = (q·qi)^{ℓ(w)} · [coefficient of T_w in x]`. -/
theorem symTrace_mul_stdElt_inv (m : ℕ) (x : Hecke K q qi m) (w : Perm (Fin (m + 1))) :
    symTrace q qi m (x * stdElt m w⁻¹) = (stdBasisAny q qi m).repr x w * (q * qi) ^ ninv w := by
  conv_lhs => rw [← (stdBasisAny q qi m).sum_repr x]
  rw [Finset.sum_mul, map_sum, Finset.sum_eq_single w]
  · rw [smul_mul_assoc, map_smul, stdBasisAny_apply, symTrace_stdElt_mul_stdElt, if_pos rfl,
      smul_eq_mul]
  · intro u _ hu
    rw [smul_mul_assoc, map_smul, stdBasisAny_apply, symTrace_stdElt_mul_stdElt, if_neg, smul_zero]
    intro h; exact hu (inv_injective h).symm
  · intro h; exact absurd (Finset.mem_univ w) h

/-- **Nondegeneracy**: if `q·qi` is a unit and `τ(x y) = 0` for all `y`, then `x = 0`.  So
`H_{m+1}(q)` is a symmetric algebra over `K`. -/
theorem eq_zero_of_symTrace_mul_eq_zero (hu : IsUnit (q * qi)) (m : ℕ) (x : Hecke K q qi m)
    (hx : ∀ y, symTrace q qi m (x * y) = 0) : x = 0 := by
  refine (stdBasisAny q qi m).ext_elem fun w => ?_
  have h := symTrace_mul_stdElt_inv q qi m x w
  rw [hx, eq_comm] at h
  rw [map_zero, Finsupp.zero_apply]
  exact (hu.pow (ninv w)).mul_left_eq_zero.mp h

/-- **Uniqueness**: every Markov trace with parameter `z = 0` is the symmetrising trace. -/
theorem MarkovTraceFamily.tr_eq_symTrace (T : MarkovTraceFamily K q qi 0) (m : ℕ) :
    T.tr m = symTrace q qi m := by
  refine (stdBasisAny q qi m).ext fun w => ?_
  rw [stdBasisAny_apply, T.tr_stdElt_of_zero, symTrace_stdElt]

end QOU.SchurWeyl.HeckeCoset
