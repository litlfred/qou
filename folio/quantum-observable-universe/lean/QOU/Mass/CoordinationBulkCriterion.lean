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
degree loss `1 − k'/k` and measured its answer generic (67.9 % of the plausible window). No value
of that ratio matters until an edge set satisfies `HasBulk`.

## What is new here, and what the corpus already had

A corpus-grep (six paths; path 0 unavailable, so grep-open not graph-open) puts four prior results
between this file and a claim of novelty. Each is cited so a reader does not have to find it.

* **The general affine object already has a Lean `def`.**
  `QOU.Mass.AffineCountMultiplicityWindow.mu (α β A : R) : R := α * A + β` is the same object over
  a generic field, used there for *cumulants*, never for a surface exponent. `affineBondCount` is
  therefore a second definition of it, and the two should be reconciled if either grows consumers.
  That file's own scope note — *"the window below is stated for a general affine multiplicity and
  is **instantiated at nothing**"* — describes exactly the step this file takes.
* **The chain half of Part 2 is already closed in prose, twice.**
  `computations/qbeta/qbeta_chain_cannot_carry_coulomb_or_surface_probe.py` §2 states it verbatim:
  *"In a path every interior vertex has degree exactly 2 and the two endpoints have degree 1 — a
  deficit of `2`, **independent of `A`**. No `A^(2/3)` piece can arise from the edge count of a
  path, for any letters."* Restated in `docs/audits/2026-09-05-binding-law-arc-synthesis.md`. So
  `boundedSurface_not_hasBulk` **formalises an argument the corpus already carries**; it does not
  discover it. Neither prior site has Lean.
* **The deltahedron half is my own prose from #6780**, whose header already said a convex
  deltahedron *"is `d = 3` geometrically while having no bulk at all"*. `linearSurface_not_hasBulk`
  promotes that objection to a decidable `Prop`. That is worth doing and it is not a new finding.
* **`AffineCountIsNotASurfaceTerm` is a one-instance result**, and its generalisation over
  *invariants* was already made informally: `computations/probes/every_seifert_invariant_is_affine_probe.py`
  records scope-(b) for any Seifert invariant of the canonical closure *"via
  `QOU.Mass.AffineCountIsNotASurfaceTerm`'s strictly-monotone ratio, which applies verbatim to each
  affine invariant"* — measured on six nuclei, target fixed at `A^(2/3)`, never written as a
  theorem.

**What is new** is accordingly narrow and worth stating precisely: arbitrary `(α, β)` against
**every** `p ≠ 1` rather than one count against one target; the deltahedron instantiation in Lean;
and `HasBulk` itself, which a full grep finds nowhere in the corpus in any wording — neither the
conjunction, nor `Tendsto (A_surf A / A) atTop (nhds 0)` in any Lean file.

## Scope

* **Proved:** the affine identity and its exclusion of every `p ≠ 1`; both derived edge sets are
  affine; the three `HasBulk` verdicts (constant fails, linear fails, sublinear power succeeds).
* **NOT proved, and this is the open item:** that the substrate cannot emit a non-affine
  coordination object. Reaching a scope-(b) exclusion would need an argument that *every* edge set
  the braid word can express is affine, which is not attempted here — and the corpus already
  carries two scope-(a) negatives pointing the same way, which must be cited rather than
  re-derived: `every_seifert_invariant_is_affine_probe.py` (*"the framework's nuclear encoding has
  no surface … a surface term must come from geometry the encoding does not currently carry"*,
  measured at six `A`) and `computations/substrate/nf_inter_nucleon_is_a_count_not_a_graph_probe.py`
  (a **stronger** negative on one layer: the NF encoding expresses a bond *count* by type and no
  graph at all, since two different graphs with the same type counts give a bit-identical vector).
* **🛑 The enumeration of derived edge sets is EMPIRICAL, so "no derived edge set has a bulk" is
  scope-(a) and is stated here only for the AFFINE ones.** The corpus keeps its own list at
  `QOU.Hecke.BoundedDegreeCoulomb`, and it is longer than two. Beyond the chain and the deltahedron
  there is at least **max-contact sphere packing** (`computations/binding_edge_set_selection.py`),
  whose contact numbers for `A ≥ 5` are case-by-case geometry, are **not the deltahedron family in
  general**, and are **not known to be affine** — so this file does not cover it, and says so rather
  than letting the conclusion overreach. There is also the degree-capped count
  `f_k(A) = A·min(A−1,k)/2` (`QOU.Mass.SaturationInvisibleToCumulants`), which is piecewise and so
  not affine on `ℝ`, though Part 2 does reach it. **The honest claim is about affine edge sets, not
  about every edge set the corpus derives.**
* **Relation to `QOU.Mass.AffineCountIsNotASurfaceTerm`:** that file excludes one specific affine
  count (`12A − 1`, a crossing count) against one specific target (`c·A^(2/3)`), by monotonicity
  of the ratio. This is the same conclusion reached in the **exponent** variable and for an
  arbitrary affine count against **every** `p ≠ 1` — a generalisation of it, not a re-derivation,
  and the two are proved by different routes.
* **Not a fit.** Nothing here is measured against data; the companion probe checks the corpus's
  edge sets against the criterion.

Ground ring `ℝ` (§7c: archimedean — real powers and limits).

-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/SurfaceExponentIsDimension.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/CoordinationSurfaceDeficit.lean
-- Ref: [leitner2026] folio/quantum-observable-universe/lean/QOU/Mass/AffineCountIsNotASurfaceTerm.lean
-- Ref: [leitner2026] computations/probes/geometric_saturation_and_labelling_probe.py (E = 3A − 6)
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
