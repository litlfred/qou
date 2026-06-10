import Mathlib.Analysis.SpecialFunctions.Pow.Real

/-!
# QOU.BraidKnot.eigenvalue_product_expansion — `Λ_sym(Z, N) = q^{(Z−N)(A−1)/2} · ([2]_q/2)^{ZN}`

**Proposition** ([`prop:eigenvalue-product-expansion`](../../../quantum-observable-universe/braids-and-knots/eigenvalue-product-expansion.md)).

*For a nucleus with `Z` protons and `N` neutrons (`A = Z + N`), the
symmetric-channel eigenvalue product of the nuclear braid in the
`[2,1]` representation of `H_3(R, q)` is*

```
  Λ_sym = q^((Z−N)(A−1)/2) · ([2]_q/2)^{Z·N}.
```

The Lean encoding records the closed form as a real-valued
function of `(Z, N, q)`.

-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/eigenvalue-product-expansion.md
-/

namespace QOU.BraidKnot

/-- The q-integer `[2]_q = q + q⁻¹`. -/
noncomputable def qInt2 (q : ℝ) : ℝ := q + q⁻¹

/-- The symmetric-channel eigenvalue product
    `Λ_sym(Z, N) = q^{(Z−N)(A−1)/2} · ([2]_q/2)^{Z·N}`. -/
noncomputable def lambdaSym (q : ℝ) (Z N : ℕ) : ℝ :=
  let A : ℕ := Z + N
  q ^ (((Z : ℝ) - N) * ((A : ℝ) - 1) / 2)
    * (qInt2 q / 2) ^ ((Z : ℕ) * (N : ℕ))

/-- **Closed form of the symmetric-channel eigenvalue product**
    ([`prop:eigenvalue-product-expansion`]). -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/eigenvalue-product-expansion.md
theorem eigenvalue_product_expansion (q : ℝ) (Z N : ℕ) :
    lambdaSym q Z N
      = q ^ (((Z : ℝ) - N) * (((Z + N) : ℝ) - 1) / 2)
        * (qInt2 q / 2) ^ (Z * N) := by
  -- Direct by definition.
  rfl

/-- **Boundary value at `Z = N`** (isospin-symmetric).
    For `Z = N`, the `q^{(Z−N)(A−1)/2}` factor is `q^0 = 1`, so
    `Λ_sym(Z, Z) = ([2]_q/2)^{Z²}`. -/
-- Ref: [manuscript] quantum-observable-universe/braids-and-knots/eigenvalue-product-expansion.md
theorem lambdaSym_at_isospin_symmetric (q : ℝ) (Z : ℕ) (h_q_pos : 0 < q) :
    lambdaSym q Z Z = (qInt2 q / 2) ^ (Z * Z) := by
  unfold lambdaSym
  simp only []
  -- The `((Z : ℝ) - Z) * _ / 2` is `0`; `q^0 = 1`.
  have h_zero : ((Z : ℝ) - Z) * (((Z + Z) : ℝ) - 1) / 2 = 0 := by ring
  rw [h_zero, Real.rpow_zero, one_mul]

end QOU.BraidKnot
