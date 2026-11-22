/-
Copyright (c) 2026 litlfred. All rights reserved.

# Typed interface to the cited RSZ isoformal-classification statements

Ramis–Sauloy–Zhang, *Local analytic classification of q-difference equations*
(Astérisque 355, `library/arxiv-0903.0853v3/0903.0853v3.pdf`), §3.3.

**Why this file exists.** Prose citations do not typecheck. The corpus carried,
from 2026-08-01, the chain

    C1 has slope ½  ⇒  RSZ level d = 2  ⇒  B_{q,2}  ⇒  F(P₁,P₂) ≅ ℂ²
                    ⇒  two Stokes multipliers,

which drove a staged work plan. Reading §3.3 shows two of those links misread the
source:

* §3.3 is titled *"Explicit description of `F(P₁,…,P_k)` in the case of
  **integral slopes**"*. C1's slope `½` is not integral.
* RSZ p.38 defines the level as `d := μ₂ − μ₁ ∈ ℕ` — the **difference between
  two consecutive slopes** — not the denominator of a single slope.

Both errors are invisible in prose and mechanical in a type. This file states the
cited assertions so that supplying a single slope, or a non-integral one, cannot
elaborate.

**Two tiers, deliberately not blurred.**

* *Provable outright* (here, proved): the dimension formula of Thm 3.3.5 as a
  definition, its vanishing at `k = 1`, and the level as a genuinely binary
  operation.
* *External input* (here, a hypothesis class carrying real content — never an
  empty marker): the standing assumptions of §3.3.

This file does **not** re-prove RSZ and claims no Stokes multiplier. It fixes the
*interfaces* of what the corpus cites.

§7c: `ℤ`-valued slopes and ranks; pure arithmetic, nothing archimedean.
Sorry-free.

-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853 (§3.3, Thm 3.3.5)
-- Ref: [leitner2026] docs/audits/2026-08-08-w2-stokes-qborel-attack-plan.md
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Fin
import Mathlib.Algebra.Order.Ring.Int
import Mathlib.Tactic.Ring

namespace QOU.MathlibExt.RSZ

open Finset

/-- **RSZ's level**, p.38: `d := μ₂ − μ₁`, the difference between two consecutive
slopes of the filtration.

The arity is the point. This is a **binary** operation on slopes; there is no
"level of a slope". A single slope cannot be supplied, so the misreading
"slope `½` ⇒ level `2`" is not expressible here. -/
def rszLevel (μ₁ μ₂ : ℤ) : ℤ := μ₂ - μ₁

/-- Consecutive slopes are strictly increasing, so the level is positive. -/
theorem rszLevel_pos {μ₁ μ₂ : ℤ} (h : μ₁ < μ₂) : 0 < rszLevel μ₁ μ₂ := by
  simpa [rszLevel] using sub_pos.mpr h

/-- The level is *not* a function of one slope: it is translation-invariant, so
knowing `μ₂` alone determines nothing. -/
theorem rszLevel_translation_invariant (μ₁ μ₂ c : ℤ) :
    rszLevel (μ₁ + c) (μ₂ + c) = rszLevel μ₁ μ₂ := by
  simp [rszLevel]

/-- **RSZ Thm 3.3.5.** `F(P₁,…,P_k)` is an affine space of dimension
`∑_{i<j} rᵢ rⱼ (μⱼ − μᵢ)`. Stated as the dimension formula itself. -/
def rszIsoformalDim (k : ℕ) (r : Fin k → ℤ) (μ : Fin k → ℤ) : ℤ :=
  ∑ i : Fin k, ∑ j : Fin k, if i < j then r i * r j * rszLevel (μ i) (μ j) else 0

/-- **The fact that decides the C1 question.** With a single slope there are no
pairs `i < j`, so the isoformal space is a point: dimension `0`. A pure isoclinic
module has no isoformal moduli, hence no Stokes data to extract. -/
@[simp] theorem rszIsoformalDim_one (r μ : Fin 1 → ℤ) :
    rszIsoformalDim 1 r μ = 0 := by
  simp [rszIsoformalDim]

/-- Degenerate case, for completeness: no slopes, no moduli. -/
@[simp] theorem rszIsoformalDim_zero (r μ : Fin 0 → ℤ) :
    rszIsoformalDim 0 r μ = 0 := by
  simp [rszIsoformalDim]

/-- **The standing hypotheses of §3.3**, as a class carrying its actual content.

Deliberately *not* an empty marker: `two_or_more` and `integral` are exactly the
assumptions the C1 chain dropped, and `strictly_increasing` is RSZ's `μ₁ < ⋯ < μ_k`.
A consumer that cites §3.3 takes this as an instance binder and thereby inherits
all three in its own type. -/
class IntegralSlopeSetting (k : ℕ) (μ : Fin k → ℤ) : Prop where
  /-- §3.3 needs at least two slopes: the level `μ₂ − μ₁` presupposes a pair. -/
  two_or_more : 2 ≤ k
  /-- RSZ's `μ₁ < ⋯ < μ_k`. -/
  strictly_increasing : ∀ i j : Fin k, i < j → μ i < μ j
  -- NOTE: §3.3's *integral*-slope hypothesis needs no field: it is carried by
  -- the type `μ : Fin k → ℤ`. A non-integral slope (C1's `½`) simply cannot be
  -- supplied. The ramified/non-integral setting is Bugeaud [14], not this class.

/-- **A single slope cannot satisfy §3.3's hypotheses** — mechanically. This is
the C1 situation: one edge in the Newton polygon at `∞`, hence `k = 1`. -/
theorem not_integralSlopeSetting_one (μ : Fin 1 → ℤ) :
    ¬ IntegralSlopeSetting 1 μ := by
  intro h
  have := h.two_or_more
  omega

/-- Under §3.3's hypotheses the isoformal space of a *two*-slope class has the
expected dimension `r₀ r₁ (μ₁ − μ₀)` — the only case in which the "`ℂ^d`"
description of the corpus could have applied. -/
theorem rszIsoformalDim_two (r μ : Fin 2 → ℤ) :
    rszIsoformalDim 2 r μ = r 0 * r 1 * rszLevel (μ 0) (μ 1) := by
  simp [rszIsoformalDim, Fin.sum_univ_two]

/-- **C1's `∞` has NO Stokes data — the instance, not just the general lemma.**

`L1`'s Newton polygon at `∞` has a single edge `(r,d) = (2,1)`: slope `½` with
multiplicity `2`, pure isoclinic.  After the ramified pullback `ζ² = x` — which
`QOU.QBeta.ramified_qBorel_budget` showed is the only pairing with sub-quadratic
leftover — the data is `k = 1`, rank `2`, slope `1`.  The isoformal space is a
**point**.

So there is no **local isoformal** q-Stokes multiplier at C1's `∞` to compute.
Independently: RSZ's Stokes matrices are unipotent automorphisms inducing the
identity on `gr M₀` (§4.4, Thm 5.5.7), and with one slope there is no
strictly-upper-triangular part — the Stokes group is trivial.

**Do not read this as "C1 has no Stokes multipliers".**  Two different objects
share the name, and only the first is zero-dimensional:

* *local isoformal moduli at `∞`* — `F(P₁,…,P_k)` at a single point.  **This
  lemma. Dimension 0.**
* *the connection-matrix Stokes multipliers* — the data in `P = Y₀⁻¹Y_∞` between
  the theta-normalised solutions at `0` and at `∞`, functions of the invariant
  `χ = P₀₀P₁₁/(P₀₁P₁₀)`.  **Global, live, and open** (bean `qou-wgnx`; the
  connection matrix and `χ` are already built).  A dimension count at one point
  says nothing about it.

**This instance exists because the general lemma above was not enough.**
`rszIsoformalDim_one`'s docstring already said "no Stokes data to extract", and I
still wrote "the Stokes multiplier is the remaining open item" three times across
PRs #4771 and #4783.  A lemma naming C1 is harder to walk past than a lemma about
an abstract `k = 1`.  Retraction:
[`2026-08-08-c1-infinity-has-no-stokes-multiplier.md`](../../../../../docs/audits/2026-08-08-c1-infinity-has-no-stokes-multiplier.md). -/
theorem c1_infinity_isoformalDim_eq_zero :
    rszIsoformalDim 1 (fun _ => 2) (fun _ => 1) = 0 :=
  rszIsoformalDim_one _ _

/-- The same conclusion for **any** rank and slope, so it cannot be read as an
artefact of the particular numbers `(2, 1)`: what kills the Stokes data is `k = 1`
alone. -/
theorem isoformalDim_eq_zero_of_pure (r μ : Fin 1 → ℤ) :
    rszIsoformalDim 1 r μ = 0 :=
  rszIsoformalDim_one r μ

/-- Under `IntegralSlopeSetting k μ`, every pair `i < j` has strictly positive
    RSZ level `0 < rszLevel (μ i) (μ j)`. -/
theorem rszLevel_pos_of_integralSlopeSetting {k : ℕ} {μ : Fin k → ℤ}
    [hμ : IntegralSlopeSetting k μ] {i j : Fin k} (hij : i < j) :
    0 < rszLevel (μ i) (μ j) :=
  rszLevel_pos (hμ.strictly_increasing i j hij)

/-- In the two-slope integral setting (`k = 2`) with positive ranks `1 ≤ r 0`
    and `1 ≤ r 1`, the isoformal space has strictly positive dimension
    `0 < rszIsoformalDim 2 r μ`. -/
theorem rszIsoformalDim_two_pos (r μ : Fin 2 → ℤ)
    [hμ : IntegralSlopeSetting 2 μ] (hr0 : 1 ≤ r 0) (hr1 : 1 ≤ r 1) :
    0 < rszIsoformalDim 2 r μ := by
  rw [rszIsoformalDim_two]
  have h01 : (0 : Fin 2) < 1 := by decide
  have hlev : 0 < rszLevel (μ 0) (μ 1) := rszLevel_pos_of_integralSlopeSetting h01
  have hr0' : 0 < r 0 := by omega
  have hr1' : 0 < r 1 := by omega
  exact mul_pos (mul_pos hr0' hr1') hlev

/-- **Tier B (§3b conditional class): RSZ Theorem 3.3.5 isoformal classification.**
    Carries the standing hypotheses of §3.3 (`2 ≤ k`, integral slopes `μ : Fin k → ℤ`,
    and strict slope ordering `μ₁ < ⋯ < μ_k`) together with positive slope-piece ranks
    `1 ≤ r i` and the affine-moduli dimension `moduliDim = rszIsoformalDim k r μ`.
    Any downstream consumer taking `[RSZIsoformalClassification k r μ]` inherits the
    integral-slope and `2 ≤ k` hypotheses in its type, making single-slope or
    non-integral misuse a type error. -/
class RSZIsoformalClassification (k : ℕ) (r μ : Fin k → ℤ) : Prop
    extends IntegralSlopeSetting k μ where
  /-- Each isoclinic summand `P_i` has positive rank `1 ≤ r_i`. -/
  ranks_pos : ∀ i : Fin k, 1 ≤ r i

/-- Under `[RSZIsoformalClassification 2 r μ]`, the two-slope isoformal space has
    strictly positive dimension `0 < rszIsoformalDim 2 r μ`. -/
theorem rszIsoformalDim_pos_of_classification_two (r μ : Fin 2 → ℤ)
    [hcls : RSZIsoformalClassification 2 r μ] :
    0 < rszIsoformalDim 2 r μ :=
  rszIsoformalDim_two_pos r μ (hcls.ranks_pos 0) (hcls.ranks_pos 1)

end QOU.MathlibExt.RSZ
