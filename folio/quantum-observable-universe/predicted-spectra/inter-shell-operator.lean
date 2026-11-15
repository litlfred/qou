import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.Archimedean.InterShellOperator — inter-shell torus-knot crossing map

The crossing of a new nucleon with a closed shell `ℓ` of occupancy `n_s`
is encoded by the torus-knot transfer matrix `(c_{n_s} σ + d_{n_s})`,
post-composed with Gröbner–Shirshov reduction `r(·, G)`.  As a map of
Hecke algebras this is `Φ_shell^{(ℓ)} : H_A(q) → H_{A+1}(q)`.

We axiomatise the data of such an operator over the ground ring
`R_q = ℤ[q, q⁻¹]`: the Chebyshev crossing coefficients `c_ns, d_ns`,
the carrier dimensions, and the (Gröbner–Shirshov reduced) action.  The
reduction map is the only piece that is not constructive here.

LaTeX label: `def:inter-shell-operator`

## References
- [leitner2026] §13/inter-shell-operator
-/

namespace QOU.Archimedean

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]`. -/
abbrev R_q := LaurentPolynomial ℤ

/-- The data of the inter-shell torus-knot crossing operator for a closed
    shell of occupancy `n_s`.  `cCoeff`, `dCoeff` are the Chebyshev crossing
    coefficients of `T_{2,n_s}`; `act` is the Gröbner–Shirshov reduced action
    on a normal form `N_A` carried as an `R_q`-vector indexed by basis words. -/
structure InterShellOperator (n_s : ℕ) where
  /-- Chebyshev crossing coefficient `c_{n_s}` of `T_{2,n_s}`. -/
  cCoeff : R_q
  /-- Chebyshev crossing coefficient `d_{n_s}` of `T_{2,n_s}`. -/
  dCoeff : R_q
  /-- Dimension of the source Hecke algebra `H_A(q)` (basis-word count). -/
  srcDim : ℕ
  /-- Dimension of the target Hecke algebra `H_{A+1}(q)`. -/
  tgtDim : ℕ
  /-- The Gröbner–Shirshov reduced action `N_A ↦ r(N_A · (c σ + d), G)`,
      as a map on coordinate vectors. -/
  act : (Fin srcDim → R_q) → (Fin tgtDim → R_q)

end

end QOU.Archimedean
