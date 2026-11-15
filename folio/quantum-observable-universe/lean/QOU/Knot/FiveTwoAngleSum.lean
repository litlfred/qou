/-
  `VOL_5_2` in ANGLE form: three times a Λ-sum over the 5₂ tetrahedron's
  dihedral angles.

  WHY.  `qou-52ch` bounds `VOL_5_2` below by a chord under Rivin concavity, and
  concavity is stated for the ANGLE functional `Λ(α)+Λ(β)+Λ(γ)`
  (`QOU.Knot.Rivin.strictConcaveOn_tetVolLine`), whereas `VOL_5_2` is defined
  through Bloch–Wigner as `3·D(y₁)`.  This is the translation between them.

  It is three lines because the corpus already had both halves — `fiveTwoTet`
  and `IdealTetrahedron.volume_eq_lob_sum` (`rfl`).  Recorded as its own lemma
  anyway: the chord argument consumes exactly this shape, and re-deriving it
  inline at the use site is how a `rfl`-chain gets copied rather than cited.

  WHAT THIS IS NOT.  Per the `IdealTriangulation` header, `volume` there is
  DEFINED as the Bloch–Wigner value; that it is an ideal tetrahedron's
  hyperbolic volume is `qou-idvt` T2, still open.  So this says "`VOL_5_2` is
  three times a Λ-sum", and nothing about a manifold.

  Archimedean (ℝ): `arg`, `Λ` — §7c.

  -- Ref: [neumann-zagier1985] Volumes of hyperbolic three-manifolds
  -- Ref: [leitner2026] bean qou-52ch
-/

import QOU.Knot.FiveTwoVolumeConstant

namespace QOU.Knot.FiveTwoVolume

open Real QOU.Archimedean

/-- The 5₂ tetrahedron's three dihedral angles sum to `π` — one of the two
hypotheses Rivin concavity takes. -/
theorem fiveTwoTet_angle_sum :
    fiveTwoTet.angle₁ + fiveTwoTet.angle₂ + fiveTwoTet.angle₃ = π :=
  fiveTwoTet.angle_sum

theorem fiveTwoTet_angle₁_pos : 0 < fiveTwoTet.angle₁ := fiveTwoTet.angle₁_mem.1
theorem fiveTwoTet_angle₂_pos : 0 < fiveTwoTet.angle₂ := fiveTwoTet.angle₂_mem.1
theorem fiveTwoTet_angle₃_pos : 0 < fiveTwoTet.angle₃ := fiveTwoTet.angle₃_mem.1

/-- **`VOL_5_2` is three times the Λ-sum over the 5₂ dihedral angles.**

This is what lets a bound proved for the angle functional — Rivin concavity, and
the `qou-52ch` chord — be read as a bound on `VOL_5_2`. -/
theorem VOL_5_2_eq_three_mul_lob_sum :
    VOL_5_2 = 3 * (Lob fiveTwoTet.angle₁ + Lob fiveTwoTet.angle₂
      + Lob fiveTwoTet.angle₃) := by
  rw [← fiveTwoTet.volume_eq_lob_sum]
  rfl

end QOU.Knot.FiveTwoVolume
