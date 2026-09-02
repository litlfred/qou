/-
  The figure-eight knot, through the volume bridge — EXACTLY, and with positivity.

  Bean `qou-hq3m` / `qou-8mtd`.

  ═══ WHY THIS FILE EXISTS: A CORRECTION TO ITS OWN SIBLING ═══

  `Encounter/MostowTriangulationBridge.lean` carries
  `figureEight_literal_eq_triangulation_volume`, whose conclusion is

      (2.02988321281930 : ℝ) = T.volume

  keyed on the decimal literal that `MostowRigidity.figureEight` supplies.  The
  theorem is true and correctly derived, and it is **unusable at the figure-eight**,
  which is the one place it was written for.

  The reason is that the literal is a **15-significant-digit truncation**.  The corpus
  records the exact value one file over, in `Knot/FigureEightVolume.lean`:

      VOL_4_1        := 2 · Cl₂(π/3)                        -- exact
      VOL_4_1_decimal := 2.029883212819307250042405108549   -- the approximation carrier

  and `MostowRigidity.figureEight.volume := 2.02988321281930`.  Those differ at the
  16th significant digit, so `volumeInvariant FigureEight ≠ VOL_4_1`.  Instantiating the
  sibling theorem at the corpus's own `figureEightTriangulation`, whose volume IS
  `VOL_4_1` by a sorry-free theorem, therefore forces a false conclusion — meaning its
  hypotheses are jointly unsatisfiable there and no correct bridge instance for
  `FigureEight` can ever discharge them.

  **This is the vacuity trap the sibling file itself documents, one file later.**  That
  file records catching a degenerate `Realises := fun _ _ => False` by writing the model
  out; the same discipline applied to the *numbers* rather than the relation catches
  this.  A theorem can be sound, derived, sorry-free, and still name hypotheses nothing
  can satisfy.

  ═══ WHAT THIS FILE DOES INSTEAD ═══

  Keys the figure-eight statement on the **exact** constant, so it applies:

  * `vol_eq_VOL_4_1_of_realises` — a manifold realised by the 4₁ triangulation has
    volume exactly `VOL_4_1`.  Composes the bridge's transport with the corpus's proved
    `figureEightTriangulation_volume`.
  * `vol_eq_two_clausen_of_realises` — the same, spelled out as `2 · Cl₂(π/3)`.
  * `vol_pos_of_realises` — **positivity**, which the bridge module left open.

  That last one is worth stating plainly.  `ManifoldVolumeBridge` declines to assume
  positivity as a class field, on the grounds that `0 < D(z)` on the upper half plane is
  not in the corpus and assuming it would be the dishonest move.  That reasoning was
  right in general and too pessimistic here: for **this** shape the corpus already
  proves `0 < Cl₂(π/3)` (`QOU.Knot.Cl_2_pi_div_three_pos`), so at the figure-eight
  positivity is *derived* rather than assumed.  The general case stays open.

  ═══ WHAT IS STILL NOT PROVED ═══

  That `figureEightTriangulation` is a triangulation of the complement `S³ ∖ 4₁`.  That
  is Thurston, it is not here, and it is why the bridge is still a hypothesis: the
  theorems below say "a manifold realised by *this triangulation*", not "the figure-eight
  knot complement".  The gap is the same one `qou-8mtd` names.

  Also not proved: that the Mostow literal differs from `VOL_4_1`.  That is a *numerical*
  observation (the digits above), not a Lean theorem — separating them needs a rigorous
  16-digit lower bound on `Cl₂(π/3)`, which the corpus does not have.  Recorded in
  `qou-hq3m` rather than asserted here.

  -- Ref: [thurston1978] Ch. 4 (the 4₁ complement as two regular ideal tetrahedra)
  -- Ref: [milnor1982] (the Lobachevsky/Clausen evaluation of the regular tetrahedron)
-/
import QOU.MathlibExt.ManifoldVolumeBridge
import QOU.Knot.FigureEightTriangulation
import QOU.Knot.Clausen

namespace QOU.Encounter.FigureEightVolumeBridge

open Real QOU.MathlibExt QOU.Knot.FigureEightTri

variable {M : Type*} [HyperbolicVolumeBridge M]

/-- **A manifold realised by the 4₁ triangulation has volume exactly `VOL_4_1`.**

Composes the bridge's transport with the corpus's sorry-free
`figureEightTriangulation_volume`. Keyed on the exact constant rather than on
`MostowRigidity.figureEight`'s truncated literal — see the module header for why the
literal version cannot be applied here. -/
theorem vol_eq_VOL_4_1_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises figureEightTriangulation m) :
    HyperbolicVolumeBridge.vol m = QOU.Knot.FigureEightVolume.VOL_4_1 := by
  rw [HyperbolicVolumeBridge.vol_eq_of_realises figureEightTriangulation m h,
    figureEightTriangulation_volume]

/-- The same, spelled out: two regular ideal tetrahedra, each contributing `Cl₂(π/3)`. -/
theorem vol_eq_two_clausen_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises figureEightTriangulation m) :
    HyperbolicVolumeBridge.vol m = 2 * QOU.Archimedean.Cl_2 (π / 3) :=
  vol_eq_VOL_4_1_of_realises m h

/-- **Positivity — derived, not assumed.**

`ManifoldVolumeBridge` deliberately declines to carry positivity as a class field,
because `0 < D(z)` on the upper half plane is not in the corpus. At the figure-eight it
does not need to be assumed: `Cl_2_pi_div_three_pos` supplies it. -/
theorem vol_pos_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises figureEightTriangulation m) :
    0 < HyperbolicVolumeBridge.vol m := by
  rw [vol_eq_two_clausen_of_realises m h]
  have := QOU.Knot.Cl_2_pi_div_three_pos
  linarith

/-- **The 4₁ volume is not zero**, hence the triangulation is not degenerate. A corollary
worth naming because a bridge whose `vol` collapsed to `0` would satisfy every transport
statement vacuously — the degenerate-model check, applied to the value rather than to the
relation. -/
theorem vol_ne_zero_of_realises (m : M)
    (h : HyperbolicVolumeBridge.Realises figureEightTriangulation m) :
    HyperbolicVolumeBridge.vol m ≠ 0 :=
  ne_of_gt (vol_pos_of_realises m h)

end QOU.Encounter.FigureEightVolumeBridge
