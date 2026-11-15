/-
# Exact `Jb` traces of the six mixed-site γγ words (generic field)

Bean `qou-a1hh`. Companion to `GammaGammaFourStrandFlavour.lean` (PR #7950), on the explicit `(3,1)`
representation of `H₄(q)` from `FlavourDoubletFourStrands.lean` (PR #7957).

At m = 6 exactly six γγ words pass reading 3 without being pure braids. For each of them:
* over any field, `tr(Jb · w · Jb)` is an explicit rational function of `q` (`mixedN_trace`);
* over `ℝ`, it is **negative for `1 ≤ q ≤ 113/100`**, an interval containing the proton
  `q₀ ≈ 1.10998` (`mixedN_Jb_trace_neg`). The sign comes from one polynomial per word, bounded
  after the substitution `q = 1 + t`, `0 ≤ t ≤ 13/100`.

Archimedean statements (ordering on `ℝ`) sit after the substrate→archimedean wall, in the second section.
No empirical number enters: `113/100` is a chosen interval, not a fitted value.
No `sorry`, no axiom, no `native_decide`, no class.

-- Ref: [humphreys1990] §7.4 (Hecke algebra, generic q)
-/
import QOU.QuarkState.GammaGammaFourStrandFlavour
import Mathlib.LinearAlgebra.Matrix.Trace

namespace QOU.QuarkState.GammaGammaFourStrand

open Matrix QOU.QuarkState.FlavourDoubletFour

local macro "mat3" : tactic =>
  `(tactic| ((try simp only [Matrix.mul_fin_three, Matrix.one_fin_three, Matrix.smul_of,
      Matrix.smul_vec3, Matrix.of_sub_of, Matrix.of_add_of]) <;> ext i j <;>
    fin_cases i <;> fin_cases j <;> (try simp) <;> (try field_simp) <;> (try ring) <;> (try simp)))

section Generic
variable {K : Type*} [Field K]

/-- `B0.V1.B0.V1.B1.V0` -/
def mixed1 (q : K) : Matrix (Fin 3) (Fin 3) K := B0 q * V1 q * B0 q * V1 q * B1 q * V0 q

/-- `B0.V1.B1.V0.B0.V1` -/
def mixed2 (q : K) : Matrix (Fin 3) (Fin 3) K := B0 q * V1 q * B1 q * V0 q * B0 q * V1 q

/-- `V1.B0.V1.B1.V0.B0` -/
def mixed3 (q : K) : Matrix (Fin 3) (Fin 3) K := V1 q * B0 q * V1 q * B1 q * V0 q * B0 q

/-- `V1.B1.V0.B0.V1.B0` -/
def mixed4 (q : K) : Matrix (Fin 3) (Fin 3) K := V1 q * B1 q * V0 q * B0 q * V1 q * B0 q

/-- `B1.V0.B0.V1.B0.V1` -/
def mixed5 (q : K) : Matrix (Fin 3) (Fin 3) K := B1 q * V0 q * B0 q * V1 q * B0 q * V1 q

/-- `B1.V0.B1.V0.B1.V0` -/
def mixed6 (q : K) : Matrix (Fin 3) (Fin 3) K := B1 q * V0 q * B1 q * V0 q * B1 q * V0 q

section
variable {q : K} (hq : q ≠ 0) (hn : q ^ 2 + 1 ≠ 0) (hD : q ^ 4 + q ^ 2 + 1 ≠ 0)
include hq hn hD

set_option maxHeartbeats 4000000 in
theorem mixed1_p2 : B0 q * V1 q =
    !![(2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1));
     (1 - q^2) / (q^2*(q^2 + 1)), (-q^4 - 1) / (q^2 + 1), (q^2 - 1) / (q^2 + 1);
     (1 - q^2) / (q^2*(q^2 + 1)), (q^2 - 1) / (q^2 + 1), (-q^4 - 1) / (q^2 + 1)] := by
  rw [B0_eq hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed1_p3 : B0 q * V1 q * B0 q =
    !![(-2*q^8 + 4*q^6 - 4*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (q^10 - 3*q^8 + 3*q^6 - 4*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1)), (-q^10 + 3*q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1));
     (q^6 - 2*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1)), (-q^8 + q^6 - 2*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1));
     (q^6 - 2*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1)), (2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1))] := by
  rw [mixed1_p2 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed1_p4 : B0 q * V1 q * B0 q * V1 q =
    !![(-2*q^10 + 6*q^8 - 6*q^6 + 6*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1)), (-q^12 + 3*q^10 - 5*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (-q^12 + 3*q^10 - 5*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1));
     (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1)), (q^10 - q^8 + 3*q^6 - 3*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1)), (-2*q^8 + 3*q^6 - 3*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1));
     (q^8 - 3*q^6 + 4*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1)), (-2*q^8 + 3*q^6 - 3*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1)), (q^10 - q^8 + 3*q^6 - 3*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1))] := by
  rw [mixed1_p3 hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed1_p5 : B0 q * V1 q * B0 q * V1 q * B1 q =
    !![(q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (2*q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 1) / (q^10*(q^2 + 1)), (-q^10 + 2*q^8 - 2*q^6 + 3*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (-q^6 + q^4 - 2*q^2 + 1) / (q^2 + 1), (-q^6 + q^4 - 2*q^2 + 1) / (q^8*(q^2 + 1)), (q^8 - q^6 + q^4 - q^2 + 1) / (q^2 + 1);
     (2*q^4 - 2*q^2 + 1) / (q^2 + 1), (-q^6 + q^4 - 2*q^2 + 1) / (q^8*(q^2 + 1)), (-q^6 + 2*q^4 - q^2 + 1) / (q^2 + 1)] := by
  rw [mixed1_p4 hq hn hD, B1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed1_p6 : B0 q * V1 q * B0 q * V1 q * B1 q * V0 q =
    !![(-q^16 + 5*q^14 - 10*q^12 + 13*q^10 - 14*q^8 + 10*q^6 - 7*q^4 + 3*q^2 - 1) / (q^8*(q^2 + 1)), (-q^18 + 4*q^16 - 7*q^14 + 10*q^12 - 12*q^10 + 11*q^8 - 9*q^6 + 6*q^4 - 3*q^2 + 1) / (q^10*(q^2 + 1)), (q^16 - 4*q^14 + 8*q^12 - 12*q^10 + 14*q^8 - 12*q^6 + 8*q^4 - 4*q^2 + 1) / (q^6*(q^2 + 1));
     (q^14 - 3*q^12 + 5*q^10 - 7*q^8 + 7*q^6 - 5*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (q^16 - 2*q^14 + 4*q^12 - 5*q^10 + 6*q^8 - 6*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1)), (-q^14 + 2*q^12 - 5*q^10 + 6*q^8 - 7*q^6 + 6*q^4 - 4*q^2 + 1) / (q^4*(q^2 + 1));
     (-2*q^12 + 6*q^10 - 8*q^8 + 7*q^6 - 5*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (-2*q^14 + 4*q^12 - 6*q^10 + 6*q^8 - 6*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1)), (2*q^12 - 4*q^10 + 7*q^8 - 8*q^6 + 6*q^4 - 4*q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [mixed1_p5 hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed1_trace : Matrix.trace (Jb q * mixed1 q * Jb q) =
    (q^4 + 1)*(2*q^10 - 3*q^8 + 3*q^6 - 4*q^4 + 2*q^2 - 2) / ((q^4 + q^2 + 1)*q^4*(q^2 + 1)) := by
  have := D_ne' hD; have := D_ne'' hD
  unfold mixed1; rw [mixed1_p6 hq hn hD]; unfold Jb
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

set_option maxHeartbeats 4000000 in
theorem mixed2_p2 : B0 q * V1 q =
    !![(2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1));
     (1 - q^2) / (q^2*(q^2 + 1)), (-q^4 - 1) / (q^2 + 1), (q^2 - 1) / (q^2 + 1);
     (1 - q^2) / (q^2*(q^2 + 1)), (q^2 - 1) / (q^2 + 1), (-q^4 - 1) / (q^2 + 1)] := by
  rw [B0_eq hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed2_p3 : B0 q * V1 q * B1 q =
    !![(-q^4 + q^2) / (q^2 + 1), (q^4 + 1) / (q^6*(q^2 + 1)), (q^6 + q^2) / (q^2 + 1);
     (q^4) / (q^2 + 1), (1) / (q^4*(q^2 + 1)), (-q^6) / (q^2 + 1);
     (-q^2) / (q^2 + 1), (1) / (q^4*(q^2 + 1)), (-q^2) / (q^2 + 1)] := by
  rw [mixed2_p2 hq hn hD, B1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed2_p4 : B0 q * V1 q * B1 q * V0 q =
    !![(q^10 - 3*q^8 + 3*q^6 - 3*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (q^12 - 2*q^10 + 2*q^8 - 3*q^6 + 2*q^4 - q^2 + 1) / (q^6*(q^2 + 1)), (-q^10 + 2*q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1));
     (-q^8 + 2*q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^10 + q^8 - q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - q^2 + 1) / (q^2 + 1);
     (q^6 - 2*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - 2*q^2 + 2) / (q^2 + 1)] := by
  rw [mixed2_p3 hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed2_p5 : B0 q * V1 q * B1 q * V0 q * B0 q =
    !![(q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^12 - 2*q^10 + 3*q^8 - 3*q^6 + 3*q^4 - q^2 + 1) / (q^6*(q^2 + 1)), (q^10 - 2*q^8 + 3*q^6 - 4*q^4 + 2*q^2 - 2) / (q^2 + 1);
     (-q^8 + 2*q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^10 + q^8 - 2*q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + q^8 - 2*q^6 + 2*q^4 - q^2) / (q^2 + 1);
     (q^6 - 2*q^4 + 2*q^2 - 2) / (q^2*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - 2*q^2 + 1) / (q^2 + 1)] := by
  rw [mixed2_p4 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed2_p6 : B0 q * V1 q * B1 q * V0 q * B0 q * V1 q =
    !![(q^10 - 3*q^8 + 4*q^6 - 4*q^4 + 2*q^2 - 2) / (q^4*(q^2 + 1)), (-q^12 + 2*q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^12 - 2*q^10 + 3*q^8 - 4*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1));
     (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (q^10 - q^8 + 2*q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^10 + q^8 - 2*q^6 + 2*q^4 - 2*q^2) / (q^2 + 1);
     (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^8 + q^6 - 2*q^4 + 2*q^2 - 2) / (q^2*(q^2 + 1)), (q^10 - q^8 + 2*q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [mixed2_p5 hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed2_trace : Matrix.trace (Jb q * mixed2 q * Jb q) =
    (q^4 + 1)*(q^6 - q^4 - 2) / ((q^4 + q^2 + 1)*q^4*(q^2 + 1)) := by
  have := D_ne' hD; have := D_ne'' hD
  unfold mixed2; rw [mixed2_p6 hq hn hD]; unfold Jb
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

set_option maxHeartbeats 4000000 in
theorem mixed3_p2 : V1 q * B0 q =
    !![(-2*q^6 + 2*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1));
     (q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^6 + q^4 - q^2 + 1) / (q^2*(q^2 + 1)), (-2*q^4 + q^2 - 1) / (q^2 + 1);
     (-q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-2*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - q^2 + 1) / (q^2*(q^2 + 1))] := by
  rw [V1_eq hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed3_p3 : V1 q * B0 q * V1 q =
    !![(-2*q^8 + 4*q^6 - 4*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (-q^10 + 2*q^8 - 4*q^6 + 3*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + 2*q^8 - 4*q^6 + 3*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1));
     (q^6 - 3*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1));
     (-q^6 + 3*q^4 - 2*q^2 + 1) / (q^6*(q^2 + 1)), (2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-q^8 + q^6 - 2*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1))] := by
  rw [mixed3_p2 hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed3_p4 : V1 q * B0 q * V1 q * B1 q =
    !![(q^6 - 2*q^4 + 2*q^2 - 1) / (q^2 + 1), (2*q^6 - q^4 + 2*q^2 - 1) / (q^8*(q^2 + 1)), (-q^8 + q^6 - 2*q^4 + q^2 - 1) / (q^2 + 1);
     (-q^6 + q^4 - q^2) / (q^2 + 1), (-q^4 + q^2 - 1) / (q^6*(q^2 + 1)), (q^8 - q^6 - q^2) / (q^2 + 1);
     (1 - 2*q^2) / (q^2 + 1), (q^4 - q^2 + 1) / (q^8*(q^2 + 1)), (q^4 - q^2 + 1) / (q^2 + 1)] := by
  rw [mixed3_p3 hq hn hD, B1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed3_p5 : V1 q * B0 q * V1 q * B1 q * V0 q =
    !![(-q^14 + 4*q^12 - 7*q^10 + 9*q^8 - 8*q^6 + 5*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1)), (-q^16 + 3*q^14 - 5*q^12 + 7*q^10 - 7*q^8 + 7*q^6 - 4*q^4 + 3*q^2 - 1) / (q^8*(q^2 + 1)), (q^14 - 3*q^12 + 6*q^10 - 8*q^8 + 9*q^6 - 6*q^4 + 4*q^2 - 1) / (q^4*(q^2 + 1));
     (q^12 - 3*q^10 + 4*q^8 - 4*q^6 + 4*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (q^14 - 2*q^12 + 3*q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1)), (-q^12 + 2*q^10 - 4*q^8 + 4*q^6 - 4*q^4 + 3*q^2 - 1) / (q^2*(q^2 + 1));
     (2*q^10 - 5*q^8 + 5*q^6 - 4*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1)), (2*q^12 - 3*q^10 + 4*q^8 - 4*q^6 + 3*q^4 - 2*q^2 + 1) / (q^8*(q^2 + 1)), (-2*q^10 + 3*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [mixed3_p4 hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed3_p6 : V1 q * B0 q * V1 q * B1 q * V0 q * B0 q =
    !![(-q^14 + 4*q^12 - 8*q^10 + 10*q^8 - 10*q^6 + 6*q^4 - 4*q^2 + 1) / (q^6*(q^2 + 1)), (-q^16 + 3*q^14 - 6*q^12 + 8*q^10 - 9*q^8 + 8*q^6 - 5*q^4 + 3*q^2 - 1) / (q^8*(q^2 + 1)), (-q^14 + 3*q^12 - 6*q^10 + 9*q^8 - 10*q^6 + 8*q^4 - 5*q^2 + 2) / (q^2*(q^2 + 1));
     (q^12 - 3*q^10 + 5*q^8 - 5*q^6 + 4*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (q^14 - 2*q^12 + 4*q^10 - 4*q^8 + 4*q^6 - 4*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1)), (q^12 - 2*q^10 + 4*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 2) / (q^2 + 1);
     (2*q^10 - 5*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (2*q^12 - 3*q^10 + 5*q^8 - 5*q^6 + 4*q^4 - 2*q^2 + 1) / (q^8*(q^2 + 1)), (2*q^10 - 3*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 2) / (q^2*(q^2 + 1))] := by
  rw [mixed3_p5 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed3_trace : Matrix.trace (Jb q * mixed3 q * Jb q) =
    (q^14 - 2*q^12 + 4*q^10 - 5*q^8 + 3*q^6 - 5*q^4 + q^2 - 1) / ((q^4 + q^2 + 1)*q^4*(q^2 + 1)) := by
  have := D_ne' hD; have := D_ne'' hD
  unfold mixed3; rw [mixed3_p6 hq hn hD]; unfold Jb
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

set_option maxHeartbeats 4000000 in
theorem mixed4_p2 : V1 q * B1 q =
    !![(-q^4 + q^2) / (q^2 + 1), (-q^4 - 1) / (q^4*(q^2 + 1)), (q^6 + q^2) / (q^2 + 1);
     (q^4) / (q^2 + 1), (-1) / (q^2*(q^2 + 1)), (-q^6) / (q^2 + 1);
     (1) / (q^2 + 1), (1) / (q^4*(q^2 + 1)), (1) / (q^2 + 1)] := by
  rw [V1_eq hq hn hD, B1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed4_p3 : V1 q * B1 q * V0 q =
    !![(q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (q^10 - 2*q^8 + 2*q^6 - 3*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (-q^8 + 2*q^6 - 3*q^4 + 2*q^2 - 2) / (q^2 + 1);
     (-q^6 + 2*q^4 - q^2 + 1) / (q^2 + 1), (-q^8 + q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - q^2) / (q^2 + 1);
     (-q^4 + 2*q^2 - 2) / (q^2*(q^2 + 1)), (-q^6 + q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (q^6 - q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [mixed4_p2 hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed4_p4 : V1 q * B1 q * V0 q * B0 q =
    !![(q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 2) / (q^2*(q^2 + 1)), (q^10 - 2*q^8 + 3*q^6 - 3*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^10 - 2*q^8 + 3*q^6 - 3*q^4 + 2*q^2 - 1) / (q^2 + 1);
     (-q^6 + 2*q^4 - 2*q^2 + 1) / (q^2 + 1), (-q^8 + q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^10 + q^8 - 2*q^6 + 2*q^4) / (q^2 + 1);
     (-q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - 2*q^2 + 2) / (q^4*(q^2 + 1)), (-q^8 + q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [mixed4_p3 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed4_p5 : V1 q * B1 q * V0 q * B0 q * V1 q =
    !![(q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (-q^10 + 2*q^8 - 3*q^6 + 4*q^4 - 2*q^2 + 2) / (q^2*(q^2 + 1)), (q^12 - 2*q^10 + 3*q^8 - 3*q^6 + 3*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (-q^6 + 2*q^4 - 2*q^2 + 2) / (q^2 + 1), (q^8 - q^6 + 2*q^4 - 2*q^2 + 1) / (q^2 + 1), (-q^10 + q^8 - 2*q^6 + 2*q^4 - q^2) / (q^2 + 1);
     (-q^8 + 2*q^6 - 2*q^4 + q^2 - 1) / (q^6*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + q^8 - 2*q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [mixed4_p4 hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed4_p6 : V1 q * B1 q * V0 q * B0 q * V1 q * B0 q =
    !![(-q^14 + 4*q^12 - 8*q^10 + 10*q^8 - 10*q^6 + 6*q^4 - 4*q^2 + 1) / (q^6*(q^2 + 1)), (-2*q^14 + 5*q^12 - 8*q^10 + 10*q^8 - 9*q^6 + 6*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1)), (-q^16 + 3*q^14 - 6*q^12 + 8*q^10 - 9*q^8 + 8*q^6 - 5*q^4 + 3*q^2 - 1) / (q^4*(q^2 + 1));
     (q^10 - 3*q^8 + 5*q^6 - 6*q^4 + 5*q^2 - 2) / (q^2*(q^2 + 1)), (2*q^10 - 3*q^8 + 5*q^6 - 6*q^4 + 4*q^2 - 2) / (q^2*(q^2 + 1)), (q^12 - 2*q^10 + 4*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 2) / (q^2 + 1);
     (q^12 - 3*q^10 + 5*q^8 - 5*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1)), (2*q^12 - 3*q^10 + 5*q^8 - 5*q^6 + 4*q^4 - 2*q^2 + 1) / (q^8*(q^2 + 1)), (q^14 - 2*q^12 + 4*q^10 - 4*q^8 + 4*q^6 - 4*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1))] := by
  rw [mixed4_p5 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed4_trace : Matrix.trace (Jb q * mixed4 q * Jb q) =
    (q^16 - q^14 + 2*q^12 - 4*q^10 + 3*q^8 - 5*q^6 + 2*q^4 - 3*q^2 + 1) / ((q^4 + q^2 + 1)*q^6*(q^2 + 1)) := by
  have := D_ne' hD; have := D_ne'' hD
  unfold mixed4; rw [mixed4_p6 hq hn hD]; unfold Jb
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

set_option maxHeartbeats 4000000 in
theorem mixed5_p2 : B1 q * V0 q =
    !![(q^6 - 3*q^4 + 2*q^2 - 2) / (q^2 + 1), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2 + 1);
     (q^4 - 2*q^2 + 1) / (q^2 + 1), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^6 + q^4 - 2*q^2) / (q^2 + 1);
     (-q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (-q^4 + q^2 - 2) / (q^2*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [B1_eq hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed5_p3 : B1 q * V0 q * B0 q =
    !![(q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (q^8 - 2*q^6 + 3*q^4 - 2*q^2 + 2) / (q^2*(q^2 + 1)), (q^10 - 2*q^8 + 2*q^6 - 3*q^4 + q^2 - 1) / (q^2 + 1);
     (q^4 - 2*q^2 + 2) / (q^2 + 1), (q^6 - q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - q^2) / (q^2 + 1);
     (-q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (-q^6 + q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^8 + q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [mixed5_p2 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed5_p4 : B1 q * V0 q * B0 q * V1 q =
    !![(q^10 - 3*q^8 + 3*q^6 - 3*q^4 + q^2 - 1) / (q^4*(q^2 + 1)), (-q^10 + 2*q^8 - 3*q^6 + 3*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (q^12 - 2*q^10 + 2*q^8 - 3*q^6 + 2*q^4 - q^2 + 1) / (q^2*(q^2 + 1));
     (q^6 - 2*q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (-q^6 + q^4 - 2*q^2 + 2) / (q^2 + 1), (q^8 - q^6 + 2*q^4 - q^2 + 1) / (q^2 + 1);
     (-q^8 + 2*q^6 - q^4 + q^2 - 1) / (q^6*(q^2 + 1)), (q^8 - q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + q^8 - q^6 + q^4 - q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [mixed5_p3 hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed5_p5 : B1 q * V0 q * B0 q * V1 q * B0 q =
    !![(-q^14 + 4*q^12 - 7*q^10 + 9*q^8 - 8*q^6 + 5*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1)), (-2*q^14 + 5*q^12 - 7*q^10 + 9*q^8 - 7*q^6 + 5*q^4 - 2*q^2 + 1) / (q^6*(q^2 + 1)), (-q^16 + 3*q^14 - 5*q^12 + 7*q^10 - 8*q^8 + 6*q^6 - 5*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1));
     (-q^10 + 3*q^8 - 5*q^6 + 5*q^4 - 4*q^2 + 1) / (q^4*(q^2 + 1)), (-2*q^10 + 3*q^8 - 5*q^6 + 5*q^4 - 3*q^2 + 1) / (q^4*(q^2 + 1)), (-q^12 + 2*q^10 - 4*q^8 + 4*q^6 - 4*q^4 + 3*q^2 - 1) / (q^2*(q^2 + 1));
     (q^12 - 3*q^10 + 4*q^8 - 4*q^6 + 3*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1)), (2*q^12 - 3*q^10 + 4*q^8 - 4*q^6 + 3*q^4 - 2*q^2 + 1) / (q^8*(q^2 + 1)), (q^14 - 2*q^12 + 3*q^10 - 3*q^8 + 4*q^6 - 3*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1))] := by
  rw [mixed5_p4 hq hn hD, B0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed5_p6 : B1 q * V0 q * B0 q * V1 q * B0 q * V1 q =
    !![(-q^16 + 5*q^14 - 10*q^12 + 13*q^10 - 14*q^8 + 10*q^6 - 7*q^4 + 3*q^2 - 1) / (q^8*(q^2 + 1)), (2*q^16 - 6*q^14 + 10*q^12 - 13*q^10 + 13*q^8 - 10*q^6 + 6*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1)), (-q^18 + 3*q^16 - 6*q^14 + 10*q^12 - 12*q^10 + 12*q^8 - 10*q^6 + 6*q^4 - 3*q^2 + 1) / (q^6*(q^2 + 1));
     (-q^12 + 4*q^10 - 7*q^8 + 8*q^6 - 7*q^4 + 4*q^2 - 1) / (q^6*(q^2 + 1)), (2*q^12 - 4*q^10 + 7*q^8 - 8*q^6 + 6*q^4 - 4*q^2 + 1) / (q^4*(q^2 + 1)), (-q^14 + 2*q^12 - 5*q^10 + 6*q^8 - 7*q^6 + 6*q^4 - 4*q^2 + 1) / (q^4*(q^2 + 1));
     (q^14 - 4*q^12 + 6*q^10 - 6*q^8 + 6*q^6 - 5*q^4 + 3*q^2 - 1) / (q^10*(q^2 + 1)), (-2*q^14 + 4*q^12 - 6*q^10 + 6*q^8 - 6*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1)), (q^16 - 2*q^14 + 4*q^12 - 5*q^10 + 6*q^8 - 6*q^6 + 4*q^4 - 3*q^2 + 1) / (q^8*(q^2 + 1))] := by
  rw [mixed5_p5 hq hn hD, V1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed5_trace : Matrix.trace (Jb q * mixed5 q * Jb q) =
    (q^4 + 1)*(q^16 - 2*q^12 + 4*q^10 - 5*q^8 + q^6 - 2*q^4 + 2*q^2 - 1) / ((q^4 + q^2 + 1)*q^8*(q^2 + 1)) := by
  have := D_ne' hD; have := D_ne'' hD
  unfold mixed5; rw [mixed5_p6 hq hn hD]; unfold Jb
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

set_option maxHeartbeats 4000000 in
theorem mixed6_p2 : B1 q * V0 q =
    !![(q^6 - 3*q^4 + 2*q^2 - 2) / (q^2 + 1), (q^8 - 2*q^6 + 2*q^4 - 2*q^2 + 1) / (q^2*(q^2 + 1)), (-q^8 + 2*q^6 - 2*q^4 + 2*q^2 - 1) / (q^2 + 1);
     (q^4 - 2*q^2 + 1) / (q^2 + 1), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1)), (-q^6 + q^4 - 2*q^2) / (q^2 + 1);
     (-q^4 + 2*q^2 - 1) / (q^2*(q^2 + 1)), (-q^4 + q^2 - 2) / (q^2*(q^2 + 1)), (q^6 - q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [B1_eq hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed6_p3 : B1 q * V0 q * B1 q =
    !![(-q^8 + 3*q^6 - 4*q^4 + 4*q^2 - 2) / (q^2 + 1), (q^10 - 3*q^8 + 3*q^6 - 4*q^4 + 2*q^2 - 1) / (q^4*(q^2 + 1)), (q^10 - 3*q^8 + 3*q^6 - 4*q^4 + 2*q^2 - 1) / (q^2 + 1);
     (-q^6 + 2*q^4 - 3*q^2 + 1) / (q^2 + 1), (q^8 - 2*q^6 + 2*q^4 - q^2 + 1) / (q^4*(q^2 + 1)), (q^8 - 2*q^6 + 2*q^4 - 2*q^2) / (q^2 + 1);
     (q^6 - 2*q^4 + 3*q^2 - 1) / (q^2*(q^2 + 1)), (-q^6 + 2*q^4 - 2*q^2 + 2) / (q^4*(q^2 + 1)), (-q^8 + 2*q^6 - 2*q^4 + q^2 - 1) / (q^2*(q^2 + 1))] := by
  rw [mixed6_p2 hq hn hD, B1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed6_p4 : B1 q * V0 q * B1 q * V0 q =
    !![(q^12 - 5*q^10 + 10*q^8 - 12*q^6 + 12*q^4 - 6*q^2 + 2) / (q^2*(q^2 + 1)), (q^14 - 4*q^12 + 8*q^10 - 11*q^8 + 11*q^6 - 8*q^4 + 4*q^2 - 1) / (q^4*(q^2 + 1)), (-q^14 + 4*q^12 - 8*q^10 + 11*q^8 - 11*q^6 + 8*q^4 - 4*q^2 + 1) / (q^2*(q^2 + 1));
     (q^10 - 4*q^8 + 7*q^6 - 7*q^4 + 4*q^2 - 1) / (q^2*(q^2 + 1)), (q^12 - 3*q^10 + 6*q^8 - 6*q^6 + 5*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + 3*q^8 - 6*q^6 + 6*q^4 - 5*q^2 + 3) / (q^2 + 1);
     (-q^10 + 4*q^8 - 7*q^6 + 7*q^4 - 4*q^2 + 1) / (q^4*(q^2 + 1)), (-q^10 + 3*q^8 - 6*q^6 + 6*q^4 - 5*q^2 + 3) / (q^4*(q^2 + 1)), (q^12 - 3*q^10 + 6*q^8 - 6*q^6 + 5*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [mixed6_p3 hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed6_p5 : B1 q * V0 q * B1 q * V0 q * B1 q =
    !![(-q^14 + 5*q^12 - 12*q^10 + 18*q^8 - 20*q^6 + 16*q^4 - 8*q^2 + 2) / (q^2*(q^2 + 1)), (q^16 - 5*q^14 + 11*q^12 - 16*q^10 + 19*q^8 - 15*q^6 + 10*q^4 - 4*q^2 + 1) / (q^6*(q^2 + 1)), (q^16 - 5*q^14 + 11*q^12 - 16*q^10 + 19*q^8 - 15*q^6 + 10*q^4 - 4*q^2 + 1) / (q^2*(q^2 + 1));
     (-q^12 + 4*q^10 - 9*q^8 + 11*q^6 - 10*q^4 + 5*q^2 - 1) / (q^2*(q^2 + 1)), (q^14 - 4*q^12 + 8*q^10 - 10*q^8 + 9*q^6 - 6*q^4 + 2*q^2 - 1) / (q^6*(q^2 + 1)), (q^12 - 4*q^10 + 8*q^8 - 10*q^6 + 9*q^4 - 6*q^2 + 3) / (q^2 + 1);
     (q^12 - 4*q^10 + 9*q^8 - 11*q^6 + 10*q^4 - 5*q^2 + 1) / (q^4*(q^2 + 1)), (-q^12 + 4*q^10 - 8*q^8 + 10*q^6 - 9*q^4 + 6*q^2 - 3) / (q^6*(q^2 + 1)), (-q^14 + 4*q^12 - 8*q^10 + 10*q^8 - 9*q^6 + 6*q^4 - 2*q^2 + 1) / (q^4*(q^2 + 1))] := by
  rw [mixed6_p4 hq hn hD, B1_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed6_p6 : B1 q * V0 q * B1 q * V0 q * B1 q * V0 q =
    !![(q^18 - 7*q^16 + 22*q^14 - 42*q^12 + 58*q^10 - 62*q^8 + 48*q^6 - 28*q^4 + 10*q^2 - 2) / (q^4*(q^2 + 1)), (q^20 - 6*q^18 + 18*q^16 - 35*q^14 + 51*q^12 - 58*q^10 + 51*q^8 - 35*q^6 + 18*q^4 - 6*q^2 + 1) / (q^6*(q^2 + 1)), (-q^20 + 6*q^18 - 18*q^16 + 35*q^14 - 51*q^12 + 58*q^10 - 51*q^8 + 35*q^6 - 18*q^4 + 6*q^2 - 1) / (q^4*(q^2 + 1));
     (q^16 - 6*q^14 + 17*q^12 - 29*q^10 + 34*q^8 - 29*q^6 + 17*q^4 - 6*q^2 + 1) / (q^4*(q^2 + 1)), (q^18 - 5*q^16 + 14*q^14 - 24*q^12 + 31*q^10 - 29*q^8 + 21*q^6 - 11*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1)), (-q^16 + 5*q^14 - 14*q^12 + 24*q^10 - 31*q^8 + 29*q^6 - 21*q^4 + 11*q^2 - 4) / (q^2*(q^2 + 1));
     (-q^16 + 6*q^14 - 17*q^12 + 29*q^10 - 34*q^8 + 29*q^6 - 17*q^4 + 6*q^2 - 1) / (q^6*(q^2 + 1)), (-q^16 + 5*q^14 - 14*q^12 + 24*q^10 - 31*q^8 + 29*q^6 - 21*q^4 + 11*q^2 - 4) / (q^6*(q^2 + 1)), (q^18 - 5*q^16 + 14*q^14 - 24*q^12 + 31*q^10 - 29*q^8 + 21*q^6 - 11*q^4 + 3*q^2 - 1) / (q^6*(q^2 + 1))] := by
  rw [mixed6_p5 hq hn hD, V0_eq hq hn hD]; mat3

set_option maxHeartbeats 4000000 in
theorem mixed6_trace : Matrix.trace (Jb q * mixed6 q * Jb q) =
    (q^4 + 1)*(q^18 - 5*q^16 + 11*q^14 - 13*q^12 + 13*q^10 - 13*q^8 + 8*q^6 - 4*q^4 + q^2 - 1) / ((q^4 + q^2 + 1)*q^4*(q^2 + 1)) := by
  have := D_ne' hD; have := D_ne'' hD
  unfold mixed6; rw [mixed6_p6 hq hn hD]; unfold Jb
  simp [Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
  field_simp; ring

end
end Generic

end QOU.QuarkState.GammaGammaFourStrand


