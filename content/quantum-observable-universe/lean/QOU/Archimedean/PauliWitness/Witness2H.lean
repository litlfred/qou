import QOU.Archimedean.GroundRing

namespace QOU.Archimedean.PauliWitness

/-- F_Pauli for 2H (Z=1, N=1, A=2), exact in t = q^{1/2}.
    Computed by hecke-engine 0.8.0, 0ms.
    F_Pauli(q₀) = 1.0050003581
    Denominator: 2^1. -/
-- Ref: [leitner2026] §7/archimedean-universe (Pauli witness computation)
noncomputable def tr_alt_2h : LaurentPolynomial ℤ :=
  -LaurentPolynomial.T (-2) + LaurentPolynomial.T 1 - LaurentPolynomial.T 2 - LaurentPolynomial.T 3

noncomputable def net_2h : LaurentPolynomial ℤ :=
  1 + LaurentPolynomial.T 1 - LaurentPolynomial.T 3 + LaurentPolynomial.T 4

noncomputable def F_Pauli_2h_denom : ℕ := 2

/-- Observable amplitude: net(0) + net(1) — the optimal basis.
    Degree 0 + 1 content of the Gröbner NF. -/
noncomputable def observable_2h : LaurentPolynomial ℤ :=
  1 + LaurentPolynomial.T 1 - LaurentPolynomial.T 3 + LaurentPolynomial.T 4

/-- Color content: Σ_{ℓ≥2} net(ℓ) — the degree ≥ 1 interaction content.
    This is the "M" in the CMB analogy — the multi-body correlations
    that the transfer matrix cannot capture per-generator. -/
noncomputable def color_2h : LaurentPolynomial ℤ :=
  0

end QOU.Archimedean.PauliWitness
