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

  ═══ NONNEGATIVE, NOT STRICTLY POSITIVE ═══

  This proves `0 ≤ D(z)`, which is **weaker than what the two bridge files say is
  missing**: they name `0 < BlochWigner_lob z`.  Do not read this file as closing that.

  Strictness is genuinely a further step, and the reason is visible in the shape of the
  argument above: `lob_sum_nonneg` descends from *subadditivity* of `Λ` on `[0, π/2]`,
  which is not strict, and the Λ-sum really does tend to `0` as the tetrahedron
  degenerates.  Ruling that out needs the angles bounded away from the corners, or a
  strict form of the subadditivity — neither of which is here.  What the corpus does
  carry, for the specific shapes it cares about, is a *comparison*: at 5₂, positivity
  comes from `Knot.FiveTwoVolumeChord.VOL_4_1_lt_VOL_5_2` against `Cl_2_pi_div_three_pos`
  (see `Encounter/FiveTwoVolumeBridge.VOL_5_2_pos`), not from this file.

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
  volume_nonneg ⟨z, hz⟩

end QOU.Archimedean.BlochWignerNonneg
