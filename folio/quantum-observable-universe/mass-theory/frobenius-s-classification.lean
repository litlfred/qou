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

-- Ref: [leitner2026] prop:frobenius-s-classification
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

/-! ## Why `Φ₃` is S-odd on chains of the primitives (bean qou-fd2u)

A two-strand element `c σ + d` is the pair `(c, d)`; with `h = q − q⁻¹` the
Hecke relation `σ² = h σ + 1` gives the product `hmul`.  The two characters
are `χ_sym(σ) = q` and `χ_alt(σ) = −q⁻¹`.  The bar involution acts on the
coefficients by a field automorphism `σ̄ : K →+* K` with `σ̄ q = q⁻¹`, and
sends `σ ↦ σ⁻¹ = σ − h`, so `S(c, d) = (σ̄ c, σ̄ d − σ̄ c · h)` (`sbar`).

The key notion is *bar-homogeneity*: `σ̄ c = ε c` and `σ̄ d = −ε d`.  The three
quark primitives `(1, 0)`, `(1, −h)`, `(1, −h/2)` have `ε = 1`, and the unit
`(0, 1)` has `ε = −1`.  Homogeneous elements are closed under products
(`ε'' = −ε ε'`), and on a homogeneous element `S` swaps the two characters up
to the common sign `−ε` (`chi_swap`).  Hence on every chain of homogeneous
factors `S` inverts the ratio `χ_sym / χ_alt`, which gives `Φ₃ ∘ S = −Φ₃`
term by term.  Nothing here is claimed for non-homogeneous elements: for
`σ + 1` the ratio is not inverted (see the proof block). -/

section ChiralitySwap

variable {K : Type*} [Field K]

/-- Product of `a σ + b` and `c σ + d` under `σ² = h σ + 1`. -/
def hmul (h : K) (X Y : K × K) : K × K :=
  (X.1 * Y.1 * h + X.1 * Y.2 + X.2 * Y.1, X.1 * Y.1 + X.2 * Y.2)

/-- The symmetric character, `σ ↦ q`. -/
def chiSym (q : K) (X : K × K) : K := X.1 * q + X.2

/-- The alternating character, `σ ↦ −q⁻¹`. -/
def chiAlt (q : K) (X : K × K) : K := -X.1 * q⁻¹ + X.2

/-- The bar involution on `c σ + d`: coefficients by `σ̄`, `σ ↦ σ − h`. -/
def sbar (σ : K →+* K) (h : K) (X : K × K) : K × K :=
  (σ X.1, σ X.2 - σ X.1 * h)

/-- Bar-homogeneity of sign `ε`: `σ̄ c = ε c`, `σ̄ d = −ε d`. -/
def BarHom (σ : K →+* K) (ε : K) (X : K × K) : Prop :=
  σ X.1 = ε * X.1 ∧ σ X.2 = -ε * X.2

/-- The chain product of a list of two-strand factors. -/
def chainProd (h : K) : List (K × K) → K × K
  | [] => (0, 1)
  | P :: Ps => hmul h P (chainProd h Ps)

/-- `σ̄ h = −h` when `σ̄ q = q⁻¹`. -/
theorem bar_h (σ : K →+* K) (q : K) (hσ : σ q = q⁻¹) :
    σ (q - q⁻¹) = -(q - q⁻¹) := by
  rw [map_sub, map_inv₀, hσ, inv_inv]; ring

/-- The bar involution is multiplicative on two-strand elements. -/
theorem sbar_hmul (σ : K →+* K) (h : K) (hh : σ h = -h) (X Y : K × K) :
    sbar σ h (hmul h X Y) = hmul h (sbar σ h X) (sbar σ h Y) := by
  simp only [sbar, hmul, map_add, map_mul, hh, Prod.mk.injEq]
  constructor <;> ring

/-- Bar of a chain is the chain of the barred factors. -/
theorem sbar_chainProd (σ : K →+* K) (h : K) (hh : σ h = -h) (Ps : List (K × K)) :
    sbar σ h (chainProd h Ps) = chainProd h (Ps.map (sbar σ h)) := by
  induction Ps with
  | nil => simp [chainProd, sbar]
  | cons P Ps ih => simp only [chainProd, List.map_cons, sbar_hmul σ h hh, ih]

/-- Homogeneous elements are closed under products, with `ε'' = −ε ε'`. -/
theorem barHom_hmul (σ : K →+* K) (h : K) (hh : σ h = -h) {ε ε' : K} {X Y : K × K}
    (hX : BarHom σ ε X) (hY : BarHom σ ε' Y) :
    BarHom σ (-(ε * ε')) (hmul h X Y) := by
  obtain ⟨h1, h2⟩ := hX
  obtain ⟨h3, h4⟩ := hY
  refine ⟨?_, ?_⟩ <;> simp only [hmul, map_add, map_mul, h1, h2, h3, h4, hh] <;> ring

/-- Every chain of homogeneous factors is homogeneous. -/
theorem barHom_chainProd (σ : K →+* K) (h : K) (hh : σ h = -h) (Ps : List (K × K))
    (hPs : ∀ P ∈ Ps, ∃ ε, BarHom σ ε P) : ∃ ε, BarHom σ ε (chainProd h Ps) := by
  induction Ps with
  | nil => exact ⟨-1, by simp [chainProd, BarHom]⟩
  | cons P Ps ih =>
    obtain ⟨ε, hP⟩ := hPs P List.mem_cons_self
    obtain ⟨ε', hR⟩ := ih (fun Q hQ => hPs Q (List.mem_cons_of_mem _ hQ))
    exact ⟨_, barHom_hmul σ h hh hP hR⟩

/-- **Character swap.** On a homogeneous element of sign `ε`, the bar
    involution exchanges the two characters up to the sign `−ε`. -/
theorem chi_swap (σ : K →+* K) (q : K) (hq : q ≠ 0) {ε : K} {X : K × K}
    (hX : BarHom σ ε X) :
    chiSym q (sbar σ (q - q⁻¹) X) = -ε * chiAlt q X ∧
      chiAlt q (sbar σ (q - q⁻¹) X) = -ε * chiSym q X := by
  obtain ⟨h1, h2⟩ := hX
  refine ⟨?_, ?_⟩ <;> simp only [chiSym, chiAlt, sbar, h1, h2]
  · ring
  · field_simp; ring

/-- The three quark primitives `uu = (1,0)`, `dd = (1,−h)`, `ud = (1,−h/2)`
    are homogeneous of sign `1`. -/
theorem primitives_barHom (σ : K →+* K) (q : K) (hσ : σ q = q⁻¹) :
    BarHom σ 1 (1, 0) ∧ BarHom σ 1 (1, -(q - q⁻¹)) ∧
      BarHom σ 1 (1, -(q - q⁻¹) / 2) := by
  have hh := bar_h σ q hσ
  refine ⟨⟨?_, ?_⟩, ⟨?_, ?_⟩, ⟨?_, ?_⟩⟩ <;>
    simp only [map_one, map_zero, map_neg, map_div₀, hh, map_ofNat] <;> ring

/-- **`Φ₃` is S-odd on chains of homogeneous factors.** For a chain `Ps`
    of bar-homogeneous factors, `S` inverts the ratio `χ_sym/χ_alt`
    (stated without division), so `log|χ_sym/χ_alt|` changes sign
    under `S` at every evaluation point where both characters are nonzero. -/
theorem chiRatio_inverts (σ : K →+* K) (q : K) (hq : q ≠ 0) (hσ : σ q = q⁻¹)
    (Ps : List (K × K)) (hPs : ∀ P ∈ Ps, ∃ ε, BarHom σ ε P) :
    chiSym q (chainProd (q - q⁻¹) (Ps.map (sbar σ (q - q⁻¹)))) *
        chiSym q (chainProd (q - q⁻¹) Ps) =
      chiAlt q (chainProd (q - q⁻¹) (Ps.map (sbar σ (q - q⁻¹)))) *
        chiAlt q (chainProd (q - q⁻¹) Ps) := by
  have hh := bar_h σ q hσ
  obtain ⟨ε, hX⟩ := barHom_chainProd σ (q - q⁻¹) hh Ps hPs
  rw [← sbar_chainProd σ _ hh Ps]
  obtain ⟨s1, s2⟩ := chi_swap σ q hq hX
  rw [s1, s2]; ring

end ChiralitySwap


end QOU.WedderburnMass
