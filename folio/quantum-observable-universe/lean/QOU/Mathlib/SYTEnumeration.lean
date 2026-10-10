import QOU.BraidKnot.IdentityIContentDecomposition

/-!
# QOU.Mathlib.SYTEnumeration — brute-force `#SYT` over the list model, validating the hook formula

The Frame–Robinson–Thrall hook-length dimension `dimHLF l = (∑l)!/∏h_c` is the repo's combinatorial
`#SYT(λ)` (`QOU.BraidKnot.IdentityI`).  It is `decide`-validated only *in aggregate*
(`dim_validated_le12 : Σ_λ dimHLF(λ)² = n!`, the RSK sum-of-squares) — never **per shape** against an
independent count of actual standard tableaux.

This file supplies the missing direct check: a **computable brute-force enumeration** of standard
Young tableaux of a shape `l : List ℕ` (weakly-decreasing row lengths), and `decide`-proves
`numSYTenum l = dimHLF l` **for every shape with `n = ∑l ≤ 4`** — confirming the hook formula gives
the genuine `#SYT` shape by shape, not merely on the sum.  (Bounded at `n ≤ 4` because the count
enumerates all `n!` fillings in the kernel; the aggregate `dim_validated_le12` already covers
`n ≤ 12` via the cheaper hook product.)

A standard filling is a bijection of the `n` cells onto `{1,…,n}` that is strictly increasing along
rows and down columns.  We represent a candidate as a permutation of `[1,…,n]` laid out in row-major
order, reshape it into rows by `l`, and check strict rows + strict columns — all `Bool`, hence
`Decidable`.  Pure combinatorics on `ℕ`; nothing archimedean; no fit.

**Why a hand-rolled `allPerms`, not `List.permutations`.**  Mathlib's `List.permutations` is defined
by well-founded recursion, which the kernel does **not** reduce — `decide` gets stuck on it.  The
generator here (`allPerms`/`insertEverywhere`) is *structurally* recursive on the list, so it reduces
definitionally in the kernel; this keeps `numSYTenum_eq_dimHLF_le4` a genuine, fully kernel-checked
`decide` proof rather than a `native_decide` (which would offload to compiled code — avoidable here,
and contentious per AGENTS.md §1a).
-/

namespace QOU.Mathlib.SYTEnum

open QOU.BraidKnot.IdentityI (dimHLF)

/-- Reshape a flat list `a` into rows of lengths given by `l` (row-major). -/
def chunk : List ℕ → List ℕ → List (List ℕ)
  | [], _ => []
  | len :: ls, a => a.take len :: chunk ls (a.drop len)

/-- Is a list strictly increasing? -/
def strictInc : List ℕ → Bool
  | [] => true
  | [_] => true
  | a :: b :: rest => (a < b) && strictInc (b :: rest)

/-- Are adjacent rows strictly increasing column-wise (`rᵢ[j] < rᵢ₊₁[j]` for every `j` of the
shorter, lower row)?  `(r₂.zip r₁)` pairs `(r₂[j], r₁[j])`; require `r₁[j] < r₂[j]`. -/
def colsOK : List (List ℕ) → Bool
  | [] => true
  | [_] => true
  | r1 :: r2 :: rest => (r2.zip r1).all (fun p => p.2 < p.1) && colsOK (r2 :: rest)

/-- A flat filling `a` (a permutation of `[1,…,n]` in row-major order) is a standard tableau of
shape `l`: reshape and check strict rows and strict columns. -/
def isStdFilling (l : List ℕ) (a : List ℕ) : Bool :=
  let rows := chunk l a
  rows.all strictInc && colsOK rows

/-- All ways to insert `x` into `l` (at each of the `|l|+1` gaps).  Structural recursion on `l`. -/
def insertEverywhere (x : ℕ) : List ℕ → List (List ℕ)
  | [] => [[x]]
  | a :: rest => (x :: a :: rest) :: (insertEverywhere x rest).map (a :: ·)

/-- All permutations of `l`, by structural recursion (kernel-reducible, unlike `List.permutations`,
which is well-founded and stalls `decide`). -/
def allPerms : List ℕ → List (List ℕ)
  | [] => [[]]
  | a :: rest => (allPerms rest).flatMap (insertEverywhere a)

/-- **Brute-force `#SYT(λ)`**: the number of permutations of `[1,…,∑l]` that are standard fillings
of shape `l`.  Computable (bijectivity is built in by ranging over permutations). -/
def numSYTenum (l : List ℕ) : ℕ :=
  (allPerms ((List.range l.sum).map (· + 1))).countP (isStdFilling l)

/-- The partitions with `n = ∑ ≤ 4` (every shape; weakly-decreasing row lengths). -/
def shapesLE4 : List (List ℕ) :=
  [[1], [2], [1, 1], [3], [2, 1], [1, 1, 1],
   [4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]

/-- The partitions of `n`, grouped by `n`, for `n = 1,…,4` (paired with `n` for the `n!` check). -/
def partitionsByN : List (ℕ × List (List ℕ)) :=
  [(1, [[1]]),
   (2, [[2], [1, 1]]),
   (3, [[3], [2, 1], [1, 1, 1]]),
   (4, [[4], [3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]])]

/-- **Per-shape validation of the hook-length formula (sorry-free).** For every shape with
`∑ ≤ 4`, the brute-force standard-tableau count equals the Frame–Robinson–Thrall hook dimension:
`#SYT(λ) = dimHLF(λ)`.  An independent per-shape check that `dim_validated_le12` (sum only) does not
provide. -/
theorem numSYTenum_eq_dimHLF_le4 :
    ∀ l ∈ shapesLE4, numSYTenum l = dimHLF l := by decide

/-- **Identity I axiom (i), validated against genuine standard-tableau counts (sorry-free).**  For
every `n ≤ 4`, the RSK / Burnside sum of squares of the *brute-force* `#SYT(λ)` counts equals `n!`:

    Σ_{λ ⊢ n} (numSYTenum λ)² = n!.

`dim_validated_le12` proves the same sum-of-squares for the *hook* dimension `dimHLF`; this proves it
for the **independently-enumerated** standard-tableau count — so the RSK identity holds at the level
of actual tableaux, not merely of the hook closed form.  Together with `numSYTenum_eq_dimHLF_le4`
(per-shape `numSYTenum = dimHLF`), this re-grounds `dim_validated_le12` itself in genuine `#SYT` for
`n ≤ 4`. -/
theorem rsk_sumSq_eq_factorial_le4 :
    ∀ nps ∈ partitionsByN, (nps.2.map (fun l => (numSYTenum l) ^ 2)).sum = nps.1.factorial := by
  decide

/-! ## Extension to `n = 5` and `n = 6`

The `n ≤ 4` checks above enumerate `n!` fillings in the kernel.  `n = 5` (`120` fillings/shape) still
`decide`s at the default `maxRecDepth`; `n = 6` (`720` fillings/shape) needs the recursion-depth limit
raised (the structural `allPerms`/`insertEverywhere` recursion goes `720` deep per shape).  `n = 7`
(`5040` fillings/shape) is left to the aggregate `dim_validated_le12`: the per-shape kernel enumeration
becomes the build-time bottleneck, not a soundness limit — recorded here, not silently dropped. -/

/-- The partitions of `5` (every weakly-decreasing shape with `∑ = 5`). -/
def shapes5 : List (List ℕ) :=
  [[5], [4, 1], [3, 2], [3, 1, 1], [2, 2, 1], [2, 1, 1, 1], [1, 1, 1, 1, 1]]

/-- The partitions of `6` (every weakly-decreasing shape with `∑ = 6`). -/
def shapes6 : List (List ℕ) :=
  [[6], [5, 1], [4, 2], [4, 1, 1], [3, 3], [3, 2, 1], [3, 1, 1, 1],
   [2, 2, 2], [2, 2, 1, 1], [2, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

/-- **Per-shape hook-length validation at `n = 5` (sorry-free).** `#SYT(λ) = dimHLF(λ)` for every
shape of `5`, extending `numSYTenum_eq_dimHLF_le4`. -/
theorem numSYTenum_eq_dimHLF_5 :
    ∀ l ∈ shapes5, numSYTenum l = dimHLF l := by decide

set_option maxRecDepth 20000 in
/-- **Per-shape hook-length validation at `n = 6` (sorry-free).** `#SYT(λ) = dimHLF(λ)` for every
shape of `6`.  Needs `maxRecDepth` raised for the `720`-deep structural permutation recursion. -/
theorem numSYTenum_eq_dimHLF_6 :
    ∀ l ∈ shapes6, numSYTenum l = dimHLF l := by decide

/-- **RSK sum-of-squares at `n = 5` (sorry-free).** `Σ_{λ ⊢ 5} (#SYT λ)² = 5!`, on the
independently-enumerated standard-tableau count. -/
theorem rsk_sumSq_eq_factorial_5 :
    (shapes5.map (fun l => (numSYTenum l) ^ 2)).sum = (5).factorial := by decide

set_option maxRecDepth 20000 in
/-- **RSK sum-of-squares at `n = 6` (sorry-free).** `Σ_{λ ⊢ 6} (#SYT λ)² = 6!`. -/
theorem rsk_sumSq_eq_factorial_6 :
    (shapes6.map (fun l => (numSYTenum l) ^ 2)).sum = (6).factorial := by decide

end QOU.Mathlib.SYTEnum
