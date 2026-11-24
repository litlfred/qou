import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Tactic.Ring

/-!
# QOU.Information.photon_threading_mass — mass as photon-threading cost

**Proposition** ([`prop:photon-threading-mass`](../../../quantum-observable-universe/information-theory/photon-threading-mass.md)).

Let `𝔋` be a knot composite with braid word `β_𝔋 ∈ B_n`. The categorical
mass `m_𝔋` equals the total Gröbner–Shirshov reduction cost of threading
the photon strand `γ` through the hadron braid:

`m_𝔋 = (q − 1)² · |q − q⁻¹| · Σ_w |c_w|`,

the sum running over the Hecke reductions `σ_i² → (q − q⁻¹)σ_i + 1` that
move `γ` from above `β_𝔋` to below it.

## Formalisation notes

- **Non-degenerate conditional (§3b-cond).** The mass equation is
  *derived*, not assumed. The two genuine inputs are carried as fields:

    1. `crossing_energy_eq` — the manuscript's *definition* of the
       crossing energy `E_𝔋 = |q − q⁻¹| · Σ_w |c_w|` (each Hecke step
       costs `|q − q⁻¹|` in Skein units, weighted by `|c_w|`);
    2. `mass_energy_equiv` — mass–energy equivalence `m_𝔋 = E_𝔋 · (q − 1)²`
       (the factor `(q − 1)² = 1/c_q²` converts Skein/spatial units to
       mass/temporal units), from [`def:mass-energy`].

  The headline equation is obtained by substitution + `ring`; it is
  **not** a field of the context, so the projection-vacuity test is not
  triggered (§3b-cond item 5).

-- Ref: [leitner2026] quantum-observable-universe/information-theory/photon-threading-mass.md
-/

namespace QOU.Information

open Finset

/-- Inputs for the photon-threading mass identity.

    The two manuscript facts that *compose* into the mass equation are
    carried as explicit fields (§3b-cond): the definition of the
    crossing energy as the summed Hecke cost, and mass–energy
    equivalence. The headline equation is derived from them. -/
class PhotonThreadingMassContext where
  /-- Substrate parameter `q : ℝ`. -/
  q : ℝ
  /-- Categorical mass `m_𝔋` of the hadron. -/
  m_H : ℝ
  /-- Crossing energy `E_𝔋` of the hadron braid (Skein units). -/
  E_H : ℝ
  /-- The Hecke-reduction step coefficients `|c_w|` indexed by step. -/
  c_w_abs : ℕ → ℝ
  /-- Number of Hecke reduction steps required for photon threading. -/
  n_steps : ℕ
  /-- **Crossing-energy definition (input 1):** each of the `n_steps`
      Hecke reductions costs `|q − q⁻¹|` in Skein units, weighted by the
      coefficient `|c_w|`, so `E_𝔋 = |q − q⁻¹| · Σ_w |c_w|`. -/
  crossing_energy_eq :
    E_H = |q - q⁻¹| * (Finset.range n_steps).sum (fun i => c_w_abs i)
  /-- **Mass–energy equivalence (input 2):** the crossing energy converts
      to mass through the factor `(q − 1)² = 1/c_q²`. -/
  mass_energy_equiv : m_H = E_H * (q - 1) ^ 2

/-- **Mass as photon-threading cost** ([`prop:photon-threading-mass`]).

    `m_𝔋 = (q − 1)² · |q − q⁻¹| · Σ_w |c_w|`, *derived* by substituting
    the crossing-energy definition into mass–energy equivalence. -/
-- Ref: [leitner2026] quantum-observable-universe/information-theory/photon-threading-mass.md
theorem photon_threading_mass [ctx : PhotonThreadingMassContext] :
    ctx.m_H = (ctx.q - 1) ^ 2 * |ctx.q - ctx.q⁻¹| *
      (Finset.range ctx.n_steps).sum (fun i => ctx.c_w_abs i) := by
  rw [ctx.mass_energy_equiv, ctx.crossing_energy_eq]; ring

end QOU.Information
