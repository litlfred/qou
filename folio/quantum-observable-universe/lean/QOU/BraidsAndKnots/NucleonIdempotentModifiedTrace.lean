import QOU.BraidsAndKnots.NucleonWeightSpaceTraces
import QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder
import QOU.Machinery.MarkovTraceOnHecke
import QOU.Machinery.HeckeH3Characters
import QOU.Machinery.HeckeH3BlockRep
import QOU.Machinery.HeckeH3BlockCharacter
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.LinearCombination
import Mathlib.Tactic.NormNum

/-!
# Route 2: Hecke Idempotents (`e_{(2,1)}`), Modified Quantum Dimensions (`d_D(V_λ)`),
# and Mixed-Symmetry Nucleon Observables

This module formalizes Route 2 for the three-strand nucleon Hecke algebra `H_3(q)` and
the `3`-dimensional proton `(2,1)` and neutron `(1,2)` weight spaces of `(K^2)^{⊗ 3}`:

1. **Weight-Space Central Idempotent Decomposition (`1 = e_{(3)} + e_{(2,1)}`)**:
   Using the quadratic minimal polynomial `FEp_sector` / `EFn_sector` from
   `QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder`, we construct the explicit central
   idempotents `e3p`, `e21p` on `W_{(2,1)}` and `e3n`, `e21n` on `W_{(1,2)}`, and prove
   idempotency, orthogonality, completeness, `H_3(q)`-commutation, intertwiner transport
   under `P`, highest/lowest-weight kernel annihilation, and rank traces (`tr(e_{(3)}) = 1`,
   `tr(e_{(2,1)}) = 2`).
2. **Full-Twist Framing & Jucys–Murphy Content Eigenvalues**:
   We prove the exact Aiston–Morton (Theorem 5.5 & 5.7) / Hadji–Morton (Theorem 3.1 & 3.4)
   full-twist framing eigenvalues (`q^6`, `1`, `q^{-6}`) and Jucys–Murphy content sum
   eigenvalues (`q^3 + 2q`, `q - q⁻¹`, `-q^{-3} - 2q⁻¹`) on the three Wedderburn blocks
   `(3)`, `(2,1)`, `(1^3)` of `H_3(q)`.
3. **Wedderburn Character Decomposition of `trM` & GPMT Renormalized Trace `tMod111`**:
   We prove the general Wedderburn decomposition of the Markov trace `trM z (q - q⁻¹) v`
   over a generic `[Field K]`, its Convention-D (`z_D = q^3 / (q^2 + 1)`) specialization
   (`w_{(3)}(z_D) = (q^4 + 1)/(q^2 + 1)^2`, `w_{(2,1)}(z_D) = q^2/(q^2 + 1)^2`,
   `w_{(1^3)}(z_D) = 0`), and the Geer–Patureau-Mirand–Turaev (Theorem 3, Lemma 16,
   Corollary 17) first-order modified trace functional `tMod111` on the killed `(1^3)` sector.
4. **Per-Sector Nucleon Observables (`protonCoord` & `neutronCoord`)**:
   We evaluate the production proton and neutron Hecke elements on each Wedderburn sector
   at `a = -(q - q⁻¹)/2`, proving:
   * On the symmetric `(3)` decuplet sector: `χ_{(3)}(p) = q^2 · χ_{(3)}(n)` (`n/p = q^{-2} < 1`).
   * On the GPMT-renormalized `(1^3)` sector: `tMod111(n) = q^2 · tMod111(p)` (`n/p = q^{+2} > 1`).
   * On the mixed-symmetry `(2,1)` nucleon sector (`e_{(2,1)}` projection): exact factored closed
     forms for `χ_{(2,1)}(p)` and `χ_{(2,1)}(n)` with non-singular classical limit ratio
     `χ̃_{(2,1)}(n) / χ̃_{(2,1)}(p) → 4/3 > 1` at `q = 1`.

-- Ref: [aiston-morton-1997] Theorem 4.7, Theorem 5.5, Lemma 5.6, Theorem 5.7, Proposition 6.2.
-- Ref: [geer-patureau-mirand-turaev-2009] Lemma 1, Lemma 2, Theorem 3, Lemma 11, Lemma 16, Corollary 17.
-- Ref: [geer-patureau-mirand-turaev-2013] Lemma 1, Lemma 2, Theorem 3, Lemma 11, Lemma 16, Corollary 17.
-- Ref: [hadji-morton-2009] Corollary 1.3, Theorem 3.1, Theorem 3.4, Theorem 3.5.
-- Ref: [morton-2001-skein-murphy] Theorem 3.9; [lukac-2001] Lemma 4.1, Theorem 7.2.
-/

namespace QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder
open QOU.Machinery.H3

/-! ## Section 1: Explicit Central Idempotent Decomposition on the 3D Weight Spaces -/

section WeightSpaceIdempotents

variable {R : Type*} [Field R]

/-- The balanced quantum integer `[3]_q = q^2 + 1 + q^{-2}`. -/
def qInt3 (q : R) : R := q ^ 2 + 1 + q⁻¹ ^ 2

/-- Symmetric decuplet `(3)` central idempotent on the proton `(2,1)` weight space:
`e_{(3)}^p = [3]_q⁻¹ · FE_p`. -/
def e3p (q : R) : Matrix (Fin 3) (Fin 3) R := (qInt3 q)⁻¹ • FEp q

/-- Mixed-symmetry nucleon `(2,1)` central idempotent on the proton `(2,1)` weight space:
`e_{(2,1)}^p = 1 - [3]_q⁻¹ · FE_p`. -/
def e21p (q : R) : Matrix (Fin 3) (Fin 3) R := 1 - e3p q

/-- Symmetric decuplet `(3)` central idempotent on the neutron `(1,2)` weight space:
`e_{(3)}^n = [3]_q⁻¹ · EF_n`. -/
def e3n (q : R) : Matrix (Fin 3) (Fin 3) R := (qInt3 q)⁻¹ • EFn q

/-- Mixed-symmetry nucleon `(2,1)` central idempotent on the neutron `(1,2)` weight space:
`e_{(2,1)}^n = 1 - [3]_q⁻¹ · EF_n`. -/
def e21n (q : R) : Matrix (Fin 3) (Fin 3) R := 1 - e3n q

/-- Completeness on the proton weight space: `e_{(3)}^p + e_{(2,1)}^p = 1`. -/
theorem e3p_add_e21p (q : R) : e3p q + e21p q = 1 := by
  unfold e21p
  abel

/-- Completeness on the neutron weight space: `e_{(3)}^n + e_{(2,1)}^n = 1`. -/
theorem e3n_add_e21n (q : R) : e3n q + e21n q = 1 := by
  unfold e21n
  abel

/-- Quadratic relation `FE_p * FE_p = [3]_q • FE_p` on the proton weight space. -/
theorem FEp_mul_self (q : R) (hq : q ≠ 0) :
    FEp q * FEp q = qInt3 q • FEp q := by
  have hsec := FEp_sector q hq
  rw [mul_sub, Matrix.mul_smul, mul_one, sub_eq_zero] at hsec
  simpa [qInt3] using hsec

/-- Quadratic relation `EF_n * EF_n = [3]_q • EF_n` on the neutron weight space. -/
theorem EFn_mul_self (q : R) (hq : q ≠ 0) :
    EFn q * EFn q = qInt3 q • EFn q := by
  have hsec := EFn_sector q hq
  rw [mul_sub, Matrix.mul_smul, mul_one, sub_eq_zero] at hsec
  simpa [qInt3] using hsec

/-- Idempotency of `e_{(3)}^p`: `(e_{(3)}^p)^2 = e_{(3)}^p`. -/
theorem e3p_idem (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e3p q * e3p q = e3p q := by
  unfold e3p
  rw [Matrix.smul_mul, Matrix.mul_smul, FEp_mul_self q hq, smul_smul, smul_smul]
  have hinv : (qInt3 q)⁻¹ * (qInt3 q)⁻¹ * qInt3 q = (qInt3 q)⁻¹ := by
    rw [mul_assoc, inv_mul_cancel₀ hq3, mul_one]
  rw [hinv]

/-- Idempotency of `e_{(3)}^n`: `(e_{(3)}^n)^2 = e_{(3)}^n`. -/
theorem e3n_idem (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e3n q * e3n q = e3n q := by
  unfold e3n
  rw [Matrix.smul_mul, Matrix.mul_smul, EFn_mul_self q hq, smul_smul, smul_smul]
  have hinv : (qInt3 q)⁻¹ * (qInt3 q)⁻¹ * qInt3 q = (qInt3 q)⁻¹ := by
    rw [mul_assoc, inv_mul_cancel₀ hq3, mul_one]
  rw [hinv]

/-- Orthogonality on the proton weight space: `e_{(3)}^p * e_{(2,1)}^p = 0`. -/
theorem e3p_mul_e21p (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e3p q * e21p q = 0 := by
  unfold e21p
  rw [mul_sub, mul_one, e3p_idem q hq hq3, sub_self]

/-- Orthogonality on the proton weight space: `e_{(2,1)}^p * e_{(3)}^p = 0`. -/
theorem e21p_mul_e3p (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21p q * e3p q = 0 := by
  unfold e21p
  rw [sub_mul, one_mul, e3p_idem q hq hq3, sub_self]

/-- Idempotency of the mixed-symmetry nucleon projector `e_{(2,1)}^p`. -/
theorem e21p_idem (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21p q * e21p q = e21p q := by
  conv_lhs => rhs; unfold e21p
  rw [mul_sub, mul_one, e21p_mul_e3p q hq hq3, sub_zero]

/-- Orthogonality on the neutron weight space: `e_{(3)}^n * e_{(2,1)}^n = 0`. -/
theorem e3n_mul_e21n (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e3n q * e21n q = 0 := by
  unfold e21n
  rw [mul_sub, mul_one, e3n_idem q hq hq3, sub_self]

/-- Orthogonality on the neutron weight space: `e_{(2,1)}^n * e_{(3)}^n = 0`. -/
theorem e21n_mul_e3n (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21n q * e3n q = 0 := by
  unfold e21n
  rw [sub_mul, one_mul, e3n_idem q hq hq3, sub_self]

/-- Idempotency of the mixed-symmetry nucleon projector `e_{(2,1)}^n`. -/
theorem e21n_idem (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21n q * e21n q = e21n q := by
  conv_lhs => rhs; unfold e21n
  rw [mul_sub, mul_one, e21n_mul_e3n q hq hq3, sub_zero]

/-- `e_{(2,1)}^p` annihilates `FE_p` (projects onto the highest-weight kernel `ker E_p`). -/
theorem e21p_annihilates_FEp (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21p q * FEp q = 0 := by
  unfold e21p e3p
  rw [sub_mul, one_mul, Matrix.smul_mul, FEp_mul_self q hq, smul_smul,
    inv_mul_cancel₀ hq3, one_smul, sub_self]

/-- `e_{(2,1)}^n` annihilates `EF_n` (projects onto the lowest-weight kernel `ker F_n`). -/
theorem e21n_annihilates_EFn (q : R) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21n q * EFn q = 0 := by
  unfold e21n e3n
  rw [sub_mul, one_mul, Matrix.smul_mul, EFn_mul_self q hq, smul_smul,
    inv_mul_cancel₀ hq3, one_smul, sub_self]

/-- `e_{(2,1)}^p` commutes with the Hecke generator `A₁` on `W_{(2,1)}`. -/
theorem e21p_comm_A1 (q : R) (hq : q ≠ 0) :
    e21p q * A₁ q = A₁ q * e21p q := by
  unfold e21p e3p
  rw [sub_mul, mul_sub, one_mul, mul_one, Matrix.smul_mul, Matrix.mul_smul, FEp_comm₁ q hq]

/-- `e_{(2,1)}^p` commutes with the Hecke generator `A₂` on `W_{(2,1)}`. -/
theorem e21p_comm_A2 (q : R) (hq : q ≠ 0) :
    e21p q * A₂ q = A₂ q * e21p q := by
  unfold e21p e3p
  rw [sub_mul, mul_sub, one_mul, mul_one, Matrix.smul_mul, Matrix.mul_smul, FEp_comm₂ q hq]

/-- `e_{(2,1)}^n` commutes with the Hecke generator `B₁` on `W_{(1,2)}`. -/
theorem e21n_comm_B1 (q : R) (hq : q ≠ 0) :
    e21n q * B₁ q = B₁ q * e21n q := by
  unfold e21n e3n
  rw [sub_mul, mul_sub, one_mul, mul_one, Matrix.smul_mul, Matrix.mul_smul, EFn_comm₁ q hq]

/-- `e_{(2,1)}^n` commutes with the Hecke generator `B₂` on `W_{(1,2)}`. -/
theorem e21n_comm_B2 (q : R) (hq : q ≠ 0) :
    e21n q * B₂ q = B₂ q * e21n q := by
  unfold e21n e3n
  rw [sub_mul, mul_sub, one_mul, mul_one, Matrix.smul_mul, Matrix.mul_smul, EFn_comm₂ q hq]

/-- The weight-space intertwiner `P` transports `e_{(3)}^p` to `e_{(3)}^n`. -/
theorem intertwine_e3 (q : R) (hq : q ≠ 0) :
    P q * e3p q = e3n q * P q := by
  unfold e3p e3n
  rw [Matrix.mul_smul, Matrix.smul_mul, intertwine_FE_EF q hq]

/-- The weight-space intertwiner `P` transports `e_{(2,1)}^p` to `e_{(2,1)}^n`. -/
theorem intertwine_e21 (q : R) (hq : q ≠ 0) :
    P q * e21p q = e21n q * P q := by
  unfold e21p e21n
  rw [mul_sub, sub_mul, mul_one, one_mul, intertwine_e3 q hq]

/-- The trace of `FE_p` on `W_{(2,1)}` is `[3]_q`. -/
theorem trace_FEp (q : R) : (FEp q).trace = qInt3 q := by
  rw [Matrix.trace, Fin.sum_univ_three]
  have h0 : (FEp q).diag 0 = q⁻¹ ^ 2 := rfl
  have h1 : (FEp q).diag 1 = 1 := rfl
  have h2 : (FEp q).diag 2 = q ^ 2 := rfl
  rw [h0, h1, h2]
  unfold qInt3
  ring

/-- The trace of `EF_n` on `W_{(1,2)}` is `[3]_q`. -/
theorem trace_EFn (q : R) : (EFn q).trace = qInt3 q := by
  rw [Matrix.trace, Fin.sum_univ_three]
  have h0 : (EFn q).diag 0 = q⁻¹ ^ 2 := rfl
  have h1 : (EFn q).diag 1 = 1 := rfl
  have h2 : (EFn q).diag 2 = q ^ 2 := rfl
  rw [h0, h1, h2]
  unfold qInt3
  ring

/-- Rank trace of `e_{(3)}^p`: `tr(e_{(3)}^p) = 1` (1-dimensional `I = 3/2` decuplet sector). -/
theorem trace_e3p (q : R) (hq3 : qInt3 q ≠ 0) : (e3p q).trace = 1 := by
  unfold e3p
  rw [Matrix.trace_smul, trace_FEp, smul_eq_mul, inv_mul_cancel₀ hq3]

/-- Rank trace of `e_{(2,1)}^p`: `tr(e_{(2,1)}^p) = 2` (2-dimensional `I = 1/2` nucleon sector). -/
theorem trace_e21p (q : R) (hq3 : qInt3 q ≠ 0) : (e21p q).trace = 2 := by
  have h1 : (1 : Matrix (Fin 3) (Fin 3) R).trace = 3 := by
    rw [Matrix.trace_one, Fintype.card_fin]
    norm_num
  unfold e21p
  rw [Matrix.trace_sub, h1, trace_e3p q hq3]
  norm_num

end WeightSpaceIdempotents

/-! ## Section 2: Full-Twist Framing & Jucys–Murphy Content Eigenvalues on `H_3(q)` -/

section FullTwistAndMurphyEigenvalues

variable {K : Type*} [Field K]

/-- The longest element `w_0 = σ_0 σ_1 σ_0` in the 6-element normal-form basis
`[1, σ_0, σ_1, σ_1 σ_0, σ_0 σ_1, σ_0 σ_1 σ_0]` of `H_3(q)`. -/
def w0NF : Fin 6 → K := ![0, 0, 0, 0, 0, 1]

/-- The full-twist framing element `Δ_3^2 = w_0^2 = (σ_0 σ_1 σ_0)^2` in `H_3(q)`. -/
def fullTwistNF (h : K) : Fin 6 → K := mulNF h w0NF w0NF

/-- The second additive Jucys–Murphy element `M(2) = σ_0` in `H_3(q)`. -/
def murphy2NF : Fin 6 → K := ![0, 1, 0, 0, 0, 0]

/-- The third additive Jucys–Murphy element `M(3) = σ_1 σ_0 σ_1⁻¹ + h σ_1 = σ_1 + σ_0 σ_1 σ_0`
satisfying `(q - q⁻¹) M(3) = σ_1 σ_0^2 σ_1 - 1` in `H_3(q)`. -/
def murphy3NF : Fin 6 → K := ![0, 0, 1, 0, 0, 1]

/-- The total additive Jucys–Murphy content sum `M = M(1) + M(2) + M(3) = σ_0 + σ_1 + σ_0 σ_1 σ_0 ∈ Z(H_3(q))`
([aiston-morton-1997] Theorem 5.7). -/
def murphySumNF : Fin 6 → K := ![0, 1, 1, 0, 0, 1]

/-- Half-twist eigenvalue on the symmetric `(3)` block: `χ_{(3)}(w_0) = q^3`. -/
theorem chi3_w0 (q : K) : chiNF q (w0NF : Fin 6 → K) = q ^ 3 := by
  simp [chiNF, w0NF]

/-- Full-twist framing eigenvalue on the symmetric `(3)` block ([aiston-morton-1997] Theorem 5.5):
`χ_{(3)}(Δ_3^2) = q^6` (`n_{(3)} = 2(0 + 1 + 2) = 6`). -/
theorem chi3_fullTwist (q : K) (hq : q ≠ 0) :
    chiNF q (fullTwistNF (q - q⁻¹)) = q ^ 6 := by
  have h1 : q * q = (q - q⁻¹) * q + 1 := by
    rw [sub_mul, inv_mul_cancel₀ hq, sub_add_cancel]
  rw [fullTwistNF, chiNF_mulNF (q - q⁻¹) q h1, chi3_w0]
  ring

/-- Half-twist eigenvalue on the antisymmetric `(1^3)` block: `χ_{(1^3)}(w_0) = (-q⁻¹)^3`. -/
theorem chi111_w0 (q : K) : chiNF (-q⁻¹) (w0NF : Fin 6 → K) = (-q⁻¹) ^ 3 := by
  simp [chiNF, w0NF]

/-- Full-twist framing eigenvalue on the antisymmetric `(1^3)` block ([aiston-morton-1997] Theorem 5.5):
`χ_{(1^3)}(Δ_3^2) = (q⁻¹)^6` (`n_{(1^3)} = 2(0 - 1 - 2) = -6`). -/
theorem chi111_fullTwist (q : K) (hq : q ≠ 0) :
    chiNF (-q⁻¹) (fullTwistNF (q - q⁻¹)) = (q⁻¹) ^ 6 := by
  have h1 : (-q⁻¹) * (-q⁻¹) = (q - q⁻¹) * (-q⁻¹) + 1 := by
    field_simp; ring
  rw [fullTwistNF, chiNF_mulNF (q - q⁻¹) (-q⁻¹) h1, chi111_w0]
  ring

/-- Closed linear form of the 2-dimensional `(2,1)` character `chiM q v`:
`χ_{(2,1)}(v) = 2 v_0 + (q - q⁻¹)(v_1 + v_2) - v_3 - v_4`. -/
theorem chiM_eq_closed (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    chiM q v = 2 * v 0 + (q - q⁻¹) * v 1 + (q - q⁻¹) * v 2 - v 3 - v 4 := by
  unfold chiM blockOf
  simp only [Matrix.trace_fin_two, S0, S1, Matrix.add_apply, Matrix.smul_apply,
    Matrix.one_apply, Matrix.mul_apply, Fin.sum_univ_two, Matrix.of_apply,
    cons_val_zero, cons_val_one, smul_eq_mul, if_true]
  field_simp
  ring

/-- Full-twist framing action on the 2D mixed-symmetry `(2,1)` block ([aiston-morton-1997] Theorem 5.5):
`blockOf q (Δ_3^2) = 1 = q^0 · I_2` (`n_{(2,1)} = 2(0 + 1 - 1) = 0`). -/
theorem blockOf_fullTwist (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    blockOf q (fullTwistNF (q - q⁻¹)) = 1 := by
  rw [fullTwistNF, blockOf_mulNF q hq hq2]
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [blockOf, w0NF, S0, S1, Matrix.mul_apply, Fin.sum_univ_two] <;>
    field_simp <;> ring

/-- Full-twist character on the 2D mixed-symmetry `(2,1)` block: `χ_{(2,1)}(Δ_3^2) = 2 · q^0 = 2`. -/
theorem chi21_fullTwist (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    chiM q (fullTwistNF (q - q⁻¹)) = 2 := by
  unfold chiM
  rw [blockOf_fullTwist q hq hq2, Matrix.trace_one, Fintype.card_fin]
  norm_num

/-- Jucys–Murphy content sum eigenvalue on `(3)` ([aiston-morton-1997] Theorem 5.7):
`m_{(3)} = q[1]_q + q^2[2]_q = q^3 + 2q`. -/
theorem chi3_murphySum (q : K) :
    chiNF q (murphySumNF : Fin 6 → K) = q ^ 3 + 2 * q := by
  simp [chiNF, murphySumNF]
  ring

/-- Jucys–Murphy content sum eigenvalue on `(1^3)` ([aiston-morton-1997] Theorem 5.7):
`m_{(1^3)} = q⁻¹[-1]_q + q^{-2}[-2]_q = -q⁻¹^3 - 2q⁻¹`. -/
theorem chi111_murphySum (q : K) :
    chiNF (-q⁻¹) (murphySumNF : Fin 6 → K) = -(q⁻¹) ^ 3 - 2 * q⁻¹ := by
  simp [chiNF, murphySumNF]
  ring

/-- Jucys–Murphy content sum action on the 2D `(2,1)` block ([aiston-morton-1997] Theorem 5.7):
`blockOf q M = (q - q⁻¹) • I_2` (`m_{(2,1)} = q[1]_q + q⁻¹[-1]_q = q - q⁻¹`). -/
theorem blockOf_murphySum (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) :
    blockOf q (murphySumNF : Fin 6 → K) = (q - q⁻¹) • (1 : Matrix (Fin 2) (Fin 2) K) := by
  ext i j
  fin_cases i <;> fin_cases j <;>
    simp [blockOf, murphySumNF, S0, S1] <;>
    field_simp <;> ring

end FullTwistAndMurphyEigenvalues

/-! ## Section 3: Wedderburn Decomposition of `trM`, Convention D, and GPMT Modified Trace -/

section WedderburnMarkovAndModifiedTrace

variable {K : Type*} [Field K]

/-- Symmetric `(3)` character on `H_3(q)` normal-form vectors. -/
def chi3 (q : K) (v : Fin 6 → K) : K := chiNF q v

/-- Mixed-symmetry `(2,1)` nucleon character on `H_3(q)` normal-form vectors. -/
noncomputable def chi21 (q : K) (v : Fin 6 → K) : K := chiM q v

/-- Antisymmetric `(1^3)` character on `H_3(q)` normal-form vectors. -/
def chi111 (q : K) (v : Fin 6 → K) : K := chiNF (-q⁻¹) v

/-- General Ocneanu/Wedderburn weight `w_{(3)}(q, z)` of the symmetric `(3)` sector. -/
def w3 (q z : K) : K :=
  (q * z + 1) * (q ^ 3 * z + q * z + 1) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- General Ocneanu/Wedderburn weight `w_{(2,1)}(q, z)` of the mixed-symmetry `(2,1)` nucleon sector. -/
def w21 (q z : K) : K :=
  q * (q - z) * (q * z + 1) / (q ^ 4 + q ^ 2 + 1)

/-- General Ocneanu/Wedderburn weight `w_{(1^3)}(q, z)` of the antisymmetric `(1^3)` sector. -/
def w111 (q z : K) : K :=
  q ^ 2 * (z - q) * ((q ^ 2 + 1) * z - q ^ 3) / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- Closed linear formula for `trM z h v` expanding all 6 normal-form coordinates. -/
theorem trM_eq_closed (z h : K) (v : Fin 6 → K) :
    trM z h v =
      v 0 + z * v 1 + z * v 2 + z ^ 2 * v 3 + z ^ 2 * v 4 + (h * z ^ 2 + z) * v 5 := by
  unfold trM TRM
  rw [Fin.sum_univ_six]
  change v 0 * 1 + v 1 * z + v 2 * z + v 3 * z ^ 2 + v 4 * z ^ 2 + v 5 * (h * z ^ 2 + z) = _
  ring

/-- **General Wedderburn character decomposition of the Markov trace on `H_3(q)`**:
For every normal-form vector `v : Fin 6 → K` and every Markov parameter `z : K`,
`trM z (q - q⁻¹) v = w_{(3)}(q,z) χ_{(3)}(v) + w_{(2,1)}(q,z) χ_{(2,1)}(v) + w_{(1^3)}(q,z) χ_{(1^3)}(v)`. -/
theorem trM_eq_wedderburn_sum (q z : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    trM z (q - q⁻¹) v =
      w3 q z * chi3 q v + w21 q z * chi21 q v + w111 q z * chi111 q v := by
  have h4inv : (1 + q ^ 2 + q ^ 4) * (1 + q ^ 2 + q ^ 4)⁻¹ = 1 := by
    apply mul_inv_cancel₀
    have : 1 + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 := by ring
    rw [this]; exact hq4
  rw [trM_eq_closed, chi3, chi21, chiM_eq_closed q hq hq2 v, chi111]
  unfold w3 w21 w111 chiNF
  field_simp
  linear_combination
    -(v 0 * q + v 0 * q ^ 3 + z * v 1 * q + z * v 1 * q ^ 3 + z * v 2 * q + z * v 2 * q ^ 3 +
      z * q * v 5 + z * q ^ 3 * v 5 + z ^ 2 * v 3 * q + z ^ 2 * v 3 * q ^ 3 +
      z ^ 2 * v 4 * q + z ^ 2 * v 4 * q ^ 3 + z ^ 2 * q ^ 4 * v 5 - z ^ 2 * v 5) * h4inv

/-- The canonical Convention-D Markov parameter `z_D = q^3 / (q^2 + 1)`. -/
def zD (q : K) : K := q ^ 3 / (q ^ 2 + 1)

/-- At Convention D, the symmetric `(3)` weight is `(q^4 + 1) / (q^2 + 1)^2`. -/
theorem w3_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w3 q (zD q) = (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 := by
  have h4inv : (1 + q ^ 2 + q ^ 4) * (1 + q ^ 2 + q ^ 4)⁻¹ = 1 := by
    apply mul_inv_cancel₀
    have : 1 + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 := by ring
    rw [this]; exact hq4
  unfold w3 zD
  field_simp
  linear_combination (1 + q ^ 4) * h4inv

/-- At Convention D, the mixed-symmetry `(2,1)` nucleon weight is `q^2 / (q^2 + 1)^2 ≠ 0`. -/
theorem w21_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w21 q (zD q) = q ^ 2 / (q ^ 2 + 1) ^ 2 := by
  have h4inv : (1 + q ^ 2 + q ^ 4) * (1 + q ^ 2 + q ^ 4)⁻¹ = 1 := by
    apply mul_inv_cancel₀
    have : 1 + q ^ 2 + q ^ 4 = q ^ 4 + q ^ 2 + 1 := by ring
    rw [this]; exact hq4
  unfold w21 zD
  field_simp
  linear_combination q ^ 2 * h4inv

/-- At Convention D, the antisymmetric `(1^3)` weight vanishes identically: `w_{(1^3)}(z_D) = 0`. -/
theorem w111_conventionD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    w111 q (zD q) = 0 := by
  unfold w111 zD
  have hnum : (q ^ 2 + 1) * (q ^ 3 / (q ^ 2 + 1)) - q ^ 3 = 0 := by
    rw [mul_div_cancel₀ _ hq2, sub_self]
  rw [hnum, mul_zero, zero_div]

/-- At Convention D, the Markov weights satisfy `w_{(3)}(z_D) + 2 w_{(2,1)}(z_D) = 1`. -/
theorem weights_conventionD_sum_eq_one (q : K) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    w3 q (zD q) + 2 * w21 q (zD q) = 1 := by
  rw [w3_conventionD q hq2 hq4, w21_conventionD q hq2 hq4]
  rw [mul_div_assoc', ← add_div, div_eq_iff (pow_ne_zero 2 hq2)]
  ring

/-- **Convention-D Wedderburn Decomposition of `trM`**:
At `z = z_D`, the `(1^3)` sector is killed and `trM` reduces to the two-row sum over `(3)` and `(2,1)`. -/
theorem trM_conventionD_eq_twoRow_sum (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) (v : Fin 6 → K) :
    trM (zD q) (q - q⁻¹) v =
      (q ^ 4 + 1) / (q ^ 2 + 1) ^ 2 * chi3 q v +
      q ^ 2 / (q ^ 2 + 1) ^ 2 * chi21 q v := by
  rw [trM_eq_wedderburn_sum q (zD q) hq hq2 hq4 v, w3_conventionD q hq2 hq4,
    w21_conventionD q hq2 hq4, w111_conventionD q hq2, zero_mul, add_zero]

/-- **Geer–Patureau-Mirand–Turaev First-Order Factorization of `w_{(1^3)}(q, z)`**
([geer-patureau-mirand-turaev-2009] / [geer-patureau-mirand-turaev-2013] Lemma 16 & Corollary 17):
`w_{(1^3)}(q, z)` factors as `(z - z_D)` times the regular factor `q^2 (z - q) / (q^4 + q^2 + 1)`. -/
theorem w111_factor_zD (q z : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    w111 q z = (z - zD q) * (q ^ 2 * (z - q) / (q ^ 4 + q ^ 2 + 1)) := by
  unfold w111 zD
  have hsub : z - q ^ 3 / (q ^ 2 + 1) = ((q ^ 2 + 1) * z - q ^ 3) / (q ^ 2 + 1) := by
    rw [sub_div' hq2]; ring
  rw [hsub, div_mul_div_comm]
  ring

/-- The Geer–Patureau-Mirand–Turaev modified quantum dimension `d_D(S^{(1^3)}) = w'_{(1^3)}(z_D)`
of the killed `(1^3)` sector at Convention D. -/
def dMod111 (q : K) : K :=
  -q ^ 3 / ((q ^ 2 + 1) * (q ^ 4 + q ^ 2 + 1))

/-- The regular factor of `w_{(1^3)}(q, z) / (z - z_D)` evaluated at `z = z_D` equals `dMod111 q`. -/
theorem w111_slope_at_zD (q : K) (hq2 : q ^ 2 + 1 ≠ 0) :
    q ^ 2 * (zD q - q) / (q ^ 4 + q ^ 2 + 1) = dMod111 q := by
  unfold zD dMod111
  have hsub : q ^ 3 / (q ^ 2 + 1) - q = -q / (q ^ 2 + 1) := by
    rw [div_sub' hq2]; ring
  rw [hsub, mul_div_assoc', div_div]
  ring

/-- The GPMT modified quantum dimension `dMod111 q` is non-vanishing for all `q ≠ 0`. -/
theorem dMod111_ne_zero (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (hq4 : q ^ 4 + q ^ 2 + 1 ≠ 0) :
    dMod111 q ≠ 0 := by
  unfold dMod111
  exact div_ne_zero (neg_ne_zero.mpr (pow_ne_zero 3 hq)) (mul_ne_zero hq2 hq4)

/-- The Geer–Patureau-Mirand–Turaev renormalized trace `t_D` on the `(1^3)` ideal
([geer-patureau-mirand-turaev-2009] Theorem 3 & Corollary 17):
`tMod111 q v = d_D(S^{(1^3)}) · χ_{(1^3)}(v)`. -/
def tMod111 (q : K) (v : Fin 6 → K) : K :=
  dMod111 q * chi111 q v

end WedderburnMarkovAndModifiedTrace

/-! ## Section 4: Per-Sector Evaluation of Production Proton and Neutron Words -/

section NucleonSectorObservables

variable {K : Type*} [Field K]

/-- Normal-form coordinate vector of the production proton word
`σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ (σ₀+a) (σ₁+a) σ₀ σ₀`
(matching step `s10` of `QOU.Mass.NucleonWordTraceClosedForm.protonCoord`). -/
def protonCoord (h a : K) : Fin 6 → K :=
  ![ -a^2 * h^7 - 3 * a^2 * h^5 - a^2 * h^3 + a^2 * h - a * h^8 - 4 * a * h^6 - 3 * a * h^4 + a + h^5 + h^3,
     -a^2 * h^8 - 4 * a^2 * h^6 - 3 * a^2 * h^4 + a^2 * h^2 + a^2 - a * h^9 - 5 * a * h^7 - 6 * a * h^5
       - a * h^3 + 2 * a * h + h^6 + 2 * h^4 + h^2,
     -a^2 * h^2 - 2 * a * h^3 - h^4 + 1,
     -a^2 * h^3 - a * h^4 + h^3 + h,
     a^2 * h^5 + a^2 * h^3 + a * h^6 + a * h^4 + a * h^2 + a - h^5 - h^3 + h,
     a^2 * h^6 + 2 * a^2 * h^4 + a^2 * h^2 + a * h^7 + 3 * a * h^5 + 3 * a * h^3 + a * h ]

/-- Normal-form coordinate vector of the production neutron word
`σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ (σ₀+a) (σ₀+a) σ₁⁻¹ σ₀ σ₀`
(matching step `s10` of `QOU.Mass.NucleonWordTraceClosedForm.neutronCoord`). -/
def neutronCoord (h a : K) : Fin 6 → K :=
  ![ a^2 * h^7 + 3 * a^2 * h^5 + 2 * a^2 * h^3 - a^2 * h + 2 * a * h^8 + 6 * a * h^6 + 2 * a * h^4
       - 4 * a * h^2 + h^9 + 4 * h^7 + 4 * h^5 - h,
     a^2 * h^8 + 4 * a^2 * h^6 + 4 * a^2 * h^4 + 2 * a * h^9 + 8 * a * h^7 + 6 * a * h^5 - 4 * a * h^3
       - 2 * a * h + h^10 + 5 * h^8 + 7 * h^6 + 2 * h^4 - h^2,
     a^2 + 1,
     a^2 * h^3 + a^2 * h + 2 * a * h^4 + 2 * a * h^2 + h^5 + 2 * h^3 + h,
     -a^2 * h^5 - 2 * a^2 * h^3 - 2 * a * h^6 - 4 * a * h^4 + 2 * a - h^7 - 3 * h^5 - 2 * h^3 + h,
     -a^2 * h^6 - 2 * a^2 * h^4 - a^2 * h^2 - 2 * a * h^7 - 4 * a * h^5 + 2 * a * h - h^8 - 3 * h^6 - 2 * h^4 ]

@[simp] theorem protonCoord_5 (h a : K) :
    protonCoord h a 5 =
      a^2 * h^6 + 2 * a^2 * h^4 + a^2 * h^2 + a * h^7 + 3 * a * h^5 + 3 * a * h^3 + a * h := rfl

@[simp] theorem neutronCoord_5 (h a : K) :
    neutronCoord h a 5 =
      -a^2 * h^6 - 2 * a^2 * h^4 - a^2 * h^2 - 2 * a * h^7 - 4 * a * h^5 + 2 * a * h - h^8 - 3 * h^6 - 2 * h^4 := rfl

/-- One affine letter `(i, s, b) ↦ s • 1 + b • σ_i`, `i ≤ 1`, acting on `H_3(q)` normal-form
coordinates via `QOU.Machinery.H3.mulσ₀` and `mulσ₁`
(matching `QOU.Mass.NucleonWordTraceClosedForm.nfStep`). -/
def nfStep (h : K) (v : Fin 6 → K) (l : ℕ × K × K) : Fin 6 → K :=
  l.2.1 • v + l.2.2 • (if l.1 = 0 then mulσ₀ h v else mulσ₁ h v)

/-- The production proton word (`intra_order = "borromean"`, matching
`QOU.Mass.NucleonWordTraceClosedForm.protonWord`):
`σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ (σ₀+a) (σ₁+a) σ₀ σ₀` with `σ⁻¹ = σ - h`. -/
def protonWord (h a : K) : List (ℕ × K × K) :=
  [(0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, 0, 1),
   (0, a, 1), (1, a, 1), (0, 0, 1), (0, 0, 1)]

/-- The production neutron word (`intra_order = "borromean"`, matching
`QOU.Mass.NucleonWordTraceClosedForm.neutronWord`):
`σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ σ₀ σ₁⁻¹ (σ₀+a) (σ₀+a) σ₁⁻¹ σ₀ σ₀` with `σ⁻¹ = σ - h`. -/
def neutronWord (h a : K) : List (ℕ × K × K) :=
  [(0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, 0, 1), (1, -h, 1), (0, a, 1),
   (0, a, 1), (1, -h, 1), (0, 0, 1), (0, 0, 1)]

theorem nfStep_zero (h x0 x1 x2 x3 x4 x5 s b : K) :
    nfStep h ![x0, x1, x2, x3, x4, x5] (0, s, b)
      = ![s * x0 + b * x1, s * x1 + b * (x0 + h * x1), s * x2 + b * x3,
          s * x3 + b * (x2 + h * x3), s * x4 + b * x5, s * x5 + b * (x4 + h * x5)] := by
  funext i
  fin_cases i <;> simp [nfStep, mulσ₀]

theorem nfStep_one (h x0 x1 x2 x3 x4 x5 s b : K) :
    nfStep h ![x0, x1, x2, x3, x4, x5] (1, s, b)
      = ![s * x0 + b * x2, s * x1 + b * x4, s * x2 + b * (x0 + h * x2),
          s * x3 + b * x5, s * x4 + b * (x1 + h * x4), s * x5 + b * (x3 + h * x5)] := by
  funext i
  fin_cases i <;> simp [nfStep, mulσ₁]

omit [Field K] in
/-- Componentwise equality of six-vectors. -/
theorem vec6_ext {a0 a1 a2 a3 a4 a5 b0 b1 b2 b3 b4 b5 : K} (e0 : a0 = b0) (e1 : a1 = b1)
    (e2 : a2 = b2) (e3 : a3 = b3) (e4 : a4 = b4) (e5 : a5 = b5) :
    (![a0, a1, a2, a3, a4, a5] : Fin 6 → K) = ![b0, b1, b2, b3, b4, b5] := by
  subst e0 e1 e2 e3 e4 e5; rfl

set_option maxHeartbeats 1000000 in
/-- **Exact Word-Fold Bridge for the Proton Word**:
`protonCoord h a` is identically the `nfStep` fold of the production proton word
`protonWord h a` from the identity coordinate vector `![1, 0, 0, 0, 0, 0]`. -/
theorem protonWord_foldl_eq_protonCoord (h a : K) :
    (protonWord h a).foldl (nfStep h) ![1, 0, 0, 0, 0, 0] = protonCoord h a := by
  simp only [protonWord, List.foldl_cons, List.foldl_nil]
  have s0 : nfStep h ![1, 0, 0, 0, 0, 0] (0, 0, 1) =
      ![0, 1, 0, 0, 0, 0] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s1 : nfStep h ![0, 1, 0, 0, 0, 0] (1, -h, 1) =
      ![0, -h, 0, 0, 1, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s2 : nfStep h ![0, -h, 0, 0, 1, 0] (0, 0, 1) =
      ![-h, -h^2, 0, 0, 0, 1] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s3 : nfStep h ![-h, -h^2, 0, 0, 0, 1] (1, -h, 1) =
      ![h^2, h^3, -h, 1, -h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s4 : nfStep h ![h^2, h^3, -h, 1, -h^2, 0] (0, 0, 1) =
      ![h^3, h^4 + h^2, 1, 0, 0, -h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s5 : nfStep h ![h^3, h^4 + h^2, 1, 0, 0, -h^2] (1, -h, 1) =
      ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s6 : nfStep h ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] (0, 0, 1) =
      ![-h^5 - h^3, -h^6 - 2*h^4 + 1, -h^2, 0, 0, h^4 + h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s7 : nfStep h ![-h^5 - h^3, -h^6 - 2*h^4 + 1, -h^2, 0, 0, h^4 + h^2] (0, a, 1) =
      ![-a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, -a*h^6 - 2*a*h^4 + a - h^7 - 3*h^5 - h^3 + h, -a*h^2, -h^2, h^4 + h^2, a*h^4 + a*h^2 + h^5 + h^3] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s8 : nfStep h ![-a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, -a*h^6 - 2*a*h^4 + a - h^7 - 3*h^5 - h^3 + h, -a*h^2, -h^2, h^4 + h^2, a*h^4 + a*h^2 + h^5 + h^3] (1, a, 1) =
      ![-a^2*h^5 - a^2*h^3 - a*h^6 - 2*a*h^4 - a*h^2 + a, -a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^2 - a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a*h^4 + h^5 + h^3, -a*h^6 - a*h^4 + a*h^2 + a - h^7 - 2*h^5 + h, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s9 : nfStep h ![-a^2*h^5 - a^2*h^3 - a*h^6 - 2*a*h^4 - a*h^2 + a, -a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^2 - a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a*h^4 + h^5 + h^3, -a*h^6 - a*h^4 + a*h^2 + a - h^7 - 2*h^5 + h, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2] (0, 0, 1) =
      ![-a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^7 - 3*a^2*h^5 - a^2*h^3 + a^2*h - a*h^8 - 4*a*h^6 - 3*a*h^4 + a + h^5 + h^3, a*h^4 + h^5 + h^3, -a^2*h^2 - 2*a*h^3 - h^4 + 1, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2, a^2*h^5 + a^2*h^3 + a*h^6 + a*h^4 + a*h^2 + a - h^5 - h^3 + h] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s10 : nfStep h ![-a^2*h^6 - 2*a^2*h^4 + a^2 - a*h^7 - 3*a*h^5 - a*h^3 + a*h + h^4 + h^2, -a^2*h^7 - 3*a^2*h^5 - a^2*h^3 + a^2*h - a*h^8 - 4*a*h^6 - 3*a*h^4 + a + h^5 + h^3, a*h^4 + h^5 + h^3, -a^2*h^2 - 2*a*h^3 - h^4 + 1, a^2*h^4 + a^2*h^2 + 2*a*h^5 + 2*a*h^3 + h^6 + h^4 - h^2, a^2*h^5 + a^2*h^3 + a*h^6 + a*h^4 + a*h^2 + a - h^5 - h^3 + h] (0, 0, 1) =
      protonCoord h a := by
    rw [nfStep_zero, protonCoord]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  rw [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

set_option maxHeartbeats 1000000 in
/-- **Exact Word-Fold Bridge for the Neutron Word**:
`neutronCoord h a` is identically the `nfStep` fold of the production neutron word
`neutronWord h a` from the identity coordinate vector `![1, 0, 0, 0, 0, 0]`. -/
theorem neutronWord_foldl_eq_neutronCoord (h a : K) :
    (neutronWord h a).foldl (nfStep h) ![1, 0, 0, 0, 0, 0] = neutronCoord h a := by
  simp only [neutronWord, List.foldl_cons, List.foldl_nil]
  have s0 : nfStep h ![1, 0, 0, 0, 0, 0] (0, 0, 1) =
      ![0, 1, 0, 0, 0, 0] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s1 : nfStep h ![0, 1, 0, 0, 0, 0] (1, -h, 1) =
      ![0, -h, 0, 0, 1, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s2 : nfStep h ![0, -h, 0, 0, 1, 0] (0, 0, 1) =
      ![-h, -h^2, 0, 0, 0, 1] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s3 : nfStep h ![-h, -h^2, 0, 0, 0, 1] (1, -h, 1) =
      ![h^2, h^3, -h, 1, -h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s4 : nfStep h ![h^2, h^3, -h, 1, -h^2, 0] (0, 0, 1) =
      ![h^3, h^4 + h^2, 1, 0, 0, -h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s5 : nfStep h ![h^3, h^4 + h^2, 1, 0, 0, -h^2] (1, -h, 1) =
      ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s6 : nfStep h ![1 - h^4, -h^5 - h^3, h^3, -h^2, h^4 + h^2, 0] (0, a, 1) =
      ![-a*h^4 + a - h^5 - h^3, -a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, a*h^3 - h^2, -a*h^2, a*h^4 + a*h^2, h^4 + h^2] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s7 : nfStep h ![-a*h^4 + a - h^5 - h^3, -a*h^5 - a*h^3 - h^6 - 2*h^4 + 1, a*h^3 - h^2, -a*h^2, a*h^4 + a*h^2, h^4 + h^2] (0, a, 1) =
      ![-a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, a^2*h^3 - 2*a*h^2, -a^2*h^2 - h^2, a^2*h^4 + a^2*h^2 + h^4 + h^2, 2*a*h^4 + 2*a*h^2 + h^5 + h^3] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s8 : nfStep h ![-a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, a^2*h^3 - 2*a*h^2, -a^2*h^2 - h^2, a^2*h^4 + a^2*h^2 + h^4 + h^2, 2*a*h^4 + 2*a*h^2 + h^5 + h^3] (1, -h, 1) =
      ![a^2*h^5 + a^2*h^3 - a^2*h + 2*a*h^6 + 2*a*h^4 - 2*a*h^2 + h^7 + 2*h^5 - h, a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, -a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, -a^2*h^2 - h^2] := by
    rw [nfStep_one]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s9 : nfStep h ![a^2*h^5 + a^2*h^3 - a^2*h + 2*a*h^6 + 2*a*h^4 - 2*a*h^2 + h^7 + 2*h^5 - h, a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, -a^2*h^4 + a^2 - 2*a*h^5 - 2*a*h^3 - h^6 - 2*h^4 + 1, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, -a^2*h^5 - a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - h^3 + h, -a^2*h^2 - h^2] (0, 0, 1) =
      ![a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, a^2*h^7 + 3*a^2*h^5 + 2*a^2*h^3 - a^2*h + 2*a*h^8 + 6*a*h^6 + 2*a*h^4 - 4*a*h^2 + h^9 + 4*h^7 + 4*h^5 - h, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, a^2 + 1, -a^2*h^2 - h^2, -a^2*h^5 - 2*a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - 2*h^3 + h] := by
    rw [nfStep_zero]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  have s10 : nfStep h ![a^2*h^6 + 2*a^2*h^4 + a^2*h^2 + 2*a*h^7 + 4*a*h^5 - 2*a*h + h^8 + 3*h^6 + 2*h^4, a^2*h^7 + 3*a^2*h^5 + 2*a^2*h^3 - a^2*h + 2*a*h^8 + 6*a*h^6 + 2*a*h^4 - 4*a*h^2 + h^9 + 4*h^7 + 4*h^5 - h, a^2*h^3 + 2*a*h^4 + 2*a*h^2 + h^5 + 2*h^3, a^2 + 1, -a^2*h^2 - h^2, -a^2*h^5 - 2*a^2*h^3 - 2*a*h^6 - 4*a*h^4 + 2*a - h^7 - 3*h^5 - 2*h^3 + h] (0, 0, 1) =
      neutronCoord h a := by
    rw [nfStep_zero, neutronCoord]; refine vec6_ext ?_ ?_ ?_ ?_ ?_ ?_ <;> ring
  rw [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]

/-- **Symmetric `(3)` Decuplet Sector on Proton Word**:
At `a = -(q - q⁻¹)/2`, `χ_{(3)}(protonCoord) = q (q^2 + 1)^2 / 4`. -/
theorem chi3_protonCoord (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi3 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) = q * (q ^ 2 + 1) ^ 2 / 4 := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold chi3 chiNF
  rw [protonCoord_5]
  simp only [protonCoord, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- **Symmetric `(3)` Decuplet Sector on Neutron Word**:
At `a = -(q - q⁻¹)/2`, `χ_{(3)}(neutronCoord) = (q^2 + 1)^2 / (4 q)`. -/
theorem chi3_neutronCoord (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi3 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) = (q ^ 2 + 1) ^ 2 / (4 * q) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold chi3 chiNF
  rw [neutronCoord_5]
  simp only [neutronCoord, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- **Symmetric `(3)` Sector Ratio**:
In the unphysical `I = 3/2` decuplet sector `(3)`, the proton character is `q^2` times the
neutron character (`χ_{(3)}(n) / χ_{(3)}(p) = q^{-2} < 1` for `q > 1`). -/
theorem chi3_proton_eq_q_sq_mul_neutron (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi3 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      q ^ 2 * chi3 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) := by
  rw [chi3_protonCoord q hq h2, chi3_neutronCoord q hq h2]
  field_simp

/-- **Antisymmetric `(1^3)` Sector on Proton Word**:
At `a = -(q - q⁻¹)/2`, `χ_{(1^3)}(protonCoord) = -(q^2 + 1)^2 / (4 q^5)`. -/
theorem chi111_protonCoord (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi111 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) = -(q ^ 2 + 1) ^ 2 / (4 * q ^ 5) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold chi111 chiNF
  rw [protonCoord_5]
  simp only [protonCoord, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- **Antisymmetric `(1^3)` Sector on Neutron Word**:
At `a = -(q - q⁻¹)/2`, `χ_{(1^3)}(neutronCoord) = -(q^2 + 1)^2 / (4 q^3)`. -/
theorem chi111_neutronCoord (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi111 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) = -(q ^ 2 + 1) ^ 2 / (4 * q ^ 3) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold chi111 chiNF
  rw [neutronCoord_5]
  simp only [neutronCoord, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- **GPMT Renormalized Trace Ratio on the Killed `(1^3)` Sector**:
Under the Geer–Patureau-Mirand–Turaev renormalized trace `tMod111` on `H_3(q) e_{(1^3)}`,
the neutron observable is `q^2` times the proton observable (`t_D(n) / t_D(p) = q^{+2} > 1`
for `q > 1`, the exact inverse of the `(3)` decuplet ratio!). -/
theorem tMod111_neutron_eq_q_sq_mul_proton (q : K) (hq : q ≠ 0) (h2 : (2 : K) ≠ 0) :
    tMod111 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      q ^ 2 * tMod111 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) := by
  simp only [tMod111, chi111_protonCoord q hq h2, chi111_neutronCoord q hq h2]
  field_simp

/-- **Mixed-Symmetry `(2,1)` Nucleon Sector on Proton Word (Projected onto `e_{(2,1)}`)**:
Exact factored closed form of `χ_{(2,1)}(protonCoord)` at `a = -(q - q⁻¹)/2`. -/
theorem chi21_protonCoord (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi21 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) *
        (q ^ 12 - 3 * q ^ 10 + 6 * q ^ 8 - 9 * q ^ 6 + 6 * q ^ 4 - 3 * q ^ 2 + 1) /
        (4 * q ^ 11) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  rw [chi21, chiM_eq_closed q hq hq2]
  simp only [protonCoord, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- **Mixed-Symmetry `(2,1)` Nucleon Sector on Neutron Word (Projected onto `e_{(2,1)}`)**:
Exact factored closed form of `χ_{(2,1)}(neutronCoord)` at `a = -(q - q⁻¹)/2`. -/
theorem chi21_neutronCoord (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0) (h2 : (2 : K) ≠ 0) :
    chi21 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) *
        (q ^ 12 - 2 * q ^ 10 + 2 * q ^ 8 - 3 * q ^ 6 + 2 * q ^ 4 - 2 * q ^ 2 + 1) /
        (4 * q ^ 11) := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  rw [chi21, chiM_eq_closed q hq hq2]
  simp only [neutronCoord, cons_val_zero, cons_val_one, cons_val_two, cons_val_three,
    cons_val_four, head_cons, tail_cons]
  field_simp
  ring

/-- Desingularized mixed-symmetry `(2,1)` proton amplitude `χ_{(2,1)}(p) / (q^2 - 1)`. -/
def chi21ReducedProton (q : K) : K :=
  (q ^ 4 + 1) * (q ^ 4 + q ^ 2 + 1) *
    (q ^ 12 - 3 * q ^ 10 + 6 * q ^ 8 - 9 * q ^ 6 + 6 * q ^ 4 - 3 * q ^ 2 + 1) /
    (4 * q ^ 11)

/-- Desingularized mixed-symmetry `(2,1)` neutron amplitude `χ_{(2,1)}(n) / (q^2 - 1)`. -/
def chi21ReducedNeutron (q : K) : K :=
  (q ^ 2 + 1) ^ 2 * (q ^ 4 + 1) *
    (q ^ 12 - 2 * q ^ 10 + 2 * q ^ 8 - 3 * q ^ 6 + 2 * q ^ 4 - 2 * q ^ 2 + 1) /
    (4 * q ^ 11)

/-- Factorization `χ_{(2,1)}(p) = (q^2 - 1) · χ̃_{(2,1)}(p)`. -/
theorem chi21_proton_eq_sub_sq_mul_reduced (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    chi21 q (protonCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * chi21ReducedProton q := by
  rw [chi21_protonCoord q hq hq2 h2, chi21ReducedProton]
  ring

/-- Factorization `χ_{(2,1)}(n) = (q^2 - 1) · χ̃_{(2,1)}(n)`. -/
theorem chi21_neutron_eq_sub_sq_mul_reduced (q : K) (hq : q ≠ 0) (hq2 : q ^ 2 + 1 ≠ 0)
    (h2 : (2 : K) ≠ 0) :
    chi21 q (neutronCoord (q - q⁻¹) (-(q - q⁻¹) / 2)) =
      (q ^ 2 - 1) * chi21ReducedNeutron q := by
  rw [chi21_neutronCoord q hq hq2 h2, chi21ReducedNeutron]
  ring

/-- Classical anchor value of the reduced `(2,1)` proton amplitude at `q = 1`:
`4 · χ̃_{(2,1)}(p)|_{q=1} = -6`. -/
theorem four_mul_chi21ReducedProton_at_one (h2 : (2 : K) ≠ 0) :
    4 * chi21ReducedProton (1 : K) = -6 := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold chi21ReducedProton
  field_simp
  ring

/-- Classical anchor value of the reduced `(2,1)` neutron amplitude at `q = 1`:
`4 · χ̃_{(2,1)}(n)|_{q=1} = -8`. -/
theorem four_mul_chi21ReducedNeutron_at_one (h2 : (2 : K) ≠ 0) :
    4 * chi21ReducedNeutron (1 : K) = -8 := by
  have h4 : (4 : K) ≠ 0 := by
    have : (4 : K) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  unfold chi21ReducedNeutron
  field_simp
  ring

/-- **Mixed-Symmetry `(2,1)` Nucleon Sector Ratio at the Classical Limit `q = 1`**:
When projected onto the physical `I = 1/2` mixed-symmetry nucleon idempotent `e_{(2,1)}`
(removing the `O(1)` symmetric `(3)` decuplet background), the neutron-to-proton amplitude
ratio at `q = 1` is `4 / 3 > 1` (`3 · χ̃_{(2,1)}(n)|_{q=1} = 4 · χ̃_{(2,1)}(p)|_{q=1}`). -/
theorem chi21Reduced_ratio_at_one (h2 : (2 : K) ≠ 0) :
    3 * (4 * chi21ReducedNeutron (1 : K)) = 4 * (4 * chi21ReducedProton (1 : K)) := by
  rw [four_mul_chi21ReducedNeutron_at_one h2, four_mul_chi21ReducedProton_at_one h2]
  ring

end NucleonSectorObservables

end QOU.BraidsAndKnots.NucleonIdempotentModifiedTrace
