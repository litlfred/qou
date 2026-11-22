import QOU.BringsSurface.GenusFourFromGermStabilisers
import QOU.RiemannSurface.CombinatorialMapQuotient
import QOU.RiemannSurface.MapGenusNonneg

/-!
# `QOU.BringsSurface.GenusFourFromEquivariantMap` — `χ = −6` from an equivariant map

Bean `qou-m3tr` (Bring milestone M3, step 3 interface), parent `qou-qhcr`.

The genus-4 capstone `genus_eq_four_of_cellular` takes abstract cell data `V E F` with the Euler
characteristics `hX : χ(X) = 2 − 2g` and `hY : χ(X/G) = 2 − 2h` as hypotheses. This file
replaces that cell data by a **combinatorial map** — darts `D`, a vertex rotation `σ`, and a
fixed-point-free involution `α` — and **derives** `hX` and `hY`:

* `hX` from `exists_genus_nonneg` (Ree's inequality): a connected map has `χ = 2 − 2g`, `g : ℕ`;
* `hY` from `cycleOrbitsEquiv` (orbits of cells are the cells of the quotient map), the
  quotient map being again a connected map (`quotPerm_involutive`,
  `quotAlpha_fixedPointFree`, `orbits_quot_eq_one`).

## Main result

`chi_eq_neg_six_of_equivariant_map`: let a connected map carry an `A₅`-action and an
`S₅`-action commuting with `σ, α`, free on edges and faces, with cyclic vertex stabilisers. If its
genus lies in `{1, 3, 4, 5}` and is at least `2` (the hypothesis `H¹ = 2W`, `W` irreducible, of
`IrreducibleH1ForcesGenusFour`), then **`χ = −6`**.

## What stays a hypothesis

* **Triangulation.** That a compact Riemann surface with a holomorphic `G`-action carries such a
  `G`-equivariant map, with branch points at vertices. This is Radó's theorem plus an equivariant
  refinement; Mathlib has neither. It is the only topological input left, and it is not stated
  here as an axiom or class: the theorem simply starts from the map.
* **Cyclic stabilisers** (`hcycA`, `hcycS`): supplied by `GermAction.isCyclic` once the chart
  step (M2) is available.
* **Genus window** (`hχ`): `H¹ = 2W` with `W` irreducible (gaps G2/G3).

Ref: [farkas-kra1992] Farkas–Kra, *Riemann Surfaces*, §I.2 and §V.1.
-/

namespace QOU.BringsSurface.GenusFourFromEquivariantMap

open MulAction Equiv
open QOU.RiemannSurface.CombinatorialMapQuotient QOU.RiemannSurface.MapGenusNonneg
  QOU.RiemannSurface.CombinatorialMapEuler QOU.BringsSurface.GenusFourFromGermStabilisers

set_option linter.unusedSectionVars false

section Quotient

variable {G D : Type*} [Group G] [MulAction G D]

theorem quotPerm_mul {σ α : Perm D} (hσ : Equivariant σ G) (hα : Equivariant α G) :
    quotPerm (hσ.mul hα) = quotPerm hσ * quotPerm hα := by
  ext q
  induction q using Quotient.inductionOn' with
  | h x => rfl

/-- A connected map stays connected in the quotient. -/
theorem orbits_quot_eq_one [Fintype D] [DecidableEq D] [Nonempty D]
    [Fintype (orbitRel.Quotient G D)] [DecidableEq (orbitRel.Quotient G D)]
    {σ α : Perm D} (hσ : Equivariant σ G) (hα : Equivariant α G)
    (hconn : orbits σ α = 1) : orbits (quotPerm hσ) (quotPerm hα) = 1 := by
  have hsub : ∀ x y : D, orbitSetoid σ α x y := by
    have : Subsingleton (Quotient (orbitSetoid σ α)) :=
      (Nat.card_eq_one_iff_unique.1 hconn).1
    exact fun x y => Quotient.exact (Subsingleton.elim (Quotient.mk _ x) (Quotient.mk _ y))
  have hmap : ∀ x y : D, orbitSetoid (quotPerm hσ) (quotPerm hα)
      (Quotient.mk'' x) (Quotient.mk'' y) := by
    intro x y
    have h := hsub x y
    induction h with
    | rel u v k =>
      rcases k with rfl | rfl
      · exact Relation.EqvGen.rel _ _ (Or.inl rfl)
      · exact Relation.EqvGen.rel _ _ (Or.inr rfl)
    | refl u => exact Relation.EqvGen.refl _
    | symm u v _ ih => exact Relation.EqvGen.symm _ _ ih
    | trans u v w _ _ ih1 ih2 => exact Relation.EqvGen.trans _ _ _ ih1 ih2
  unfold orbits
  rw [Nat.card_eq_one_iff_unique]
  refine ⟨⟨fun p q => ?_⟩, ⟨Quotient.mk _ (Quotient.mk'' (Classical.arbitrary D))⟩⟩
  induction p using Quotient.inductionOn with
  | h p =>
  induction q using Quotient.inductionOn with
  | h q =>
  induction p using Quotient.inductionOn' with
  | h x =>
  induction q using Quotient.inductionOn' with
  | h y => exact Quotient.sound (hmap x y)

/-- **`hY` from the map.** The orbit counts of the cells of a connected map, under an action free
on edges, satisfy `|V/G| − |E/G| + |F/G| = 2 − 2h` with `h : ℕ`. -/
theorem quotient_genus [Fintype D] [DecidableEq D] [Nonempty D]
    {σ α : Perm D} (hσ : Equivariant σ G) (hα : Equivariant α G)
    (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x)
    (hfree : letI := cycleAction hα; ∀ (g : G) (e : Cycles α), g • e = e → g = 1)
    (hconn : orbits σ α = 1) :
    ∃ h : ℕ,
      ((letI := cycleAction hσ; Nat.card (orbitRel.Quotient G (Cycles σ)) : ℕ) : ℤ)
      - (letI := cycleAction hα; Nat.card (orbitRel.Quotient G (Cycles α)) : ℕ)
      + (letI := cycleAction (hσ.mul hα);
          Nat.card (orbitRel.Quotient G (Cycles (σ * α))) : ℕ) = 2 - 2 * h := by
  classical
  letI : Fintype (orbitRel.Quotient G D) := Fintype.ofFinite _
  rw [card_cycleOrbits_eq hσ, card_cycleOrbits_eq hα, card_cycleOrbits_eq (hσ.mul hα),
    quotPerm_mul]
  have hinv' := quotPerm_involutive hα hinv
  have hfix' := quotAlpha_fixedPointFree hα hfix hfree
  have hconn' := orbits_quot_eq_one hσ hα hconn
  exact exists_genus_nonneg (quotPerm hσ) (quotPerm hα) hinv' hfix' hconn'

end Quotient

/-- Free on cells, in the cardinality form of the capstone. -/
theorem card_stabilizer_eq_one {G X : Type*} [Group G] [MulAction G X] [Fintype G]
    (x : X) [Fintype (stabilizer G x)] (h : ∀ g : G, g • x = x → g = 1) :
    Fintype.card (stabilizer G x) = 1 := by
  rw [Fintype.card_eq_one_iff]
  refine ⟨1, fun y => Subtype.ext ?_⟩
  exact h y.1 y.2

/-- **`χ = −6` from an `A₅`- and `S₅`-equivariant connected map.** -/
theorem chi_eq_neg_six_of_equivariant_map
    {D : Type*} [Fintype D] [DecidableEq D] [Nonempty D]
    (σ α : Perm D) (hinv : α * α = 1) (hfix : ∀ x, α x ≠ x) (hconn : orbits σ α = 1)
    (GA GS : Type*) [Group GA] [Fintype GA] [Group GS] [Fintype GS]
    [MulAction GA D] [MulAction GS D]
    (eA : GA ≃* alternatingGroup (Fin 5)) (eS : GS ≃* Perm (Fin 5))
    (hσA : Equivariant σ GA) (hαA : Equivariant α GA)
    (hσS : Equivariant σ GS) (hαS : Equivariant α GS)
    (hEA : letI := cycleAction hαA; ∀ (g : GA) (e : Cycles α), g • e = e → g = 1)
    (hFA : letI := cycleAction (hσA.mul hαA); ∀ (g : GA) (f : Cycles (σ * α)), g • f = f → g = 1)
    (hES : letI := cycleAction hαS; ∀ (g : GS) (e : Cycles α), g • e = e → g = 1)
    (hFS : letI := cycleAction (hσS.mul hαS); ∀ (g : GS) (f : Cycles (σ * α)), g • f = f → g = 1)
    (hcycA : letI := cycleAction hσA; ∀ v : Cycles σ, IsCyclic (stabilizer GA v))
    (hcycS : letI := cycleAction hσS; ∀ v : Cycles σ, IsCyclic (stabilizer GS v))
    (hχ2 : (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) ≤ -2)
    (hχ : (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = 0 ∨
      (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = -4 ∨
      (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = -6 ∨
      (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = -8) :
    (numCycles σ : ℤ) - numCycles α + numCycles (σ * α) = -6 := by
  classical
  obtain ⟨g, hg⟩ := exists_genus_nonneg σ α hinv hfix hconn
  obtain ⟨hA, hYA⟩ := quotient_genus hσA hαA hinv hfix hEA hconn
  obtain ⟨hS, hYS⟩ := quotient_genus hσS hαS hinv hfix hES hconn
  have hX : ((Nat.card (Cycles σ) : ℕ) : ℤ) - (Nat.card (Cycles α) : ℕ)
      + (Nat.card (Cycles (σ * α)) : ℕ) = 2 - 2 * g := hg
  have hg2 : 2 ≤ g := by omega
  have hgdim : g = 1 ∨ g = 3 ∨ g = 4 ∨ g = 5 := by omega
  have h4 : g = 4 := by
    letI iVA := cycleAction (G := GA) hσA
    letI iEA := cycleAction (G := GA) hαA
    letI iFA := cycleAction (G := GA) (hσA.mul hαA)
    letI iVS := cycleAction (G := GS) hσS
    letI iES := cycleAction (G := GS) hαS
    letI iFS := cycleAction (G := GS) (hσS.mul hαS)
    simp only [Nat.card_eq_fintype_card] at hX hYA hYS
    exact genus_eq_four_of_cyclic_stabilisers GA GS eA eS
      (Cycles σ) (Cycles α) (Cycles (σ * α)) (Cycles σ) (Cycles α) (Cycles (σ * α))
      (fun e => card_stabilizer_eq_one e (hEA · e))
      (fun f => card_stabilizer_eq_one f (hFA · f))
      (fun e => card_stabilizer_eq_one e (hES · e))
      (fun f => card_stabilizer_eq_one f (hFS · f))
      hcycA hcycS g hA hS hX hYA hX hYS hg2 hgdim
  omega

end QOU.BringsSurface.GenusFourFromEquivariantMap
