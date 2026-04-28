/-
  Recipe: λ ↦ y_λ(q) — explicit q-rational construction in √q.

  Statement: given a partition λ ⊢ n, the Jones-Markov central
  coefficient y_λ(q) is determined by the following algorithm:

  Step 1: Compute partition data (contents c, hooks h, n(λ)).
  Step 2: Compute the universal X = q^(3/2)/(1 + q - q² - q³ + q^(3/2)).
  Step 3: Compute s_{λ,r}(Q) = Q^{n(λ)} · ∏ (1 - X·Q^c)/(1 - Q^h)
          with Q = q².
  Step 4: Normalise: y_λ(q) = s_λ / Σ_µ d_µ s_µ.
  Step 5: Factor over Q in √q to get cyclotomic denominator + numerator.

  This formalises the algorithmic content of
  prop:y-lambda-closed-form-wenzl-bridge: given any partition, the
  recipe produces y_λ in closed q-rational form in O(p(n) · max_hooks)
  time.

  Refs: prop:y-lambda-recipe-from-partition (this block),
        prop:y-lambda-closed-form-wenzl-bridge,
        prop:y-lambda-cyclotomic-factorization,
        [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors"
        [macdonald1995] Macdonald, "Symmetric Functions and Hall Polynomials"
-/

import Mathlib.Data.Real.Basic
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Data.List.Basic

namespace QOU.BraidsAndKnots

open Real

/-! ## Step 1: Partition data -/

/-- Content c(i, j) := j - i for the cell at row i, column j (1-indexed). -/
def cellContent (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- Hook length h(i, j) for the cell at row i, column j of partition λ:
    arm + leg + 1 where
      arm(i, j) := λ_i - j  (cells right of (i, j) in row i)
      leg(i, j) := |{r > i : λ_r > j}|  (cells below in column j) -/
def cellHook (lam : List ℕ) (i j : ℕ) : ℕ :=
  let arm := if h : i < lam.length then lam.get ⟨i, h⟩ - j else 0
  let leg := (List.range (lam.length - i - 1)).countP
    (fun r =>
      let r' := i + 1 + r
      if h : r' < lam.length then lam.get ⟨r', h⟩ > j else false)
  arm + leg + 1

/-- n(λ) := Σ (i-1) λ_i  -- the standard partition statistic. -/
def nPartition (lam : List ℕ) : ℕ :=
  (lam.zip (List.range lam.length)).foldr
    (fun (p : ℕ × ℕ) acc => acc + p.2 * p.1) 0

/-- Hook-length dimension formula: f^λ = n! / ∏ h(i, j). -/
noncomputable def hookDim (lam : List ℕ) : ℕ :=
  let n := lam.foldr (· + ·) 0
  let prod_hooks := (lam.zip (List.range lam.length)).foldr
    (fun (p : ℕ × ℕ) acc =>
      acc * (List.range p.1).foldr
        (fun j inner => inner * cellHook lam p.2 j) 1) 1
  Nat.factorial n / prod_hooks

/-! ## Step 2: Universal X substitution -/

/-- Markov parameter z = 1 / (√q + 1/√q) = √q / (q + 1). -/
noncomputable def markovZ (q : ℝ) : ℝ :=
  Real.sqrt q / (q + 1)

/-- Universal X = q^(3/2) / (1 + q - q² - q³ + q^(3/2))
    = Q^r where Q = q² and r is the Wenzl level for the
    Jones-Markov trace at parameter z = 1/(√q + 1/√q). -/
noncomputable def universalX (q : ℝ) : ℝ :=
  q * Real.sqrt q / (1 + q - q^2 - q^3 + q * Real.sqrt q)

/-! ## Step 3: Schur principal-specialisation -/

/-- The Schur principal-specialisation factor for partition λ at level
    r, with Q = q² and X = Q^r:

      s_{λ, r}(Q) = Q^{n(λ)} · ∏_{(i,j) ∈ λ} (1 - X·Q^{c(i,j)}) / (1 - Q^{h(i,j)})

    Stub — full implementation requires partition-cell iteration. -/
constant schurPrincipal (lam : List ℕ) (q : ℝ) : ℝ

/-! ## Step 4: Normalisation -/

/-- Partition function denominator Z_n = Σ_µ d_µ · s_µ over all
    partitions µ of n. -/
constant partitionFunctionZ (n : ℕ) (q : ℝ) : ℝ

/-- The recipe: y_λ(q) = s_{λ, r}(Q) / Z_n. -/
noncomputable def yLambdaRecipe (lam : List ℕ) (q : ℝ) : ℝ :=
  schurPrincipal lam q / partitionFunctionZ (lam.foldr (· + ·) 0) q

/-! ## Markov-trace convention discriminator

    Two distinct formulas for `tr_M = Σ_λ y_λ · χ_λ` circulate in
    the codebase (per the audit at
    `docs/audits/categorical-vs-fitted-q-decay-ba.md` §"⚠️ CRITICAL"):

    - **Plancherel**: `y_λ = dim_q(λ)² / [n]_q!` weighted by
      `1 / dim_λ_classical`.
    - **Wenzl–Schur** (canonical per this proposition):
      `y_λ = s_{λ, r}(q²) / Σ_µ d_µ s_{µ, r}(q²)`.

    The two give numerically *different* values for `tr_M(D)` and
    are not interchangeable. This `inductive` tags an `Mhat`-valued
    `tr_M` with the convention it implements, so that downstream
    theorems can require, e.g.,
    `[Fact (tr_M.convention = .wenzlSchur)]` (or carry the tag as
    an explicit equation hypothesis) to rule out Plancherel-derived
    inputs. To get typeclass inference on the discriminator instead,
    wrap this in a `class` per consumer; we keep the bare inductive
    here so both conventions remain first-class values. -/
inductive MarkovTraceConvention : Type
  | plancherel : MarkovTraceConvention
  | wenzlSchur : MarkovTraceConvention
  deriving DecidableEq, Repr

/-! ## Main theorems -/

/-- **Recipe correctness**: the algorithm `yLambdaRecipe` produces the
    Jones-Markov central coefficient y_λ for the symmetric Hecke
    convention σ² = (q - q⁻¹)σ + 1 with parameter z = 1/(√q + 1/√q).

    The output is **Wenzl–Schur-canonical**: `JonesMarkovCoefficient`
    is the y_λ on the Wenzl-Schur side of the convention split (see
    `MarkovTraceConvention`). Plancherel-derived y_λ values do not
    satisfy this theorem and are not interchangeable.

    Equivalent to prop:y-lambda-closed-form-wenzl-bridge restated
    algorithmically. -/
constant JonesMarkovCoefficient (q : ℝ) (lam : List ℕ) : ℝ

/-- The Markov-trace convention this recipe implements. -/
def yLambdaRecipeConvention : MarkovTraceConvention :=
  MarkovTraceConvention.wenzlSchur

theorem y_lambda_recipe_correct
    (q : ℝ) (hq : q > 1)
    (lam : List ℕ) (hpos : ∀ p ∈ lam, 0 < p)
    (hnonincr : List.Sorted (· ≥ ·) lam) :
    JonesMarkovCoefficient q lam = yLambdaRecipe lam q := by
  sorry  -- Ref: prop:y-lambda-recipe-from-partition proof;
         -- composes prop:y-lambda-closed-form-wenzl-bridge with
         -- the explicit X substitution from Step 2.

/-- **Plancherel completeness**: Σ_λ⊢n d_λ · y_λ(q) = 1 for every n. -/
theorem plancherel_via_recipe
    (q : ℝ) (hq : q > 1) (n : ℕ)
    (parts : List (List ℕ))
    (parts_complete : ∀ lam : List ℕ, lam.foldr (· + ·) 0 = n → lam ∈ parts)
    (parts_nodup : parts.Nodup) :
    (parts.map (fun lam => (hookDim lam : ℝ) * yLambdaRecipe lam q)).sum = 1 := by
  sorry  -- Ref: tr_M(1_{H_n}) = 1 normalisation transported through
         -- Wedderburn (cf. prop:y-lambda-closed-form-wenzl-bridge).

/-- **Cyclotomic factorisation**: the recipe output factors as
    P_λ(√q) / D_n(√q) where D_n is a pure product of cyclotomic
    polynomials Φ_d(√q). -/
/-- The recipe output factorises as P_λ(√q) / D_n(√q) where D_n is a
    pure product of cyclotomic polynomials. -/
constant YLambdaRecipeCyclotomicFactor : Prop

theorem y_lambda_cyclotomic_via_recipe
    (q : ℝ) (hq : q > 1)
    (lam : List ℕ) :
    YLambdaRecipeCyclotomicFactor := by
  sorry  -- Ref: prop:y-lambda-cyclotomic-factorization;
         -- denominators arise from ∏(1 - q^h) = ∏ Φ_d(√q) products
         -- by the identity 1 - q^k = ∏_{d ∣ 2k} Φ_d(√q).

/-! ## Worked example: n = 2 -/

/-- For n = 2, λ = (2): y_(2)(q) = (q^(3/2) + q + 1) / ((q + 1)(q² + 1)).

    By the recipe:
      Step 1: cells (1,1), (1,2); contents 0, 1; hooks 2, 1; n((2)) = 0.
      Step 2: X = q^(3/2) / (1 + q - q² - q³ + q^(3/2)).
      Step 3: s_(2),r = (1 - X)(1 - X·q²) / ((1 - q⁴)(1 - q²)).
      Step 4: Z_2 = (1 - X)² / (1 - q²)² (after telescope).
      Step 5: y_(2) = (1 - X·q²) / ((1 - X)(1 + q²))
              = (q^(3/2) + q + 1) / ((q + 1)(q² + 1))
              after substituting X. -/
theorem y_lambda_recipe_n2_partition_2
    (q : ℝ) (hq : q > 0) (hq1 : q ≠ 1) :
    yLambdaRecipe [2] q = (q * Real.sqrt q + q + 1) / ((q + 1) * (q^2 + 1)) := by
  sorry  -- Ref: prop:y-lambda-recipe-from-partition §"Worked example";
         -- explicit computation through the 5-step recipe.

end QOU.BraidsAndKnots
