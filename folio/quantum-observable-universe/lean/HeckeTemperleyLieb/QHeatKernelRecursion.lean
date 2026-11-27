import HeckeTemperleyLieb.QHeatKernelModeSet
import Mathlib.RingTheory.Polynomial.Vieta

/-!
# The recursion coefficients `a_j(q)` and their exact bar-parity

Bean `qou-8vt2` (define `ϑ_K`), fibre route, the step after `QHeatKernelModeSet`.

`prop:q-beta-c-k-recursion-from-habiro-q-difference` writes the recursion coefficients as
elementary symmetric polynomials of the per-mode rates,

    a_j = e_j({ r_λ }),        r_λ = (q − 1)·μ_λ,

and states the bar-parity law "a_j is bar-even for even j and bar-odd for odd j, **up to the
monomial twist q^j**", *under the hypothesis* that each μ_λ is bar-even.

## What this file changes

With the Hecke-derived rate `μ_λ = q^{−1/2}·g_λ` (`QHeatKernelRate`), `μ_λ` is **not**
bar-even; it satisfies `μ_λ(1/q) = q·μ_λ(q)`. That factor `q` is exactly the twist. Absorbed into
the rate, it makes `r_λ` **exactly bar-odd**:

    r_λ(1/q) = (q⁻¹ − 1)·q·μ_λ(q) = −(q − 1)·μ_λ(q) = −r_λ(q)            (`modeRate_bar`)

and therefore, for **any** finite mode set `S`,

    a_j(1/q) = (−1)^j · a_j(q)        exactly, with no twist            (`recCoeff_bar`).

So the proposition's two qualifications are discharged: the bar-evenness hypothesis is
replaced by a proved parity, and the twist disappears. Everything is stated with `t = q^{1/2}`,
so the bar involution is `t ↦ t⁻¹`.

All sorry-free; no anchor, no measured value. `ϑ_K` is still undefined: this fixes the form
of the `a_j` but evaluates nothing.
-/

namespace QOU.SchurWeyl.HeatKernelRate

open QOU.SchurWeyl

variable {K : Type*} [Field K] {N : ℕ}

/-- **The per-mode recursion rate** `r_λ = (q − 1)·μ_λ`, with `q = t²`. -/
noncomputable def modeRate (t : K) (lam : Partition N) : K :=
  (t ^ 2 - 1) * heatRate t lam

/-- **`r_λ` is exactly bar-odd**: `r_λ(1/q) = −r_λ(q)`, for every `λ`. -/
theorem modeRate_bar (t : K) (ht : t ≠ 0) (lam : Partition N) :
    modeRate t⁻¹ lam = -modeRate t lam := by
  unfold modeRate
  rw [heatRate_bar t ht lam, inv_pow]
  field_simp
  ring

/-- **The recursion coefficient** `a_j = e_j({r_λ : λ ∈ S})` for a finite mode set `S`. -/
noncomputable def recCoeff (t : K) (S : Finset (Partition N)) (j : ℕ) : K :=
  (S.val.map (modeRate t)).esymm j

/-- **Exact bar-parity of the recursion coefficients**: `a_j(1/q) = (−1)^j · a_j(q)`. -/
theorem recCoeff_bar (t : K) (ht : t ≠ 0) (S : Finset (Partition N)) (j : ℕ) :
    recCoeff t⁻¹ S j = (-1) ^ j * recCoeff t S j := by
  unfold recCoeff
  have h : S.val.map (modeRate t⁻¹) = (S.val.map (modeRate t)).map Neg.neg := by
    rw [Multiset.map_map]
    exact Multiset.map_congr rfl (fun lam _ => modeRate_bar t ht lam)
  rw [h, Multiset.esymm_neg]

/-- Odd-index coefficients are bar-odd. -/
theorem recCoeff_bar_odd (t : K) (ht : t ≠ 0) (S : Finset (Partition N)) {j : ℕ}
    (hj : Odd j) : recCoeff t⁻¹ S j = -recCoeff t S j := by
  rw [recCoeff_bar t ht, hj.neg_one_pow, neg_one_mul]

/-- Even-index coefficients are bar-even. -/
theorem recCoeff_bar_even (t : K) (ht : t ≠ 0) (S : Finset (Partition N)) {j : ℕ}
    (hj : Even j) : recCoeff t⁻¹ S j = recCoeff t S j := by
  rw [recCoeff_bar t ht, hj.neg_one_pow, one_mul]

end QOU.SchurWeyl.HeatKernelRate
