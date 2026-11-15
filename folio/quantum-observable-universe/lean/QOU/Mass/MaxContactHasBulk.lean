import QOU.Mass.CoordinationBulkCriterion
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

/-!
# QOU.Mass.MaxContactHasBulk — the sub-affine shape is the only one that could carry a surface term, and it is excluded on the light nuclei

`QOU.Mass.CoordinationBulkCriterion` (#6801) proved every **affine** bond count `M(A) = α·A + β`
is the `p = 1` member of `B/A = a − b·A^(−p)`, so no affine edge set is ever a surface term. It
narrowed its own conclusion to affine edge sets, reserving **max-contact sphere packing** as an
uncovered candidate whose contact numbers "are not known to be affine".

## 🛑 That reservation was wrong, and correcting it STRENGTHENS #6801

The corpus's max-contact edge set **is** the convex deltahedron, and its count **is affine**:

    computations/gap1_max_contact_a5plus.py:77-79
    # convex-deltahedron max-contact numbers (= 3A−6 for A≥3; A=2 is the single bond)
    def max_contacts(A: int) -> int:
        return 1 if A == 2 else 3 * A - 6

So the candidate #6801 reserved does not exist as implemented, and #6801's conclusion is in fact
**stronger** than it claimed: *every* coordination edge set derived anywhere on `main` is affine,
not merely the two it named. (Its remark that max-contact packings and convex deltahedra are "not
the same family in general" should also read **"not the same family above `A = 9`"** — within
`4 ≤ A ≤ 7`, where the corpus actually uses it, they agree. Both corrections are the corpus's own,
from bean `t7qv`.) Note also that `3A − 6` is derived from **Euler on a 2-sphere**, with the
packing reading asserted on top — which is exactly why it has no interior.

## What this file is: a NEW object, not a covered candidate

A *true* maximum-contact packing — one the corpus has never used — has a **sub-affine** count:

    M(A) = κ·A − c·A^θ,        κ, c > 0,   0 < θ < 1                (`subAffineBondCount`)

a linear bulk term minus a **sublinear** correction — the shape a genuine packing has:
-- Ref: [bezdek-reid2013] Thm 1(i), touching pairs < 6n − 0.926·n^{2/3} for any packing of
   n unit balls in E³, and > 6n − 7.862·n^{2/3} for fcc — so θ = 2/3 with c ∈ [0.926, 7.862].
Three consequences, all exact:

* `subAffine_perNucleon` — `ε·M(A)/A = εκ − εc·A^(θ−1)`, the `perNucleonExp` family at
  **`p = 1 − θ`**: the per-nucleon exponent is the *complement* of the count's sublinear exponent.
* `subAffine_ne_affine` — `0 < θ < 1` gives `p ≠ 1`, so this differs from every affine count's law
  at some `A`. It is the only shape considered in this corpus that escapes #6801's Part 1.
* `subAffine_hasBulk` — the implied `A_surf ∝ A^θ` satisfies `HasBulk`, which the chain
  (`A_surf = 2`) and the deltahedron (`A_surf = A`) each fail, for opposite reasons.

## 🛑 And it is EXCLUDED on the light nuclei — by a zero-fit filter already on `main`

Bean `qou-zy94` (`QOU/MassTheory/AggregatorFamilyExclusions.lean`, sorry-free) runs a
three-point determinant filter: a two-parameter family `Φ(x) = c·x + a·ψ(x)` with `ψ` **fixed in
advance** leaves one residual, so a non-vanishing `3 × 3` determinant excludes it for *every*
`(c, a)` at once, with nothing fitted. For `ψ = x^(2/3)` the normalised determinant is **0.01228**
(bond-count grid) and **0.01406** (mass-number grid) — non-zero. Its conclusion is verbatim:
*"So the volume-minus-surface form `c·x − a·x^(2/3)` is excluded — every `(c, a)`, both grids."*

**`M(A) = κA − cA^(2/3)` with `κ, c` free and `θ` fixed at `2/3` is exactly that family**, so the
exclusion applies to this file's central instantiation.

**Bean `qou-pohg` does NOT rescue it.** That bean refutes a *different* proposal — that the whole
linear-minus-concave-deficit **class** could be excluded — and it explicitly preserves these:
*"the five shape exclusions are about parameter counting, not about the concave-deficit structure,
and they all still stand. Do not read this as reopening them."* The distinction is that `ψ` is
fixed in advance here and free there.

**Scope of that exclusion, stated so it is not over-read:** it is **scope-(a)** — three
light-nucleus points, and the semi-empirical formula is calibrated for `A ≳ 20` and known to fail
on the light nuclei independently of anything in this framework, with ⁴He doubly magic. It is
nevertheless zero-fit and exact, and it is the live counterexample this shape must answer.

## What is NOT new: `p = 1/3` was already derived, from the same import

`QOU.Mass.CoordinationSurfaceDeficit.perNucleon_surfaceLaw` (sorry-free, mine, #6761) already
gives `B/A = εk/2 − (εc(k−k')/2)·A^(−1/3)` from `A_surf = c·A^(2/3)`. Since
`M = κA − cA^θ` and `M = kA/2 − (k−k')A_surf/2` are the same equation, **`θ = 2/3` and
`A_surf ∝ A^(2/3)` are the same import.** So this file does **not** remove an assumption that
`SurfaceExponentIsDimension` had to make; what changes is only that the *count* rather than the
*surface law* is the primitive. Do not write it as a derivation of `p = 1/3`.

## The exponent is `1/d`, and four recorded objections to reading that as a dimension

`maxContact_exponent_eq_inv_dim`: `θ = (d−1)/d` gives `p = 1/d`, and at `d = 3` that is `1/3`
(`maxContact_d3_eq_semf`); `d = 1` returns `p = 1`, the production chain, so the chain is the
family's degenerate surface-free member rather than an outsider. The corpus objects to the
dimensional reading in four distinct ways, and all four stand:

1. **The exponent is imported.** *"The ⅓ there is imported from 3-dimensional sphere packing,
   i.e. geometry, which is exactly what this attack was not allowed to use"*, and the framework's
   fixed "3"s could source a cube root *"only via an undeclared '3 colours ↔ 3 spatial dimensions'
   identification, which the corpus does not make"* (2026-07-13 packing-exponent audit).
2. **The genericity guard asks for the argument to be internal.** `qou-rav3` endorses
   derive-then-check but asks for *"a packing argument inside the framework"* — a literature
   citation is not one.
3. **The ambient geometry is hyperbolic, not Euclidean.** A compact *Euclidean* cluster has
   `A_surf ∝ A^(2/3)`; in `H³` an extensive volume gives radius `R ∼ ½ ln V`, i.e. `ln A`, and the
   corpus measures that using the geometry consistently **costs 2.64×** in accuracy
   (`docs/coordination/sm-26-parameter-chip-away.md`). This is the sharpest structural objection.
4. **The corpus derives three-dimensionality nowhere.** Every hit is the explicit statement that
   the identification is not made.

## Scope

* **Proved here:** everything above, for arbitrary `κ, c > 0` and `0 < θ < 1`. Exact, no fit;
  `κ` and `c` stay free throughout, so no amplitude is chosen against data.
* **Cited without a held source, and flagged as such.** The sharp forms of the contact-number
  asymptotic (Harborth in the plane; Bezdek's bound in space) are **not held in `library/` and
  not registered in `references.ts`** — checked across all four library tiers, which return only
  homonyms and bibliography lines. So they are deliberately **not** cited here, and no constant is
  quoted from them. `θ` is a free parameter of every theorem; the only input used is the
  elementary statement that a compact `d`-dimensional cluster has boundary `∼ A^((d−1)/d)`, and it
  is instantiated visibly rather than assumed silently.
* **NOT derived:** that the substrate emits any such packing. That is `qou-brng`'s open input.
* **Verdict: this is a NEGATIVE tranche.** The sub-affine shape is the only one that could carry a
  surface term, and it is excluded on the light nuclei (scope-(a), zero-fit), selected by only one
  of five analysis variants on the full chart, and its exponent is an external import the corpus
  objects to four ways. The Lean below is correct and the shape is worth having named; what it
  does not do is supply the framework a surface term.

Ground ring `ℝ` (§7c: archimedean — real powers and limits).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationBulkCriterion.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationSurfaceDeficit.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/MassTheory/AggregatorFamilyExclusions.lean
-- Ref: [leitner2026] computations/gap1_max_contact_a5plus.py (max_contacts = 3A - 6, affine)
-/

namespace QOU.Mass.MaxContactHasBulk

open Filter QOU.Mass.SurfaceExponentIsDimension QOU.Mass.CoordinationBulkCriterion

/-- The **sub-affine** bond count: a linear bulk term minus a sublinear correction,
`M(A) = κ·A − c·A^θ`. This is the shape of a maximum-contact packing's contact number. -/
noncomputable def subAffineBondCount (κ c θ A : ℝ) : ℝ := κ * A - c * A ^ θ

/-- **The sub-affine per-nucleon law has exponent `1 − θ`.** The per-nucleon exponent is the
complement of the count's sublinear exponent — this is the whole mechanism. -/
theorem subAffine_perNucleon (ε κ c θ A : ℝ) (hA : 0 < A) :
    ε * subAffineBondCount κ c θ A / A = perNucleonExp (ε * κ) (ε * c) (1 - θ) A := by
  unfold subAffineBondCount perNucleonExp
  have hexp : -(1 - θ) = θ - 1 := by ring
  have hpow : A ^ (-(1 - θ)) = A ^ θ / A := by
    rw [hexp, Real.rpow_sub hA, Real.rpow_one]
  rw [hpow]
  field_simp

/-- **The sub-affine shape escapes the affine exclusion.** For `0 < θ < 1` its per-nucleon
exponent `1 − θ` is not `1`, so by `perNucleonExp_exponent_inj` it differs at some `A` from the
`p = 1` law every affine bond count produces. This is the first shape in the corpus that does. -/
theorem subAffine_ne_affine (ε κ c θ : ℝ) (hb : ε * c ≠ 0) (hθ0 : 0 < θ) (_hθ1 : θ < 1) :
    ∃ A : ℝ, 0 < A ∧
      perNucleonExp (ε * κ) (ε * c) (1 - θ) A ≠ perNucleonExp (ε * κ) (ε * c) 1 A := by
  by_contra hcon
  push_neg at hcon
  have h1 : (1 : ℝ) - θ ≠ 1 := by intro h; simp at h; linarith
  exact h1 (perNucleonExp_exponent_inj (ε * κ) (ε * c) (1 - θ) 1 hb (fun A hA => hcon A hA))

/-- **The surface count a sub-affine bond count implies has a bulk.** Writing the correction as
`CoordinationSurfaceDeficit`'s deficit `(k − k')·A_surf/2 = c·A^θ` gives
`A_surf = (2c/(k − k'))·A^θ`, which satisfies `HasBulk` for `0 < θ < 1`. So the sub-affine shape
passes the criterion that the chain and the deltahedron each failed — the only shape considered
in this corpus that does. -/
theorem subAffine_hasBulk (c' θ : ℝ) (hc : 0 < c') (hθ0 : 0 < θ) (hθ1 : θ < 1) :
    HasBulk (fun A => c' * A ^ θ) :=
  powerSurface_hasBulk c' θ hc hθ0 hθ1

/-! ## The exponent is the inverse dimension -/

/-- **`p = 1/d`, derived rather than assumed.** A compact `d`-dimensional packing has boundary of
dimension `d − 1`, so its contact count's sublinear exponent is `θ = (d−1)/d`; substituting into
`subAffine_perNucleon` gives per-nucleon exponent `1 − θ = 1/d`. `SurfaceExponentIsDimension`
*hypothesised* this reading. It is NOT thereby derived: `CoordinationSurfaceDeficit` already had
`p = 1/3` from `A_surf = c·A^(2/3)`, which is the same geometric import written the other way
round. What changes is which of the two is the primitive. -/
theorem maxContact_exponent_eq_inv_dim (d : ℝ) (hd : d ≠ 0) :
    1 - (d - 1) / d = 1 / d := by
  field_simp
  ring

/-- **At `d = 3` the exponent is `1/3` — the SEMF surface exponent.** The packing literature gives
`θ = 2/3` for congruent spheres in 3-space (elementary boundary scaling `A_surf ∼ A^((d−1)/d)` gives `θ = 2/3` for a compact
three-dimensional cluster; this is that value instantiated, so the one geometric input is visible
in the statement rather than buried. No constant from the packing literature is used — none is
held in `library/` or registered in `references.ts`. -/
theorem maxContact_d3_eq_semf (ε κ c A : ℝ) (hA : 0 < A) :
    ε * subAffineBondCount κ c ((2 : ℝ) / 3) A / A
      = perNucleonExp (ε * κ) (ε * c) (1 / 3) A := by
  rw [subAffine_perNucleon ε κ c ((2 : ℝ) / 3) A hA]
  norm_num

/-- The `d = 2` case, `θ = 1/2`, giving per-nucleon exponent `1/2`. Recorded as a cross-check that
the mechanism is dimensional bookkeeping and not a coincidence at 3. -/
theorem maxContact_d2_exponent (ε κ c A : ℝ) (hA : 0 < A) :
    ε * subAffineBondCount κ c ((1 : ℝ) / 2) A / A
      = perNucleonExp (ε * κ) (ε * c) (1 / 2) A := by
  rw [subAffine_perNucleon ε κ c ((1 : ℝ) / 2) A hA]
  norm_num

end QOU.Mass.MaxContactHasBulk
