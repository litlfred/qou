import Mathlib.Algebra.Group.Basic
import Mathlib.Algebra.Group.Units.Defs
import Mathlib.Algebra.Ring.Defs
import Mathlib.Tactic.Ring

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

## Ground ring (§7c) — a `CommRing` with `q` carried as a unit

The content exponents are **negative as well as positive**, so `q` must be
invertible; it need not lie in a field. Carrying `q : Rˣ` and reading the
generating function back into `R` through the unit coercion puts the block on
its natural base ring — `ℤ[q, q⁻¹] = LaurentPolynomial ℤ` is the intended
instance, and it is not a field. The `Units` group supplies the `ℤ`-power
`q ^ (e : ℤ)` directly, so no ring-level division appears anywhere.

This is strictly stronger than the earlier `[Field K]` + `q ≠ 0` statement:
instantiate `R := K` and `q := Units.mk0 q hq` to recover it.
-/

namespace QOU.Mass
namespace ContentGenfun

variable {R : Type*} [CommRing R]

/-- `C_4(q) = q⁶ + 3q² + 2 + 3q⁻² + q⁻⁶` (the `n = 4` content generating
function), read into `R` through the unit coercion. -/
def C4 (q : Rˣ) : R :=
  ↑(q ^ (6 : ℤ)) + 3 * ↑(q ^ (2 : ℤ)) + 2 + 3 * ↑(q ^ (-2 : ℤ)) + ↑(q ^ (-6 : ℤ))

/-- **Palindromy (n = 4 instance)**: `C_4(q) = C_4(q⁻¹)`. Over the unit group the
exponent flip `q ^ e ↦ q ^ (-e)` permutes the five terms, so no non-vanishing
hypothesis is needed. -/
theorem C4_palindromic (q : Rˣ) : C4 (R := R) q = C4 q⁻¹ := by
  have e : ∀ n : ℤ, (q⁻¹ : Rˣ) ^ n = q ^ (-n) := fun n => by rw [inv_zpow, zpow_neg]
  unfold C4
  simp only [e, neg_neg]
  ring

/-- **First moment vanishes (n = 4 instance)**: `Σ_λ f^λ · content(λ) = 0` — the
bar-even `O((q−1)²)` rigidity coefficient's linear term. -/
theorem C4_first_moment_zero :
    (1 * 6 + 3 * 2 + 2 * 0 + 3 * (-2) + 1 * (-6) : ℤ) = 0 := by decide

end ContentGenfun
end QOU.Mass
