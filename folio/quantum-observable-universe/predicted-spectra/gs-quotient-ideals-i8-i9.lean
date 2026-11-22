import Mathlib.Algebra.Polynomial.Laurent

/-!
# QOU.OptimalNF.GSQuotientIdealsI8I9 — adjacency / chain-collapse quotient ideals

Two quotient ideals refine the raw Gröbner–Shirshov normal form into the
per-generator transfer-matrix factorisation:

* `I₈` (adjacency correlation): a length-2 reduced word `σ_i σ_{i+1}` is
  absorbed into `σ_{i+1}` when the latter is present; its coefficient is the
  off-diagonal entry of the transfer-matrix product `M_i` (structural).
* `I₉` (closed-shell chain collapse): a reduced word `w · σ_j` is absorbed
  when its prefix `w` is present (the per-generator `V̂_i` factorisation).

We axiomatise the ideal data over the ground ring `R_q = ℤ[q, q⁻¹]`: each
ideal is a predicate on reduced words (encoded as lists of generator indices)
selecting the absorbed monomials, together with the structural coefficient.

LaTeX label: `def:gs-quotient-ideals-I8-I9`

## References
- [leitner2026] §13/gs-quotient-ideals-I8-I9
-/

namespace QOU.OptimalNF

noncomputable section

/-- Ground ring `R_q = ℤ[q, q⁻¹]`. -/
abbrev R_q := LaurentPolynomial ℤ

/-- A reduced word, encoded as the list of its generator indices. -/
abbrev ReducedWord := List ℕ

/-- The data of the two quotient ideals `I₈` and `I₉` for a normal form whose
    support is `support`.  `absorbedI8`/`absorbedI9` flag the reduced words
    removed by each ideal; `structCoeff` records the structural coefficient
    (transfer-matrix off-diagonal entry) assigned to an absorbed word. -/
structure GSQuotientIdealsI8I9 where
  /-- Support of the raw normal form. -/
  support : List ReducedWord
  /-- `I₈`: a word `σ_i σ_{i+1}` is absorbed when `σ_{i+1}` is in the support. -/
  absorbedI8 : ReducedWord → Prop
  /-- `I₉`: a word `w · σ_j` is absorbed when its prefix `w` is in the support. -/
  absorbedI9 : ReducedWord → Prop
  /-- Structural coefficient of an absorbed word (transfer-matrix entry). -/
  structCoeff : ReducedWord → R_q

end

end QOU.OptimalNF
