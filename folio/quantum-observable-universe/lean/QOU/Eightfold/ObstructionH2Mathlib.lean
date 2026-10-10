import Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree
import QOU.Eightfold.ObstructionH2

/-!
# Agreement with Mathlib's `groupCohomology`

`ObstructionH2` defines `Z2`/`B2`/`H2` by transcribing Mathlib's `IsCocycle₂` /
`IsCoboundary₂` and specialising to the trivial action, because importing
`Mathlib.RepresentationTheory.Homological.GroupCohomology.LowDegree` needed 79 further
oleans the restored cache did not carry.  Those 79 are now built (`scripts/build-missing-mathlib-oleans.sh`, 79/79, no failures), so
the transcription is discharged here: the two objects are literally EQUAL, and nothing
downstream rests on "agrees by transcription" any more.

## What the proofs came to

Almost nothing, which is the good outcome — the definitions line up without translation.
`mem_cocycles₂_iff` reduces membership to
`f (g*h, j) + f (g, h) = A.ρ g (f (h, j)) + f (g, h*j)`, and
`Rep.ofDistribMulAction_ρ_apply_apply` rewrites `A.ρ g a` to `g • a`, which the trivial
action collapses to `a`.  That is the carrier of `Z2` verbatim, so the cocycle half closes
by `Iff.rfl`.  The coboundary half is the same fact one level down: `coboundaries₂` is the
range of `d₁₂`, which under a trivial `ρ` is `x g.2 - x (g.1 * g.2) + x g.1` — `B2`'s
existential, transposed between a pointwise statement and a `funext`.

Two things the elaborator required, neither mathematical:

* **`Γ : Type`, not `Type*`.**  `Rep k G` puts `k` and `G` in the same universe, and
  `ZMod 3` is in `Type 0`.  Harmless for the application — the fundamental group of a
  3-manifold is in `Type` — but it does mean these two lemmas are less general than the
  `ObstructionH2` results they connect, which stay universe-polymorphic.
* **`noncomputable`**, because `Rep.ofDistribMulAction` is.

Mathlib's bridges are stated for `Rep.ofDistribMulAction`, a representation induced from a
`DistribMulAction`, rather than for `Rep.trivial`.  That is the better fit here: `Z2` is
`IsCocycle₂` under a trivial action, so using the induced representation makes the two
sides definitionally the same object instead of merely isomorphic ones.
-/

namespace QOU.Eightfold.ObstructionH2

open groupCohomology

variable (Γ : Type) [Group Γ]

/-- The centre `μ₃` is fixed under conjugation, so `Γ` acts trivially on `ZMod 3`. -/
instance trivDMA : DistribMulAction Γ (ZMod 3) where
  smul _ a := a
  one_smul _ := rfl
  mul_smul _ _ _ := rfl
  smul_zero _ := rfl
  smul_add _ _ _ := rfl

instance : SMulCommClass Γ (ZMod 3) (ZMod 3) := ⟨fun _ _ _ => rfl⟩

@[simp] lemma trivDMA_smul (g : Γ) (a : ZMod 3) : g • a = a := rfl

/-- The representation the obstruction class actually lives in. -/
noncomputable abbrev triv3 : Rep (ZMod 3) Γ := Rep.ofDistribMulAction (ZMod 3) Γ (ZMod 3)

/-- **Our `Z2` is Mathlib's `cocycles₂`.** -/
theorem Z2_eq_cocycles₂ : Z2 Γ = cocycles₂ (triv3 Γ) := by
  ext f
  rw [mem_cocycles₂_iff]
  simp only [Rep.ofDistribMulAction_ρ_apply_apply, trivDMA_smul]
  exact Iff.rfl

/-- **Our `B2` is Mathlib's `coboundaries₂`.** -/
theorem B2_eq_coboundaries₂ : B2 Γ = coboundaries₂ (triv3 Γ) := by
  ext f
  constructor
  · rintro ⟨t, ht⟩
    exact ⟨t, funext fun g => by simpa using ht g.1 g.2⟩
  · rintro ⟨t, ht⟩
    exact ⟨t, fun g h => by simpa using congrFun ht (g, h)⟩

end QOU.Eightfold.ObstructionH2
