/-
Copyright (c) 2026 litlfred. All rights reserved.

# The binding series has no alien plane — on the classical side AND the q-side

The binding gap's one unlocated piece is the irreducibly many-body term, measured
as the connected 3-body cumulant `b₃ = +1.4262 MeV` against a model value of
exactly `0` (`docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md`
§0.1).  A natural attack is resurgence: the model's `b₃ = 0` is a shadow of
semisimplicity (`HH^k(H_n(q), H_n(q)) = 0` at generic `q`), and an *irregular*
q-difference module carries a **unipotent** — hence non-semisimple — Stokes group,
which is exactly a place a genuinely 3-body datum could live without contradicting
the vanishing Hochschild cohomology.

**That attack is excluded, and this file records the q-half of why.**  Two proved
invariants close the two planes independently:

* **Classical plane — closed by growth.**  `QOU.Mass.BindingGevreyHalf` proves the
  integer sandwich `n! ≤ 4ⁿ·I(n)² ≤ 8ⁿ·n!`, so the lever-1 binding period is
  Gevrey-**1/2**, not Gevrey-1.  The level-1 Borel transform is therefore entire:
  no finite singularities, so **no alien derivatives live in that plane**.
* **q-plane — closed by purity.**  `QOU.Mass.BindingScalarKernelParityExclusion`
  proves the binding kernel `L_K = (q²x−1)σ² − (q−1)σ − (q−1)` is irreducible of
  rank `2` and **pure isoclinic** of Newton slope `½` at `∞`.  Ramis–Sauloy,
  *The q-analogue of the wild fundamental group (I)* §2.2, states of pure modules:
  "they are **irregular objects without wild monodromy**".  Pure ⇒ no wild
  monodromy ⇒ no q-alien derivations, no Stokes operators.  Quantitatively, RSZ
  Thm 3.3.5's isoformal dimension `∑_{i<j} rᵢrⱼ(μⱼ−μᵢ)` has an **empty index set**
  at one slope: the isoformal space is a point.

  The same paper forces it a third way, from the *definition* rather than from a
  count.  Ramis–Sauloy Thm 3.5 **defines** the q-alien derivations as residues
  `Δ̇_c(A) = Res_{d=c} log S_{c₀,d}`, valued in the Stokes Lie algebra and
  **graded by level `δ = μ_j − μ_i`** (eq. 16) — a *difference of two slopes*.
  With one slope that grading has no valid index, so there is no graded piece for
  an alien derivation to live in.  Three independent routes, one conclusion.

**The dimension-count half of this is PRIOR ART and is not claimed here.**  The
`references.ts` note on Bugeaud's non-integral generalisation already records
(2026-08-08, bean `qou-qbp5`) that "neither RSZ §3.3 nor this note supplies Stokes
data for a module that is pure isoclinic (a single slope) at the point in
question", and it adds something this file does not re-derive: Bugeaud's
*non-integral* generalisation is **still a two-slope theory** (§2 "Classification
analytique isoformelle à DEUX pentes"), so ramifying to make the slope an integer
does not by itself produce a second slope.  What is new here is the application to
`L_K` — the binding kernel, a different module from C1's `L1` — together with the
Ramis–Sauloy §2.2 statement, which reaches the exclusion structurally rather than
by arithmetic and which this corpus did not hold until 2026-09-07.

`bindingKernel_isoformalDim_eq_zero` is that count at `L_K`'s own Newton data
`(r,d) = (2,1)`.  It is the same arithmetic as
`QOU.MathlibExt.RSZ.c1_infinity_isoformalDim_eq_zero`, and it is stated separately
for the reason that file gives in its own docstring: a lemma naming the object is
harder to walk past than a lemma about an abstract `k = 1`.  `L_K` and C1's `L1`
are different modules that happen to share a Newton polygon.

**`isoformalDim_two_slope_pos` is the anti-vacuity guard, and it carries the
content.**  Without it, `= 0` could be a fact about the *formula* rather than
about `L_K`.  It is not: at two slopes with positive ranks the dimension is
strictly positive.  So the vanishing at `L_K` is a statement about `L_K` having
one slope.

**What this does NOT exclude — and it is the only crack left.**  RSZ's *local
isoformal moduli at `∞`* and the *global connection matrix* `P = Y₀⁻¹Y_∞` between
theta-normalised solutions at `0` and at `∞` are two different objects; the
distinction is drawn in `RSZIsoformalInterface`'s own docstring, where conflating
them cost three retracted claims.  This file closes the first for `L_K` and says
nothing about the second.  The connection matrix for `L_K` is untouched: not
built, not excluded, and not the same question as C1's (bean `qou-wgnx`), which
concerns a different module.

§7c: everything here is `ℤ` arithmetic on ranks and slopes — no ordering on a
substrate quantity, no `ℝ`.  Sorry-free.

-- Ref: [ramis-sauloy2006] https://arxiv.org/abs/math/0611521
-- Ref: [ramis-sauloy-zhang2013] https://arxiv.org/abs/0903.0853
-- Ref: [leitner2026] docs/audits/2026-09-05-binding-gap-groupoids-derived-categories-full-tower.md
-/
import QOU.MathlibExt.RSZIsoformalInterface

namespace QOU.Mass.BindingNoAlienPlane

open QOU.MathlibExt.RSZ

/-- **The binding kernel's `∞` has no local isoformal moduli.**

`L_K = (q²x−1)σ² − (q−1)σ − (q−1)` is pure isoclinic at `∞` with Newton data
`(r, d) = (2, 1)` — one edge, rank `2`, slope `½`
(`QOU.Mass.BindingScalarKernelParityExclusion`).  One slope means no pairs
`i < j` in RSZ Thm 3.3.5's sum, so the isoformal space is a point.

There is therefore no local q-Stokes multiplier at the binding kernel's `∞` to
extract, and no q-alien derivation acting there. -/
theorem bindingKernel_isoformalDim_eq_zero :
    rszIsoformalDim 1 (fun _ => 2) (fun _ => 1) = 0 :=
  rszIsoformalDim_one _ _

/-- **The vanishing above is a fact about `L_K`, not about the formula.**

At two slopes with positive ranks the isoformal dimension is strictly positive.
So `bindingKernel_isoformalDim_eq_zero` is not vacuous: it says the binding
kernel has *one* slope, and it is exactly that one-slope-ness — purity — that
empties the Stokes plane. -/
theorem isoformalDim_two_slope_pos {r₀ r₁ μ₀ μ₁ : ℤ}
    (hr₀ : 0 < r₀) (hr₁ : 0 < r₁) (hμ : μ₀ < μ₁) :
    0 < rszIsoformalDim 2 ![r₀, r₁] ![μ₀, μ₁] := by
  rw [rszIsoformalDim_two]
  exact mul_pos (mul_pos hr₀ hr₁) (rszLevel_pos hμ)

/-- **The binding kernel cannot satisfy RSZ §3.3's standing hypotheses.**

§3.3 presupposes at least two slopes (the level `μ₂ − μ₁` is a *binary*
operation).  `L_K` has one.  So the section whose machinery would produce a
Stokes multiplier does not apply to it — mechanically, not by inspection. -/
theorem not_integralSlopeSetting_bindingKernel :
    ¬ IntegralSlopeSetting 1 (fun _ => 1) :=
  not_integralSlopeSetting_one _

end QOU.Mass.BindingNoAlienPlane
