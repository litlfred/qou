import Mathlib.LinearAlgebra.Matrix.Kronecker
import Mathlib.LinearAlgebra.Matrix.Trace
import Mathlib.Tactic

/-!
# The lepton two-term trace, derived the way the nucleon one was (bean `qou-99qc`)

Owner, 2026-11-21: *"The two term came out from looking at the Lagrangian and tracking through
non-abelian Stokes. Do the same for the lepton."*

The nucleon chain (`CategoricalLagrangianTwoTermBridge`, `NucleonQEDCovariance`,
`NucleonWeightSpaceQTrace`) has three algebraic steps that this file repeats with a lepton strand:

1. **Pairs (§1).** The Reeb contraction of the connection on a tensor product of strand objects is
   additive (Leibniz rule), so the charge is `Q_tot = Σ_a Q_a`. The second-order term is its square,
   whose cross terms are *every* pair of strands with weight 2, with no species distinction.
2. **Covariance (§2, §3).** Under non-abelian Stokes the insertion is carried along the closed
   boundary word, so its value is basepoint independent only if it commutes with every crossing it is
   carried through, with each strand's charge carried along with the strand. On two `C²` strands with
   the Jimbo crossing `Ř`, a diagonal operator is carried through `Ř` iff four entry conditions and one
   `h`-weighted condition hold (`diag_carry_iff`). For the species-weighted quadratic charge insertion
   `α₁Q₁² + α₂Q₂² + βQ₁Q₂`, `Q_a = T³_a + y_a/2` (stated on `2Q` to avoid `1/2`), the condition is
   `h·((2α₁ − β)y₁ − (2α₂ − β)y₂) = 0` up to a factor 2 (`quad_carry_iff`), `h = q − q⁻¹`.
   With a spectator strand the pair weights must agree (`pairWeight_uniform`).
3. **Consequences (§4).**
   * Equal hypercharges (three quarks): every such insertion is carried, so the ruled all-pairs
     insertion is admissible (`pairOnly_quark_quark_carried`).
   * A quark–lepton crossing (`y = 1/3` vs `−1`): the pairs-only insertion is **not** carried for
     `h ≠ 0` (`pairOnly_quark_lepton_not_carried`). Keeping the ruled quark self-weight `0`, the
     lepton self-weight is forced to `2β/3` (`lepton_self_weight_forced`).
   * The admissible family is `(β/2)Q_tot² + κ Σ_a Q_a²/y_a`; on spin-½ strands it is a function of
     `T³_tot` and the species content only (`natVal_eq_totals`), so it is a scalar on every total-weight
     space, its connected part vanishes for every word (`connected_zero_of_scalar`), and it takes the
     same value on `n⊗ν` and `p⊗e⁻` (`natural_beta_split_zero`). The pairs-only insertion would split
     them by `2/3` (`pairOnly_beta_split`).
   * A strand that braids under the same `Ř` but carries charge `0` on both states (a "neutral"
     doublet) cannot be carried (`singleCharge_not_carried`): the charge coupling must contain `T³`
     with the same coefficient on every braided strand.

All statements are over a generic field `R`; the `Ř` here is the same matrix as
`QOU.BraidsAndKnots.NucleonWeightSpaceQTrace.crossingR` (basis `uu, ud, du, dd`), restated to keep the
import cone to Mathlib. No numerical value enters.
-/

namespace QOU.QBeta.LeptonTwoTermStokesCovariance

open Matrix
open scoped Kronecker

variable {R : Type*} [Field R]

/-! ## §1. Pairs: the square of the additive (Leibniz) charge -/

/-- Three quarks and one lepton: the square of the total charge is the self terms plus twice every
pair, quark–quark and quark–lepton alike, each with weight 1. -/
theorem sq_total_four (q₁ q₂ q₃ ℓ : R) :
    (q₁ + q₂ + q₃ + ℓ) ^ 2 =
      (q₁ ^ 2 + q₂ ^ 2 + q₃ ^ 2 + ℓ ^ 2) +
        2 * ((q₁ * q₂ + q₁ * q₃ + q₂ * q₃) + (q₁ * ℓ + q₂ * ℓ + q₃ * ℓ)) := by
  ring

/-- The same split on three strands (the nucleon). -/
theorem sq_total_three (q₁ q₂ q₃ : R) :
    (q₁ + q₂ + q₃) ^ 2 = (q₁ ^ 2 + q₂ ^ 2 + q₃ ^ 2) + 2 * (q₁ * q₂ + q₁ * q₃ + q₂ * q₃) := by
  ring

/-! ## §2. Carrying a diagonal insertion through one crossing -/

/-- The Jimbo crossing on `C² ⊗ C²`, basis `uu, ud, du, dd`. -/
def crossingR (q : R) : Matrix (Fin 4) (Fin 4) R :=
  !![q, 0, 0, 0; 0, 0, 1, 0; 0, 1, q - q⁻¹, 0; 0, 0, 0, q]

/-- The defect of carrying `diagonal d` through `Ř` into `diagonal d'`. -/
theorem diag_defect (q : R) (d d' : Fin 4 → R) :
    crossingR q * diagonal d - diagonal d' * crossingR q =
      !![q * (d 0 - d' 0), 0, 0, 0;
         0, 0, d 2 - d' 1, 0;
         0, d 1 - d' 2, (q - q⁻¹) * (d 2 - d' 2), 0;
         0, 0, 0, q * (d 3 - d' 3)] := by
  ext i j
  simp only [Matrix.sub_apply, Matrix.mul_diagonal, Matrix.diagonal_mul]
  fin_cases i <;> fin_cases j <;> simp [crossingR] <;> ring

/-- **Carry criterion.** `Ř · diag d = diag d' · Ř` iff the four permuted entries agree and
`h·(d₂ − d'₂) = 0`. -/
theorem diag_carry_iff (q : R) (hq : q ≠ 0) (d d' : Fin 4 → R) :
    crossingR q * diagonal d = diagonal d' * crossingR q ↔
      (d 0 = d' 0 ∧ d 2 = d' 1 ∧ d 1 = d' 2 ∧ (q - q⁻¹) * (d 2 - d' 2) = 0 ∧ d 3 = d' 3) := by
  rw [← sub_eq_zero, diag_defect]
  constructor
  · intro h
    have e00 := congrFun (congrFun h 0) 0
    have e12 := congrFun (congrFun h 1) 2
    have e21 := congrFun (congrFun h 2) 1
    have e22 := congrFun (congrFun h 2) 2
    have e33 := congrFun (congrFun h 3) 3
    simp at e00 e12 e21 e22 e33
    refine ⟨?_, sub_eq_zero.mp e12, sub_eq_zero.mp e21, mul_eq_zero.mpr e22, ?_⟩
    · rcases e00 with h0 | h0
      · exact absurd h0 hq
      · exact sub_eq_zero.mp h0
    · rcases e33 with h0 | h0
      · exact absurd h0 hq
      · exact sub_eq_zero.mp h0
  · rintro ⟨h0, h12, h21, h22, h3⟩
    have h0' : d 0 - d' 0 = 0 := sub_eq_zero.mpr h0
    have h12' : d 2 - d' 1 = 0 := sub_eq_zero.mpr h12
    have h21' : d 1 - d' 2 = 0 := sub_eq_zero.mpr h21
    have h3' : d 3 - d' 3 = 0 := sub_eq_zero.mpr h3
    ext i j
    fin_cases i <;> fin_cases j <;> simp [h0', h12', h21', h22, h3']

/-- Twice the charge of a doublet state: `2Q = 2T³ + y = ±1 + y` (`+` on `u`, `−` on `d`).
Working with `2Q` keeps every identity free of `1/2`, so nothing needs `char R ≠ 2`. -/
def chg2 (up : Bool) (y : R) : R := (if up then (1 : R) else -1) + y

/-- Per-state value of `α₁(2Q₁)² + α₂(2Q₂)² + β(2Q₁)(2Q₂)` on the basis `uu, ud, du, dd`
(strand 1 hypercharge `y₁`, strand 2 hypercharge `y₂`); this is `4·(α₁Q₁² + α₂Q₂² + βQ₁Q₂)`. -/
def quadVec (α₁ α₂ β y₁ y₂ : R) : Fin 4 → R :=
  ![α₁ * chg2 true y₁ ^ 2 + α₂ * chg2 true y₂ ^ 2 + β * chg2 true y₁ * chg2 true y₂,
    α₁ * chg2 true y₁ ^ 2 + α₂ * chg2 false y₂ ^ 2 + β * chg2 true y₁ * chg2 false y₂,
    α₁ * chg2 false y₁ ^ 2 + α₂ * chg2 true y₂ ^ 2 + β * chg2 false y₁ * chg2 true y₂,
    α₁ * chg2 false y₁ ^ 2 + α₂ * chg2 false y₂ ^ 2 + β * chg2 false y₁ * chg2 false y₂]

/-- **Quadratic carry criterion.** The insertion with the strand data carried through the crossing
(`(α₁, y₁)` moves to position 2) agrees iff `h·2·((2α₁ − β)y₁ − (2α₂ − β)y₂) = 0`. -/
theorem quad_carry_iff (q : R) (hq : q ≠ 0) (α₁ α₂ β y₁ y₂ : R) :
    crossingR q * diagonal (quadVec α₁ α₂ β y₁ y₂) =
        diagonal (quadVec α₂ α₁ β y₂ y₁) * crossingR q ↔
      (q - q⁻¹) * (2 * ((2 * α₁ - β) * y₁ - (2 * α₂ - β) * y₂)) = 0 := by
  rw [diag_carry_iff q hq]
  simp only [quadVec, chg2, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, if_true, Bool.false_eq_true,
    if_false]
  constructor
  · rintro ⟨-, -, -, h, -⟩
    linear_combination (-1 : R) * h
  · intro h
    refine ⟨by ring, by ring, by ring, ?_, by ring⟩
    linear_combination (-1 : R) * h

/-- Linear version: `c₁(2Q₁) + c₂(2Q₂)`. -/
def linVec (c₁ c₂ y₁ y₂ : R) : Fin 4 → R :=
  ![c₁ * chg2 true y₁ + c₂ * chg2 true y₂, c₁ * chg2 true y₁ + c₂ * chg2 false y₂,
    c₁ * chg2 false y₁ + c₂ * chg2 true y₂, c₁ * chg2 false y₁ + c₂ * chg2 false y₂]

theorem lin_carry_iff (q : R) (hq : q ≠ 0) (c₁ c₂ y₁ y₂ : R) :
    crossingR q * diagonal (linVec c₁ c₂ y₁ y₂) = diagonal (linVec c₂ c₁ y₂ y₁) * crossingR q ↔
      (q - q⁻¹) * (2 * (c₁ - c₂)) = 0 := by
  rw [diag_carry_iff q hq]
  simp only [linVec, chg2, Matrix.cons_val_zero, Matrix.cons_val_one, Matrix.cons_val_two,
    Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons, if_true, Bool.false_eq_true,
    if_false]
  constructor
  · rintro ⟨-, -, -, h, -⟩
    linear_combination (-1 : R) * h
  · intro h
    refine ⟨by ring, by ring, by ring, ?_, by ring⟩
    linear_combination (-1 : R) * h

/-- The total charge `Q₁ + Q₂` is always carried, for any hypercharges. -/
theorem total_charge_carried (q : R) (hq : q ≠ 0) (y₁ y₂ : R) :
    crossingR q * diagonal (linVec 1 1 y₁ y₂) = diagonal (linVec 1 1 y₂ y₁) * crossingR q :=
  (lin_carry_iff q hq 1 1 y₁ y₂).mpr (by ring)

/-- `(Q₁ + Q₂)²` (self weights `1`, pair weight `2`) is always carried. -/
theorem total_charge_sq_carried (q : R) (hq : q ≠ 0) (y₁ y₂ : R) :
    crossingR q * diagonal (quadVec 1 1 2 y₁ y₂) = diagonal (quadVec 1 1 2 y₂ y₁) * crossingR q :=
  (quad_carry_iff q hq 1 1 2 y₁ y₂).mpr (by ring)

/-- Pairs only (`α₁ = α₂ = 0`): carried iff `h·2·β·(y₁ − y₂) = 0`. -/
theorem pairOnly_carry_iff (q : R) (hq : q ≠ 0) (β y₁ y₂ : R) :
    crossingR q * diagonal (quadVec 0 0 β y₁ y₂) = diagonal (quadVec 0 0 β y₂ y₁) * crossingR q ↔
      (q - q⁻¹) * (2 * β * (y₁ - y₂)) = 0 := by
  rw [quad_carry_iff q hq]
  constructor <;> intro h <;> linear_combination (-1 : R) * h

/-- Equal hypercharges (a quark–quark crossing): pairs only is carried. This is the nucleon case. -/
theorem pairOnly_quark_quark_carried (q : R) (hq : q ≠ 0) (β y : R) :
    crossingR q * diagonal (quadVec 0 0 β y y) = diagonal (quadVec 0 0 β y y) * crossingR q :=
  (pairOnly_carry_iff q hq β y y).mpr (by ring)

/-- A quark–lepton crossing (`y = 1/3`, `y = −1`): pairs only is **not** carried for `h ≠ 0`. -/
theorem pairOnly_quark_lepton_not_carried (q : R) (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0)
    (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (β : R) (hβ : β ≠ 0) :
    crossingR q * diagonal (quadVec 0 0 β (1 / 3) (-1)) ≠
      diagonal (quadVec 0 0 β (-1) (1 / 3)) * crossingR q := by
  rw [Ne, pairOnly_carry_iff q hq]
  have h4 : (1 / 3 : R) - -1 = 2 * 2 / 3 := by field_simp; ring
  rw [h4]
  exact mul_ne_zero hh (mul_ne_zero (mul_ne_zero h2 hβ) (div_ne_zero (mul_ne_zero h2 h2) h3))

/-- With the ruled nucleon self-weight `α_q = 0`, carrying through a quark–lepton crossing forces
the lepton self-weight `α_ℓ = 2β/3` (for `h ≠ 0`, `char R ∉ {2, 3}`). -/
theorem lepton_self_weight_forced (q : R) (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) (h2 : (2 : R) ≠ 0)
    (h3 : (3 : R) ≠ 0) (β αℓ : R)
    (hcarry : crossingR q * diagonal (quadVec 0 αℓ β (1 / 3) (-1)) =
      diagonal (quadVec αℓ 0 β (-1) (1 / 3)) * crossingR q) :
    αℓ = 2 * β / 3 := by
  have h := (quad_carry_iff q hq 0 αℓ β (1 / 3) (-1)).mp hcarry
  have h' := (mul_eq_zero.mp ((mul_eq_zero.mp h).resolve_left hh)).resolve_left h2
  have h3' : (3 : R) * (1 / 3) = 1 := by field_simp
  have key : (2 : R) * (αℓ * 3 - 2 * β) = 0 := by linear_combination (3 : R) * h' + β * h3'
  have k2 := (mul_eq_zero.mp key).resolve_left h2
  rw [eq_div_iff h3]
  linear_combination k2

/-- The converse: `α_q = 0`, `α_ℓ = 2β/3` is carried. -/
theorem lepton_completion_carried (q : R) (hq : q ≠ 0) (h3 : (3 : R) ≠ 0) (β : R) :
    crossingR q * diagonal (quadVec 0 (2 * β / 3) β (1 / 3) (-1)) =
      diagonal (quadVec (2 * β / 3) 0 β (-1) (1 / 3)) * crossingR q :=
  (quad_carry_iff q hq 0 (2 * β / 3) β (1 / 3) (-1)).mpr (by field_simp; ring)

/-- A doublet strand braided by the same `Ř` but with charge `0` on both states, next to a strand
with charge `T³ + y/2`: the single charge cannot be carried for `h ≠ 0`, `char R ≠ 2`. -/
theorem singleCharge_not_carried (q : R) (hq : q ≠ 0) (hh : q - q⁻¹ ≠ 0) (h2 : (2 : R) ≠ 0)
    (y : R) :
    crossingR q * diagonal ![chg2 true y, chg2 true y, chg2 false y, chg2 false y] ≠
      diagonal ![chg2 true y, chg2 false y, chg2 true y, chg2 false y] * crossingR q := by
  intro h
  have h' := ((diag_carry_iff q hq _ _).mp h).2.2.2.1
  simp only [chg2, Matrix.cons_val_two, Matrix.head_cons, Matrix.tail_cons, if_true,
    Bool.false_eq_true, if_false] at h'
  have e : (-1 + y) - (1 + y) = -2 := by ring
  rw [e] at h'
  exact (mul_ne_zero hh (neg_ne_zero.mpr h2)) h'

/-! ## §3. A spectator strand forces uniform pair weights -/

/-- Cancellation of a non-zero Kronecker factor. -/
theorem kron_left_cancel {m n : Type*} [Fintype m] [Fintype n]
    (A : Matrix m m R) (X Y : Matrix n n R) (hA : A ≠ 0) :
    A ⊗ₖ X = A ⊗ₖ Y ↔ X = Y := by
  constructor
  · intro h
    obtain ⟨i, j, hij⟩ : ∃ i j, A i j ≠ 0 := by
      by_contra hc
      push_neg at hc
      exact hA (Matrix.ext hc)
    ext k l
    have := congrFun (congrFun h (i, k)) (j, l)
    simp only [Matrix.kronecker_apply] at this
    exact mul_left_cancel₀ hij this
  · rintro rfl
    rfl

/-- A crossing on strands 2–3 carries `A ⊗ L` (spectator strand 1, `A ≠ 0`) iff it carries `L`. -/
theorem spectator_reduction {m : Type*} [Fintype m] [DecidableEq m] (q : R)
    (A : Matrix m m R) (hA : A ≠ 0) (L L' : Matrix (Fin 4) (Fin 4) R) :
    ((1 : Matrix m m R) ⊗ₖ crossingR q) * (A ⊗ₖ L) = (A ⊗ₖ L') * ((1 : Matrix m m R) ⊗ₖ crossingR q) ↔
      crossingR q * L = L' * crossingR q := by
  rw [← Matrix.mul_kronecker_mul, ← Matrix.mul_kronecker_mul, Matrix.one_mul, Matrix.mul_one]
  exact kron_left_cancel A _ _ hA

/-- **Uniform pair weights.** With a spectator strand of non-zero charge `A`, the cross terms
`β₁ Q_c Q_a + β₂ Q_c Q_b` are carried through the `a–b` crossing iff `h·(β₁ − β₂) = 0`. -/
theorem pairWeight_uniform {m : Type*} [Fintype m] [DecidableEq m] (q : R) (hq : q ≠ 0)
    (A : Matrix m m R) (hA : A ≠ 0) (β₁ β₂ y₁ y₂ : R) :
    ((1 : Matrix m m R) ⊗ₖ crossingR q) * (A ⊗ₖ diagonal (linVec β₁ β₂ y₁ y₂)) =
        (A ⊗ₖ diagonal (linVec β₂ β₁ y₂ y₁)) * ((1 : Matrix m m R) ⊗ₖ crossingR q) ↔
      (q - q⁻¹) * (2 * (β₁ - β₂)) = 0 := by
  rw [spectator_reduction q A hA]
  exact lin_carry_iff q hq β₁ β₂ y₁ y₂

/-! ## §4. The carried family: scalar on weight spaces, blind to the β split -/

/-- On a spin-½ strand (`(2T)² = 1`), `Q²/y = 1/(4y) + T + y/4` for `Q = T + y/2`. -/
theorem sq_div_y (T y : R) (h2 : (2 : R) ≠ 0) (hT : (2 * T) ^ 2 = 1) (hy : y ≠ 0) :
    (T + y / 2) ^ 2 / y = 1 / (4 * y) + T + y / 4 := by
  have h4 : (4 : R) ≠ 0 := by
    have : (4 : R) = 2 * 2 := by norm_num
    rw [this]; exact mul_ne_zero h2 h2
  field_simp
  linear_combination (4 : R) * hT

/-- Per-state value of the carried family on four strands. -/
def natVal (β κ : R) (Q y : Fin 4 → R) : R :=
  β / 2 * (Q 0 + Q 1 + Q 2 + Q 3) ^ 2 +
    κ * (Q 0 ^ 2 / y 0 + Q 1 ^ 2 / y 1 + Q 2 ^ 2 / y 2 + Q 3 ^ 2 / y 3)

/-- **The carried family depends only on `T³_tot` and the species content.** -/
theorem natVal_eq_totals (β κ : R) (T y : Fin 4 → R) (h2 : (2 : R) ≠ 0)
    (hT : ∀ a, (2 * T a) ^ 2 = 1)
    (hy : ∀ a, y a ≠ 0) :
    natVal β κ (fun a => T a + y a / 2) y =
      β / 2 * ((T 0 + T 1 + T 2 + T 3) + (y 0 + y 1 + y 2 + y 3) / 2) ^ 2 +
        κ * ((1 / (4 * y 0) + 1 / (4 * y 1) + 1 / (4 * y 2) + 1 / (4 * y 3)) +
          (T 0 + T 1 + T 2 + T 3) + (y 0 + y 1 + y 2 + y 3) / 4) := by
  unfold natVal
  rw [sq_div_y _ _ h2 (hT 0) (hy 0), sq_div_y _ _ h2 (hT 1) (hy 1), sq_div_y _ _ h2 (hT 2) (hy 2),
    sq_div_y _ _ h2 (hT 3) (hy 3)]
  ring

/-- **The connected part of a scalar insertion is zero on every word.** -/
theorem connected_zero_of_scalar {n : Type*} [Fintype n] [DecidableEq n] (c : R)
    (X : Matrix n n R) (hd : (Fintype.card n : R) ≠ 0) :
    trace ((c • (1 : Matrix n n R)) * X) -
        trace (c • (1 : Matrix n n R)) / (Fintype.card n : R) * trace X = 0 := by
  rw [Matrix.smul_mul, Matrix.one_mul, Matrix.trace_smul, Matrix.trace_smul, Matrix.trace_one,
    smul_eq_mul, smul_eq_mul]
  field_simp
  ring

/-- Charges and hypercharges of `n ⊗ ν = (u, d, d) ⊗ ν` and `p ⊗ e⁻ = (u, u, d) ⊗ e⁻`. -/
def Qnnu : Fin 4 → R := ![2 / 3, -1 / 3, -1 / 3, 0]
def Qpe : Fin 4 → R := ![2 / 3, 2 / 3, -1 / 3, -1]
def Ysm : Fin 4 → R := ![1 / 3, 1 / 3, 1 / 3, -1]

/-- **The carried family takes the same value on `n⊗ν` and `p⊗e⁻`** for every `β, κ`. -/
theorem natural_beta_split_zero (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (β κ : R) :
    natVal β κ Qnnu Ysm - natVal β κ Qpe Ysm = 0 := by
  simp only [natVal, Qnnu, Qpe, Ysm, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  field_simp
  ring

/-- Pair sum on four strands. -/
def pairSum (Q : Fin 4 → R) : R :=
  Q 0 * Q 1 + Q 0 * Q 2 + Q 1 * Q 2 + Q 0 * Q 3 + Q 1 * Q 3 + Q 2 * Q 3

/-- Contrast: the pairs-only insertion splits them, `−1/3` on `n⊗ν`, `−1` on `p⊗e⁻`. -/
theorem pairOnly_beta_split (h3 : (3 : R) ≠ 0) :
    pairSum (Qnnu : Fin 4 → R) = -1 / 3 ∧ pairSum (Qpe : Fin 4 → R) = -1 ∧
      pairSum (Qnnu : Fin 4 → R) - pairSum Qpe = 2 / 3 := by
  simp only [pairSum, Qnnu, Qpe, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  refine ⟨?_, ?_, ?_⟩ <;> field_simp <;> ring

/-- **Nucleon recovery.** With equal hypercharges `y ≠ 0` and `κ = −βy/2`, the carried family is
`β·(Q₁Q₂ + Q₁Q₃ + Q₂Q₃)`: the ruled all-pairs insertion. -/
theorem natural_family_nucleon (β y Q₁ Q₂ Q₃ : R) (h2 : (2 : R) ≠ 0) (hy : y ≠ 0) :
    β / 2 * (Q₁ + Q₂ + Q₃) ^ 2 + (-(β * y) / 2) * (Q₁ ^ 2 / y + Q₂ ^ 2 / y + Q₃ ^ 2 / y) =
      β * (Q₁ * Q₂ + Q₁ * Q₃ + Q₂ * Q₃) := by
  field_simp
  ring

/-- **Lepton completion.** The same `κ = −β·y_q/2` with a lepton strand (`y_q = 1/3`, `y_ℓ = −1`) is
the all-pairs sum (quark–lepton pairs included) plus `(2/3)·β·Q_ℓ²`. -/
theorem natural_family_lepton (h2 : (2 : R) ≠ 0) (h3 : (3 : R) ≠ 0) (β Q₁ Q₂ Q₃ ℓ : R) :
    natVal β (-(β * (1 / 3)) / 2) ![Q₁, Q₂, Q₃, ℓ] Ysm =
      β * pairSum ![Q₁, Q₂, Q₃, ℓ] + 2 * β / 3 * ℓ ^ 2 := by
  simp only [natVal, pairSum, Ysm, Matrix.cons_val_zero, Matrix.cons_val_one,
    Matrix.cons_val_two, Matrix.cons_val_three, Matrix.head_cons, Matrix.tail_cons]
  field_simp
  ring

end QOU.QBeta.LeptonTwoTermStokesCovariance
