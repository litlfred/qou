import QOU.Hecke.TwMul
import QOU.Hecke.TwGram

/-!
# QOU.Hecke.TwTrace — the regular trace in the `T_w` basis

Fourth brick of bean `qou-0y6h`, and the first step of the route the
2026-08-30 scoping audit redirected to.

`QOU.Hecke.TwGram` reduces semisimplicity of `H_n(q)` at every rank to
`det (twGram) ≠ 0`.  The entries of that matrix are `tr(L_{T_v T_w})`, so the
determinant computation starts by making `tr(L_x)` explicit in the basis.

## What is proved

* `repr_Tw` — the basis coordinates of a basis vector, `δ_{v,w}`.
* `trace_lmul_eq_sum` — `tr(L_x) = Σ_w ⟨x · T_w⟩_w`, the diagonal coefficients.
* `repr_σ_mul_Tw_diag` — that coefficient for `x = σ_i` is `0` when the length
  goes **up** and `q - 1` when it goes **down**.  Only descents contribute.
* `trace_lmul_σ` — hence `tr(L_{σ_i}) = (q-1) · #{w : w has a descent at i}`.

The last is a genuine value, not a restatement: the trace of a generator is
counted by descents, and the count is a purely combinatorial quantity.

## The closed form

* `card_descent_eq_card_ascent`, `two_mul_card_descent` — exactly half the
  permutations have a descent at `i`, by the involution `w ↦ w · s_i`.
* `two_mul_trace_lmul_σ` — hence `2·tr(L_{σ_i}) = (q-1)·(n+1)!`, in closed
  form.  Stated doubled so no division is needed and it holds in any
  characteristic.

## What is NOT here

The general `tr(L_{T_u})` for `u` beyond a single generator, and the
determinant itself.
-/

namespace QOU.Hecke.TwBasis

open QOU.Hecke.IwahoriHecke (σ)

variable (K : Type*) [Field K] (q : K) (n : ℕ)

/-- The basis coordinates of a basis vector: `⟨T_v⟩_w = δ_{v,w}`. -/
theorem repr_Tw (v w : Equiv.Perm (Fin (n + 1))) :
    (basisTwOfField K q n).repr (Tw K q n v) w = if v = w then 1 else 0 := by
  rw [← coe_basisTwOfField K q n, Module.Basis.repr_self, Finsupp.single_apply]

/-- **The regular trace is the sum of the diagonal coefficients** of left
    multiplication, read in the `T_w` basis. -/
theorem trace_lmul_eq_sum (x : QOU.Hecke.IwahoriHecke K q n) :
    LinearMap.trace K _ (Algebra.lmul K (QOU.Hecke.IwahoriHecke K q n) x)
      = ∑ w : Equiv.Perm (Fin (n + 1)),
          (basisTwOfField K q n).repr (x * Tw K q n w) w := by
  rw [LinearMap.trace_eq_matrix_trace K (basisTwOfField K q n)]
  refine Finset.sum_congr rfl fun w _ => ?_
  rw [Matrix.diag_apply, LinearMap.toMatrix_apply, coe_basisTwOfField]
  rfl

/-- **Only descents contribute.**  The diagonal coefficient of `σ_i · T_w` is
    `0` when the length goes up and `q - 1` when it goes down — the `q`-term of
    the down case lands on `T_{w s_i}`, off the diagonal. -/
theorem repr_σ_mul_Tw_diag (i : Fin n) (w : Equiv.Perm (Fin (n + 1))) :
    (basisTwOfField K q n).repr (σ K q n i * Tw K q n w) w
      = if w i.castSucc < w i.succ then 0 else q - 1 := by
  have hne : w * Equiv.swap i.castSucc i.succ ≠ w := by
    intro h
    have : Equiv.swap i.castSucc i.succ = (1 : Equiv.Perm (Fin (n + 1))) := by
      simpa using congrArg (fun u => w⁻¹ * u) h
    exact (Fin.castSucc_lt_succ i).ne (Equiv.swap_eq_one_iff.mp this)
  rw [σ_mul_Tw]
  by_cases h : w i.castSucc < w i.succ
  · rw [if_pos h, if_pos h, repr_Tw, if_neg hne]
  · rw [if_neg h, if_neg h, map_add, map_smul, map_smul, Finsupp.add_apply,
      Finsupp.smul_apply, Finsupp.smul_apply, repr_Tw, repr_Tw,
      if_pos rfl, if_neg hne]
    simp

/-- **The trace of a generator is counted by descents.** -/
theorem trace_lmul_σ (i : Fin n) :
    LinearMap.trace K _ (Algebra.lmul K (QOU.Hecke.IwahoriHecke K q n) (σ K q n i))
      = (q - 1) * (Finset.univ.filter
          (fun w : Equiv.Perm (Fin (n + 1)) => ¬ w i.castSucc < w i.succ)).card := by
  classical
  rw [trace_lmul_eq_sum]
  simp only [repr_σ_mul_Tw_diag]
  rw [Finset.sum_ite, Finset.sum_const_zero, zero_add, Finset.sum_const,
    nsmul_eq_mul, mul_comm]

/-- Right multiplication by `s_i` swaps ascents and descents at `i`. -/
theorem card_descent_eq_card_ascent (i : Fin n) :
    (Finset.univ.filter
        (fun w : Equiv.Perm (Fin (n + 1)) => ¬ w i.castSucc < w i.succ)).card
      = (Finset.univ.filter
          (fun w : Equiv.Perm (Fin (n + 1)) => w i.castSucc < w i.succ)).card := by
  classical
  refine Finset.card_nbij' (fun w => w * Equiv.swap i.castSucc i.succ)
    (fun w => w * Equiv.swap i.castSucc i.succ) ?_ ?_ ?_ ?_
  · intro w hw
    simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_univ, true_and] at hw ⊢
    have hne : w i.castSucc ≠ w i.succ := fun h =>
      (Fin.castSucc_lt_succ i).ne (w.injective h)
    simpa [Equiv.Perm.mul_apply] using lt_of_le_of_ne (not_lt.mp hw) hne.symm
  · intro w hw
    simp only [Finset.mem_coe, Finset.mem_filter, Finset.mem_univ, true_and] at hw ⊢
    simpa [Equiv.Perm.mul_apply] using not_lt.mpr (le_of_lt hw)
  · intro w _; simp [mul_assoc]
  · intro w _; simp [mul_assoc]

/-- **Exactly half the permutations have a descent at `i`.** -/
theorem two_mul_card_descent (i : Fin n) :
    2 * (Finset.univ.filter
        (fun w : Equiv.Perm (Fin (n + 1)) => ¬ w i.castSucc < w i.succ)).card
      = Nat.factorial (n + 1) := by
  classical
  have hsplit := Finset.filter_card_add_filter_neg_card_eq_card
    (s := (Finset.univ : Finset (Equiv.Perm (Fin (n + 1)))))
    (p := fun w => w i.castSucc < w i.succ)
  have hcard : (Finset.univ : Finset (Equiv.Perm (Fin (n + 1)))).card
      = Nat.factorial (n + 1) := by
    rw [Finset.card_univ, Fintype.card_perm, Fintype.card_fin]
  rw [← card_descent_eq_card_ascent] at hsplit
  omega

/-- **The trace of a generator, in closed form.**  Stated doubled so no
    division is needed and the statement holds in any characteristic. -/
theorem two_mul_trace_lmul_σ (i : Fin n) :
    2 * LinearMap.trace K _
        (Algebra.lmul K (QOU.Hecke.IwahoriHecke K q n) (σ K q n i))
      = (q - 1) * (Nat.factorial (n + 1) : K) := by
  classical
  rw [trace_lmul_σ, ← two_mul_card_descent n i]
  push_cast
  ring

end QOU.Hecke.TwBasis
