import QOU.Machinery.HeckeBraidedCategoryScaffold

/-!
# `MarkovStabilization` is a hypothesis on free trace parameters

`MarkovStabilization R q Hn Hn1 σn σn1 ι trn trn1` takes the two "Markov
traces" `trn : Hn → R`, `trn1 : Hn1 → R` as **arbitrary functions**: nothing
in its signature requires them to be linear, cyclic, or Markov. Its one field
`trn1 (ι x) = trn x` is therefore a compatibility condition on whatever
functions are supplied, not a statement about the Hecke tower.

**What is proved (sorry-free).**
* `presentation_const` — the unbounded `HeckeBraidedPresentation` is
  inhabited by any constant generator family `σ i = s` with `s` satisfying the
  Hecke quadratic (braid and far commutation are then trivial). Concretely
  `s = 2 ∈ ℚ` at `q = 2`. (So the source docstring's remark that the unbounded
  class "has no contentful instance" is right only in the sense that constant
  families are degenerate: they collapse the braid group to an abelian quotient.)
* `markovStabilization_id` — with `Hn = Hn1 = ℚ`, `ι = id`, `trn = trn1 = id`
  the class holds.
* `not_markovStabilization_zero` — with the same presentation data but
  `trn = 0`, `trn1 = id` it fails.
So the class is neither a theorem nor refutable for all parameters; it is a
parameter property.

**What is not proved.** General-`n` stabilization of the actual Ocneanu/Jones
Markov trace along `H_n(q) ⊂ H_{n+1}(q)` (the open item, bean `qou-ep0a`). To
become a real debt item the class must bind `trn`, `trn1` to the Markov trace
(e.g. via `QOU.Machinery.MarkovTrace` plus the Markov reduction field); that is
a refactor needing owner approval.

-- Ref: [leitner2026] QOU.Machinery.HeckeBraidedCategoryScaffold; [jones1987]
-- V. F. R. Jones, Hecke algebra representations of braid groups and link
-- polynomials, Ann. Math. 126 (1987), §5 (Ocneanu trace, `tr(ι x) = tr x`).
-/

namespace QOU.Machinery.HeckeBraidedCategory.Instances

open QOU.Machinery.HeckeBraidedCategory

/-- A constant generator family satisfying the Hecke quadratic inhabits the
unbounded braided presentation. -/
theorem presentation_const {R : Type*} [Field R] {q : R} {H : Type*} [Ring H]
    [Algebra R H] (s : H) (hs : s * s = (q - q⁻¹) • s + 1) :
    HeckeBraidedPresentation R q H (fun _ => s) where
  hecke_quadratic _ := hs
  braid_adjacent _ := rfl
  far_commute _ _ _ := rfl

/-- `2 ∈ ℚ` satisfies the Hecke quadratic at `q = 2`: `4 = (2 − ½)·2 + 1`. -/
theorem two_hecke : (2 : ℚ) * 2 = ((2 : ℚ) - (2 : ℚ)⁻¹) • (2 : ℚ) + 1 := by
  norm_num

instance presentation_two : HeckeBraidedPresentation ℚ 2 ℚ (fun _ => (2 : ℚ)) :=
  presentation_const (2 : ℚ) two_hecke

/-- Inhabited: identity traces along the identity inclusion. -/
theorem markovStabilization_id :
    MarkovStabilization ℚ 2 ℚ ℚ (fun _ => (2 : ℚ)) (fun _ => (2 : ℚ))
      (AlgHom.id ℚ ℚ) id id :=
  ⟨fun _ => rfl⟩

/-- Not universal: the zero function and the identity are not compatible. -/
theorem not_markovStabilization_zero :
    ¬ MarkovStabilization ℚ 2 ℚ ℚ (fun _ => (2 : ℚ)) (fun _ => (2 : ℚ))
      (AlgHom.id ℚ ℚ) (fun _ => 0) id := by
  intro h
  have := h.stabilizes 1
  simp at this

end QOU.Machinery.HeckeBraidedCategory.Instances
