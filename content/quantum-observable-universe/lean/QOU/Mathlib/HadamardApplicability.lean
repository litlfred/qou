/-
  Does the Hadamard chain apply to its stated target? — a scoping check.

  WHY THIS FILE EXISTS. `QOU.Mathlib.HadamardFactorization` opens by stating its
  motivation: the residual leg of `PentagonRigidity.uniqueUpToScalar` reduces to
  "the analytic fact that the canonical minimal Faddeev solution `phiBProd` is
  selected among all `phiBProd·(elliptic)` multiples by a growth/minimality
  principle", and "that principle is a special case of the **Hadamard
  factorization theorem**".

  Hadamard's theorem is about ENTIRE functions. `phiBProd` is not one.

  WHAT IS PROVED HERE. `QOU.MathlibExt.PhiBProd.phiBProd` is defined as a RATIO
  of two infinite products,

      phiBProd b z = (∏' k, numFactor b z k) / (∏' k, denFactor b z k),

  and the theorem below exhibits, for EVERY `b ≠ 0`, an explicit `z` at which the
  `k = 0` denominator factor vanishes:

      z₀ = (i·b/2)·(1 + 1/b²)     ⟹     denFactor b z₀ 0 = 0.

  The point is not exotic and not a boundary case: it exists for every `b ≠ 0`,
  including the substrate `b = √(ln q₀/2π)·e^{iπ/4}` this corpus uses.

  WHAT THAT DOES AND DOES NOT ESTABLISH — the distinction matters.

    PROVED (here, sorry-free): a denominator FACTOR vanishes at an explicit
    point, for every `b ≠ 0`.

    NOT PROVED (standard, but not formalised): that the denominator PRODUCT
    therefore vanishes there — that needs the multipliability hypotheses
    `phiBProd`'s own theorems carry — and that the numerator does not vanish to
    matching order, which would make the singularity removable. Neither is
    expected to fail, but neither is checked.

  So the honest conclusion is not "phiBProd has a pole at z₀" but the weaker and
  sufficient: **`Differentiable ℂ (phiBProd b)` cannot be assumed, and therefore
  `IsEntireOfOrderLE (phiBProd b) ρ` — whose first conjunct is exactly that
  differentiability — is not available for any `ρ` without an argument nobody has
  made.** The Hadamard chain's stated application is unestablished.

  THE LIKELY REPAIR, recorded so the next agent does not re-derive it. Each
  `numFactor`/`denFactor` is entire in `z`, and for `Im b² > 0` both products
  converge locally uniformly, so the NUMERATOR and DENOMINATOR are separately
  entire. Hadamard applies to each of them, not to their ratio. Whether the
  minimality principle survives that reformulation is an open question, not a
  translation.

  Bean qou-c3if (the roast that produced this check), bean qou-v4if (the chain).

  -- Ref: [faddeev1995] Faddeev, Lett. Math. Phys. 34 (1995) 249.
-/
import QOU.MathlibExt.PhiBProd

namespace QOU.Mathlib.HadamardApplicability

open Complex QOU.MathlibExt.PhiBProd

/-- The `k = 0` denominator factor of the modular-double product vanishes at an
explicit point, for every `b ≠ 0`.

`phiBProd` is defined as a quotient by `∏' k, denFactor b z k`, so this is the
obstruction to `phiBProd` being entire — see the module docstring for exactly
what is and is not concluded from it. -/
theorem denFactor_eq_zero {b : ℂ} (hb : b ≠ 0) :
    denFactor b ((I * b / 2) * (1 + 1 / b ^ 2)) 0 = 0 := by
  have hb2 : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
  unfold denFactor
  have hexp : -((Real.pi : ℂ) * I) / b ^ 2 * (2 * ((0 : ℕ) : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * ((I * b / 2) * (1 + 1 / b ^ 2)) / b
      = (Real.pi : ℂ) * I := by
    field_simp
    ring
  rw [hexp, Complex.exp_mul_I]
  simp

/-- The vanishing point is not a single accident: shifting `z` by any multiple of
`i b` along the dual period keeps the `k = 0` factor at zero, so the obstruction
recurs. -/
theorem denFactor_eq_zero_shift {b : ℂ} (hb : b ≠ 0) (m : ℤ) :
    denFactor b ((I * b / 2) * (1 + 1 / b ^ 2) + (m : ℂ) * I * b) 0 = 0 := by
  have hb2 : b ^ 2 ≠ 0 := pow_ne_zero 2 hb
  unfold denFactor
  have hexp : -((Real.pi : ℂ) * I) / b ^ 2 * (2 * ((0 : ℕ) : ℂ) + 1)
      + 2 * (Real.pi : ℂ) * ((I * b / 2) * (1 + 1 / b ^ 2) + (m : ℂ) * I * b) / b
      = (Real.pi : ℂ) * I + (2 * (m : ℂ)) * ((Real.pi : ℂ) * I) := by
    field_simp
    ring
  rw [hexp]
  rw [Complex.exp_add]
  have h2 : Complex.exp ((2 * (m : ℂ)) * ((Real.pi : ℂ) * I)) = 1 := by
    have : (2 * (m : ℂ)) * ((Real.pi : ℂ) * I) = (m : ℂ) * (2 * (Real.pi : ℂ) * I) := by
      ring
    rw [this, Complex.exp_int_mul_two_pi_mul_I]
  rw [h2, Complex.exp_mul_I]
  simp

end QOU.Mathlib.HadamardApplicability
