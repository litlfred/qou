/-
  T4: the REGULAR ideal tetrahedron maximises the Lobachevsky volume sum.

  This is `qou-idvt` T4 ("the regular triple maximises T2 ... and feeds
  `qou-7y3g`"), obtained from T3's strict concavity plus the symmetry of the
  functional.  Milnor's classical theorem, in the analytic form the corpus can
  state without hyperbolic-volume theory.

  THE MATHLIB GAP THIS FILLS.  Two small facts about `Λ` that Mathlib lacks and
  the corpus had not yet stated -- both immediate from Clausen lemmas already
  in the tree, which is why this is a thin fill rather than new theory:

    `continuous_Lob`  : `Λ` is continuous            (from `QOU.Knot.continuous_Cl_2`)
    `Lob_pi_sub`      : `Λ(π - t) = -Λ(t)`           (from `QOU.Knot.Cl_2_two_pi_sub`)

  `Lob_pi_sub` is the load-bearing one: it makes the volume sum vanish on the
  ENTIRE boundary of the closed simplex, which is what confines the maximum to
  the interior and so makes T3's uniqueness applicable at all.

  THE ARGUMENT.
    1. The closed simplex is compact and `volChart` is continuous, so a maximum
       exists on it.
    2. On the boundary the sum is `0` (each degenerate face kills it, via
       `Lob_pi_sub` and `Lob_zero`).
    3. At the regular point the value is `3Λ(π/3) = Cl₂(π/3) > 0` -- reusing
       the corpus's own `three_Lob_pi_div_three` and `Cl_2_pi_div_three_pos`.
    4. So the maximiser lies in the OPEN simplex, where T3 says it is unique.
    5. `volChart` is invariant under the two generating angle swaps, so the
       unique maximiser is fixed by both -- forcing it to be `(π/3, π/3)`.

  Step 5 is the standard symmetry argument, and it is legitimate here only
  because step 4 supplied EXISTENCE: uniqueness alone would let the "maximiser"
  be vacuous.

  WHAT THIS IS NOT -- read before citing.

  * **Still not a hyperbolic-volume statement.**  As in
    `IdealTetrahedronVolumeConcavity`, `volChart` is DEFINED as the Λ-sum.  That
    the Λ-sum is the ideal tetrahedron's volume is `qou-idvt` T2, still open and
    still needing hyperbolic-volume theory Mathlib does not have.  So this says
    "the regular triple maximises this analytic function", NOT "the regular
    ideal tetrahedron has maximal hyperbolic volume" -- the latter is the former
    ONLY modulo T2.
  * **`qou-7y3g` is NOT closed.**  That bean wants `Vol(4₁) = 2 × V_tet` as a
    statement about the manifold's volume.  What lands here is the `V_tet` side:
    the maximum value is exactly `Cl₂(π/3)`, so `2 × (the max) = 2 Cl₂(π/3)`,
    the number the bean records numerically.  The bridge from "the manifold's
    volume" to "twice this maximum" is the geometric content, untouched.
  * **`qou-krvm` (iv) is NOT discharged** -- see the sibling file's header.
  * **Nothing wired.**  No mass, binding, or substrate claim.

  Archimedean (ℝ): ordering, `sin`, `cos`, `log` -- §7c.

  -- Ref: [milnor1982] Hyperbolic geometry: the first 150 years (the regular
  --      ideal simplex maximises volume)
  -- Ref: [leitner2026] beans qou-idvt (T4), qou-7y3g
-/

import QOU.Archimedean.IdealTetrahedronVolumeConcavity
import QOU.Knot.Clausen

namespace QOU.Archimedean.IdealTetrahedronConcavity

open QOU.Archimedean Set

/-! ### Mathlib-gap fills for `Λ` -/

/-- **`Λ` is continuous**, inherited from `Cl₂`. -/
theorem continuous_Lob : Continuous Lob := by
  unfold Lob
  exact (QOU.Knot.continuous_Cl_2.comp (continuous_const.mul continuous_id)).div_const 2

/-- **`Λ(π - t) = -Λ(t)`** -- antisymmetry about `π/2`, from `Cl₂`'s
antisymmetry about `π`.  This is what makes the volume sum vanish on every
degenerate face of the simplex. -/
theorem Lob_pi_sub (t : ℝ) : Lob (Real.pi - t) = -Lob t := by
  unfold Lob
  rw [show 2 * (Real.pi - t) = 2 * Real.pi - 2 * t by ring, QOU.Knot.Cl_2_two_pi_sub]
  ring

/-! ### The two identities Milnor's volume proof actually consumes

Sourced from the Appendix of [milnor1982] (full text now in `library/`), which
states `Λ` is "odd, periodic of period π" and, in the orthoscheme computation,
substitutes `Λ(2a) = 2Λ(a) + 2Λ(a + π/2)` to reduce the value to `Λ(a)/2`.
Those are H4-4's inputs; both fall out of Clausen lemmas already in the tree.

Milnor's general multiplication identity `Λ(nθ) = n Σ_{k mod n} Λ(θ + kπ/n)` is
NOT proved here -- only the `n = 2` case below, which is what the volume proof
uses. The general case is left open (`qou-w3eg`). -/

/-- **`Λ` has period `π`** -- Milnor's Appendix, Lemma 1. Immediate from `Cl₂`'s
`2π`-periodicity, since `Λ(t) = Cl₂(2t)/2` doubles the argument. -/
theorem Lob_add_pi (t : ℝ) : Lob (t + Real.pi) = Lob t := by
  unfold Lob
  rw [show 2 * (t + Real.pi) = 2 * t + 2 * Real.pi by ring, Cl_2_add_two_pi]

/-- **The duplication identity `Λ(2a) = 2Λ(a) + 2Λ(a + π/2)`.**

This is the `n = 2` case of Milnor's multiplication identity, and the exact
substitution his orthoscheme computation makes to collapse
`(Λ(π/2 + a) + Λ(2a) + Λ(π/2 - a) - Λ(0))/4` to `Λ(a)/2`.

Proof: `Cl_2_duplication` at `θ = 2a` gives `Cl₂(4a) = 2Cl₂(2a) - 2Cl₂(π - 2a)`,
and `Cl_2_two_pi_sub` at `π - 2a` gives `Cl₂(π + 2a) = -Cl₂(π - 2a)`, which is
precisely the term needed to match. -/
theorem Lob_duplication (a : ℝ) :
    Lob (2 * a) = 2 * Lob a + 2 * Lob (a + Real.pi / 2) := by
  unfold Lob
  have hdup : Cl_2 (2 * (2 * a)) = 2 * Cl_2 (2 * a) - 2 * Cl_2 (Real.pi - 2 * a) :=
    Cl_2_duplication (2 * a)
  have hrefl : Cl_2 (2 * Real.pi - (Real.pi - 2 * a)) = -Cl_2 (Real.pi - 2 * a) :=
    QOU.Knot.Cl_2_two_pi_sub (Real.pi - 2 * a)
  have hsimp : 2 * Real.pi - (Real.pi - 2 * a) = 2 * (a + Real.pi / 2) := by ring
  rw [hsimp] at hrefl
  rw [hdup, hrefl]
  ring

/-! ### The closed simplex -/

/-- The CLOSED angle simplex.  Compact, so a maximum exists on it. -/
def closedSimplex : Set (ℝ × ℝ) :=
  {p | 0 ≤ p.1 ∧ 0 ≤ p.2 ∧ p.1 + p.2 ≤ Real.pi}

theorem angleSimplex_subset_closed : angleSimplex ⊆ closedSimplex := by
  rintro p ⟨h1, h2, h3⟩
  exact ⟨h1.le, h2.le, h3.le⟩

theorem isClosed_closedSimplex : IsClosed closedSimplex := by
  have h : closedSimplex = {p : ℝ × ℝ | 0 ≤ p.1} ∩
      ({p : ℝ × ℝ | 0 ≤ p.2} ∩ {p : ℝ × ℝ | p.1 + p.2 ≤ Real.pi}) := by
    ext p; simp [closedSimplex]
  rw [h]
  exact (isClosed_le continuous_const continuous_fst).inter
    ((isClosed_le continuous_const continuous_snd).inter
      (isClosed_le (continuous_fst.add continuous_snd) continuous_const))

theorem isCompact_closedSimplex : IsCompact closedSimplex := by
  refine IsCompact.of_isClosed_subset
    ((isCompact_Icc (a := (0 : ℝ)) (b := Real.pi)).prod
      (isCompact_Icc (a := (0 : ℝ)) (b := Real.pi)))
    isClosed_closedSimplex ?_
  rintro p ⟨h1, h2, h3⟩
  exact ⟨⟨h1, by linarith⟩, ⟨h2, by linarith⟩⟩

theorem continuous_volChart : Continuous volChart := by
  unfold volChart
  exact ((continuous_Lob.comp continuous_fst).add
    (continuous_Lob.comp continuous_snd)).add
    (continuous_Lob.comp ((continuous_const.sub continuous_fst).sub continuous_snd))

/-! ### The boundary is where the volume vanishes -/

/-- **The volume sum vanishes on the boundary of the closed simplex.**
Each of the three degenerate faces kills it, via `Lob_pi_sub`. -/
theorem volChart_eq_zero_of_not_mem
    {p : ℝ × ℝ} (hp : p ∈ closedSimplex) (hnot : p ∉ angleSimplex) :
    volChart p = 0 := by
  obtain ⟨h1, h2, h3⟩ := hp
  simp only [angleSimplex, Set.mem_setOf_eq, not_and_or, not_lt] at hnot
  unfold volChart
  rcases hnot with h | h | h
  · -- α = 0
    have hα : p.1 = 0 := le_antisymm h h1
    rw [hα, Lob_zero, show Real.pi - 0 - p.2 = Real.pi - p.2 by ring, Lob_pi_sub]
    ring
  · -- β = 0
    have hβ : p.2 = 0 := le_antisymm h h2
    rw [hβ, Lob_zero, show Real.pi - p.1 - 0 = Real.pi - p.1 by ring, Lob_pi_sub]
    ring
  · -- α + β = π, so γ = 0
    have hsum : p.1 + p.2 = Real.pi := le_antisymm h3 h
    have hγ : Real.pi - p.1 - p.2 = 0 := by linarith
    have hβ : p.2 = Real.pi - p.1 := by linarith
    rw [hγ, Lob_zero, hβ, Lob_pi_sub]
    ring

/-- At the regular point the value is `3Λ(π/3) = Cl₂(π/3) > 0`. -/
theorem volChart_regular_pos : 0 < volChart ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) := by
  have hval : volChart ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ)
      = 3 * (Cl_2 (2 * (Real.pi / 3)) / 2) := by
    unfold volChart Lob
    rw [show Real.pi - Real.pi / 3 - Real.pi / 3 = 2 * (Real.pi / 3) / 2 * 2 - Real.pi / 3
      by ring]
    ring_nf
  rw [hval, three_Lob_pi_div_three]
  exact QOU.Knot.Cl_2_pi_div_three_pos

/-! ### Existence of the maximiser -/

/-- **A maximiser exists, and it lies in the OPEN simplex.**

Compactness gives a maximum on the closed simplex; the boundary value `0` and
the strictly positive regular value push it into the interior.  This is the step
that makes T3's uniqueness non-vacuous. -/
theorem exists_isMaxOn_angleSimplex :
    ∃ m ∈ angleSimplex, IsMaxOn volChart angleSimplex m := by
  obtain ⟨m, hmS, hmax⟩ := isCompact_closedSimplex.exists_isMaxOn
    ⟨(Real.pi / 3, Real.pi / 3), by
      refine ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩⟩
    continuous_volChart.continuousOn
  have hreg : ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) ∈ closedSimplex :=
    ⟨by linarith [Real.pi_pos], by linarith [Real.pi_pos], by linarith [Real.pi_pos]⟩
  have hpos : 0 < volChart m := lt_of_lt_of_le volChart_regular_pos (hmax hreg)
  have hmem : m ∈ angleSimplex := by
    by_contra hcon
    rw [volChart_eq_zero_of_not_mem hmS hcon] at hpos
    exact lt_irrefl 0 hpos
  exact ⟨m, hmem, fun x hx => hmax (angleSimplex_subset_closed hx)⟩

/-! ### The two generating symmetries -/

theorem volChart_swap (p : ℝ × ℝ) : volChart ((p.2, p.1) : ℝ × ℝ) = volChart p := by
  unfold volChart
  rw [show Real.pi - p.2 - p.1 = Real.pi - p.1 - p.2 by ring]
  ring

theorem volChart_swap_snd_thd (p : ℝ × ℝ) :
    volChart ((p.1, Real.pi - p.1 - p.2) : ℝ × ℝ) = volChart p := by
  unfold volChart
  rw [show Real.pi - p.1 - (Real.pi - p.1 - p.2) = p.2 by ring]
  ring

theorem swap_mem {p : ℝ × ℝ} (hp : p ∈ angleSimplex) :
    ((p.2, p.1) : ℝ × ℝ) ∈ angleSimplex :=
  ⟨hp.2.1, hp.1, by have := hp.2.2; simpa using by linarith⟩

theorem swap_snd_thd_mem {p : ℝ × ℝ} (hp : p ∈ angleSimplex) :
    ((p.1, Real.pi - p.1 - p.2) : ℝ × ℝ) ∈ angleSimplex := by
  obtain ⟨h1, h2, h3⟩ := hp
  exact ⟨h1, by simpa using by linarith, by simpa using by linarith⟩

/-! ### T4 -/

/-- **T4 — the regular triple `(π/3, π/3, π/3)` maximises the Lobachevsky volume
sum, and is the ONLY maximiser.**

Milnor's theorem, in its analytic form: this is a statement about the function
`Λ(α) + Λ(β) + Λ(π - α - β)`, and becomes the geometric statement only modulo
`qou-idvt` T2 (open). -/
theorem volChart_isMaxOn_regular :
    IsMaxOn volChart angleSimplex ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) := by
  obtain ⟨m, hmem, hmax⟩ := exists_isMaxOn_angleSimplex
  -- the swapped points are maximisers too, hence equal to `m` by T3
  have h1 : ((m.2, m.1) : ℝ × ℝ) = m := by
    refine volChart_maximiser_unique ?_ hmax (swap_mem hmem) hmem
    intro x hx
    rw [mem_setOf_eq, volChart_swap]
    exact hmax hx
  have h2 : ((m.1, Real.pi - m.1 - m.2) : ℝ × ℝ) = m := by
    refine volChart_maximiser_unique ?_ hmax (swap_snd_thd_mem hmem) hmem
    intro x hx
    rw [mem_setOf_eq, volChart_swap_snd_thd]
    exact hmax hx
  -- fixed by both swaps forces the regular point
  have he1 : m.2 = m.1 := congrArg Prod.fst h1
  have he2 : Real.pi - m.1 - m.2 = m.2 := congrArg Prod.snd h2
  have hm1 : m.1 = Real.pi / 3 := by linarith
  have hm2 : m.2 = Real.pi / 3 := by linarith
  have : m = ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) := Prod.ext hm1 hm2
  rwa [this] at hmax

/-- **The maximum VALUE is exactly `Cl₂(π/3)`.**

`qou-7y3g` records `Vol(4₁) = 2 × V_tet` numerically with
`V_tet = Cl₂(π/3)`; this supplies the `V_tet` side exactly.  The bridge to the
manifold's volume is the geometric content and is NOT supplied. -/
theorem volChart_max_value :
    volChart ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ) = Cl_2 (Real.pi / 3) := by
  have hval : volChart ((Real.pi / 3, Real.pi / 3) : ℝ × ℝ)
      = 3 * (Cl_2 (2 * (Real.pi / 3)) / 2) := by
    unfold volChart Lob
    rw [show Real.pi - Real.pi / 3 - Real.pi / 3 = 2 * (Real.pi / 3) / 2 * 2 - Real.pi / 3
      by ring]
    ring_nf
  rw [hval, three_Lob_pi_div_three]

end QOU.Archimedean.IdealTetrahedronConcavity
