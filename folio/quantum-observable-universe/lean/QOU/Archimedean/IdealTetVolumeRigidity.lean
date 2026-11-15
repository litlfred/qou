import QOU.Archimedean.BlochRigidity.Instance

/-!
# Ideal-tetrahedron volume = a multiple of Bloch–Wigner, by rigidity (T2 route)

Categorify audit 2026-11-15, item 2. The T2 identity (`MostowIdealTetVolume`) is proved there
by integrating over the chimney, and its obtuse case by analytic continuation
(`TetVolAnalytic`). This file gives the other route: **any** function of the shape parameter
that has the three properties below is `c · D`, by PR #7946's rigidity theorem
(`blochSuslinRigidity_blochD`), and the constant is fixed by one value.

For the hyperbolic volume `V(z)` of the ideal tetrahedron with vertices `0, 1, z, ∞`, the three
inputs are geometric:

1. **Continuity** of `V` in `z` off `{0, 1}` (`hc`).
2. **Symmetries** (`hs`): `V(z̄) = −V(z)` (orientation reversal) and `V(1/z) = −V(z)` (the
   relabelling that inverts the shape parameter, with orientation).
3. **The five-term relation** (`h5`): the 2–3 move cuts one polytope into two tetrahedra or
   into three, so the signed volumes satisfy Suslin's relation. This uses only finite additivity
   and isometry invariance of volume.

**What is proved here.** The implication: (1)–(3) ⟹ `V = (V(i)/D(i))·D` on `ℂ ∖ {0,1}`,
acute and obtuse shapes at once, with no integral. **What is not proved here.** (1)–(3) for the
Lean hyperbolic volume: they are the remaining geometric propositions of this route, and none is
assumed as an axiom.

-- Ref: [leitner2026] /mnt/project-files/qou-categorify-audit/analytic-steps-ranked-2026-11-15.md item 2
-/

namespace QOU.Archimedean.IdealTetVolumeRigidity

open Complex QOU.Archimedean QOU.Archimedean.FiveTermProof

/-- **Rigidity for a volume-type function.** Under continuity, the Bloch–Wigner symmetries and
the five-term relation, `V` is the multiple of `D` fixed by its value at `i`. -/
theorem eq_div_mul_blochD (V : ℂ → ℝ) (hc : ContinuousOn V {0, 1}ᶜ) (hs : BlochSymmetric V)
    (h5 : SuslinFiveTerm V) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → V z = V I / blochD I * blochD z := by
  obtain ⟨c, hcV⟩ := BlochSuslinRigidity.uniqueness (D := blochD) V hc hs h5
  have hI1 : (I : ℂ) ≠ 1 := by intro h; have := congrArg Complex.im h; simp at this
  have hcI : c = V I / blochD I := by
    rw [hcV I I_ne_zero hI1, mul_div_assoc, div_self blochD_I_pos.ne', mul_one]
  intro z h0 h1
  rw [hcV z h0 h1, hcI]

/-- **The calibrated form.** If moreover `V(i) = D(i)` (the regular ideal octahedron's
quarter, i.e. the right-angled shape), then `V = D` on `ℂ ∖ {0,1}`. -/
theorem eq_blochD_of_value_at_I (V : ℂ → ℝ) (hc : ContinuousOn V {0, 1}ᶜ)
    (hs : BlochSymmetric V) (h5 : SuslinFiveTerm V) (hI : V I = blochD I) :
    ∀ z : ℂ, z ≠ 0 → z ≠ 1 → V z = blochD z := by
  intro z h0 h1
  rw [eq_div_mul_blochD V hc hs h5 z h0 h1, hI, div_self blochD_I_pos.ne', one_mul]

end QOU.Archimedean.IdealTetVolumeRigidity
