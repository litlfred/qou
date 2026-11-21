/-
  `0 ≤ D(z)` on the upper half plane — the general statement, at last.

  Beans `qou-f8lit` (item 3) and `qou-52ch`.

  ═══ WHY THIS FILE EXISTS, AND WHY IT IS SIX LINES ═══

  `Encounter/FiveTwoVolumeBridge.lean` and `MathlibExt/ManifoldVolumeBridge.lean` both
  record that the corpus carries **no** positivity for `BlochWigner_lob` on the upper half
  plane, and `ManifoldVolumeBridge` deliberately declines to assume it as a class field.
  That was measured and true.

  It stopped being true when `Archimedean/LobMonotonicity.lean` landed
  (`lob_sum_nonneg` — three positive angles summing to `π` give a nonnegative `Λ`-sum,
  by concavity and subadditivity on `[0, π/2]`).  Nothing else was needed: the corpus
  already had every other piece, in `MathlibExt/IdealTriangulation.lean`.

      T.volume       = BlochWigner_lob T.shape                      (definition)
      volume_eq_lob_sum : T.volume = Λ a₁ + Λ a₂ + Λ a₃             (Milnor, `rfl`)
      angle_sum         : a₁ + a₂ + a₃ = π
      angleᵢ_mem        : 0 < aᵢ ∧ aᵢ < π

  So `lob_sum_nonneg` applies directly, and every `z` with `0 < z.im` is the shape of an
  `IdealTetrahedron` by construction.  The gap was never in the geometry — it was that
  the Λ-sum lemma had not been written.

  ═══ NONNEGATIVE, NOT STRICTLY POSITIVE — AND THE REASON GIVEN HERE WAS WRONG ═══

  This proves `0 ≤ D(z)`.  The **strict** `0 < D(z)` is a separate statement and lives in
  `Archimedean/BlochWignerPositive.lean` (bean `qou-0ag0`), which landed within the hour.

  This paragraph originally read: *"Ruling that out needs the angles bounded away from the
  corners, or a strict form of the subadditivity — neither of which is here."*  **Neither
  is what the strict proof uses.**  It runs Rivin strict concavity along a horizontal
  chord whose two endpoints stay strictly interior, and bounds those endpoints below with
  `lob_sum_nonneg` — this file's own lemma, in its existing non-strict form.  The
  strictness comes from the concavity, not from any strengthening of the subadditivity and
  not from any bound on the angles.

  The observation that survives is the narrow one: `lob_sum_nonneg` alone cannot give
  strictness, because subadditivity is not strict and the Λ-sum really does tend to `0` as
  the tetrahedron degenerates.  That says this file does not extend to the strict case; it
  says nothing about whether some other argument does, and one does.  Recorded because
  naming an obstacle to a result is a claim about the problem, and this one was a claim
  about the route.

  -- Ref: [milnor1982] §2
  -- Ref: [neumann-zagier1985] §2
-/
import QOU.MathlibExt.IdealTriangulation
import QOU.Archimedean.LobMonotonicity

namespace QOU.Archimedean.BlochWignerNonneg

open QOU.Archimedean QOU.MathlibExt

/-- **An ideal tetrahedron has nonnegative volume.**

Milnor's formula plus the fact that the three dihedral angles are positive and sum to
`π`, which is exactly the hypothesis of `lob_sum_nonneg`. -/
theorem volume_nonneg (T : IdealTetrahedron) : 0 ≤ T.volume := by
  rw [T.volume_eq_lob_sum]
  exact LobMonotonicity.lob_sum_nonneg
    T.angle₁_mem.1 T.angle₂_mem.1 T.angle₃_mem.1 T.angle_sum

/-- **`0 ≤ D(z)` for every `z` in the upper half plane.**

The general nonnegativity that `ManifoldVolumeBridge` declined to assume as a class
field.  Note this is the **non-strict** statement — see the module header for why
strictness does not follow from the same argument. -/
theorem blochWigner_lob_nonneg {z : ℂ} (hz : 0 < z.im) : 0 ≤ BlochWigner_lob z :=
  volume_nonneg (.ofIm z hz)

end QOU.Archimedean.BlochWignerNonneg
