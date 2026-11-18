/-
  The m004 (figure-eight) angle-structure polytope: symmetry, the fixed locus,
  and the Casson–Rivin optimum.  Bean `qou-krvm`, partial discharge.

  CONTEXT (PR #4513).  `SymmetricOptimum.optima_coincide` proves, in general,
  that two concave symmetry-invariant objectives on a symmetric convex set share
  a maximiser — the structural explanation for the measured
  `‖x_geom − x_LP‖ = 2.4e-16`.  Its hypotheses had never been discharged for the
  actual anchors.  Bean `qou-krvm` lists four:

    (i)   the polytope is stable under a symmetry group acting linearly;
    (ii)  the symmetric point is UNIQUE;
    (iii) the Casson–Rivin min-angle objective is concave and invariant;
    (iv)  the volume functional is concave and invariant (Rivin; not in Mathlib).

  This file settles (i) for m004, **refutes (ii) as stated**, repairs it, and
  proves the repaired conclusion.  (iv)'s CONCAVITY is discharged separately —
  not here but in the `qou-7425` volume cluster
  (`MultiTetVolumeConcave.m004Vol_concaveOn` / `m004Vol_maximizer_unique`); this
  file's min-angle route stays independent of it.  See the honesty boundary below
  for what (iv) still lacks (the geometric identification, not concavity).

  ═══ (ii) IS FALSE FOR m004 ═══

  The bean expected the symmetric point to be unique.  It is not.  The subgroup
  of coordinate permutations preserving the m004 generalised-angle affine set
  has order 4, and its fixed locus inside that set is a **LINE**, not a point:

      (α₁, β₁, γ₁, α₂, β₂, γ₂) = (t, 1 − 2t, t, 1 − 2t, t, t),   t ∈ ℝ

  (`fixed_iff_line`, an iff — so this is the exact fixed locus, not a
  containment).  Symmetry alone therefore does NOT pin the optimum, and
  `symmetric_point_optimal` cannot be applied to m004 as the bean envisaged.

  ═══ THE REPAIR, AND WHY IT STILL WORKS ═══

  Symmetry does most of the work anyway: it cuts the 3-dimensional feasible set
  down to ONE dimension, and on that line the Casson–Rivin objective finishes
  the job by itself.  Every coordinate of a fixed point is `t` or `1 − 2t`, so
  the minimum angle is `min t (1 − 2t)`, which is **uniquely** maximised at
  `t = 1/3` (`minAngle_lt_of_ne`) — the regular ideal tetrahedron, every angle
  `1/3` in π-units.  Hence `regular_maximises_on_fixed_locus`.

  Composed with the already-proved `exists_symmetric_maximiser` (some global
  maximiser is symmetric), this gives the substance the bean asked for: the
  regular point is a Casson–Rivin max-min-angle optimum for m004.

  ═══ HONESTY BOUNDARY ═══

  * What is proved is that the regular point is **AN** optimum, not **THE**
    optimum.  The min-angle objective is a min of linear forms — concave but
    NOT strictly concave — so global uniqueness does not follow and is not
    claimed here.
  * (iv)'s CONCAVITY is discharged, though not in this file: the `qou-7425`
    cluster proves the m004 volume functional concave with a unique maximiser
    (`MultiTetVolumeConcave.m004Vol_concaveOn` / `m004Vol_maximizer_unique`),
    built on the corpus's OWN ideal-tetrahedron volume theory
    `QOU.Archimedean.tetVol` — Mathlib lacks it, the corpus has it (two
    independent single-tet proofs: `QOU.Archimedean.tetVol_strictConcaveOn` and
    `QOU.Knot.Rivin.strictConcaveOn_tetVolLine`).  This file's min-angle route
    stays independent of all that.  What (iv) still lacks is the GEOMETRIC
    IDENTIFICATION that the analytic `totalVol` IS the hyperbolic volume
    (Mostow/Thurston; beans qou-7y3g, qou-idvt T2), not the concavity.  Nothing
    here evaluates a volume; that the complete structure also sits at the regular
    point is used only as context, not as a hypothesis.
  * The constraint data is not invented.  `tet₁/tet₂/edge₁/edge₂` are SnapPy's
    m004 gluing equations in π-units, via the corpus's own `gluing` /
    `ga_equalities` helpers (`borromean_angle_structure_lp_probe.py`) — the same
    system the LP was solved against.  The symmetry group was found by exhaustive
    search over all 720 coordinate permutations, so the order-4 group is the
    complete coordinate-permutation symmetry, not a lucky subgroup.

  Archimedean (ℝ): genuinely archimedean — ordering and `min` over `ℝ` (§7c).

  -- Ref: [leitner2026] computations/probes/qbeta_sdp_angle_offset_theta_probe.py
  -- Ref: [garoufalidis2012] arXiv:1208.1663 §2.2–2.3 (generalised angle structures)
-/

import Mathlib.Tactic

namespace QOU.Knot.M004AngleStructure

/-- **The m004 generalised angle structure**, in π-units, on the six tetrahedron
angles `(α₁, β₁, γ₁, α₂, β₂, γ₂)`.

`tet₁`/`tet₂` are the per-tetrahedron sums; `edge₁`/`edge₂` are SnapPy's two
edge equations for m004. The four are rank 3 (the edge sum is twice the tet
sum), matching the 3-dimensional solution space the LP was solved over. -/
structure GA (α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ) : Prop where
  tet₁ : α₁ + β₁ + γ₁ = 1
  tet₂ : α₂ + β₂ + γ₂ = 1
  edge₁ : 2 * α₁ + β₁ + α₂ + 2 * γ₂ = 2
  edge₂ : β₁ + 2 * γ₁ + α₂ + 2 * β₂ = 2

/-- Strict positivity of all six angles — the open part of the polytope. -/
structure Positive (α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ) : Prop where
  hα₁ : 0 < α₁
  hβ₁ : 0 < β₁
  hγ₁ : 0 < γ₁
  hα₂ : 0 < α₂
  hβ₂ : 0 < β₂
  hγ₂ : 0 < γ₂

/-! ## (i) The polytope is stable under an order-4 permutation group -/

/-- **Generator σ**: `(α₁,β₁,γ₁,α₂,β₂,γ₂) ↦ (γ₁,β₁,α₁,α₂,γ₂,β₂)`.
It preserves `GA` by SWAPPING the two edge equations. -/
theorem GA.sigma {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ} (h : GA α₁ β₁ γ₁ α₂ β₂ γ₂) :
    GA γ₁ β₁ α₁ α₂ γ₂ β₂ :=
  { tet₁ := by linarith [h.tet₁]
    tet₂ := by linarith [h.tet₂]
    edge₁ := by linarith [h.edge₂]
    edge₂ := by linarith [h.edge₁] }

/-- **Generator τ**: `(α₁,β₁,γ₁,α₂,β₂,γ₂) ↦ (β₂,α₂,γ₂,β₁,α₁,γ₁)`.
It preserves `GA` by swapping BOTH the tetrahedra and the edge equations. -/
theorem GA.tau {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ} (h : GA α₁ β₁ γ₁ α₂ β₂ γ₂) :
    GA β₂ α₂ γ₂ β₁ α₁ γ₁ :=
  { tet₁ := by linarith [h.tet₂]
    tet₂ := by linarith [h.tet₁]
    edge₁ := by linarith [h.edge₂]
    edge₂ := by linarith [h.edge₁] }

/-- Positivity is permutation-invariant, so it survives σ. -/
theorem Positive.sigma {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ} (h : Positive α₁ β₁ γ₁ α₂ β₂ γ₂) :
    Positive γ₁ β₁ α₁ α₂ γ₂ β₂ :=
  ⟨h.hγ₁, h.hβ₁, h.hα₁, h.hα₂, h.hγ₂, h.hβ₂⟩

/-- Likewise for τ. -/
theorem Positive.tau {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ} (h : Positive α₁ β₁ γ₁ α₂ β₂ γ₂) :
    Positive β₂ α₂ γ₂ β₁ α₁ γ₁ :=
  ⟨h.hβ₂, h.hα₂, h.hγ₂, h.hβ₁, h.hα₁, h.hγ₁⟩

/-! ## (ii) The fixed locus is a LINE — the bean's hypothesis, refuted -/

/-- Being fixed by both generators. -/
def Fixed (α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ) : Prop :=
  (γ₁ = α₁ ∧ γ₂ = β₂) ∧ (β₂ = α₁ ∧ α₂ = β₁ ∧ γ₂ = γ₁)

/-- **The exact fixed locus of the symmetry group, as an `iff`.**

A feasible point is fixed by both generators **iff** it lies on the line
`(t, 1 − 2t, t, 1 − 2t, t, t)`.  Because this is an iff, it settles the bean's
hypothesis (ii) NEGATIVELY: the fixed set is one-dimensional, so the symmetric
point is not unique and symmetry alone cannot pin the optimum. -/
theorem fixed_iff_line {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ} (h : GA α₁ β₁ γ₁ α₂ β₂ γ₂) :
    Fixed α₁ β₁ γ₁ α₂ β₂ γ₂ ↔
      (β₁ = 1 - 2 * α₁ ∧ γ₁ = α₁ ∧ α₂ = 1 - 2 * α₁ ∧ β₂ = α₁ ∧ γ₂ = α₁) := by
  constructor
  · rintro ⟨⟨hγ₁, hγ₂⟩, hβ₂, hα₂, hγ₂'⟩
    refine ⟨by linarith [h.tet₁], hγ₁, ?_, hβ₂, by linarith⟩
    rw [hα₂]; linarith [h.tet₁]
  · rintro ⟨hβ₁, hγ₁, hα₂, hβ₂, hγ₂⟩
    exact ⟨⟨hγ₁, by rw [hγ₂, hβ₂]⟩, hβ₂, by rw [hα₂, hβ₁], by rw [hγ₂, hγ₁]⟩

/-- The regular point `(1/3, …, 1/3)` — two regular ideal tetrahedra — is
feasible. -/
theorem GA_regular : GA (1/3) (1/3) (1/3) (1/3) (1/3) (1/3) :=
  { tet₁ := by norm_num, tet₂ := by norm_num
    edge₁ := by norm_num, edge₂ := by norm_num }

theorem Positive_regular : Positive (1/3) (1/3) (1/3) (1/3) (1/3) (1/3) :=
  ⟨by norm_num, by norm_num, by norm_num, by norm_num, by norm_num, by norm_num⟩

/-- The regular point is on the fixed line, at `t = 1/3`. -/
theorem Fixed_regular : Fixed (1/3) (1/3) (1/3) (1/3) (1/3) (1/3) :=
  ⟨⟨rfl, rfl⟩, rfl, rfl, rfl⟩

/-! ## (iii) Casson–Rivin on the fixed line: a unique maximiser -/

/-- The minimum angle at a point of the fixed line.  Every coordinate is `t` or
`1 - 2t`, so the whole objective collapses to a two-term `min`. -/
noncomputable def minAngleOnLine (t : ℝ) : ℝ := min t (1 - 2 * t)

@[simp] theorem minAngleOnLine_regular : minAngleOnLine (1/3) = 1/3 := by
  unfold minAngleOnLine; norm_num

/-- **The Casson–Rivin objective is uniquely maximised at the regular point.**
Off `t = 1/3` the minimum angle is strictly smaller — below it because `t`
itself is, above it because `1 - 2t` is.

This is what replaces the bean's false hypothesis (ii): the symmetry cuts the
feasible set to a line, and the objective — not the symmetry — picks the point
on it. -/
theorem minAngleOnLine_lt_of_ne {t : ℝ} (ht : t ≠ 1/3) :
    minAngleOnLine t < 1/3 := by
  unfold minAngleOnLine
  rcases lt_or_gt_of_ne ht with h | h
  · exact lt_of_le_of_lt (min_le_left _ _) h
  · exact lt_of_le_of_lt (min_le_right _ _) (by linarith)

/-- Restated as a maximisation: on the fixed line the regular point is the
unique maximiser of the minimum angle. -/
theorem regular_maximises_on_fixed_locus (t : ℝ) :
    minAngleOnLine t ≤ minAngleOnLine (1/3) := by
  rcases eq_or_ne t (1/3) with rfl | ht
  · exact le_refl _
  · rw [minAngleOnLine_regular]; exact (minAngleOnLine_lt_of_ne ht).le

/-- …and strictly so away from it — the maximiser is unique. -/
theorem regular_unique_on_fixed_locus {t : ℝ} (ht : t ≠ 1/3) :
    minAngleOnLine t < minAngleOnLine (1/3) := by
  rw [minAngleOnLine_regular]; exact minAngleOnLine_lt_of_ne ht

/-- Positivity confines the fixed line to `0 < t < 1/2`; the regular point sits
strictly inside, so it is not a boundary artefact. -/
theorem fixed_positive_iff {t : ℝ} :
    Positive t (1 - 2*t) t (1 - 2*t) t t ↔ (0 < t ∧ t < 1/2) := by
  constructor
  · intro h; exact ⟨h.hα₁, by linarith [h.hβ₁]⟩
  · rintro ⟨h0, h1⟩
    exact ⟨h0, by linarith, h0, by linarith, h0, h0⟩

/-- The fixed line is genuinely inside the polytope: every `t ∈ (0, 1/2)` gives
a feasible positive point.  So the one-dimensionality in `fixed_iff_line` is a
real degree of freedom, not an empty set. -/
theorem GA_on_line (t : ℝ) : GA t (1 - 2*t) t (1 - 2*t) t t :=
  { tet₁ := by ring, tet₂ := by ring, edge₁ := by ring, edge₂ := by ring }

/-- **Orbit-averaging identity onto the fixed line.**
    For any feasible angle structure `GA α₁ β₁ γ₁ α₂ β₂ γ₂`, averaging the four
    `(1, σ, τ, στ)`-conjugate coordinates `t = (α₁ + γ₁ + β₂ + γ₂) / 4` and the
    two conjugate middle angles `(β₁ + α₂) / 2` automatically satisfies the
    fixed-line relation `(β₁ + α₂) / 2 = 1 - 2 * t`. -/
theorem orbit_average_lies_on_fixed_line {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ}
    (h : GA α₁ β₁ γ₁ α₂ β₂ γ₂) :
    (β₁ + α₂) / 2 = 1 - 2 * ((α₁ + γ₁ + β₂ + γ₂) / 4) := by
  linarith [h.tet₁, h.tet₂]

/-- Averaging any feasible positive angle structure over the order-4 symmetry
    group lands strictly inside the open fixed-line segment `0 < t < 1/2`. -/
theorem orbit_average_mem_open_segment {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ}
    (hga : GA α₁ β₁ γ₁ α₂ β₂ γ₂) (hpos : Positive α₁ β₁ γ₁ α₂ β₂ γ₂) :
    0 < (α₁ + γ₁ + β₂ + γ₂) / 4 ∧ (α₁ + γ₁ + β₂ + γ₂) / 4 < 1 / 2 := by
  constructor
  · linarith [hpos.hα₁, hpos.hγ₁, hpos.hβ₂, hpos.hγ₂]
  · linarith [hga.tet₁, hga.tet₂, hpos.hβ₁, hpos.hα₂]

/-- Consequently the 4-group orbit average of any feasible positive point in the
    m004 polytope is itself both `GA`-feasible and `Positive` on the fixed line. -/
theorem GA_and_Positive_orbit_average {α₁ β₁ γ₁ α₂ β₂ γ₂ : ℝ}
    (hga : GA α₁ β₁ γ₁ α₂ β₂ γ₂) (hpos : Positive α₁ β₁ γ₁ α₂ β₂ γ₂) :
    let t := (α₁ + γ₁ + β₂ + γ₂) / 4
    GA t (1 - 2 * t) t (1 - 2 * t) t t ∧
      Positive t (1 - 2 * t) t (1 - 2 * t) t t := by
  refine ⟨GA_on_line _, ?_⟩
  rw [fixed_positive_iff]
  exact orbit_average_mem_open_segment hga hpos

end QOU.Knot.M004AngleStructure
