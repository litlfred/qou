import Mathlib.Data.Real.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum


/-!
# Frobenius S-eigenvalue classification

Under the Frobenius antipode `S` (the bar involution `q ↦ q⁻¹`,
`σ ↦ σ⁻¹`), the coefficients `1`, `[3]_q`, `H_A²` of the Wedderburn mass
formula are S-even and `H_A` is S-odd; the functionals `Φ₂` and `Φ₃` have
eigenvalues `+1` and `−1`.  The raw `Φ₁` is **not** an S-eigenvector under
convention D (`S` acts on it as the evaluation flip `q₀ ↦ q₀⁻¹`,
`markov_bar_equivariant_zD`); only its symmetrised projection
`Φ₁⁺ = (Φ₁ + Φ₁∘S)/2` is S-even.

Consequently the S-odd part of the mass has **two** channels, the odd part
`Φ₁⁻ = (Φ₁ − Φ₁∘S)/2` and the chirality term `H_A²·Φ₃`
(`mass_S_difference`); chirality is the sole S-odd channel exactly when
`α·Φ₁⁻` vanishes (`chirality_sole_S_odd_channel_iff`).  An earlier revision
asserted "exactly one S-odd term" (`chirality_is_unique_S_odd`); that
holds only for `Φ₁⁺`, not for the raw `Φ₁` the formula uses, and was
removed on owner ruling 2026-10-10 (bean qou-fd2u).

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

/-- **Theorem (term-by-term S-classification, with `Φ₁⁺`).** In the formula
    M = ... + α(1·Φ₁⁺ − 2[3]_q·Φ₂ + H_A²·Φ₃), i.e. with `Φ₁` replaced by its
    S-symmetrised projection (the `Phi_1` field), the three terms have
    eigenvalues +1, +1, −1.  This does not apply to the raw `Φ₁`, which has
    no S-eigenvalue; see `mass_S_difference`. -/
theorem frobenius_s_classification :
    let c : FrobeniusClassification := {}
    -- Term 1: 1 · Φ₁⁺
    termEigenvalue .even c.Phi_1 = .even ∧
    -- Term 2: -2[3]_q · Φ₂
    termEigenvalue c.q3 c.Phi_2 = .even ∧
    -- Term 3: H_A² · Φ₃  (S-ODD)
    termEigenvalue c.H_A2 c.Phi_3 = .odd := by
  refine ⟨?_, ?_, ?_⟩ <;> rfl

/-- **Lemma (S-even tags multiply to S-even).**
    If α, V_a, V_b are all S-even, then so are α·V_a and α·V_b.  This
    concerns eigenvalue tags only; for the statement about actual
    functionals see `s_invariant_ansatz_captures_S_odd_iff`. -/
theorem s_symmetric_ansatz_misses_chirality
    (α V_a V_b : SEigenvalue)
    (h_α : α = .even) (h_a : V_a = .even) (h_b : V_b = .even) :
    α * V_a = .even ∧ α * V_b = .even := by
  subst h_α; subst h_a; subst h_b
  exact ⟨rfl, rfl⟩

/-! ## The S-odd part of the mass has two channels (bean qou-fd2u)

Functionals are maps `B → R` on braids `B`, with `S : B → B`.  The mass is
`m β = A β + α (Φ₁ β − c Φ₂ β + h2 Φ₃ β)` with the scalars `α, c, h2`
S-invariant.  Hypotheses: `A` and `Φ₂` are S-invariant, `Φ₃` is S-odd.
Nothing is assumed about `Φ₁`. -/

section TwoChannels

variable {B R : Type*} [CommRing R]

/-- The mass functional of the Wedderburn formula, with raw `Φ₁`. -/
def massS (A Φ₁ Φ₂ Φ₃ : B → R) (α c h2 : R) (β : B) : R :=
  A β + α * (Φ₁ β - c * Φ₂ β + h2 * Φ₃ β)

/-- **The S-difference of the mass.**
    `m(Sβ) − m(β) = −α·(Φ₁ β − Φ₁(Sβ)) − 2·α·h2·Φ₃ β`, i.e.
    `−2α(Φ₁⁻ + h²Φ₃)` with `Φ₁⁻ = (Φ₁ − Φ₁∘S)/2`. -/
theorem mass_S_difference (S : B → B) (A Φ₁ Φ₂ Φ₃ : B → R) (α c h2 : R)
    (hA : ∀ β, A (S β) = A β) (h2e : ∀ β, Φ₂ (S β) = Φ₂ β)
    (h3o : ∀ β, Φ₃ (S β) = -Φ₃ β) (β : B) :
    massS A Φ₁ Φ₂ Φ₃ α c h2 (S β) - massS A Φ₁ Φ₂ Φ₃ α c h2 β
      = -(α * (Φ₁ β - Φ₁ (S β))) - 2 * α * h2 * Φ₃ β := by
  unfold massS
  rw [hA, h2e, h3o]
  ring

/-- **Chirality is the sole S-odd channel iff `α·Φ₁⁻` vanishes.**
    The S-difference of the mass equals the chirality contribution
    `−2·α·h2·Φ₃ β` exactly when `α·(Φ₁ β − Φ₁(Sβ)) = 0`. -/
theorem chirality_sole_S_odd_channel_iff (S : B → B) (A Φ₁ Φ₂ Φ₃ : B → R)
    (α c h2 : R) (hA : ∀ β, A (S β) = A β) (h2e : ∀ β, Φ₂ (S β) = Φ₂ β)
    (h3o : ∀ β, Φ₃ (S β) = -Φ₃ β) (β : B) :
    massS A Φ₁ Φ₂ Φ₃ α c h2 (S β) - massS A Φ₁ Φ₂ Φ₃ α c h2 β
        = -(2 * α * h2 * Φ₃ β) ↔
      α * (Φ₁ β - Φ₁ (S β)) = 0 := by
  rw [mass_S_difference S A Φ₁ Φ₂ Φ₃ α c h2 hA h2e h3o β]
  constructor
  · intro h; linear_combination -h
  · intro h; linear_combination -h

/-- **What an S-invariant ansatz can and cannot capture.**  If `V` is
    S-invariant, its S-difference is zero, so it reproduces the mass's
    S-difference at `β` exactly when the two S-odd channels cancel:
    `α·(Φ₁ β − Φ₁(Sβ)) + 2·α·h2·Φ₃ β = 0`.  In particular such an ansatz
    misses both `Φ₁⁻` and `H_A²·Φ₃`, not only the chirality term. -/
theorem s_invariant_ansatz_captures_S_odd_iff (S : B → B) (A Φ₁ Φ₂ Φ₃ V : B → R)
    (α c h2 : R) (hA : ∀ β, A (S β) = A β) (h2e : ∀ β, Φ₂ (S β) = Φ₂ β)
    (h3o : ∀ β, Φ₃ (S β) = -Φ₃ β) (hV : ∀ β, V (S β) = V β) (β : B) :
    V (S β) - V β = massS A Φ₁ Φ₂ Φ₃ α c h2 (S β) - massS A Φ₁ Φ₂ Φ₃ α c h2 β ↔
      α * (Φ₁ β - Φ₁ (S β)) + 2 * α * h2 * Φ₃ β = 0 := by
  rw [mass_S_difference S A Φ₁ Φ₂ Φ₃ α c h2 hA h2e h3o β, hV, sub_self]
  constructor
  · intro h; linear_combination h
  · intro h; linear_combination h

end TwoChannels

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
