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

That is the whole "which level" question on the `ħ`-vs-`k` axis: whichever way a book writes
`ħ` in terms of `k` (`1/(k+2)`, `2/(k+2)`, …), the relation `e^{iπħ} = q²`, i.e.
`ħ = (2/iπ)·ln q`, is invariant under rescaling the generator and under that bookkeeping. For
the framework's real `q₀ > 1` this makes `ħ` **purely imaginary** — the precise content of
"imaginary level". The corpus's earlier form, *"KD matching forces `ħ = 2 ln q`"*
(`qbeta_fibre_unit_circle_opens_route5_probe.py`), is the same relation with `iπħ` renamed `ħ`.

**Scope (corrected 2026-09-07 after the `qou-99qc` review on PR #7088).** The ratio `−q²` is read
off the §7a Skein normalisation (H) `L₊ − L₋ = (q − q⁻¹)L₀`, which AGENTS.md makes STRICT; the
relation is **conditional on that normalisation**, not normalisation-free. The corpus also carries
the normalisation (J) `q[L₊] − q⁻¹[L₋] = (q^{1/2} − q^{−1/2})[L₀]` (bean `qou-8bxv`, 8 content
blocks), which is *not* a rescaling of (H): its generator eigenvalues are `{q^{−1/2}, −q^{−3/2}}`,
ratio `−q`, so under (J) the same matching gives `e^{iπħ} = q` and `ħ` halves. `ratio_invariant`
covers rescaling and `ħ`-vs-`k` bookkeeping; it does not cover a change of Skein normalisation.

**Level bookkeeping, corrected.** With `ħ = (2/iπ)·ln q₀` (`|ħ| = 0.0664` at the proton pin):
`ħ = 1/(k+2)` gives `k+2 = iπ/(2 ln q₀) ≈ 15.05 i`; `ħ = 2/(k+2)` gives `k+2 = iπ/ln q₀ ≈ 30.1 i`
(the convention `q = e^{iπ/(k+2)}`); the bean's other candidate `k+2 = 2πi/ln q₀ ≈ 60.2 i` is the
convention `q = e^{2πi/(k+2)}`, i.e. `ħ = 4/(k+2)`. An earlier version of this paragraph mapped
`60.2 i` and `30.1 i` onto `ħ = 2/(k+2)` and `1/(k+2)`, which is off by a factor of two; the probe
`kz_pullback_monodromy_exact_probe.py` computed the correct values (`15.05 i`, `30.1 i`) all along.

This file proves the algebraic core over a generic field: if a pair of eigenvalues has product
`−1` and ratio `−q²`, it is `{q, −q⁻¹}` up to a global sign, and the ratio is invariant under
rescaling. The exponential bookkeeping (`e^{iπħ/4}`, `e^{−3iπħ/4}`) lives in the probe
`computations/probes/kz_pullback_monodromy_exact_probe.py`, which evaluates it at the proton pin.

-- Ref: [kohno1987] Kohno, Ann. Inst. Fourier 37 (1987).
-- Ref: [leitner2026] computations/qbeta/qbeta_fibre_unit_circle_opens_route5_probe.py §1.
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

/-- **Square of the first Hecke eigenvalue from product `-1` and ratio `-q^2` (`qou-l2vh`).**
If `a * b = -1` and `a / b = -(q ^ 2)` with `q ≠ 0` and `b ≠ 0`, then `a ^ 2 = q ^ 2`. -/
theorem eigen_first_sq_of_product_ratio {a b q : K} (hq : q ≠ 0) (hb : b ≠ 0)
    (hprod : a * b = -1) (hratio : a / b = -(q ^ 2)) : a ^ 2 = q ^ 2 := by
  rcases eigen_pair_of_product_ratio hq hb hprod hratio with ⟨rfl, _⟩ | ⟨rfl, _⟩ <;> ring

end QOU.Mass.KZLevelFromHeckeNormalisation
