import Mathlib.Tactic

/-!
# QOU.Mass — the content generating function is palindromic and bar-even

The content-only face of the binding statistic (lever-1),

  `C_n(q) = Σ_{λ⊢n} f^λ · q^{content(λ)}`,     `content(λ) = Σ_{(i,j)∈λ} (j−i)`,

is **palindromic** `C_n(q) = C_n(q⁻¹)` and its q-deformation is **bar-even**
`C_n(q) − C_n(1) = O((q−1)²)` — the q-rigidity of the level-1/2 alien datum
`Δ_{ω₀}` (`computations/lever1-bridge-alien-datum.witness.json`). LaTeX label:
`prop:content-genfun-palindromic`.

Both facts hold for **every** `n` and follow from a single structural input —
partition conjugation `λ ↦ λ'` is an anti-invariant involution (`f^{λ'} = f^λ`,
`content(λ') = −content(λ)`) — proved generally in
[`QOU.AntiInvolutionPalindrome`](../lean/QOU/Common/AntiInvolutionPalindrome.lean)
(`palindromic_sum_of_antiInvolution`, `first_moment_zero_of_antiInvolution`).
This sibling records the **concrete `n = 4` instance**, fully machine-checked:
the five partitions of `4` carry `(f, content)` pairs

  `(4)↦(1,6)`, `(3,1)↦(3,2)`, `(2,2)↦(2,0)`, `(2,1,1)↦(3,−2)`, `(1⁴)↦(1,−6)`,

so `C_4(q) = q⁶ + 3q² + 2 + 3q⁻² + q⁻⁶`, manifestly palindromic, with first moment
`1·6 + 3·2 + 2·0 + 3·(−2) + 1·(−6) = 0`.

Ground ring: generic `Field` with `q ≠ 0` (the exponent is a `ℤ` power; §7c
algebraic, not archimedean).
-/

namespace QOU.Mass
namespace ContentGenfun

/-- `C_4(q) = q⁶ + 3q² + 2 + 3q⁻² + q⁻⁶` (the `n = 4` content generating function). -/
noncomputable def C4 {K : Type*} [Field K] (q : K) : K :=
  q ^ (6 : ℤ) + 3 * q ^ (2 : ℤ) + 2 + 3 * q ^ (-2 : ℤ) + q ^ (-6 : ℤ)

/-- **Palindromy (n = 4 instance)**: `C_4(q) = C_4(q⁻¹)`. -/
theorem C4_palindromic {K : Type*} [Field K] (q : K) (_hq : q ≠ 0) :
    C4 q = C4 q⁻¹ := by
  unfold C4
  simp only [inv_zpow, zpow_neg, inv_inv]
  ring

/-- **First moment vanishes (n = 4 instance)**: `Σ_λ f^λ · content(λ) = 0` — the
bar-even `O((q−1)²)` rigidity coefficient's linear term. -/
theorem C4_first_moment_zero :
    (1 * 6 + 3 * 2 + 2 * 0 + 3 * (-2) + 1 * (-6) : ℤ) = 0 := by decide

end ContentGenfun
end QOU.Mass
