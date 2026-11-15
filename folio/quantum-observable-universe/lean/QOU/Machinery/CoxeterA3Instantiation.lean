/-
# The A₃ instantiation — faithfulness residues killed, braid + far-commutation unconditional

The concrete payoff of the transversal bricks: at the type-A₃ Coxeter
system (`CoxeterMatrix.Aₙ 3`, the S₄ tower rung), the Tits-faithfulness
residues `IsReduced [i,j,i]` / `IsReduced [i,j]` are PROVED, so the
dihedral and commuting coset structures — and with them the braid and
far-commutation relations on the length-rule module — hold with NO
remaining hypothesis at this rung.

Method: the permutation representation. `CoxeterSystem.lift` sends the
three A₃ generators to the adjacent transpositions of `Perm (Fin 4)`
(`fA3_liftable` is a finite `decide`). A cell word could only fail to be
reduced by having short length; parity and the length bound leave a
single alternative (`ℓ = 1` for the braid word, `ℓ = 0` for the
commuting word), and the permutation image refutes it by computation —
`t₀t₁t₀` is not a transposition image of any generator, `t₀t₂ ≠ 1`.

Results:

* **`isReduced_010` / `isReduced_121` / `isReduced_02`** — the three
  residues of the A₃ system, proved.
* **`transversalA3_01` / `transversalA3_12`** — `DihedralCosetStructure`
  on the A₃ Coxeter group for both braid pairs, hypothesis-free.
* **`commutingA3_02`** — `CommutingCosetStructure` for the far pair.
* **`braid_A3_01` / `braid_A3_12` / `far_commute_A3_02`** — the three
  presentation laws on the length-rule module of the A₃ group,
  UNCONDITIONAL.

HONESTY (STRICT): sorry-free, no axioms; `decide` is used only on finite
`Perm (Fin 4)` / Coxeter-matrix-entry facts (kernel-checked
computation), never to mask a claim. The general-rank residue (Tits
faithfulness for arbitrary systems) remains open and is unaffected.
Nothing wired; `1/(8π)` stays phase-4.

-- Ref: [kassel1995] https://doi.org/10.1007/978-1-4612-0783-2
-- Ref: [jones1987] https://doi.org/10.2307/1971403
-/
import QOU.Machinery.CoxeterCommutingTransversal

namespace QOU.Machinery.CoxeterParabolic

open CoxeterSystem List CoxeterMatrix

/-- The A₃ Coxeter system on its presented group (the S₄ rung). -/
noncomputable def csA3 : CoxeterSystem (Aₙ 3) (Aₙ 3).Group :=
  (Aₙ 3).toCoxeterSystem

local prefix:100 "ℓ" => csA3.length
local prefix:100 "π" => csA3.wordProd
local prefix:100 "σ" => csA3.simple

/-- The adjacent-transposition assignment `sₖ ↦ (k, k+1)`. -/
def fA3 : Fin 3 → Equiv.Perm (Fin 4) := fun k => Equiv.swap k.castSucc k.succ

/-- The transpositions satisfy the A₃ Coxeter relations (finite check). -/
lemma fA3_liftable : (Aₙ 3).IsLiftable fA3 := by
  intro i i'
  fin_cases i <;> fin_cases i' <;> decide

/-- The permutation representation of the A₃ Coxeter group. -/
noncomputable def φA3 : (Aₙ 3).Group →* Equiv.Perm (Fin 4) :=
  csA3.lift ⟨fA3, fA3_liftable⟩

@[simp] lemma φA3_simple (k : Fin 3) : φA3 (σ k) = fA3 k :=
  csA3.lift_apply_simple fA3_liftable k

/-! ## The residues, killed -/

/-- Core step, shared by the two braid pairs: `ℓ(σᵢσⱼσᵢ) = 3` because the
length is ≤ 3 and odd, and the permutation image rules out length 1. -/
private lemma isReduced_iji_of_perm (i j : Fin 3)
    (hperm : ∀ k : Fin 3, fA3 i * fA3 j * fA3 i ≠ fA3 k) :
    csA3.IsReduced [i, j, i] := by
  have hπ : π [i, j, i] = σ i * σ j * σ i := wordProd_iji csA3 i j
  have hupper : ℓ (π [i, j, i]) ≤ 3 := by
    simpa using csA3.length_wordProd_le [i, j, i]
  have hparity : ℓ (π [i, j, i]) % 2 = 1 := by
    rw [hπ]
    have h1 := csA3.length_mul_mod_two (σ i * σ j) (σ i)
    have h2 := csA3.length_mul_mod_two (σ i) (σ j)
    have h3 := csA3.length_simple i
    have h4 := csA3.length_simple j
    omega
  have hne1 : ℓ (π [i, j, i]) ≠ 1 := by
    intro h1
    obtain ⟨k, hk⟩ := csA3.length_eq_one_iff.mp h1
    rw [hπ] at hk
    have happ := congrArg φA3 hk
    rw [map_mul, map_mul, φA3_simple, φA3_simple, φA3_simple] at happ
    exact hperm k happ
  show ℓ (π [i, j, i]) = [i, j, i].length
  simp only [List.length_cons, List.length_nil]
  omega

/-- `IsReduced [0, 1, 0]` — the first A₃ braid-pair residue. -/
theorem isReduced_010 : csA3.IsReduced [(0 : Fin 3), 1, 0] :=
  isReduced_iji_of_perm 0 1 (by decide)

/-- `IsReduced [1, 2, 1]` — the second A₃ braid-pair residue. -/
theorem isReduced_121 : csA3.IsReduced [(1 : Fin 3), 2, 1] :=
  isReduced_iji_of_perm 1 2 (by decide)

/-- `IsReduced [0, 2]` — the A₃ far-pair residue: length ≤ 2, even, and
nonzero because `t₀t₂ ≠ 1` in `Perm (Fin 4)`. -/
theorem isReduced_02 : csA3.IsReduced [(0 : Fin 3), 2] := by
  have hπ : π [(0 : Fin 3), 2] = σ 0 * σ 2 := wordProd_ij csA3 0 2
  have hupper : ℓ (π [(0 : Fin 3), 2]) ≤ 2 := by
    simpa using csA3.length_wordProd_le [(0 : Fin 3), 2]
  have hparity : ℓ (π [(0 : Fin 3), 2]) % 2 = 0 := by
    rw [hπ]
    have h2 := csA3.length_mul_mod_two (σ 0) (σ 2)
    have h3 := csA3.length_simple (0 : Fin 3)
    have h4 := csA3.length_simple (2 : Fin 3)
    omega
  have hne0 : ℓ (π [(0 : Fin 3), 2]) ≠ 0 := by
    intro h0
    have hone : π [(0 : Fin 3), 2] = 1 := csA3.length_eq_zero_iff.mp h0
    rw [hπ] at hone
    have happ := congrArg φA3 hone
    rw [map_mul, φA3_simple, φA3_simple, map_one] at happ
    revert happ
    decide
  show ℓ (π [(0 : Fin 3), 2]) = [(0 : Fin 3), 2].length
  simp only [List.length_cons, List.length_nil]
  omega

/-! ## The coset structures and presentation laws, unconditional -/

open QOU.Machinery.HeckeGeneral

/-- The dihedral coset structure of the A₃ pair `(0, 1)` — no hypothesis. -/
noncomputable def transversalA3_01 : DihedralCosetStructure (Aₙ 3).Group :=
  dihedralTransversal csA3 0 1 (by decide) isReduced_010

/-- The dihedral coset structure of the A₃ pair `(1, 2)` — no hypothesis. -/
noncomputable def transversalA3_12 : DihedralCosetStructure (Aₙ 3).Group :=
  dihedralTransversal csA3 1 2 (by decide) isReduced_121

/-- The commuting coset structure of the A₃ far pair `(0, 2)` — no
hypothesis. -/
noncomputable def commutingA3_02 : CommutingCosetStructure (Aₙ 3).Group :=
  commutingTransversal csA3 0 2 (by decide) isReduced_02

variable {R : Type*} [CommRing R]

/-- **The braid relation at the A₃ pair `(0,1)`, UNCONDITIONAL.** -/
theorem braid_A3_01 (h : R) (v : (Aₙ 3).Group → R) :
    mulStep transversalA3_01.Di h
        (mulStep transversalA3_01.Dj h (mulStep transversalA3_01.Di h v))
      = mulStep transversalA3_01.Dj h
          (mulStep transversalA3_01.Di h (mulStep transversalA3_01.Dj h v)) :=
  DihedralCosetStructure.braid_of_dihedral _ h v

/-- **The braid relation at the A₃ pair `(1,2)`, UNCONDITIONAL.** -/
theorem braid_A3_12 (h : R) (v : (Aₙ 3).Group → R) :
    mulStep transversalA3_12.Di h
        (mulStep transversalA3_12.Dj h (mulStep transversalA3_12.Di h v))
      = mulStep transversalA3_12.Dj h
          (mulStep transversalA3_12.Di h (mulStep transversalA3_12.Dj h v)) :=
  DihedralCosetStructure.braid_of_dihedral _ h v

/-- **Far commutation at the A₃ pair `(0,2)`, UNCONDITIONAL.** -/
theorem far_commute_A3_02 (h : R) (v : (Aₙ 3).Group → R) :
    mulStep commutingA3_02.Di h (mulStep commutingA3_02.Dj h v)
      = mulStep commutingA3_02.Dj h (mulStep commutingA3_02.Di h v) :=
  CommutingCosetStructure.far_commute_of_commuting _ h v

end QOU.Machinery.CoxeterParabolic
