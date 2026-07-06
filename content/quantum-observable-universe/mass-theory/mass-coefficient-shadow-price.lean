import Mathlib.Algebra.Field.Basic

/-!
# QOU.BraidKnot.MassCoefficientShadowPrice

Each QOU mass-formula coefficient is the **shadow price** (LP dual variable) of
the corresponding partition's Frobenius positivity constraint in the nuclear
operator-selection LP.  By strong duality + complementary slackness
(`prop:operator-selection-lp`), the optimal dual variable factorises as

  u_λ* = C_λ · S_λ(Z,N,A),      C_λ = tilde w_λ · h/2,   h = q - q⁻¹

where `C_λ` is the **partition-only** LP shadow-price coefficient (the same
`C_λ` as in `prop:wedderburn-weight-canonical`) and `S_λ` is the
nuclear-datum **scaling function** (classified by the content sum `c(λ)`:
`>0` volume-type, `=0` isospin-type, `<0` charge-type).  The total binding is

  B(Z,N) = (Σ_λ C_λ · S_λ) · m_e,

and at the normalisation point `S_λ = 1` the shadow price equals `C_λ`.

## What is axiomatised vs. derived

The **LP-duality content** — that the optimal dual variables ARE the mass
coefficients (strong duality + complementary slackness over the block-diagonal
Frobenius Gram matrix `G_λ = (w_λ/d_λ) I`) — is recorded in the class fields
`C_eq` and `factor`, cited to `prop:operator-selection-lp`.  The **algebraic
consequences** are then DERIVED sorry-free:

  • `shadow_price_weight_form` — the canonical-weight form
    `u_λ* = tilde w_λ · (h/2) · S_λ` (combines `factor` and `C_eq`);
  • `normalization` — at `S_λ = 1`, `u_λ* = C_λ`;
  • `coefficient_nuclear_independent` — `C_λ` is independent of the nuclear
    datum (`u_λ* / S_λ = C_λ` whenever `S_λ ≠ 0`).

**Pre-Archimedean.**  Polymorphic in the ground field `R` (§7c): `C_λ` is
`q`-rational (Laurent in `q`), not a real number; the Archimedean
specialisation `q ↦ q₀ ∈ ℝ` is downstream (`QOU.Calculations`).

Ref: [wedderburn1908] Wedderburn, "On hypercomplex numbers," Proc. London Math. Soc. s2-6 (1908)
Ref: [hoefsmit1974] Hoefsmit, representations of Hecke algebras of type A
Ref: [jones1985] https://doi.org/10.2307/1971403
-/

namespace QOU.BraidKnot

universe u

/-- A partition `λ ⊢ k` (placeholder; an abstract index so the discipline holds
    for any realisation). -/
structure Partition where
  parts : List ℕ

/-- The shadow-price discipline for the mass-formula coefficients, polymorphic
    in the ground field `R`.

    An instance records, for the nuclear operator-selection LP:
      • the canonical Wedderburn weight `tilde w_λ` and the Hecke scalar `h`;
      • the partition-only LP coefficient `C_λ = tilde w_λ · h/2`;
      • the nuclear-datum scaling function `S_λ(Z,N,A)`;
      • the optimal dual variable `u_λ*` with the strong-duality factorisation
        `u_λ* = C_λ · S_λ` (`prop:operator-selection-lp`). -/
class MassCoefficientShadowPrice (R : Type u) [Field R] where
  /-- Hecke-generator scalar `h = q - q⁻¹`. -/
  h : R
  /-- Canonical q-deformed Wedderburn weight `tilde w_λ`
      (cf. `WedderburnWeightCanonical`). -/
  w : Partition → R
  /-- Content sum `c(λ) = Σ (j - i)` — determines the scaling type
      (`>0` volume, `=0` isospin, `<0` charge). -/
  contentSum : Partition → ℤ
  /-- LP shadow-price coefficient `C_λ` (partition-only, no nuclear datum). -/
  C : Partition → R
  /-- Scaling function `S_λ(Z,N,A)` — the only nuclear-datum-dependent factor. -/
  S : Partition → R
  /-- Optimal dual variable (shadow price) of the `λ`-Frobenius constraint. -/
  uStar : Partition → R
  /-- LP shadow-price scaling identity `C_λ = tilde w_λ · h/2` (definitional;
      the same `C_λ` as `prop:wedderburn-weight-canonical`). -/
  C_eq : ∀ lam, C lam = w lam * (h / 2)
  /-- Strong-duality factorisation `u_λ* = C_λ · S_λ`
      (`prop:operator-selection-lp`: strong duality + complementary slackness). -/
  factor : ∀ lam, uStar lam = C lam * S lam

/-- The shadow price in canonical-weight form:
    `u_λ* = tilde w_λ · (h/2) · S_λ`.  Combines the strong-duality
    factorisation with the LP scaling identity. -/
theorem MassCoefficientShadowPrice.shadow_price_weight_form
    {R : Type u} [Field R] [c : MassCoefficientShadowPrice R] (lam : Partition) :
    c.uStar lam = c.w lam * (c.h / 2) * c.S lam := by
  rw [c.factor, c.C_eq]

/-- At the normalisation point `S_λ = 1`, the shadow price equals the
    partition-only coefficient `C_λ`. -/
theorem MassCoefficientShadowPrice.normalization
    {R : Type u} [Field R] [c : MassCoefficientShadowPrice R] (lam : Partition)
    (hS : c.S lam = 1) :
    c.uStar lam = c.C lam := by
  rw [c.factor, hS, mul_one]

/-- The coefficient `C_λ` is independent of the nuclear datum: dividing the
    shadow price by the scaling recovers the partition-only `C_λ`
    (whenever `S_λ ≠ 0`). -/
theorem MassCoefficientShadowPrice.coefficient_nuclear_independent
    {R : Type u} [Field R] [c : MassCoefficientShadowPrice R] (lam : Partition)
    (hS : c.S lam ≠ 0) :
    c.uStar lam / c.S lam = c.C lam := by
  rw [c.factor, mul_div_assoc, div_self hS, mul_one]

end QOU.BraidKnot
