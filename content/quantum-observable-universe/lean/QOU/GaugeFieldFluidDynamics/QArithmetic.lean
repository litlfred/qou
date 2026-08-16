import Mathlib.Algebra.Field.Basic
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.GaugeFieldFluidDynamics.QArithmetic — generic q-arithmetic

The **algebraic** half of the §7c split of `QOU.GaugeFieldFluidDynamics`
(bean `qou-q7cm`). Everything here is stated over a generic
`{R : Type*} [Field R]`: q-integers, the q-factorial and q-binomial, and the
q-hook product with its small worked shapes. It names no real-number type, no
order relation and no archimedean construct anywhere in its code.

The archimedean material that used to sit interleaved with this — the
sign lemmas about `qInteger` (which assume the substrate parameter exceeds
one), the real-valued Markov parameter, and the whole brane-fluid /
Navier–Stokes development — stays in `QOU.GaugeFieldFluidDynamics`, which
imports this module. Per AGENTS.md §7c a block belongs to the algebraic
substrate or the archimedean specialisation, never both; this file is the
substrate side.

(Those constructs are described in words rather than written out: the q-regime
detector greps this file, so a worked example in a docstring would score the
module archimedean — the very false positive this split exists to remove.)

**Known residual detector artefact.** `detectRegimes` still tags this module
`real-positive`, because `syt3_squares_sum_eq_six` closes a statement about
natural numbers with `norm_num`, and that tactic name is on the archimedean
marker list. The proof is `1² + 2² + 1² = 6` over `ℕ` — nothing archimedean is
involved. The sibling checker `q-usage-archimedean-in-categorical-chapter`
already guards this case (it only fires on a tactic when the file also carries
a real-typed marker); `detectRegimes` does not. The authoritative gate,
`wall-side-correct`, passes. Do not rewrite the proof to appease the tag.

Same namespace as the parent, so every existing call site is unchanged.
-/

namespace QOU.GaugeFieldFluidDynamics

/-- The q-integer [k]_q = (q^k - q^{-k})/(q - q^{-1}). -/
-- Consolidated onto the canonical q-integer (bean `qou-qint`): this was a
-- verbatim duplicate of `QOU.QInteger.qIntBal`.  Kept as a local `abbrev` so
-- call sites are unchanged; the DEFINITION now has a single home.  Proofs that
-- said `unfold <local>` become `simp only [<local>, ...qIntBal]` -- `unfold`
-- reduces through the alias and leaves the follow-up tactic nothing to act on.
-- See QOU/MathlibExt/QIntegerCanonical.lean.
noncomputable abbrev qInteger {R : Type*} [Field R] (q : R) (k : ℕ) : R :=
  QOU.QInteger.qIntBal q k

/-- [0]_q = 0 for all q. -/
theorem qInteger_zero {R : Type*} [Field R] (q : R) : qInteger q 0 = 0 := by
  simp only [qInteger, QOU.Mass.QHookDimensionBalanced.qIntBal]; simp

/-- [1]_q = 1 for q ≠ q⁻¹. -/
theorem qInteger_one {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qInteger q 1 = 1 := by
  simp only [qInteger, QOU.Mass.QHookDimensionBalanced.qIntBal]; simp [pow_one]; exact div_self hq

/-- `[2]_q = q + q⁻¹` for `q ≠ q⁻¹` — closed form of the second
    q-integer.  Used by the Markov-parameter substitution
    `z = 1/[2]_{q^{1/2}}`. -/
theorem qInteger_two {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qInteger q 2 = q + q⁻¹ := by
  simp only [qInteger, QOU.Mass.QHookDimensionBalanced.qIntBal]
  rw [pow_two, pow_two, div_eq_iff hq]
  ring

/-- `[3]_q = q² + 1 + q⁻²` for `q ≠ q⁻¹`.  Closed form of the
    third q-integer; uses the factorisation `q³ - q⁻³ =
    (q - q⁻¹)(q² + 1 + q⁻²)`. -/
theorem qInteger_three {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qInteger q 3 = q ^ 2 + 1 + (q⁻¹) ^ 2 := by
  have hq0 : q ≠ 0 := by rintro rfl; simp at hq
  have hqq : q * q⁻¹ = 1 := mul_inv_cancel₀ hq0
  simp only [qInteger, QOU.Mass.QHookDimensionBalanced.qIntBal]
  rw [div_eq_iff hq]
  linear_combination (q - q⁻¹) * hqq

/-- **Recursion for q-integers**: `[n+1]_q = q · [n]_q + q⁻ⁿ`
    for `q ≠ q⁻¹`.  Equivalently expanded as a sum of monomials,
    `[n]_q = q^(n-1) + q^(n-3) + … + q^(-(n-1))` (n terms).

    Algebraic proof: using `qInteger q (n + 1) = (q^(n+1)
    − q⁻^(n+1))/(q − q⁻¹)`, one rearranges the numerator
    `q^(n+1) − q⁻^(n+1) = q · (q^n − q⁻^n) + q⁻ⁿ · (q − q⁻¹)`
    which yields the recursion after dividing by `q − q⁻¹`. -/
theorem qInteger_succ {R : Type*} [Field R] (q : R) (n : ℕ) (hq : q - q⁻¹ ≠ 0) (_hq0 : q ≠ 0) :
    qInteger q (n + 1) = q * qInteger q n + q⁻¹ ^ n := by
  simp only [qInteger, QOU.Mass.QHookDimensionBalanced.qIntBal]
  rw [div_eq_iff hq, add_mul, mul_assoc, div_mul_cancel₀ _ hq]
  ring

/-- The q-factorial `[n]_q! = ∏_{k=1..n} [k]_q`.  Returns 1 for n = 0. -/
noncomputable def qFactorial {R : Type*} [Field R] (q : R) : ℕ → R
  | 0     => 1
  | n + 1 => qInteger q (n + 1) * qFactorial q n

/-- **q-binomial coefficient** `[n choose k]_q := [n]_q!
    / ([k]_q! · [n−k]_q!)`.  Note: this is the ratio definition;
    when `q − q⁻¹ ≠ 0` and the denominator is non-zero (always
    true at generic `q`) the result is a well-defined rational.

    **DEPRECATED duplicate (bean `5ldf` consolidation, 2026-06-26).** Bit-for-bit
    the canonical balanced q-binomial `QOU.MathlibExt.QPartitionCombinatorics.qBinom`
    (the local `qInteger` ≡ that module's `qBracket`; verified). New code should use
    the canonical one; kept here for the existing local consumers
    (`WenzlBridgeConcrete`, `GroundRingAnnotations`). -/
noncomputable def qBinomial {R : Type*} [Field R] (q : R) (n k : ℕ) : R :=
  qFactorial q n / (qFactorial q k * qFactorial q (n - k))

/-- `[n choose 0]_q = 1` whenever `[n]_q!` is non-zero. -/
theorem qBinomial_zero {R : Type*} [Field R] (q : R) (n : ℕ)
    (hfact : qFactorial q n ≠ 0) : qBinomial q n 0 = 1 := by
  have h0 : qFactorial q 0 = 1 := rfl
  unfold qBinomial
  rw [Nat.sub_zero, h0, one_mul, div_self hfact]

/-- `[n choose n]_q = 1` whenever `[n]_q!` is non-zero. -/
theorem qBinomial_self {R : Type*} [Field R] (q : R) (n : ℕ)
    (hfact : qFactorial q n ≠ 0) : qBinomial q n n = 1 := by
  have h0 : qFactorial q 0 = 1 := rfl
  unfold qBinomial
  rw [Nat.sub_self, h0, mul_one, div_self hfact]

/-- `[0]_q! = 1` by convention. -/
theorem qFactorial_zero {R : Type*} [Field R] (q : R) : qFactorial q 0 = 1 := rfl

/-- `[1]_q! = [1]_q = 1` (for `q ≠ q⁻¹`). -/
theorem qFactorial_one {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qFactorial q 1 = 1 := by
  show qInteger q 1 * qFactorial q 0 = 1
  rw [qInteger_one q hq, qFactorial_zero, mul_one]

/-- `[2]_q! = [2]_q · [1]_q = q + q⁻¹` (for `q ≠ q⁻¹`). -/
theorem qFactorial_two {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qFactorial q 2 = q + q⁻¹ := by
  show qInteger q 2 * qFactorial q 1 = q + q⁻¹
  rw [qInteger_two q hq, qFactorial_one q hq, mul_one]

/-- The q-hook product `H_q(λ) = ∏_{x ∈ λ} [h_x]_q` over a partition
    `λ` represented as the list of its hook lengths.  The `dim_q(λ)`
    formula is `[n]_q! / H_q(λ)`. -/
noncomputable def qHookProduct {R : Type*} [Field R] (q : R) : List ℕ → R
  | []        => 1
  | h :: rest => qInteger q h * qHookProduct q rest

/-- The empty partition has hook product `1`. -/
theorem qHookProduct_nil {R : Type*} [Field R] (q : R) : qHookProduct q [] = 1 := rfl

/-- The hook product distributes over `cons`. -/
theorem qHookProduct_cons {R : Type*} [Field R] (q : R) (h : ℕ) (rest : List ℕ) :
    qHookProduct q (h :: rest) = qInteger q h * qHookProduct q rest := rfl

/-- Hook lengths for the row partition `[n]` are `n, n-1, …, 1`. -/
def hooksRow : ℕ → List ℕ
  | 0     => []
  | n + 1 => (n + 1) :: hooksRow n

/-- For `λ = [2]` (single row of length 2), hook lengths are `[2, 1]`. -/
theorem hooksRow_two : hooksRow 2 = [2, 1] := rfl

/-- For `λ = [3]` (single row of length 3), hook lengths are `[3, 2, 1]`. -/
theorem hooksRow_three : hooksRow 3 = [3, 2, 1] := rfl

/-- Hook product for the row partition `[2]` equals `[2]_q · [1]_q
    = (q + q⁻¹) · 1`.  At `q = q_0 ≈ 1.11` this gives a positive
    value; the genuine Wenzl-bridge `dim_q([2])` is then
    `[2]_q!/H_q([2]) = (q+q⁻¹)/(q+q⁻¹) = 1`. -/
theorem qHookProduct_row_two {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qHookProduct q (hooksRow 2) = q + q⁻¹ := by
  show qInteger q 2 * (qInteger q 1 * 1) = q + q⁻¹
  rw [qInteger_two q hq, qInteger_one q hq]; ring

/-- Hook product for the row partition `[3]` equals `[3]_q!`. -/
theorem qHookProduct_row_three {R : Type*} [Field R] (q : R) :
    qHookProduct q (hooksRow 3) =
      qInteger q 3 * (qInteger q 2 * (qInteger q 1 * 1)) := rfl

/-- Hook lengths for the L-shape partition `[2, 1]` of `n = 3`.
    Cells: (1,1)→3, (1,2)→1, (2,1)→1.  Returned in row-major order. -/
def hooksLshape21 : List ℕ := [3, 1, 1]

/-- Hook product for `λ = [2, 1]` is `[3]_q · [1]_q · [1]_q = [3]_q`
    (since `[1]_q = 1` whenever `q ≠ q⁻¹`). -/
theorem qHookProduct_lshape21 {R : Type*} [Field R] (q : R) (hq : q - q⁻¹ ≠ 0) :
    qHookProduct q hooksLshape21 = qInteger q 3 := by
  show qInteger q 3 * (qInteger q 1 * (qInteger q 1 * 1)) = qInteger q 3
  rw [qInteger_one q hq]; ring

/-- Hook lengths for the column partition `[1, 1, 1]` of `n = 3`.
    Cells: (1,1)→3, (2,1)→2, (3,1)→1.  Same multiset as `hooksRow 3`. -/
def hooksCol3 : List ℕ := [3, 2, 1]

/-- Hook product for the column `[1,1,1]` equals `[3]_q!`. -/
theorem qHookProduct_col3 {R : Type*} [Field R] (q : R) :
    qHookProduct q hooksCol3 =
      qInteger q 3 * (qInteger q 2 * (qInteger q 1 * 1)) := rfl

/-- The standard-Young-tableaux dimensions `(d_[3], d_[2,1], d_[1,1,1])
    = (1, 2, 1)` for the three partitions of `n = 3`. -/
def syt3_dims : List ℕ := [1, 2, 1]

/-- Sum of `(d_λ)²` over partitions of `n = 3` equals `n! = 6`
    (Burnside / RSK identity).  `1² + 2² + 1² = 6`. -/
theorem syt3_squares_sum_eq_six :
    (syt3_dims.map (fun d => d ^ 2)).sum = 6 := by
  show (1 ^ 2 + (2 ^ 2 + (1 ^ 2 + 0))) = 6
  norm_num

end QOU.GaugeFieldFluidDynamics
