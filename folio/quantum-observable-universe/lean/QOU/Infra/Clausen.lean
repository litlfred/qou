import QOU.Infra.Polylogarithm

/-!
# Axiomatic Clausen function infrastructure

The Glaisher–Clausen function

    Cl_n(θ) :=  Im Li_n(e^{iθ})   if n is even
             :=  Re Li_n(e^{iθ})   if n is odd

is not yet in Mathlib.  This file packages the *closed-form
predictions* used downstream as axiomatic functions, with the
substantive series-identification deferred to the `TheoremA` /
`TheoremB` / `JonquiereGeneral` classes in
`QOU.Infra.Polylogarithm`.

References:
- [zagier1986] Zagier, polylogarithms and L-values.
- Lewin (1991), *Polylogarithms and Associated Functions*, Ch. 4.
-/

namespace QOU.Infra.Clausen

open QOU.Infra.Polylogarithm

/-- Closed form for `Cl_n` at every depth and root of unity index,
    predicted by Theorems E + F + G (the all-depths generalisation
    of Theorems A + B).  For `n` odd this is the orbit-sum
    multiplier; for `n` even it vanishes (parity case-split). -/
noncomputable def clNAtZetaPredicted (n : ℕ) (K : ℕ) (zetaN : ℝ) : ℝ :=
  if n % 2 = 1 then
    (((K : ℝ)^(1 - n : ℤ) - 1) * zetaN)
  else
    0

/-- **Jonquière inversion (closed-form RHS) at depth `n`.**
    The "wrong-parity" part of `Li_n(ζ_K)` equals
    `-(2π i)^n / n! · B_n(1/K)`.

    Right now we encode the *real-part* magnitude using a Bernoulli
    polynomial value supplied symbolically (Mathlib has
    `Polynomial.bernoulli` but partial evaluation infrastructure).
    Concrete instances of `JonquiereGeneral` plug in the actual
    Bernoulli value. -/
noncomputable def jonquiereWrongParity
    (n : ℕ) (K : ℕ) (bernoulliAtOneOverK : ℝ) : ℝ :=
  -(((2 * Real.pi) ^ n) / (Nat.factorial n : ℝ)) * bernoulliAtOneOverK

end QOU.Infra.Clausen
