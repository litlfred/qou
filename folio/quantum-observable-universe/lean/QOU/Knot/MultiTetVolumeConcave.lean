/-
  Multi-tetrahedron total volume: strict concavity on the coupled angle-structure
  polytope, and the unique maximiser.  Bean `qou-7425` — the REACHABLE completion
  of `qou-krvm` (ii) for the multi-tetrahedron case.

  WHAT WAS ALREADY DONE (on `main`), AND WHAT THIS ADDS.

  * `QOU.Archimedean.tetVol_strictConcaveOn` (bean `qou-idvt` T3-plumbing): the
    Lobachevsky volume `tetVol` of a SINGLE ideal tetrahedron is strictly concave
    on the open angle simplex `tetSimplex ⊆ ℝ × ℝ`.
  * `QOU.Knot.AngleStructureUniqueness.strictConcaveOn_maximizer_unique` /
    `…strictConcave_symmetric_maximizer_unique` (bean `qou-krvm` (ii), analytic
    half): a strictly concave objective on a convex set has at most one maximiser,
    and — when invariant under a symmetry acting on a stable set — that unique
    maximiser is symmetric.  Instantiated there for the single tetrahedron
    (`tetVol_maximizer_unique`).
  * This file lifts both to the MULTI-tetrahedron coupled polytope: for a finite
    family of tetrahedra whose angle variables live on a convex, coupled domain
    in `ι → ℝ × ℝ` (each block landing in `tetSimplex`), the total volume
    `totalVol x = Σ_i tetVol (x i)` is strictly concave, hence has a unique
    (and, when a symmetry is supplied, symmetric) maximiser.

  THE ARGUMENT for strict concavity of the sum.  A block-separated sum of
  strictly concave functions is strictly concave: for two distinct points `x ≠ y`
  they differ in at least one block `i₀` (`Function.ne_iff`), where the single-tet
  strict concavity `tetVol_strictConcaveOn.2` gives a STRICT inequality, while
  every other block gives `≤` (the concave companion `.concaveOn.2`, valid even
  where the two blocks agree).  `Finset.sum_lt_sum` (all `≤`, one `<`) then makes
  the whole sum strict.  No new analysis is needed — only the block structure of
  the Pi type and the two inequalities already proved for one tetrahedron.

  WHAT IS PROVED, AND WHAT IS NOT.

  * PROVED, sorry-free, GENERIC in the number of tetrahedra:
    `totalVol_strictConcaveOn`, `totalVol_maximizer_unique`,
    `totalVol_symmetric_maximizer_unique`.  These are the multi-tetrahedron
    analytic discharge of `qou-krvm` (ii): the coupled polytope has a unique
    volume maximiser, by strict concavity of the total volume — the correct route,
    since the fixed-locus-is-a-point route is FALSE for m004 (its fixed locus is a
    line; see bean `qou-krvm` and `M004AngleStructure.fixed_iff_line`).

  * PROVED, sorry-free, CONCRETE for m004 (figure-eight = 2 ideal tetrahedra):
    `convex_m004Polytope` and `m004Vol_maximizer_unique`.  The m004 coupled
    polytope is transcribed into `Fin 2 → ℝ × ℝ` (radians) directly from the
    on-`main` SnapPy gluing data (`M004AngleStructure.GA`): its two edge equations,
    after eliminating the third angle `γ = π − α − β` per tetrahedron, reduce to
    the single homogeneous linear constraint `2α₁ + β₁ − α₂ − 2β₂ = 0` (edge₂ is
    the negation of edge₁, matching the rank-3 count).  Homogeneity makes it
    identical in π-units and radians.  Convexity is the intersection of the two
    block simplices with this hyperplane; uniqueness of the volume maximiser is
    then the generic lemma.  `m004_regular_mem` records that the regular ideal
    point `(π/3, π/3)²` is feasible (the on-`main` `GA_regular` / `Positive_regular`
    in radians).

  * NOT PROVED, and NOT claimed (honest gaps, no faked `sorry`):
    1. **The geometric identification (T2).**  That `tetVol = Λ(α)+Λ(β)+Λ(γ)` IS
       the hyperbolic volume of the ideal simplex is a Mostow/Thurston geometric
       fact Mathlib lacks (beans `qou-7y3g`, `qou-idvt` T2).  Everything here is a
       statement about the analytic functional `totalVol`, correct on its own
       terms; nothing supplies the geometric meaning of the maximiser.
    2. **L6a4 / Borromean concrete wiring.**  The generic lemmas apply verbatim to
       any `Fintype ι` (so to the octahedral decomposition), but the concrete
       L6a4 gluing constraints — currently `L6a4AngleStructure.GA` on `Nat → ℝ` in
       π-units — are NOT transcribed into a `Set (ι → ℝ × ℝ)` radian polytope here.
       That transcription (and the proof that each block lands in `tetSimplex`) is
       the remaining wiring; it is mechanical, not open mathematics.
    3. **The symmetry representation.**  `totalVol_symmetric_maximizer_unique` is
       stated for an arbitrary supplied `Representation`; building the concrete
       order-4 m004 symmetry (or the L6a4 group) as a `Representation ℝ G
       (ι → ℝ × ℝ)` is not done here.  It is not needed for m004 uniqueness — the
       strict concavity alone pins the maximiser, without invoking the symmetry.

  Archimedean (ℝ): `tetVol`, the simplex ordering, and Jensen/strict concavity
  live over `ℝ` (§7c) — angles are real.

  -- Ref: [rivin2003] arXiv:math/9907032, Thm 1.4 (uniqueness of the structure
  --      with prescribed dihedral angles — multi-tetrahedron triangulations)
  -- Ref: [rivin1994] https://doi.org/10.2307/2118572 (strict concavity of the
  --      hyperbolic volume on the angle-structure polytope)
  -- Ref: [leitner2026] beans qou-7425, qou-krvm (ii); QOU/Knot/M004AngleStructure.lean
  --      (SnapPy m004 gluing data), QOU/Knot/AngleStructureUniqueness.lean
-/

import Mathlib.Data.Fin.VecNotation
import QOU.Knot.AngleStructureUniqueness

namespace QOU.Knot.MultiTetVolumeConcave

open QOU.Archimedean
open QOU.Knot.AngleStructureUniqueness

set_option linter.unusedVariables false

/-! ## The total volume of a coupled family of tetrahedra -/

/-- **Total volume** of a finite family of ideal tetrahedra indexed by `ι`, with
angle coordinates `x i ∈ ℝ × ℝ` (third angle `π − (x i).1 − (x i).2` implicit):
`totalVol x = Σ_i tetVol (x i)`. -/
noncomputable def totalVol {ι : Type*} [Fintype ι] (x : ι → ℝ × ℝ) : ℝ :=
  ∑ i, tetVol (x i)

/-! ## Strict concavity of the total volume on any coupled polytope -/

/-- **The total volume is strictly concave on any convex, block-in-simplex
coupled polytope.**

For a convex feasible set `K ⊆ ι → ℝ × ℝ` on which every tetrahedron's angle
block lands in `tetSimplex`, `totalVol` is `StrictConcaveOn ℝ K`.  This is the key
new lemma of bean `qou-7425`: a block-separated sum of strictly concave functions
is strictly concave.  Two distinct feasible points differ in some block `i₀`,
where single-tet strict concavity gives a strict inequality; every other block
contributes `≤`; `Finset.sum_lt_sum` makes the total strict.

Generic in the number of tetrahedra — no assumption on `ι` beyond finiteness, and
no assumption on `K` beyond convexity and block-membership, so the coupling among
tetrahedra (the edge equations) is carried entirely by `K`. -/
theorem totalVol_strictConcaveOn {ι : Type*} [Fintype ι]
    {K : Set (ι → ℝ × ℝ)} (hK : Convex ℝ K)
    (hmem : ∀ x ∈ K, ∀ i, x i ∈ tetSimplex) :
    StrictConcaveOn ℝ K totalVol := by
  refine ⟨hK, ?_⟩
  intro x hx y hy hxy a b ha hb hab
  obtain ⟨i₀, hi₀⟩ := Function.ne_iff.mp hxy
  simp only [totalVol]
  rw [Finset.smul_sum, Finset.smul_sum, ← Finset.sum_add_distrib]
  apply Finset.sum_lt_sum
  · -- every block: concavity gives `≤`
    intro i _
    have hxi := hmem x hx i
    have hyi := hmem y hy i
    have hcc := (tetVol_strictConcaveOn.concaveOn).2 hxi hyi ha.le hb.le hab
    have hpt : (a • x + b • y) i = a • x i + b • y i := by
      simp only [Pi.add_apply, Pi.smul_apply]
    rw [hpt]; exact hcc
  · -- the differing block `i₀`: strict concavity gives `<`
    refine ⟨i₀, Finset.mem_univ i₀, ?_⟩
    have hxi := hmem x hx i₀
    have hyi := hmem y hy i₀
    have hstrict := tetVol_strictConcaveOn.2 hxi hyi hi₀ ha hb hab
    have hpt : (a • x + b • y) i₀ = a • x i₀ + b • y i₀ := by
      simp only [Pi.add_apply, Pi.smul_apply]
    rw [hpt]; exact hstrict

/-! ## Unique maximiser of the coupled total volume -/

/-- **The coupled total volume has at most one maximiser.**  The multi-tetrahedron
analytic discharge of `qou-krvm` (ii): on any convex block-in-simplex coupled
polytope, two maximisers of `totalVol` coincide.  This is what pins the LP optimum
and the volume-maximising point to a single common point (the vanishing-offset
explanation), by strict concavity rather than by the symmetry fixing a lone
point. -/
theorem totalVol_maximizer_unique {ι : Type*} [Fintype ι]
    {K : Set (ι → ℝ × ℝ)} (hK : Convex ℝ K)
    (hmem : ∀ x ∈ K, ∀ i, x i ∈ tetSimplex)
    {p q : ι → ℝ × ℝ}
    (hpK : p ∈ K) (hp : ∀ z ∈ K, totalVol z ≤ totalVol p)
    (hqK : q ∈ K) (hq : ∀ z ∈ K, totalVol z ≤ totalVol q) : p = q :=
  strictConcaveOn_maximizer_unique (totalVol_strictConcaveOn hK hmem) hpK hp hqK hq

/-- **Unique symmetric maximiser of the coupled total volume.**  When a symmetry
`ρ` stabilises the coupled polytope and leaves `totalVol` invariant, the (unique)
maximiser is symmetric — the multi-tetrahedron form of
`strictConcave_symmetric_maximizer_unique`.  The representation is a hypothesis:
the concrete m004 / L6a4 symmetry groups are not built here (see the file header,
gap 3); for m004, uniqueness needs no symmetry at all. -/
theorem totalVol_symmetric_maximizer_unique {ι G : Type*} [Fintype ι]
    [Group G] [Fintype G] (ρ : Representation ℝ G (ι → ℝ × ℝ))
    {K : Set (ι → ℝ × ℝ)} (hK : Convex ℝ K)
    (hmem : ∀ x ∈ K, ∀ i, x i ∈ tetSimplex)
    (hstab : ∀ g : G, ∀ y ∈ K, ρ g y ∈ K)
    (hinv : ∀ (g : G) (y : ι → ℝ × ℝ), totalVol (ρ g y) = totalVol y)
    {p : ι → ℝ × ℝ} (hpK : p ∈ K) (hp : ∀ z ∈ K, totalVol z ≤ totalVol p) :
    (∀ g : G, ρ g p = p) ∧
      (∀ q : ι → ℝ × ℝ, q ∈ K → (∀ z ∈ K, totalVol z ≤ totalVol q) → q = p) :=
  strictConcave_symmetric_maximizer_unique ρ (totalVol_strictConcaveOn hK hmem)
    hstab hinv hpK hp

/-! ## Concrete instantiation: the m004 (figure-eight) coupled polytope

Two ideal tetrahedra, indexed by `Fin 2`.  The m004 gluing data
(`M004AngleStructure.GA`, SnapPy, π-units) has two edge equations on the six
angles `(α₁,β₁,γ₁,α₂,β₂,γ₂)`.  Eliminating `γⱼ = π − αⱼ − βⱼ` (the per-tet sum),
`edge₁ : 2α₁+β₁+α₂+2γ₂ = 2` becomes `2α₁+β₁−α₂−2β₂ = 0`, and `edge₂` becomes its
negation — a single independent constraint, matching the rank-3 feasible set.  The
constraint is homogeneous, hence identical in π-units and radians, so it reads off
directly on the radian coordinates `x : Fin 2 → ℝ × ℝ`. -/

/-- The m004 coupled angle polytope (open, radians): both tetrahedron blocks in
the open simplex, cut by the single reduced edge equation. -/
def m004Polytope : Set (Fin 2 → ℝ × ℝ) :=
  {x | (∀ i, x i ∈ tetSimplex) ∧
        2 * (x 0).1 + (x 0).2 - (x 1).1 - 2 * (x 1).2 = 0}

/-- **The m004 coupled polytope is convex** — the intersection of the two block
simplices (each convex, `convex_tetSimplex`) with a hyperplane. -/
theorem convex_m004Polytope : Convex ℝ m004Polytope := by
  intro x hx y hy a b ha hb hab
  obtain ⟨hxs, hxe⟩ := hx
  obtain ⟨hys, hye⟩ := hy
  have e0 : (a • x + b • y) 0 = a • x 0 + b • y 0 := by
    simp only [Pi.add_apply, Pi.smul_apply]
  have e1 : (a • x + b • y) 1 = a • x 1 + b • y 1 := by
    simp only [Pi.add_apply, Pi.smul_apply]
  refine ⟨fun i => ?_, ?_⟩
  · have hpt : (a • x + b • y) i = a • x i + b • y i := by
      simp only [Pi.add_apply, Pi.smul_apply]
    rw [hpt]
    exact convex_tetSimplex (hxs i) (hys i) ha hb hab
  · rw [e0, e1]
    simp only [Prod.fst_add, Prod.snd_add, Prod.smul_fst, Prod.smul_snd, smul_eq_mul]
    linear_combination a * hxe + b * hye

/-- **The m004 coupled volume has at most one maximiser** — bean `qou-7425`, the
concrete multi-tetrahedron discharge of `qou-krvm` (ii) for the figure-eight knot.
Sorry-free, by the generic `totalVol_maximizer_unique` applied to the transcribed
SnapPy polytope.  (What remains open — the geometric identification that `totalVol`
IS the hyperbolic volume — is gap 1 in the file header, a sibling-bean matter, not
sorried here.) -/
theorem m004Vol_maximizer_unique {p q : Fin 2 → ℝ × ℝ}
    (hpK : p ∈ m004Polytope) (hp : ∀ z ∈ m004Polytope, totalVol z ≤ totalVol p)
    (hqK : q ∈ m004Polytope) (hq : ∀ z ∈ m004Polytope, totalVol z ≤ totalVol q) :
    p = q :=
  totalVol_maximizer_unique convex_m004Polytope (fun x hx i => hx.1 i)
    hpK hp hqK hq

/-- The regular ideal tetrahedron block `(π/3, π/3)` (third angle `π/3`) lies in
the open angle simplex. -/
theorem regTet_mem : ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) ∈ tetSimplex :=
  ⟨by positivity, by positivity, by linarith [Real.pi_pos]⟩

/-- **The regular ideal point is feasible for m004** — two regular ideal
tetrahedra `(π/3, π/3)²`, the radian image of the on-`main` `GA_regular` /
`Positive_regular`.  A concrete sanity anchor that `m004Polytope` is nonempty and
faithfully transcribes the gluing data. -/
theorem m004_regular_mem :
    (![(Real.pi / 3, Real.pi / 3), (Real.pi / 3, Real.pi / 3)] : Fin 2 → ℝ × ℝ)
      ∈ m004Polytope := by
  refine ⟨fun i => ?_, ?_⟩
  · fin_cases i <;> simpa using regTet_mem
  · simp only [Matrix.cons_val_zero, Matrix.cons_val_one]
    ring

/-- **Hypothesis (iv) of `SymmetricOptimum.optima_coincide` for m004, concave
half — DISCHARGED.**  The figure-eight volume functional `totalVol` is concave on
the m004 coupled polytope, in the exact `ConcaveOn ℝ m004Polytope totalVol` form
`optima_coincide` consumes as its `hf₂`.  This is the `ConcaveOn` companion of the
strict concavity behind `m004Vol_maximizer_unique`.

Beans `qou-krvm` (iv) / `qou-rvnc` / `qou-7425`.  Two independent single-tetrahedron
proofs feed the strict concavity this weakens from:
`QOU.Archimedean.tetVol_strictConcaveOn` (the 2-D simplex route used here, through
`totalVol_strictConcaveOn`) and `QOU.Knot.Rivin.strictConcaveOn_tetVolLine` (the
line-parametrised sum-of-squares Hessian, `−cot` on the tangent space of
`α+β+γ = π`).

What (iv) still lacks is **only the geometric identification** — that the analytic
functional `totalVol` IS the hyperbolic volume of the ideal simplex — a
Mostow/Thurston fact Mathlib has no theory for (beans `qou-7y3g`, `qou-idvt` T2).
The concavity itself is complete.  Invariance under the concrete m004 symmetry is
not needed for m004: strict concavity alone pins the maximiser
(`m004Vol_maximizer_unique`), so `optima_coincide`'s symmetry route is not the one
that closes this anchor. -/
theorem m004Vol_concaveOn : ConcaveOn ℝ m004Polytope totalVol :=
  (totalVol_strictConcaveOn convex_m004Polytope (fun x hx i => hx.1 i)).concaveOn

end QOU.Knot.MultiTetVolumeConcave
