import Mathlib.Data.Real.Basic
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Fintype.BigOperators
import Mathlib.Data.Fintype.Card
import Mathlib.Tactic.Linarith
import QOU.BraidKnot.KnotFactorAmphicheiral


/-!
# QOU.BraidKnot.knot_factor_borromean

For a Brunnian k-component composite, the knot factor is the k-th
power of the constituent pairing.

LaTeX label: `cor:knot-factor-borromean-composite`

## Re-encoded 2026-09-04 (bean `qou-tmmt`) — §3b-cond item 5

`BrunnianDecoupling` had one field, `decouples : composite_factor =
component_factor ^ k`, and the "corollary" was `decouple.decouples`. The
hypothesis *was* the conclusion, so the theorem derived nothing.

The Brunnian content is not the `k`-th power — it is **decoupling**: the
composite pairs as a product over components with no cross-term. The `k`-th
power is what that product becomes when the components are uniform, and it is
now derived from `Finset.prod_const`. So the class carries a product over an
indexed family of components, and uniformity is a separate, explicit
hypothesis.

## The component factor is NOT `1 - h²` under the stated normalisation

Stating uniformity separately makes visible something the old shape hid. This
file's own upstream, `QOU.BraidKnot.knot_factor_amphicheiral`, derives

    a_K(β, β*) = 1 - w_alt · (1 + h²)

and says in its docstring, of the manuscript's displayed `1 - h²`, that *"this
is not the manuscript's displayed `a = 1 - h²`, and the difference is not a
rearrangement"* — the displayed form needs the non-alternating blocks to sum to
`1`, while the normalisation as stated sums them to `1 - w_alt`.

The old corollary hard-coded `1 - h²` into its statement and so inherited a form
its own upstream flags as underived. Both are now available:
`knot_factor_borromean` keeps the manuscript's form as a hypothesis on the
components, and `knot_factor_borromean_amphicheiral` gives the composite in the
form the upstream corollary actually proves. Which normalisation the chapter
intends is the authoring question upstream already records; it is not settled
here.

## References

- [leitner2026] Ch. Braids and Knots, §Knot factor / Borromean
-/

namespace QOU.BraidKnot

/-- **Brunnian decoupling hypothesis.**

    The knot factor of a `k`-component Brunnian composite is the product of its
    components' factors — one factor per component, no cross-term. This is the
    decoupling; it does not presuppose that the components agree. -/
structure BrunnianDecoupling (k : ℕ) (component : Fin k → ℝ)
    (composite : ℝ) : Prop where
  decouples : composite = ∏ i, component i

/-- **Uniform components give the `k`-th power.** Derived from decoupling by
    `Finset.prod_const`; the exponent is the component count, not an assumption. -/
theorem knot_factor_borromean_of_uniform {k : ℕ} {component : Fin k → ℝ}
    {composite a : ℝ} (huniform : ∀ i, component i = a)
    (decouple : BrunnianDecoupling k component composite) :
    composite = a ^ k := by
  rw [decouple.decouples, Finset.prod_congr rfl fun i _ => huniform i,
    Finset.prod_const, Finset.card_univ, Fintype.card_fin]

/-- **Corollary (Borromean-k composite knot factor).**

    A `k`-fold Brunnian composite whose components each have knot factor
    `1 - h²` has total knot factor `(1 - h²)^k`.

    The per-component value is a *hypothesis* here, not an import: see the
    module header — `knot_factor_amphicheiral` derives `1 - w_alt(1 + h²)`
    under the normalisation it states. -/
-- Ref: [leitner2026] Ch. Braids and Knots, §Knot factor / Borromean
theorem knot_factor_borromean {k : ℕ} (h : ℝ) {component : Fin k → ℝ}
    {composite : ℝ} (huniform : ∀ i, component i = 1 - h ^ 2)
    (decouple : BrunnianDecoupling k component composite) :
    composite = (1 - h ^ 2) ^ k :=
  knot_factor_borromean_of_uniform huniform decouple

/-- **The same composite in the form the upstream corollary proves.** With each
    component at `1 - w_alt(1 + h²)` — what `knot_factor_amphicheiral` derives —
    the composite is that quantity to the `k`. -/
theorem knot_factor_borromean_amphicheiral {k : ℕ} (w_alt h : ℝ)
    {component : Fin k → ℝ} {composite : ℝ}
    (huniform : ∀ i, component i = 1 - w_alt * (1 + h ^ 2))
    (decouple : BrunnianDecoupling k component composite) :
    composite = (1 - w_alt * (1 + h ^ 2)) ^ k :=
  knot_factor_borromean_of_uniform huniform decouple

/-- **The two per-component forms agree exactly on one locus.** Not a
    rearrangement of each other, and not generically equal: the derived and the
    displayed factor coincide iff the alternating block carries weight
    `h²/(1 + h²)`. -/
theorem amphicheiral_factor_eq_displayed_iff (w_alt h : ℝ) :
    1 - w_alt * (1 + h ^ 2) = 1 - h ^ 2 ↔ w_alt * (1 + h ^ 2) = h ^ 2 := by
  constructor <;> intro hEq <;> linarith

/-- **At zero alternating weight the composite is `1` and carries no
    information about `h`.** This is the degenerate case the upstream docstring
    names, propagated to the composite: `w_alt = 0` makes every component `1`,
    so the `k`-fold product is `1` for every `h` and every `k`. -/
theorem knot_factor_borromean_trivial_of_zero_weight {k : ℕ} (h : ℝ)
    {component : Fin k → ℝ} {composite : ℝ}
    (huniform : ∀ i, component i = 1 - 0 * (1 + h ^ 2))
    (decouple : BrunnianDecoupling k component composite) :
    composite = 1 := by
  have := knot_factor_borromean_of_uniform huniform decouple
  simpa using this

-- The former `knot_factor_borromean_value : ∃ a : ℝ, a = (1 - h ^ 2) ^ k`
-- was removed: `∃ a, a = e` is provable by `⟨e, rfl⟩` for any `e`, so it
-- asserted nothing about the Borromean composite.

end QOU.BraidKnot
