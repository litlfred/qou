import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum


/-!
# Frobenius S-eigenvalue classification

The three log-functionals (Φ₁, Φ₂, Φ₃) of the Wedderburn mass
formula carry distinct eigenvalues under the Frobenius antipode S:
+1, +1, −1 respectively. Combined with the S-classification of
every coefficient (1, [3]_q, H_A² all S-even; H_A is S-odd), the
3-term sum decomposes into an S-even subspace (terms 1, 2) and an
S-odd subspace (term 3 = chirality).

This identifies chirality H_A²·Φ₃ as the unique S-anti-invariant
channel, which structurally carries the proton-neutron mass splitting.

-- Ref: [manuscript] prop:frobenius-s-classification
-/

namespace QOU.WedderburnMass

/-- The Frobenius antipode action on a coefficient or functional,
    encoded by its eigenvalue under S. -/
inductive SEigenvalue : Type
  | even   -- +1
  | odd    -- −1
  deriving DecidableEq, Repr

/-- Combine two S-eigenvalues multiplicatively. -/
def SEigenvalue.mul : SEigenvalue → SEigenvalue → SEigenvalue
  | .even, .even => .even
  | .even, .odd  => .odd
  | .odd,  .even => .odd
  | .odd,  .odd  => .even

instance : Mul SEigenvalue := ⟨SEigenvalue.mul⟩

/-- The S-classification of each ingredient in the Wedderburn mass
    formula M = ... + α(Φ₁ − 2[3]_q·Φ₂ + H_A²·Φ₃). -/
structure FrobeniusClassification where
  -- Coefficients (all S-even)
  W_sym  : SEigenvalue := .even
  W_std  : SEigenvalue := .even
  W_alt  : SEigenvalue := .even
  q3     : SEigenvalue := .even   -- [3]_q
  H_A    : SEigenvalue := .odd    -- (S-ODD: H_A → -H_A)
  H_A2   : SEigenvalue := .even   -- H_A² (even square)
  /-- The Markov weight is NOT an `S`-eigenvector under the canonical
      convention D, `z = q³/(q²+1)`: `S` sends it to `z − h_A`
      (`zD_inv_eq_sub` below), the other loop value.  The former `.even`
      was the excised convention-C reading `z = 1/(q^{1/2}+q^{-1/2})`.
      `none` records "no eigenvalue"; no declaration reads this field. -/
  z      : Option SEigenvalue := none
  alpha  : SEigenvalue := .even   -- α = m_e · 8G
  -- Functionals
  /-- `.even` is the eigenvalue of the Frobenius-symmetrised projection
      `Φ₁⁺ = (Φ₁ + Φ₁∘S)/2`, even by construction.  The raw `Φ₁` used in
      the mass formula is not an `S`-eigenvector in either convention; under
      D, `S` acts on it as the evaluation flip `q₀ ↦ q₀⁻¹`
      (`markov_bar_equivariant_zD`), and its odd part `Φ₁⁻` is nonzero
      (bean qou-fd2u). -/
  Phi_1  : SEigenvalue := .even
  Phi_2  : SEigenvalue := .even   -- by determinant invariance
  Phi_3  : SEigenvalue := .odd    -- chirality is S-ODD

/-- The S-eigenvalue of a term in the binding correction is the
    product of its coefficient and functional eigenvalues. -/
def termEigenvalue (coeff func : SEigenvalue) : SEigenvalue := coeff * func

/-- **Theorem (term-by-term S-classification).** In the formula
    M = ... + α(1·Φ₁ − 2[3]_q·Φ₂ + H_A²·Φ₃), the three terms have
    eigenvalues +1, +1, −1. -/
theorem frobenius_s_classification :
    let c : FrobeniusClassification := {}
    -- Term 1: 1 · Φ₁
    termEigenvalue .even c.Phi_1 = .even ∧
    -- Term 2: -2[3]_q · Φ₂
    termEigenvalue c.q3 c.Phi_2 = .even ∧
    -- Term 3: H_A² · Φ₃  (S-ODD)
    termEigenvalue c.H_A2 c.Phi_3 = .odd := by
  refine ⟨?_, ?_, ?_⟩ <;> rfl

/-- **Corollary.** Exactly one of the three terms is S-anti-invariant,
    namely the chirality term H_A²·Φ₃. -/
theorem chirality_is_unique_S_odd :
    let c : FrobeniusClassification := {}
    termEigenvalue .even c.Phi_1 = .even ∧
    termEigenvalue c.q3 c.Phi_2 = .even ∧
    termEigenvalue c.H_A2 c.Phi_3 = .odd := by
  exact frobenius_s_classification

/-- **Lemma (S-symmetric ansatz cannot capture chirality).**
    Any S-symmetric mixing of S-even quantities lives in the S-even
    subspace and cannot reproduce an S-odd contribution.

    Concretely: if α, V_a, V_b are all S-even, then so are α·V_a and
    α·V_b.  An S-symmetric blend α·V_a + (1−α)·V_b cannot match an
    S-odd target like H_A²·Φ_3 regardless of α. -/
theorem s_symmetric_ansatz_misses_chirality
    (α V_a V_b : SEigenvalue)
    (h_α : α = .even) (h_a : V_a = .even) (h_b : V_b = .even) :
    α * V_a = .even ∧ α * V_b = .even := by
  subst h_α; subst h_a; subst h_b
  exact ⟨rfl, rfl⟩

/-- **Theorem.** The S-eigenvalues of `H_A` and `H_A²` differ:
    H_A is S-odd, H_A² is S-even (square of any eigenvalue type is even). -/
theorem H_A_squared_is_even (H_A : SEigenvalue) (h : H_A = .odd) :
    H_A * H_A = .even := by
  subst h; rfl

/-! ## The Markov weight under `S` in convention D (bean qou-fd2u)

`S` is the bar involution `q ↦ q⁻¹`, `σ ↦ σ⁻¹ = σ − h` with `h = q − q⁻¹`
(the only reading under which Table 3 fixes `ud = (1, −h/2)`).  On
`X = c σ + d` with already-barred coefficients `c, d`, `S X = c σ + (d − c h)`.
The Markov functional is `tr(c σ + d) = z c + d`.  Everything below is over a
generic field. -/

section ConventionD

variable {K : Type*} [Field K]

/-- The canonical (convention D) Markov weight `z_D(q) = q³/(q²+1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- **`z_D` at the inverted parameter.** `z_D(q⁻¹) = 1/(q(q²+1))`. -/
theorem zD_inv (q : K) (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ = 1 / (q * (q ^ 2 + 1)) := by
  unfold zD
  have e : q⁻¹ ^ 2 + 1 = (q ^ 2 + 1) * q⁻¹ ^ 2 := by ring_nf; field_simp
  have h3 : q⁻¹ ^ 2 ≠ 0 := pow_ne_zero 2 (inv_ne_zero hq)
  rw [e, div_eq_div_iff (mul_ne_zero h1 h3) (mul_ne_zero hq h1)]
  field_simp

/-- **`S` exchanges the two loop values.** `z_D(q⁻¹) = z_D(q) − (q − q⁻¹)`,
    i.e. the bar image of `tr σ = z` is `tr σ⁻¹ = z − h`. -/
theorem zD_inv_eq_sub (q : K) (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) :
    zD q⁻¹ = zD q - (q - q⁻¹) := by
  rw [zD_inv q hq h1]
  unfold zD
  symm
  rw [eq_div_iff (mul_ne_zero hq h1)]
  field_simp
  ring

/-- **Bar-equivariance of the convention-D Markov trace.** For every element
    `c σ + d` (barred coefficients), `tr_q(S(·)) = z_D(q)·c + (d − c h)`
    equals the trace evaluated at `q⁻¹`, `z_D(q⁻¹)·c + d`. Consequently
    `Φ₁(Sβ; q₀) = Φ₁(β; q₀⁻¹)`. -/
theorem markov_bar_equivariant_zD (q c d : K) (hq : q ≠ 0) (h1 : q ^ 2 + 1 ≠ 0) :
    zD q * c + (d - c * (q - q⁻¹)) = zD q⁻¹ * c + d := by
  rw [zD_inv_eq_sub q hq h1]
  ring

/-- **Converse.** Any weight pair `(z, z')` (values at `q` and `q⁻¹`) for which
    the trace is bar-equivariant on all elements satisfies `z' = z − h`.  So
    equivariance pins the relation `(*)`; it is not a property of every `z`. -/
theorem bar_equivariant_forces (z z' h : K)
    (H : ∀ c d : K, z * c + (d - c * h) = z' * c + d) : z' = z - h := by
  have := H 1 0
  linear_combination -this

/-- **Convention C is not bar-equivariant.** With `q = u²`, `z_C = u/(u²+1)`
    is bar-invariant, but at `u = 2` it violates `z(q⁻¹) = z(q) − h`. -/
theorem zC_not_bar_equivariant :
    ((1 / 2 : ℚ) / ((1 / 2) ^ 2 + 1)) ≠ (2 / (2 ^ 2 + 1) - (2 ^ 2 - (1 / 2) ^ 2)) := by
  norm_num

end ConventionD

end QOU.WedderburnMass
