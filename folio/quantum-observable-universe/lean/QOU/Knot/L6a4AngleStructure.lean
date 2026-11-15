/-
  L6a4 (Borromean rings) angle structure: the symmetric point is UNIQUE, and it
  is the regular ideal octahedron.  Bean `qou-krvm`, the L6a4 half.

  COMPANION TO `M004AngleStructure` — AND ITS OPPOSITE.  Bean qou-krvm's
  hypothesis (ii) ("the symmetric point is UNIQUE") is FALSE for m004, whose
  fixed locus is a line.  For L6a4 it is TRUE, and this file proves it.  So the
  two anchors of PR #4513 are explained differently:

    m004  (muon)   |Sym| = 4    fixed locus a LINE   -> symmetry does NOT pin it;
                                the Casson-Rivin objective finishes the job
    L6a4 (proton)  |Sym| = 16   fixed locus a POINT  -> symmetry ALONE pins it,
                                so `SymmetricOptimum.symmetric_point_optimal`
                                applies directly and the measured vanishing
                                offset at the proton anchor is forced

  WHAT IS PROVED HERE (sorry-free)

  * `GA.gen0/1/2` — the three generators of the order-16 coordinate symmetry
    preserve the generalised-angle system.  (The full group is order 16; three
    generators suffice, verified minimal by exhaustive search.)
  * `fixed_orbitA` / `fixed_orbitB` — a fixed point is CONSTANT on each of the
    two orbits (sizes 16 and 8), by explicit chains of generator steps.
  * `unique_symmetric_point` — a fixed feasible point is exactly the regular
    ideal octahedron point: `1/4` on the size-16 orbit, `1/2` on the size-8
    orbit.  This is bean qou-krvm's hypothesis (ii), TRUE for this anchor.

  THE SYSTEM IS OVERDETERMINED AND CONSISTENT, which is what makes uniqueness
  immediate.  On an orbit-constant point the 16 constraints collapse to just
  three distinct equations:

      tet   (x8):  2a + b = 1
      edge  (x4):  8a     = 2      ->  a = 1/4
      edge  (x4):      4b = 2      ->  b = 1/2

  The two edge families pin `a` and `b` OUTRIGHT, and `2a + b = 1` is then a
  compatibility check that happens to hold (2/4 + 1/2 = 1).  Every tetrahedron
  carries exactly one size-8 coordinate and two size-16 coordinates — the
  (pi/4, pi/4, pi/2) shape of the regular ideal octahedron.

  PROVENANCE.  The 24-variable system, the generators and the orbits are NOT
  hand-typed: this file is GENERATED from SnapPy via the corpus's own
  `gluing` / `ga_equalities` helpers (`borromean_angle_structure_lp_probe`),
  the same system the LP was solved against.  The symmetry group was found by
  label-preserving graph automorphism with every candidate verified
  algebraically (rref of the augmented system), and recorded in
  `computations/probes/qbeta-krvm-ga-symmetry-fixed-locus.witness.json`.

  HONESTY BOUNDARY.  As in the m004 file: this is the SYMMETRY half.  Bean
  qou-krvm's hypothesis (iv) — that the hyperbolic volume functional is concave
  and invariant (Rivin) — is untouched; Mathlib has no ideal-tetrahedron volume
  theory.  Nothing here says the LP optimum is unique, only that the SYMMETRIC
  point is.

  Archimedean (R): ordering and division over R (§7c).

  -- Ref: [leitner2026] computations/probes/qbeta_krvm_ga_symmetry_fixed_locus_probe.py
  -- Ref: [garoufalidis2012] arXiv:1208.1663 §2.2-2.3 (generalised angle structures)
-/

import Mathlib.Tactic

namespace QOU.Knot.L6a4AngleStructure

/-- The 24 tetrahedron angles of the L6a4 (Borromean rings) triangulation,
in pi-units: 8 ideal tetrahedra, 3 angles each.  Indexed by `Nat` rather than
`Fin 24` so the permutation generators reduce definitionally at literal indices;
coordinates past 23 are simply unconstrained and never referenced. -/
abbrev Pt := Nat -> ℝ

/-- **The L6a4 generalised angle structure.**  SnapPy's 8 per-tetrahedron
sums and 8 edge equations, in pi-units. Generated from the measured system. -/
structure GA (x : Pt) : Prop where
  tet0 : x 0 + x 1 + x 2 = 1
  tet1 : x 3 + x 4 + x 5 = 1
  tet2 : x 6 + x 7 + x 8 = 1
  tet3 : x 9 + x 10 + x 11 = 1
  tet4 : x 12 + x 13 + x 14 = 1
  tet5 : x 15 + x 16 + x 17 = 1
  tet6 : x 18 + x 19 + x 20 = 1
  tet7 : x 21 + x 22 + x 23 = 1
  edge0 : x 0 + x 1 + x 3 + x 5 + x 6 + x 11 + x 15 + x 19 = 2
  edge1 : x 2 + x 4 + x 13 + x 23 = 2
  edge2 : x 2 + x 7 + x 10 + x 13 = 2
  edge3 : x 1 + x 5 + x 6 + x 8 + x 14 + x 15 + x 16 + x 22 = 2
  edge4 : x 0 + x 3 + x 9 + x 11 + x 12 + x 18 + x 19 + x 21 = 2
  edge5 : x 4 + x 17 + x 20 + x 23 = 2
  edge6 : x 7 + x 10 + x 17 + x 20 = 2
  edge7 : x 8 + x 9 + x 12 + x 14 + x 16 + x 18 + x 21 + x 22 = 2

/-- Symmetry generator 0 of the order-16 coordinate group. -/
def sigma0 : Nat -> Nat
  | 0 => 1
  | 1 => 0
  | 2 => 2
  | 3 => 5
  | 4 => 4
  | 5 => 3
  | 6 => 11
  | 7 => 10
  | 8 => 9
  | 9 => 8
  | 10 => 7
  | 11 => 6
  | 12 => 14
  | 13 => 13
  | 14 => 12
  | 15 => 19
  | 16 => 18
  | 17 => 20
  | 18 => 16
  | 19 => 15
  | 20 => 17
  | 21 => 22
  | 22 => 21
  | 23 => 23
  | n => n

/-- Symmetry generator 1 of the order-16 coordinate group. -/
def sigma1 : Nat -> Nat
  | 0 => 3
  | 1 => 5
  | 2 => 4
  | 3 => 0
  | 4 => 2
  | 5 => 1
  | 6 => 15
  | 7 => 17
  | 8 => 16
  | 9 => 18
  | 10 => 20
  | 11 => 19
  | 12 => 21
  | 13 => 23
  | 14 => 22
  | 15 => 6
  | 16 => 8
  | 17 => 7
  | 18 => 9
  | 19 => 11
  | 20 => 10
  | 21 => 12
  | 22 => 14
  | 23 => 13
  | n => n

/-- Symmetry generator 2 of the order-16 coordinate group. -/
def sigma2 : Nat -> Nat
  | 0 => 6
  | 1 => 8
  | 2 => 7
  | 3 => 15
  | 4 => 17
  | 5 => 16
  | 6 => 14
  | 7 => 13
  | 8 => 12
  | 9 => 0
  | 10 => 2
  | 11 => 1
  | 12 => 11
  | 13 => 10
  | 14 => 9
  | 15 => 22
  | 16 => 21
  | 17 => 23
  | 18 => 3
  | 19 => 5
  | 20 => 4
  | 21 => 19
  | 22 => 18
  | 23 => 20
  | n => n

/-- A point is **fixed** when all three generators leave it unchanged. -/
def Fixed (x : Pt) : Prop :=
  (∀ i, x (sigma0 i) = x i) ∧ (∀ i, x (sigma1 i) = x i) ∧
  (∀ i, x (sigma2 i) = x i)

/-- **Generator 0 preserves the angle structure.**  It permutes the
constraint rows among themselves; the proof is the resulting linear identity. -/
theorem GA.gen0 {x : Pt} (h : GA x) : GA (fun i => x (sigma0 i)) := by
  obtain ⟨t0, t1, t2, t3, t4, t5, t6, t7, e0, e1, e2, e3, e4, e5, e6, e7⟩ := h
  constructor <;> simp only [sigma0] <;> linarith

/-- **Generator 1 preserves the angle structure.**  It permutes the
constraint rows among themselves; the proof is the resulting linear identity. -/
theorem GA.gen1 {x : Pt} (h : GA x) : GA (fun i => x (sigma1 i)) := by
  obtain ⟨t0, t1, t2, t3, t4, t5, t6, t7, e0, e1, e2, e3, e4, e5, e6, e7⟩ := h
  constructor <;> simp only [sigma1] <;> linarith

/-- **Generator 2 preserves the angle structure.**  It permutes the
constraint rows among themselves; the proof is the resulting linear identity. -/
theorem GA.gen2 {x : Pt} (h : GA x) : GA (fun i => x (sigma2 i)) := by
  obtain ⟨t0, t1, t2, t3, t4, t5, t6, t7, e0, e1, e2, e3, e4, e5, e6, e7⟩ := h
  constructor <;> simp only [sigma2] <;> linarith

/-- A fixed point is **constant on the size-16 orbit** (representative `0`). -/
theorem fixed_orbitA {x : Pt} (hf : Fixed x) :
    x 1 = x 0 ∧ x 3 = x 0 ∧ x 5 = x 0 ∧ x 6 = x 0 ∧ x 8 = x 0 ∧ x 9 = x 0 ∧ x 11 = x 0 ∧ x 12 = x 0 ∧ x 14 = x 0 ∧ x 15 = x 0 ∧ x 16 = x 0 ∧ x 18 = x 0 ∧ x 19 = x 0 ∧ x 21 = x 0 ∧ x 22 = x 0 := by
  obtain ⟨f0, f1, f2⟩ := hf
  have h1 : x 1 = x 0 := by
    have := f0 0; simpa [sigma0] using this
  have h3 : x 3 = x 0 := by
    have := f1 0; simpa [sigma1] using this
  have h6 : x 6 = x 0 := by
    have := f2 0; simpa [sigma2] using this
  have h5 : x 5 = x 1 := by
    have := f1 1; simpa [sigma1] using this
  have h8 : x 8 = x 1 := by
    have := f2 1; simpa [sigma2] using this
  have h11 : x 11 = x 6 := by
    have := f0 6; simpa [sigma0] using this
  have h14 : x 14 = x 6 := by
    have := f2 6; simpa [sigma2] using this
  have h15 : x 15 = x 3 := by
    have := f2 3; simpa [sigma2] using this
  have h9 : x 9 = x 8 := by
    have := f0 8; simpa [sigma0] using this
  have h12 : x 12 = x 8 := by
    have := f2 8; simpa [sigma2] using this
  have h16 : x 16 = x 5 := by
    have := f2 5; simpa [sigma2] using this
  have h19 : x 19 = x 15 := by
    have := f0 15; simpa [sigma0] using this
  have h22 : x 22 = x 15 := by
    have := f2 15; simpa [sigma2] using this
  have h18 : x 18 = x 16 := by
    have := f0 16; simpa [sigma0] using this
  have h21 : x 21 = x 16 := by
    have := f2 16; simpa [sigma2] using this
  exact ⟨by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith⟩

/-- A fixed point is **constant on the size-8 orbit** (representative `2`). -/
theorem fixed_orbitB {x : Pt} (hf : Fixed x) :
    x 4 = x 2 ∧ x 7 = x 2 ∧ x 10 = x 2 ∧ x 13 = x 2 ∧ x 17 = x 2 ∧ x 20 = x 2 ∧ x 23 = x 2 := by
  obtain ⟨f0, f1, f2⟩ := hf
  have h4 : x 4 = x 2 := by
    have := f1 2; simpa [sigma1] using this
  have h7 : x 7 = x 2 := by
    have := f2 2; simpa [sigma2] using this
  have h10 : x 10 = x 7 := by
    have := f0 7; simpa [sigma0] using this
  have h13 : x 13 = x 7 := by
    have := f2 7; simpa [sigma2] using this
  have h17 : x 17 = x 4 := by
    have := f2 4; simpa [sigma2] using this
  have h20 : x 20 = x 17 := by
    have := f0 17; simpa [sigma0] using this
  have h23 : x 23 = x 17 := by
    have := f2 17; simpa [sigma2] using this
  exact ⟨by linarith, by linarith, by linarith, by linarith, by linarith, by linarith, by linarith⟩

/-- **The unique symmetric point (bean qou-krvm hypothesis (ii), TRUE here).**
A feasible point fixed by the symmetry group is exactly the regular ideal
octahedron: `1/4` on the size-16 orbit, `1/2` on the size-8 orbit.

Contrast `M004AngleStructure.fixed_iff_line`, where the same hypothesis is
FALSE and the fixed locus is one-dimensional. -/
theorem unique_symmetric_point {x : Pt} (h : GA x) (hf : Fixed x) :
    x 0 = 1/4 ∧ x 2 = 1/2 := by
  obtain ⟨t0, t1, t2, t3, t4, t5, t6, t7, e0, e1, e2, e3, e4, e5, e6, e7⟩ := h
  obtain ⟨a1, a3, a5, a6, a8, a9, a11, a12, a14, a15, a16, a18, a19, a21, a22⟩ := fixed_orbitA hf
  obtain ⟨b4, b7, b10, b13, b17, b20, b23⟩ := fixed_orbitB hf
  constructor <;> linarith

/-! ## Non-vacuity: the point exists

`unique_symmetric_point` says AT MOST one symmetric feasible point. On its own
that would also hold if there were NONE — the theorem would be vacuously true.
These two witnesses close that hole by exhibiting the point. -/

/-- The regular ideal octahedron point: `1/2` on the size-8 orbit, `1/4`
elsewhere. -/
noncomputable def regularOctahedron : Pt := fun n =>
  if n = 2 ∨ n = 4 ∨ n = 7 ∨ n = 10 ∨ n = 13 ∨ n = 17 ∨ n = 20 ∨ n = 23
  then 1/2 else 1/4

/-- It is feasible. -/
theorem GA_regularOctahedron : GA regularOctahedron := by
  constructor <;> norm_num [regularOctahedron]

/-- It is fixed by the whole symmetry group. -/
theorem Fixed_regularOctahedron : Fixed regularOctahedron := by
  refine ⟨?_, ?_, ?_⟩ <;> intro i <;>
    (rcases i with _|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|n <;>
      simp [sigma0, sigma1, sigma2, regularOctahedron])

/-- **The symmetric point exists and is unique.**  Combining the two: L6a4's
fixed locus is exactly one point, the regular ideal octahedron — bean
`qou-krvm` hypothesis (ii), TRUE for this anchor and FALSE for m004. -/
theorem symmetric_point_exists_unique :
    GA regularOctahedron ∧ Fixed regularOctahedron ∧
      ∀ x : Pt, GA x → Fixed x → x 0 = 1/4 ∧ x 2 = 1/2 :=
  ⟨GA_regularOctahedron, Fixed_regularOctahedron,
   fun _ h hf => unique_symmetric_point h hf⟩

end QOU.Knot.L6a4AngleStructure
