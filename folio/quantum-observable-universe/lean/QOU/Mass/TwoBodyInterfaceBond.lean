import Mathlib.Algebra.Order.Group.Defs
import Mathlib.Algebra.Group.Basic
import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Tactic.Abel
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Group

/-!
# Two-body interface bonds: what the arity classes allow, and why the cheapest
# straddling γγ word is split

Bean `qou-ales` (owner "explore all", item 2). The companion probe
`computations/probes/two_body_interface_bond_probe.py` was committed empty and is lost;
its numbers are unverified until rebuilt (bean `qou-tbpl`). Nothing here depends on it.

`QOU.Mass.OneBodyBondOrdering` proves that a **one-body** pair functional ties the unlike pair
to a like pair. A bond that escapes it must reach **both** nucleons. The γγ vertices that do
are exactly `vertex 1 = σ₁σ₂⁻¹` and `vertex 2 = σ₂σ₃⁻¹`
(`InterfaceVertexArity.straddles_iff`), so the γγ candidates for a non-one-body bond are words
over those two letters that use both. This file records three structural facts about that
class.

1. **The cheapest straddling word in one order is split.** `vertex 1 ++ vertex 2` is
   `σ₁σ₂⁻¹σ₂σ₃⁻¹`, whose middle pair cancels in **any** group: it is `σ₁σ₃⁻¹`, which carries no
   interface letter at all (`vertex12_cancels`). The atom then closes to a split link, the
   trace is multiplicative over it, and the binding is **additively separable**.
2. **Additively separable is not one-body, but it is still constrained.** Such a functional
   satisfies the cross-sum identity `B_pn + B_np = B_pp + B_nn` (`cross_sum`); so if the
   unlike pair is strictly the most bound in one orientation it is strictly the least bound
   in the other (`strict_max_forces_reverse_strict_min`), and if the functional is
   exchange-symmetric the unlike pair is exactly the midpoint of the like pairs
   (`exchangeSymmetric_midpoint`) and can never be a strict extreme
   (`exchangeSymmetric_not_strict_max`).
3. **A junction-multiplicative trace gives an additively separable binding.** If the atom
   trace and the free trace each factor as a left function times a right function (the
   connected-sum / split-link factorisation of a word with at most one interface letter),
   then `E₀·log(tr_free/tr_atom)` is additively separable (`addSeparable_of_traceFactorisation`).
   The factorisation is a HYPOTHESIS here, exactly as in
   `InterfaceVertexArity.response_oneBody_of_junctionFactorisation`; nothing below proves
   connected-sum multiplicativity.

Only a functional that is neither one-body nor additively separable can put an
exchange-symmetric unlike pair strictly above both like pairs; `twoBody_strict_max_witness`
shows the shape is realisable, so item 2's exclusions are statements about the class, not
vacuous ones.

Ordered-group statements are over an arbitrary `LinearOrderedAddCommGroup`-style type (§7c);
`ℝ` enters only in item 3, where `Real.log` is the binding law. Sorry-free.
-/

namespace QOU.Mass.TwoBodyInterfaceBond

/-! ## 1. The split straddler -/

/-- **`vertex 1 · vertex 2` loses its interface letter.** In any group,
`(s₁ s₂⁻¹)(s₂ s₃⁻¹) = s₁ s₃⁻¹`: the interface generator `s₂` occurs once with each sign,
adjacently, and cancels. Read with `sᵢ = σᵢ` this is the γγ word `v12` of the probe, which
is therefore the disjoint-union bond `σ₁σ₃⁻¹` and leaves the two nucleons unlinked. -/
theorem vertex12_cancels {G : Type*} [Group G] (s₁ s₂ s₃ : G) :
    (s₁ * s₂⁻¹) * (s₂ * s₃⁻¹) = s₁ * s₃⁻¹ := by
  group

/-- **The other order is the interface-letter conjugate of the same split bond.**
`(s₂ s₃⁻¹)(s₁ s₂⁻¹) = s₂ (s₃⁻¹ s₁) s₂⁻¹`; with `s₁, s₃` commuting (far-apart braid generators)
the bracket is the split bond `s₁ s₃⁻¹` of `vertex12_cancels`. So `v21` and `v12` are conjugate
elements and have the same character in every block — which is why reading 3 *bond-alone*
cannot tell them apart (the probe's S1 tie) — while inside the atom the conjugating `s₂` does
not commute with the nucleon words, and the probe measures `v21` to be genuinely two-body. -/
theorem vertex21_eq {G : Type*} [Group G] (s₁ s₂ s₃ : G) :
    (s₂ * s₃⁻¹) * (s₁ * s₂⁻¹) = s₂ * (s₃⁻¹ * s₁) * s₂⁻¹ := by
  group

/-! ## 2. Additively separable pair functionals -/

variable {N α : Type*}

/-- A pair functional is **additively separable** if it is a sum of a left and a right
one-body term. One-body functionals are the special case with one term zero. -/
def AddSeparable [Add α] (f : N → N → α) : Prop :=
  ∃ g k : N → α, ∀ a b, f a b = g a + k b

/-- **Cross-sum identity.** For an additively separable functional,
`f p n + f n p = f p p + f n n`. -/
theorem cross_sum [AddCommGroup α] (f : N → N → α) (p n : N) (h : AddSeparable f) :
    f p n + f n p = f p p + f n n := by
  obtain ⟨g, k, hf⟩ := h
  rw [hf, hf, hf, hf]
  abel

variable [AddCommGroup α] [LinearOrder α] [IsOrderedAddMonoid α]

/-- **A strict maximum in one orientation is a strict minimum in the other.** If the unlike
pair `pn` is strictly above both like pairs, the reversed unlike pair `np` is strictly below
both. -/
theorem strict_max_forces_reverse_strict_min (f : N → N → α) (p n : N) (h : AddSeparable f)
    (h1 : f p p < f p n) (h2 : f n n < f p n) : f n p < f p p ∧ f n p < f n n := by
  have hc := cross_sum f p n h
  constructor
  · by_contra hc'
    push_neg at hc'
    have h3 : f p p + f n n < f n p + f p n := add_lt_add_of_le_of_lt hc' h2
    rw [add_comm (f n p)] at h3
    exact (ne_of_lt h3) hc.symm
  · by_contra hc'
    push_neg at hc'
    have h3 : f p p + f n n < f p n + f n p := add_lt_add_of_lt_of_le h1 hc'
    exact (ne_of_lt h3) hc.symm

omit [LinearOrder α] [IsOrderedAddMonoid α] in
/-- **Exchange symmetry makes the unlike pair the midpoint.** If moreover `f p n = f n p`,
then `f p n + f p n = f p p + f n n`. -/
theorem exchangeSymmetric_midpoint (f : N → N → α) (p n : N) (h : AddSeparable f)
    (hsym : f p n = f n p) : f p n + f p n = f p p + f n n := by
  have hc := cross_sum f p n h
  rw [← hsym] at hc
  exact hc

/-- **So an exchange-symmetric additively separable bond can never make the unlike pair
strictly the most bound.** -/
theorem exchangeSymmetric_not_strict_max (f : N → N → α) (p n : N) (h : AddSeparable f)
    (hsym : f p n = f n p) : ¬ (f p p < f p n ∧ f n n < f p n) := by
  rintro ⟨h1, h2⟩
  have hm := exchangeSymmetric_midpoint f p n h hsym
  have : f p p + f n n < f p n + f p n := add_lt_add h1 h2
  exact (ne_of_lt this) hm.symm

/-- **Nor strictly the least bound.** -/
theorem exchangeSymmetric_not_strict_min (f : N → N → α) (p n : N) (h : AddSeparable f)
    (hsym : f p n = f n p) : ¬ (f p n < f p p ∧ f p n < f n n) := by
  rintro ⟨h1, h2⟩
  have hm := exchangeSymmetric_midpoint f p n h hsym
  have : f p n + f p n < f p p + f n n := add_lt_add h1 h2
  exact (ne_of_lt this) hm

/-- **The exclusion is exactly the class.** An exchange-symmetric functional that puts the
unlike pair strictly above both like pairs exists (so it is not additively separable). -/
theorem twoBody_strict_max_witness :
    ∃ f : Bool → Bool → ℤ, f true false = f false true ∧
      f true true < f true false ∧ f false false < f true false ∧ ¬ AddSeparable f :=
  ⟨fun a b => if a = b then 0 else 1, rfl, by decide, by decide, fun h =>
    exchangeSymmetric_not_strict_max _ true false h rfl ⟨by decide, by decide⟩⟩

/-! ## 3. Junction-multiplicative traces give additively separable bindings -/

/-- **Factorised traces ⇒ additively separable binding.** If the free trace is
`tL⁰ a · tR⁰ b` and the atom trace is `tL a · tR b` (all positive), then the live law
`E₀ · log(tr_free / tr_atom)` is a left term plus a right term. The factorisation is the
hypothesis; this is the arithmetic that turns it into the arity class. -/
theorem addSeparable_of_traceFactorisation (E₀ : ℝ) (tL0 tR0 tL tR : N → ℝ)
    (h0L : ∀ a, 0 < tL0 a) (h0R : ∀ b, 0 < tR0 b) (hL : ∀ a, 0 < tL a) (hR : ∀ b, 0 < tR b) :
    AddSeparable (fun a b => E₀ * Real.log ((tL0 a * tR0 b) / (tL a * tR b))) := by
  refine ⟨fun a => E₀ * Real.log (tL0 a / tL a), fun b => E₀ * Real.log (tR0 b / tR b), ?_⟩
  intro a b
  dsimp only
  have e : (tL0 a * tR0 b) / (tL a * tR b) = (tL0 a / tL a) * (tR0 b / tR b) := by
    field_simp [(hL a).ne', (hR b).ne']
  rw [e, Real.log_mul (div_pos (h0L a) (hL a)).ne' (div_pos (h0R b) (hR b)).ne', mul_add]

omit [LinearOrder α] [IsOrderedAddMonoid α] in
/-- **Two-body Ursell cross-difference vanishes on additively separable functionals (`qou-tbpl`).**
For any additively separable pair functional `f`, the mixed-minus-like cross difference
`(f p n + f n p) - (f p p + f n n)` is identically zero. -/
theorem cross_difference_eq_zero (f : N → N → α) (p n : N) (h : AddSeparable f) :
    (f p n + f n p) - (f p p + f n n) = 0 := by
  rw [cross_sum f p n h, sub_self]

end QOU.Mass.TwoBodyInterfaceBond
