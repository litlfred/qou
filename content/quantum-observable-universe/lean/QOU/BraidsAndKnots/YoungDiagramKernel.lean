import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.BigOperators.Ring.List
import Mathlib.Tactic.IntervalCases

/-!
# QOU.BraidsAndKnots.YoungDiagramKernel — elementary Lean infrastructure for the Δ_λ covariance kernel

The Δ_λ growth bound (#3939) reduces (via #3959) to the covariance kernel
`Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`, equivalently the elementary content form

    ∀ k,  Σ_{λ ⊢ k} (f^λ)³ · (Σ_□ c(□)² − C(k,2))  ≤  0,

with `f^λ` = number of standard Young tableaux (hook-length dimension) and `c(□)` = content.
Stating this in Lean does **not** need `S_k`-character theory or free probability (which Mathlib
lacks) — only the hook-length dimension and the content sum, which this file defines
self-contained on `List ℕ` (weakly-decreasing parts). The full character / free-cumulant framing
(`Σ̂₃ = R₄ + R₂`, `E_Planch[R₄] = −k`) that situates the kernel in Biane–Śniady / Kerov-CLT theory
is verified computationally in `computations/deltalambda/wlambda_covariance_kernel_frontier.py`.

The kernel itself is **OPEN** (a Biane–Śniady / Kerov-CLT character-ratio anti-correlation),
carried here as an honest `sorry`-conjecture (§3b) with the elementary statement machine-checkable
as well-typed. Verified `k ≤ 30`. The `sorry` is a **conjecture**, not a proof gap.
-/

namespace QOU.BraidsAndKnots.YoungDiagramKernel

/-- Enumerate partitions of `n` with parts `≤ maxPart`, structural on `fuel` (take `fuel = n`).
Each partition is a weakly-decreasing `List ℕ` of positive parts. -/
def partsFuel : ℕ → ℕ → ℕ → List (List ℕ)
  | _, 0, _ => [[]]
  | 0, _, _ => []
  | (f + 1), (n + 1), maxP =>
      (List.range' 1 (min (n + 1) maxP)).flatMap fun i =>
        (partsFuel f (n + 1 - i) i).map (fun r => i :: r)

/-- Partitions of `n` (as weakly-decreasing lists of positive parts). -/
def partsOf (n : ℕ) : List (List ℕ) := partsFuel n n n

/-- Content-square sum `Σ_□ c(□)²`, `c(i,j) = j − i`, over cells of the diagram `l`. -/
def contentSq (l : List ℕ) : ℤ :=
  ((List.range l.length).map (fun i =>
    ((List.range (l.getD i 0)).map (fun j => ((j : ℤ) - (i : ℤ)) ^ 2)).sum)).sum

/-- Conjugate partition: `λ'_j = #{ i : λ_i > j }`, for `j = 0 .. λ_0 − 1`. -/
def conj (l : List ℕ) : List ℕ :=
  (List.range (l.headD 0)).map (fun j => l.countP (fun x => decide (j < x)))

/-- Product of hook lengths over all cells: hook`(i,j) = λ_i + λ'_j − i − j − 1`. -/
def hookProd (l : List ℕ) : ℕ :=
  let cj := conj l
  ((List.range l.length).map (fun i =>
    let li := l.getD i 0
    ((List.range li).map (fun j => li + cj.getD j 0 - j - i - 1)).prod)).prod

/-- Hook-length dimension `f^λ = |λ|! / ∏_□ h(□)` (number of standard Young tableaux). -/
def sytDim (l : List ℕ) : ℕ := Nat.factorial l.sum / hookProd l

/-- The elementary content form of the covariance kernel value at level `k`:
`Σ_{λ ⊢ k} (f^λ)³ · (Σ_□ c(□)² − C(k,2))`. -/
def kernelValue (k : ℕ) : ℤ :=
  ((partsOf k).map (fun l =>
    (sytDim l : ℤ) ^ 3 * (contentSq l - ((k * (k - 1) / 2 : ℕ) : ℤ)))).sum

/-- **CONJECTURE (OPEN).** The covariance kernel `Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`, in its
elementary content form: for every `k`, `Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0`. This is the sole
open input of the Δ_λ super-exponential growth bound (`WstdSuperExpBound.lean`, via the reduction
`DeltaLambdaDReduction.D_of_T3_nonpos`). It is a Biane–Śniady / Kerov-CLT character-ratio
anti-correlation; verified `k ≤ 30` computationally. Not proved.
-- Ref: [manuscript] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md -/
theorem covariance_kernel_conjecture (k : ℕ) : kernelValue k ≤ 0 := by
  sorry

/-- **Base cases (sorry-free).** The covariance-kernel conjecture holds for every `k ≤ 7`,
proved outright by kernel evaluation (`decide`) rather than the computational spot-check.
This discharges the small-`k` tail of `covariance_kernel_conjecture` in Lean; the general
`∀ k` statement remains the open epic input (Śniady genus expansion, `qou-x631`). -/
theorem kernelValue_nonpos_of_le_seven (k : ℕ) (hk : k ≤ 7) : kernelValue k ≤ 0 := by
  interval_cases k <;> decide

end QOU.BraidsAndKnots.YoungDiagramKernel
