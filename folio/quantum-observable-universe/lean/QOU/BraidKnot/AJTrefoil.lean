import QOU.BraidKnot.AJFigureEight
import QOU.MathlibExt.QIntegerCanonical

/-!
# QOU.BraidKnot.AJTrefoil

**The AJ conjecture at the QOU electron knot (trefoil), stated concretely.**

Companion to `QOU.BraidKnot.AJFigureEight`, completing the AJ statement
layer for the QOU knot set ("do the same for the trefoil", bean `3eeq`;
audit: `docs/audits/2026-07-03-aj-conjecture-dialog-assessment.md`
§"Prove AJ in QOU, fully").  AJ for the trefoil is literature-established
(two-bridge knots — Lê 2006; Ref: [garoufalidis2004] for the statement);
the corpus-side reconstruction + verification is
`computations/aj_trefoil_operator_construct_verify.py` (witness
`aj-trefoil-operator-construct-verify.witness.json`): the tower is the
Rosso–Jones twist-eigenvalue sum for the closure of `σ₁³` in `B₂` with the
convention self-anchored against the Jones polynomial (left-handed
`V(3₁) = −q⁻⁴ + q⁻³ + q⁻¹`); the annihilator is inhomogeneous **order 1**
(the trefoil A-polynomial is linear in `L`), verified exactly for
`N = 1..10`, with `q → 1` specialization `(1−M²)/M¹⁰ · (1 + L·M⁶)` under
the meridian-squared convention.

## Encoding

The braiding eigenvalues live at quarter-powers of `q`, so the tower is
parameterized by `w` with `q = w⁴`:
`T_j = (−1)^{n−j} w^{2j(j+1) − n(n+2)}` (integer `ℤ`-powers of `w`),
`J_N = w^{−3n(n+2)} · (∑_{j≤n} T_j³ [2j+1]_v) / [N]_v`, `v = w²`, `n = N−1`.

## Honest status (§3b)

Machine-checked sorry-free: the operator transcription, the `q = 1`
specialization to the classical trefoil A-polynomial `1 + L·M⁶`,
nontriviality (char 0, single witness — no case split needed), unit
nondegeneracy, and — since the root-of-unity evaluation cores were
discharged in `QOU.BraidKnot.AJTrefoilRootEval` — the **general-`N`
annihilation** assembled in `QOU.BraidKnot.AJTrefoilAnnihilation`.
No `sorry` remains anywhere in the trefoil strong-AJ chain.  Unlike
`4₁` there is **no** bar-transport theorem: the trefoil is chiral, its
tower is not bar-symmetric — the operator-level face of chirality.

## Base ring (§7c)

Generic `{K : Type*} [Field K]` (+ `[CharZero K]` where stated); `ℤ`-powers
via `zpow`; no `ℝ`, no ordering, no archimedean constructs.
-/

namespace QOU.BraidKnot.AJTrefoil

open Finset
open QOU.BraidKnot.AJFigureEight

variable {K : Type*} [Field K]

/-- Quantum integer `[k]_v = (v^k − v^{−k})/(v − v⁻¹)`. -/
def qInt (v : K) (k : ℕ) : K := (v ^ k - (v ^ k)⁻¹) / (v - v⁻¹)

/-- **Bridge to the canonical balanced bracket.** The alias was refused —
a proof below needs this literal body — so the consolidation is this
equation: same function, one canonical meaning, no proof touched. -/
theorem qInt_eq_canonical (v : K) (k : ℕ) :
    qInt v k = QOU.QInteger.qIntBal v k := by
  dsimp only [qInt, QOU.QInteger.qIntBal, QOU.QInteger.qIntBalCl,
    QOU.Mass.QHookDimensionBalanced.qIntBal]
  simp only [inv_pow, zpow_neg, zpow_natCast]

/-- Twist eigenvalue of the braiding on the `V_{2j}` summand of
    `V_n ⊗ V_n`, at `w = q^{1/4}`:
    `T_j = (−1)^{n−j} · w^{2j(j+1) − n(n+2)}` (a `ℤ`-power). -/
def twistEigenvalue (w : K) (n j : ℕ) : K :=
  (-1 : K) ^ (n - j) * w ^ ((2 * j * (j + 1) : ℤ) - (n * (n + 2) : ℤ))

/-- The N-colored Jones tower of the (left-handed) trefoil `T(2,3)` —
    Rosso–Jones twist-eigenvalue sum for the closure of `σ₁³` in `B₂`,
    with the framing correction `θ^{−3} = w^{−3n(n+2)}`.  Conventions
    self-anchored corpus-side (`J₁ = 1`, `J₂ = V(3₁)` exact). -/
def coloredJonesTrefoil (w : K) (N : ℕ) : K :=
  let n := N - 1
  w ^ (-(3 : ℤ) * (n * (n + 2) : ℤ))
    * (∑ j ∈ Finset.range (n + 1),
        (twistEigenvalue w n j) ^ 3 * qInt (w ^ 2) (2 * j + 1))
    / qInt (w ^ 2) N

/-- Coefficient functions of the explicit trefoil annihilator, transcribed
    verbatim from the verified reconstruction (order 1;
    `a₀ = −(m−1)/m⁵`, `a₁ = −q(mq−1)/m²`). -/
def trCoeff : ℕ → K → K → K
  | 0, _, m => -(m - 1) / m ^ 5
  | 1, q, m => -(q * (m * q - 1)) / m ^ 2
  | _ + 2, _, _ => 0

/-- Inhomogeneous part: `b = −q(m²q − 1)/m⁴`. -/
def trRhs (q m : K) : K := -(q * (m ^ 2 * q - 1)) / m ^ 4

/-- The explicit trefoil annihilator as a `QDifferenceOperator`. -/
def trefoilOperator : QDifferenceOperator K where
  order := 1
  coeff := trCoeff
  rhs := trRhs

/-- The classical A-polynomial of the (left-handed) trefoil:
    `A_{3₁}(L, M) = 1 + L·M⁶` (CCGLS tables, nonabelian component). -/
def aPolyTrefoil (L M : K) : K := 1 + L * M ^ 6

/-- The strong-AJ unit factor of the trefoil specialization:
    `(1 − M²)/M¹⁰`. -/
def trUnit (M : K) : K := (1 - M ^ 2) / M ^ 10

/-- **Strong AJ for the trefoil (§3b class; literature theorem).**
    Fields mirror `StrongAJFigureEight`, at order 1, against the concrete
    Rosso–Jones tower (parameterized by `w`, `q = w⁴`). -/
class StrongAJTrefoil (K : Type*) [Field K] where
  /-- The annihilating operator. -/
  op : QDifferenceOperator K
  /-- The inhomogeneous presentation has order 1. -/
  order_eq : op.order = 1
  /-- Non-trivial at every `q ≠ 0`. -/
  nontrivial : ∀ q : K, q ≠ 0 → NontrivialAt op q
  /-- Annihilates the trefoil tower at every `w ≠ 0` (with `q = w⁴`). -/
  annihilates : ∀ w : K, w ≠ 0 →
    Annihilates op (w ^ 4) (coloredJonesTrefoil w)
  /-- The strong-AJ unit factor. -/
  unit : K → K
  /-- The unit factor is not identically zero. -/
  unit_nondegenerate : ∃ m : K, m ≠ 0 ∧ unit m ≠ 0
  /-- **Specialization, meridian-squared convention**: at `q = 1`,
      `m = M²`, the homogeneous part equals `unit M · A_{3₁}(L, M)`. -/
  specializes : ∀ L M : K, M ≠ 0 →
    op.coeff 1 1 (M ^ 2) * L + op.coeff 0 1 (M ^ 2)
      = unit M * aPolyTrefoil L M

/-- **Specialization, proved**: `−(M²−1)/M⁴·L − (M²−1)/M¹⁰
    = (1−M²)/M¹⁰ · (1 + L·M⁶)`. -/
theorem trefoilOperator_specializes (L M : K) (hM : M ≠ 0) :
    (trefoilOperator (K := K)).coeff 1 1 (M ^ 2) * L
        + (trefoilOperator (K := K)).coeff 0 1 (M ^ 2)
      = trUnit M * aPolyTrefoil L M := by
  show trCoeff 1 1 (M ^ 2) * L + trCoeff 0 1 (M ^ 2)
      = trUnit M * aPolyTrefoil L M
  simp only [trCoeff, trUnit, aPolyTrefoil]
  field_simp
  ring

/-- The unit factor is not identically zero (witness `M = 2`). -/
theorem trUnit_nondegenerate [CharZero K] :
    ∃ m : K, m ≠ 0 ∧ trUnit (K := K) m ≠ 0 := by
  refine ⟨2, by norm_num, ?_⟩
  simp only [trUnit]
  rw [div_ne_zero_iff]
  norm_num

/-- **Nontriviality, proved** (char 0): witness `m = 2/q` — a single
    witness suffices (`mq = 2 ≠ 1`), no case split. -/
theorem trefoilOperator_nontrivial [CharZero K] {q : K} (hq : q ≠ 0) :
    NontrivialAt (trefoilOperator (K := K)) q := by
  refine ⟨2 / q, ?_⟩
  show trCoeff 1 q (2 / q) ≠ 0
  have hm : (2 : K) / q ≠ 0 := div_ne_zero (by norm_num) hq
  have hA : (2 : K) / q * q - 1 = 1 := by
    rw [div_mul_cancel₀ _ hq]; ring
  simp only [trCoeff]
  rw [div_ne_zero_iff]
  refine ⟨?_, pow_ne_zero _ hm⟩
  rw [neg_ne_zero]
  exact mul_ne_zero hq (by rw [hA]; norm_num)

/-!
The instance `StrongAJTrefoil K` lives in
`QOU.BraidKnot.AJTrefoilAnnihilation`, where the general-`N` annihilation
is **assembled** (`trefoilOperator_annihilates`: P-form + case split; the
root-of-unity evaluation cores are proved in
`QOU.BraidKnot.AJTrefoilRootEval`, so the chain is sorry-free).  A broad
cited-`sorry` instance formerly lived here; it is superseded.
-/

/-- **Derived (conditional on the literature class): the trefoil tower is
    q-holonomic at every `q = w⁴`, `w ≠ 0`** — ∃-packaging as for `4₁`.
    Note `w ≠ 0 → w⁴ ≠ 0` supplies the nontriviality hypothesis. -/
abbrev coloredJonesTrefoil_qholonomic [inst : StrongAJTrefoil K]
    {w : K} (hw : w ≠ 0) :
    IsQHolonomic (w ^ 4) (coloredJonesTrefoil w) :=
  ⟨inst.op, inst.nontrivial (w ^ 4) (pow_ne_zero _ hw),
    inst.annihilates w hw⟩

/-- **Classical `q = 1` inhomogeneous-to-leading coefficient identity and `m = 1` zero (`qou-6vo0`).**
At `q = 1`, the inhomogeneous right-hand side `trRhs 1 M` equals the leading coefficient
`trCoeff 1 1 (M ^ 2)`, and at `m = 1` the zero-shift coefficient `trCoeff 0 q 1` vanishes. -/
theorem trRhs_at_one_eq_trCoeff_and_trCoeff_zero_at_one (q M : K) :
    trRhs 1 M = trCoeff 1 1 (M ^ 2) ∧ trCoeff 0 q 1 = 0 := by
  dsimp only [trRhs, trCoeff]
  refine ⟨by ring, by ring⟩

end QOU.BraidKnot.AJTrefoil
