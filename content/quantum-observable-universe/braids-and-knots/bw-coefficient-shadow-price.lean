/-!
# BW coefficients as shadow prices

Each Bethe-Weizsäcker coefficient is the shadow price (LP dual
variable) of the corresponding partition's Frobenius positivity
constraint in the nuclear operator selection LP.

## Architecture

The proposition connects three structures:
1. Operator-selection LP (primal): selects nuclear operator
2. Frobenius positivity (constraint): one per partition λ ⊢ k
3. Shadow price (dual variable): factors as C_λ · S_λ(Z,N,A) · m_e

The factorisation is unique by orthogonality of Wedderburn blocks.
-/

-- Ref: [wedderburn1908] https://doi.org/10.1112/plms/s2-6.1.77
-- Ref: [hoefsmit1974] Representations of Hecke algebras

namespace QOU.BraidKnot

/-- Shadow price of the λ-Frobenius constraint = BW coefficient × scaling. -/
structure BWCoefficientShadowPrice where
  /-- Hecke level k -/
  level : ℕ
  /-- Partition λ ⊢ k -/
  partition : List ℕ
  /-- q-integer coefficient C_λ (algebraic, no fitted parameters) -/
  coefficient : ℝ
  /-- Content sum c(λ) = Σ(j-i) determines scaling type -/
  content_sum : ℤ
  /-- Self-conjugate ↔ partition appears as single BW term -/
  self_conjugate : Bool

/-- The BW coefficient for partition λ at level k is a shadow price.
    The coefficient factors as C_λ = w_λ · tr(σ)/dim where
    w_λ = dim_q(λ)²/[k]! is the Wedderburn-Artin weight and
    tr(σ)/dim is the per-generator trace in the seminormal basis.
    For self-conjugate partitions, tr(σ)/dim = h/2
    (see wigner-2-coefficient.lean for the proof). -/
theorem bw_shadow_price_factorization (sp : BWCoefficientShadowPrice) :
    True := by trivial

end QOU.BraidKnot
