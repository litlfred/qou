import Mathlib.RepresentationTheory.Character
import Mathlib.LinearAlgebra.Matrix.PosDef
import Mathlib.LinearAlgebra.Matrix.ToLinearEquiv
import Mathlib.Analysis.Complex.Polynomial.Basic

import QOU.BringsSurface.IrreducibleH1ForcesGenusFour

/-!
# `QOU.BringsSurface.CharacterBound` — irreducible dimensions are bounded by `√|G|`

Bean `qou-qhcr`, milestone M4 (audit
`docs/audits/2026-11-17-bring-foundations-trace-sites-and-genus-attack.md`).

The arithmetic file `QOU.BringsSurface.IrreducibleH1ForcesGenusFour` took the irreducible
dimensions of `A₅` (`1, 3, 3, 4, 5`) as the hypothesis `hdim`. This file proves part of it from
character theory, with no group-specific input:

* `character_inv_eq_conj` (M4a): `χ(g⁻¹) = conj χ(g)`, by the unitary trick — the matrix
  `P = Σ_g ρ(g)ᴴ ρ(g)` is positive definite and `ρ(h)ᴴ P ρ(h) = P`.
* `finrank_sq_le_card` (M4b): an irreducible complex representation has `(dim V)² ≤ |G|`,
  from Mathlib's `FDRep.char_orthonormal`: `Σ_g |χ(g)|² = |G|`, and the `g = 1` term is
  `(dim V)²`.
* `genus_four_or_six_of_irreducible`: so `g = dim W ≤ 7` for `|A₅| = 60`, and Riemann–Hurwitz
  for `A₅` and `S₅` leaves `g ∈ {4, 6}`.

## What is still a hypothesis

To reach `g = 4` one must exclude `g = 6`, i.e. show `A₅` has no 6-dimensional irreducible
representation. That needs either the sum-of-squares identity `Σ (dim Vᵢ)² = |G|` together with
the number of irreducibles, or the explicit character table. Neither is in Mathlib; it stays the
named hypothesis `hno6` of `genus_eq_four_of_irreducible` below.
Ref: [fulton-harris1991] Fulton–Harris, *Representation Theory*, §2.1 and §5.1.
-/

open Matrix ComplexOrder
open QOU.BringsSurface.IrreducibleH1ForcesGenusFour

namespace QOU.BringsSurface.CharacterBound

variable {G : Type} [Group G] [Fintype G] {n : Type} [Fintype n] [DecidableEq n]

theorem trace_inv_eq_star_trace (M : G →* Matrix n n ℂ) (h : G) :
    (M h⁻¹).trace = star (M h).trace := by
  classical
  set P : Matrix n n ℂ := ∑ g, (M g)ᴴ * M g with hPdef
  have hinv : M h * M h⁻¹ = 1 := by rw [← map_mul, mul_inv_cancel, map_one]
  have key : (M h)ᴴ * P * M h = P := by
    rw [hPdef, Finset.mul_sum, Finset.sum_mul]
    refine (Fintype.sum_equiv (Equiv.mulRight h) _ _ (fun g => ?_))
    simp only [Equiv.coe_mulRight, map_mul, conjTranspose_mul, Matrix.mul_assoc]
  have hP : P.PosDef := by
    rw [hPdef, ← Finset.add_sum_erase _ _ (Finset.mem_univ (1 : G))]
    simp only [map_one, conjTranspose_one, Matrix.mul_one]
    exact Matrix.PosDef.one.add_posSemidef
      (Finset.sum_induction _ (fun A : Matrix n n ℂ => A.PosSemidef)
        (fun _ _ ha hb => ha.add hb) Matrix.PosSemidef.zero
        (fun g _ => Matrix.posSemidef_conjTranspose_mul_self (M g)))
  have hPu : IsUnit P.det := (Matrix.isUnit_iff_isUnit_det P).mp hP.isUnit
  have hPM : P * M h⁻¹ = (M h)ᴴ * P := by
    calc P * M h⁻¹ = (M h)ᴴ * P * M h * M h⁻¹ := by rw [key]
      _ = (M h)ᴴ * P := by rw [Matrix.mul_assoc _ (M h), hinv, Matrix.mul_one]
  calc (M h⁻¹).trace = (P⁻¹ * (P * M h⁻¹)).trace := by
        rw [← Matrix.mul_assoc, Matrix.nonsing_inv_mul _ hPu, Matrix.one_mul]
    _ = (P⁻¹ * ((M h)ᴴ * P)).trace := by rw [hPM]
    _ = ((M h)ᴴ * (P * P⁻¹)).trace := by
        rw [Matrix.trace_mul_comm, Matrix.mul_assoc]
    _ = star (M h).trace := by
        rw [Matrix.mul_nonsing_inv _ hPu, Matrix.mul_one, Matrix.trace_conjTranspose]


/-- The matrix form of a finite-dimensional representation, in a chosen basis. -/
noncomputable def matrixRep (V : FDRep ℂ G) :
    G →* Matrix (Fin (Module.finrank ℂ V.V)) (Fin (Module.finrank ℂ V.V)) ℂ :=
  (LinearMap.toMatrixAlgEquiv (Module.finBasis ℂ V.V)).toRingEquiv.toMonoidHom.comp V.ρ

omit [Fintype G] in
theorem character_eq_trace (V : FDRep ℂ G) (g : G) :
    V.character g = (matrixRep V g).trace := by
  simp only [FDRep.character, matrixRep, MonoidHom.coe_comp, Function.comp_apply]
  rw [LinearMap.trace_eq_matrix_trace ℂ (Module.finBasis ℂ V.V)]
  rfl

/-- **M4a.** `χ(g⁻¹) = conj χ(g)` for a finite-dimensional complex representation of a
finite group. Proof by the unitary trick (`trace_inv_eq_star_trace`). -/
theorem character_inv_eq_conj (V : FDRep ℂ G) (g : G) :
    V.character g⁻¹ = star (V.character g) := by
  rw [character_eq_trace, character_eq_trace, trace_inv_eq_star_trace]

/-- **M4b.** An irreducible complex representation of a finite group `G` has
`(dim V)² ≤ |G|`. From character orthonormality: `Σ_g |χ(g)|² = |G|`, and the `g = 1` term is
`(dim V)²`. -/
theorem finrank_sq_le_card (V : FDRep ℂ G) [CategoryTheory.Simple V] :
    Module.finrank ℂ V.V ^ 2 ≤ Fintype.card G := by
  have horth := FDRep.char_orthonormal V V
  rw [if_pos ⟨CategoryTheory.Iso.refl V⟩] at horth
  have hsum : (∑ g, V.character g * V.character g⁻¹) = (Fintype.card G : ℂ) := by
    have := congrArg (fun z => (Fintype.card G : ℂ) • z) horth
    simpa only [smul_eq_mul, ← mul_assoc, mul_invOf_self, one_mul, mul_one] using this
  have hreal : (∑ g, Complex.normSq (V.character g)) = (Fintype.card G : ℝ) := by
    have : ((∑ g, Complex.normSq (V.character g) : ℝ) : ℂ) = ((Fintype.card G : ℝ) : ℂ) := by
      rw [Complex.ofReal_sum]
      simp only [← Complex.mul_conj, ← Complex.star_def, ← character_inv_eq_conj]
      rw [hsum]; simp
    exact_mod_cast this
  have hle : Complex.normSq (V.character 1) ≤ ∑ g, Complex.normSq (V.character g) :=
    Finset.single_le_sum (fun g _ => Complex.normSq_nonneg _) (Finset.mem_univ 1)
  rw [hreal, FDRep.char_one, Complex.normSq_natCast] at hle
  have : ((Module.finrank ℂ V.V ^ 2 : ℕ) : ℝ) ≤ (Fintype.card G : ℝ) := by
    push_cast; nlinarith [hle]
  exact_mod_cast this

/-- **M4 consequence.** `A₅` (order 60) and `S₅` act on a curve of genus `g ≥ 2`, and
`g = dim W` for an irreducible complex `A₅`-representation `W`. Then `g = 4` or `g = 6`. -/
theorem genus_four_or_six_of_irreducible
    (GA : Type) [Group GA] [Fintype GA] (hA60 : Fintype.card GA = 60)
    (W : FDRep ℂ GA) [CategoryTheory.Simple W]
    (g hA hS : Nat) (tsA tsS : List Nat)
    (htsA : ∀ t ∈ tsA, A5Branch t) (hRHA : RH 60 g hA tsA)
    (htsS : ∀ t ∈ tsS, S5Branch t) (hRHS : RH 120 g hS tsS)
    (hgW : Module.finrank ℂ W.V = g) (hg : 2 ≤ g) : g = 4 ∨ g = 6 := by
  have hsq := finrank_sq_le_card W
  rw [hgW, hA60] at hsq
  have hg7 : g ≤ 7 := by nlinarith
  exact genus_four_or_six_of_le_seven g hA hS tsA tsS htsA hRHA htsS hRHS hg hg7

/-- **Genus 4, with `hdim` narrowed to one fact.** As above, plus the hypothesis that `W` is
not 6-dimensional (true for `A₅`, whose irreducible dimensions are `1, 3, 3, 4, 5`; not yet
formalised). -/
theorem genus_eq_four_of_irreducible
    (GA : Type) [Group GA] [Fintype GA] (hA60 : Fintype.card GA = 60)
    (W : FDRep ℂ GA) [CategoryTheory.Simple W]
    (g hA hS : Nat) (tsA tsS : List Nat)
    (htsA : ∀ t ∈ tsA, A5Branch t) (hRHA : RH 60 g hA tsA)
    (htsS : ∀ t ∈ tsS, S5Branch t) (hRHS : RH 120 g hS tsS)
    (hgW : Module.finrank ℂ W.V = g) (hg : 2 ≤ g)
    (hno6 : Module.finrank ℂ W.V ≠ 6) : g = 4 := by
  rcases genus_four_or_six_of_irreducible GA hA60 W g hA hS tsA tsS htsA hRHA htsS hRHS hgW hg
    with h | h
  · exact h
  · exact absurd (hgW.trans h) hno6

end QOU.BringsSurface.CharacterBound
