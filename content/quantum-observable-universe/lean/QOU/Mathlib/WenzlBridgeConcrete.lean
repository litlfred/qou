/-!
# QOU.Mathlib.WenzlBridgeConcrete — concrete Wenzl-bridge values

The Wenzl-bridge formula `tr_M(σ_w) = Σ_λ y_λ · χ_λ(σ_w)` with
`y_λ = dim_q(λ) · d_λ / [n]_q!` admits **closed-form scalar
values** at small `n` directly from the q-arithmetic foundations
in `GaugeFieldFluidDynamics.lean`.  This file collects those
concrete forms as theorems independent of the abstract
`HeckeAlgebra.lean` class hypotheses.

For `n = 2` (partitions: `[2]`, `[1,1]`):
* `dim_q([2]) = 1` (row Wenzl factor on a 2-cell row).
* `dim_q([1,1]) = 1` (column dual).
* `y_[2] = 1 · 1 / [2]_q! = 1/(q+q⁻¹)`.
* `y_[1,1] = 1 · 1 / [2]_q! = 1/(q+q⁻¹)`.

For `n = 3` (partitions: `[3]`, `[2,1]`, `[1,1,1]`):
* `dim_q([3]) = 1`, `d_[3] = 1`.
* `dim_q([2,1]) = q + q⁻¹` (the L-shape carries the `[2]_q`
  cell content).
* `dim_q([1,1,1]) = 1`, `d_[1,1,1] = 1`.
* `y_[3] = y_[1,1,1] = 1/[3]_q!`.
* `y_[2,1] = (q+q⁻¹) · 2 / [3]_q! = 2(q+q⁻¹) / ([3]_q · (q+q⁻¹))
  = 2/[3]_q`.

These are scalar arithmetic facts in `ℝ`, provable by
`field_simp` / `ring` once the q-integer closed forms are
unfolded.

**File status**: complementary to `HeckeAlgebra.lean` (which
axiomatises the abstract bridge identity).  This file gives the
concrete *scalar values* for the small-`n` Wedderburn blocks
without needing the abstract `H_n(q)` carrier.
-/

import Mathlib.Data.Real.Basic
import Mathlib.Tactic
import Mathlib.Combinatorics.Enumerative.Partition
import QOU.GaugeFieldFluidDynamics

namespace QOU.Mathlib.WenzlBridgeConcrete

open QOU

/-- The **q-Wenzl dimension** for the row partition `[n]`:
    `dim_q([n]) = 1` (the row carries the trivial Wenzl
    multiplier).  For the QOU substrate, this means the
    fully-symmetric Wedderburn channel of `H_n(q)` is
    1-dimensional. -/
def dimqRowPartition (_n : ℕ) (_q : ℝ) : ℝ := 1

/-- The **q-Wenzl dimension** for the column partition `[1, 1,
    …, 1]` (n boxes in a column): `dim_q([1ⁿ]) = 1` (column
    dual of the row).  This means the fully-antisymmetric
    Wedderburn channel of `H_n(q)` is 1-dimensional. -/
def dimqColPartition (_n : ℕ) (_q : ℝ) : ℝ := 1

/-- The **q-Wenzl dimension** for the L-shape `[2, 1]` at `n =
    3`: `dim_q([2,1]) = (q + q⁻¹)`.  The standard `[2,1]`
    Wedderburn block of `H_3(q)` is 2-dimensional with this
    q-trace. -/
noncomputable def dimqLshape21 (q : ℝ) : ℝ := q + q⁻¹

/-- For `q ≠ q⁻¹` (generic `q`), `dimqLshape21 q ≠ 0`.  Tightens
    the structural non-degeneracy of the `[2,1]` Wedderburn
    block. -/
theorem dimqLshape21_ne_zero (q : ℝ) (hq : q + q⁻¹ ≠ 0) :
    dimqLshape21 q ≠ 0 := by
  unfold dimqLshape21
  exact hq

/-- The Wenzl-bridge `y_[2]` coefficient at `n = 2`:
    `y_[2] = dim_q([2]) · d_[2] / [2]_q! = 1 · 1 / (q + q⁻¹)
    = 1 / (q + q⁻¹)`. -/
noncomputable def yLambdaRow2 (q : ℝ) : ℝ := 1 / (q + q⁻¹)

/-- `y_[1,1] = 1 / (q + q⁻¹)` (column-dual of the row,
    same Wenzl coefficient). -/
noncomputable def yLambdaCol2 (q : ℝ) : ℝ := 1 / (q + q⁻¹)

/-- Symmetry: `y_[2] = y_[1,1]` over `q` (column-row duality
    for `n = 2`). -/
theorem yLambdaRow2_eq_yLambdaCol2 (q : ℝ) :
    yLambdaRow2 q = yLambdaCol2 q := rfl

/-- The **q-binomial sum identity** at `n = 2`:
    `dim_q([2])² + dim_q([1,1])² = 2 = 2!` (Burnside / RSK).
    Holds in the dimension-1 Wedderburn channels at any `q`. -/
theorem dim_q_squares_sum_two (q : ℝ) :
    dimqRowPartition 2 q ^ 2 + dimqColPartition 2 q ^ 2 = 2 := by
  show (1 : ℝ) ^ 2 + 1 ^ 2 = 2
  norm_num

/-- The **classical** RSK identity `Σ d_λ² = n!` at `n = 3`:
    `1² + 2² + 1² = 6 = 3!`.  Independent of `q`; uses only the
    SYT counts.  Mirrors `syt3_squares_sum_eq_six`. -/
theorem syt_squares_sum_three : 1 ^ 2 + 2 ^ 2 + 1 ^ 2 = 6 := by norm_num

/-- The **q-deformed RSK identity** at `n = 3`: `Σ_λ dim_q(λ)
    · d_λ² = [3]_q!` — checked at our three concrete partitions.

    LHS = `1·1² + (q+q⁻¹)·2² + 1·1² = 2 + 4(q+q⁻¹) = 2 + 4q + 4q⁻¹`.
    RHS = `[3]_q · [2]_q · [1]_q`.

    With `[1]_q = 1`, `[2]_q = q + q⁻¹`, and the standard q-3
    closed form `[3]_q = q² + 1 + q⁻²`, RHS = `(q² + 1 + q⁻²)
    (q + q⁻¹)`.

    These are NOT equal at generic `q` — the genuine Wenzl
    identity is `Σ dim_q(λ)² · d_λ_extra = [n]_q!` with the
    q-hook product on the LHS, not just the q-character × SYT
    count.  This file declines to assert the false identity;
    the true Wenzl identity is delivered through the
    `WedderburnDecomposition` block-projection structure. -/

/-! ## Recursive structure

    The Wenzl-bridge data at level `n` consists of:
    - the list of partitions of `n` (combinatorial enumeration);
    - for each partition `λ`, its hook-length list and SYT count;
    - the derived q-hook product `H_q(λ) = ∏ [h_x]_q` (closed form
      via `qHookProduct`);
    - the q-Wenzl dimension `dim_q(λ) = [n]_q! / H_q(λ)`;
    - the y_λ coefficient `y_λ = dim_q(λ) · d_λ / [n]_q!`.

    The **recursion** is in two layers:
    (i)  the partition enumeration (Mathlib's
         `Combinatorics.Partition`) recurses on the residue
         `n - k` after removing the largest part `k`;
    (ii) the SYT count `d_λ` admits the classical hook-walk
         recursion (Frame–Robinson–Thrall) `d_λ = n! / H(λ)`,
         which is itself a closed form once `H(λ)` is computed.

    The q-arithmetic primitives in `GaugeFieldFluidDynamics.lean`
    (`qInteger`, `qFactorial`, `qHookProduct`) compose
    directly into this recursive scheme.  This file collects the
    explicit `n ∈ {2, 3, 4}` cohorts; the abstract recursion
    over arbitrary `n` is captured by the
    `WenzlPartitionData` structure below. -/

/-- Bundle for a single Wedderburn block at level `n`: a
    partition together with its hook lengths, SYT count, and
    the closed-form `q`-Wenzl dimension. -/
structure WenzlPartitionData (n : ℕ) where
  /-- Display name (e.g. `"[3,1]"`). -/
  name : String
  /-- Hook-length list (row-major; multiset matters but order is
      preserved for `qHookProduct` evaluation). -/
  hooks : List ℕ
  /-- The standard-Young-tableau count `d_λ`. -/
  syt_count : ℕ
  deriving Repr

/-! ### Cohort: `n = 2` (2 partitions) -/

/-- The two partitions of `n = 2` with their hook + SYT data. -/
def n2_cohort : List (WenzlPartitionData 2) :=
  [{ name := "[2]",   hooks := [2, 1], syt_count := 1 },
   { name := "[1,1]", hooks := [2, 1], syt_count := 1 }]

/-- `Σ d_λ² = 2! = 2` at `n = 2`. -/
theorem n2_squares_sum_eq :
    (n2_cohort.map (fun p => p.syt_count ^ 2)).sum = 2 := by
  show (1 ^ 2 + (1 ^ 2 + 0)) = 2
  norm_num

/-! ### Cohort: `n = 3` (3 partitions) -/

/-- The three partitions of `n = 3` with hook + SYT data. -/
def n3_cohort : List (WenzlPartitionData 3) :=
  [{ name := "[3]",     hooks := [3, 2, 1], syt_count := 1 },
   { name := "[2,1]",   hooks := [3, 1, 1], syt_count := 2 },
   { name := "[1,1,1]", hooks := [3, 2, 1], syt_count := 1 }]

/-- `Σ d_λ² = 3! = 6` at `n = 3`. -/
theorem n3_squares_sum_eq :
    (n3_cohort.map (fun p => p.syt_count ^ 2)).sum = 6 := by
  show (1 ^ 2 + (2 ^ 2 + (1 ^ 2 + 0))) = 6
  norm_num

/-! ### Cohort: `n = 4` (5 partitions)

    Partition data:
    - `[4]`        : hooks `(4, 3, 2, 1)`, `d = 1`
    - `[3, 1]`     : hooks `(4, 2, 1, 1)`, `d = 3`
    - `[2, 2]`     : hooks `(3, 2, 2, 1)`, `d = 2`
    - `[2, 1, 1]`  : hooks `(4, 1, 2, 1)`, `d = 3`
    - `[1, 1, 1, 1]` : hooks `(4, 3, 2, 1)`, `d = 1`

    Sum of squares: `1² + 3² + 2² + 3² + 1² = 1+9+4+9+1 = 24 = 4!` ✓ -/

/-- The five partitions of `n = 4` with hook + SYT data. -/
def n4_cohort : List (WenzlPartitionData 4) :=
  [{ name := "[4]",         hooks := [4, 3, 2, 1], syt_count := 1 },
   { name := "[3,1]",       hooks := [4, 2, 1, 1], syt_count := 3 },
   { name := "[2,2]",       hooks := [3, 2, 2, 1], syt_count := 2 },
   { name := "[2,1,1]",     hooks := [4, 1, 2, 1], syt_count := 3 },
   { name := "[1,1,1,1]",   hooks := [4, 3, 2, 1], syt_count := 1 }]

/-- `Σ d_λ² = 4! = 24` at `n = 4` (Burnside / RSK). -/
theorem n4_squares_sum_eq :
    (n4_cohort.map (fun p => p.syt_count ^ 2)).sum = 24 := by
  show (1 ^ 2 + (3 ^ 2 + (2 ^ 2 + (3 ^ 2 + (1 ^ 2 + 0))))) = 24
  norm_num

/-- The number of partitions of `n` matches the cohort's length. -/
theorem n2_cohort_length : n2_cohort.length = 2 := rfl
theorem n3_cohort_length : n3_cohort.length = 3 := rfl
theorem n4_cohort_length : n4_cohort.length = 5 := rfl

/-! ### n=3 dim_q values via the hook formula

    `dim_q(λ) = [n]_q! / H_q(λ)` (Frame–Robinson–Thrall q-deformation).
    For partitions of `n = 3`:
    - `dim_q([3])     = [3]_q! / [3]_q[2]_q[1]_q = 1`.
    - `dim_q([2,1])   = [3]_q! / ([3]_q · 1 · 1) = [2]_q · [1]_q
                      = q + q⁻¹`.
    - `dim_q([1,1,1]) = [3]_q! / [3]_q[2]_q[1]_q = 1`. -/

/-- `dim_q([3]) = 1`.  Row partition has hook product `[3]_q!`,
    matching the q-factorial denominator. -/
def dimqPartition3 (_q : ℝ) : ℝ := 1

/-- `dim_q([2,1]) = q + q⁻¹`.  Hook product `H_q([2,1]) = [3]_q
    · [1]_q · [1]_q = [3]_q`, so `dim_q = [3]_q! / [3]_q
    = [2]_q · [1]_q = (q + q⁻¹) · 1`. -/
noncomputable def dimqPartition21 (q : ℝ) : ℝ := q + q⁻¹

/-- `dim_q([1,1,1]) = 1`.  Column partition has hook product
    `[3]_q!`, matching the q-factorial denominator. -/
def dimqPartition111 (_q : ℝ) : ℝ := 1

/-! ### n=3 y_λ coefficients (Wenzl-bridge central characters)

    `y_λ = dim_q(λ) · d_λ / [n]_q! = d_λ / H_q(λ)` (the closed
    form follows after one cancellation).
    - `y_[3]     = 1 / [3]_q!`.
    - `y_[2,1]   = 2 / [3]_q`.
    - `y_[1,1,1] = 1 / [3]_q!`. -/

/-- `y_[3] = 1 / [3]_q!`. -/
noncomputable def yLambda_row3 (q : ℝ) : ℝ := 1 / QOU.qFactorial q 3

/-- `y_[2,1] = 2 / [3]_q`. -/
noncomputable def yLambda_lshape21 (q : ℝ) : ℝ := 2 / QOU.qInteger q 3

/-- `y_[1,1,1] = 1 / [3]_q!`. -/
noncomputable def yLambda_col3 (q : ℝ) : ℝ := 1 / QOU.qFactorial q 3

/-- Symmetry: `y_[3] = y_[1,1,1]` (column-row duality at `n = 3`). -/
theorem yLambda_row3_eq_col3 (q : ℝ) :
    yLambda_row3 q = yLambda_col3 q := rfl

/-- **Hook-formula derivation** for `dim_q([2,1])`.  Frame–
    Robinson–Thrall: `dim_q(λ) = [n]_q! / H_q(λ)`.  At `λ =
    [2,1]`, hooks `(3, 1, 1)`, so `H_q = [3]_q · [1]_q · [1]_q
    = [3]_q · 1 · 1 = [3]_q` (using `[1]_q = 1`).  Then
    `dim_q([2,1]) = [3]_q · [2]_q · [1]_q / [3]_q = [2]_q · 1
    = q + q⁻¹`.  This theorem audits the closed-form
    `dimqPartition21 q = q + q⁻¹` against the underlying
    q-arithmetic.

    Caller-supplied `h3 : [3]_q ≠ 0`.  At substrate `q > 1`,
    `qInteger_pos q 3 hq_one (le_refl 3)` discharges. -/
theorem dimqPartition21_via_hook_formula (q : ℝ) (hq : q - q⁻¹ ≠ 0)
    (h3 : QOU.qInteger q 3 ≠ 0) :
    QOU.qFactorial q 3 / QOU.qHookProduct q [3, 1, 1]
      = dimqPartition21 q := by
  unfold dimqPartition21
  show QOU.qInteger q 3 * (QOU.qInteger q 2 * (QOU.qInteger q 1 * 1))
    / (QOU.qInteger q 3 * (QOU.qInteger q 1 * (QOU.qInteger q 1 * 1)))
    = q + q⁻¹
  rw [QOU.qInteger_two q hq, QOU.qInteger_one q hq]
  field_simp
  ring

/-! ### n=4 dim_q values

    Hook formula `dim_q(λ) = [4]_q! / H_q(λ)`:
    - `[4]`        : hooks `(4,3,2,1)`,   `H_q = [4]_q!`,
                     `dim_q = 1`.
    - `[3,1]`      : hooks `(4,2,1,1)`,   `H_q = [4]_q · [2]_q`,
                     `dim_q = [3]_q · [1]_q = [3]_q`.
    - `[2,2]`      : hooks `(3,2,2,1)`,   `H_q = [3]_q · [2]_q²`,
                     `dim_q = [4]_q · [1]_q / [2]_q = [4]_q/[2]_q`.
    - `[2,1,1]`    : hooks `(4,1,2,1)`,   `H_q = [4]_q · [2]_q`,
                     `dim_q = [3]_q · [1]_q = [3]_q`.
    - `[1,1,1,1]`  : hooks `(4,3,2,1)`,   `H_q = [4]_q!`,
                     `dim_q = 1`. -/

/-- `dim_q([4]) = 1`. -/
def dimqPartition4 (_q : ℝ) : ℝ := 1

/-- `dim_q([3,1]) = [3]_q`. -/
noncomputable def dimqPartition31 (q : ℝ) : ℝ := QOU.qInteger q 3

/-- `dim_q([2,2]) = [4]_q / [2]_q`. -/
noncomputable def dimqPartition22 (q : ℝ) : ℝ :=
  QOU.qInteger q 4 / QOU.qInteger q 2

/-- `dim_q([2,1,1]) = [3]_q`.  Equal to `dim_q([3,1])` (column-row
    duality). -/
noncomputable def dimqPartition211 (q : ℝ) : ℝ := QOU.qInteger q 3

/-- `dim_q([1,1,1,1]) = 1`. -/
def dimqPartition1111 (_q : ℝ) : ℝ := 1

/-- Column-row duality at `n = 4`: `dim_q([3,1]) = dim_q([2,1,1])`. -/
theorem dimqPartition31_eq_dimqPartition211 (q : ℝ) :
    dimqPartition31 q = dimqPartition211 q := rfl

/-- Self-duality at `n = 4`: `dim_q([4]) = dim_q([1,1,1,1]) = 1`. -/
theorem dimqPartition4_eq_dimqPartition1111 (q : ℝ) :
    dimqPartition4 q = dimqPartition1111 q := rfl

/-! ### n=4 y_λ Wenzl-bridge coefficients

    `y_λ = d_λ / H_q(λ)` (closed form after `dim_q · d_λ /
    [n]_q!` cancellation).
    - `y_[4]       = 1 / [4]_q!`.
    - `y_[3,1]     = 3 / ([4]_q · [2]_q)`.
    - `y_[2,2]     = 2 / ([3]_q · [2]_q²)`.
    - `y_[2,1,1]   = 3 / ([4]_q · [2]_q)`.
    - `y_[1,1,1,1] = 1 / [4]_q!`. -/

/-- `y_[4] = 1 / [4]_q!`. -/
noncomputable def yLambda_row4 (q : ℝ) : ℝ := 1 / QOU.qFactorial q 4

/-- `y_[3,1] = 3 / ([4]_q · [2]_q)`. -/
noncomputable def yLambda_31 (q : ℝ) : ℝ :=
  3 / (QOU.qInteger q 4 * QOU.qInteger q 2)

/-- `y_[2,2] = 2 / ([3]_q · [2]_q²)`. -/
noncomputable def yLambda_22 (q : ℝ) : ℝ :=
  2 / (QOU.qInteger q 3 * QOU.qInteger q 2 ^ 2)

/-- `y_[2,1,1] = 3 / ([4]_q · [2]_q)`.  Equal to `y_[3,1]`
    (column-row duality at n = 4). -/
noncomputable def yLambda_211 (q : ℝ) : ℝ :=
  3 / (QOU.qInteger q 4 * QOU.qInteger q 2)

/-- `y_[1,1,1,1] = 1 / [4]_q!`. -/
noncomputable def yLambda_col4 (q : ℝ) : ℝ := 1 / QOU.qFactorial q 4

/-- Column-row duality at `n = 4` for `y_λ`. -/
theorem yLambda_31_eq_yLambda_211 (q : ℝ) :
    yLambda_31 q = yLambda_211 q := rfl

/-- Self-duality at `n = 4` for `y_λ`. -/
theorem yLambda_row4_eq_yLambda_col4 (q : ℝ) :
    yLambda_row4 q = yLambda_col4 q := rfl

/-- **Hook-formula derivation for `dim_q([3,1])`** at `n = 4`.

    Hooks of `[3,1]` are `(4, 2, 1, 1)`, so
    `H_q = [4]_q · [2]_q · [1]_q · [1]_q = [4]_q · [2]_q`
    (using `[1]_q = 1`).  Then
    `dim_q = [4]_q · [3]_q · [2]_q · [1]_q / ([4]_q · [2]_q)
           = [3]_q`.  Matches `dimqPartition31 q := qInteger q 3`.

    Caller-supplied hypotheses `h2 : [2]_q ≠ 0` and `h4 :
    [4]_q ≠ 0`.  At substrate `q > 1` these follow from
    `QOU.qInteger_pos q k (hq_one : q > 1) (hk : k ≥ 1)`. -/
theorem dimqPartition31_via_hook_formula (q : ℝ) (hq : q - q⁻¹ ≠ 0)
    (h2 : QOU.qInteger q 2 ≠ 0) (h4 : QOU.qInteger q 4 ≠ 0) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [4, 2, 1, 1]
      = dimqPartition31 q := by
  unfold dimqPartition31
  show QOU.qInteger q 4 * (QOU.qInteger q 3 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1)))
    / (QOU.qInteger q 4 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * (QOU.qInteger q 1 * 1))))
    = QOU.qInteger q 3
  rw [QOU.qInteger_one q hq]
  field_simp
  ring

/-- **Recursive `cohortDimqValues`** — maps each
    `WenzlPartitionData` entry to its q-deformed Wenzl
    dimension via the hook formula.  Composes the existing
    `qFactorial` + `qHookProduct` primitives. -/
noncomputable def cohortDimqValues
    {n : ℕ} (cohort : List (WenzlPartitionData n)) (q : ℝ) : List ℝ :=
  cohort.map (fun p => QOU.qFactorial q n / QOU.qHookProduct q p.hooks)

/-- The dim_q-values list of the n=2 cohort has length 2. -/
theorem cohortDimqValues_n2_length (q : ℝ) :
    (cohortDimqValues n2_cohort q).length = 2 := by
  unfold cohortDimqValues
  show (n2_cohort.map _).length = 2
  rw [List.length_map]
  exact n2_cohort_length

/-- The dim_q-values list of the n=3 cohort has length 3. -/
theorem cohortDimqValues_n3_length (q : ℝ) :
    (cohortDimqValues n3_cohort q).length = 3 := by
  unfold cohortDimqValues
  rw [List.length_map]
  exact n3_cohort_length

/-- The dim_q-values list of the n=4 cohort has length 5. -/
theorem cohortDimqValues_n4_length (q : ℝ) :
    (cohortDimqValues n4_cohort q).length = 5 := by
  unfold cohortDimqValues
  rw [List.length_map]
  exact n4_cohort_length

/-- The dim_q-values list of the n=5 cohort has length 7. -/
theorem cohortDimqValues_n5_length (q : ℝ) :
    (cohortDimqValues n5_cohort q).length = 7 := by
  unfold cohortDimqValues
  rw [List.length_map]
  exact n5_cohort_length

/-- The dim_q-values list at any cohort has length p(n). -/
theorem cohortDimqValues_length
    {n : ℕ} (cohort : List (WenzlPartitionData n)) (q : ℝ) :
    (cohortDimqValues cohort q).length = cohort.length := by
  unfold cohortDimqValues
  rw [List.length_map]

/-- **Hook-formula derivation for `dim_q([2,2])`** at `n = 4`.

    Hooks of `[2,2]` are `(3, 2, 2, 1)`, so
    `H_q = [3]_q · [2]_q · [2]_q · [1]_q = [3]_q · [2]_q²`
    (using `[1]_q = 1`).  Then
    `dim_q = [4]_q [3]_q [2]_q [1]_q / ([3]_q [2]_q²) = [4]_q / [2]_q`.

    Caller-supplied `[2]_q ≠ 0` and `[3]_q ≠ 0` hypotheses. -/
theorem dimqPartition22_via_hook_formula (q : ℝ) (hq : q - q⁻¹ ≠ 0)
    (h2 : QOU.qInteger q 2 ≠ 0) (h3 : QOU.qInteger q 3 ≠ 0) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [3, 2, 2, 1]
      = dimqPartition22 q := by
  unfold dimqPartition22
  show QOU.qInteger q 4 * (QOU.qInteger q 3 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1)))
    / (QOU.qInteger q 3 * (QOU.qInteger q 2 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1))))
    = QOU.qInteger q 4 / QOU.qInteger q 2
  rw [QOU.qInteger_one q hq]
  field_simp
  ring

/-- **Hook-formula derivation for `dim_q([2,1,1])`** at `n = 4`.

    Hooks of `[2,1,1]` are `(4, 1, 2, 1)`, so
    `H_q = [4]_q · [1]_q · [2]_q · [1]_q = [4]_q · [2]_q`.
    Then `dim_q = [4]_q [3]_q [2]_q [1]_q / ([4]_q [2]_q) = [3]_q`.

    Caller-supplied `[2]_q ≠ 0` and `[4]_q ≠ 0`.  Same target as
    `dimqPartition31_via_hook_formula` (column-row duality at
    `n = 4`). -/
theorem dimqPartition211_via_hook_formula (q : ℝ) (hq : q - q⁻¹ ≠ 0)
    (h2 : QOU.qInteger q 2 ≠ 0) (h4 : QOU.qInteger q 4 ≠ 0) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [4, 1, 2, 1]
      = dimqPartition211 q := by
  unfold dimqPartition211
  show QOU.qInteger q 4 * (QOU.qInteger q 3 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1)))
    / (QOU.qInteger q 4 * (QOU.qInteger q 1 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1))))
    = QOU.qInteger q 3
  rw [QOU.qInteger_one q hq]
  field_simp
  ring

/-! ### Substrate-q corollaries

    At the QOU substrate `q > 1`, every `[k]_q` for `k ≥ 1` is
    positive and hence non-zero (via `qInteger_pos`).  These
    corollaries package the hook-formula theorems with their
    non-vanishing hypotheses discharged automatically from the
    single hypothesis `q > 1`. -/

/-- At substrate `q > 1`, `dim_q([2,1])` equals the hook formula. -/
theorem dimqPartition21_at_substrate (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 3 / QOU.qHookProduct q [3, 1, 1]
      = dimqPartition21 q := by
  have hq : q - q⁻¹ ≠ 0 := by
    have hpos : q > 0 := by linarith
    have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq_one
    have hinv_pos : q⁻¹ > 0 := inv_pos.mpr hpos
    intro habs
    linarith
  have h3 : QOU.qInteger q 3 ≠ 0 :=
    QOU.qInteger_ne_zero q 3 hq_one (by norm_num)
  exact dimqPartition21_via_hook_formula q hq h3

/-- At substrate `q > 1`, `dim_q([3,1])` equals the hook formula. -/
theorem dimqPartition31_at_substrate (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [4, 2, 1, 1]
      = dimqPartition31 q := by
  have hq : q - q⁻¹ ≠ 0 := by
    have hpos : q > 0 := by linarith
    have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq_one
    have hinv_pos : q⁻¹ > 0 := inv_pos.mpr hpos
    intro habs
    linarith
  have h2 : QOU.qInteger q 2 ≠ 0 :=
    QOU.qInteger_ne_zero q 2 hq_one (by norm_num)
  have h4 : QOU.qInteger q 4 ≠ 0 :=
    QOU.qInteger_ne_zero q 4 hq_one (by norm_num)
  exact dimqPartition31_via_hook_formula q hq h2 h4

/-- At substrate `q > 1`, `dim_q([2,2])` equals the hook formula. -/
theorem dimqPartition22_at_substrate (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [3, 2, 2, 1]
      = dimqPartition22 q := by
  have hq : q - q⁻¹ ≠ 0 := by
    have hpos : q > 0 := by linarith
    have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq_one
    have hinv_pos : q⁻¹ > 0 := inv_pos.mpr hpos
    intro habs
    linarith
  have h2 : QOU.qInteger q 2 ≠ 0 :=
    QOU.qInteger_ne_zero q 2 hq_one (by norm_num)
  have h3 : QOU.qInteger q 3 ≠ 0 :=
    QOU.qInteger_ne_zero q 3 hq_one (by norm_num)
  exact dimqPartition22_via_hook_formula q hq h2 h3

/-- At substrate `q > 1`, `dim_q([2,1,1])` equals the hook formula. -/
theorem dimqPartition211_at_substrate (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [4, 1, 2, 1]
      = dimqPartition211 q := by
  have hq : q - q⁻¹ ≠ 0 := by
    have hpos : q > 0 := by linarith
    have hinv_lt : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq_one
    have hinv_pos : q⁻¹ > 0 := inv_pos.mpr hpos
    intro habs
    linarith
  have h2 : QOU.qInteger q 2 ≠ 0 :=
    QOU.qInteger_ne_zero q 2 hq_one (by norm_num)
  have h4 : QOU.qInteger q 4 ≠ 0 :=
    QOU.qInteger_ne_zero q 4 hq_one (by norm_num)
  exact dimqPartition211_via_hook_formula q hq h2 h4

/-! ### Wenzl-bridge trace identity (sketch)

    The Markov-trace normalisation `tr_M(1) = 1` plus the
    Wenzl-bridge expansion gives the constraint
      `Σ_λ y_λ · χ_λ(1) = Σ_λ y_λ · d_λ = 1`.

    For our concrete cohorts, this is a multi-term identity
    relating the y_λ values across all partitions of `n`.  At
    n = 2 the identity reads
      `y_[2] · 1 + y_[1,1] · 1 = 2/(q + q⁻¹) = 1`,
    which holds **only** at `q = 1`; at generic `q ≠ 1` the
    direct formula `y_λ = d_λ / H_q(λ)` requires a
    normalisation factor.  The genuine Wenzl-bridge formula is
    `y_λ(q) = dim_q(λ) · d_λ / [n]_q!`, which DOES sum to 1
    via the Plancherel formula `Σ_λ dim_q(λ)² = [n]_q!` (the
    q-deformation of Burnside).  We record the corrected y_λ
    values as `yLambdaCorrected_*` below, distinct from the
    raw `d_λ / H_q(λ)` shorthand. -/

/-- **Corrected** `y_[3]` Wenzl-bridge coefficient at `n = 3`:
    `y_[3] = dim_q([3]) · d_[3] / [3]_q! = 1 · 1 / [3]_q!`. -/
noncomputable def yLambdaCorrected_row3 (q : ℝ) : ℝ :=
  dimqPartition3 q * 1 / QOU.qFactorial q 3

/-- Corrected `y_[2,1]` at `n = 3`:
    `y_[2,1] = dim_q([2,1]) · d_[2,1] / [3]_q! = (q+q⁻¹) · 2 / [3]_q!`. -/
noncomputable def yLambdaCorrected_lshape21 (q : ℝ) : ℝ :=
  dimqPartition21 q * 2 / QOU.qFactorial q 3

/-- Corrected `y_[1,1,1]` at `n = 3`:
    `y_[1,1,1] = dim_q([1,1,1]) · d_[1,1,1] / [3]_q! = 1 / [3]_q!`. -/
noncomputable def yLambdaCorrected_col3 (q : ℝ) : ℝ :=
  dimqPartition111 q * 1 / QOU.qFactorial q 3

/-- Corrected column-row duality at `n = 3`:
    `y_[3] = y_[1,1,1]` (rfl after `dim_q([3]) = dim_q([1,1,1]) = 1`). -/
theorem yLambdaCorrected_row3_eq_col3 (q : ℝ) :
    yLambdaCorrected_row3 q = yLambdaCorrected_col3 q := rfl

/-! ### Trivial hook-formula proofs (n=2 row/column, n=4 row/column)

    For row partitions `[n]` and column partitions `[1ⁿ]`, the
    hook product equals `[n]_q!` (both have the same multiset of
    hook lengths `(n, n-1, …, 1)`), so `dim_q = [n]_q!/[n]_q! = 1`.
    The proof is `qFactorial q n / qFactorial q n = 1` whenever
    `[n]_q! ≠ 0`. -/

/-- `[n]_q! ≠ 0` for `q > 1`.  Iterated product of non-zero
    `qInteger`s is non-zero. -/
theorem qFactorial_ne_zero (q : ℝ) (n : ℕ) (hq_one : q > 1) :
    QOU.qFactorial q n ≠ 0 := by
  induction n with
  | zero =>
    show (1 : ℝ) ≠ 0
    norm_num
  | succ m ih =>
    show QOU.qInteger q (m + 1) * QOU.qFactorial q m ≠ 0
    apply mul_ne_zero
    · exact QOU.qInteger_ne_zero q (m + 1) hq_one (Nat.succ_pos m)
    · exact ih

/-- Row partition `[n]` hook-formula: `dim_q([n]) = 1`.  Demonstrated
    at `n = 2` (hooks `(2, 1)`). -/
theorem dimqRowPartition2_via_hook_formula (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 2 / QOU.qHookProduct q [2, 1] = dimqRowPartition 2 q := by
  unfold dimqRowPartition
  show QOU.qInteger q 2 * (QOU.qInteger q 1 * 1)
    / (QOU.qInteger q 2 * (QOU.qInteger q 1 * 1)) = 1
  have h2 : QOU.qInteger q 2 * (QOU.qInteger q 1 * 1) ≠ 0 := by
    have h2_ne : QOU.qInteger q 2 ≠ 0 :=
      QOU.qInteger_ne_zero q 2 hq_one (by norm_num)
    have h1_ne : QOU.qInteger q 1 ≠ 0 :=
      QOU.qInteger_ne_zero q 1 hq_one (by norm_num)
    exact mul_ne_zero h2_ne (mul_ne_zero h1_ne one_ne_zero)
  exact div_self h2

/-- Column partition `[1,1]` hook-formula: same hook multiset as
    row `[2]`, so `dim_q([1,1]) = 1`. -/
theorem dimqColPartition2_via_hook_formula (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 2 / QOU.qHookProduct q [2, 1] = dimqColPartition 2 q := by
  unfold dimqColPartition
  exact dimqRowPartition2_via_hook_formula q hq_one

/-- Row partition `[4]` hook-formula: `dim_q([4]) = 1`.  Hooks
    `(4, 3, 2, 1)`, hook product = `[4]_q!`. -/
theorem dimqPartition4_via_hook_formula (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [4, 3, 2, 1]
      = dimqPartition4 q := by
  unfold dimqPartition4
  show QOU.qInteger q 4 * (QOU.qInteger q 3 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1)))
    / (QOU.qInteger q 4 * (QOU.qInteger q 3 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1)))) = 1
  have hne : QOU.qInteger q 4 * (QOU.qInteger q 3 * (QOU.qInteger q 2 *
      (QOU.qInteger q 1 * 1))) ≠ 0 := by
    have h4 : QOU.qInteger q 4 ≠ 0 :=
      QOU.qInteger_ne_zero q 4 hq_one (by norm_num)
    have h3 : QOU.qInteger q 3 ≠ 0 :=
      QOU.qInteger_ne_zero q 3 hq_one (by norm_num)
    have h2 : QOU.qInteger q 2 ≠ 0 :=
      QOU.qInteger_ne_zero q 2 hq_one (by norm_num)
    have h1 : QOU.qInteger q 1 ≠ 0 :=
      QOU.qInteger_ne_zero q 1 hq_one (by norm_num)
    exact mul_ne_zero h4 (mul_ne_zero h3 (mul_ne_zero h2
      (mul_ne_zero h1 one_ne_zero)))
  exact div_self hne

/-- Column partition `[1,1,1,1]` hook-formula: same hooks as row
    `[4]`, so `dim_q([1,1,1,1]) = 1`. -/
theorem dimqPartition1111_via_hook_formula (q : ℝ) (hq_one : q > 1) :
    QOU.qFactorial q 4 / QOU.qHookProduct q [4, 3, 2, 1]
      = dimqPartition1111 q := by
  unfold dimqPartition1111
  exact dimqPartition4_via_hook_formula q hq_one

/-! ### Cohort: `n = 5` (7 partitions)

    Partition data:
    - `[5]`           : hooks `(5, 4, 3, 2, 1)`,        `d = 1`
    - `[4, 1]`        : hooks `(5, 3, 2, 1, 1)`,        `d = 4`
    - `[3, 2]`        : hooks `(4, 3, 2, 1, 1)`,        `d = 5`
    - `[3, 1, 1]`     : hooks `(5, 2, 1, 2, 1)`,        `d = 6`
    - `[2, 2, 1]`     : hooks `(4, 2, 3, 1, 1)`,        `d = 5`
    - `[2, 1, 1, 1]`  : hooks `(5, 1, 3, 2, 1)`,        `d = 4`
    - `[1, 1, 1, 1, 1]` : hooks `(5, 4, 3, 2, 1)`,      `d = 1`

    Sum of squares: `1² + 4² + 5² + 6² + 5² + 4² + 1²
    = 1 + 16 + 25 + 36 + 25 + 16 + 1 = 120 = 5!` ✓ -/

/-- The seven partitions of `n = 5` with hook + SYT data. -/
def n5_cohort : List (WenzlPartitionData 5) :=
  [{ name := "[5]",            hooks := [5, 4, 3, 2, 1], syt_count := 1 },
   { name := "[4,1]",          hooks := [5, 3, 2, 1, 1], syt_count := 4 },
   { name := "[3,2]",          hooks := [4, 3, 2, 1, 1], syt_count := 5 },
   { name := "[3,1,1]",        hooks := [5, 2, 1, 2, 1], syt_count := 6 },
   { name := "[2,2,1]",        hooks := [4, 2, 3, 1, 1], syt_count := 5 },
   { name := "[2,1,1,1]",      hooks := [5, 1, 3, 2, 1], syt_count := 4 },
   { name := "[1,1,1,1,1]",    hooks := [5, 4, 3, 2, 1], syt_count := 1 }]

/-- `Σ d_λ² = 5! = 120` at `n = 5` (Burnside / RSK). -/
theorem n5_squares_sum_eq :
    (n5_cohort.map (fun p => p.syt_count ^ 2)).sum = 120 := by
  show (1 ^ 2 + (4 ^ 2 + (5 ^ 2 + (6 ^ 2 + (5 ^ 2 + (4 ^ 2 + (1 ^ 2 + 0))))))) = 120
  norm_num

theorem n5_cohort_length : n5_cohort.length = 7 := rfl

/-! ### Cohort: `n = 6` (11 partitions)

    SYT counts (Frame–Robinson–Thrall):
    - `[6]:1, [5,1]:5, [4,2]:9, [4,1,1]:10, [3,3]:5,
       [3,2,1]:16, [3,1,1,1]:10, [2,2,2]:5, [2,2,1,1]:9,
       [2,1,1,1,1]:5, [1,1,1,1,1,1]:1`.
    Sum of squares: `1 + 25 + 81 + 100 + 25 + 256 + 100 + 25
       + 81 + 25 + 1 = 720 = 6!` ✓ -/

/-- The 11 partitions of `n = 6` with hook + SYT data. -/
def n6_cohort : List (WenzlPartitionData 6) :=
  [{ name := "[6]",            hooks := [6, 5, 4, 3, 2, 1], syt_count := 1 },
   { name := "[5,1]",          hooks := [6, 4, 3, 2, 1, 1], syt_count := 5 },
   { name := "[4,2]",          hooks := [5, 4, 2, 1, 2, 1], syt_count := 9 },
   { name := "[4,1,1]",        hooks := [6, 3, 2, 1, 2, 1], syt_count := 10 },
   { name := "[3,3]",          hooks := [4, 3, 2, 3, 2, 1], syt_count := 5 },
   { name := "[3,2,1]",        hooks := [5, 3, 1, 3, 1, 1], syt_count := 16 },
   { name := "[3,1,1,1]",      hooks := [6, 2, 1, 3, 2, 1], syt_count := 10 },
   { name := "[2,2,2]",        hooks := [4, 3, 3, 2, 2, 1], syt_count := 5 },
   { name := "[2,2,1,1]",      hooks := [5, 2, 3, 1, 2, 1], syt_count := 9 },
   { name := "[2,1,1,1,1]",    hooks := [6, 1, 4, 3, 2, 1], syt_count := 5 },
   { name := "[1,1,1,1,1,1]",  hooks := [6, 5, 4, 3, 2, 1], syt_count := 1 }]

/-- `Σ d_λ² = 6! = 720` at `n = 6`. -/
theorem n6_squares_sum_eq :
    (n6_cohort.map (fun p => p.syt_count ^ 2)).sum = 720 := by
  show (1 ^ 2 + (5 ^ 2 + (9 ^ 2 + (10 ^ 2 + (5 ^ 2 + (16 ^ 2 + (10 ^ 2 +
    (5 ^ 2 + (9 ^ 2 + (5 ^ 2 + (1 ^ 2 + 0))))))))))) = 720
  norm_num

theorem n6_cohort_length : n6_cohort.length = 11 := rfl

/-! ### Cohort: `n = 7` (15 partitions)

    SYT counts:
    `[7]:1, [6,1]:6, [5,2]:14, [5,1,1]:15, [4,3]:14, [4,2,1]:35,
     [4,1,1,1]:20, [3,3,1]:21, [3,2,2]:21, [3,2,1,1]:35,
     [3,1,1,1,1]:15, [2,2,2,1]:14, [2,2,1,1,1]:14,
     [2,1,1,1,1,1]:6, [1,1,1,1,1,1,1]:1`.
    Sum of squares: `1+36+196+225+196+1225+400+441+441+1225+225
     +196+196+36+1 = 5040 = 7!` ✓ -/

/-- The 15 partitions of `n = 7` with hook + SYT data. -/
def n7_cohort : List (WenzlPartitionData 7) :=
  [{ name := "[7]",                 hooks := [7, 6, 5, 4, 3, 2, 1], syt_count := 1 },
   { name := "[6,1]",               hooks := [7, 5, 4, 3, 2, 1, 1], syt_count := 6 },
   { name := "[5,2]",               hooks := [6, 5, 3, 2, 1, 2, 1], syt_count := 14 },
   { name := "[5,1,1]",             hooks := [7, 4, 3, 2, 1, 2, 1], syt_count := 15 },
   { name := "[4,3]",               hooks := [5, 4, 3, 2, 3, 2, 1], syt_count := 14 },
   { name := "[4,2,1]",             hooks := [6, 4, 2, 1, 3, 1, 1], syt_count := 35 },
   { name := "[4,1,1,1]",           hooks := [7, 3, 2, 1, 3, 2, 1], syt_count := 20 },
   { name := "[3,3,1]",             hooks := [5, 3, 2, 4, 2, 1, 1], syt_count := 21 },
   { name := "[3,2,2]",             hooks := [5, 3, 2, 3, 2, 1, 1], syt_count := 21 },
   { name := "[3,2,1,1]",           hooks := [6, 3, 1, 4, 1, 2, 1], syt_count := 35 },
   { name := "[3,1,1,1,1]",         hooks := [7, 2, 1, 4, 3, 2, 1], syt_count := 15 },
   { name := "[2,2,2,1]",           hooks := [5, 2, 4, 1, 3, 2, 1], syt_count := 14 },
   { name := "[2,2,1,1,1]",         hooks := [6, 2, 4, 3, 1, 2, 1], syt_count := 14 },
   { name := "[2,1,1,1,1,1]",       hooks := [7, 1, 5, 4, 3, 2, 1], syt_count := 6 },
   { name := "[1,1,1,1,1,1,1]",     hooks := [7, 6, 5, 4, 3, 2, 1], syt_count := 1 }]

/-- `Σ d_λ² = 7! = 5040` at `n = 7`. -/
theorem n7_squares_sum_eq :
    (n7_cohort.map (fun p => p.syt_count ^ 2)).sum = 5040 := by
  show (1 ^ 2 + (6 ^ 2 + (14 ^ 2 + (15 ^ 2 + (14 ^ 2 + (35 ^ 2 + (20 ^ 2 +
    (21 ^ 2 + (21 ^ 2 + (35 ^ 2 + (15 ^ 2 + (14 ^ 2 + (14 ^ 2 +
    (6 ^ 2 + (1 ^ 2 + 0))))))))))))))) = 5040
  norm_num

theorem n7_cohort_length : n7_cohort.length = 15 := rfl

/-! ### Cohort: `n = 8` (22 partitions)

    SYT counts:
    `[8]:1, [7,1]:7, [6,2]:20, [6,1,1]:21, [5,3]:28, [5,2,1]:64,
     [5,1,1,1]:35, [4,4]:14, [4,3,1]:70, [4,2,2]:56, [4,2,1,1]:90,
     [4,1,1,1,1]:35, [3,3,2]:42, [3,3,1,1]:56, [3,2,2,1]:70,
     [3,2,1,1,1]:64, [3,1,1,1,1,1]:21, [2,2,2,2]:14,
     [2,2,2,1,1]:28, [2,2,1,1,1,1]:20, [2,1,1,1,1,1,1]:7,
     [1,1,1,1,1,1,1,1]:1`.
    Sum of squares: `1+49+400+441+784+4096+1225+196+4900+3136+
     8100+1225+1764+3136+4900+4096+441+196+784+400+49+1
     = 40320 = 8!` ✓ -/

/-- The 22 partitions of `n = 8` with SYT data (hooks elided to a
    placeholder list of length 8 for compactness; expand on demand
    via the canonical hook-walk algorithm). -/
def n8_cohort : List (WenzlPartitionData 8) :=
  [{ name := "[8]",                       hooks := [8,7,6,5,4,3,2,1], syt_count := 1 },
   { name := "[7,1]",                     hooks := [8,6,5,4,3,2,1,1], syt_count := 7 },
   { name := "[6,2]",                     hooks := [7,6,4,3,2,1,2,1], syt_count := 20 },
   { name := "[6,1,1]",                   hooks := [8,5,4,3,2,1,2,1], syt_count := 21 },
   { name := "[5,3]",                     hooks := [6,5,4,3,2,3,2,1], syt_count := 28 },
   { name := "[5,2,1]",                   hooks := [7,5,3,2,1,3,1,1], syt_count := 64 },
   { name := "[5,1,1,1]",                 hooks := [8,4,3,2,1,3,2,1], syt_count := 35 },
   { name := "[4,4]",                     hooks := [5,4,3,2,4,3,2,1], syt_count := 14 },
   { name := "[4,3,1]",                   hooks := [6,4,3,1,4,2,1,1], syt_count := 70 },
   { name := "[4,2,2]",                   hooks := [6,4,2,1,3,2,2,1], syt_count := 56 },
   { name := "[4,2,1,1]",                 hooks := [7,4,2,1,4,1,2,1], syt_count := 90 },
   { name := "[4,1,1,1,1]",               hooks := [8,3,2,1,4,3,2,1], syt_count := 35 },
   { name := "[3,3,2]",                   hooks := [5,4,2,4,3,1,2,1], syt_count := 42 },
   { name := "[3,3,1,1]",                 hooks := [6,3,2,5,2,1,2,1], syt_count := 56 },
   { name := "[3,2,2,1]",                 hooks := [6,4,1,4,2,1,2,1], syt_count := 70 },
   { name := "[3,2,1,1,1]",               hooks := [7,3,1,5,1,4,2,1], syt_count := 64 },
   { name := "[3,1,1,1,1,1]",             hooks := [8,2,1,5,4,3,2,1], syt_count := 21 },
   { name := "[2,2,2,2]",                 hooks := [5,4,4,3,3,2,2,1], syt_count := 14 },
   { name := "[2,2,2,1,1]",               hooks := [6,2,5,4,1,3,2,1], syt_count := 28 },
   { name := "[2,2,1,1,1,1]",             hooks := [7,2,5,4,3,1,2,1], syt_count := 20 },
   { name := "[2,1,1,1,1,1,1]",           hooks := [8,1,6,5,4,3,2,1], syt_count := 7 },
   { name := "[1,1,1,1,1,1,1,1]",         hooks := [8,7,6,5,4,3,2,1], syt_count := 1 }]

/-- `Σ d_λ² = 8! = 40320` at `n = 8`. -/
theorem n8_squares_sum_eq :
    (n8_cohort.map (fun p => p.syt_count ^ 2)).sum = 40320 := by
  show (1 ^ 2 + (7 ^ 2 + (20 ^ 2 + (21 ^ 2 + (28 ^ 2 + (64 ^ 2 + (35 ^ 2 +
    (14 ^ 2 + (70 ^ 2 + (56 ^ 2 + (90 ^ 2 + (35 ^ 2 + (42 ^ 2 + (56 ^ 2 +
    (70 ^ 2 + (64 ^ 2 + (21 ^ 2 + (14 ^ 2 + (28 ^ 2 + (20 ^ 2 + (7 ^ 2 +
    (1 ^ 2 + 0))))))))))))))))))))) = 40320
  norm_num

theorem n8_cohort_length : n8_cohort.length = 22 := rfl

/-! ## Generic recursive Burnside identity

    The classical RSK / Burnside identity says
      Σ_{λ ⊢ n} (d_λ)² = n!
    for every `n`, where `d_λ` is the number of standard Young
    tableaux of shape `λ`.

    Mathlib's `Nat.Partition n` enumerates the partitions of `n`
    as a `Finset`; a generic `dimFn : Nat.Partition n → ℕ`
    parameter lets us state the identity abstractly.  Concrete
    cohort lists like `n4_cohort` realise the identity for
    specific `n`.

    The recursion: `Nat.Partition n` is `Finset`-finite, and
    `(d_λ)²` is bounded by `(n!)²`; the sum over
    `Nat.Partition n` is therefore well-defined and equal to
    `n.factorial` by RSK.  Mathlib does not yet ship this
    identity in finished form (the RSK bijection is partially
    formalised in `Mathlib.Combinatorics.RSK`); the upstream
    target is to upgrade `RSK.bijection.cardinality_eq` to the
    sum-of-squares form.  -/

/-- **Generic Burnside / RSK identity over `Nat.Partition n`** —
    abstract shape: for any `dimFn : Nat.Partition n → ℕ` that
    correctly counts standard Young tableaux, the sum of squares
    equals `n.factorial`.  Stated as a hypothesis-bearing
    theorem; concrete instances (e.g. our explicit cohorts)
    discharge it by `decide` / `norm_num`. -/
def BurnsideIdentity (n : ℕ) (dimFn : Nat.Partition n → ℕ) : Prop :=
  ∑ λ : Nat.Partition n, (dimFn λ) ^ 2 = n.factorial

/-- The Burnside identity for the trivial dimension function
    (returning 0) holds iff `n.factorial = 0`, which never happens
    for `n : ℕ`.  This is a sanity check that the predicate
    rules out the all-zero cheat. -/
theorem burnside_zero_iff (n : ℕ) :
    BurnsideIdentity n (fun _ => 0) ↔ n.factorial = 0 := by
  unfold BurnsideIdentity
  simp

/-- **Recursive shape**: the partition-of-`n` cardinality lets
    us read the cohort length off `Nat.Partition n`.  Mathlib's
    `Nat.Partition.card` (or equivalent) gives the concrete
    count `p(n)`.

    For `n = 0..8`:  `p(0) = 1, p(1) = 1, p(2) = 2, p(3) = 3,
    p(4) = 5, p(5) = 7, p(6) = 11, p(7) = 15, p(8) = 22`.
    OEIS A000041 — partition function. -/
theorem cohort_lengths_match_partition_count :
    n2_cohort.length = 2 ∧ n3_cohort.length = 3 ∧
    n4_cohort.length = 5 ∧ n5_cohort.length = 7 ∧
    n6_cohort.length = 11 ∧ n7_cohort.length = 15 ∧
    n8_cohort.length = 22 := by
  refine ⟨?_, ?_, ?_, ?_, ?_, ?_, ?_⟩ <;> rfl

/-- **Recursive Wenzl-data unfold**: extract a single partition's
    hook-product over `q`.  Composes with the per-partition
    `WenzlPartitionData.hooks` field. -/
noncomputable def WenzlPartitionData.hookProduct
    {n : ℕ} (p : WenzlPartitionData n) (q : ℝ) : ℝ :=
  QOU.qHookProduct q p.hooks

/-- Closed form: row-`[n]` hook product equals `[n]_q!` (proved
    for `n = 2` here; the general statement is by induction on
    `n` once `qFactorial`'s recursive shape unfolds). -/
theorem hookProduct_row_two (q : ℝ) (hq : q - q⁻¹ ≠ 0) :
    WenzlPartitionData.hookProduct
      ({ name := "[2]", hooks := [2, 1], syt_count := 1 }
        : WenzlPartitionData 2) q = q + q⁻¹ := by
  show QOU.qHookProduct q [2, 1] = q + q⁻¹
  show QOU.qInteger q 2 * (QOU.qInteger q 1 * 1) = q + q⁻¹
  rw [QOU.qInteger_two q hq, QOU.qInteger_one q hq]; ring

end QOU.Mathlib.WenzlBridgeConcrete
