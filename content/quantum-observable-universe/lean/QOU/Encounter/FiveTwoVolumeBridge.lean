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

  ═══ POSITIVITY, BY A ROUTE THAT AVOIDS BLOCH–WIGNER ENTIRELY ═══

  This section used to record that positivity was absent here and that its absence was
  the honest outcome.  **The reasoning it gave was correct and is kept below; only its
  conclusion has moved**, because a different route supplied the fact.

  The reasoning, unchanged: `FigureEightVolumeBridge`'s `0 < vol m` goes through
  `QOU.Knot.Cl_2_pi_div_three_pos`, which exists because the 4₁ shape sits on the unit
  circle, so its Bloch–Wigner value *is* a Clausen value.  The 5₂ shape is the root of
  `X³ − 2X² + 3X − 1`; it is not on the unit circle and there is no Clausen special case
  to appeal to.  That is still true, and the corpus still has **no**
  `0 < BlochWigner_lob z` for `0 < z.im` — the **strict** inequality, which is the one
  `ManifoldVolumeBridge` declined to assume, remains open.

  Say *strict*, though.  `Archimedean.BlochWignerNonneg.blochWigner_lob_nonneg` gives
  `0 ≤ D(z)` on the whole upper half plane, from Milnor's angle formula and
  `LobMonotonicity.lob_sum_nonneg`, so an unqualified "the corpus has no positivity for
  `D`" is now wrong.  Nonneg does not give what this file needs — `vol_ne_zero_of_realises`
  wants `≠ 0` — which is why the comparison route below is still the one doing the work.

  What closed it at 5₂ is `QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2` (bean
  `qou-52ch`): Rivin's strict concavity of the ideal-tetrahedron volume, applied along
  the line from the regular shape to the 5₂ shape, gives `VOL_4_1 < VOL_5_2` as a proved
  Lean fact.  Composed with `Cl_2_pi_div_three_pos` — which bounds `VOL_4_1` from below,
  not `VOL_5_2` — that yields `0 < VOL_5_2` without any statement about
  `BlochWigner_lob` on the upper half plane at all.

  So the shape of the earlier warning survives inverted: 5₂ does **not** follow from 4₁
  by the same argument, and it did not.  It follows from 4₁ by a *comparison*, which is
  a different thing and is the only reason this file can now carry positivity.

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
import QOU.Knot.FiveTwoVolumeChord

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
Stated as an equivalence because it is the transport statement: it says the bridge
carries the comparison faithfully, whatever the comparison turns out to be.  The
comparison itself is now proved — `vol_lt_of_realises` below discharges the right-hand
side — but the two are worth keeping separate, because `MostowRigidity`'s version of the
same comparison discharges by `norm_num` on the two **truncated literals**, which is a
statement about the decimals and not about the constants. -/
theorem vol_lt_iff_of_realises {N : Type*} [HyperbolicVolumeBridge N]
    (m : M) (n : N)
    (hm : HyperbolicVolumeBridge.Realises
      QOU.Knot.FigureEightTri.figureEightTriangulation m)
    (hn : HyperbolicVolumeBridge.Realises fiveTwoTriangulation n) :
    HyperbolicVolumeBridge.vol m < HyperbolicVolumeBridge.vol n ↔
      QOU.Knot.FigureEightVolume.VOL_4_1 < VOL_5_2 := by
  rw [QOU.Encounter.FigureEightVolumeBridge.vol_eq_VOL_4_1_of_realises m hm,
    vol_eq_VOL_5_2_of_realises n hn]

/-- **The 5₂ manifold has strictly larger volume than the 4₁ manifold** — the
inequality itself, not merely the transport of it.

Discharges the right-hand side of `vol_lt_iff_of_realises` with
`QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2`, which is proved from Rivin's strict
concavity along the chord from the regular ideal shape to the 5₂ shape — keyed on the
exact constants throughout, never on `MostowRigidity`'s truncated literals. -/
theorem vol_lt_of_realises {N : Type*} [HyperbolicVolumeBridge N]
    (m : M) (n : N)
    (hm : HyperbolicVolumeBridge.Realises
      QOU.Knot.FigureEightTri.figureEightTriangulation m)
    (hn : HyperbolicVolumeBridge.Realises fiveTwoTriangulation n) :
    HyperbolicVolumeBridge.vol m < HyperbolicVolumeBridge.vol n :=
  (vol_lt_iff_of_realises m n hm hn).mpr QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2

/-- **`VOL_5_2` is positive** — with no positivity statement about `BlochWigner_lob`
anywhere in the proof.

`Cl_2_pi_div_three_pos` bounds `VOL_4_1 = 2·Cl₂(π/3)` below; the chord inequality puts
`VOL_5_2` above it.  See the module header for why the direct route (a Clausen special
value, as at 4₁) is unavailable at this shape and remains so. -/
theorem VOL_5_2_pos : 0 < VOL_5_2 := by
  have h4 := QOU.Knot.Cl_2_pi_div_three_pos
  have hlt := QOU.Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2
  rw [QOU.Knot.FigureEightVolume.VOL_4_1] at hlt
  linarith

/-- **Positivity through the bridge — derived, not assumed.**

The 5₂ counterpart of `FigureEightVolumeBridge.vol_pos_of_realises`.  Its absence was
recorded in this file's header as an honest gap; the chord inequality closed it. -/
theorem vol_pos_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises fiveTwoTriangulation m) :
    0 < HyperbolicVolumeBridge.vol m := by
  rw [vol_eq_VOL_5_2_of_realises m h]
  exact VOL_5_2_pos

/-- **The 5₂ volume is not zero**, hence the triangulation is not degenerate — the
degenerate-model check applied to the value, matching the 4₁ file. -/
theorem vol_ne_zero_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises fiveTwoTriangulation m) :
    HyperbolicVolumeBridge.vol m ≠ 0 :=
  ne_of_gt (vol_pos_of_realises m h)

end QOU.Encounter.FiveTwoVolumeBridge
