import Mathlib.CategoryTheory.Groupoid
import Mathlib.Data.Rat.Defs

/-!
# Conjecture: the hypercharge invariant

The framing-phase analysis (2026-06-02 hypercharge audit) derived the
Coulomb charge `Q = w/2` and the writhe-to-isospin map `w ↦ I₃`, and
*falsified* the writhe as a hypercharge assignment: the proton and
neutron share `Y = +1` while their writhes differ. The precisely
identified missing object is a second invariant, independent of the
writhe, from which `Y` is read.

This file is the formalize-first artifact for that gap (bean
`qou-q377`): a content-bearing conjecture class stating exactly what
the missing invariant must satisfy — gauge-orbit invariance, the
Gell-Mann–Nishijima relation against the given charge, and
non-factorization through the writhe — together with a *proved*
factorization criterion showing the non-factorization clause is
equivalent to the existence of a writhe-degenerate pair separated by
`Y` (the proton–neutron configuration). No instance is provided; the
open state is a content-bearing class with no instance.

This is a **primary conjecture** (AGENTS.md §3b-tax): its signature
binds no other conjecture class.

## References

- [leitner2026] Appendix: Toward the Standard Model
- [bilson-thompson2005] helon model — charge from ribbon twist
-/

namespace QOU.StandardModel

open CategoryTheory

universe u v

/-- **Factorization criterion** (proved). A function `Y` factors
through `w` iff `Y` is constant on the fibres of `w`. The reverse
direction builds the factoring map by choice on nonempty fibres. -/
theorem factors_through_iff {α β γ : Type*} [Inhabited β]
    (Y : α → β) (w : α → γ) :
    (∃ f : γ → β, ∀ X, Y X = f (w X)) ↔
      ∀ X X', w X = w X' → Y X = Y X' := by
  constructor
  · rintro ⟨f, hf⟩ X X' hw
    rw [hf X, hf X', hw]
  · intro h
    classical
    refine ⟨fun z => if hz : ∃ X, w X = z then Y hz.choose else default,
      fun X => ?_⟩
    have hex : ∃ X', w X' = w X := ⟨X, rfl⟩
    simp only [dif_pos hex]
    exact (h hex.choose X hex.choose_spec).symm

/-- **Conjecture (hypercharge invariant).** Over a groupoid `S` of
topological states with a charge function `Q` and a writhe function
`w`, there exist isospin and hypercharge functions `I₃, Y` that are
constant on gauge orbits, satisfy the Gell-Mann–Nishijima relation
`Q = I₃ + Y/2`, and — the sharp clause — `Y` does **not** factor
through the writhe. By `factors_through_iff`, the last clause is
equivalent to the existence of a writhe-degenerate pair of states
separated by `Y`; physically, the missing second invariant must
separate states the writhe cannot.

Intended instantiation: `S` = knot-state groupoid, `Q` the Coulomb
charge `w/2` reading at the hadron level, `w` the writhe. Open: no
candidate invariant currently passes; the ribbon-framing twist is a
recorded candidate direction, untested. -/
class HyperchargeInvariant (S : Type u) [Groupoid.{v} S]
    (Q : S → ℚ) (w : S → ℤ) : Prop where
  /-- Existence of gauge-invariant `I₃` and `Y` with Gell-Mann–Nishijima
  holding and `Y` not a function of the writhe. -/
  exists_hypercharge :
    ∃ I3 Y : S → ℚ,
      (∀ {X X' : S}, (X ⟶ X') → I3 X = I3 X') ∧
      (∀ {X X' : S}, (X ⟶ X') → Y X = Y X') ∧
      (∀ X, Q X = I3 X + Y X / 2) ∧
      ¬∃ f : ℤ → ℚ, ∀ X, Y X = f (w X)

/-- Any hypercharge invariant forces a writhe-degenerate pair: two
states with equal writhe but distinct hypercharge (the proton–neutron
configuration). Proved from the factorization criterion. -/
theorem HyperchargeInvariant.exists_writhe_degenerate_pair
    {S : Type u} [Groupoid.{v} S] {Q : S → ℚ} {w : S → ℤ}
    [inst : HyperchargeInvariant S Q w] :
    ∃ Y : S → ℚ, ∃ X X' : S, w X = w X' ∧ Y X ≠ Y X' := by
  obtain ⟨I3, Y, _, _, _, hnf⟩ := inst.exists_hypercharge
  refine ⟨Y, ?_⟩
  by_contra hall
  push_neg at hall
  exact hnf ((factors_through_iff Y w).mpr hall)

end QOU.StandardModel
