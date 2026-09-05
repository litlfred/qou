import QOU.Mass.SurfaceExponentIsDimension
import Mathlib.Tactic
import Mathlib.Analysis.SpecialFunctions.Pow.Asymptotics

/-!
# QOU.Mass.CoordinationBulkCriterion — an edge set can supply a surface term only if it has a bulk

`QOU.Mass.SurfaceExponentIsDimension` rejected the production braid word's chain against the AME
chart: its coordination graph is a path, so its bond count is `A − 1` and its per-nucleon law is
the `p = 1` member of `B/A = a − b·A^(−p)`, which the data exclude. It left the sharpened
question — **what edge set could supply a surface term at all?**

This file answers the general form of that question, and the answer is not about amplitudes.

## Part 1 — every affine bond count is `p = 1`, so none of them is ever a surface term

An edge set whose bond count is affine in `A`,

    M(A) = α·A + β,

has per-nucleon binding `ε·M(A)/A = εα + εβ/A` **exactly** (`affine_perNucleon`) — the `p = 1`
member of the family, whatever `α` and `β` are (`affine_eq_perNucleonExp`). By
`perNucleonExp_exponent_inj` it therefore differs from **every** `p ≠ 1` law at some `A`
(`affine_ne_surfaceLaw`), provided `β ≠ 0` — i.e. provided the count is not exactly proportional
to `A`, in which case there is no correction at all.

Both coordination objects derived anywhere on `main` are affine, and this one theorem covers both:

* the production word's chain, `A − 1` bonds (`chain_is_affine`, at `α = 1, β = −1`);
* the deltahedron contact graph, `E = 3A − 6` by Euler (`deltahedron_is_affine`, at `α = 3,
  β = −6`).

So the obstruction is not that the chain is *one-dimensional* in particular. **Affineness alone
is enough**, and it is a property both derived candidates share.

## Part 2 — the criterion an edge set must satisfy, and why both candidates fail it

`CoordinationSurfaceDeficit.perNucleon_split` puts the whole `A`-dependence of the correction in
the surface **fraction** `A_surf/A`. Two things must hold at once for that fraction to carry a
genuine surface term:

    HasBulk A_surf  ↔  A_surf → ∞      (there IS a surface, and it grows)
                    ∧  A_surf/A → 0    (there IS an interior — a bulk)

Each clause alone is cheap; the conjunction is what has content. The two derived candidates fail
one clause each, for opposite reasons:

* **The chain has `A_surf = 2`**, a constant. It has an interior, but its surface does not grow,
  so the deficit is a fixed number of missing bonds spread over `A` nucleons — `1/A`, exponent 1
  (`boundedSurface_not_hasBulk`).
* **A convex deltahedron has `A_surf = A`**: every nucleon is a vertex of the hull, so it is
  three-dimensional and yet has **no interior at all**. Its surface fraction is constant, so the
  deficit renormalises the volume term and contributes no `A`-dependence whatever
  (`linearSurface_not_hasBulk`). Two caveats, both measured by the companion probe and both
  weakening what this row can be taken to show: convex deltahedra exist only for
  `A ∈ {4,…,10,12}`, and the corpus records them only up to **`A = 7`** — so `HasBulk`, an
  `A → ∞` criterion, is applied here to the *idealisation* `A_surf = A` and never to the
  corpus's actual data, which does not reach far enough to have an asymptotic regime at all.

The satisfying case is exactly the one `CoordinationSurfaceDeficit` assumed:
`A_surf = c·A^θ` with `0 < θ < 1` (`powerSurface_hasBulk`), which is where the compact-packing
hypothesis `θ = 2/3` lives.

**This is why the question is prior to the amplitude.** #6761 asked what fixes the fractional
degree loss `1 − k'/k` and measured its answer generic (67.9 % of the plausible window). But no
value of that ratio matters until an edge set satisfies `HasBulk`, and no edge set derived in this
corpus does.

## Scope

* **Proved:** the affine identity and its exclusion of every `p ≠ 1`; both derived edge sets are
  affine; the three `HasBulk` verdicts (constant fails, linear fails, sublinear power succeeds).
* **NOT proved, and this is the open item:** that the substrate cannot emit a non-affine
  coordination object. This file gives the criterion and disqualifies the two candidates that
  exist; it does not survey the space of edge sets the substrate could emit. Reaching a scope-(b)
  exclusion would need an argument that *every* edge set the braid word can express is affine,
  which is not attempted here.
* **Relation to `QOU.Mass.AffineCountIsNotASurfaceTerm`:** that file excludes one specific affine
  count (`12A − 1`, a crossing count) against one specific target (`c·A^(2/3)`), by monotonicity
  of the ratio. This is the same conclusion reached in the **exponent** variable and for an
  arbitrary affine count against **every** `p ≠ 1` — a generalisation of it, not a re-derivation,
  and the two are proved by different routes.
* **Not a fit.** Nothing here is measured against data; the companion probe checks the corpus's
  edge sets against the criterion.

Ground ring `ℝ` (§7c: archimedean — real powers and limits).

-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/Mass/SurfaceExponentIsDimension.lean
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/Mass/CoordinationSurfaceDeficit.lean
-- Ref: [manuscript] content/quantum-observable-universe/lean/QOU/Mass/AffineCountIsNotASurfaceTerm.lean
-- Ref: [manuscript] computations/probes/geometric_saturation_and_labelling_probe.py (E = 3A − 6)
-/

namespace QOU.Mass.CoordinationBulkCriterion

open Filter QOU.Mass.SurfaceExponentIsDimension

/-! ## Part 1 — affine bond counts are all `p = 1` -/

/-- A bond count affine in the mass number: `M(A) = α·A + β`. -/
noncomputable def affineBondCount (α β A : ℝ) : ℝ := α * A + β

/-- **An affine bond count's per-nucleon binding is `εα + εβ/A`, exactly.** -/
theorem affine_perNucleon (ε α β A : ℝ) (hA : A ≠ 0) :
    ε * affineBondCount α β A / A = ε * α + ε * β / A := by
  unfold affineBondCount
  field_simp

/-- **Every affine bond count is the `p = 1` member of the family**, whatever `α` and `β` are. -/
theorem affine_eq_perNucleonExp (ε α β A : ℝ) (hA : 0 < A) :
    ε * affineBondCount α β A / A = perNucleonExp (ε * α) (-(ε * β)) 1 A := by
  unfold perNucleonExp
  rw [affine_perNucleon ε α β A (ne_of_gt hA), Real.rpow_neg_one]
  field_simp
  ring

/-- **No affine bond count is a surface law.** For `ε ≠ 0` and `β ≠ 0`, the affine law differs
from the `p` law with the same amplitude at some `A > 0`, for every `p ≠ 1`. The exponent is the
obstruction; no choice of `α`, `β` or `ε` removes it. -/
theorem affine_ne_surfaceLaw (ε α β : ℝ) (hε : ε ≠ 0) (hβ : β ≠ 0) (p : ℝ) (hp : p ≠ 1) :
    ∃ A : ℝ, 0 < A ∧
      perNucleonExp (ε * α) (-(ε * β)) 1 A ≠ perNucleonExp (ε * α) (-(ε * β)) p A := by
  by_contra hcon
  push_neg at hcon
  have hb : -(ε * β) ≠ 0 := neg_ne_zero.mpr (mul_ne_zero hε hβ)
  exact hp (perNucleonExp_exponent_inj (ε * α) (-(ε * β)) 1 p hb (fun A hA => hcon A hA)).symm

/-- The production word's chain is affine at `α = 1, β = −1`. -/
theorem chain_is_affine (A : ℝ) :
    QOU.Mass.CoordinationSurfaceDeficit.bondCount 2 1 (A - 2) 2 = affineBondCount 1 (-1) A := by
  unfold QOU.Mass.CoordinationSurfaceDeficit.bondCount affineBondCount
  ring

/-- The deltahedron contact graph `E = 3A − 6` (Euler, `2E = 3F`) is affine at `α = 3, β = −6`. -/
theorem deltahedron_is_affine (A : ℝ) : 3 * A - 6 = affineBondCount 3 (-6) A := by
  unfold affineBondCount
  ring

/-! ## Part 2 — the bulk criterion -/

/-- **An edge set has a bulk** when its surface count grows without bound — there *is* a
surface — while the surface *fraction* vanishes — there *is* an interior. Each clause alone is
cheap; the conjunction is the content. -/
def HasBulk (Asurf : ℝ → ℝ) : Prop :=
  Tendsto Asurf atTop atTop ∧ Tendsto (fun A => Asurf A / A) atTop (nhds 0)

/-- **A constant surface count has no bulk** — the chain's case, `A_surf = 2`. There is an
interior but the surface does not grow, so the deficit is a fixed number of missing bonds. -/
theorem boundedSurface_not_hasBulk (c : ℝ) : ¬ HasBulk (fun _ => c) := by
  rintro ⟨h, -⟩
  obtain ⟨A, hA⟩ := (h.eventually_ge_atTop (c + 1)).exists
  linarith

/-- **A surface count proportional to `A` has no bulk** — the convex deltahedron's case, where
every nucleon is a hull vertex. The surface grows, but there is no interior, so the deficit
renormalises the volume term and contributes no `A`-dependence. -/
theorem linearSurface_not_hasBulk (γ : ℝ) (hγ : γ ≠ 0) : ¬ HasBulk (fun A => γ * A) := by
  rintro ⟨-, h⟩
  have heq : (fun A : ℝ => γ * A / A) =ᶠ[atTop] (fun _ => γ) := by
    filter_upwards [eventually_gt_atTop (0 : ℝ)] with A hA
    field_simp
  exact hγ (tendsto_nhds_unique tendsto_const_nhds (Filter.Tendsto.congr' heq h))

/-- **A sublinear power surface count has a bulk** — the compact-packing case, where the
`θ = 2/3` of `CoordinationSurfaceDeficit` lives. -/
theorem powerSurface_hasBulk (c θ : ℝ) (hc : 0 < c) (hθ0 : 0 < θ) (hθ1 : θ < 1) :
    HasBulk (fun A => c * A ^ θ) := by
  refine ⟨Filter.Tendsto.const_mul_atTop hc (tendsto_rpow_atTop hθ0), ?_⟩
  have hy : (0 : ℝ) < 1 - θ := by linarith
  have hmul : Tendsto (fun A : ℝ => c * A ^ (-(1 - θ))) atTop (nhds (c * 0)) :=
    (tendsto_rpow_neg_atTop hy).const_mul c
  rw [mul_zero] at hmul
  refine Filter.Tendsto.congr' ?_ hmul
  filter_upwards [eventually_gt_atTop (0 : ℝ)] with A hA
  rw [show -(1 - θ) = θ - 1 by ring, Real.rpow_sub hA, Real.rpow_one]
  ring

/-- The chain's surface count fails the criterion. -/
theorem chainSurface_not_hasBulk : ¬ HasBulk (fun _ => (2 : ℝ)) :=
  boundedSurface_not_hasBulk 2

/-- The convex deltahedron's surface count fails the criterion, for the opposite reason. -/
theorem deltahedronSurface_not_hasBulk : ¬ HasBulk (fun A => (1 : ℝ) * A) :=
  linearSurface_not_hasBulk 1 one_ne_zero

end QOU.Mass.CoordinationBulkCriterion
