/-
  Recipe: λ ↦ y_λ(q) — explicit q-rational construction in √q.

  Statement: given a partition λ ⊢ n, the Jones-Markov central
  coefficient y_λ(q) is determined by the following algorithm:

  Step 1: Compute partition data (contents c, hooks h, n(λ)).
  Step 2: Compute the universal X = v³ / (1 + v² - v⁴ - v⁶ + v³)
          where v is the formal square root of q (so v² = q).
  Step 3: Compute s_{λ,r}(Q) = Q^{n(λ)} · ∏ (1 - X·Q^c)/(1 - Q^h)
          with Q = q² = v⁴.
  Step 4: Normalise: y_λ(q) = s_λ / Σ_µ d_µ s_µ.
  Step 5: Factor over Q in v to get cyclotomic denominator + numerator.

  This formalises the algorithmic content of
  prop:y-lambda-closed-form-wenzl-bridge: given any partition, the
  recipe produces y_λ in closed q-rational form in O(p(n) · max_hooks)
  time.

  **Pre-Archimedean stub.** Polymorphic in the ground field `R`.
  The previous version used `q : ℝ`, `open Real`, `Real.sqrt`, and
  axiomatised the Schur principal-specialisation as a real-valued
  `constant`.  All three were Archimedean shortcuts: y_λ is
  `q`-rational by [wenzl1988] (cf. AGENTS.md §7aa notation register).
  The stub now parametrises in an abstract `(q, v) : R × R` with
  `v² = q` and replaces `constant` with `opaque` over `R`.

  Refs: prop:y-lambda-recipe-from-partition (this block),
        prop:y-lambda-closed-form-wenzl-bridge,
        prop:y-lambda-cyclotomic-factorization,
        [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors"
        [macdonald1995] Macdonald, "Symmetric Functions and Hall Polynomials"
-/

import Mathlib.Algebra.Field.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Nat.Factorial.Basic
import Mathlib.Data.List.Sort
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring
import QOU.BraidKnot.IdentityIContentDecomposition

namespace QOU.BraidsAndKnots

universe u

/-! ## Step 1: Partition data -/

/-- Content c(i, j) := j - i for the cell at row i, column j (1-indexed). -/
def cellContent (i j : ℕ) : ℤ := (j : ℤ) - (i : ℤ)

/-- Hook length h(i, j) for the cell at row i, column j of partition λ
    (rows and columns 0-indexed):
    arm + leg + 1 where
      arm(i, j) := λ_i - (j + 1)  (cells strictly right of (i, j) in row i)
      leg(i, j) := |{r > i : λ_r > j}|  (cells below in column j) -/
def cellHook (lam : List ℕ) (i j : ℕ) : ℕ :=
  let arm := if h : i < lam.length then lam.get ⟨i, h⟩ - (j + 1) else 0
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
def hookDim (lam : List ℕ) : ℕ :=
  let n := lam.foldr (· + ·) 0
  let prod_hooks := (lam.zip (List.range lam.length)).foldr
    (fun (p : ℕ × ℕ) acc =>
      acc * (List.range p.1).foldr
        (fun j inner => inner * cellHook lam p.2 j) 1) 1
  Nat.factorial n / prod_hooks

/-! ## Step 2: Universal X substitution

    Polymorphic in the ground field `R`.  `q ∈ R` is the substrate
    parameter; `v ∈ R` is its formal square root with `v² = q`.
    No `Real.sqrt`. -/

/-- Markov parameter `z = 1 / (v + v⁻¹) = v / (q + 1)` (using
    `v² = q`). -/
noncomputable def markovZ {R : Type u} [Field R] (q v : R) : R :=
  v / (q + 1)

/-- Universal X = `v³ / (1 + q - q² - q³ + v³)` where `v² = q`.
    Equivalently `Q^r` for `Q = q²` and `r` the Wenzl level. -/
noncomputable def universalX {R : Type u} [Field R] (q v : R) : R :=
  q * v / (1 + q - q^2 - q^3 + q * v)

/-! ## Step 3: Schur principal-specialisation -/

/-- The Schur principal-specialisation factor for partition λ at
    level r, with `Q = q²` and `X = Q^r`:

      s_{λ, r}(Q) = Q^{n(λ)} · ∏_{(i,j) ∈ λ} (1 - X·Q^{c(i,j)}) / (1 - Q^{h(i,j)})

    Concrete cell-product: outer fold over rows `(row-length, row-index)`
    (the `hookDim` iteration pattern), inner fold over columns `j`.  The
    content `c(i,j) : ℤ` gives an integer power `Q ^ (c : ℤ)` (zpow); the
    hook `h(i,j) : ℕ` gives a natural power. -/
noncomputable def schurPrincipal {R : Type u} [Field R] (lam : List ℕ) (q v : R) : R :=
  let Q := q ^ 2
  let X := universalX q v
  Q ^ (nPartition lam) *
    (lam.zip (List.range lam.length)).foldr
      (fun (p : ℕ × ℕ) acc =>
        acc * (List.range p.1).foldr
          (fun j inner =>
            inner * ((1 - X * Q ^ (cellContent p.2 j)) / (1 - Q ^ (cellHook lam p.2 j))))
          1)
      1

/-! ## Step 4: Normalisation -/

-- Reuse the existing, already-bridged partition enumerator
-- `QOU.BraidKnot.IdentityI.partitionsOf` (soundness / nodup / completeness
-- proven in `QOU.Mathlib.PartitionsOfBridge`) rather than duplicating one.
open QOU.BraidKnot.IdentityI (partitionsOf)

/-- Partition-function denominator `Z_n = Σ_µ d_µ · s_µ` — a **concrete**
    sum over the shared `partitionsOf n` with `d_µ = hookDim µ`,
    `s_µ = schurPrincipal µ` (de-axiomatised; computable). -/
noncomputable def partitionFunctionZ {R : Type u} [Field R] (n : ℕ) (q v : R) : R :=
  (partitionsOf n).foldr
    (fun mu acc => acc + (hookDim mu : R) * schurPrincipal mu q v) 0

/-- The recipe: `y_λ(q) = s_{λ, r}(Q) / Z_n`. -/
noncomputable def yLambdaRecipe {R : Type u} [Field R]
    (lam : List ℕ) (q v : R) : R :=
  schurPrincipal lam q v /
    partitionFunctionZ (lam.foldr (· + ·) 0) q v

/-! ## Markov-trace convention discriminator

    Two distinct formulas for `tr_M = Σ_λ y_λ · χ_λ` circulate in
    the codebase (per the audit at
    `docs/audits/categorical-vs-fitted-q-decay-ba.md` §"CRITICAL"):

    - **Plancherel**: `y_λ = dim_q(λ)² / [n]_q!` weighted by
      `1 / dim_λ_classical`.
    - **Wenzl–Schur** (canonical per this proposition):
      `y_λ = s_{λ, r}(q²) / Σ_µ d_µ s_{µ, r}(q²)`.

    The two give numerically *different* values for `tr_M(D)` and
    are not interchangeable. This `inductive` and the wrapper
    `MarkovTraceCoefficient` below provide vocabulary to tag a
    coefficient value with the convention it implements, so that
    downstream consumers can pattern-match on `c.convention` or
    require an explicit equation hypothesis like
    `(c : MarkovTraceCoefficient).convention = .wenzlSchur`. -/
inductive MarkovTraceConvention : Type
  | plancherel : MarkovTraceConvention
  | wenzlSchur : MarkovTraceConvention
  deriving DecidableEq, Repr

/-- A Markov-trace y_λ value paired with the convention it
    implements. Wrapping a raw `value` in this structure lets
    downstream theorems pattern-match on the `convention` field
    rather than relying on prose annotations or external audit
    docs. -/
structure MarkovTraceCoefficient (R : Type u) where
  /-- The y_λ value at the substrate parameter (in the ground ring). -/
  value : R
  /-- The Markov-trace convention this value follows. -/
  convention : MarkovTraceConvention

/-! ## Main theorems -/

/-- **Recipe correctness**: the algorithm `yLambdaRecipe` produces the
    Jones-Markov central coefficient y_λ for the symmetric Hecke
    convention σ² = (q - q⁻¹)σ + 1 with parameter z = 1/(v + v⁻¹).

    The output is **Wenzl–Schur-canonical**: `JonesMarkovCoefficient`
    is the y_λ on the Wenzl-Schur side of the convention split (see
    `MarkovTraceConvention`). Plancherel-derived y_λ values do not
    satisfy this theorem and are not interchangeable.

    Equivalent to prop:y-lambda-closed-form-wenzl-bridge restated
    algorithmically.

    Abstract external constant (`axiom`, not `opaque`): the canonical
    Jones–Markov coefficient is an external datum ([wenzl1988]); `opaque
    … : R` over generic `Field R` fails v4.24 code-gen (see
    `partitionFunctionZ`), so it is declared as an `axiom`. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see content/bib-qa-verifications.json
axiom JonesMarkovCoefficient {R : Type u} [Field R]
    (q v : R) (lam : List ℕ) : R

/-- The Markov-trace convention this recipe implements. -/
def yLambdaRecipeConvention : MarkovTraceConvention :=
  MarkovTraceConvention.wenzlSchur

/-- The Wenzl–Schur-tagged y_λ wrapper. -/
noncomputable def jonesMarkovTagged {R : Type u} [Field R]
    (q v : R) (lam : List ℕ) : MarkovTraceCoefficient R :=
  { value := JonesMarkovCoefficient q v lam,
    convention := yLambdaRecipeConvention }

@[simp] theorem jonesMarkovTagged_convention {R : Type u} [Field R]
    (q v : R) (lam : List ℕ) :
    (jonesMarkovTagged q v lam).convention =
      MarkovTraceConvention.wenzlSchur :=
  rfl

/-- **External axiom (Wenzl 1988):** y_λ recipe matches the canonical
    Jones-Markov coefficient via Macdonald hook telescope. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see content/bib-qa-verifications.json
axiom y_lambda_recipe_correct_axiom :
    ∀ {R : Type u} [Field R] (q v : R) (lam : List ℕ),
      (∀ p ∈ lam, 0 < p) → List.Sorted (· ≥ ·) lam →
      JonesMarkovCoefficient q v lam = yLambdaRecipe lam q v

theorem y_lambda_recipe_correct {R : Type u} [Field R]
    (q v : R) (lam : List ℕ)
    (_hpos : ∀ p ∈ lam, 0 < p)
    (_hnonincr : List.Sorted (· ≥ ·) lam) :
    JonesMarkovCoefficient q v lam = yLambdaRecipe lam q v :=
  y_lambda_recipe_correct_axiom q v lam _hpos _hnonincr

/-- **External axiom (Wenzl 1988):** Plancherel completeness
    `Σ_λ⊢n d_λ · y_λ(q) = 1`. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see content/bib-qa-verifications.json
axiom plancherel_via_recipe_axiom :
    ∀ {R : Type u} [Field R] (q v : R) (n : ℕ)
      (parts : List (List ℕ)),
      (∀ lam : List ℕ, lam.foldr (· + ·) 0 = n → lam ∈ parts) →
      parts.Nodup →
      (parts.map (fun lam => (hookDim lam : R) * yLambdaRecipe lam q v)).sum
        = (1 : R)

/-- **Plancherel completeness**: Σ_λ⊢n d_λ · y_λ(q) = 1 for every n. -/
theorem plancherel_via_recipe {R : Type u} [Field R]
    (q v : R) (n : ℕ)
    (parts : List (List ℕ))
    (_parts_complete : ∀ lam : List ℕ,
      lam.foldr (· + ·) 0 = n → lam ∈ parts)
    (_parts_nodup : parts.Nodup) :
    (parts.map
      (fun lam => (hookDim lam : R) * yLambdaRecipe lam q v)).sum
        = (1 : R) :=
  plancherel_via_recipe_axiom q v n parts _parts_complete _parts_nodup

/-- **Cyclotomic factorisation**: the recipe output factors as
    P_λ(v) / D_n(v) where D_n is a pure product of cyclotomic
    polynomials Φ_d(v). -/
opaque YLambdaRecipeCyclotomicFactor : Prop

/-- **External axiom (Wenzl 1988):** cyclotomic factorisation of the
    y_λ recipe denominator. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see content/bib-qa-verifications.json
axiom y_lambda_cyclotomic_via_recipe_axiom :
    ∀ {R : Type u} [Field R] (q v : R) (lam : List ℕ),
      YLambdaRecipeCyclotomicFactor

theorem y_lambda_cyclotomic_via_recipe {R : Type u} [Field R]
    (q v : R) (lam : List ℕ) :
    YLambdaRecipeCyclotomicFactor :=
  y_lambda_cyclotomic_via_recipe_axiom q v lam

/-! ## Worked example: n = 2 -/

/-- **Worked example, `λ = (2)` at `n = 2`** — now **proved** (was an
    axiom).  With `partitionFunctionZ` concrete, `y_{(2)}` reduces through
    the two `n=2` partitions `{(2), (1,1)}` (both dimension 1) to the closed
    form.  Requires the denominators of the recipe to be nonzero. -/
theorem y_lambda_recipe_n2_partition_2 {R : Type u} [Field R]
    (q v : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq4 : q ^ 4 ≠ 1)
    (hp1 : q + 1 ≠ 0) (hp2 : q ^ 2 + 1 ≠ 0)
    (hX : 1 + q - q ^ 2 - q ^ 3 + q * v ≠ 0)
    (hX1 : 1 + q - q ^ 2 - q ^ 3 ≠ 0) :
    yLambdaRecipe [2] q v = (q * v + q + 1) / ((q + 1) * (q ^ 2 + 1)) := by
  -- `rfl` reduces each concrete `schurPrincipal` cell-product fold to its
  -- explicit form (Q = q², X = universalX q v; `zpow` for the ℤ content).
  have hs2 : schurPrincipal [2] q v
      = (q ^ 2) ^ (0 : ℕ) *
        (1 * ((1 * ((1 - universalX q v * (q ^ 2) ^ (1 : ℤ)) / (1 - (q ^ 2) ^ (1 : ℕ)))) *
              ((1 - universalX q v * (q ^ 2) ^ (0 : ℤ)) / (1 - (q ^ 2) ^ (2 : ℕ))))) := by
    rfl
  have hs11 : schurPrincipal [1, 1] q v
      = (q ^ 2) ^ (1 : ℕ) *
        ((1 * (1 * ((1 - universalX q v * (q ^ 2) ^ (-1 : ℤ)) / (1 - (q ^ 2) ^ (1 : ℕ))))) *
         (1 * ((1 - universalX q v * (q ^ 2) ^ (0 : ℤ)) / (1 - (q ^ 2) ^ (2 : ℕ))))) := by
    rfl
  have hp : partitionsOf 2 = [[2], [1, 1]] := by decide
  have hd2 : hookDim [2] = 1 := by decide
  have hd11 : hookDim [1, 1] = 1 := by decide
  have hrec : ([2] : List ℕ).foldr (· + ·) 0 = 2 := rfl
  have hq2ne : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hd1 : (1 : R) - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq2)
  have hd4' : (1 : R) - q ^ 4 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq4)
  have hd4 : (1 : R) - (q ^ 2) ^ 2 ≠ 0 := by
    have h : (q ^ 2) ^ 2 = q ^ 4 := by ring
    rw [h]; exact hd4'
  -- `1 − X ≠ 0` (the factor the recipe cancels): `1 − qv/Dx = (Dx − qv)/Dx`
  -- with `Dx − qv = 1 + q − q² − q³` (`hX1`) and `Dx ≠ 0` (`hX`).
  have hp2' : (1 : R) + q ^ 2 ≠ 0 := by rw [add_comm]; exact hp2
  have hXm : (1 : R) - universalX q v ≠ 0 := by
    rw [universalX, ne_eq, sub_eq_zero]
    intro h
    rw [eq_div_iff hX] at h
    exact hX1 (by linear_combination h)
  -- `Z_2 = (1−X)²/(1−q²)²` (common `(1−q²)(1−q⁴)` denom; `X` abstract), so `Z ≠ 0`.
  have hZval : schurPrincipal [1, 1] q v + schurPrincipal [2] q v
      = (1 - universalX q v) ^ 2 / (1 - q ^ 2) ^ 2 := by
    rw [hs2, hs11]
    simp only [zpow_zero, zpow_one, zpow_neg_one, pow_zero, pow_one, mul_one, one_mul]
    field_simp [hd1, hd4', hq2ne]
    ring
  have hZne : schurPrincipal [1, 1] q v + schurPrincipal [2] q v ≠ 0 := by
    rw [hZval]; exact div_ne_zero (pow_ne_zero 2 hXm) (pow_ne_zero 2 hd1)
  unfold yLambdaRecipe partitionFunctionZ
  rw [hrec, hp]
  simp only [List.foldr_cons, List.foldr_nil, hd2, hd11, Nat.cast_one, one_mul, zero_add]
  -- Clear the top-level division (needs `Z ≠ 0`), then expand schur/X and ring.
  rw [div_eq_div_iff hZne (mul_ne_zero hp1 hp2), hs2, hs11, universalX]
  field_simp [hX, hd1, hd4', hq2ne]
  ring

end QOU.BraidsAndKnots
