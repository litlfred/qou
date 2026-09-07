import Mathlib.Tactic

/-!
# The level is fixed by the eigenvalue ratio — an exact, convention-free statement

Bean `qou-d0qq`. A half-twist's monodromy under the `𝔰𝔩₂` Knizhnik–Zamolodchikov connection on
`V ⊗ V` (`V` the fundamental representation) is `P · exp(iπħ Ω)` with `P` the swap and `Ω` the
split Casimir, whose eigenvalues are `1/4` on `Sym² V` and `−3/4` on `Λ² V`; so the monodromy
has eigenvalues `λ₁ = e^{iπħ/4}` on `Sym²` and `λ₂ = −e^{−3iπħ/4}` on `Λ²`, with **ratio**
`λ₁/λ₂ = −e^{iπħ}` and **product** `λ₁λ₂ = −e^{−iπħ/2}`. The framework's Hecke normalisation
`(σ − q)(σ + q⁻¹) = 0` has eigenvalues `q, −q⁻¹`: product `−1`, ratio `−q²`. A scalar rescaling
of the generator changes the product but never the ratio, so the ratio is the invariant that
matches the two — and it gives `q² = e^{iπħ}`.

That is the whole "which level" question, stated so no convention can move it: whichever way a
book writes `ħ` in terms of `k` (`1/(k+2)`, `2/(k+2)`, …), the *invariant* relation is
`e^{iπħ} = q²`, i.e. `ħ = (2/iπ)·ln q`. For the framework's real `q₀ > 1` this makes `ħ`
**purely imaginary** — the precise content of "imaginary level". The corpus's earlier form,
*"KD matching forces `ħ = 2 ln q`"* (`qbeta_fibre_unit_circle_opens_route5_probe.py`), is the
same relation with `iπħ` renamed `ħ`. The two candidate levels recorded on the bean,
`k + 2 = 2πi/ln q₀ ≈ 60.2 i` and `iπ/ln q₀ ≈ 30.1 i`, are the two bookkeeping conventions
`ħ = 2/(k+2)` and `ħ = 1/(k+2)`; neither is more canonical than the ratio.

This file proves the algebraic core over a generic field: if a pair of eigenvalues has product
`−1` and ratio `−q²`, it is `{q, −q⁻¹}` up to a global sign, and the ratio is invariant under
rescaling. The exponential bookkeeping (`e^{iπħ/4}`, `e^{−3iπħ/4}`) lives in the probe
`computations/probes/kz_pullback_monodromy_exact_probe.py`, which evaluates it at the proton pin.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987).
-- Ref: [manuscript] computations/qbeta/qbeta_fibre_unit_circle_opens_route5_probe.py §1.
-/

namespace QOU.Mass.KZLevelFromHeckeNormalisation

variable {K : Type*} [Field K]

/-- Rescaling both eigenvalues by the same non-zero scalar leaves their ratio unchanged. -/
theorem ratio_invariant (c a b : K) (hc : c ≠ 0) (hb : b ≠ 0) : (c * a) / (c * b) = a / b := by
  field_simp

/-- If two eigenvalues have product `−1` and ratio `−q²`, they are `q, −q⁻¹` up to a common sign:
`λ₂² = q⁻²`. -/
theorem eigen_sq_of_product_ratio {a b q : K} (hq : q ≠ 0) (hb : b ≠ 0)
    (hprod : a * b = -1) (hratio : a / b = -(q ^ 2)) : b ^ 2 = (q ^ 2)⁻¹ := by
  have ha : a = -(q ^ 2) * b := by
    field_simp at hratio
    linear_combination hratio
  rw [ha] at hprod
  have hq2 : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  field_simp
  linear_combination -hprod

/-- The two signed solutions: `(a, b) = (q, −q⁻¹)` or `(−q, q⁻¹)`. -/
theorem eigen_pair_of_product_ratio {a b q : K} (hq : q ≠ 0) (hb : b ≠ 0)
    (hprod : a * b = -1) (hratio : a / b = -(q ^ 2)) :
    (a = q ∧ b = -q⁻¹) ∨ (a = -q ∧ b = q⁻¹) := by
  have ha : a = -(q ^ 2) * b := by
    field_simp at hratio
    linear_combination hratio
  have hb2 := eigen_sq_of_product_ratio hq hb hprod hratio
  have : (b - (-q⁻¹)) * (b - q⁻¹) = 0 := by
    have h1 : (q ^ 2)⁻¹ = q⁻¹ ^ 2 := by rw [inv_pow]
    rw [h1] at hb2
    linear_combination hb2
  rcases mul_eq_zero.mp this with h | h
  · left
    have hbv : b = -q⁻¹ := by linear_combination h
    refine ⟨?_, hbv⟩
    rw [ha, hbv]; field_simp
  · right
    have hbv : b = q⁻¹ := by linear_combination h
    refine ⟨?_, hbv⟩
    rw [ha, hbv]; field_simp

end QOU.Mass.KZLevelFromHeckeNormalisation
