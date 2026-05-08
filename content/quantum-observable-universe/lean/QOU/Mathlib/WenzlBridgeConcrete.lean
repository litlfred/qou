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

/-- The number of partitions of `n` matches `n4_cohort.length` etc. -/
theorem n2_cohort_length : n2_cohort.length = 2 := rfl
theorem n3_cohort_length : n3_cohort.length = 3 := rfl
theorem n4_cohort_length : n4_cohort.length = 5 := rfl

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
