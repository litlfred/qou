import QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
import QOU.Eightfold.ColemanGlashowIdentity
import QOU.Eightfold.OctetWeightDegeneracy

/-!
# Eightfold Way U-Spin Charge Invariance, Microscopic Coleman–Glashow Borromean `V³` QED Identity, and `Λ–Σ⁰` `e_{(2,1)}` Sub-Projector Resolution

This module bridges the abstract Eightfold Way files (`ColemanGlashowIdentity.lean` and
`OctetWeightDegeneracy.lean`) to the microscopic three-strand weight-space and Hecke-idempotent
calculus of `NucleonWeightSpaceTwoTerm.lean`:

1. **Three-Flavor (`u, d, s`) Quark Charges & Exact U-Spin Charge Invariance**:
   Defines the rational quark charges `qUp = +2/3`, `qDown = -1/3`, `qStrange = -1/3` over any
   `[Field K]`, proves exact U-spin charge invariance `qDown = qStrange`, and constructs the
   three-strand adjacent pairwise charge operators `Q₁₂`, `Q₂₃`, and `Q_Adj = Q₁₂ + Q₂₃` for all
   six outer baryon-octet states (`p = uud`, `Σ⁺ = uus`, `n = udd`, `Ξ⁰ = uss`, `Σ⁻ = dds`,
   `Ξ⁻ = dss`). Proves exact U-spin operator equality on the `3×3` weight spaces:
   `QAdjSigmaPlus = QAdjp`, `QAdjXiZero = QAdjn`, and
   `QAdjSigmaMinus = QAdjXiMinus = (2/9) • I₃`.

2. **Microscopic Connected Borromean `V³` Realization of the Coleman–Glashow QED Relation**:
   Evaluates the connected fourth-order `(q - 1)⁴` Borromean braid `V³ = (σ₁ σ₂⁻¹)³`
   electromagnetic trace on all six outer octet baryons, proves the closed-form polynomial
   expressions for all three individual electromagnetic doublet splittings (`p - n`,
   `Σ⁺ - Σ⁻`, `Ξ⁰ - Ξ⁻`), proves that all three individual splittings are non-zero (witnessed
   at `q = 2` over `ℚ`), and proves that their alternating Coleman–Glashow combination vanishes
   identically for all `q` (`coleman_glashow_borromeanV3_connected`), realizing premises (P1) and
   (P2) of `QOU.Eightfold.ColemanGlashowIdentity.cgCombination` from microscopic braid traces.

3. **Operator Resolution of the `Λ–Σ⁰` `(0, 0)` Weight Degeneracy Inside `e_{(2,1)}`**:
   In `QOU.Eightfold.OctetWeightDegeneracy`, `Λ` (`I = 0`) and `Σ⁰` (`I = 1`) share the weight
   `(2I₃, Y) = (0, 0)` (`lambda_sigma0_same_weight`), so no function of the weight alone can
   separate them (`weight_function_cannot_separate_lambda_sigma0`). Inside the three-dimensional
   weight space, the rank-2 mixed-symmetry octet idempotent `e_{(2,1)}(q) = I₃ - e_{(3)}(q)` splits
   into two mutually orthogonal rank-1 Hecke sub-idempotents `e_Λ(q)` (`A₁`-eigenvalue `-q⁻¹`,
   antisymmetric `I = 0` singlet on the `(1,2)` `u–d` pair) and `e_{Σ⁰}(q) = e_{(2,1)}(q) - e_Λ(q)`
   (`A₁`-eigenvalue `+q`, symmetric `I = 1` triplet on the `(1,2)` `u–d` pair, orthogonal to the
   decuplet `e_{(3)}(q)`). Proves idempotency, mutual orthogonality, rank-1 traces, opposite
   `A₁`-eigenvalues (`tr(e_{Σ⁰} A₁) - tr(e_Λ A₁) = q + q⁻¹ ≠ 0`), and the identity
   `tr(e_Λ(q) A₂(q)) = q³ / (q² + 1) = z_D` connecting the `I = 0` `Λ` sub-projector on the second
   crossing `A₂(q)` to the Convention-D Markov trace parameter `z_D`.

Conventions: generic `[Field K]` per `AGENTS.md` §7c — pure field and matrix algebra with no
ordering, no `ℝ`, and no archimedean content.

-- Ref: [colemanglashow1961] Coleman & Glashow, Phys. Rev. Lett. 6 (1961) 423.
-- Ref: [gellmann1962] Gell-Mann, Phys. Rev. 125 (1962) 1067.
-/

namespace QOU.Eightfold.USpinColemanGlashowLambdaSigma

open Matrix
open QOU.BraidsAndKnots.NucleonWeightSpaceTraces
open QOU.BraidsAndKnots.NucleonWeightSpaceSecondOrder
open QOU.BraidsAndKnots.NucleonWeightSpaceTwoTerm
open QOU.Eightfold.ColemanGlashowIdentity
open QOU.Eightfold.OctetWeightDegeneracy

variable {K : Type*} [Field K]

/-! ## Section 1: 3-Flavor (`u, d, s`) Quark Charges & Exact U-Spin Charge Invariance -/

/-- Electric charge of the up quark `u`: `+2/3`. -/
def qUp (K : Type*) [Field K] : K := (2 : K) / 3

/-- Electric charge of the down quark `d`: `-1/3`. -/
def qDown (K : Type*) [Field K] : K := -(1 : K) / 3

/-- Electric charge of the strange quark `s`: `-1/3`. -/
def qStrange (K : Type*) [Field K] : K := -(1 : K) / 3

/-- **Exact U-spin electric charge invariance (`d ↔ s`)**: the down and strange quarks carry
identical electric charge `-1/3`. -/
theorem uSpin_charge_invariance : qDown K = qStrange K := rfl

/-- Sum of the three fundamental quark charges vanishes (`Q_u + Q_d + Q_s = 0`). -/
theorem sum_three_flavor_charges_eq_zero :
    qUp K + qDown K + qStrange K = 0 := by
  unfold qUp qDown qStrange
  ring

/-- Helper rewriting `(a / 3) * (b / 3) = (a * b) / 9` over any `[Field K]` via `_root_.mul_inv_rev`. -/
theorem div_three_mul_div_three (a b : K) :
    (a / 3) * (b / 3) = (a * b) / 9 := by
  have h9 : (9 : K) = 3 * 3 := by norm_num
  rw [h9, div_eq_mul_inv, div_eq_mul_inv, div_eq_mul_inv, _root_.mul_inv_rev]
  ring

/-- Adjacent pairwise charge sum `Q_Adj^{(p)} = Q₁₂^{(p)} + Q₂₃^{(p)}` on the proton `p = (u,u,d)`
weight space (basis `|uud⟩, |udu⟩, |duu⟩`). -/
def QAdjp : Matrix (Fin 3) (Fin 3) K := Q12p + Q23p

/-- Adjacent pairwise charge sum `Q_Adj^{(n)} = Q₁₂^{(n)} + Q₂₃^{(n)}` on the neutron `n = (u,d,d)`
weight space (basis `|udd⟩, |dud⟩, |ddu⟩`). -/
def QAdjn : Matrix (Fin 3) (Fin 3) K := Q12n + Q23n

/-- Pairwise charge operator `Q₁₂^{(Σ⁺)}` on the `Σ⁺ = (u,u,s)` weight space
(basis `|uus⟩, |usu⟩, |suu⟩`), built directly from `qUp` and `qStrange`. -/
def Q12SigmaPlus : Matrix (Fin 3) (Fin 3) K :=
  !![qUp K * qUp K, 0, 0;
     0, qUp K * qStrange K, 0;
     0, 0, qStrange K * qUp K]

/-- Pairwise charge operator `Q₂₃^{(Σ⁺)}` on the `Σ⁺ = (u,u,s)` weight space
(basis `|uus⟩, |usu⟩, |suu⟩`), built directly from `qUp` and `qStrange`. -/
def Q23SigmaPlus : Matrix (Fin 3) (Fin 3) K :=
  !![qUp K * qStrange K, 0, 0;
     0, qStrange K * qUp K, 0;
     0, 0, qUp K * qUp K]

/-- Adjacent pairwise charge sum `Q_Adj^{(Σ⁺)} = Q₁₂^{(Σ⁺)} + Q₂₃^{(Σ⁺)}` on `Σ⁺ = (u,u,s)`. -/
def QAdjSigmaPlus : Matrix (Fin 3) (Fin 3) K := Q12SigmaPlus + Q23SigmaPlus

/-- Pairwise charge operator `Q₁₂^{(Ξ⁰)}` on the `Ξ⁰ = (u,s,s)` weight space
(basis `|uss⟩, |sus⟩, |ssu⟩`), built directly from `qUp` and `qStrange`. -/
def Q12XiZero : Matrix (Fin 3) (Fin 3) K :=
  !![qUp K * qStrange K, 0, 0;
     0, qStrange K * qUp K, 0;
     0, 0, qStrange K * qStrange K]

/-- Pairwise charge operator `Q₂₃^{(Ξ⁰)}` on the `Ξ⁰ = (u,s,s)` weight space
(basis `|uss⟩, |sus⟩, |ssu⟩`), built directly from `qUp` and `qStrange`. -/
def Q23XiZero : Matrix (Fin 3) (Fin 3) K :=
  !![qStrange K * qStrange K, 0, 0;
     0, qUp K * qStrange K, 0;
     0, 0, qStrange K * qUp K]

/-- Adjacent pairwise charge sum `Q_Adj^{(Ξ⁰)} = Q₁₂^{(Ξ⁰)} + Q₂₃^{(Ξ⁰)}` on `Ξ⁰ = (u,s,s)`. -/
def QAdjXiZero : Matrix (Fin 3) (Fin 3) K := Q12XiZero + Q23XiZero

/-- Pairwise charge operator `Q₁₂^{(Σ⁻)}` on the `Σ⁻ = (d,d,s)` weight space
(basis `|dds⟩, |dsd⟩, |sdd⟩`), built directly from `qDown` and `qStrange`. -/
def Q12SigmaMinus : Matrix (Fin 3) (Fin 3) K :=
  !![qDown K * qDown K, 0, 0;
     0, qDown K * qStrange K, 0;
     0, 0, qStrange K * qDown K]

/-- Pairwise charge operator `Q₂₃^{(Σ⁻)}` on the `Σ⁻ = (d,d,s)` weight space
(basis `|dds⟩, |dsd⟩, |sdd⟩`), built directly from `qDown` and `qStrange`. -/
def Q23SigmaMinus : Matrix (Fin 3) (Fin 3) K :=
  !![qDown K * qStrange K, 0, 0;
     0, qStrange K * qDown K, 0;
     0, 0, qDown K * qDown K]

/-- Adjacent pairwise charge sum `Q_Adj^{(Σ⁻)} = Q₁₂^{(Σ⁻)} + Q₂₃^{(Σ⁻)}` on `Σ⁻ = (d,d,s)`. -/
def QAdjSigmaMinus : Matrix (Fin 3) (Fin 3) K := Q12SigmaMinus + Q23SigmaMinus

/-- Pairwise charge operator `Q₁₂^{(Ξ⁻)}` on the `Ξ⁻ = (d,s,s)` weight space
(basis `|dss⟩, |sds⟩, |ssd⟩`), built directly from `qDown` and `qStrange`. -/
def Q12XiMinus : Matrix (Fin 3) (Fin 3) K :=
  !![qDown K * qStrange K, 0, 0;
     0, qStrange K * qDown K, 0;
     0, 0, qStrange K * qStrange K]

/-- Pairwise charge operator `Q₂₃^{(Ξ⁻)}` on the `Ξ⁻ = (d,s,s)` weight space
(basis `|dss⟩, |sds⟩, |ssd⟩`), built directly from `qDown` and `qStrange`. -/
def Q23XiMinus : Matrix (Fin 3) (Fin 3) K :=
  !![qStrange K * qStrange K, 0, 0;
     0, qDown K * qStrange K, 0;
     0, 0, qStrange K * qDown K]

/-- Adjacent pairwise charge sum `Q_Adj^{(Ξ⁻)} = Q₁₂^{(Ξ⁻)} + Q₂₃^{(Ξ⁻)}` on `Ξ⁻ = (d,s,s)`. -/
def QAdjXiMinus : Matrix (Fin 3) (Fin 3) K := Q12XiMinus + Q23XiMinus

/-- U-spin equality of the `(1,2)` pairwise charge matrices for `Σ⁺ = (u,u,s)` and `p = (u,u,d)`. -/
theorem Q12SigmaPlus_eq_Q12p :
    (Q12SigmaPlus : Matrix (Fin 3) (Fin 3) K) = Q12p := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Q12SigmaPlus, Q12p, qUp, qStrange, div_three_mul_div_three]; try ring)

/-- U-spin equality of the `(2,3)` pairwise charge matrices for `Σ⁺ = (u,u,s)` and `p = (u,u,d)`. -/
theorem Q23SigmaPlus_eq_Q23p :
    (Q23SigmaPlus : Matrix (Fin 3) (Fin 3) K) = Q23p := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Q23SigmaPlus, Q23p, qUp, qStrange, div_three_mul_div_three]; try ring)

/-- **U-spin doublet `p ↔ Σ⁺` (`Q = +1`) operator equality**: `Q_Adj^{(Σ⁺)} = Q_Adj^{(p)}`. -/
theorem QAdjSigmaPlus_eq_QAdjp :
    (QAdjSigmaPlus : Matrix (Fin 3) (Fin 3) K) = QAdjp := by
  rw [QAdjSigmaPlus, QAdjp, Q12SigmaPlus_eq_Q12p, Q23SigmaPlus_eq_Q23p]

/-- U-spin equality of the `(1,2)` pairwise charge matrices for `Ξ⁰ = (u,s,s)` and `n = (u,d,d)`. -/
theorem Q12XiZero_eq_Q12n :
    (Q12XiZero : Matrix (Fin 3) (Fin 3) K) = Q12n := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Q12XiZero, Q12n, qUp, qStrange, div_three_mul_div_three]; try ring)

/-- U-spin equality of the `(2,3)` pairwise charge matrices for `Ξ⁰ = (u,s,s)` and `n = (u,d,d)`. -/
theorem Q23XiZero_eq_Q23n :
    (Q23XiZero : Matrix (Fin 3) (Fin 3) K) = Q23n := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [Q23XiZero, Q23n, qUp, qStrange, div_three_mul_div_three]; try ring)

/-- **U-spin doublet `n ↔ Ξ⁰` (`Q = 0`) operator equality**: `Q_Adj^{(Ξ⁰)} = Q_Adj^{(n)}`. -/
theorem QAdjXiZero_eq_QAdjn :
    (QAdjXiZero : Matrix (Fin 3) (Fin 3) K) = QAdjn := by
  rw [QAdjXiZero, QAdjn, Q12XiZero_eq_Q12n, Q23XiZero_eq_Q23n]

/-- **U-spin doublet `Σ⁻ ↔ Ξ⁻` (`Q = -1`) operator equality**: `Q_Adj^{(Σ⁻)} = Q_Adj^{(Ξ⁻)}`. -/
theorem QAdjSigmaMinus_eq_QAdjXiMinus :
    (QAdjSigmaMinus : Matrix (Fin 3) (Fin 3) K) = QAdjXiMinus := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [QAdjSigmaMinus, QAdjXiMinus, Q12SigmaMinus, Q23SigmaMinus, Q12XiMinus, Q23XiMinus,
       ← uSpin_charge_invariance]

/-- On `Σ⁻ = (d,d,s)`, all three quark charges equal `-1/3`, so `Q_Adj^{(Σ⁻)}` is the pure scalar
matrix `(2/9) • I₃` with zero traceless connected part. -/
theorem QAdjSigmaMinus_eq_two_ninths_one :
    (QAdjSigmaMinus : Matrix (Fin 3) (Fin 3) K) =
      ((2 : K) / 9) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    (simp [QAdjSigmaMinus, Q12SigmaMinus, Q23SigmaMinus, qDown, qStrange,
      div_three_mul_div_three]; try ring)

/-- On `Ξ⁻ = (d,s,s)`, all three quark charges equal `-1/3`, so `Q_Adj^{(Ξ⁻)}` is likewise the
pure scalar matrix `(2/9) • I₃`. -/
theorem QAdjXiMinus_eq_two_ninths_one :
    (QAdjXiMinus : Matrix (Fin 3) (Fin 3) K) =
      ((2 : K) / 9) • (1 : Matrix (Fin 3) (Fin 3) K) := by
  rw [← QAdjSigmaMinus_eq_QAdjXiMinus, QAdjSigmaMinus_eq_two_ninths_one]

/-! ## Section 2: Microscopic Connected Borromean `V³` Realization of the Coleman–Glashow QED Relation -/

/-- Connected per-strand Borromean `V³` electromagnetic trace for the proton `p = (u,u,d)`
(where `tr(Q_Adj^{(p)}) = 0`, so the static background vanishes). -/
def trConnBor_p (q : K) : K :=
  (1 / 3 : K) * trace (QAdjp * borromeanV3A q)

/-- Connected per-strand Borromean `V³` electromagnetic trace for `Σ⁺ = (u,u,s)`. -/
def trConnBor_SigmaPlus (q : K) : K :=
  (1 / 3 : K) * trace (QAdjSigmaPlus * borromeanV3A q)

/-- Connected per-strand Borromean `V³` electromagnetic trace for the neutron `n = (u,d,d)`
(with static background `(-2/9) I₃` subtracted). -/
def trConnBor_n (q : K) : K :=
  (1 / 3 : K) * (trace (QAdjn * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q))

/-- Connected per-strand Borromean `V³` electromagnetic trace for `Ξ⁰ = (u,s,s)`
(with static background `(-2/9) I₃` subtracted). -/
def trConnBor_XiZero (q : K) : K :=
  (1 / 3 : K) * (trace (QAdjXiZero * borromeanV3B q) + (2 / 9 : K) * trace (borromeanV3B q))

/-- Connected per-strand Borromean `V³` electromagnetic trace for `Σ⁻ = (d,d,s)`
(with static background `(+2/9) I₃` subtracted). -/
def trConnBor_SigmaMinus (q : K) : K :=
  (1 / 3 : K) * (trace (QAdjSigmaMinus * borromeanV3A q) - (2 / 9 : K) * trace (borromeanV3A q))

/-- Connected per-strand Borromean `V³` electromagnetic trace for `Ξ⁻ = (d,s,s)`
(with static background `(+2/9) I₃` subtracted). -/
def trConnBor_XiMinus (q : K) : K :=
  (1 / 3 : K) * (trace (QAdjXiMinus * borromeanV3A q) - (2 / 9 : K) * trace (borromeanV3A q))

/-- U-spin invariance of the connected Borromean `V³` trace on the `Q = +1` doublet `p ↔ Σ⁺`. -/
theorem trConnBor_SigmaPlus_eq_p (q : K) :
    trConnBor_SigmaPlus q = trConnBor_p q := by
  rw [trConnBor_SigmaPlus, trConnBor_p, QAdjSigmaPlus_eq_QAdjp]

/-- U-spin invariance of the connected Borromean `V³` trace on the `Q = 0` doublet `n ↔ Ξ⁰`. -/
theorem trConnBor_XiZero_eq_n (q : K) :
    trConnBor_XiZero q = trConnBor_n q := by
  rw [trConnBor_XiZero, trConnBor_n, QAdjXiZero_eq_QAdjn]

/-- U-spin invariance of the connected Borromean `V³` trace on the `Q = -1` doublet `Σ⁻ ↔ Ξ⁻`. -/
theorem trConnBor_SigmaMinus_eq_XiMinus (q : K) :
    trConnBor_SigmaMinus q = trConnBor_XiMinus q := by
  rw [trConnBor_SigmaMinus, trConnBor_XiMinus, QAdjSigmaMinus_eq_QAdjXiMinus]

/-- Because `Σ⁻ = (d,d,s)` has three equal-charge `-1/3` quarks, its connected fourth-order
Borromean `V³` trace vanishes identically. -/
theorem trConnBor_SigmaMinus_eq_zero (q : K) :
    trConnBor_SigmaMinus q = 0 := by
  unfold trConnBor_SigmaMinus
  rw [QAdjSigmaMinus_eq_two_ninths_one, Matrix.smul_mul, Matrix.one_mul,
      Matrix.trace_smul, smul_eq_mul, sub_self, mul_zero]

/-- Because `Ξ⁻ = (d,s,s)` has three equal-charge `-1/3` quarks, its connected fourth-order
Borromean `V³` trace vanishes identically. -/
theorem trConnBor_XiMinus_eq_zero (q : K) :
    trConnBor_XiMinus q = 0 := by
  rw [← trConnBor_SigmaMinus_eq_XiMinus, trConnBor_SigmaMinus_eq_zero]

/-- Closed-form connected Borromean `V³` electromagnetic trace for the proton `p = (u,u,d)`. -/
theorem trConnBor_p_closed (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_p q =
      -2 * (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (27 * q ^ 6) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  have h9 : (9 : K) = 3 * 3 := by ring
  unfold trConnBor_p QAdjp
  rw [trace_QAdjp_borromeanV3 q hq h3, h27, h9]
  field_simp

/-- Closed-form connected Borromean `V³` electromagnetic trace for `Σ⁺ = (u,u,s)`. -/
theorem trConnBor_SigmaPlus_closed (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_SigmaPlus q =
      -2 * (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (27 * q ^ 6) := by
  rw [trConnBor_SigmaPlus_eq_p, trConnBor_p_closed q hq h3]

/-- Closed-form connected Borromean `V³` electromagnetic trace for the neutron `n = (u,d,d)`. -/
theorem trConnBor_n_closed (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_n q =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (27 * q ^ 6) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  have h9 : (9 : K) = 3 * 3 := by ring
  unfold trConnBor_n QAdjn
  rw [trace_QAdjn_borromeanV3_connected q hq h3, h27, h9]
  field_simp

/-- Closed-form connected Borromean `V³` electromagnetic trace for `Ξ⁰ = (u,s,s)`. -/
theorem trConnBor_XiZero_closed (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_XiZero q =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (27 * q ^ 6) := by
  rw [trConnBor_XiZero_eq_n, trConnBor_n_closed q hq h3]

/-- **Nucleon doublet (`p - n`) connected Borromean `V³` electromagnetic splitting**:
`\overline{tr}_{conn}(p) - \overline{tr}_{conn}(n) = -(q-1)⁴(q+1)⁴(4q⁴ + q² + 4) / (27 q⁶)`. -/
theorem trConnBor_p_sub_n (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_p q - trConnBor_n q =
      -(q - 1) ^ 4 * (q + 1) ^ 4 * (4 * q ^ 4 + q ^ 2 + 4) / (27 * q ^ 6) := by
  have h27 : (27 : K) = 3 * 3 * 3 := by ring
  rw [trConnBor_p_closed q hq h3, trConnBor_n_closed q hq h3, h27]
  field_simp; ring

/-- **Sigma doublet (`Σ⁺ - Σ⁻`) connected Borromean `V³` electromagnetic splitting**:
`\overline{tr}_{conn}(Σ⁺) - \overline{tr}_{conn}(Σ⁻) = -2(q-1)⁴(q+1)⁴(q⁴ + q² + 1) / (27 q⁶)`. -/
theorem trConnBor_SigmaPlus_sub_SigmaMinus (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_SigmaPlus q - trConnBor_SigmaMinus q =
      -2 * (q - 1) ^ 4 * (q + 1) ^ 4 * (q ^ 4 + q ^ 2 + 1) / (27 * q ^ 6) := by
  rw [trConnBor_SigmaPlus_closed q hq h3, trConnBor_SigmaMinus_eq_zero, sub_zero]

/-- **Cascade doublet (`Ξ⁰ - Ξ⁻`) connected Borromean `V³` electromagnetic splitting**:
`\overline{tr}_{conn}(Ξ⁰) - \overline{tr}_{conn}(Ξ⁻) = +(q-1)⁴(q+1)⁴(2q⁴ - q² + 2) / (27 q⁶)`. -/
theorem trConnBor_XiZero_sub_XiMinus (q : K) (hq : q ≠ 0) (h3 : (3 : K) ≠ 0) :
    trConnBor_XiZero q - trConnBor_XiMinus q =
      (q - 1) ^ 4 * (q + 1) ^ 4 * (2 * q ^ 4 - q ^ 2 + 2) / (27 * q ^ 6) := by
  rw [trConnBor_XiZero_closed q hq h3, trConnBor_XiMinus_eq_zero, sub_zero]

/-- **Microscopic Connected Borromean `V³` Coleman–Glashow QED Identity**:
Although each of the three doublet splittings `p - n`, `Σ⁺ - Σ⁻`, and `Ξ⁰ - Ξ⁻` is a non-zero
rational function of `q` with distinct numerator polynomials `-(4q⁴ + q² + 4)`, `-2(q⁴ + q² + 1)`,
and `+(2q⁴ - q² + 2)`, their alternating Coleman–Glashow combination vanishes identically. -/
theorem coleman_glashow_borromeanV3_connected (q : K) :
    (trConnBor_p q - trConnBor_n q) -
      (trConnBor_SigmaPlus q - trConnBor_SigmaMinus q) +
      (trConnBor_XiZero q - trConnBor_XiMinus q) = 0 := by
  rw [trConnBor_SigmaPlus_eq_p, trConnBor_XiZero_eq_n, trConnBor_SigmaMinus_eq_XiMinus]
  ring

/-- Bridge from the microscopic connected Borromean `V³` traces to
`QOU.Eightfold.ColemanGlashowIdentity.cgCombination`: for any strong isospin-multiplet masses
`N, S, X`, evaluating `cgCombination` on the U-spin Borromean electromagnetic shifts reproduces the
microscopic Borromean Coleman–Glashow combination and vanishes identically. -/
theorem coleman_glashow_borromeanV3_via_cgCombination (N S X q : K) :
    cgCombination N S X (trConnBor_p q) (trConnBor_n q) (trConnBor_SigmaMinus q) =
      (trConnBor_p q - trConnBor_n q) -
        (trConnBor_SigmaPlus q - trConnBor_SigmaMinus q) +
        (trConnBor_XiZero q - trConnBor_XiMinus q) := by
  rw [coleman_glashow_identity, coleman_glashow_borromeanV3_connected]

/-- Non-degeneracy witness over `ℚ` at `q = 2`: all three individual connected Borromean `V³`
doublet splittings (`p - n`, `Σ⁺ - Σ⁻`, `Ξ⁰ - Ξ⁻`) are strictly non-zero while their alternating
Coleman–Glashow sum is zero. -/
theorem borromeanV3_all_three_doublet_splittings_nonzero_at_two :
    trConnBor_p (2 : ℚ) - trConnBor_n (2 : ℚ) ≠ 0 ∧
      trConnBor_SigmaPlus (2 : ℚ) - trConnBor_SigmaMinus (2 : ℚ) ≠ 0 ∧
      trConnBor_XiZero (2 : ℚ) - trConnBor_XiMinus (2 : ℚ) ≠ 0 := by
  have h2 : (2 : ℚ) ≠ 0 := by norm_num
  have h3 : (3 : ℚ) ≠ 0 := by norm_num
  rw [trConnBor_p_sub_n (2 : ℚ) h2 h3,
      trConnBor_SigmaPlus_sub_SigmaMinus (2 : ℚ) h2 h3,
      trConnBor_XiZero_sub_XiMinus (2 : ℚ) h2 h3]
  norm_num

/-! ## Section 3: Operator Resolution of the `Λ–Σ⁰` `(0, 0)` Weight Degeneracy Inside `e_{(2,1)}` -/

/-- Balanced quantum integer `[2]_q = q + q⁻¹`. -/
def qInt2 (q : K) : K := q + q⁻¹

theorem qInt2_eq_div (q : K) (hq : q ≠ 0) :
    qInt2 q = (q ^ 2 + 1) / q := by
  unfold qInt2; field_simp

theorem q2_add_one_ne_zero (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    q ^ 2 + 1 ≠ 0 := by
  intro h
  apply hq2
  rw [qInt2_eq_div q hq, h, zero_div]

/-- The `I = 0` (`Λ`-like) rank-1 sub-idempotent inside `e_{(2,1)}^p(q)`, projecting onto the
`-q⁻¹` antisymmetric singlet eigenspace of the `(1,2)` pair crossing `A₁(q)`. -/
def eLambda (q : K) : Matrix (Fin 3) (Fin 3) K :=
  (qInt2 q)⁻¹ • (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q)

/-- The `I = 1` (`Σ⁰`-like) rank-1 sub-idempotent inside `e_{(2,1)}^p(q)`, defined as the
orthogonal complement `e_{(2,1)}^p(q) - e_Λ(q)` inside the mixed-symmetry octet space. -/
def eSigma0 (q : K) : Matrix (Fin 3) (Fin 3) K :=
  e21p q - eLambda q

/-- Orthogonal decomposition of the rank-2 mixed-symmetry octet projector `e_{(2,1)}^p(q)` into
its `I = 0` (`e_Λ`) and `I = 1` (`e_{Σ⁰}`) sub-idempotents. -/
theorem eLambda_add_eSigma0 (q : K) :
    eLambda q + eSigma0 q = e21p q := by
  unfold eSigma0; abel

/-- Unnormalized quadratic identity `(q I₃ - A₁(q))² = (q + q⁻¹) • (q I₃ - A₁(q))`. -/
theorem q_sub_A1_mul_self (q : K) (hq : q ≠ 0) :
    (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) *
      (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) =
      qInt2 q • (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [A₁, qInt2, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- Idempotency of the `I = 0` `Λ` sub-projector: `e_Λ(q)² = e_Λ(q)`. -/
theorem eLambda_mul_self (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    eLambda q * eLambda q = eLambda q := by
  unfold eLambda
  rw [Matrix.smul_mul, Matrix.mul_smul, q_sub_A1_mul_self q hq, smul_smul, smul_smul]
  have hinv : (qInt2 q)⁻¹ * (qInt2 q)⁻¹ * qInt2 q = (qInt2 q)⁻¹ := by
    rw [mul_assoc, inv_mul_cancel₀ hq2, mul_one]
  rw [hinv]

/-- Rank trace of `e_Λ(q)`: `tr(e_Λ(q)) = 1`. -/
theorem trace_eLambda (q : K) (hq2 : qInt2 q ≠ 0) :
    trace (eLambda q) = 1 := by
  have htr : trace (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) = qInt2 q := by
    simp [A₁, qInt2, Matrix.trace_fin_three]; ring
  unfold eLambda
  rw [Matrix.trace_smul, htr, smul_eq_mul, inv_mul_cancel₀ hq2]

/-- The decuplet operator `FE_p(q)` lies in the `+q` symmetric eigenspace of `A₁(q)`, so
`FE_p(q) * (q I₃ - A₁(q)) = 0`. -/
theorem FEp_mul_q_sub_A1 (q : K) (hq : q ≠ 0) :
    FEp q * (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [FEp, A₁, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- And `(q I₃ - A₁(q)) * FE_p(q) = 0`. -/
theorem q_sub_A1_mul_FEp (q : K) (hq : q ≠ 0) :
    (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) * FEp q = 0 := by
  ext i j; fin_cases i <;> fin_cases j <;>
    simp [FEp, A₁, Matrix.mul_apply, Fin.sum_univ_three] <;>
    field_simp <;> ring

/-- Orthogonality of the decuplet projector `e_{(3)}^p(q)` and `e_Λ(q)`: `e_{(3)}^p * e_Λ = 0`. -/
theorem e3p_mul_eLambda (q : K) (hq : q ≠ 0) :
    e3p q * eLambda q = 0 := by
  unfold e3p eLambda
  rw [Matrix.smul_mul, Matrix.mul_smul, FEp_mul_q_sub_A1 q hq, smul_zero, smul_zero]

/-- Orthogonality of `e_Λ(q)` and the decuplet projector `e_{(3)}^p(q)`: `e_Λ * e_{(3)}^p = 0`. -/
theorem eLambda_mul_e3p (q : K) (hq : q ≠ 0) :
    eLambda q * e3p q = 0 := by
  unfold eLambda e3p
  rw [Matrix.smul_mul, Matrix.mul_smul, q_sub_A1_mul_FEp q hq, smul_zero, smul_zero]

/-- Because `e_Λ(q)` is orthogonal to `e_{(3)}^p(q)`, `e_Λ(q)` is absorbed by `e_{(2,1)}^p(q)`:
`e_{(2,1)}^p(q) * e_Λ(q) = e_Λ(q)`. -/
theorem e21p_mul_eLambda (q : K) (hq : q ≠ 0) :
    e21p q * eLambda q = eLambda q := by
  unfold e21p
  rw [Matrix.sub_mul, Matrix.one_mul, e3p_mul_eLambda q hq, sub_zero]

/-- And `e_Λ(q) * e_{(2,1)}^p(q) = e_Λ(q)`. -/
theorem eLambda_mul_e21p (q : K) (hq : q ≠ 0) :
    eLambda q * e21p q = eLambda q := by
  unfold e21p
  rw [Matrix.mul_sub, Matrix.mul_one, eLambda_mul_e3p q hq, sub_zero]

/-- Mutual orthogonality of the `Λ` (`I = 0`) and `Σ⁰` (`I = 1`) sub-projectors inside `e_{(2,1)}`:
`e_Λ(q) * e_{Σ⁰}(q) = 0`. -/
theorem eLambda_mul_eSigma0 (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    eLambda q * eSigma0 q = 0 := by
  unfold eSigma0
  rw [Matrix.mul_sub, eLambda_mul_e21p q hq, eLambda_mul_self q hq hq2, sub_self]

/-- Mutual orthogonality in reverse order: `e_{Σ⁰}(q) * e_Λ(q) = 0`. -/
theorem eSigma0_mul_eLambda (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    eSigma0 q * eLambda q = 0 := by
  unfold eSigma0
  rw [Matrix.sub_mul, e21p_mul_eLambda q hq, eLambda_mul_self q hq hq2, sub_self]

/-- Idempotency of `e_{(2,1)}^p(q)`: `e_{(2,1)}^p(q)² = e_{(2,1)}^p(q)`. -/
theorem e21p_mul_self (q : K) (hq : q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    e21p q * e21p q = e21p q := by
  have hFE : FEp q * FEp q = qInt3 q • FEp q := by
    have hsec := FEp_sector q hq
    rw [mul_sub, Matrix.mul_smul, mul_one, sub_eq_zero] at hsec
    simpa [qInt3] using hsec
  have he3 : e3p q * e3p q = e3p q := by
    unfold e3p
    rw [Matrix.smul_mul, Matrix.mul_smul, hFE, smul_smul, smul_smul,
        mul_assoc, inv_mul_cancel₀ hq3, mul_one]
  unfold e21p
  rw [Matrix.sub_mul, Matrix.mul_sub, Matrix.mul_sub,
      Matrix.one_mul, Matrix.one_mul, Matrix.mul_one, he3]
  abel

/-- Idempotency of the `I = 1` `Σ⁰` sub-projector: `e_{Σ⁰}(q)² = e_{Σ⁰}(q)`. -/
theorem eSigma0_mul_self (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    eSigma0 q * eSigma0 q = eSigma0 q := by
  conv_lhs => rhs; unfold eSigma0
  rw [Matrix.mul_sub, eSigma0_mul_eLambda q hq hq2, sub_zero]
  unfold eSigma0
  rw [Matrix.sub_mul, e21p_mul_self q hq hq3, eLambda_mul_e21p q hq]

/-- Rank trace of `e_{Σ⁰}(q)`: `tr(e_{Σ⁰}(q)) = 1`. -/
theorem trace_eSigma0 (q : K) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (eSigma0 q) = 1 := by
  have hFE : trace (FEp q) = qInt3 q := by
    simp [FEp, qInt3, Matrix.trace_fin_three]; ring
  have he3 : trace (e3p q) = 1 := by
    unfold e3p
    rw [Matrix.trace_smul, hFE, smul_eq_mul, inv_mul_cancel₀ hq3]
  have h1 : trace (1 : Matrix (Fin 3) (Fin 3) K) = 3 := by
    rw [Matrix.trace_one, Fintype.card_fin]; norm_num
  unfold eSigma0 e21p
  rw [Matrix.trace_sub, Matrix.trace_sub, h1, he3, trace_eLambda q hq2]
  ring

/-- Eigenvalue action of the `(1,2)` crossing `A₁(q)` on `e_Λ(q)`: `e_Λ(q) * A₁(q) = -q⁻¹ • e_Λ(q)`. -/
theorem eLambda_mul_A1 (q : K) (hq : q ≠ 0) :
    eLambda q * A₁ q = (-q⁻¹) • eLambda q := by
  have hA1 :
      (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) * A₁ q =
        (-q⁻¹) • (q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) := by
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [A₁, Matrix.mul_apply, Fin.sum_univ_three]; try field_simp; try ring)
  unfold eLambda
  rw [Matrix.smul_mul, hA1, smul_comm]

/-- Eigenvalue action of the `(1,2)` crossing `A₁(q)` on `e_{Σ⁰}(q)`:
`e_{Σ⁰}(q) * A₁(q) = q • e_{Σ⁰}(q)`. -/
theorem eSigma0_mul_A1 (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    eSigma0 q * A₁ q = q • eSigma0 q := by
  have hFE : FEp q * A₁ q = q • FEp q := by
    have h0 := FEp_mul_q_sub_A1 q hq
    rw [Matrix.mul_sub, Matrix.mul_smul, Matrix.mul_one, sub_eq_zero] at h0
    exact h0.symm
  have he3 : e3p q * A₁ q = q • e3p q := by
    unfold e3p
    rw [Matrix.smul_mul, hFE, smul_comm]
  have h1_sub_eLambda :
      (1 : Matrix (Fin 3) (Fin 3) K) - eLambda q =
        (qInt2 q)⁻¹ • (A₁ q + q⁻¹ • (1 : Matrix (Fin 3) (Fin 3) K)) := by
    unfold eLambda
    have hid :
        (1 : Matrix (Fin 3) (Fin 3) K) =
          (qInt2 q)⁻¹ • (qInt2 q • (1 : Matrix (Fin 3) (Fin 3) K)) := by
      rw [smul_smul, inv_mul_cancel₀ hq2, one_smul]
    conv_lhs => lhs; rw [hid]
    rw [← smul_sub]
    congr 1
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [A₁, qInt2]; try ring)
  have hsym :
      (A₁ q + q⁻¹ • (1 : Matrix (Fin 3) (Fin 3) K)) * A₁ q =
        q • (A₁ q + q⁻¹ • (1 : Matrix (Fin 3) (Fin 3) K)) := by
    ext i j; fin_cases i <;> fin_cases j <;>
      (simp [A₁, Matrix.mul_apply, Fin.sum_univ_three]; try field_simp; try ring)
  have hrew : eSigma0 q = ((1 : Matrix (Fin 3) (Fin 3) K) - eLambda q) - e3p q := by
    unfold eSigma0 e21p; abel
  rw [hrew, Matrix.sub_mul, smul_sub, he3, h1_sub_eLambda, Matrix.smul_mul, hsym, smul_comm]

/-- Trace of the `(1,2)` crossing `A₁(q)` on the `I = 0` `Λ` sub-idempotent:
`tr(e_Λ(q) A₁(q)) = -q⁻¹`. -/
theorem trace_eLambda_A1 (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) :
    trace (eLambda q * A₁ q) = -q⁻¹ := by
  rw [eLambda_mul_A1 q hq, Matrix.trace_smul, trace_eLambda q hq2, smul_eq_mul, mul_one]

/-- Trace of the `(1,2)` crossing `A₁(q)` on the `I = 1` `Σ⁰` sub-idempotent:
`tr(e_{Σ⁰}(q) A₁(q)) = q`. -/
theorem trace_eSigma0_A1 (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (eSigma0 q * A₁ q) = q := by
  rw [eSigma0_mul_A1 q hq hq2, Matrix.trace_smul, trace_eSigma0 q hq2 hq3, smul_eq_mul, mul_one]

/-- **Operator separation of `Σ⁰` (`I = 1`) and `Λ` (`I = 0`) at weight `(0, 0)`**:
Although `weight_function_cannot_separate_lambda_sigma0` proves that no function of `(2I₃, Y)` can
separate `Σ⁰` and `Λ`, their Hecke sub-idempotents `e_{Σ⁰}(q)` and `e_Λ(q)` inside `e_{(2,1)}(q)`
separate them on the `(1,2)` pair crossing `A₁(q)` by `q - (-q⁻¹) = q + q⁻¹ = [2]_q ≠ 0`. -/
theorem trace_eSigma0_A1_sub_trace_eLambda_A1
    (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (eSigma0 q * A₁ q) - trace (eLambda q * A₁ q) = qInt2 q := by
  rw [trace_eSigma0_A1 q hq hq2 hq3, trace_eLambda_A1 q hq hq2]
  unfold qInt2; ring

theorem trace_eLambda_A1_ne_trace_eSigma0_A1
    (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (eLambda q * A₁ q) ≠ trace (eSigma0 q * A₁ q) := by
  intro h
  apply hq2
  rw [← trace_eSigma0_A1_sub_trace_eLambda_A1 q hq hq2 hq3, h, sub_self]

/-- **Convention-D bridge**: the trace of the `(2,3)` crossing `A₂(q)` on the `I = 0` `Λ`
sub-idempotent `e_Λ(q)` equals the Convention-D Markov trace specialization parameter
`z_D = q³ / (q² + 1)`. -/
theorem trace_eLambda_A2_eq_zD (q : K) (hq : q ≠ 0) :
    trace (eLambda q * A₂ q) = q ^ 3 / (q ^ 2 + 1) := by
  have htr : trace ((q • (1 : Matrix (Fin 3) (Fin 3) K) - A₁ q) * A₂ q) = q ^ 2 := by
    simp [A₁, A₂, Matrix.trace_fin_three, Matrix.mul_apply, Fin.sum_univ_three]
    field_simp; ring
  unfold eLambda
  rw [Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, htr, qInt2_eq_div q hq]
  field_simp

/-- And on the `I = 1` `Σ⁰` sub-idempotent `e_{Σ⁰}(q)`, the trace of `A₂(q)` is
`-1 / (q (q² + 1))`. -/
theorem trace_eSigma0_A2 (q : K) (hq : q ≠ 0) (hq2 : qInt2 q ≠ 0) (hq3 : qInt3 q ≠ 0) :
    trace (eSigma0 q * A₂ q) = -1 / (q * (q ^ 2 + 1)) := by
  have hq2_ne : q ^ 2 + 1 ≠ 0 := q2_add_one_ne_zero q hq hq2
  have hFE : trace (FEp q * A₂ q) = q * qInt3 q := by
    simp [FEp, A₂, qInt3, Matrix.trace_fin_three]; field_simp; ring
  have he3 : trace (e3p q * A₂ q) = q := by
    unfold e3p
    rw [Matrix.smul_mul, Matrix.trace_smul, smul_eq_mul, hFE,
        ← mul_assoc, mul_comm (qInt3 q)⁻¹ q, mul_assoc, inv_mul_cancel₀ hq3, mul_one]
  have hA2 : trace (A₂ q) = 2 * q - q⁻¹ := by
    simp [A₂, Matrix.trace_fin_three]; ring
  unfold eSigma0 e21p
  rw [Matrix.sub_mul, Matrix.sub_mul, Matrix.one_mul, Matrix.trace_sub, Matrix.trace_sub,
      hA2, he3, trace_eLambda_A2_eq_zD q hq]
  field_simp; ring

end QOU.Eightfold.USpinColemanGlashowLambdaSigma
