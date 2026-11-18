/-
QOU.Mass.SelfMutualPartition — mass = self-energy, binding = mutual pairing, as a THEOREM.

Arc context (bk-crossing mass-binding; bean `qou-brng`, residuals R1 + R2). `BrunnianBindingChannel`
resolved *which type* of mutual invariant carries binding (unsigned coordination count, not signed
linking number). This file resolves two residuals it left open:

* **R2 — the Hamiltonian-level assignment.** Why is rest mass the *self* (intra-component) energy and
  binding the *mutual* (inter-component) pairing? This is not a postulate. The crossing energy is a
  sum over crossings; each crossing of an assembled diagram is either intra-component (self) or
  inter-component (mutual), so the total partitions exactly:
      assembly energy = (self energy) + (mutual energy).
  An isolated component has no inter-component crossings, so its mass is its self energy. Binding, by
  the standard definition `B = (Σ isolated masses) − (assembled mass)`, is then
      B = Σ selfᵢ − assembly = − (mutual energy),
  i.e. the self energies cancel and **binding is exactly the inter-component mutual pairing** — a
  theorem (`binding_eq_neg_mutualEnergy`), given only additivity over the crossing partition and the
  mass-deficit definition of binding. Falsifiable content: binding is independent of every
  self-crossing (`binding_indep_of_self`).

* **R1 — the crossing-count → coordination coefficient.** The mutual channel's multiplicity is the
  inter-component crossing count. The coordination count (the arc's `M`) is one unit per *clasp* =
  ½ per inter-component crossing (a minimal Brunnian bond is a 2-crossing clasp), so
      coordination units = ½ · (inter-component crossing count)   (`coordinationUnits`).
  A complete graph of minimal single-clasp bonds on `A` nucleons has `2·C(A,2)` inter crossings,
  hence `C(A,2)` coordination units and per-nucleon `z = A − 1` (`complete_minimal_clasp_coordination`);
  the general coefficient beyond minimal bonds is just `½ · |inter|`. Which pairs bond, and with how
  many clasps, is the carrier's crossing structure — a topological input, saturation-limited for
  heavy `A` (`QOU.Mass.CoordinationSaturation`).

What stays open (honest): the identification of the substrate *mass observable* with this crossing
energy at the full Markov-trace granularity (the self energy closes to the q-dimension self-trace
`lw`; the archimedean dressing `m = m_e·Vol·lw/ℏ_q²`). The additive-partition assignment is proved
here; its lift to the exact mass formula is the remaining modelling step, not a fit.

Ground ring `ℝ` (archimedean energy). No fit; `energy`, `isInter` are free data.
-/
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Tactic

namespace QOU.Mass.SelfMutualPartition

open Finset

variable {C : Type*}

/-- Self (intra-component) energy: the sum over crossings that are NOT inter-component. -/
noncomputable def selfEnergy (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] : ℝ :=
  ∑ c ∈ E.filter (fun c => ¬ isInter c), energy c

/-- Mutual (inter-component) energy: the sum over inter-component crossings. -/
noncomputable def mutualEnergy (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] : ℝ :=
  ∑ c ∈ E.filter (fun c => isInter c), energy c

/-- Total energy of the assembled diagram: the sum over all its crossings. -/
noncomputable def assemblyEnergy (E : Finset C) (energy : C → ℝ) : ℝ :=
  ∑ c ∈ E, energy c

/-- **The crossing partition.** Every crossing of the assembled diagram is either self
(intra-component) or mutual (inter-component), so the total energy splits exactly. -/
theorem assemblyEnergy_partition (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] :
    assemblyEnergy E energy = selfEnergy E energy isInter + mutualEnergy E energy isInter := by
  unfold assemblyEnergy selfEnergy mutualEnergy
  rw [add_comm]
  exact (Finset.sum_filter_add_sum_filter_not E isInter energy).symm

/-- Binding energy, by the standard mass-deficit definition: the sum of the isolated component
masses (each = that component's self energy, since an isolated component has no inter-component
crossings) minus the assembled mass. Here the sum of isolated masses is `selfEnergy` (the self
crossings are exactly those present in isolation). -/
noncomputable def binding (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] : ℝ :=
  selfEnergy E energy isInter - assemblyEnergy E energy

/-- **R2 — binding is exactly the (negative of the) mutual pairing.** The self energies cancel: rest
mass is the self part, binding is the inter-component mutual part. The assignment mass ↔ self,
binding ↔ mutual is a theorem of the crossing partition plus the mass-deficit definition, not a
modelling postulate. -/
theorem binding_eq_neg_mutualEnergy (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] :
    binding E energy isInter = - mutualEnergy E energy isInter := by
  unfold binding
  rw [assemblyEnergy_partition E energy isInter]
  ring

/-- **Binding sees only inter-component structure.** Two assemblies with the same inter-component
crossings and mutual energies have equal binding, whatever their self-crossings — the falsifiable
form of "binding is purely the mutual pairing." -/
theorem binding_indep_of_self (E₁ E₂ : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter]
    (h : mutualEnergy E₁ energy isInter = mutualEnergy E₂ energy isInter) :
    binding E₁ energy isInter = binding E₂ energy isInter := by
  rw [binding_eq_neg_mutualEnergy, binding_eq_neg_mutualEnergy, h]

/-! ## R1 — the crossing-count → coordination coefficient -/

/-- The number of inter-component crossings of the assembled diagram. -/
noncomputable def interCrossingCount (E : Finset C) (isInter : C → Prop)
    [DecidablePred isInter] : ℕ :=
  (E.filter (fun c => isInter c)).card

/-- **Coordination units = ½ · (inter-component crossing count).** One coordination unit per clasp;
a clasp is two inter-component crossings (a minimal Brunnian bond, `n₊ = n₋ = 1`). This is the
general crossing-count → coordination coefficient — no minimal-bond restriction. -/
noncomputable def coordinationUnits (E : Finset C) (isInter : C → Prop)
    [DecidablePred isInter] : ℝ :=
  (interCrossingCount E isInter : ℝ) / 2

/-- **Complete graph of minimal single-clasp bonds.** If the `A`-nucleon carrier is the complete
graph in which every one of the `C(A,2)` pairs is a single minimal clasp (two inter-component
crossings), the inter-component crossing count is `2·C(A,2)`, so the coordination count is
`C(A,2) = A(A−1)/2` and the per-nucleon coordination is `z = A − 1`. -/
theorem complete_minimal_clasp_coordination (E : Finset C) (isInter : C → Prop)
    [DecidablePred isInter] (A : ℕ)
    (h : interCrossingCount E isInter = 2 * A.choose 2) :
    coordinationUnits E isInter = (A : ℝ) * ((A : ℝ) - 1) / 2 := by
  unfold coordinationUnits
  rw [h]
  rw [Nat.cast_mul, Nat.cast_choose_two]
  push_cast
  ring

/-- Per-nucleon coordination of the complete minimal-clasp cluster is `z = A − 1`
(`coordinationUnits · 2 / A`), for `A ≥ 1`. -/
theorem complete_minimal_clasp_per_nucleon (E : Finset C) (isInter : C → Prop)
    [DecidablePred isInter] (A : ℕ) (hA : 1 ≤ A)
    (h : interCrossingCount E isInter = 2 * A.choose 2) :
    coordinationUnits E isInter * 2 / A = (A : ℝ) - 1 := by
  rw [complete_minimal_clasp_coordination E isInter A h]
  have hA0 : (A : ℝ) ≠ 0 := Nat.cast_ne_zero.mpr (by omega)
  field_simp

/-- Sum of `binding` and `mutualEnergy` vanishes identically. -/
theorem binding_add_mutualEnergy_eq_zero (E : Finset C) (energy : C → ℝ) (isInter : C → Prop)
    [DecidablePred isInter] :
    binding E energy isInter + mutualEnergy E energy isInter = 0 := by
  rw [binding_eq_neg_mutualEnergy E energy isInter, neg_add_cancel]

end QOU.Mass.SelfMutualPartition
