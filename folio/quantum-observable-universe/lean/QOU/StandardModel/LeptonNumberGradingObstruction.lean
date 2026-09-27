/-
Copyright (c) 2026 QOU contributors. All rights reserved.

# Lepton number cannot be a ℤ-grading by smoothing count

`content/quantum-observable-universe/predicted-spectra/lepton-number-categorical-properties.md`
states the mechanism by which lepton number is supposed to become a property
of a *state*:

> **Lepton number as a `ℤ`-grading.** The Skein module `𝒦(S³; q)` admits a
> natural `ℤ`-grading by the smoothing count. Links in the nuclear sector
> have grade `0`. Each smoothing shifts the grade by `+1`. Hecke relations
> act within a fixed grade.

This matters because `Y = B - L` on the left-handed sector
(`HyperchargeBatteryReduction.lean`) needs `L` as a function of a **state**,
whereas `def:lepton-number-categorical` defines `L` as a count along a
**transition** (a β-decay).  The `ℤ`-grading is the stated bridge between
the two.

**This file proves the bridge as stated cannot exist.**  A genuine
`ℤ`-grading by smoothing count is inconsistent with the skein relation
holding in the module: the relation equates a grade-`g` element with a
grade-`(g+1)` element, so both must vanish.  Imposing the grading forces
every smoothing to be zero — i.e. it would make lepton number identically
`0`, which is the one thing it must not be.

## The argument

The Hecke/skein relation (AGENTS.md §7a) is

  `L₊ - L₋ = (q - q⁻¹) · L₀`

with `L₊`, `L₋` the two crossings and `L₀` the smoothing.  Under the claimed
grading, `L₊` and `L₋` sit in grade `g` (no new smoothing) while `L₀` sits in
grade `g + 1` (one more smoothing).  Scalars are grade-preserving, so the
right-hand side is a grade-`(g+1)` element.  The left-hand side is a
difference of grade-`g` elements, hence grade `g`.  An element lying in two
distinct graded pieces is zero.

## What is proved

* `skein_forces_vanishing` — the core obstruction, over any `AddCommGroup`.
* `skein_grading_kills_smoothing` — with the coefficient exhibited, the
  smoothing term `(q - q⁻¹) • L₀` is zero.
* `lepton_number_would_be_trivial` — if the grading held at every crossing,
  every smoothing term vanishes, so the grading cannot separate the lepton
  sector from the nuclear one.

## Honest scope

This is a **scope-(b) structural exclusion** in the sense of AGENTS.md
§"Before declaring refuted", and the justifying invariant is cited: the
defining property of a grading (distinct homogeneous components intersect in
`0`) against the inhomogeneity of the skein relation.  It excludes exactly
one thing — *`L` as a `ℤ`-grading by smoothing count* — and nothing else.

It does **not** refute lepton number, the Skein module, or the `Y = B - L`
route.  The natural repair is already present in the corpus and is a
**filtration** rather than a grading: `QOU/KnotTheory/Vassiliev/`
(`finiteTypeSubmodule_mono` is an increasing family of submodules).  A
filtration is exactly what an inhomogeneous relation admits — the skein
relation lowers the filtration degree by one, which is the Vassiliev /
finite-type filtration.  Nothing here shows that repair works; it shows the
stated one does not, and names where to look.

Base ring is a generic `AddCommGroup` / `CommRing` (§7c): no ordering, no
`Real`, no division, no characteristic hypothesis.
-/

import Mathlib.Algebra.Group.Subgroup.Basic
import Mathlib.Algebra.Module.Submodule.Basic
import Mathlib.Tactic.LinearCombination

namespace QOU.StandardModel

/-- The data the `.md` claims: a `ℤ`-indexed family of homogeneous
components of the Skein module, indexed by smoothing count.

`independent` is the defining property of a grading that we use: an element
lying in two *distinct* components is zero.  (This is strictly weaker than a
full internal direct-sum decomposition, so the obstruction below is
correspondingly strong — it does not need the full `DirectSum` structure to
bite.) -/
structure SmoothingGrading (M : Type*) [AddCommGroup M] where
  /-- The grade-`g` component: classes represented by diagrams with exactly
  `g` smoothings applied. -/
  piece : ℤ → AddSubgroup M
  /-- Distinct graded components meet only in `0`. -/
  independent : ∀ {g h : ℤ}, g ≠ h → ∀ x : M, x ∈ piece g → x ∈ piece h → x = 0

namespace SmoothingGrading

variable {M : Type*} [AddCommGroup M] (G : SmoothingGrading M)

/-- **The obstruction.**

If the two crossing classes `Lp`, `Lm` are homogeneous of grade `g` and the
skein term `S` is homogeneous of grade `g + 1`, then the skein relation
`Lp - Lm = S` forces **both** sides to vanish: `S = 0` and `Lp = Lm`.

The skein relation is inhomogeneous, so it cannot hold in a graded module
unless it is trivial. -/
theorem skein_forces_vanishing {g : ℤ} {Lp Lm S : M}
    (hp : Lp ∈ G.piece g) (hm : Lm ∈ G.piece g)
    (hS : S ∈ G.piece (g + 1))
    (skein : Lp - Lm = S) :
    S = 0 ∧ Lp = Lm := by
  have hdiff : Lp - Lm ∈ G.piece g := AddSubgroup.sub_mem _ hp hm
  have hSg : S ∈ G.piece g := skein ▸ hdiff
  have hne : g ≠ g + 1 := by simp
  have hS0 : S = 0 := G.independent hne S hSg hS
  refine ⟨hS0, ?_⟩
  have hz : Lp - Lm = 0 := by rw [skein, hS0]
  exact sub_eq_zero.mp hz

end SmoothingGrading

/-- With the skein coefficient exhibited: the smoothing term
`(q - q⁻¹) • L₀` is annihilated by the grading.

Stated over a generic commutative ring acting on `M`; scalars are
grade-preserving, so `c • L0` lies in the same component as `L0`. -/
theorem skein_grading_kills_smoothing
    {R M : Type*} [CommRing R] [AddCommGroup M] [Module R M]
    (G : SmoothingGrading M) {g : ℤ} {Lp Lm L0 : M} (c : R)
    (hp : Lp ∈ G.piece g) (hm : Lm ∈ G.piece g)
    (hS : c • L0 ∈ G.piece (g + 1))
    (skein : Lp - Lm = c • L0) :
    c • L0 = 0 ∧ Lp = Lm :=
  G.skein_forces_vanishing hp hm hS skein

/-- **Consequence: the grading would make lepton number identically zero.**

Lepton number is supposed to count smoothings, so a state with `L = k > 0`
is represented by a nonzero grade-`k` class.  But if the skein relation holds
at every crossing — which it does, it is the defining relation of the Skein
module — then every smoothing term is `0` by `skein_forces_vanishing`.

Formally: if every grade-`(g+1)` element arises as a skein term of grade-`g`
crossings, the whole positive-degree part collapses, so the grading cannot
distinguish a lepton-carrying state from a nuclear one. -/
theorem lepton_number_would_be_trivial
    {M : Type*} [AddCommGroup M] (G : SmoothingGrading M) (g : ℤ)
    (arises_as_skein :
      ∀ S ∈ G.piece (g + 1), ∃ Lp Lm : M,
        Lp ∈ G.piece g ∧ Lm ∈ G.piece g ∧ Lp - Lm = S) :
    ∀ S ∈ G.piece (g + 1), S = 0 := by
  intro S hS
  obtain ⟨Lp, Lm, hp, hm, skein⟩ := arises_as_skein S hS
  exact (G.skein_forces_vanishing hp hm hS skein).1

end QOU.StandardModel
