/-
  The 5₂ knot, through the volume bridge — exactly, and NOT with positivity.

  Bean `qou-f8lit`.  Companion to `Encounter/FigureEightVolumeBridge.lean`.

  ═══ THE SAME DEFECT, AT THE SECOND KNOT ═══

  The figure-eight file records that `MostowRigidity.figureEight` carries a
  15-significant-digit **truncation** rather than the exact volume.  The `:leanval`
  audit (16 sites, 7 keys) shows `MostowRigidity.knot5_2` has it too:

      MostowRigidity.knot5_2.volume := 2.82812208833078     -- entered, 15 digits
      VOL_5_2 := 3 * BlochWigner_lob fiveTwoShape
               = 2.8281220883307831627638988092766349…      -- exact

  They diverge at the 16th digit.  And `fiveTwoTriangulation_volume :
  fiveTwoTriangulation.volume = VOL_5_2` is proved sorry-free, so the same argument
  applies verbatim: a bridge statement keyed on the literal would be unusable at the
  corpus's own 5₂ triangulation.  This file is therefore keyed on `VOL_5_2`.

  **What the audit also found — the defect class is bounded, and smaller than the site
  count suggests.**  Of the seven `:leanval` keys, only the two hyperbolic volumes are
  affected.  `m_p_MeV`, `m_e_MeV` and `q_0` are **not** defects and must not be
  "fixed": a CODATA mass is a *measurement* with no closed form to disagree with, and
  `q₀` is a root of a transcendental equation whose canonical form IS the 50-dps
  witness.  A truncated literal is a defect only where the corpus carries an exact
  closed form for the same quantity and something treats the two as interchangeable.

  ═══ POSITIVITY IS ABSENT HERE, AND THAT IS THE HONEST OUTCOME ═══

  `FigureEightVolumeBridge` proves `0 < vol m`.  **This file does not, and the
  difference is not an oversight.**  That proof went through
  `QOU.Knot.Cl_2_pi_div_three_pos`, which exists because the 4₁ shape sits on the unit
  circle, so its Bloch–Wigner value *is* a Clausen value.  The 5₂ shape is the root of
  `X³ − 2X² + 3X − 1`; it is not on the unit circle and there is no Clausen special case
  to appeal to.

  Measured: the corpus has **no** `0 < BlochWigner_lob z` for `0 < z.im`.  What it has
  is `BlochWigner_lob_real_eq_zero` — vanishing *on the reals* — which is the opposite
  boundary and gives nothing here.

  So the general positivity `ManifoldVolumeBridge` declined to assume is still open, and
  the 4₁ result was a special case rather than the start of a pattern.  Recording that
  explicitly, because "we proved it for 4₁" invites the assumption that 5₂ follows, and
  it does not.

  ═══ STILL NOT PROVED ═══

  That `fiveTwoTriangulation` triangulates `S³ ∖ 5₂` — Thurston, as for 4₁ — and that
  the entered literal differs from `VOL_5_2` as a *Lean* fact rather than a numerical
  observation (that needs a rigorous 16-digit bound on `BlochWigner_lob fiveTwoShape`).

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [neumann-zagier1985] §2
-/
import QOU.MathlibExt.ManifoldVolumeBridge
import QOU.Knot.FiveTwoVolumeConstant
import QOU.Encounter.FigureEightVolumeBridge

namespace QOU.Encounter.FiveTwoVolumeBridge

open QOU.MathlibExt QOU.Archimedean QOU.Knot.FiveTwoVolume

variable {M : Type*} [HyperbolicVolumeBridge M]

/-- **A manifold realised by the 5₂ triangulation has volume exactly `VOL_5_2`.**

Keyed on the exact constant, not on `MostowRigidity.knot5_2`'s truncated literal — see
the module header. Composes the bridge's transport with the corpus's sorry-free
`fiveTwoTriangulation_volume`. -/
theorem vol_eq_VOL_5_2_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises fiveTwoTriangulation m) :
    HyperbolicVolumeBridge.vol m = VOL_5_2 := by
  rw [HyperbolicVolumeBridge.vol_eq_of_realises fiveTwoTriangulation m h,
    fiveTwoTriangulation_volume]

/-- The same, as the Bloch–Wigner sum over the three tetrahedra of the 5₂
triangulation. -/
theorem vol_eq_three_blochWigner_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises fiveTwoTriangulation m) :
    HyperbolicVolumeBridge.vol m = 3 * BlochWigner_lob fiveTwoShape :=
  vol_eq_VOL_5_2_of_realises m h

/-- **The 4₁ and 5₂ volumes are comparable through the bridge.**

If one manifold is realised by the 4₁ triangulation and another by the 5₂
triangulation, their volumes stand in the same relation as the two exact constants.
Stated as an equivalence rather than an inequality on purpose: the corpus does not
carry `VOL_4_1 < VOL_5_2` as a proved fact — `MostowRigidity`'s version of that
comparison discharges by `norm_num` on the two **truncated literals**, which is a
statement about the decimals, not about the constants. -/
theorem vol_lt_iff_of_realises {N : Type*} [HyperbolicVolumeBridge N]
    (m : M) (n : N)
    (hm : HyperbolicVolumeBridge.Realises
      QOU.Knot.FigureEightTri.figureEightTriangulation m)
    (hn : HyperbolicVolumeBridge.Realises fiveTwoTriangulation n) :
    HyperbolicVolumeBridge.vol m < HyperbolicVolumeBridge.vol n ↔
      QOU.Knot.FigureEightVolume.VOL_4_1 < VOL_5_2 := by
  rw [QOU.Encounter.FigureEightVolumeBridge.vol_eq_VOL_4_1_of_realises m hm,
    vol_eq_VOL_5_2_of_realises n hn]

end QOU.Encounter.FiveTwoVolumeBridge
