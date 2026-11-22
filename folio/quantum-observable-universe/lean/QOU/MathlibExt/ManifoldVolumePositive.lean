/-
  `0 < vol m` for a realised manifold — the field `HyperbolicVolumeBridge` declined to
  assume, now DERIVED.

  Bean `qou-0ag0`; the payoff of `Archimedean/BlochWignerPositive.lean`.

  ═══ WHAT THIS SETTLES ═══

  `MathlibExt/ManifoldVolumeBridge.lean` records positivity as the second thing it does not
  prove, and deliberately does not carry it as a class field:

      "So it is left open rather than assumed as a further class field, which would have
       been the easy and dishonest move."

  That judgement is vindicated rather than overturned.  The class was right not to assume
  it, and the corpus can now prove it: `BlochWignerPositive.volume_pos` gives every ideal
  tetrahedron a strictly positive volume, a triangulation's volume is the sum over its
  tetrahedra, and the bridge transports that to the manifold.

  ═══ THE NONEMPTINESS HYPOTHESIS IS REAL, NOT DECORATION ═══

  `0 < n` cannot be dropped.  `IdealTriangulation 0` is a legitimate inhabitant — an empty
  family `Fin 0 → IdealTetrahedron` — and its volume is the empty sum, `0`.  So a bridge
  instance admitting an empty realising triangulation genuinely has a manifold of volume
  zero, and no strengthening of the tetrahedron result can rule that out.  This is the same
  species of degenerate model the class's own `realisable` field exists to exclude, one
  level down: there the danger was `Realises := fun _ _ => False`, here it is `Realises`
  holding only of the empty triangulation.

  -- Ref: [thurston1978] Ch. 4
  -- Ref: [futer-gueritaud-angled] Def 2.4, Prop 2.5 (gluing equations give the hyperbolic metric); Thm 1.2 (complete structure = critical point of volume on angle structures) — held copy
  -- Ref: [neumann-zagier1985] §2
-/
import QOU.Archimedean.BlochWignerPositive
import QOU.MathlibExt.ManifoldVolumeBridge

namespace QOU.MathlibExt.ManifoldVolumePositive

open QOU.MathlibExt QOU.Archimedean

/-- **A nonempty ideal triangulation has strictly positive volume.**

Each tetrahedron contributes strictly positively (`BlochWignerPositive.volume_pos`), and
`0 < n` makes the index set nonempty — without which the sum is empty and the volume is
`0`. -/
theorem triangulation_volume_pos {n : ℕ} (hn : 0 < n) (T : IdealTriangulation n) :
    0 < T.volume := by
  rw [IdealTriangulation.volume_def]
  have : Nonempty (Fin n) := ⟨⟨0, hn⟩⟩
  exact Finset.sum_pos (fun i _ => BlochWignerPositive.volume_pos (T.tet i))
    Finset.univ_nonempty

/-- **A manifold realised by a nonempty ideal triangulation has strictly positive
volume.**

The general form of `Encounter.FigureEightVolumeBridge.vol_pos_of_realises` and
`Encounter.FiveTwoVolumeBridge.vol_pos_of_realises`, which reached the same conclusion at
their own two shapes through a Clausen special value and through a volume comparison
respectively.  Neither route generalised; this one does not need either. -/
theorem vol_pos_of_realises {M : Type*} [HyperbolicVolumeBridge M] {n : ℕ} (hn : 0 < n)
    (T : IdealTriangulation n) (m : M) (h : HyperbolicVolumeBridge.Realises T m) :
    0 < HyperbolicVolumeBridge.vol m := by
  rw [HyperbolicVolumeBridge.vol_eq_of_realises T m h]
  exact triangulation_volume_pos hn T

/-- **The volume of such a manifold is nonzero**, hence the realisation is not
degenerate. -/
theorem vol_ne_zero_of_realises {M : Type*} [HyperbolicVolumeBridge M] {n : ℕ} (hn : 0 < n)
    (T : IdealTriangulation n) (m : M) (h : HyperbolicVolumeBridge.Realises T m) :
    HyperbolicVolumeBridge.vol m ≠ 0 :=
  ne_of_gt (vol_pos_of_realises hn T m h)

/-- **Every realised manifold has strictly positive volume** — the `0 < n` hypothesis
of `vol_pos_of_realises` is now discharged by the bridge's own `realises_nonempty`
field (bean `qou-dx7g`), which excludes the empty-triangulation model that made it
necessary. -/
theorem vol_pos_of_realises' {M : Type*} [HyperbolicVolumeBridge M] {n : ℕ}
    (T : IdealTriangulation n) (m : M) (h : HyperbolicVolumeBridge.Realises T m) :
    0 < HyperbolicVolumeBridge.vol m :=
  vol_pos_of_realises (HyperbolicVolumeBridge.realises_nonempty T m h) T m h

end QOU.MathlibExt.ManifoldVolumePositive
