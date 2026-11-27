import QOU.MassTheory.NeutronFourStrand

/-!
# The nucleon split from the four-strand lepton reading

Beans `qou-myts` (nucleon split), related `qou-99qc`. Pre-registered in
`computations/probes/nucleon_split_four_strand/PREREGISTRATION.md`; audit
`docs/audits/2026-11-27-nucleon-split-four-strand.md`.

## Setting

`QOU.MassTheory.NeutronFourStrand` (choice C-lep): the `T³ = 0` block of `V^{⊗4}` is
`N ⊕ P`, `N = n⊗ν`, `P = p⊗e`, with `σ₁, σ₂` block-diagonal and `σ₃` (third quark × lepton)
mapping `N ↔ P`. The sector traces `trN`, `trP` are the traces with the lepton strand coloured
`ν`, resp. `e`. With `K^{⊗4} = 1` on both sectors and the same `[2]_q⁴` on both, the Gibbs map of
`NucleonSplitGibbsCoulomb` reads `m_n − m_p = E₀ · log(trP(β)/trN(β))`. The spectator word
`V³ ⊗ 1` gives ratio `1` (`NeutronFourStrand.trN_V3_eq_trP_V3`), so the split comes only from
the lepton's crossings.

## What is proved (generic `[Field R]`, no number enters)

1. **Words.** Explicit block matrices of `L = σ₃σ₂σ₁²σ₂σ₃` (the lepton loops once around the
   whole nucleon), `L⁻¹`, and the pure-braid generators `A_{k4}^{±1}` (the lepton loops around
   quark strand `k`), each proved equal to its braid word step by step (`Lp_eq`, …).
2. **`L` sees the nucleon, not a quark** (`Lp_comm_s1`, `Lp_comm_s2`): `L` commutes with `σ₁, σ₂`
   on the block. Hence (`trN_conj_mul`, `trP_conj_mul`) the sector traces of `M·L` are
   invariant under conjugating `M` by any block-diagonal invertible `G` commuting with `L`, in
   particular by every word in `σ₁^{±1}, σ₂^{±1}`: the headline does not depend on the
   representative of the nucleon word in its `B₃` conjugacy class.
3. **`L` on the proton sector** (`Lp_blockP`): the `P`-block of `L` is `q² · 1`, so
   `trP(V³L) = q² · trP(V³)` (`trP_V3_Lp_eq`).
4. **Closed forms** (`trN_V3_Lp`, `trP_V3_Lp`, …, `trN_V3_A14m`, `trP_V3_A14m`, and the
   single-crossing references `trN_V3_s3`, …): exact Laurent polynomials in `q`.
5. **Headline ratio and chirality** (`ratio_Lp`, `ratio_Lm_eq_inv`): with
   `S(q) = q¹² − 3q¹⁰ + 3q⁸ − 5q⁶ + 3q⁴ − 3q² + 1` (the spectator polynomial,
   `tr V³ = −S/q⁶`) and `Λ(q) = q¹⁶ − 4q¹⁴ + 6q¹² − 10q¹⁰ + 11q⁸ − 10q⁶ + 6q⁴ − 4q² + 1`,
   `trP(V³L)/trN(V³L) = q²S/Λ`, and the mirror word `L⁻¹` gives exactly the reciprocal. The
   magnitude of the split is chirality-free; only its sign depends on `L` vs `L⁻¹`.

## Scope

Sector traces are lepton-coloured traces: invariant under `B₃` conjugation of the nucleon word
(point 2) but not under `B₄` conjugation that moves the lepton strand. No numerical value enters.
The identity `L = Δ₄²Δ₃⁻²` is checked in the probe on the block, not proved here.
-/

namespace QOU.Nuclear.NucleonSplitFourStrand

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.MassTheory.NeutronFourStrand

variable {R : Type*} [Field R]

/-- `σ₁⁻¹` on the block. -/
def s1Inv (q : R) : Matrix Ix Ix R := fromBlocks (B₁Inv q) 0 0 (A₁Inv q)

/-- Entrywise check of a product identity on the `6 × 6` block. -/
syntax "blk6" "[" Lean.Parser.Tactic.simpLemma,* "]" : tactic
macro_rules
  | `(tactic| blk6 [$ids,*]) => `(tactic| (
      ext i j
      rcases i with i | i <;> rcases j with j | j <;> fin_cases i <;> fin_cases j <;>
        simp [$ids,*, s1, s2, s2Inv, s3, s3Inv, s1Inv, E, Et, B₁, B₂, A₁, A₂, B₁Inv, B₂Inv,
          A₁Inv, A₂Inv, Matrix.mul_apply, Fintype.sum_sum_type, Fin.sum_univ_three,
          fromBlocks] <;>
        first | done | ring1 | (field_simp <;> ring1)))

/-! ## 1. Words on the block -/

/-- `V³` on `W_n`, explicit. -/
def V3BX (q : R) : Matrix (Fin 3) (Fin 3) R := !![q ^ 2 - 2 + 3 * q⁻¹ ^ 2 - q⁻¹ ^ 4, -q ^ 5 + 3 * q ^ 3 - 5 * q + 6 * q⁻¹ - 4 * q⁻¹ ^ 3 + q⁻¹ ^ 5, q ^ 4 - 3 * q ^ 2 + 4 - 3 * q⁻¹ ^ 2 + q⁻¹ ^ 4; q ^ 3 - 3 * q + 4 * q⁻¹ - 3 * q⁻¹ ^ 3 + q⁻¹ ^ 5, -q ^ 6 + 4 * q ^ 4 - 7 * q ^ 2 + 9 - 7 * q⁻¹ ^ 2 + 4 * q⁻¹ ^ 4 - q⁻¹ ^ 6, q ^ 5 - 4 * q ^ 3 + 6 * q - 5 * q⁻¹ + 3 * q⁻¹ ^ 3 - q⁻¹ ^ 5; -q ^ 2 + 2 - q⁻¹ ^ 2, q ^ 5 - 3 * q ^ 3 + 4 * q - 3 * q⁻¹ + q⁻¹ ^ 3, -q ^ 4 + 3 * q ^ 2 - 2 + q⁻¹ ^ 2]

/-- `V³` on `W_p`, explicit. -/
def V3AX (q : R) : Matrix (Fin 3) (Fin 3) R := !![-q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 2, q ^ 5 - 2 * q ^ 3 + q, -q ^ 2 + 2 - q⁻¹ ^ 2; -q + 2 * q⁻¹ - q⁻¹ ^ 3, 1, q⁻¹ - 2 * q⁻¹ ^ 3 + q⁻¹ ^ 5; q ^ 4 - 3 * q ^ 2 + 4 - 3 * q⁻¹ ^ 2 + q⁻¹ ^ 4, -q ^ 3 + 2 * q - q⁻¹, 2 - 3 * q⁻¹ ^ 2 + 3 * q⁻¹ ^ 4 - q⁻¹ ^ 6]

/-- `L = σ₃σ₂σ₁²σ₂σ₃`: the lepton strand loops once around the whole nucleon. -/
def Lp (q : R) : Matrix Ix Ix R := s3 q * s2 q * s1 q * s1 q * s2 q * s3 q

/-- Explicit form of `Lp`. -/
def LpX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 4 - 1 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹, q ^ 4 - 2 * q ^ 2 + 1; q ^ 3 - 2 * q + q⁻¹, 2 * q ^ 4 - 3 * q ^ 2 + 2, q ^ 5 - 2 * q ^ 3 + q; q ^ 4 - 2 * q ^ 2 + 1, q ^ 5 - 2 * q ^ 3 + q, q ^ 6 - q ^ 4 + 1]
    !![q ^ 2 - 1, q ^ 3 - q, 0; q ^ 3 - q, 0, q ^ 3 - q; 0, q ^ 3 - q, q ^ 4 - q ^ 2]
    !![q ^ 2 - 1, q ^ 3 - q, 0; q ^ 3 - q, 0, q ^ 3 - q; 0, q ^ 3 - q, q ^ 4 - q ^ 2]
    !![q ^ 2, 0, 0; 0, q ^ 2, 0; 0, 0, q ^ 2]

def Lp_2 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1, 0, 0; 0, 0, q - q⁻¹; 0, q, q ^ 2 - 1]
    !![1, q - q⁻¹, 0; 0, 0, q; 0, 0, 0]
    !![0, 0, 0; q, 0, 0; 0, 0, 1]
    !![0, q, 0; 0, 0, 0; 0, 0, 0]

def Lp_3 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![0, q ^ 2 - 1, 0; 0, 0, q ^ 2 - 1; q, q ^ 2 - 1, q ^ 3 - q]
    !![q, 0, q - q⁻¹; 0, q, q ^ 2 - 1; 0, 0, 0]
    !![0, 0, 0; 0, q, 0; 0, 0, q]
    !![0, 0, q; 0, 0, 0; 0, 0, 0]

def Lp_4 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1, q ^ 3 - 2 * q + q⁻¹, 0; 0, 0, q ^ 3 - q; q ^ 2 - 1, q ^ 3 - q + q⁻¹, q ^ 4 - q ^ 2]
    !![q ^ 2, q - q⁻¹, q ^ 2 - 2 + q⁻¹ ^ 2; 0, q ^ 2 - 1, q ^ 3 - q + q⁻¹; 0, 0, 0]
    !![0, 0, 0; q, q ^ 2 - 1, 0; 0, 0, q ^ 2]
    !![0, q, q ^ 2 - 1; 0, 0, 0; 0, 0, 0]

def Lp_5 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 3 - q, 0, q ^ 3 - 2 * q + q⁻¹; 0, q ^ 3 - q, q ^ 4 - 2 * q ^ 2 + 1; q ^ 3 - q, q ^ 4 - q ^ 2, q ^ 5 - q ^ 3 + q⁻¹]
    !![q - q⁻¹, 2 * q ^ 2 - 2 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹; q ^ 2 - 1, q ^ 3 - 2 * q + q⁻¹, q ^ 4 - q ^ 2 + 1; 0, 0, 0]
    !![0, 0, 0; q ^ 2, 0, q ^ 2 - 1; 0, q ^ 2, q ^ 3 - q]
    !![q, q ^ 2 - 1, q ^ 3 - q; 0, 0, 0; 0, 0, 0]

theorem Lp_2_step (q : R) (hq : q ≠ 0) : s3 q * s2 q = Lp_2 q := by
  blk6 [s3, s2, Lp_2]

theorem Lp_3_step (q : R) (hq : q ≠ 0) : Lp_2 q * s1 q = Lp_3 q := by
  blk6 [Lp_2, s1, Lp_3]

theorem Lp_4_step (q : R) (hq : q ≠ 0) : Lp_3 q * s1 q = Lp_4 q := by
  blk6 [Lp_3, s1, Lp_4]

theorem Lp_5_step (q : R) (hq : q ≠ 0) : Lp_4 q * s2 q = Lp_5 q := by
  blk6 [Lp_4, s2, Lp_5]

theorem LpX_step (q : R) (hq : q ≠ 0) : Lp_5 q * s3 q = LpX q := by
  blk6 [Lp_5, s3, LpX]

theorem Lp_eq (q : R) (hq : q ≠ 0) : Lp q = LpX q := by
  rw [Lp, Lp_2_step q hq, Lp_3_step q hq, Lp_4_step q hq, Lp_5_step q hq, LpX_step q hq]

/-- `L⁻¹ = σ₃⁻¹σ₂⁻¹σ₁⁻²σ₂⁻¹σ₃⁻¹`. -/
def Lm (q : R) : Matrix Ix Ix R := s3Inv q * s2Inv q * s1Inv q * s1Inv q * s2Inv q * s3Inv q

/-- Explicit form of `Lm`. -/
def LmX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q⁻¹ ^ 2, 0, 0; 0, q⁻¹ ^ 2, 0; 0, 0, q⁻¹ ^ 2]
    !![-q⁻¹ ^ 2 + q⁻¹ ^ 4, -q⁻¹ + q⁻¹ ^ 3, 0; -q⁻¹ + q⁻¹ ^ 3, 0, -q⁻¹ + q⁻¹ ^ 3; 0, -q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2]
    !![-q⁻¹ ^ 2 + q⁻¹ ^ 4, -q⁻¹ + q⁻¹ ^ 3, 0; -q⁻¹ + q⁻¹ ^ 3, 0, -q⁻¹ + q⁻¹ ^ 3; 0, -q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2]
    !![1 - q⁻¹ ^ 4 + q⁻¹ ^ 6, q⁻¹ - 2 * q⁻¹ ^ 3 + q⁻¹ ^ 5, 1 - 2 * q⁻¹ ^ 2 + q⁻¹ ^ 4; q⁻¹ - 2 * q⁻¹ ^ 3 + q⁻¹ ^ 5, 2 - 3 * q⁻¹ ^ 2 + 2 * q⁻¹ ^ 4, q - 2 * q⁻¹ + q⁻¹ ^ 3; 1 - 2 * q⁻¹ ^ 2 + q⁻¹ ^ 4, q - 2 * q⁻¹ + q⁻¹ ^ 3, q ^ 2 - 1 + q⁻¹ ^ 4]

def Lm_2 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![0, 0, 0; 0, 0, 0; 0, q⁻¹, 0]
    !![1, 0, 0; 0, 0, q⁻¹; 0, 0, 0]
    !![0, 0, 0; q⁻¹, 0, 0; 0, -q + q⁻¹, 1]
    !![-1 + q⁻¹ ^ 2, q⁻¹, 0; -q + q⁻¹, 0, 0; 0, 0, -1 + q⁻¹ ^ 2]

def Lm_3 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![0, 0, 0; 0, 0, 0; q⁻¹, 0, 0]
    !![q⁻¹, 0, 0; 0, q⁻¹, 0; 0, 0, 0]
    !![0, 0, 0; -1 + q⁻¹ ^ 2, q⁻¹, 0; -q + q⁻¹, 0, q⁻¹]
    !![-q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2, q⁻¹; -1 + q⁻¹ ^ 2, 0, 0; 0, -1 + q⁻¹ ^ 2, 0]

def Lm_4 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![0, 0, 0; 0, 0, 0; -1 + q⁻¹ ^ 2, q⁻¹, 0]
    !![q⁻¹ ^ 2, 0, 0; 0, -1 + q⁻¹ ^ 2, q⁻¹; 0, 0, 0]
    !![0, 0, 0; q - q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2, 0; q ^ 2 - 2 + q⁻¹ ^ 2, -q + q⁻¹, q⁻¹ ^ 2]
    !![-q⁻¹ ^ 2 + q⁻¹ ^ 4, q - q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2; -q⁻¹ + q⁻¹ ^ 3, 0, 0; 0, q - 2 * q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2]

def Lm_5 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![0, 0, 0; 0, 0, 0; -q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2, q⁻¹]
    !![-q⁻¹ + q⁻¹ ^ 3, q⁻¹ ^ 2, 0; -1 + q⁻¹ ^ 2, 0, q⁻¹ ^ 2; 0, 0, 0]
    !![0, 0, 0; 1 - q⁻¹ ^ 2 + q⁻¹ ^ 4, q - 2 * q⁻¹ + q⁻¹ ^ 3, -1 + q⁻¹ ^ 2; q - 2 * q⁻¹ + q⁻¹ ^ 3, q ^ 2 - 2 + 2 * q⁻¹ ^ 2, -q + q⁻¹]
    !![q - q⁻¹ ^ 3 + q⁻¹ ^ 5, -q⁻¹ ^ 2 + q⁻¹ ^ 4, -q⁻¹ + q⁻¹ ^ 3; 1 - 2 * q⁻¹ ^ 2 + q⁻¹ ^ 4, -q⁻¹ + q⁻¹ ^ 3, 0; q - 2 * q⁻¹ + q⁻¹ ^ 3, 0, -q⁻¹ + q⁻¹ ^ 3]

theorem Lm_2_step (q : R) (hq : q ≠ 0) : s3Inv q * s2Inv q = Lm_2 q := by
  blk6 [s3Inv, s2Inv, Lm_2]

theorem Lm_3_step (q : R) (hq : q ≠ 0) : Lm_2 q * s1Inv q = Lm_3 q := by
  blk6 [Lm_2, s1Inv, Lm_3]

theorem Lm_4_step (q : R) (hq : q ≠ 0) : Lm_3 q * s1Inv q = Lm_4 q := by
  blk6 [Lm_3, s1Inv, Lm_4]

theorem Lm_5_step (q : R) (hq : q ≠ 0) : Lm_4 q * s2Inv q = Lm_5 q := by
  blk6 [Lm_4, s2Inv, Lm_5]

theorem LmX_step (q : R) (hq : q ≠ 0) : Lm_5 q * s3Inv q = LmX q := by
  blk6 [Lm_5, s3Inv, LmX]

theorem Lm_eq (q : R) (hq : q ≠ 0) : Lm q = LmX q := by
  rw [Lm, Lm_2_step q hq, Lm_3_step q hq, Lm_4_step q hq, Lm_5_step q hq, LmX_step q hq]

/-- `A₃₄ = σ₃²`: the lepton loops around quark strand 3. -/
def A34p (q : R) : Matrix Ix Ix R := s3 q * s3 q

/-- Explicit form of `A34p`. -/
def A34pX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1 + q⁻¹ ^ 2, 0, 0; 0, q ^ 2 - 1 + q⁻¹ ^ 2, 0; 0, 0, q ^ 2]
    !![0, q - q⁻¹, 0; 0, 0, q - q⁻¹; 0, 0, 0]
    !![0, 0, 0; q - q⁻¹, 0, 0; 0, q - q⁻¹, 0]
    !![q ^ 2, 0, 0; 0, 1, 0; 0, 0, 1]

theorem A34pX_step (q : R) (hq : q ≠ 0) : s3 q * s3 q = A34pX q := by
  blk6 [s3, s3, A34pX]

theorem A34p_eq (q : R) (hq : q ≠ 0) : A34p q = A34pX q := by
  rw [A34p, A34pX_step q hq]

/-- `A₃₄⁻¹`. -/
def A34m (q : R) : Matrix Ix Ix R := s3Inv q * s3Inv q

/-- Explicit form of `A34m`. -/
def A34mX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![1, 0, 0; 0, 1, 0; 0, 0, q⁻¹ ^ 2]
    !![0, -q + q⁻¹, 0; 0, 0, -q + q⁻¹; 0, 0, 0]
    !![0, 0, 0; -q + q⁻¹, 0, 0; 0, -q + q⁻¹, 0]
    !![q⁻¹ ^ 2, 0, 0; 0, q ^ 2 - 1 + q⁻¹ ^ 2, 0; 0, 0, q ^ 2 - 1 + q⁻¹ ^ 2]

theorem A34mX_step (q : R) (hq : q ≠ 0) : s3Inv q * s3Inv q = A34mX q := by
  blk6 [s3Inv, s3Inv, A34mX]

theorem A34m_eq (q : R) (hq : q ≠ 0) : A34m q = A34mX q := by
  rw [A34m, A34mX_step q hq]

/-- `A₂₄ = σ₃σ₂²σ₃⁻¹`: the lepton loops around quark strand 2. -/
def A24p (q : R) : Matrix Ix Ix R := s3 q * s2 q * s2 q * s3Inv q

/-- Explicit form of `A24p`. -/
def A24pX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1 + q⁻¹ ^ 2, 0, 0; 0, q ^ 2, q - 2 * q⁻¹ + q⁻¹ ^ 3; 0, 0, q ^ 2 - 1 + q⁻¹ ^ 2]
    !![1 - q⁻¹ ^ 2, q - 2 * q⁻¹ + q⁻¹ ^ 3, 0; 0, 0, -q ^ 3 + 2 * q - q⁻¹; 0, 0, q ^ 2 - 1]
    !![q ^ 2 - 1, 0, 0; 0, 0, 0; 0, 0, 1 - q⁻¹ ^ 2]
    !![1, -q ^ 3 + 2 * q - q⁻¹, 0; 0, q ^ 2, 0; 0, 0, 1]

def A24p_2 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1, 0, 0; 0, 0, q - q⁻¹; 0, q, q ^ 2 - 1]
    !![1, q - q⁻¹, 0; 0, 0, q; 0, 0, 0]
    !![0, 0, 0; q, 0, 0; 0, 0, 1]
    !![0, q, 0; 0, 0, 0; 0, 0, 0]

def A24p_3 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 3 - q, 0, 0; 0, q - q⁻¹, q ^ 2 - 2 + q⁻¹ ^ 2; 0, q ^ 2 - 1, q ^ 3 - q + q⁻¹]
    !![q - q⁻¹, q ^ 2 - 1 + q⁻¹ ^ 2, 0; 0, 0, q ^ 2; 0, 0, 0]
    !![0, 0, 0; q ^ 2, 0, 0; 0, 1, q - q⁻¹]
    !![q, q ^ 2 - 1, 0; 0, 0, 0; 0, 0, 0]

theorem A24p_2_step (q : R) (hq : q ≠ 0) : s3 q * s2 q = A24p_2 q := by
  blk6 [s3, s2, A24p_2]

theorem A24p_3_step (q : R) (hq : q ≠ 0) : A24p_2 q * s2 q = A24p_3 q := by
  blk6 [A24p_2, s2, A24p_3]

theorem A24pX_step (q : R) (hq : q ≠ 0) : A24p_3 q * s3Inv q = A24pX q := by
  blk6 [A24p_3, s3Inv, A24pX]

theorem A24p_eq (q : R) (hq : q ≠ 0) : A24p q = A24pX q := by
  rw [A24p, A24p_2_step q hq, A24p_3_step q hq, A24pX_step q hq]

/-- `A₂₄⁻¹`. -/
def A24m (q : R) : Matrix Ix Ix R := s3 q * s2Inv q * s2Inv q * s3Inv q

/-- Explicit form of `A24m`. -/
def A24mX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![1, 0, 0; 0, q⁻¹ ^ 2, -q + 2 * q⁻¹ - q⁻¹ ^ 3; 0, 0, 1]
    !![-1 + q⁻¹ ^ 2, -q + 2 * q⁻¹ - q⁻¹ ^ 3, 0; 0, 0, q ^ 3 - 2 * q + q⁻¹; 0, 0, -q ^ 2 + 1]
    !![-q ^ 2 + 1, 0, 0; 0, 0, 0; 0, 0, -1 + q⁻¹ ^ 2]
    !![q ^ 2 - 1 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹, 0; 0, q⁻¹ ^ 2, 0; 0, 0, q ^ 2 - 1 + q⁻¹ ^ 2]

def A24m_2 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![1 - q⁻¹ ^ 2, 0, 0; 0, -q ^ 2 + 2 - q⁻¹ ^ 2, q - q⁻¹; 0, q, 0]
    !![1, 0, 0; 0, 0, q⁻¹; 0, 0, 0]
    !![0, 0, 0; q⁻¹, 0, 0; 0, -q + q⁻¹, 1]
    !![-q ^ 2 + 1, q, 0; 0, 0, 0; 0, 0, 0]

def A24m_3 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q⁻¹ - q⁻¹ ^ 3, 0, 0; 0, q ^ 3 - 2 * q + 2 * q⁻¹ - q⁻¹ ^ 3, -q ^ 2 + 2 - q⁻¹ ^ 2; 0, -q ^ 2 + 1, q]
    !![-q + q⁻¹, 1, 0; 0, 0, q⁻¹ ^ 2; 0, 0, 0]
    !![0, 0, 0; q⁻¹ ^ 2, 0, 0; 0, q ^ 2 - 1 + q⁻¹ ^ 2, -q + q⁻¹]
    !![q ^ 3 - q + q⁻¹, -q ^ 2 + 1, 0; 0, 0, 0; 0, 0, 0]

theorem A24m_2_step (q : R) (hq : q ≠ 0) : s3 q * s2Inv q = A24m_2 q := by
  blk6 [s3, s2Inv, A24m_2]

theorem A24m_3_step (q : R) (hq : q ≠ 0) : A24m_2 q * s2Inv q = A24m_3 q := by
  blk6 [A24m_2, s2Inv, A24m_3]

theorem A24mX_step (q : R) (hq : q ≠ 0) : A24m_3 q * s3Inv q = A24mX q := by
  blk6 [A24m_3, s3Inv, A24mX]

theorem A24m_eq (q : R) (hq : q ≠ 0) : A24m q = A24mX q := by
  rw [A24m, A24m_2_step q hq, A24m_3_step q hq, A24mX_step q hq]

/-- `A₁₄ = σ₃σ₂σ₁²σ₂⁻¹σ₃⁻¹`: the lepton loops around quark strand 1. -/
def A14p (q : R) : Matrix Ix Ix R := s3 q * s2 q * s1 q * s1 q * s2Inv q * s3Inv q

/-- Explicit form of `A14p`. -/
def A14pX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2, q - 2 * q⁻¹ + q⁻¹ ^ 3, q ^ 2 - 2 + q⁻¹ ^ 2; 0, q ^ 2 - 1 + q⁻¹ ^ 2, 0; 0, 0, q ^ 2 - 1 + q⁻¹ ^ 2]
    !![-q ^ 2 + 2 - q⁻¹ ^ 2, -q ^ 3 + 2 * q - q⁻¹, -q ^ 4 + 2 * q ^ 2 - 2 * q⁻¹ ^ 2 + q⁻¹ ^ 4; q - q⁻¹, 0, q - 2 * q⁻¹ + q⁻¹ ^ 3; 0, q - q⁻¹, q ^ 2 - 2 + q⁻¹ ^ 2]
    !![0, q - q⁻¹, 0; 0, 0, q - q⁻¹; 0, 0, 0]
    !![1, 0, -q ^ 2 + 2 - q⁻¹ ^ 2; 0, 1, -q ^ 3 + 2 * q - q⁻¹; 0, 0, q ^ 2]

def A14p_2 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1, 0, 0; 0, 0, q - q⁻¹; 0, q, q ^ 2 - 1]
    !![1, q - q⁻¹, 0; 0, 0, q; 0, 0, 0]
    !![0, 0, 0; q, 0, 0; 0, 0, 1]
    !![0, q, 0; 0, 0, 0; 0, 0, 0]

def A14p_3 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![0, q ^ 2 - 1, 0; 0, 0, q ^ 2 - 1; q, q ^ 2 - 1, q ^ 3 - q]
    !![q, 0, q - q⁻¹; 0, q, q ^ 2 - 1; 0, 0, 0]
    !![0, 0, 0; 0, q, 0; 0, 0, q]
    !![0, 0, q; 0, 0, 0; 0, 0, 0]

def A14p_4 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1, q ^ 3 - 2 * q + q⁻¹, 0; 0, 0, q ^ 3 - q; q ^ 2 - 1, q ^ 3 - q + q⁻¹, q ^ 4 - q ^ 2]
    !![q ^ 2, q - q⁻¹, q ^ 2 - 2 + q⁻¹ ^ 2; 0, q ^ 2 - 1, q ^ 3 - q + q⁻¹; 0, 0, 0]
    !![0, 0, 0; q, q ^ 2 - 1, 0; 0, 0, q ^ 2]
    !![0, q, q ^ 2 - 1; 0, 0, 0; 0, 0, 0]

def A14p_5 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q - q⁻¹, -q ^ 4 + 3 * q ^ 2 - 3 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹; 0, q ^ 3 - q, 0; q - q⁻¹, q ^ 2 - 2 + q⁻¹ ^ 2, q ^ 3 - q + q⁻¹]
    !![-q ^ 3 + 2 * q - q⁻¹, q ^ 2, q - 2 * q⁻¹ + q⁻¹ ^ 3; q ^ 2 - 1, 0, q ^ 2 - 1 + q⁻¹ ^ 2; 0, 0, 0]
    !![0, 0, 0; 1, -q ^ 3 + 2 * q - q⁻¹, q ^ 2 - 1; 0, q ^ 2, 0]
    !![q, 0, q - q⁻¹; 0, 0, 0; 0, 0, 0]

theorem A14p_2_step (q : R) (hq : q ≠ 0) : s3 q * s2 q = A14p_2 q := by
  blk6 [s3, s2, A14p_2]

theorem A14p_3_step (q : R) (hq : q ≠ 0) : A14p_2 q * s1 q = A14p_3 q := by
  blk6 [A14p_2, s1, A14p_3]

theorem A14p_4_step (q : R) (hq : q ≠ 0) : A14p_3 q * s1 q = A14p_4 q := by
  blk6 [A14p_3, s1, A14p_4]

theorem A14p_5_step (q : R) (hq : q ≠ 0) : A14p_4 q * s2Inv q = A14p_5 q := by
  blk6 [A14p_4, s2Inv, A14p_5]

theorem A14pX_step (q : R) (hq : q ≠ 0) : A14p_5 q * s3Inv q = A14pX q := by
  blk6 [A14p_5, s3Inv, A14pX]

theorem A14p_eq (q : R) (hq : q ≠ 0) : A14p q = A14pX q := by
  rw [A14p, A14p_2_step q hq, A14p_3_step q hq, A14p_4_step q hq, A14p_5_step q hq, A14pX_step q hq]

/-- `A₁₄⁻¹`. -/
def A14m (q : R) : Matrix Ix Ix R := s3 q * s2 q * s1Inv q * s1Inv q * s2Inv q * s3Inv q

/-- Explicit form of `A14m`. -/
def A14mX (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q⁻¹ ^ 2, -q + 2 * q⁻¹ - q⁻¹ ^ 3, -q ^ 2 + 2 - q⁻¹ ^ 2; 0, 1, 0; 0, 0, 1]
    !![q ^ 2 - 2 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹, q ^ 4 - 2 * q ^ 2 + 2 * q⁻¹ ^ 2 - q⁻¹ ^ 4; -q + q⁻¹, 0, -q + 2 * q⁻¹ - q⁻¹ ^ 3; 0, -q + q⁻¹, -q ^ 2 + 2 - q⁻¹ ^ 2]
    !![0, -q + q⁻¹, 0; 0, 0, -q + q⁻¹; 0, 0, 0]
    !![q ^ 2 - 1 + q⁻¹ ^ 2, 0, q ^ 2 - 2 + q⁻¹ ^ 2; 0, q ^ 2 - 1 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹; 0, 0, q⁻¹ ^ 2]

def A14m_2 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 2 - 1, 0, 0; 0, 0, q - q⁻¹; 0, q, q ^ 2 - 1]
    !![1, q - q⁻¹, 0; 0, 0, q; 0, 0, 0]
    !![0, 0, 0; q, 0, 0; 0, 0, 1]
    !![0, q, 0; 0, 0, 0; 0, 0, 0]

def A14m_3 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![-q ^ 3 + 2 * q - q⁻¹, q ^ 2 - 1, 0; 0, 0, 1 - q⁻¹ ^ 2; q, 0, q - q⁻¹]
    !![q⁻¹, -q ^ 2 + 2 - q⁻¹ ^ 2, q - q⁻¹; 0, q, 0; 0, 0, 0]
    !![0, 0, 0; -q ^ 2 + 1, q, 0; 0, 0, q⁻¹]
    !![0, -q ^ 2 + 1, q; 0, 0, 0; 0, 0, 0]

def A14m_4 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 4 - 2 * q ^ 2 + 2 - q⁻¹ ^ 2, -q ^ 3 + 2 * q - q⁻¹, 0; 0, 0, q⁻¹ - q⁻¹ ^ 3; -q ^ 2 + 1, q, 1 - q⁻¹ ^ 2]
    !![q⁻¹ ^ 2, q ^ 3 - 2 * q + 2 * q⁻¹ - q⁻¹ ^ 3, -q ^ 2 + 2 - q⁻¹ ^ 2; 0, -q ^ 2 + 1, q; 0, 0, 0]
    !![0, 0, 0; q ^ 3 - q + q⁻¹, -q ^ 2 + 1, 0; 0, 0, q⁻¹ ^ 2]
    !![0, q ^ 3 - q + q⁻¹, -q ^ 2 + 1; 0, 0, 0; 0, 0, 0]

def A14m_5 (q : R) : Matrix Ix Ix R :=
  fromBlocks
    !![q ^ 3 - 2 * q + 2 * q⁻¹ - q⁻¹ ^ 3, q ^ 4 - 3 * q ^ 2 + 3 - q⁻¹ ^ 2, -q ^ 3 + 2 * q - q⁻¹; 0, q⁻¹ - q⁻¹ ^ 3, 0; -q + q⁻¹, -q ^ 2 + 2 - q⁻¹ ^ 2, q]
    !![q ^ 3 - 2 * q + q⁻¹, q⁻¹ ^ 2, -q + 2 * q⁻¹ - q⁻¹ ^ 3; -q ^ 2 + 1, 0, 1; 0, 0, 0]
    !![0, 0, 0; q ^ 2 - 1 + q⁻¹ ^ 2, q ^ 3 - 2 * q + q⁻¹, -q ^ 2 + 1; 0, q⁻¹ ^ 2, 0]
    !![q ^ 3 - q + q⁻¹, 0, -q + q⁻¹; 0, 0, 0; 0, 0, 0]

theorem A14m_2_step (q : R) (hq : q ≠ 0) : s3 q * s2 q = A14m_2 q := by
  blk6 [s3, s2, A14m_2]

theorem A14m_3_step (q : R) (hq : q ≠ 0) : A14m_2 q * s1Inv q = A14m_3 q := by
  blk6 [A14m_2, s1Inv, A14m_3]

theorem A14m_4_step (q : R) (hq : q ≠ 0) : A14m_3 q * s1Inv q = A14m_4 q := by
  blk6 [A14m_3, s1Inv, A14m_4]

theorem A14m_5_step (q : R) (hq : q ≠ 0) : A14m_4 q * s2Inv q = A14m_5 q := by
  blk6 [A14m_4, s2Inv, A14m_5]

theorem A14mX_step (q : R) (hq : q ≠ 0) : A14m_5 q * s3Inv q = A14mX q := by
  blk6 [A14m_5, s3Inv, A14mX]

theorem A14m_eq (q : R) (hq : q ≠ 0) : A14m q = A14mX q := by
  rw [A14m, A14m_2_step q hq, A14m_3_step q hq, A14m_4_step q hq, A14m_5_step q hq, A14mX_step q hq]
theorem V3B_eq (q : R) (hq : q ≠ 0) : borromeanV3B q = V3BX q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3B, borromeanVB, B₁, B₂Inv, V3BX, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | done | ring1 | (field_simp; ring1)

theorem V3A_eq (q : R) (hq : q ≠ 0) : borromeanV3A q = V3AX q := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [borromeanV3A, borromeanVA, A₁, A₂Inv, V3AX, Matrix.mul_apply, Fin.sum_univ_three] <;>
    first | done | ring1 | (field_simp <;> ring1)

/-! ## 2. `L` commutes with the nucleon braid group -/

theorem Lp_comm_s1 (q : R) (hq : q ≠ 0) : s1 q * Lp q = Lp q * s1 q := by
  rw [Lp_eq q hq]; blk6 [LpX]

theorem Lp_comm_s2 (q : R) (hq : q ≠ 0) : s2 q * Lp q = Lp q * s2 q := by
  rw [Lp_eq q hq]; blk6 [LpX]

/-- Sector traces are invariant under block-diagonal conjugation. -/
theorem trN_conj (g g' gi gi' : Matrix (Fin 3) (Fin 3) R) (hg : gi * g = 1)
    (M : Matrix Ix Ix R) :
    trN (fromBlocks g 0 0 g' * M * fromBlocks gi 0 0 gi') = trN M := by
  rw [← fromBlocks_toBlocks M]
  simp only [trN, fromBlocks_multiply, toBlocks_fromBlocks₁₁, Matrix.zero_mul, Matrix.mul_zero,
    add_zero, zero_add]
  rw [Matrix.trace_mul_cycle, hg, Matrix.one_mul]

theorem trP_conj (g g' gi gi' : Matrix (Fin 3) (Fin 3) R) (hg : gi' * g' = 1)
    (M : Matrix Ix Ix R) :
    trP (fromBlocks g 0 0 g' * M * fromBlocks gi 0 0 gi') = trP M := by
  rw [← fromBlocks_toBlocks M]
  simp only [trP, fromBlocks_multiply, toBlocks_fromBlocks₂₂, Matrix.zero_mul, Matrix.mul_zero,
    add_zero, zero_add]
  rw [Matrix.trace_mul_cycle, hg, Matrix.one_mul]

/-- If `G` commutes with `X`, so does a two-sided inverse of `G`. -/
theorem inv_comm {G Gi X : Matrix Ix Ix R} (h1 : G * Gi = 1) (h2 : Gi * G = 1)
    (hc : G * X = X * G) : Gi * X = X * Gi := by
  calc Gi * X = Gi * X * (G * Gi) := by rw [h1, Matrix.mul_one]
    _ = Gi * (G * X) * Gi := by simp only [Matrix.mul_assoc, hc]
    _ = X * Gi := by rw [← Matrix.mul_assoc, h2, Matrix.one_mul]

/-- **Conjugation invariance of the headline, `N` sector.** For block-diagonal `G` with
inverse `Gi` and `G·X = X·G` (e.g. `X = L` and `G` any word in `σ₁^{±1}, σ₂^{±1}`),
`trN(G M Gi · X) = trN(M · X)`. -/
theorem trN_conj_mul (g g' gi gi' : Matrix (Fin 3) (Fin 3) R) (h1 : g * gi = 1)
    (h1' : g' * gi' = 1) (h2 : gi * g = 1) (h2' : gi' * g' = 1) (M X : Matrix Ix Ix R)
    (hc : fromBlocks g 0 0 g' * X = X * fromBlocks g 0 0 g') :
    trN (fromBlocks g 0 0 g' * M * fromBlocks gi 0 0 gi' * X) = trN (M * X) := by
  have hGi : fromBlocks g 0 0 g' * fromBlocks gi 0 0 gi' = (1 : Matrix Ix Ix R) := by
    rw [fromBlocks_multiply]; simp [h1, h1', fromBlocks_one]
  have hiG : fromBlocks gi 0 0 gi' * fromBlocks g 0 0 g' = (1 : Matrix Ix Ix R) := by
    rw [fromBlocks_multiply]; simp [h2, h2', fromBlocks_one]
  have hc' := inv_comm hGi hiG hc
  rw [Matrix.mul_assoc _ (fromBlocks gi 0 0 gi') X, hc', ← Matrix.mul_assoc,
    Matrix.mul_assoc _ M X, trN_conj g g' gi gi' h2]

theorem trP_conj_mul (g g' gi gi' : Matrix (Fin 3) (Fin 3) R) (h1 : g * gi = 1)
    (h1' : g' * gi' = 1) (h2 : gi * g = 1) (h2' : gi' * g' = 1) (M X : Matrix Ix Ix R)
    (hc : fromBlocks g 0 0 g' * X = X * fromBlocks g 0 0 g') :
    trP (fromBlocks g 0 0 g' * M * fromBlocks gi 0 0 gi' * X) = trP (M * X) := by
  have hGi : fromBlocks g 0 0 g' * fromBlocks gi 0 0 gi' = (1 : Matrix Ix Ix R) := by
    rw [fromBlocks_multiply]; simp [h1, h1', fromBlocks_one]
  have hiG : fromBlocks gi 0 0 gi' * fromBlocks g 0 0 g' = (1 : Matrix Ix Ix R) := by
    rw [fromBlocks_multiply]; simp [h2, h2', fromBlocks_one]
  have hc' := inv_comm hGi hiG hc
  rw [Matrix.mul_assoc _ (fromBlocks gi 0 0 gi') X, hc', ← Matrix.mul_assoc,
    Matrix.mul_assoc _ M X, trP_conj g g' gi gi' h2']

/-! ## 3. `L` on the proton sector -/

theorem Lp_blockP (q : R) (hq : q ≠ 0) : toBlocks₂₂ (Lp q) = q ^ 2 • (1 : Matrix (Fin 3) (Fin 3) R) := by
  rw [Lp_eq q hq]
  ext i j; fin_cases i <;> fin_cases j <;> simp [LpX, toBlocks₂₂, fromBlocks]

theorem trP_V3_Lp_eq (q : R) (hq : q ≠ 0) : trP (V3_4 q * Lp q) = q ^ 2 * trP (V3_4 q) := by
  rw [← fromBlocks_toBlocks (Lp q), V3_4_eq]
  simp only [trP, fromBlocks_multiply, toBlocks_fromBlocks₂₂, Matrix.zero_mul, zero_add]
  rw [Lp_blockP q hq, Matrix.mul_smul, Matrix.mul_one, Matrix.trace_smul,
    smul_eq_mul]

/-! ## 4. Closed forms -/

theorem trN_V3_Lp (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * Lp q) = -((q ^ 16 - 4 * q ^ 14 + 6 * q ^ 12 - 10 * q ^ 10 + 11 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 6) := by
  rw [Lp_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, LpX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_Lp (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * Lp q) = -((q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 4) := by
  rw [Lp_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, LpX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_Lm (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * Lm q) = -((q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 8) := by
  rw [Lm_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, LmX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_Lm (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * Lm q) = -((q ^ 16 - 4 * q ^ 14 + 6 * q ^ 12 - 10 * q ^ 10 + 11 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 10) := by
  rw [Lm_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, LmX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_A34p (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * A34p q) = -((q ^ 16 - 4 * q ^ 14 + 8 * q ^ 12 - 15 * q ^ 10 + 16 * q ^ 8 - 14 * q ^ 6 + 8 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 8) := by
  rw [A34p_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, A34pX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_A34p (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * A34p q) = -((q ^ 14 - 3 * q ^ 12 + 3 * q ^ 10 - 2 * q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 6) := by
  rw [A34p_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, A34pX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_A34m (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * A34m q) = -((q ^ 12 - 4 * q ^ 10 + 7 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 6) := by
  rw [A34m_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, A34mX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_A34m (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * A34m q) = -((q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 8) := by
  rw [A34m_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, A34mX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_A24p (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * A24p q) = -((q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 5 * q ^ 2 + 1) / q ^ 4) := by
  rw [A24p_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, A24pX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_A24p (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * A24p q) = -((q ^ 12 - 4 * q ^ 10 + 6 * q ^ 8 - 10 * q ^ 6 + 7 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 6) := by
  rw [A24p_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, A24pX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_A24m (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * A24m q) = -((q ^ 14 - 3 * q ^ 12 + 3 * q ^ 10 - 3 * q ^ 8 - 2 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 8) := by
  rw [A24m_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, A24mX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_A24m (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * A24m q) = -((q ^ 16 - 4 * q ^ 14 + 8 * q ^ 12 - 14 * q ^ 10 + 16 * q ^ 8 - 15 * q ^ 6 + 8 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 8) := by
  rw [A24m_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, A24mX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_A14p (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * A14p q) = -((q ^ 4 - q ^ 2 + 1) * (q ^ 8 - 3 * q ^ 6 + 3 * q ^ 4 - 5 * q ^ 2 + 1) / q ^ 4) := by
  rw [A14p_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, A14pX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_A14p (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * A14p q) = -((q ^ 12 - 4 * q ^ 10 + 6 * q ^ 8 - 10 * q ^ 6 + 7 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 6) := by
  rw [A14p_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, A14pX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_A14m (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * A14m q) = -((q ^ 14 - 3 * q ^ 12 + 3 * q ^ 10 - 3 * q ^ 8 - 2 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1) / q ^ 8) := by
  rw [A14m_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, A14mX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_A14m (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * A14m q) = -((q ^ 16 - 4 * q ^ 14 + 8 * q ^ 12 - 14 * q ^ 10 + 16 * q ^ 8 - 15 * q ^ 6 + 8 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 8) := by
  rw [A14m_eq q hq, V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, A14mX, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_s3 (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * s3 q) = -((q ^ 3 - q ^ 2 + 1) * (q ^ 3 + q ^ 2 - 1) * (q ^ 8 - 3 * q ^ 6 + 2 * q ^ 4 - 2 * q ^ 2 + 1) / q ^ 7) := by
  rw [V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, s3, E, Et, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_s3 (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * s3 q) = -(q * (q ^ 2 - 2) * (q ^ 4 - q ^ 2 + 1)) := by
  rw [V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, s3, E, Et, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trN_V3_s3Inv (q : R) (hq : q ≠ 0) :
    trN (V3_4 q * s3Inv q) = -((q ^ 6 - 3 * q ^ 4 + 2 * q ^ 2 - 1) / q ^ 3) := by
  rw [V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trN, s3Inv, E, Et, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

theorem trP_V3_s3Inv (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * s3Inv q) = -((q ^ 12 - 3 * q ^ 10 + 6 * q ^ 8 - 8 * q ^ 6 + 6 * q ^ 4 - 4 * q ^ 2 + 1) / q ^ 7) := by
  rw [V3_4_eq, V3B_eq q hq, V3A_eq q hq]
  simp [trP, s3Inv, E, Et, V3BX, V3AX, fromBlocks_multiply, Matrix.trace_fin_three]
  field_simp
  ring

/-! ## 5. Headline ratio and chirality -/

/-- The spectator polynomial: `tr V³ = −S/q⁶` on either sector. -/
def polyS (q : R) : R := q ^ 12 - 3 * q ^ 10 + 3 * q ^ 8 - 5 * q ^ 6 + 3 * q ^ 4 - 3 * q ^ 2 + 1

/-- The lepton-loop polynomial. -/
def polyL (q : R) : R :=
  q ^ 16 - 4 * q ^ 14 + 6 * q ^ 12 - 10 * q ^ 10 + 11 * q ^ 8 - 10 * q ^ 6 + 6 * q ^ 4 -
    4 * q ^ 2 + 1

theorem div_aux₁ (a b q : R) (hq : q ≠ 0) : -(a / q ^ 4) / -(b / q ^ 6) = q ^ 2 * a / b := by
  rw [neg_div_neg_eq, div_div_div_eq, show a * q ^ 6 = q ^ 2 * a * q ^ 4 by ring,
    show q ^ 4 * b = b * q ^ 4 by ring, mul_div_mul_right _ _ (pow_ne_zero 4 hq)]

theorem div_aux₂ (a b q : R) (hq : q ≠ 0) : -(a / q ^ 10) / -(b / q ^ 8) = a / (q ^ 2 * b) := by
  rw [neg_div_neg_eq, div_div_div_eq, show q ^ 10 * b = q ^ 2 * b * q ^ 8 by ring,
    mul_div_mul_right _ _ (pow_ne_zero 8 hq)]

/-- **Headline ratio.** `trP(V³L)/trN(V³L) = q²S/Λ`. -/
theorem ratio_Lp (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * Lp q) / trN (V3_4 q * Lp q) = q ^ 2 * polyS q / polyL q := by
  rw [trP_V3_Lp q hq, trN_V3_Lp q hq]
  exact div_aux₁ _ _ q hq

/-- The mirror word. -/
theorem ratio_Lm (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * Lm q) / trN (V3_4 q * Lm q) = polyL q / (q ^ 2 * polyS q) := by
  rw [trP_V3_Lm q hq, trN_V3_Lm q hq]
  exact div_aux₂ _ _ q hq

/-- **Chirality.** The mirror word `L⁻¹` gives exactly the reciprocal ratio: the split changes
sign and keeps its magnitude. -/
theorem ratio_Lm_eq_inv (q : R) (hq : q ≠ 0) :
    trP (V3_4 q * Lm q) / trN (V3_4 q * Lm q) =
      (trP (V3_4 q * Lp q) / trN (V3_4 q * Lp q))⁻¹ := by
  rw [ratio_Lm q hq, ratio_Lp q hq, inv_div]

end QOU.Nuclear.NucleonSplitFourStrand
