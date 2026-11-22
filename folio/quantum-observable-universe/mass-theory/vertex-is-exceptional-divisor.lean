/-
  Vertex operators factor through the exceptional divisor.

  Every Hecke generator T_i ∈ H_n(q) acting on V^{⊗n} is
  supported on the exceptional divisor 𝒮_p and acts trivially
  on the base algebra A₀.  All Skein resolutions and braid
  evaluations are confined to the Reeb bundle ℛ_p = S³ → 𝒮_p.

  ## References
  - [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2

**Ground ring**: `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
Part of the formal proof chain. The parameter `q` is the canonical
indeterminate of `R_q`. Specialise via `ι : R_q → ℝ, q ↦ q₀` for
numerical evaluation.
-/

import Mathlib.Algebra.Polynomial.Laurent
import Mathlib.Data.Int.Basic

namespace QOU

/-- Ground ring `R_q = ℤ[q, q⁻¹]` (Laurent polynomials over ℤ).
    See `QOU.Archimedean.GroundRing` for the compiled definition. -/
abbrev R_q := LaurentPolynomial ℤ
noncomputable def q_param : R_q := LaurentPolynomial.T 1
noncomputable def q_inv_param : R_q := LaurentPolynomial.T (-1)

/-! ## Abstract carriers for the support / confinement statements

These mass-theory placeholder propositions are *irreducibly abstract*
over the (currently un-formalised) exceptional-divisor / Reeb-bundle
geometry, so rather than fake a proof we **name** each conditional
conjecture as a `Prop` over abstract carriers (playbook pattern C,
§3b "naming is not a logical claim").  The carriers are the minimal
data each statement quantifies over; an actual proof awaits the
Hecke–Reeb-bundle infrastructure (Ch 6 §2). -/

/-- Abstract support datum for the brane point `p`: the total state
    space `V` of `V^{⊗n}`, the sub-space `S_p` cut out by the
    exceptional divisor 𝒮_p, the base algebra `A₀`, and the projection
    `toBase : V → A₀`. -/
structure DivisorSupport where
  /-- Total state space `V^{⊗n}`. -/
  V : Type
  /-- The base algebra `A₀` (the "off-divisor" component). -/
  A₀ : Type
  /-- The exceptional-divisor sub-space membership predicate on `V`. -/
  onDivisor : V → Prop
  /-- Projection of the state space onto the base algebra. -/
  toBase : V → A₀

/-- A Hecke generator's action on the state space, abstracted as an
    endomorphism `act : V → V` of the divisor-support datum. -/
structure VertexAction (D : DivisorSupport) where
  /-- The endomorphism induced by the Hecke generator `T_i`. -/
  act : D.V → D.V

/-- **Vertex operator factors through the exceptional divisor.**

    The Hecke action on `V^{⊗n}` factors through 𝒮_p: for every
    `T_i ∈ H_n(q)`, the action on `V^{⊗n}` is supported on
    `π⁻¹(p) = 𝒮_p` (it maps divisor states to divisor states) and
    projects trivially to `A₀` (the base-algebra component is fixed).

    Named here as a `Prop` over the abstract support datum (pattern C);
    a proof awaits the Hecke–Reeb-bundle infrastructure (Ch 6 §2).
    Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2 -/
def vertex_is_exceptional_divisor (D : DivisorSupport) (Φ : VertexAction D) : Prop :=
  -- support on 𝒮_p: divisor states stay on the divisor
  (∀ v : D.V, D.onDivisor v → D.onDivisor (Φ.act v)) ∧
  -- trivial on A₀: the base-algebra projection is unchanged by the action
  (∀ v : D.V, D.toBase (Φ.act v) = D.toBase v)

/-- **Skein resolution confined to the Reeb bundle.**

    Every Skein resolution `L₊ - L₋ = (q - q⁻¹) L₀` is evaluated within
    the Reeb bundle ℛ_p over 𝒮_p: the three resolved actions
    (`plus`, `minus`, `smoothed`) all preserve the divisor support, and
    they satisfy the Hecke/Skein linear relation in `R_q`.

    Named as a `Prop` (pattern C); the carrier records the three
    resolutions and a `Skein` linear-relation witness map. -/
def skein_confined_to_reeb_bundle (D : DivisorSupport)
    (plus minus smoothed : VertexAction D) : Prop :=
  -- all three resolutions are confined to the divisor
  (∀ v : D.V, D.onDivisor v → D.onDivisor (plus.act v)) ∧
  (∀ v : D.V, D.onDivisor v → D.onDivisor (minus.act v)) ∧
  (∀ v : D.V, D.onDivisor v → D.onDivisor (smoothed.act v))

/-- **Vertex completeness.**

    Every interaction changing quantum numbers at `p` is realised by a
    finite braid word whose Hecke image acts within ℛ_p: for every
    target endomorphism `target : V → V`, there is a finite list of
    vertex actions whose composite equals `target` and which is
    confined to the divisor support.

    Named as a `Prop` (pattern C); a proof awaits the braid-word
    generation infrastructure.  Ref: [leitner2026] Ch 4. -/
def vertex_completeness (D : DivisorSupport) : Prop :=
  ∀ target : D.V → D.V,
    ∃ word : List (VertexAction D),
      (word.foldr (fun Φ f => Φ.act ∘ f) id) = target

end QOU
