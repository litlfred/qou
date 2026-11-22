/-
  The triangulation-to-manifold volume bridge, stated as a CONDITIONAL, with no instance.

  Bean `qou-8mtd`.

  ═══ THE GAP THIS MAKES STATABLE, AND DOES NOT CLOSE ═══

  `QOU/MathlibExt/IdealTriangulation.lean` defines the volume **of a triangulation**:
  `IdealTetrahedron.volume = D(z)`, `IdealTriangulation.volume = Σᵢ D(zᵢ)`, with
  `volume_rotate` proving it independent of the edge labelling.  All of it sorry-free.

  What is undefined is **the volume of a topological 3-manifold**.  Nothing connects an
  `IdealTriangulation` to a knot complement, so the corpus can say "the volume of *this
  triangulation* is `3·D(y₁)`" and cannot say "`Vol(5₂) = 3·D(y₁)`" -- the left side has
  no referent.  `VOL_5_2` is *defined* as `3·D(y₁)`, which is a definition, not a
  computation of an invariant.

  ⚠ **The corpus DOES carry a second "volume of M", and it is not this one.**
  `QOU.Encounter.MostowRigidity` has a class field `volume : ℝ` with *instances* --
  `figureEight` sets it to the literal `2.02988321281930`, synced from a witness by
  `codemod-leanval.ts`.  So `volumeInvariant FigureEight = 2.0298…` holds by `rfl`.
  That is a manifold-side number, but an ENTERED one: nothing in that module mentions a
  triangulation, and no theorem there relates it to `Σ D(zᵢ)`.  Two carriers for one
  quantity is the collision the notation discipline warns about, so read this file as
  supplying the missing TRANSPORT rather than a third notion.
  `QOU.Encounter.MostowTriangulationBridge` spends it on exactly that, and is where the
  two are finally connected.

  Closing the gap needs a theory of hyperbolic 3-manifolds (Mathlib has none), Mostow
  rigidity for invariance, and Thurston hyperbolisation for the bridge itself.  **This
  file does none of that.**  What it does is make the dependence EXPLICIT: downstream
  statements can now carry the bridge as a named hypothesis in their type instead of
  being silently ambiguous about which volume they mean.

  ═══ WHY THIS IS NOT "AXIOMATISATION IS NOT A PROOF" ═══

  That rule forbids assuming a result and consuming it downstream as though discharged.
  Three things keep this on the right side of it, and they are the whole design:

  1. **NO INSTANCE IS PROVIDED, AND NONE SHOULD BE.**  A content-bearing class with no
     instance is the honest representation of an open problem (AGENTS.md §3b-tax).  Every
     theorem below is conditional on `[HyperbolicVolumeBridge M]`, visible in its type.
     Nothing here becomes unconditional by importing this file.

  2. **THE CLASS CARRIES HYPOTHESES, NOT THE CONCLUSION.**  §3b-cond item 5 rejects a
     class whose field *is* the downstream claim, with a "theorem" that projects it.  The
     transported equation `vol m = T.volume` is a genuine INPUT here -- it is Thurston's
     theorem, which nobody in this corpus has proved -- and the theorems below do not
     restate it.  They COMPOSE it: `vol_eq_of_two_realisations` applies it twice and
     cancels, and `vol_eq_rotateAt` composes it with the arc's own proved relabelling
     invariance.  Neither is `fun h => h.field`.

  3. **THE UNCONDITIONAL PART IS SEPARATED AND REAL.**  §1 below proves
     `volume_rotateAt` outright, with no class in sight: relabelling any single
     tetrahedron of a triangulation leaves the total volume unchanged.  That extends the
     one-tetrahedron `volume_rotate` to triangulations and is the well-definedness the
     bridge would need on the triangulation side.

  ═══ ⚠ A VACUITY TRAP THIS FILE WALKED INTO AND BACKED OUT OF ═══

  The obvious corollary to want is "a triangulation of flat tetrahedra has volume zero,
  so any manifold it realises has volume zero".  It is **unstatable**:
  `IdealTetrahedron` carries `im_pos : 0 < shape.im` in its very definition, so a flat
  tetrahedron is not an inhabitant and such a triangulation cannot be formed.  The
  theorem would have been vacuously true over an empty hypothesis -- exactly the shape
  the vacuity audit exists to catch.  Recorded because the statement reads perfectly well
  and only the structure's own field reveals the problem.

  ═══ THE CLASS WAS DEGENERATE ON ITS FIRST DRAFT, AND THE TEST IS WHY IT IS NOT NOW ═══

  As first written, this class had three fields and admitted the model

      vol := fun _ => 0,  Realises := fun _ _ => False

  on `Unit`.  Under it `vol_eq_of_realises` is vacuously true -- there is nothing to
  transport -- so the class asserted nothing about geometry and every theorem below held
  for a reason having nothing to do with hyperbolic volume.  That instance was written
  out and **typechecked**, which is the only reason this is stated as fact rather than
  suspected.

  It is exactly the defect the corpus already records one file over, where a two-valued
  `flatBirthday` satisfies all six SurrealField birthday axioms.  Both are the same
  lesson: an axiom set is only as strong as its models, and reading the axioms does not
  reveal which models they admit -- exhibiting one does.

  The `realisable` field closes it: the degenerate instance no longer elaborates.

  The second thing not proved here, for the same class of reason: **positivity**.
  `0 < vol m` for a realised manifold would follow from `0 < D(z)` on the upper half
  plane.  It is left open rather than assumed as a further class field, which would have
  been the easy and dishonest move.

  **BOTH HALVES ARE NOW PROVED, and the decision above still stands.**  This paragraph
  originally said `0 < D(z)` "*is not in the corpus*"; then, sharpened the same day, that
  only the strict half was open.  Both are now closed --
  `Archimedean.BlochWignerNonneg.blochWigner_lob_nonneg` (`0 ≤ D(z)`) and
  `Archimedean.BlochWignerPositive.blochWigner_lob_pos` (`0 < D(z)`, by Rivin strict
  concavity along an interior chord).

  **This is a vindication of the class design, not a reason to change it.**  Declining to
  assume positivity was right: it was derivable, so assuming it would have been assuming a
  theorem.  The class keeps its three fields, and the consequence lives outside it, in
  `MathlibExt/ManifoldVolumePositive.lean`:

      vol_pos_of_realises : 0 < n → Realises T m → 0 < vol m

  Note the `0 < n`.  It is not decoration -- `IdealTriangulation 0` is legitimate and its
  volume is the empty sum `0`, so a bridge whose `Realises` holds only of the empty
  triangulation genuinely has a zero-volume manifold.  That is the `realisable` field's
  degenerate model one level down.

  ═══ 2026-11-20 (bean `qou-dx7g`): THAT DEGENERATE MODEL WAS STILL ADMITTED ═══

  The axiom-field triage found `vol := fun _ => 0`, `Realises T _ := T.volume = 0`,
  realised by the empty triangulation, satisfying all four fields.  Two fields now
  constrain the triangulation side of `Realises`: `realises_nonempty` (no empty
  triangulation realises anything) and `realises_glued` (a realising triangulation
  solves the edge and angle gluing equations for a complete `n`-tetrahedron,
  `n`-edge pattern).  The degenerate model no longer satisfies the class, and
  `vol_pos_of_realises'` (in `ManifoldVolumePositive`) drops the `0 < n` hypothesis.
  **Residual:** `M` is still an arbitrary type, so which manifold a gluing solution
  triangulates is not modelled (no 3-manifold topology in Mathlib).  A constant
  `vol` on any `M`, realised by one genuine gluing solution, still satisfies the
  class; that is a statement about a real hyperbolic triangulation, not about a
  named knot complement.

  -- Ref: [thurston1978] Ch. 4 (hyperbolisation; the gluing-equation solution)
  -- Ref: [futer-gueritaud-angled] Def 2.4, Prop 2.5 (gluing equations give the hyperbolic metric); Thm 1.2 (complete structure = critical point of volume on angle structures) — held copy
  -- Ref: [neumann-zagier1985] §2 (the volume of a triangulation, and its invariance)
-/
import QOU.MathlibExt.IdealTriangulation

namespace QOU.MathlibExt

open scoped BigOperators

/-! ## §1 — Unconditional: relabelling a tetrahedron of a triangulation

No class, no hypothesis. This is the triangulation-level form of
`IdealTetrahedron.volume_rotate`, and it is what makes "the volume of a triangulation"
independent of how each tetrahedron happened to be labelled. -/

namespace IdealTriangulation

variable {n : ℕ}

/-- Relabel the `i`-th tetrahedron of a triangulation, leaving the others alone. -/
noncomputable def rotateAt (T : IdealTriangulation n) (i : Fin n) :
    IdealTriangulation n :=
  ⟨Function.update T.tet i (T.tet i).rotate⟩

@[simp] theorem rotateAt_tet_self (T : IdealTriangulation n) (i : Fin n) :
    (T.rotateAt i).tet i = (T.tet i).rotate := by
  simp [rotateAt]

@[simp] theorem rotateAt_tet_of_ne (T : IdealTriangulation n) {i j : Fin n} (h : j ≠ i) :
    (T.rotateAt i).tet j = T.tet j := by
  simp [rotateAt, Function.update_of_ne h]

/-- **Relabelling one tetrahedron does not change the triangulation's volume.**

The sum differs in exactly one summand, and that summand is unchanged by
`IdealTetrahedron.volume_rotate`. -/
@[simp] theorem volume_rotateAt (T : IdealTriangulation n) (i : Fin n) :
    (T.rotateAt i).volume = T.volume := by
  classical
  simp only [volume]
  refine Finset.sum_congr rfl ?_
  intro j _
  by_cases h : j = i
  · subst h; simp
  · simp [rotateAt_tet_of_ne T h]

end IdealTriangulation

/-! ## §2 — The bridge, as a hypothesis

`HyperbolicVolumeBridge M` says: the type `M` has a real-valued volume, there is a
notion of a triangulation *realising* an element of `M`, and a realising triangulation
computes that volume.

The third field is **Thurston's theorem**, not something proved here. That is exactly
why this is a class with no instance rather than a definition. -/

/-- The triangulation-to-manifold volume bridge, carried as an explicit hypothesis.

**No instance is provided, and providing one would be a defect** unless it came with an
actual theory of hyperbolic 3-manifolds. The point of the class is to make every
downstream statement wear its dependence in its type. -/
class HyperbolicVolumeBridge (M : Type*) where
  /-- The volume of an element of `M`. Undefined in this corpus; supplied by the
  hypothesis. -/
  vol : M → ℝ
  /-- `Realises T m` : the ideal triangulation `T` realises the structure on `m`.
  Thurston's hyperbolisation is what would produce inhabitants of this. -/
  Realises : {n : ℕ} → IdealTriangulation n → M → Prop
  /-- **The bridge.** A realising triangulation computes the volume. This is the
  hypothesis; the theorems below compose it rather than restate it. -/
  vol_eq_of_realises :
    ∀ {n : ℕ} (T : IdealTriangulation n) (m : M), Realises T m → vol m = T.volume
  /-- **Non-triviality, and it is load-bearing.**  Without it the class admits the
  degenerate model `Realises := fun _ _ => False`, under which `vol_eq_of_realises`
  holds vacuously and the class asserts nothing about geometry -- the same failure the
  corpus records for the birthday axioms, where a two-valued function satisfies all six.
  That model was CONSTRUCTED and typechecked before this field was added; with the field
  it no longer elaborates.  A carrier must assert something (AGENTS.md §3b-tax). -/
  realisable : ∃ (n : ℕ) (T : IdealTriangulation n) (m : M), Realises T m
  /-- **A realising triangulation is nonempty** (bean `qou-dx7g`).  The triage of
  2026-11-20 found that `realisable` alone still admits a degenerate model:
  `vol := fun _ => 0` with `Realises T _ := T.volume = 0`, realised by the empty
  triangulation `IdealTriangulation 0` (empty sum).  A cusped hyperbolic 3-manifold
  has no ideal triangulation by zero tetrahedra, so this is part of what "`T`
  realises `m`" means, not an extra assumption about the geometry. -/
  realises_nonempty :
    ∀ {n : ℕ} (T : IdealTriangulation n) (m : M), Realises T m → 0 < n
  /-- **A realising triangulation solves Thurston's gluing equations** (bean
  `qou-dx7g`).  For an ideal triangulation of a cusped 3-manifold by `n`
  tetrahedra there are exactly `n` edge classes (Euler characteristic), each of the
  three opposite edge-pairs of each tetrahedron meets the edge classes exactly twice
  in total, and the shapes satisfy both the edge equations (product form) and the
  angle (Casson–Rivin) equations.  This is the data Thurston's hyperbolisation
  produces [thurston1978, Ch. 4], [neumann-zagier1985, §2]; without it `Realises`
  could hold of shapes that glue to nothing.

  **What it still does not pin.**  `M` is an arbitrary type, so nothing here says
  *which* manifold a solution of the gluing equations triangulates: that is
  topology, which Mathlib does not model.  The field constrains the triangulation
  side of `Realises`, not the manifold side. -/
  realises_glued :
    ∀ {n : ℕ} (T : IdealTriangulation n) (m : M), Realises T m →
      ∃ G : GluingData n n,
        (∀ (i : Fin n) (j : Fin 3), (∑ k, G.exp k i j) = 2) ∧
        SatisfiesEdgeEquations T G ∧ SatisfiesAngleEquations T G

namespace HyperbolicVolumeBridge

variable {M : Type*} [HyperbolicVolumeBridge M] {n k : ℕ}

/-- **Any two realising triangulations have the same volume.**

Derived, not projected: the bridge is applied to each triangulation and the two
equations are composed. This is the statement that would make "the volume of the
manifold" well defined, and it is the first thing one would want from the bridge. -/
theorem vol_eq_of_two_realisations
    (T₁ : IdealTriangulation n) (T₂ : IdealTriangulation k) (m : M)
    (h₁ : Realises T₁ m) (h₂ : Realises T₂ m) :
    T₁.volume = T₂.volume := by
  rw [← vol_eq_of_realises T₁ m h₁, ← vol_eq_of_realises T₂ m h₂]

/-- **The bridge is compatible with the arc's proved relabelling invariance.**

Composes the hypothesis with the unconditional `volume_rotateAt` of §1: if `T` realises
`m`, then the relabelled triangulation computes the same number. A consistency check on
the hypothesis rather than a consequence of the geometry — but it is derived, and it
would fail if the two halves disagreed. -/
theorem vol_eq_rotateAt (T : IdealTriangulation n) (m : M) (i : Fin n)
    (h : Realises T m) :
    vol m = (T.rotateAt i).volume := by
  rw [vol_eq_of_realises T m h, IdealTriangulation.volume_rotateAt]

/-- The volume of a realised element, written out as the sum of Bloch–Wigner values of
the shapes. Composes the bridge with `volume_def`. -/
theorem vol_eq_sum_of_realises (T : IdealTriangulation n) (m : M) (h : Realises T m) :
    vol m = ∑ i, (T.tet i).volume := by
  rw [vol_eq_of_realises T m h, IdealTriangulation.volume_def]

end HyperbolicVolumeBridge

end QOU.MathlibExt
