import QOU.Machinery.HeckeH3AlgebraInstance
import QOU.Machinery.HeckeTowerBasicConstruction
import Mathlib.Tactic.IntervalCases

/-!
# A rank-bounded braided presentation — and the corpus's first content-bearing instance

`HeckeBraidedCategory.HeckeBraidedPresentation` quantifies its three relations
over **all** `i : ℕ`, i.e. it describes `H_∞`. Two facts about that, both proved
in `HeckeTowerBasicConstruction`:

* it is satisfiable **degenerately** — a single element meeting the quadratic
  gives an instance via the constant family, with braid and far-commutation
  `rfl` (`constant_generator_presentation`);
* and no finite `H_n` satisfies it with its true generators
  (`far_commute_zero`; the same obstruction, covering both padding routes, is
  recorded in prose in `HeckeH3AlgebraLaws`'s honesty note, which predates this
  file — the Lean version machine-checks half of what was already known there).

Together those say the class cannot be given a **useful** instance: the reachable
ones carry no Hecke content, and the contentful ones do not exist.

`HeckeBraidedPresentationOfRank` fixes that by bounding the relations to a rank
`n`, which is what a finite Hecke algebra actually satisfies. It is a NEW class
rather than a change to the old one: twelve files bind
`HeckeBraidedPresentation`, and mutating its signature is a refactor whose blast
radius is unrelated to the point being made here.

## What this buys

`heckePresentationOfRank_H3A` is an instance with **real content**: the genuine
`H₃(q)` on the six-element normal-form basis, its two true generators `σ₀` and
`σ₁`, the Hecke quadratic for both, and the braid relation `σ₀σ₁σ₀ = σ₁σ₀σ₁`.
Nothing is padded and nothing is constant — `σ₀` and `σ₁` are distinct and do
not commute.

It is, as far as the corpus goes, the first presentation instance of any kind.
The concrete layer it is built from (`H3A`, `mulNF`, the proved laws) is
pre-existing; what is new is that a presentation class now has somewhere to land.

## What it does NOT do

It does not give `HeckeCosetSpanning` an instance. That class binds the
**unbounded** presentation, so re-pointing it at this one is a further change,
deliberately not made here — and the spanning statement itself would still need
proving for `H₂ ⊂ H₃` afterwards.
-/

namespace QOU.Machinery.HeckeRank

open QOU.Machinery.H3

variable {R : Type*} [Field R]

/-- **Rank-bounded braided presentation.** The three Hecke relations, each
guarded so it only speaks about generators that exist at rank `n`:
`σ₀, …, σ_{n-2}` for `H_n`.

Compare `HeckeBraidedCategory.HeckeBraidedPresentation`, whose unguarded `∀ i`
forces an infinite generator family — the reason it has no contentful instance.
The guards here are exactly what makes a finite algebra able to satisfy it. -/
class HeckeBraidedPresentationOfRank (q : R) (n : ℕ) (H : Type*)
    [Ring H] [Algebra R H] (σ : ℕ → H) : Prop where
  /-- Hecke quadratic, for generators present at rank `n`. -/
  hecke_quadratic : ∀ i, i + 1 < n → σ i * σ i = (q - q⁻¹) • σ i + 1
  /-- Braid relation, for adjacent pairs both present at rank `n`. -/
  braid_adjacent : ∀ i, i + 2 < n → σ i * σ (i + 1) * σ i = σ (i + 1) * σ i * σ (i + 1)
  /-- Far commutation, for non-adjacent pairs both present at rank `n`. -/
  far_commute : ∀ i j, i + 1 < j → j + 1 < n → σ i * σ j = σ j * σ i

/-- The unbounded class implies the bounded one at every rank — the guards only
discard obligations. So existing consumers lose nothing by moving over. -/
theorem ofRank_of_unbounded {q : R} {H : Type*} [Ring H] [Algebra R H]
    {σ : ℕ → H} [inst : QOU.Machinery.HeckeBraidedCategory.HeckeBraidedPresentation R q H σ]
    (n : ℕ) : HeckeBraidedPresentationOfRank q n H σ where
  hecke_quadratic i _ := inst.hecke_quadratic i
  braid_adjacent i _ := inst.braid_adjacent i
  far_commute i j hij _ := inst.far_commute i j hij

/-! ## The instance: genuine H₃(q) at rank 3 -/

/-- `σ₀` as an element of the normal-form algebra — basis index 1. -/
def s0 (h : R) : H3A R h := ⟨![0, 1, 0, 0, 0, 0]⟩

/-- `σ₁` as an element of the normal-form algebra — basis index 2. -/
def s1 (h : R) : H3A R h := ⟨![0, 0, 1, 0, 0, 0]⟩

/-- The generator family. At rank 3 the guards constrain only `σ 0` and `σ 1`;
indices past the rank are unconstrained, so they are sent to `0` rather than
padded with a real generator — padding is exactly what the unbounded class
cannot survive. -/
def gen (h : R) : ℕ → H3A R h := fun i => if i = 0 then s0 h else if i = 1 then s1 h else 0

theorem s0_mul_s0 (h : R) : s0 h * s0 h = h • s0 h + 1 := by
  apply H3A.ext; funext i; fin_cases i <;>
    simp [s0, mulNF, mulσ₀, mulσ₁, unitNF]

theorem s1_mul_s1 (h : R) : s1 h * s1 h = h • s1 h + 1 := by
  apply H3A.ext; funext i; fin_cases i <;>
    simp [s1, mulNF, mulσ₀, mulσ₁, unitNF]

theorem braid_s0_s1 (h : R) : s0 h * s1 h * s0 h = s1 h * s0 h * s1 h := by
  apply H3A.ext; funext i; fin_cases i <;>
    simp [s0, s1, mulNF, mulσ₀, mulσ₁]

/-- **The corpus's first content-bearing presentation instance.** Genuine
`H₃(q)` on the six-element normal-form basis, with its two true generators: the
Hecke quadratic for each and the braid relation between them. Nothing padded,
nothing constant. -/
instance heckePresentationOfRank_H3A (q : R) :
    HeckeBraidedPresentationOfRank q 3 (H3A R (q - q⁻¹)) (gen (q - q⁻¹)) where
  hecke_quadratic i hi := by
    have hlt : i < 2 := by omega
    interval_cases i
    · simpa [gen] using s0_mul_s0 (R := R) (q - q⁻¹)
    · simpa [gen] using s1_mul_s1 (R := R) (q - q⁻¹)
  braid_adjacent i hi := by
    have hlt : i < 1 := by omega
    interval_cases i
    · simpa [gen] using braid_s0_s1 (R := R) (q - q⁻¹)
  far_commute i j hij hj := by omega

/-! ## The instance is not the degenerate one

`constant_generator_presentation` shows the unbounded class is satisfiable by a
constant family, where every relation is `rfl` and nothing fails to commute. An
instance is worth having only if it is not of that shape, so that is checked
rather than assumed. -/

/-- The two generators are distinct. -/
theorem s0_ne_s1 (h : R) [Nontrivial R] : s0 h ≠ s1 h := by
  intro hEq
  have h1 := congrArg (fun x => H3A.v x 1) hEq
  simp [s0, s1] at h1

/-- **The two generators do not commute.** This is what the constant family
cannot reproduce: there, `far_commute` and `braid_adjacent` hold by `rfl`
precisely because everything commutes. Here the braid relation
`σ₀σ₁σ₀ = σ₁σ₀σ₁` is a genuine identity between two *different* products. -/
theorem s0_mul_s1_ne_s1_mul_s0 (h : R) [Nontrivial R] :
    s0 h * s1 h ≠ s1 h * s0 h := by
  intro hEq
  have h3 := congrArg (fun x => H3A.v x 3) hEq
  simp [s0, s1, mulNF, mulσ₀, mulσ₁] at h3

end QOU.Machinery.HeckeRank
