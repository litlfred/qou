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

/-- Sum of hook lengths over all cells: `Σ_□ h(□)`, `h(i,j) = λ_i + λ'_j − i − j − 1`. -/
def hookSum (l : List ℕ) : ℕ :=
  let cj := conj l
  ((List.range l.length).map (fun i =>
    let li := l.getD i 0
    ((List.range li).map (fun j => li + cj.getD j 0 - j - i - 1)).sum)).sum

/-- Row-content statistic `n_λ = Σ_i i·λ_i` (0-indexed rows). -/
def nLambda (l : List ℕ) : ℕ :=
  ((List.range l.length).map (fun i => i * l.getD i 0)).sum

/-- Sum of squared hook lengths `Σ_□ h(□)²`. -/
def hookSqSum (l : List ℕ) : ℤ :=
  let cj := conj l
  ((List.range l.length).map (fun i =>
    let li := l.getD i 0
    ((List.range li).map (fun j => (((li + cj.getD j 0 - j - i - 1 : ℕ)) : ℤ) ^ 2)).sum)).sum

/-- `(k!)²`-scaled Plancherel covariance `(k!)²·Cov_Planch(X, Y)` of two `λ`-statistics at level `k`,
kept over `ℤ` (the `dim²/k!` Plancherel weights cleared to integers):
`k!·Σ_λ (f^λ)² X(λ)Y(λ) − (Σ_λ (f^λ)² X(λ))(Σ_λ (f^λ)² Y(λ))`. -/
def scaledCov (k : ℕ) (X Y : List ℕ → ℤ) : ℤ :=
  (Nat.factorial k : ℤ) * ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 2 * X l * Y l)).sum
    - ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 2 * X l)).sum
      * ((partsOf k).map (fun l => (sytDim l : ℤ) ^ 2 * Y l)).sum

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
orthogonality, so — unlike this `dim²` total — it lies outside the polynomial-function algebra `A`).

**Why `3 ≤ k ≤ 7` is a Lean artifact, and exactly what would remove it.** The identity holds for
every `k`, and the shortest route is Jucys–Murphy rather than Prop 5.1. Writing `X_i = Σ_{j<i} (i j)`,
the JM theorem gives that `Σ_i X_i²` is **central**, acting on the irrep `λ` by the eigenvalue
`Σ_□ c(□)²` (each standard-tableau basis vector picks up `c(□)²` box by box). Expanding the square,
`(i j)² = 1` contributes `C(k,2)·1`, and every cross term `(i j)(i l)` with `j ≠ l` is a **3-cycle**:

  `Σ_i X_i² = C(k,2)·1 + (3-cycle class sum)`.

Reading off eigenvalues, `Σ_□ c(□)² = C(k,2) + const·ω^λ_{(3)}`, so
`Σ_λ (f^λ)² ω₃(λ) ∝ Σ_λ f^λ χ^λ(3-cyc) = 0` by **column orthogonality** — the whole identity is that
one vanishing, with no asymptotics anywhere.

Lifting `interval_cases … decide` to a general-`k` proof therefore needs exactly three imports from
the Specht/`S_n` epic (`sp00`), and nothing else: (i) the JM elements with their content
eigenvalues, (ii) centrality of `Σ_i X_i^m`, (iii) column orthogonality `Σ_λ f^λ χ^λ(σ) = 0` for
`σ ≠ 1`. That is the concrete `sp00` dependency for this lemma; the `k ≤ 7` bound is a `decide`
budget, not a mathematical frontier. (Recorded 2026-08-15 while attacking `qou-v8t7`; the reduction
is standard, the point here is naming the three inputs so `sp00` can be aimed at them.) -/
theorem secondMomentKernel_eq_zero_of_le_seven (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 7) :
    secondMomentKernel k = 0 := by
  interval_cases k <;> decide

/-- Lean-kernel-verified base **values** of `kernelValue` (checked by `decide` over the full
partition/hook machinery, grounding the otherwise Python-only verification). -/
theorem kernelValue_base_values :
    kernelValue 3 = -4 ∧ kernelValue 4 = -16 ∧ kernelValue 5 = -320 ∧
      kernelValue 6 = -10400 ∧ kernelValue 7 = -163520 := by decide

set_option maxRecDepth 400000 in
set_option maxHeartbeats 4000000 in
/-- Extended Lean-kernel-verified base **values** `k = 8..14` — the exact integers, cross-checking
the Python pipeline (`wlambda_covariance_kernel_frontier.py`) against the kernel evaluator over
the same partition/hook machinery. -/
theorem kernelValue_base_values_to_fourteen :
    kernelValue 8 = -3224704 ∧ kernelValue 9 = -106339296 ∧
      kernelValue 10 = -4722309120 ∧ kernelValue 11 = -176931720240 ∧
      kernelValue 12 = -6632383721920 ∧ kernelValue 13 = -289895599309888 ∧
      kernelValue 14 = -16141386718690688 :=
  ⟨by decide, by decide, by decide, by decide, by decide, by decide, by decide⟩

/-- The covariance-kernel conjecture is **Lean-verified for `3 ≤ k ≤ 7`** (kernel `decide`), a
machine-checked base for the open general statement below. -/
theorem kernelValue_nonpos_of_le_seven (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 7) :
    kernelValue k ≤ 0 := by
  interval_cases k <;> decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 8000000 in
/-- **Extended machine-checked base: the kernel conjecture holds for `3 ≤ k ≤ 20`** (kernel
`decide` over the full partition/hook/dimension machinery; `maxRecDepth`/`maxHeartbeats` raised
for the larger enumerations — elaboration limits, not a change in trust: the kernel still checks
every step). Extends the `k ≤ 7` base to cover, in particular, the whole `k ≤ 14` range on which
the two open pincer legs (`Cov₂(ln f, ω₃) ≤ 0` and the interpolation remainder bound) have been
numerically verified — so any future effective-constant proof of those legs closes the conjecture
down to a floor the kernel has already certified. -/
theorem kernelValue_nonpos_of_le_twenty (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 20) :
    kernelValue k ≤ 0 := by
  rcases le_or_gt k 7 with h7 | h7
  · exact kernelValue_nonpos_of_le_seven k hk h7
  · interval_cases k <;> decide

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 8000000 in
/-- **Extended machine-checked base for the dim²-weighted vanishing: `k ≤ 20`.** Extends
`secondMomentKernel_eq_zero_of_le_seven` over the same range as the kernel base
`kernelValue_nonpos_of_le_twenty`. Unlike the kernel conjecture, this identity is **not**
conjectural — it is `k!·E_Planch[ω₃] = 0`, exact for every `k` (the identity coefficient of
`Σ_i X_i²` in the Jucys–Murphy calculus is `C(k,2)`); what the `decide` supplies is a certified
floor pending the general character-orthogonality proof, which needs the JM-eigenvalue ⇒
Plancherel-mean bridge (Sₙ representation-theory infrastructure, not yet in the corpus). -/
theorem secondMomentKernel_eq_zero_of_le_twenty (k : ℕ) (hk : 3 ≤ k) (hk' : k ≤ 20) :
    secondMomentKernel k = 0 := by
  rcases le_or_gt k 7 with h7 | h7
  · exact secondMomentKernel_eq_zero_of_le_seven k hk h7
  · interval_cases k <;> decide

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

/-- **Hook-sum decomposition** (Lean-verified, `λ ⊢ k`, `k ≤ 7`, `decide`):
`Σ_□ h(□) = n_λ + n_{λ'} + |λ|`, splitting the total hook length into the row-content `n_λ`, the
column-content `n_{λ'} = n_λ` of the transpose, and the cell count `|λ|`. This is the algebraic key to
the first-odd-moment **transpose identity** `M₁ = 2·Cov_Planch(n_λ, Σ_□ c(□)²)` (companion probe/audit
`wlambda_covariance_epic_A2_odd_moment_structure`): substituting `Σ_□ h = n_λ + n_{λ'} + |λ|` into
`Cov_Planch(Σ_□ h, Σ_□ c²)`, the `|λ|` term is constant (zero covariance) and transpose-invariance of
Plancherel measure together with the conjugation-symmetry of `contentSq`
(`contentSq_conj_invariant_of_le_six`) equate the `n_λ` and `n_{λ'}` covariances — collapsing the sum
to `2·Cov_Planch(n_λ, Σc²)`. -/
theorem hookSum_eq_nLambda_add_conj_add_card_of_le_seven (k : ℕ) (hk : k ≤ 7) :
    ∀ l ∈ partsOf k, hookSum l = nLambda l + nLambda (conj l) + l.sum := by
  interval_cases k <;> decide

/-- **First-odd-moment transpose identity** (Lean-verified, `k ≤ 5`, `decide`), the `(k!)²`-scaled form
of `M₁ = Cov_Planch(Σ_□ h, Σ_□ h²) = 2·Cov_Planch(n_λ, Σ_□ c²)`:
`scaledCov k (Σh) (Σh²) = 2·scaledCov k n_λ (Σc²)`. This is the odd-`k=1` companion of the *even*-moment
result: unlike the even moments (exact polynomials, positivity proved — `threeM4_pos`, `M6_pos`), `M₁`
is non-polynomial, but the hook-sum decomposition (`hookSum_eq_nLambda_add_conj_add_card_of_le_seven`)
together with Plancherel transpose-invariance collapses it to twice a *content*-spread covariance
`Cov_Planch(n_λ, Σc²)` — the same difficulty class as the open kernel `Cov_Planch(f^λ, Σc²) ≤ 0`. The
identity is verified computationally to `n ≤ 14` (`wlambda_covariance_epic_A2_odd_moment_structure.py`);
this `decide` machine-checks it over the full partition/dimension machinery for `k ≤ 5`. -/
theorem m1_transpose_identity_scaled_of_le_five (k : ℕ) (hk : k ≤ 5) :
    scaledCov k (fun l => (hookSum l : ℤ)) hookSqSum
      = 2 * scaledCov k (fun l => (nLambda l : ℤ)) contentSq := by
  interval_cases k <;> decide

/-- Sum of squared row lengths `Σ_i λ_i²` (a `List ℕ` power sum), cast to `ℤ`. -/
def rowSqSum (l : List ℕ) : ℤ := (l.map (fun x => (x : ℤ) ^ 2)).sum

/-- **Per-partition hook-square / content-square identity** `Σ_□ h(□)² = Σ_□ c(□)² + |λ|²`, verified
for all `λ ⊢ k`, `k ≤ 8` (`decide`). Classical (`Σh² = Σc² + n²`); the exact reason `M₁` can be
written against `contentSq` rather than `hookSqSum`: at fixed `n` the two differ by the `λ`-independent
constant `n²`, so they have the same Plancherel covariance with any statistic. -/
theorem hookSqSum_eq_contentSq_add_sq_card_of_le_eight (k : ℕ) (hk : k ≤ 8) :
    ∀ l ∈ partsOf k, hookSqSum l = contentSq l + (l.sum : ℤ) ^ 2 := by
  interval_cases k <;> decide

/-- **`M₁` as a content-spread covariance and as a row-length covariance** (Lean-verified `k ≤ 5`,
`decide`), the `(k!)²`-scaled chain
`Cov(Σh, Σh²) = Cov(Σh, Σc²) = Cov(Σ_i λ_i², Σc²)`. The first equality is the constant-shift from
`hookSqSum_eq_contentSq_add_sq_card_of_le_eight`; the second is today's antidiagonal reformulation
(`docs/audits/2026-08-21-covariance-kernel-M1-antidiagonal-reformulation.md`): via
`Σ_□ h = n_λ + n_{λ'} + n` and `Σ_i C(λ_i,2) = (Σ_i λ_i² − n)/2`, the first odd moment equals the
covariance of the **squared row lengths** with the **squared contents**. Both `Σ_i λ_i²` and `Σ_□ c²`
are second moments (of parts, of contents); `Σ_i λ_i² ∉` the shifted-symmetric algebra, which is why
`M₁` is non-polynomial. This is verified computationally to `n ≤ 24`
(`wlambda_covariance_epic_M1_antidiagonal_reformulation.py`,
`wlambda_covariance_epic_A2_odd_moment_structure.py`); `decide` machine-checks it for `k ≤ 5`. -/
theorem m1_eq_cov_rowSq_contentSq_of_le_five (k : ℕ) (hk : k ≤ 5) :
    scaledCov k (fun l => (hookSum l : ℤ)) hookSqSum
      = scaledCov k (fun l => (hookSum l : ℤ)) contentSq
    ∧ scaledCov k (fun l => (hookSum l : ℤ)) hookSqSum
      = scaledCov k rowSqSum contentSq := by
  interval_cases k <;> exact ⟨by decide, by decide⟩

set_option maxRecDepth 1000000 in
set_option maxHeartbeats 120000000 in
/-- **`M₁ > 0` — the first odd hook-power moment, Lean-verified base cases `3 ≤ k ≤ 8`** (`decide`).
The `(k!)²`-scaled Plancherel covariance `scaledCov k (Σ□ h) (Σ□ c²) = (k!)²·Cov_Planch(Σ□ h, Σ□ c²)`
(same sign as `M₁`, since `(k!)² > 0`) is **strictly positive** for every `3 ≤ k ≤ 8`. Machine-checked
over the full partition / SYT-dimension / hook / content machinery. (`k = 8` decides in ≈40 s cold;
the `k ≤ 8` range matches `hookSqSum_eq_contentSq_add_sq_card_of_le_eight` above.)

This certifies the **finite base** of the one-sided reduction of the all-`n` conjecture
`M₁(n) > 0 ⟸ (exact `M₁>0` for small `n`) ∧ (κ_n ≥ κ for `n ≥ 13`)` (bean `qou-k5r5`), where
`κ_n = M₁/n^{5/2} → κ = 128/(225π²)` (derived). Unlike the **even** moments (`threeM4_pos`, `M6_pos`,
exact polynomials with manifest-positive factorisations), `M₁` is **non-polynomial**, so its all-`n`
positivity is **open**: the remaining content is the *sign* `κ_n → κ` from above, a **second-order
Plancherel-fluctuation** statement whose asymptotic order is **undetermined** at reachable `n` — the
edge (Tracy–Widom) contributes at relative order `n^{-2/3}` (a valid scaling estimate) and a bulk CLT
correction at `n^{-1/2}`, but the measured effective exponent of `κ_n − κ` is still rising (`≈ 0.25 →
0.36` over `n = 40 … 64`, not converged), so edge vs bulk **cannot be ranked**. Not settled here; see
`docs/audits/2026-08-23-covariance-kernel-M1-correction-bulk-not-edge.md`. Exact `Fraction`
computation independently verifies `M₁ > 0` for all `n ≤ 67`. -/
theorem m1_pos_of_le_eight (k : ℕ) (hk3 : 3 ≤ k) (hk : k ≤ 8) :
    0 < scaledCov k (fun l => (hookSum l : ℤ)) contentSq := by
  interval_cases k <;> decide

/-! ## Even hook-power moment positivity (proved)

The even hook-power moments of the covariance measure,
`M_{2j}(n) = Cov_Planch(Σ_□ h^{2j}, Σ_□ h²) = Σ_v v^{2j} ν_v`, are exact polynomials in `n` (both
weights shifted-symmetric; Ivanov–Olshanski, `math/0304010`). Derived exactly (Lagrange
interpolation over exact `Fraction` values, cross-verified) and factored to a manifestly-positive
form in `computations/deltalambda/wlambda_covariance_epic_A2_even_moment_positivity_proved.py`:

    M_2(n) = n(n-1)(n-2)/3                 (= |C₃|; cofactor 1)
    M_4(n) = n(n-1)(n-2)/3 · 5(3n-8)       [exact poly  5n⁴ − 85/3·n³ + 50n² − 80/3·n]
    M_6(n) = 7·n(n-1)(n-2)·(3n-8)²         [exact poly  63n⁵ − 525n⁴ + 1582n³ − 2016n² + 896n]

The cofactors relative to `|C₃| = n(n-1)(n-2)/3` are `1`, `5(3n-8)`, `21(3n-8)²`. (The `5(3n-8)` /
`21(3n-8)²` forms are the exact ones checked by the probe's `cert_ok`; an earlier prose label
`5(n-8/3)` / `7(3n-8)²` was off by a factor of 3 — positivity is unaffected.) We formalize
`M_4, M_6 > 0` for `n ≥ 3` directly from the factored forms. `M_4` carries a `/3`, so we state
`3·M_4` as an integer polynomial; `M_6` is already integer-coefficient. -/

/-- `3·M₄(n) = 5·n(n−1)(n−2)·(3n−8)` — the integer form of the fourth even hook-power moment
`M₄(n) = n(n−1)(n−2)/3 · 5(3n−8)` (so `M₄(n) = threeM4 n / 3`). -/
def threeM4 (n : ℤ) : ℤ := 5 * (n * (n - 1) * (n - 2)) * (3 * n - 8)

/-- `M₆(n) = 7·n(n−1)(n−2)·(3n−8)²` — the sixth even hook-power moment (already integer-coefficient;
exact polynomial `[0, 896, −2016, 1582, −525, 63]` in `n⁰..n⁵`). -/
def M6 (n : ℤ) : ℤ := 7 * (n * (n - 1) * (n - 2)) * (3 * n - 8) ^ 2

/-- **`M₄(n) > 0` for `n ≥ 3`** (stated as `3·M₄ > 0`, whence `M₄ = 3·M₄/3 > 0`): after the positive
`n(n−1)(n−2)` the cofactor `5(3n−8)` is positive past its root `8/3 < 3`. Manifest linear-past-root
certificate for the fourth even hook-power moment. -/
theorem threeM4_pos (n : ℤ) (hn : 3 ≤ n) : 0 < threeM4 n := by
  unfold threeM4
  have h1 : (0 : ℤ) < n := by omega
  have h2 : (0 : ℤ) < n - 1 := by omega
  have h3 : (0 : ℤ) < n - 2 := by omega
  have h4 : (0 : ℤ) < 3 * n - 8 := by omega
  have h5 : (0 : ℤ) < (5 : ℤ) := by omega
  exact mul_pos (mul_pos h5 (mul_pos (mul_pos h1 h2) h3)) h4

/-- **`M₆(n) > 0` for `n ≥ 3`**: `(3n−8)²` is a perfect square, positive since `3n−8 ≥ 1 > 0`, and
`n(n−1)(n−2) > 0`. Manifest perfect-square certificate for the sixth even hook-power moment. Together
with `threeM4_pos` this is the first proved positivity in the covariance-kernel epic (`qou-x631`)
beyond the `k ≤ 7` `decide` instances. It settles the EVEN half of the moment skeleton; the odd-`k`
moments are non-polynomial and remain empirical, and this does **not** prove A2 (whose weight `ln` is
concave — a global argument is still required). -/
theorem M6_pos (n : ℤ) (hn : 3 ≤ n) : 0 < M6 n := by
  unfold M6
  have h1 : (0 : ℤ) < n := by omega
  have h2 : (0 : ℤ) < n - 1 := by omega
  have h3 : (0 : ℤ) < n - 2 := by omega
  have h4 : (0 : ℤ) < 3 * n - 8 := by omega
  have h7 : (0 : ℤ) < (7 : ℤ) := by omega
  exact mul_pos (mul_pos h7 (mul_pos (mul_pos h1 h2) h3)) (pow_pos h4 2)

/-- **CONJECTURE (OPEN).** The covariance kernel `Cov_Planch(f^λ, Σ_□ c(□)²) ≤ 0`, in its
elementary content form: for every `k`, `Σ_{λ⊢k} (f^λ)³ (Σ_□c(□)² − C(k,2)) ≤ 0`. This is the sole
open input of the Δ_λ super-exponential growth bound (`WstdSuperExpBound.lean`, via the reduction
`DeltaLambdaDReduction.D_of_T3_nonpos`). It is a Biane–Śniady / Kerov-CLT character-ratio
anti-correlation; verified `k ≤ 30` computationally. Not proved.
-- Ref: [manuscript] docs/audits/2026-07-18-deltalambda-covariance-kernel-frontier.md -/
theorem covariance_kernel_conjecture (k : ℕ) : kernelValue k ≤ 0 := by
  sorry

/-- **The conjecture holds on `k ≤ 8`** — proved in Lean, not sampled.

    `kernelValue` is fully computable (a sum over `partsOf k`), so every
    instance decides. Kernel evaluation only, **no `native_decide`**. This
    upgrades part of the "verified `k ≤ 30` computationally" above from an
    external Python check to a machine-checked statement.

    Evaluated further out: `k = 0,1,2` give `0`, and the value is strictly
    negative from `k = 3` —
    `-4, -16, -320, -10400, -163520, -3224704, -106339296, -4722309120`
    at `k = 3…10`. So the §9 small-instance check finds nothing here: this is a
    **genuine open conjecture**, and the only survivor of the sweep in bean
    `qou-octr`, where eight sibling `sorry`s all turned out to be refutable.

    The general case is real mathematics: `Σ_{λ⊢k} (f^λ)³ · ω₃(λ) ≤ 0` carries
    a *cubed* dimension, so it is not the Plancherel expectation of `ω₃` and
    the standard `E_Planch[ω₃] = 0` identity does not reach it. -/
theorem covariance_kernel_le_zero_of_le_eight (k : ℕ) (hk : k ≤ 8) :
    kernelValue k ≤ 0 := by
  interval_cases k <;> decide

end QOU.BraidsAndKnots.YoungDiagramKernel
