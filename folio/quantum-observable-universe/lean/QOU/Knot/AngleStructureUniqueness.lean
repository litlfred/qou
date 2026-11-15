import Mathlib.Analysis.Convex.Jensen
import Mathlib.Tactic
import QOU.Knot.SymmetricOptimum
import QOU.Archimedean.IdealTetrahedronVolumeConcave

/-!
# QOU.Knot.AngleStructureUniqueness — uniqueness of the angle-structure optimum

Rivin, *Combinatorial optimization in geometry* (arXiv:math/9907032), Thm 1.4
(uniqueness), meets the strict concavity of the ideal-tetrahedron volume
(`QOU.Archimedean.tetVol_strictConcaveOn`).  This file discharges the
"uniqueness of the [maximising] symmetric point" role that `qou-krvm`
hypothesis (ii) plays, via the *strictly concave objective* route rather than
the fixed-locus-is-a-point route (which is **false** for m004 — its fixed locus
is a line, not a point; see bean `qou-krvm`).

The mathematical content, stated generically and reused twice:

* **`strictConcaveOn_maximizer_unique`** — a strictly concave objective on a
  convex feasible set has **at most one** maximiser.  This is the whole of
  Rivin's uniqueness at the analytic level: strict concavity *is* the
  uniqueness mechanism; the symmetric point is singled out not because the
  symmetry fixes it alone but because the strictly concave volume functional
  has one and only one maximiser.
* **`strictConcave_maximizer_symmetric`** — that unique maximiser is a
  *symmetric* point.  By orbit averaging (`SymmetricOptimum.orbitAvg`), the
  orbit average of a maximiser is feasible, symmetry-fixed, and (Jensen) at
  least as good, hence *also* a maximiser; uniqueness then forces it to equal
  the original.  So the maximiser is fixed by the group.
* **`tetVol_maximizer_unique`** — the instantiation to the single ideal
  tetrahedron: `tetVol` has at most one maximiser on the open angle simplex.
  This is Rivin Thm 1.4 for the one-tetrahedron case, sorry-free, wired to the
  strict-concavity result already on `main`.

## What this discharges, and what it does not

* **Discharged (sorry-free):** the *analytic* half of `qou-krvm` (ii) — that a
  strictly concave, symmetry-invariant objective on a convex, symmetry-stable
  feasible set has a **unique** maximiser and that maximiser is the symmetric
  point.  Instantiated for the ideal tetrahedron's volume via
  `tetVol_maximizer_unique`.  Because the maximiser is unique, two *different*
  invariant strictly-concave objectives on the same set land at the same point,
  which is exactly why the measured LP-vs-geometry offset vanishes.

* **Not discharged (honest gaps, not faked):**
  1. **Multi-tetrahedron polytopes (m004 = 2 tets, L6a4 = octahedron).** These
     need the strict concavity of the *total* volume `Σᵢ tetVol(tetᵢ)` on the
     coupled angle-structure polytope, plus the concrete polytope from
     `M004AngleStructure` / `L6a4AngleStructure`.  A block-separated sum of
     strictly concave functions is strictly concave, and strict concavity is
     inherited on a convex subset, so this is reachable — but it is not wired
     here.
  2. **The geometric identification (T2).** That `tetVol = Λ(α)+Λ(β)+Λ(γ)` *is*
     the hyperbolic volume of the ideal simplex is a Mostow/Thurston geometric
     fact Mathlib lacks (beans `qou-7y3g`, `qou-idvt` T2).  Nothing here
     supplies it; the uniqueness above is a statement about the analytic
     functional `tetVol`, correct on its own terms.

Archimedean (ℝ): genuinely archimedean — strict concavity and Jensen over `ℝ`
(§7c).

-- Ref: [rivin2003] arXiv:math/9907032, Thm 1.4 (uniqueness of the structure
--      with prescribed dihedral angles)
-- Ref: [rivin1994] https://doi.org/10.2307/2118572 (strict concavity of the
--      hyperbolic volume on the angle-structure polytope)
-- Ref: [leitner2026] docs/audits/2026-08-15-rivin-9907032-comb-opt-analysis.md,
--      beans qou-krvm (ii), qou-tcfb
-/

namespace QOU.Knot.AngleStructureUniqueness

-- The maximiser binders (`p`, `q`) occur in the *statement* conclusions/hypotheses
-- but not by name in the term-mode proofs, which the unused-variable linter flags
-- spuriously; disabled file-wide for this small, hand-reviewed file.
set_option linter.unusedVariables false

open QOU.Knot.SymmetricOptimum

/-! ## The generic uniqueness mechanism -/

section Unique
variable {V : Type*} [AddCommGroup V] [Module ℝ V]
variable {K : Set V} {f : V → ℝ}

/-- **Uniqueness of the maximiser of a strictly concave objective.**

If `f` is strictly concave on the convex set `K` and both `p` and `q` maximise
`f` over `K`, then `p = q`.  The midpoint of two distinct maximisers would beat
them by strict concavity, contradicting maximality.  This is the analytic core
of Rivin's uniqueness theorem: strict concavity, by itself, forbids a second
optimum. -/
theorem strictConcaveOn_maximizer_unique (hf : StrictConcaveOn ℝ K f)
    {p q : V} (hpK : p ∈ K) (hp : ∀ z ∈ K, f z ≤ f p)
    (hqK : q ∈ K) (hq : ∀ z ∈ K, f z ≤ f q) : p = q := by
  by_contra hne
  have hmid :
      (1 / 2 : ℝ) • f p + (1 / 2 : ℝ) • f q
        < f ((1 / 2 : ℝ) • p + (1 / 2 : ℝ) • q) :=
    hf.2 hpK hqK hne (by norm_num) (by norm_num) (by norm_num)
  have hmemK : ((1 / 2 : ℝ) • p + (1 / 2 : ℝ) • q) ∈ K :=
    hf.1 hpK hqK (by norm_num) (by norm_num) (by norm_num)
  have hle : f ((1 / 2 : ℝ) • p + (1 / 2 : ℝ) • q) ≤ f p := hp _ hmemK
  have hpq : f p = f q := le_antisymm (hq p hpK) (hp q hqK)
  rw [smul_eq_mul, smul_eq_mul] at hmid
  linarith [hmid, hle, hpq]

end Unique

/-! ## The unique maximiser is symmetric -/

section Symmetric
variable {G V : Type*} [Group G] [Fintype G]
variable [AddCommGroup V] [Module ℝ V]
variable (ρ : Representation ℝ G V) {K : Set V} {f : V → ℝ}

/-- **A maximiser of a strictly-concave invariant objective is a symmetric
point.**

Given a maximiser `p`, its orbit average is feasible (`orbitAvg_mem`),
symmetry-fixed (`orbitAvg_fixed`), and — since `f` is concave and invariant —
does not decrease `f` (`le_apply_orbitAvg`).  So the orbit average is *also* a
maximiser; strict-concavity uniqueness (`strictConcaveOn_maximizer_unique`)
forces it to equal `p`, whence `p` is fixed by every group element. -/
theorem strictConcave_maximizer_symmetric (hf : StrictConcaveOn ℝ K f)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv : ∀ (g : G) (y : V), f (ρ g y) = f y)
    {p : V} (hpK : p ∈ K) (hp : ∀ z ∈ K, f z ≤ f p) :
    ∀ g : G, ρ g p = p := by
  have hmem : orbitAvg ρ p ∈ K := orbitAvg_mem ρ hf.1 hstab hpK
  have hge : f p ≤ f (orbitAvg ρ p) :=
    le_apply_orbitAvg ρ hf.concaveOn hstab hinv hpK
  have havgmax : ∀ z ∈ K, f z ≤ f (orbitAvg ρ p) := fun z hz => (hp z hz).trans hge
  have heq : orbitAvg ρ p = p :=
    strictConcaveOn_maximizer_unique hf hmem havgmax hpK hp
  intro g
  have h := orbitAvg_fixed ρ (x := p) g
  rwa [heq] at h

/-- **Unique symmetric maximiser (the `qou-krvm` (ii) statement, corrected).**

A strictly concave, symmetry-invariant objective on a convex, symmetry-stable
feasible set has a maximiser that is both **unique** and **symmetric**.  This is
what pins the LP optimum and the geometric (volume-maximising) point to a single
common point — the vanishing-offset explanation — with uniqueness coming from
strict concavity rather than from the symmetry fixing a lone point. -/
theorem strictConcave_symmetric_maximizer_unique (hf : StrictConcaveOn ℝ K f)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv : ∀ (g : G) (y : V), f (ρ g y) = f y)
    {p : V} (hpK : p ∈ K) (hp : ∀ z ∈ K, f z ≤ f p) :
    (∀ g : G, ρ g p = p) ∧
      (∀ q : V, q ∈ K → (∀ z ∈ K, f z ≤ f q) → q = p) :=
  ⟨strictConcave_maximizer_symmetric ρ hf hstab hinv hpK hp,
    fun q hqK hq => strictConcaveOn_maximizer_unique hf hqK hq hpK hp⟩

end Symmetric

/-! ## Instantiation: the single ideal tetrahedron -/

open QOU.Archimedean in
/-- **Rivin Thm 1.4 for the single ideal tetrahedron.** The Lobachevsky volume
`tetVol` of an ideal tetrahedron has **at most one** maximiser on the open angle
simplex `tetSimplex`.  Discharged sorry-free from the strict concavity
`tetVol_strictConcaveOn` (bean `qou-idvt` T3-plumbing) via the generic
uniqueness mechanism above — the analytic half of `qou-krvm` (ii) for the
one-tetrahedron anchor. -/
theorem tetVol_maximizer_unique {p q : ℝ × ℝ}
    (hpK : p ∈ tetSimplex) (hp : ∀ z ∈ tetSimplex, tetVol z ≤ tetVol p)
    (hqK : q ∈ tetSimplex) (hq : ∀ z ∈ tetSimplex, tetVol z ≤ tetVol q) : p = q :=
  strictConcaveOn_maximizer_unique tetVol_strictConcaveOn hpK hp hqK hq

end QOU.Knot.AngleStructureUniqueness
