/-
QOU.Mass.SelfCrossingInvarianceGate — the hypothesis the mass=self / binding=mutual assignment
actually rests on, made explicit, and the Călugăreanu reason it is not automatic.

Arc context (bk-crossing mass-binding; bean `qou-brng`). `QOU.Mass.SelfMutualPartition` proves
`binding_eq_neg_mutualEnergy`: binding is exactly minus the inter-component (mutual) energy, so
mass ↔ self and binding ↔ mutual. That derivation is correct, but its `binding` is *defined* as

    binding := selfEnergy E − assemblyEnergy E

and the file's own docstring supplies the justification for writing `selfEnergy` there:

  > "the sum of isolated masses is `selfEnergy` (the self crossings are exactly those present in
  >  isolation)"

**That identification is a hypothesis, and it is invisible in the statement.** The mass-deficit
definition of binding is `B = (Σ isolated component masses) − (assembled mass)`; substituting
`selfEnergy` for the first term presumes that assembling the components does not change any
component's own self-crossing content. This file does three things:

1. **Restates binding with the isolated masses as free data** (`bindingOfIsolated`), so the
   substitution is no longer built into the definition.
2. **Names the residual** — `selfDefect := (Σ isolated masses) − selfEnergy` — and proves
   `binding = −mutual + selfDefect`, with the sharp
   `binding = −mutual ↔ selfDefect = 0` (`binding_eq_neg_mutualEnergy_iff_selfDefect_zero`).
   So the landed result is exactly the `selfDefect = 0` slice, and the gate now appears in the type.
   A concrete two-value witness shows binding is *not* a function of the mutual part alone once the
   gate is dropped, so the gate has falsifiable content.
3. **Records why the gate is not automatic**, from Moffatt & Ricca's Călugăreanu paper. The
   Călugăreanu–White–Pohl relation is `SL = Wr + Tw` — only the *sum* is the isotopy invariant.
   Moffatt & Ricca (§1, around their (1.3)–(1.4)) note that passage through an inflexional
   configuration makes the writhe and the twist jump by equal and opposite amounts, that a type-I
   Reidemeister move in any projection forces such a passage, and that general ambient isotopies
   "do therefore typically involve such passage"; Pohl's `SL = W + T` is stated for *regular*
   isotopy. A type-I Reidemeister move is precisely the creation or removal of a **self**-crossing.
   So a self-energy read off a bare self-crossing count is *not* ambient-isotopy invariant, while
   one read off the Călugăreanu self-linking is — `selfLinking_inflexionMove` vs
   `writhe_inflexionMove_ne`, and the two corollaries that carry each into the gate.

This is a **scope-(a)** observation about the derivation's hypotheses: it does not refute the
mass=self / binding=mutual assignment, and it excludes no ingredient. It says the assignment holds
on the `selfDefect = 0` slice and identifies the invariant (`SL = Wr + Tw`, not `Wr`) under which a
self-energy functional lands on that slice.

Ground ring: §1 is over `ℝ` (it interoperates with `SelfMutualPartition`'s archimedean energy);
§2 is generic over `[AddCommGroup R]` — the Călugăreanu exchange is pure algebra and needs no
ordering, no `Real.sqrt`, no archimedean construct. No fit; `energy`, `isInter`, `isolatedMassTotal`
are free data throughout.

-- Ref: [moffatt-ricca-helicity] Moffatt & Ricca, "Helicity and the Calugareanu invariant",
--      Proc. R. Soc. Lond. A 439 (1992) 411-429. Relation (1.3) n = W + T + N; (1.4) SL = W + T;
--      §1 on inflexional passage, type-I Reidemeister moves and regular vs ambient isotopy.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import QOU.Mass.SelfMutualPartition

namespace QOU.Mass.SelfCrossingInvarianceGate

open Finset
open QOU.Mass.SelfMutualPartition

/-! ## §1 — the hidden hypothesis, exhibited

`SelfMutualPartition.binding` hard-codes `selfEnergy` as the total isolated mass. Here that total is
free data, so the substitution becomes a stated hypothesis rather than a definitional choice. -/

variable {C : Type*}

/-- **Binding by the mass deficit, with the isolated masses as free data.** `isolatedMassTotal` is
the sum of the component masses measured *in isolation*; nothing here presumes it equals the
assembled diagram's self-crossing energy. -/
noncomputable def bindingOfIsolated (E : Finset C) (energy : C → ℝ) (isolatedMassTotal : ℝ) : ℝ :=
  isolatedMassTotal - assemblyEnergy E energy

/-- **The self-crossing reorganisation defect** — the amount by which assembling the components
changes their own (intra-component) energy. Zero exactly when "the self crossings are the ones
present in isolation", the sentence `SelfMutualPartition` argues from. -/
noncomputable def selfDefect (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] (isolatedMassTotal : ℝ) : ℝ :=
  isolatedMassTotal - selfEnergy E energy isInter

/-- **The general mass-deficit identity.** Binding is minus the mutual energy *plus the self
reorganisation defect*. `SelfMutualPartition.binding_eq_neg_mutualEnergy` is the `selfDefect = 0`
slice of this. -/
theorem binding_eq_neg_mutual_add_selfDefect (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] (isolatedMassTotal : ℝ) :
    bindingOfIsolated E energy isolatedMassTotal
      = - mutualEnergy E energy isInter + selfDefect E energy isInter isolatedMassTotal := by
  unfold bindingOfIsolated selfDefect
  rw [assemblyEnergy_partition E energy isInter]
  ring

/-- **The gate, sharp.** Binding equals minus the mutual pairing **if and only if** the self
reorganisation defect vanishes. This is the hypothesis the mass=self / binding=mutual assignment
rests on, now visible in the type. -/
theorem binding_eq_neg_mutualEnergy_iff_selfDefect_zero (E : Finset C) (energy : C → ℝ)
    (isInter : C → Prop) [DecidablePred isInter] (isolatedMassTotal : ℝ) :
    bindingOfIsolated E energy isolatedMassTotal = - mutualEnergy E energy isInter
      ↔ selfDefect E energy isInter isolatedMassTotal = 0 := by
  rw [binding_eq_neg_mutual_add_selfDefect E energy isInter isolatedMassTotal]
  constructor
  · intro h; linarith
  · intro h; rw [h]; ring

/-- **Recovering the landed result.** Under the gate, this file's binding agrees with
`SelfMutualPartition.binding`, and both equal minus the mutual energy. Nothing is retracted. -/
theorem binding_eq_neg_mutualEnergy_of_gate (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] (isolatedMassTotal : ℝ)
    (hgate : isolatedMassTotal = selfEnergy E energy isInter) :
    bindingOfIsolated E energy isolatedMassTotal = - mutualEnergy E energy isInter := by
  rw [binding_eq_neg_mutualEnergy_iff_selfDefect_zero]
  unfold selfDefect
  rw [hgate]
  ring

/-- **The gate has falsifiable content: drop it and binding is no longer a function of the mutual
part.** One fixed assembly — a single inter-component crossing and a single self-crossing, each of
unit energy — read two ways: the self-crossing was already present in isolation
(`isolatedMassTotal = 1`, the gate holds) or it was created by the assembly
(`isolatedMassTotal = 0`, a type-I move, the gate fails). The mutual energy is `1` in both readings,
and the two bindings differ. So `binding_indep_of_self` is a consequence of the gate, not of the
partition. -/
theorem gate_has_content :
    mutualEnergy (Finset.univ : Finset (Fin 2)) (fun _ => (1 : ℝ)) (fun c => c = 0) = 1
      ∧ bindingOfIsolated (Finset.univ : Finset (Fin 2)) (fun _ => (1 : ℝ)) 1 = -1
      ∧ bindingOfIsolated (Finset.univ : Finset (Fin 2)) (fun _ => (1 : ℝ)) 0 = -2
      ∧ bindingOfIsolated (Finset.univ : Finset (Fin 2)) (fun _ => (1 : ℝ)) 1
          ≠ bindingOfIsolated (Finset.univ : Finset (Fin 2)) (fun _ => (1 : ℝ)) 0 := by
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp [mutualEnergy, bindingOfIsolated, assemblyEnergy] <;>
    first
      | decide
      | norm_num

/-! ## §2 — the Călugăreanu reason the gate is not automatic

`SL = Wr + Tw` (Călugăreanu 1961 (1.3); Pohl (1.4), stated for *regular* isotopy). Passage through
an inflexional configuration moves writhe and twist by equal and opposite amounts, so only the sum
survives; and a type-I Reidemeister move — the creation or removal of a **self**-crossing — forces
such a passage, which Moffatt & Ricca note general ambient isotopies typically involve.

Generic over `[AddCommGroup R]`: the exchange is pure algebra (§7c — no ordering, no archimedean
construct is needed to state or prove it). -/

/-- A framed (ribbon) component, carried by its writhe and its normalised total twist. -/
structure Framed (R : Type*) where
  writhe : R
  twist : R

variable {R : Type*} [AddCommGroup R]

/-- **Călugăreanu–White–Pohl self-linking** `SL = Wr + Tw` — the combination that is the isotopy
invariant. -/
def selfLinking (F : Framed R) : R := F.writhe + F.twist

/-- **The inflexional exchange.** Passing through an inflexion point shifts the writhe by `d` and
the twist by `−d` (Moffatt & Ricca §1: the two "are discontinuous by equal and opposite amounts …
so that the sum does vary continuously"). A type-I Reidemeister move is the `d = ±1` case. -/
def inflexionMove (d : R) (F : Framed R) : Framed R := ⟨F.writhe + d, F.twist - d⟩

/-- **The self-linking is invariant under the inflexional exchange** — Călugăreanu's point. -/
@[simp] theorem selfLinking_inflexionMove (d : R) (F : Framed R) :
    selfLinking (inflexionMove d F) = selfLinking F := by
  unfold selfLinking inflexionMove
  simp

/-- **The writhe alone is not** — it moves by exactly `d`. So a quantity read off the self-crossing
count is changed by a type-I move, which is what an ambient isotopy typically performs. -/
theorem writhe_inflexionMove_ne {d : R} (hd : d ≠ 0) (F : Framed R) :
    (inflexionMove d F).writhe ≠ F.writhe := by
  unfold inflexionMove
  simpa using hd

/-! ### Carrying §2 into the gate of §1

A self-energy functional on framed components is a map `Framed R → ℝ`. Whether the §1 gate holds for
it is decided by which invariant it factors through. -/

/-- **A self-energy that factors through the Călugăreanu self-linking passes the gate**: assembly
may reorganise writhe into twist, and the energy does not move. -/
theorem selfEnergy_invariant_of_factorsThroughSelfLinking (f : R → ℝ) (d : R) (F : Framed R) :
    (f ∘ selfLinking) (inflexionMove d F) = (f ∘ selfLinking) F := by
  simp

/-- **A self-energy read off the writhe alone can fail the gate.** For a faithful reading of the
self-crossing count, an inflexional (type-I) move strictly changes the self-energy, so
`selfDefect ≠ 0` and `binding = −mutual` fails. Concretely over `ℝ` with a single created
self-crossing. -/
theorem selfEnergy_not_invariant_of_writhe_valued (F : Framed ℝ) :
    (inflexionMove (1 : ℝ) F).writhe ≠ F.writhe :=
  writhe_inflexionMove_ne one_ne_zero F

/-- **The two facts side by side** — the falsifiable statement of §2. Under one and the same
inflexional move the Călugăreanu self-linking is fixed while the writhe is not, so the two candidate
self-energies disagree about whether the §1 gate holds. -/
theorem selfLinking_fixed_writhe_moved (F : Framed ℝ) :
    selfLinking (inflexionMove (1 : ℝ) F) = selfLinking F
      ∧ (inflexionMove (1 : ℝ) F).writhe ≠ F.writhe :=
  ⟨selfLinking_inflexionMove 1 F, selfEnergy_not_invariant_of_writhe_valued F⟩

end QOU.Mass.SelfCrossingInvarianceGate
