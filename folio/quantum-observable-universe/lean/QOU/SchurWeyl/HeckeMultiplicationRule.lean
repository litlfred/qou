import QOU.SchurWeyl.HeckeMatsumoto

/-!
# QOU.SchurWeyl.HeckeMultiplicationRule — `T_w σ_i` in the standard basis

With `T_w := stdElt m w` (well defined on reduced words by `HeckeMatsumoto.matsumoto`), the right
action of a generator is

```
T_w σ_i = T_{w s_i}                              if w(i) < w(i+1)   (ascent),
T_w σ_i = (q − qi) T_w + (q·qi) T_{w s_i}        if w(i) > w(i+1)   (descent),
```

and on the left (`σ_mul_stdElt`) the same rule with `s_i w` and the test `w⁻¹(i) < w⁻¹(i+1)`.

This is the defining multiplication rule of the Iwahori–Hecke algebra in the `T_w` basis.

## Proof

The ascent case is `HeckeMatsumoto.stdElt_mul_σ_of_ascent` together with
`ninv_mul_adjT_of_lt`.  At a descent, `v := w s_i` has `v(i) < v(i+1)`, so `T_w = T_v σ_i` by the
ascent case, and the quadratic relation `σ_i² = (q − qi) σ_i + q·qi` (`Hecke.σ_quadratic`) gives
`T_w σ_i = T_v σ_i² = (q − qi) T_w + q·qi · T_v`.

On the left, Matsumoto does the work: if `s_i w` is longer than `w`, then `i` followed by the
word of `w` is a reduced word for `s_i w`, so `σ_i T_w = T_{s_i w}` (`prod_σ_of_reduced`).  The
length test is moved to `w⁻¹` by `ninv_inv`.

## Base ring (§7c)

Generic `[CommRing K]`, with `q, qi : K` free.  Nothing archimedean.

LaTeX label: `thm:hecke-multiplication-rule`

-- Ref: [geckpfeiffer2000] https://doi.org/10.1093/oso/9780198502500.001.0001 (Thm 4.4.6: the multiplication rule of the `T_w` basis)
-/

namespace QOU.SchurWeyl
namespace HeckeCoset

open Hecke HeckeInclusion Equiv

variable {K : Type*} [CommRing K] {q qi : K}

/-- **The ascent case**: `T_w σ_i = T_{w s_i}` when `w(i) < w(i+1)`. -/
theorem stdElt_mul_σ_of_lt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : w i.castSucc < w i.succ) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i = stdElt m (w * adjT i) :=
  stdElt_mul_σ_of_ascent m w i (ninv_mul_adjT_of_lt w i h)

/-- **The descent case**: `T_w σ_i = (q − qi) T_w + (q·qi) T_{w s_i}` when `w(i) > w(i+1)`. -/
theorem stdElt_mul_σ_of_gt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : w i.succ < w i.castSucc) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i
      = (q - qi) • stdElt m w + (q * qi) • stdElt m (w * adjT i) := by
  set v := w * adjT i
  have hv : v i.castSucc < v i.succ := by
    simpa [v, adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using h
  have hvw : v * adjT i = w := by rw [mul_assoc, adjT_mul_self, mul_one]
  have hw : stdElt (K := K) (q := q) (qi := qi) m w = stdElt m v * σ K q qi m i := by
    rw [stdElt_mul_σ_of_lt m v i hv, hvw]
  rw [hw, mul_assoc, σ_quadratic, mul_add, mul_smul_comm, mul_smul_comm, mul_one]

/-- **The multiplication rule of the `T_w` basis.** -/
theorem stdElt_mul_σ (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m) :
    stdElt (K := K) (q := q) (qi := qi) m w * σ K q qi m i
      = if w i.castSucc < w i.succ then stdElt m (w * adjT i)
        else (q - qi) • stdElt m w + (q * qi) • stdElt m (w * adjT i) := by
  split_ifs with h
  · exact stdElt_mul_σ_of_lt m w i h
  · have hne : w i.castSucc ≠ w i.succ := w.injective.ne (Fin.castSucc_lt_succ i).ne
    exact stdElt_mul_σ_of_gt m w i (lt_of_le_of_ne (not_lt.mp h) hne.symm)

/-! ## Left multiplication -/

/-- The inversion number is invariant under inversion. -/
theorem ninv_inv {n : ℕ} (w : Perm (Fin n)) : ninv w⁻¹ = ninv w := by
  unfold ninv
  refine Finset.card_bij' (fun p _ => (w⁻¹ p.2, w⁻¹ p.1)) (fun p _ => (w p.2, w p.1)) ?_ ?_ ?_ ?_
  · intro p hp
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Perm.apply_inv_self] at hp ⊢
    exact ⟨hp.2, hp.1⟩
  · intro p hp
    simp only [Finset.mem_filter, Finset.mem_univ, true_and, Perm.inv_apply_self] at hp ⊢
    exact ⟨hp.2, hp.1⟩
  · intro p _; simp
  · intro p _; simp

/-- `s_i w` adds an inversion when `w⁻¹(i) < w⁻¹(i+1)`. -/
theorem ninv_adjT_mul_of_lt {n : ℕ} (w : Perm (Fin (n + 1))) (i : Fin n)
    (h : w⁻¹ i.castSucc < w⁻¹ i.succ) : ninv (adjT i * w) = ninv w + 1 := by
  have hs : (adjT i)⁻¹ = adjT i := swap_inv _ _
  rw [← ninv_inv (adjT i * w), mul_inv_rev, hs, ninv_mul_adjT_of_lt w⁻¹ i h, ninv_inv]

/-- **Left ascent**: `σ_i T_w = T_{s_i w}` when `w⁻¹(i) < w⁻¹(i+1)`. -/
theorem σ_mul_stdElt_of_lt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : w⁻¹ i.castSucc < w⁻¹ i.succ) :
    σ K q qi m i * stdElt (K := K) (q := q) (qi := qi) m w = stdElt m (adjT i * w) := by
  have hred : (i :: stdWord m w).length = ninv (((i :: stdWord m w).map adjT).prod) := by
    rw [List.map_cons, List.prod_cons, stdWord_prod_eq, ninv_adjT_mul_of_lt w i h,
      List.length_cons, stdWord_length]
  have hu := prod_σ_of_reduced (K := K) (q := q) (qi := qi) m (i :: stdWord m w) hred
  rw [List.map_cons, List.prod_cons, List.map_cons, List.prod_cons, stdWord_prod_eq,
    ← stdElt_eq_prod_word] at hu
  exact hu

/-- **Left descent**: `σ_i T_w = (q − qi) T_w + (q·qi) T_{s_i w}` when `w⁻¹(i) > w⁻¹(i+1)`. -/
theorem σ_mul_stdElt_of_gt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m)
    (h : w⁻¹ i.succ < w⁻¹ i.castSucc) :
    σ K q qi m i * stdElt (K := K) (q := q) (qi := qi) m w
      = (q - qi) • stdElt m w + (q * qi) • stdElt m (adjT i * w) := by
  set v := adjT i * w
  have hs : (adjT i)⁻¹ = adjT i := swap_inv _ _
  have hv : v⁻¹ i.castSucc < v⁻¹ i.succ := by
    simpa [v, mul_inv_rev, hs, adjT, Perm.mul_apply, swap_apply_left, swap_apply_right] using h
  have hvw : adjT i * v = w := by rw [← mul_assoc, adjT_mul_self, one_mul]
  have hw : stdElt (K := K) (q := q) (qi := qi) m w = σ K q qi m i * stdElt m v := by
    rw [σ_mul_stdElt_of_lt m v i hv, hvw]
  conv_lhs => rw [hw]
  rw [← mul_assoc, σ_quadratic, add_mul, smul_mul_assoc, smul_mul_assoc, one_mul, ← hw]

/-- **The left multiplication rule of the `T_w` basis.** -/
theorem σ_mul_stdElt (m : ℕ) (w : Perm (Fin (m + 1))) (i : Fin m) :
    σ K q qi m i * stdElt (K := K) (q := q) (qi := qi) m w
      = if w⁻¹ i.castSucc < w⁻¹ i.succ then stdElt m (adjT i * w)
        else (q - qi) • stdElt m w + (q * qi) • stdElt m (adjT i * w) := by
  split_ifs with h
  · exact σ_mul_stdElt_of_lt m w i h
  · have hne : w⁻¹ i.castSucc ≠ w⁻¹ i.succ := w⁻¹.injective.ne (Fin.castSucc_lt_succ i).ne
    exact σ_mul_stdElt_of_gt m w i (lt_of_le_of_ne (not_lt.mp h) hne.symm)

end HeckeCoset
end QOU.SchurWeyl
