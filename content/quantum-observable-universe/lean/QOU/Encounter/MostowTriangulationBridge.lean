/-
  Connecting the corpus's TWO "volume of M" notions.

  Bean `qou-8mtd`, second half of its title: "and connect it to the triangulation
  volume".

  ═══ WHY THIS FILE EXISTS: THE CORPUS HAD TWO, AND THEY DID NOT TOUCH ═══

  Before this file the corpus carried two unrelated notions of the volume of a
  3-manifold, in different namespaces, with no theorem relating them:

  1. `QOU.Encounter.MostowRigidity.volume : ℝ` — one real per type-marker, supplied
     by an *instance*.  `figureEight` sets it to the decimal literal
     `2.02988321281930`, kept in sync with `hyperbolic-volumes.witness.json` by
     `codemod-leanval.ts`.  So `volumeInvariant FigureEight = 2.0298…` holds by
     `rfl`: the number is ENTERED, not computed.  Nothing in that module mentions a
     triangulation.

  2. `QOU.MathlibExt.IdealTriangulation.volume = Σᵢ D(zᵢ)` — genuinely computed from
     the shapes, sorry-free, and proved invariant under relabelling.

  Two carriers for one quantity, unconnected, is the collision the notation
  discipline warns about: whichever a downstream reader picks, nothing tells them
  the other exists.  `HyperbolicVolumeBridge` (added in the same PR as this file)
  supplies the missing transport; this file spends it on notion 1.

  ═══ WHAT IS PROVED, AND WHAT IS STILL ASSUMED ═══

  `mostow_volume_eq_triangulation_volume` says: **under the bridge, and given that
  the two notions agree at all, the Mostow invariant equals the triangulation sum.**
  It is derived by composing three separate inputs — the compatibility hypothesis,
  the bridge's transport, and the definition of `volumeInvariant` — and is not a
  projection of any one of them (AGENTS.md §3b-cond item 5).

  What it does NOT do is prove that the entered literal is right.  `compat` is an
  explicit hypothesis, deliberately NOT a class field: making it a field would let
  it travel implicitly and read as established.  As an argument it must be supplied,
  by name, at every use site.

  ═══ THE VACUITY QUESTION, WHICH IS NOT THE SAME AS THE ONE NEXT DOOR ═══

  `ManifoldVolumeBridge.lean` records a corollary it could not state because
  `IdealTetrahedron.im_pos` makes the hypothesis PROVABLY uninhabited.  The
  hypotheses here are a different case and the distinction is the whole point:
  `HyperbolicVolumeBridge M` is OPEN — no instance exists and none is provided, but
  nothing proves none can exist.  A conditional theorem over an open hypothesis is
  the §3b-cond pattern working as intended; a theorem over a refutable one is
  vacuous.  Same shape on the page, opposite epistemic status.

  -- Ref: [mostow1968] (rigidity: the volume is a topological invariant)
  -- Ref: [thurston1978] Ch. 4 (the gluing-equation solution the bridge would need)
-/
import QOU.Encounter.MostowRigidity
import QOU.MathlibExt.ManifoldVolumeBridge

namespace QOU.Encounter.MostowTriangulationBridge

open QOU.MathlibExt QOU.Encounter.MostowRigidity

variable {M : Type*} {n : ℕ}

/-- **The Mostow volume invariant equals the triangulation sum, under the bridge.**

Composes three inputs: `compat` (the two notions agree), the bridge's transport
`vol_eq_of_realises`, and the definition of `volumeInvariant`. None of them alone
gives the conclusion.

`compat` is an explicit argument rather than a class field on purpose — a field
would be inferred silently at every use site and would read as established. -/
theorem mostow_volume_eq_triangulation_volume
    [HyperbolicVolumeBridge M] [MR : MostowRigidity M]
    (compat : ∀ m : M, HyperbolicVolumeBridge.vol m = MR.volume)
    (T : IdealTriangulation n) (m : M)
    (h : HyperbolicVolumeBridge.Realises T m) :
    volumeInvariant M = T.volume := by
  show MR.volume = T.volume
  rw [← compat m]
  exact HyperbolicVolumeBridge.vol_eq_of_realises T m h

/-- **The entered literal, pinned to a computed sum.**

⚠ **CORRECTED — this theorem cannot be applied at the actual figure-eight.**  The
literal below is a 15-significant-digit *truncation*; the corpus's exact value is
`VOL_4_1 = 2·Cl₂(π/3) = 2.029883212819307250011597804990…`, and the two differ at the
16th digit.  So instantiating this at `QOU.Knot.FigureEightTri.figureEightTriangulation`,
whose volume is `VOL_4_1` by a sorry-free theorem, forces a false conclusion — its
hypotheses are jointly unsatisfiable there.  The statement is sound and derived; it is
simply unusable at the one knot it names.  Use
`QOU.Encounter.FigureEightVolumeBridge.vol_eq_VOL_4_1_of_realises`, which is keyed on the
exact constant.  Kept here rather than deleted because the defect is instructive: a
theorem can be sorry-free and still name hypotheses nothing satisfies (bean `qou-hq3m`).

`figureEight` sets `volume := 2.02988321281930` as a decimal literal. Under the
bridge, that literal is not free: it is the Bloch–Wigner sum of any triangulation
realising the complement.

This is what the bridge buys. It does not verify the literal — `compat` is still
assumed — but it converts "a number was entered here" into "this number is the
value of a computed quantity, given the bridge", which is a statement the corpus
could not previously make at all. -/
theorem figureEight_literal_eq_triangulation_volume
    [HyperbolicVolumeBridge FigureEight]
    (compat : ∀ m : FigureEight,
      HyperbolicVolumeBridge.vol m = (figureEight).volume)
    (T : IdealTriangulation n) (m : FigureEight)
    (h : HyperbolicVolumeBridge.Realises T m) :
    (2.02988321281930 : ℝ) = T.volume :=
  mostow_volume_eq_triangulation_volume compat T m h

/-- **Any two triangulations realising a Mostow-rigid manifold agree with its
invariant.**

The well-definedness statement in the form the Mostow module can consume: it is
the invariant, not merely some real, that both sums compute. -/
theorem volumeInvariant_eq_of_two_realisations
    [HyperbolicVolumeBridge M] [MR : MostowRigidity M] {k : ℕ}
    (compat : ∀ m : M, HyperbolicVolumeBridge.vol m = MR.volume)
    (T₁ : IdealTriangulation n) (T₂ : IdealTriangulation k) (m : M)
    (h₁ : HyperbolicVolumeBridge.Realises T₁ m)
    (h₂ : HyperbolicVolumeBridge.Realises T₂ m) :
    volumeInvariant M = T₁.volume ∧ T₁.volume = T₂.volume :=
  ⟨mostow_volume_eq_triangulation_volume compat T₁ m h₁,
   HyperbolicVolumeBridge.vol_eq_of_two_realisations T₁ T₂ m h₁ h₂⟩

end QOU.Encounter.MostowTriangulationBridge
