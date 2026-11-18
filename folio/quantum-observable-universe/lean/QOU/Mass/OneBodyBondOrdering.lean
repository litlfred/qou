import Mathlib.Order.Basic
import Mathlib.Order.Lattice

/-!
# A one-body bond fixes the two-nucleon ORDERING, not only its sign

Bean `qou-ales` (extension of step 11 to the nn / pn systems).

`QOU.Mass.InterfaceVertexArity.no_signMixed_of_oneBody` proves that a pair functional which
depends on only one of its two nucleon arguments cannot put the unlike pair on the opposite
side of zero from both like pairs. This file proves the corresponding statements about the
**order** of the three numbers `f p p`, `f n n`, `f p n`, which is strictly more: the measured
nuclear pattern (deuteron bound, diproton and dineutron not) is excluded by these lemmas
whatever the signs, and so is every arrangement in which the unlike pair is a strict extreme
or sits strictly between the like pairs.

Measured context (probe `computations/probes/gamma_gamma_nn_pn_selection_probe.py`, proton
pin, convention D, 60 dps): with the γγ bond selected by reading 3 (`(σ₂σ₃⁻¹)³` at the
canonical placement), `B_pp = B_np = −4.469 keV` and `B_nn = B_pn = −2.583 keV` — the
one-body pattern exactly, with `B_pn` tied to `B_nn`. The one-body premise itself is step 11's
junction-factorisation result (`response_oneBody_of_junctionFactorisation`, conditional on
connected-sum multiplicativity); it is a HYPOTHESIS here, and nothing below asserts it.

Stated over an arbitrary index type `N` with two named elements and any linear order `α`
(§7c: no `ℝ` is needed), so it applies to `InterfaceVertexArity.Nucleon` and to binding,
trace ratio or response alike. Sorry-free.
-/

namespace QOU.Mass.OneBodyBondOrdering

variable {N α : Type*}

/-- A pair functional is **one-body** if it is a function of one argument only — the right
one (`V1`, `V2` placements) or the left one (`V3`, `V4`). -/
def OneBody (f : N → N → α) : Prop :=
  (∃ g : N → α, ∀ a b, f a b = g b) ∨ (∃ g : N → α, ∀ a b, f a b = g a)

/-- **The unlike pair is always tied to a like pair.** Right-dependent: `f p n = f n n`;
left-dependent: `f p n = f p p`. -/
theorem pn_eq_like (f : N → N → α) (p n : N) (h : OneBody f) :
    f p n = f n n ∨ f p n = f p p := by
  rcases h with ⟨g, hg⟩ | ⟨g, hg⟩
  · exact Or.inl (by rw [hg, hg])
  · exact Or.inr (by rw [hg, hg])

variable [LinearOrder α]

/-- **The unlike pair cannot be strictly the largest.** With `f` the binding, the deuteron can
never be more bound than both the diproton and the dineutron. -/
theorem not_pn_strict_max (f : N → N → α) (p n : N) (h : OneBody f) :
    ¬ (f p p < f p n ∧ f n n < f p n) := by
  rintro ⟨h1, h2⟩
  rcases pn_eq_like f p n h with e | e <;> rw [e] at h1 h2 <;> exact lt_irrefl _ (by assumption)

/-- **Nor strictly the smallest.** -/
theorem not_pn_strict_min (f : N → N → α) (p n : N) (h : OneBody f) :
    ¬ (f p n < f p p ∧ f p n < f n n) := by
  rintro ⟨h1, h2⟩
  rcases pn_eq_like f p n h with e | e <;> rw [e] at h1 h2 <;> exact lt_irrefl _ (by assumption)

/-- **Nor strictly between the like pairs**, in either orientation. -/
theorem not_pn_strictly_between (f : N → N → α) (p n : N) (h : OneBody f) :
    ¬ (f p p < f p n ∧ f p n < f n n) ∧ ¬ (f n n < f p n ∧ f p n < f p p) := by
  refine ⟨?_, ?_⟩ <;> rintro ⟨h1, h2⟩ <;>
    rcases pn_eq_like f p n h with e | e <;> rw [e] at h1 h2 <;>
    exact lt_irrefl _ (by assumption)

omit [LinearOrder α] in
/-- **Charge independence collapses the whole table.** On a two-element index set, a one-body
functional with `f p p = f n n` is constant on all four ordered channels: charge independence
and charge symmetry leave no room for an unlike-pair difference. -/
theorem chargeIndependent_const (f : N → N → α) (p n : N) (hpn : ∀ x : N, x = p ∨ x = n)
    (h : OneBody f) (hci : f p p = f n n) : ∀ a b, f a b = f p p := by
  intro a b
  rcases h with ⟨g, hg⟩ | ⟨g, hg⟩
  · have hgp : g p = g n := by rw [← hg p p, ← hg n n]; exact hci
    rw [hg, hg p p]
    rcases hpn b with rfl | rfl
    · rfl
    · exact hgp.symm
  · have hgp : g p = g n := by rw [← hg p p, ← hg n n]; exact hci
    rw [hg, hg p p]
    rcases hpn a with rfl | rfl
    · rfl
    · exact hgp.symm

/-- **The hypothesis is load-bearing.** The measured ordering pattern — unlike pair strictly
above both like pairs — is realised by a two-body functional, so `not_pn_strict_max` is a
statement about one-body functionals and not a vacuous one. -/
theorem strict_max_realisable_two_body :
    ∃ f : Bool → Bool → ℕ, f true true < f true false ∧ f false false < f true false :=
  ⟨fun a b => if a = b then 0 else 1, by decide, by decide⟩

/-- **And that functional is not one-body**, so the exclusion is exactly the one-body
premise. -/
theorem strict_max_witness_not_oneBody :
    ¬ OneBody (fun a b : Bool => if a = b then (0 : ℕ) else 1) := fun h =>
  not_pn_strict_max _ true false h ⟨by decide, by decide⟩

omit [LinearOrder α] in
/-- **All pair evaluations agree under a charge-independent one-body functional (`qou-zrbv`).**
For any two pairs `(a₁, b₁)` and `(a₂, b₂)` on a two-element nucleon type `{p, n}`,
a charge-independent one-body functional satisfies `f a₁ b₁ = f a₂ b₂`. -/
theorem chargeIndependent_eq_pairs (f : N → N → α) (p n : N) (hpn : ∀ x : N, x = p ∨ x = n)
    (h : OneBody f) (hci : f p p = f n n) (a₁ b₁ a₂ b₂ : N) :
    f a₁ b₁ = f a₂ b₂ := by
  rw [chargeIndependent_const f p n hpn h hci a₁ b₁,
    chargeIndependent_const f p n hpn h hci a₂ b₂]

end QOU.Mass.OneBodyBondOrdering
