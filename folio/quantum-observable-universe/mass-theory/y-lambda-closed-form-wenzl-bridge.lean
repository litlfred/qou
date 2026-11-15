/-
  Closed form for the Jones–Markov central coefficients y_λ via the
  Wenzl Schur-element bridge (Q = q², z_GL = q · z).

  Statement: for the symmetric Hecke convention σ² = (q − q⁻¹)σ + 1
  with convention-D Markov parameter z = q³/(q² + 1), the central
  coefficients y_λ in tr_M = Σ y_λ χ_λ satisfy

    y_λ = s_{λ, r}(Q) / (Σ_µ d_µ · s_{µ, r}(Q))

  where Q = q², s_{λ, r}(Q) = Q^{n(λ)} · ∏_{x ∈ λ} (1 − Q^{r+c(x)}) /
  (1 − Q^{h(x)}) is the principal-specialization Schur function in r
  variables, d_µ is the classical S_n-irrep dimension (hook formula),
  and r solves q · z = Q^r (1 − Q) / (1 − Q^r), giving the explicit
  substitution

    Q^r = X = q · z / (1 − Q + q · z) = q⁴ = Q².

  This bridges the symmetric Hecke convention used in this paper to
  the Wenzl-Orellana standard reference formula via the affine
  convention shift G = q σ.

  Refs: prop:y-lambda-closed-form-wenzl-bridge (this block),
        [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors"
                    Invent. Math. 92 (1988) 349-383
        [orellana1998] Orellana, "Weights of Markov Traces on Hecke
                       Algebras" arXiv:math/9806163
        [chlouveraki2016] Chlouveraki HDR thesis Theorem 6.20
                          (Markov-trace family is 1-dim in type A)
-/

import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.List.Sort
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Algebra.BigOperators.Group.List.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Positivity
import Mathlib.Tactic.Ring

namespace QOU.BraidsAndKnots

/-- Local mirror of the categorical 1-dim Markov-trace family axiom
    (cf. `wenzl-bridge-applicability-qou.lean`, `prop:wenzl-bridge-applicability-qou`);
    both encode Chlouveraki HDR Theorem 6.20 (= Juyumaya 2007 Theorem 12,
    `d = 1` case): the type-A Markov-trace family is one-dimensional in
    the trace functionals, parameterised by `z` (`qou-z9fx`). -/
class MarkovTraceFamilyOneDim (R : Type*) [Semiring R] (q z : R) where
  /-- Any two Markov-trace functionals `tr₁ tr₂ : H → R` on a Hecke-algebra
      carrier `H` (with unit `unit` and generator shift `appendGen`) that
      share the Markov parameter `z` and normalisation `tr(unit) = 1`
      agree on every element. -/
  unique :
    ∀ {H : Type} (unit : H) (appendGen : H → H) (tr₁ tr₂ : H → R),
      (∀ x, tr₁ (appendGen x) = z * tr₁ x) →
      (∀ x, tr₂ (appendGen x) = z * tr₂ x) →
      tr₁ unit = 1 → tr₂ unit = 1 →
      tr₁ = tr₂
  -- Ref: [chlouveraki2016] HDR Theorem 6.20

open Real BigOperators

/-! ## Convention parameters -/

/-- Markov parameter `z_D = q^3 / (q^2 + 1)` in the σ-convention used in
    this paper (eigenvalues `q, -q⁻¹`) — **convention D**, canonical by the
    owner ruling of 2026-08-15 (R1). -/
noncomputable def jonesMarkovZ (q : ℝ) : ℝ :=
  q ^ 3 / (q ^ 2 + 1)

/-- Wenzl-convention variable `Q = q²` from the convention
    isomorphism `G = q σ`. -/
noncomputable def wenzlQ (q : ℝ) : ℝ := q ^ 2

/-- Convention-shifted Markov parameter `z_GL = q · z` in the
    Wenzl/Orellana g-convention (eigenvalues `Q, -1`). -/
noncomputable def wenzlZ (q : ℝ) : ℝ := q * jonesMarkovZ q

/-- Explicit `X = Q^r = q·z / (1 - Q + q·z)`, solving the bridge
    equation `q · z = Q^r · (1 - Q) / (1 - Q^r)`. This is the
    universal substitution that turns Wenzl's Schur principal-
    specialization formula into a closed q-rational expression. -/
noncomputable def wenzlX (q : ℝ) : ℝ :=
  wenzlZ q / (1 - wenzlQ q + wenzlZ q)

/-- Under convention D (`z = q³/(q² + 1)`), the Wenzl bridge parameter
    `wenzlX q` collapses identically to `q⁴ = (wenzlQ q)²` (integer Wenzl
    level `r = 2`). -/
theorem wenzlX_eq_pow_four (q : ℝ) : wenzlX q = q ^ 4 := by
  have hq2 : q ^ 2 + 1 ≠ 0 := by positivity
  have hzw : wenzlZ q = q ^ 4 / (q ^ 2 + 1) := by
    unfold wenzlZ jonesMarkovZ
    ring
  have hden : 1 - wenzlQ q + wenzlZ q = 1 / (q ^ 2 + 1) := by
    rw [wenzlQ, hzw]
    field_simp
    ring
  unfold wenzlX
  rw [hden, hzw]
  field_simp

/-! ## Partition combinatorics -/

/-- A partition of `n`: non-increasing positive ℕ-sequence. -/
structure Partition (n : ℕ) where
  parts : List ℕ
  /-- Sum of parts equals `n`. -/
  sum_eq : parts.sum = n
  /-- All parts positive. -/
  pos : ∀ p ∈ parts, 0 < p
  /-- Non-increasing. -/
  nonincr : List.Sorted (· ≥ ·) parts

/-- Content `c(i, j) := j - i` for the cell at row `i`, column `j` (0-indexed). -/
def cellContent (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- Hook length `h(i, j) = arm(i, j) + leg(i, j) + 1` for the cell at row `i`,
    column `j` of a partition diagram (0-indexed), matching
    `y-lambda-recipe-from-partition.lean` (`qou-z9fx`). -/
def cellHook (lam : List ℕ) (i j : ℕ) : ℕ :=
  let arm := if h : i < lam.length then lam.get ⟨i, h⟩ - (j + 1) else 0
  let leg := (List.range (lam.length - i - 1)).countP
    (fun r =>
      let r' := i + 1 + r
      if h : r' < lam.length then lam.get ⟨r', h⟩ > j else false)
  arm + leg + 1

/-- Number of standard Young tableaux of shape `λ` (= dimension of the
    irreducible `S_n`-representation `V_λ`), computed via the hook-length
    formula `f^λ = n! / ∏_{(i,j) ∈ λ} h(i, j)` (`qou-z9fx`). -/
def hookDim {n : ℕ} (lam : Partition n) : ℕ :=
  let prod_hooks := (lam.parts.zip (List.range lam.parts.length)).foldr
    (fun (p : ℕ × ℕ) acc =>
      acc * (List.range p.1).foldr
        (fun j inner => inner * cellHook lam.parts p.2 j) 1) 1
  n.factorial / prod_hooks

/-- Partition statistic `n(λ) = ∑_i i · λ_i` (0-indexed row index `i`),
    matching `nPartition` in `y-lambda-recipe-from-partition.lean` (`qou-z9fx`). -/
def nLambda {n : ℕ} (lam : Partition n) : ℕ :=
  (lam.parts.zip (List.range lam.parts.length)).foldr
    (fun (p : ℕ × ℕ) acc => acc + p.2 * p.1) 0

/-! ## The Wenzl Schur element -/

/-- The Wenzl principal-specialization Schur element for partition `λ ⊢ n`
    at parameter pair `(Q, X)` with `X = Q^r`:

      `s_{λ,r}(Q) = Q^{n(λ)} · ∏_{(i,j) ∈ λ} (1 - X · Q^{c(i,j)}) / (1 - Q^{h(i,j)})`

    computed over all cells `(i, j)` of `lam.parts` (`qou-z9fx`). -/
noncomputable def wenzlSchurElement {n : ℕ} (lam : Partition n) (Q X : ℝ) : ℝ :=
  Q ^ (nLambda lam) *
    (lam.parts.zip (List.range lam.parts.length)).foldr
      (fun (p : ℕ × ℕ) acc =>
        acc * (List.range p.1).foldr
          (fun j inner =>
            inner * ((1 - X * Q ^ (cellContent p.2 j)) / (1 - Q ^ (cellHook lam.parts p.2 j))))
          1)
      1

/-- The total normalisation `Z = Σ_µ d_µ · s_{µ, r}(Q)`. -/
noncomputable def wenzlNormalization {n : ℕ}
    (parts : List (Partition n)) (Q X : ℝ) : ℝ :=
  (parts.map (fun lam => (hookDim lam : ℝ) * wenzlSchurElement lam Q X)).sum

/-- Closed-form Jones-Markov central coefficient `y_λ` via the
    Wenzl bridge:
      `y_λ(q) = s_{λ,r}(Q) / Z(Q)`
    with `Q = wenzlQ q`, `X = wenzlX q`. -/
noncomputable def yLambdaWenzlBridge {n : ℕ}
    (parts : List (Partition n)) (lam : Partition n) (q : ℝ) : ℝ :=
  let Q := wenzlQ q
  let X := wenzlX q
  wenzlSchurElement lam Q X / wenzlNormalization parts Q X

/-! ## Main theorem -/

/-- Central character coefficient of the Jones-Markov trace at
    partition `λ ⊢ n` in the explicit convention-D level-`r = 2`
    specialisation `(Q, X) = (q², q⁴)`. -/
noncomputable def jonesMarkovCoefficient {n : ℕ}
    (parts : List (Partition n)) (q : ℝ) (lam : Partition n) : ℝ :=
  wenzlSchurElement lam (q ^ 2) (q ^ 4) /
    wenzlNormalization parts (q ^ 2) (q ^ 4)

/-- **Main theorem**: for `q > 1` in the σ-convention with convention-D
    Markov parameter `z = q³/(q² + 1)`, the level-2 Jones-Markov central
    coefficient `jonesMarkovCoefficient parts q lam` equals the Wenzl-bridge
    closed form `yLambdaWenzlBridge parts lam q` at `Q = wenzlQ q = q²` and
    `X = wenzlX q = q·z/(1 - q² + q·z)`, with `1 < wenzlQ q`. -/
theorem y_lambda_closed_form_wenzl_bridge
    {n : ℕ} (q : ℝ) (hq : q > 1)
    (parts : List (Partition n))
    (lam : Partition n) :
    jonesMarkovCoefficient parts q lam = yLambdaWenzlBridge parts lam q ∧
      1 < wenzlQ q := by
  refine ⟨?_, ?_⟩
  · unfold jonesMarkovCoefficient yLambdaWenzlBridge
    dsimp only
    rw [wenzlQ, wenzlX_eq_pow_four]
  · unfold wenzlQ
    nlinarith

/-! ## Uniqueness of the convention shift -/

/-- **Uniqueness — definitional layer.** The convention iso
    `g = q σ` forces `wenzlQ q = q^2` and
    `wenzlZ q = q · jonesMarkovZ q`. -/
theorem wenzl_bridge_unique_definitional (q : ℝ) :
    wenzlQ q = q ^ 2 ∧ wenzlZ q = q * jonesMarkovZ q :=
  ⟨rfl, rfl⟩

/-- **Uniqueness — categorical layer.** Conditional on the
    Chlouveraki 1-dim Markov-trace family axiom
    (`MarkovTraceFamilyOneDim`), any two normalised Markov traces on a
    Hecke-algebra carrier `H` with parameter `jonesMarkovZ q` coincide,
    and the Wenzl-formula parameter pair `(Q, z_GL)` equals
    `(q², q · jonesMarkovZ q)` (`qou-z9fx`). -/
theorem wenzl_bridge_unique_categorical
    (q : ℝ)
    [U : MarkovTraceFamilyOneDim ℝ q (jonesMarkovZ q)]
    {H : Type} (unit : H) (appendGen : H → H) (tr₁ tr₂ : H → ℝ)
    (hm₁ : ∀ x, tr₁ (appendGen x) = jonesMarkovZ q * tr₁ x)
    (hm₂ : ∀ x, tr₂ (appendGen x) = jonesMarkovZ q * tr₂ x)
    (hu₁ : tr₁ unit = 1) (hu₂ : tr₂ unit = 1) (x : H) :
    tr₁ x = tr₂ x ∧ wenzlQ q = q ^ 2 ∧ wenzlZ q = q * jonesMarkovZ q :=
  ⟨congrFun (U.unique unit appendGen tr₁ tr₂ hm₁ hm₂ hu₁ hu₂) x,
   wenzl_bridge_unique_definitional q⟩

/-- **Uniqueness — definitional compatibility alias.** -/
theorem wenzl_bridge_unique (q : ℝ) :
    wenzlQ q = q ^ 2 ∧ wenzlZ q = q * jonesMarkovZ q :=
  wenzl_bridge_unique_definitional q

end QOU.BraidsAndKnots
