import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Algebra.BigOperators.Ring.List
import Mathlib.Tactic.Ring
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

/-- The 3-cycle class-sum eigenvalue on the irrep `λ`: `ω₃(λ) = Σ_□ c(□)² − C(k,2)`. -/
def omega3 (k : ℕ) (l : List ℕ) : ℤ := contentSq l - ((k * (k - 1) / 2 : ℕ) : ℤ)

/-- The 4th free cumulant `R₄` of the transition measure of `λ`, in Biane's normalisation
`Σ̂₃ = R₄ + R₂` with `R₂ = k`: `R₄(λ) = 3·ω₃(λ) − k`. This is an **exactly affine** relabelling of
the content spread `ω₃` — verified `E_Planch[R₄] = −k` computationally
(`wlambda_covariance_epic_phase2.py`, `k ≤ 8`). -/
def r4Value (k : ℕ) (l : List ℕ) : ℤ := 3 * omega3 k l - (k : ℤ)

/-- Cube-of-dimension total `Σ_{λ ⊢ k} (f^λ)³` (the `(f^λ)³`-biasing normaliser). -/
def cubeSum (k : ℕ) : ℤ := ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 3)).sum

/-- The `R₄`-weighted total `Σ_{λ ⊢ k} (f^λ)³ · R₄(λ)`. -/
def r4WeightedSum (k : ℕ) : ℤ :=
  ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 3 * r4Value k l)).sum

/-- General list form of the affine linearity: for any list `L` of diagrams,
`Σ_l (f^l)³ · (3·ω₃(l) − k) = 3·Σ_l (f^l)³·ω₃(l) − k·Σ_l (f^l)³`. Sorry-free (induction on `L`);
it exhibits exactly how the `−k` shift enters at the **summed** level. -/
theorem r4_sum_affine_list (k : ℕ) (L : List (List ℕ)) :
    (L.map (fun l => (sytDim l : ℤ) ^ 3 * r4Value k l)).sum
      = 3 * (L.map (fun l => (sytDim l : ℤ) ^ 3 * omega3 k l)).sum
          - (k : ℤ) * (L.map (fun l => (sytDim l : ℤ) ^ 3)).sum := by
  induction L with
  | nil => simp
  | cons a t ih =>
      simp only [List.map_cons, List.sum_cons]
      rw [ih]
      simp only [r4Value]
      ring

/-- **Sum-level affine identity (sorry-free).** `Σ_{λ⊢k} (f^λ)³ R₄(λ) = 3·kernelValue(k) − k·cubeSum(k)`.
The `R₄`-weighted total differs from the covariance kernel only by the affine cube-sum term `k·cubeSum`.
Consequence: adding the constant `−k` to `ω₃` shifts the raw weighted sum but leaves the *covariance*
`Cov_Planch(f^λ, ·)` unchanged, so the free-cumulant form `Cov_Planch(f^λ, R₄) ≤ 0` is the **same
inequality** as the content form `Cov_Planch(f^λ, ω₃) ≤ 0` — `R₄` is not an independent handle on the
open kernel. (Phase-2 finding, `qou-x631`.) -/
theorem r4WeightedSum_eq (k : ℕ) :
    r4WeightedSum k = 3 * kernelValue k - (k : ℤ) * cubeSum k := by
  unfold r4WeightedSum kernelValue cubeSum
  have h := r4_sum_affine_list k (partsOf k)
  simpa [omega3] using h

/-- Second-moment (dim²-weighted) content-spread total `Σ_{λ⊢k} (f^λ)² · ω₃(λ)`. -/
def secondMomentKernel (k : ℕ) : ℤ :=
  ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 2 * omega3 k l)).sum

/-- **The dim²-weighted 3-cycle content-spread total VANISHES** (Lean-verified, `3 ≤ k ≤ 7`):
`Σ_{λ⊢k} (f^λ)² ω₃(λ) = 0`. This is `k!·E_Planch[ω₃] = 0` (the Plancherel content mean is `C(k,2)`) —
an **exact** identity, not conjectural. It isolates the open kernel as the *first-order response to the
extra dimension factor*: `cov(k) = Σ (f^λ)³ ω₃ = k!·Cov_Planch(f^λ, ω₃)`, a genuine dimension-tilt
covariance (Ivanov–Olshanski Prop 5.1; the `dim³` weight has one surplus `dim` beyond column
orthogonality, so — unlike this `dim²` total — it lies outside the polynomial-function algebra `A`). -/
theorem secondMomentKernel_eq_zero_of_le_seven (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 7) :
    secondMomentKernel k = 0 := by
  interval_cases k <;> decide

/-- Lean-kernel-verified base **values** of `kernelValue` (checked by `decide` over the full
partition/hook machinery, grounding the otherwise Python-only verification). -/
theorem kernelValue_base_values :
    kernelValue 3 = -4 ∧ kernelValue 4 = -16 ∧ kernelValue 5 = -320 ∧
      kernelValue 6 = -10400 ∧ kernelValue 7 = -163520 := by decide

/-- The covariance-kernel conjecture is **Lean-verified for `3 ≤ k ≤ 7`** (kernel `decide`), a
machine-checked base for the open general statement below. -/
theorem kernelValue_nonpos_of_le_seven (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 7) :
    kernelValue k ≤ 0 := by
  interval_cases k <;> decide

/-- Content-square is **conjugation-invariant** — verified for all `λ ⊢ k`, `k ≤ 6` (`decide`):
`contentSq (conj λ) = contentSq λ`. Reason: the transpose bijection on cells `(i,j) ↦ (j,i)` sends the
content `j−i` to `i−j`, and `(i−j)² = (j−i)²`. Consequence: `ω₃` is conjugation-symmetric, hence
**U-shaped** (large at both the row and column extremes, small in the balanced middle) — which is
exactly why no monotone / FKG / comonotone certificate for the kernel can work. The general (`∀`
sorted `l`) statement follows from the sorted-List transpose bijection
`cellSum (conj l) f = cellSum l (fun i j => f j i)` (via `len (conj l) = l.headD 0`,
`conj l |>.getD r 0 = #{i : l.getD i 0 > r}`, and the staircase equivalence
`c < (conj l).getD r 0 ↔ r < l.getD c 0`); that infra is not yet built here. -/
theorem contentSq_conj_invariant_of_le_six (k : ℕ) (hk : k ≤ 6) :
    ∀ l ∈ partsOf k, contentSq (conj l) = contentSq l := by
  interval_cases k <;> decide

/-- `ω₃` is conjugation-invariant on `λ ⊢ k`, `k ≤ 6` (`decide`): `omega3 k (conj λ) = omega3 k λ`
(immediate from `contentSq_conj_invariant_of_le_six`, since `ω₃` only shifts `contentSq` by a
`λ`-independent constant). This symmetry pairs the kernel summands `(f^λ)³ω₃(λ)` into conjugate pairs
(except at self-conjugate `λ`), the structural obstruction to any local sign certificate. -/
theorem omega3_conj_invariant_of_le_six (k : ℕ) (hk : k ≤ 6) :
    ∀ l ∈ partsOf k, omega3 k (conj l) = omega3 k l := by
  interval_cases k <;> decide

/-- **CONJECTURE (OPEN).** The covariance kernel `Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`, in its
elementary content form: for every `k`, `Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0`. This is the sole
open input of the Δ_λ super-exponential growth bound (`WstdSuperExpBound.lean`, via the reduction
`DeltaLambdaDReduction.D_of_T3_nonpos`). It is a Biane–Śniady / Kerov-CLT character-ratio
anti-correlation; verified `k ≤ 30` computationally. Not proved.
-- Ref: [manuscript] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md -/
theorem covariance_kernel_conjecture (k : ℕ) : kernelValue k ≤ 0 := by
  sorry

end QOU.BraidsAndKnots.YoungDiagramKernel
