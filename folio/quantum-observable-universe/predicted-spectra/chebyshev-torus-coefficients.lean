import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.Archimedean.ChebyshevTorusCoefficients — crossing coefficients of `T_{2,n}`

The torus knot `T_{2,n}` is the closure of `σ^n` in `H_2(q)`.  Its crossing
coefficients `(c_n, d_n)` satisfy the recurrence

```
  c_1 = 1,  d_1 = 0
  c_{n+1} = c_n (q - q⁻¹) + c_n + d_n
  d_{n+1} = c_n
```

equivalent to `c_n = U_{n-1}((q - q⁻¹)/2)` for `U` the Chebyshev polynomial
of the second kind.  We give the constructive recurrence over the ground
ring `R_q = ℤ[q, q⁻¹]`.

LaTeX label: `def:chebyshev-torus-coefficients`

## References
- [leitner2026] §13/chebyshev-torus-coefficients
-/

namespace QOU.Archimedean

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]`. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The indeterminate `q`. -/
def qParam : R_q := LaurentPolynomial.T 1

/-- The inverse indeterminate `q⁻¹`. -/
def qInvParam : R_q := LaurentPolynomial.T (-1)

/-- The Chebyshev crossing coefficients `(c_n, d_n)` of `T_{2,n}`, defined by
    the recurrence `c_{n+1} = c_n (q - q⁻¹) + c_n + d_n`, `d_{n+1} = c_n`,
    with base case `(c_1, d_1) = (1, 0)`.  Indexed so that `n = 0` returns
    the trivial `(0, 0)` and `n = 1` the bare crossing `(1, 0)`. -/
def chebyshevTorusCoefficients : ℕ → R_q × R_q
  | 0 => (0, 0)
  | 1 => (1, 0)
  | (n + 2) =>
      let (c, d) := chebyshevTorusCoefficients (n + 1)
      (c * (qParam - qInvParam) + c + d, c)

/-- The `c_n` component. -/
def cCoeff (n : ℕ) : R_q := (chebyshevTorusCoefficients n).1

/-- The `d_n` component. -/
def dCoeff (n : ℕ) : R_q := (chebyshevTorusCoefficients n).2

/-- Base case: the bare crossing `T_{2,1}` has `(c_1, d_1) = (1, 0)`. -/
theorem chebyshev_base : chebyshevTorusCoefficients 1 = (1, 0) := rfl

/-- The recurrence holds by definition. -/
theorem chebyshev_succ (n : ℕ) :
    chebyshevTorusCoefficients (n + 2)
      = ((chebyshevTorusCoefficients (n + 1)).1 * (qParam - qInvParam)
            + (chebyshevTorusCoefficients (n + 1)).1
            + (chebyshevTorusCoefficients (n + 1)).2,
         (chebyshevTorusCoefficients (n + 1)).1) := rfl

end

end QOU.Archimedean
