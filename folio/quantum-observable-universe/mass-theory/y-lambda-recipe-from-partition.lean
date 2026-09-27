/-
  Recipe: λ ↦ y_λ(q) — explicit q-rational construction over ℚ(q).

  **MIGRATED TO CONVENTION D (2026-08-24).**  The 2026-08-15 owner
  ruling makes convention D (`z = q³/(q²+1)`) canonical and excises
  convention C (`z = √q/(q+1)`).  This file was convention C, and the
  tell was the formal square root: the old universal substitution
  `X = v³/(1 + q − q² − q³ + v³)` inverts, through the Wenzl lattice
  relation `X = z_W/(1 − Q + z_W)` at `Q = q²`, to exactly
  `z_W = q·z_C = q^{3/2}/(q+1)` — the Wenzl-normalised convention-C
  parameter.  Measured, not inferred.

  Under D the same inversion gives `z_W = q·z_D = q⁴/(q²+1)` and hence

      X = q⁴ = Q²,

  an **integer Wenzl level r = 2**, on the nose.  Three consequences,
  all of them simplifications:

  * `v` disappears.  Nothing here needs a square root; the whole recipe
    lives over ℚ(q), not ℚ(√q).  Every signature loses a parameter.
  * Step 4's normaliser is closed-form: `Z_n = [2]_Q^n = (1 + q²)^n`,
    proved at every integer level as
    `QOU.SchurWeyl.sum_dim_schurPrincipal`, so the sum over all `p(n)`
    partitions is no longer needed to evaluate it.
  * `y_λ = 0` for every λ with more than two rows
    (`QOU.SchurWeyl.wenzlWeight_eq_zero_iff`), which the C-frame form
    does not make visible.

  This was NOT a `z`-swap into a C-frame result — the kind of move
  bean `qou-cds1` forbids.  `X` is a *parameter* of the recipe, fixed
  by `z` through the lattice relation, so re-deriving it under D is
  substituting into the derivation, not into its conclusion.

  Statement: given a partition λ ⊢ n, the Jones-Markov central
  coefficient y_λ(q) is determined by the following algorithm:

  Step 1: Compute partition data (contents c, hooks h, n(λ)).
  Step 2: Take the universal X = Q^r with Q = q² and r = 2, i.e.
          X = q⁴.  Equivalently X = z_W/(1 - Q + z_W) for the
          Wenzl-normalised convention-D parameter z_W = q·z_D
          (`universalX_eq_lattice` below proves the equality).
  Step 3: Compute s_{λ,r}(Q) = Q^{n(λ)} · ∏ (1 - X·Q^c)/(1 - Q^h).
  Step 4: Normalise: y_λ(q) = s_λ / Σ_µ d_µ s_µ, and that denominator
          is (1 + q²)^n in closed form.
  Step 5: Factor over ℚ(q) to get cyclotomic denominator + numerator.

  This formalises the algorithmic content of
  prop:y-lambda-closed-form-wenzl-bridge: given any partition, the
  recipe produces y_λ in closed q-rational form in O(p(n) · max_hooks)
  time.

  **Pre-Archimedean stub.** Polymorphic in the ground field `R`.
  An early version used `q : ℝ`, `open Real` and `Real.sqrt`; those
  were Archimedean shortcuts, since y_λ is `q`-rational by [wenzl1988].
  A later version carried an abstract `(q, v)` with `v² = q`.  Under
  convention D the square root is not needed at all, so `v` is gone and
  every declaration takes `q` alone.

  **Base ring (§7c): the `Field` is essential here, not scaffolding.**
  Adjudicated against `wall-base-ring-minimal`.  The recipe is a
  q-**rational** object — the header calls it that in its first line —
  and *every* step of it is a genuine quotient by an element that
  vanishes somewhere, so none of them is a unit and none is a Laurent
  polynomial:

  * `markovZ = v/(q+1)` — denominator zero at `q = −1`;
  * `universalX = qv/(1 + q − q² − q³ + qv)` — denominator a non-unit
    polynomial;
  * `schurPrincipal` — one factor `1/(1 − Q^{h(i,j)})` per cell, each
    zero at a root of unity;
  * `yLambdaRecipe = s_λ / Z_n` — divided by the partition function.

  The worked example `y_lambda_recipe_n2_partition_2` makes this
  explicit rather than hypothetical: it must carry `hq2 : q² ≠ 1`,
  `hq4 : q⁴ ≠ 1`, `hp1 : q + 1 ≠ 0`, `hp2 : q² + 1 ≠ 0`, `hX`, `hX1`
  as hypotheses precisely because those denominators do vanish.  A
  division-free restatement over `ℤ[q, q⁻¹]` is therefore not available:
  the object being defined is not in that ring.  `Field` is the weakest
  class in the §7c table that admits the construction.  Nothing here is
  archimedean — no ordering, no `Real.*` — so the file is already on the
  substrate side of the wall; the `Field` is an algebraic inverse, not a
  post-τ one.

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

/-- **Convention-D Markov parameter** `z_D = q³/(q² + 1)`. -/
noncomputable def markovZ {R : Type u} [Field R] (q : R) : R :=
  q ^ 3 / (q ^ 2 + 1)

/-- The **Wenzl-normalised** parameter `z_W = q · z_D`.  The factor `q` is
    the Hecke-normalisation shift between `g² = (Q−1)g + Q` and
    `σ² = (q − q⁻¹)σ + 1`, under which `σ = g/q` and `Q = q²`. -/
noncomputable def markovZW {R : Type u} [Field R] (q : R) : R :=
  q * markovZ q

/-- **Universal X**, convention D: `X = Q^r` at `Q = q²`, `r = 2`. -/
noncomputable def universalX {R : Type u} [Field R] (q : R) : R :=
  q ^ 4

/-- **`X` is on the Wenzl lattice at level 2.**  `X = z_W/(1 − Q + z_W)`
    with `Q = q²` — the relation that pins the level — evaluates to `q⁴`,
    i.e. `Q²`, so the convention-D recipe sits at the integer level `r = 2`.

    This is the lemma the old convention-C form could not state: there the
    same inversion gives `z_W = q^{3/2}/(q+1)` and an effective level of
    about `2.5995` at the substrate anchor, which is not an integer and so
    not on the lattice at all. -/
theorem universalX_eq_lattice {R : Type u} [Field R] (q : R) (hq2 : q ^ 2 + 1 ≠ 0) :
    markovZW q / (1 - q ^ 2 + markovZW q) = universalX q := by
  have hzw : markovZW q = q ^ 4 / (q ^ 2 + 1) := by
    rw [markovZW, markovZ]; ring
  -- `(1 − q²)(q² + 1) + q⁴ = 1`, so the whole denominator collapses.
  have hden : (1 : R) - q ^ 2 + markovZW q = 1 / (q ^ 2 + 1) := by
    rw [hzw]; field_simp; ring
  rw [universalX, hden, hzw]
  field_simp

/-! ## Step 3: Schur principal-specialisation -/

/-- The Schur principal-specialisation factor for partition λ at
    level r, with `Q = q²` and `X = Q^r`:

      s_{λ, r}(Q) = Q^{n(λ)} · ∏_{(i,j) ∈ λ} (1 - X·Q^{c(i,j)}) / (1 - Q^{h(i,j)})

    Concrete cell-product: outer fold over rows `(row-length, row-index)`
    (the `hookDim` iteration pattern), inner fold over columns `j`.  The
    content `c(i,j) : ℤ` gives an integer power `Q ^ (c : ℤ)` (zpow); the
    hook `h(i,j) : ℕ` gives a natural power. -/
noncomputable def schurPrincipal {R : Type u} [Field R] (lam : List ℕ) (q : R) : R :=
  let Q := q ^ 2
  let X := universalX q
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
noncomputable def partitionFunctionZ {R : Type u} [Field R] (n : ℕ) (q : R) : R :=
  (partitionsOf n).foldr
    (fun mu acc => acc + (hookDim mu : R) * schurPrincipal mu q) 0

/-- The recipe: `y_λ(q) = s_{λ, r}(Q) / Z_n`. -/
noncomputable def yLambdaRecipe {R : Type u} [Field R]
    (lam : List ℕ) (q : R) : R :=
  schurPrincipal lam q /
    partitionFunctionZ (lam.foldr (· + ·) 0) q

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
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see folio/bib-qa-verifications.json
-- Converted `axiom` -> `opaque` 2026-09-04: this declares a SYMBOL, not a claim.
-- `axiom f : T` and `opaque f : T := <witness>` are equally opaque, but only the
-- first is a global axiom contaminating `#print axioms` downstream.  No
-- proposition becomes provable either way.
opaque JonesMarkovCoefficient {R : Type u} [Field R]
    (q : R) (lam : List ℕ) : R := 0

/-- The Markov-trace convention this recipe implements. -/
def yLambdaRecipeConvention : MarkovTraceConvention :=
  MarkovTraceConvention.wenzlSchur

/-- The Wenzl–Schur-tagged y_λ wrapper. -/
noncomputable def jonesMarkovTagged {R : Type u} [Field R]
    (q : R) (lam : List ℕ) : MarkovTraceCoefficient R :=
  { value := JonesMarkovCoefficient q lam,
    convention := yLambdaRecipeConvention }

@[simp] theorem jonesMarkovTagged_convention {R : Type u} [Field R]
    (q : R) (lam : List ℕ) :
    (jonesMarkovTagged q lam).convention =
      MarkovTraceConvention.wenzlSchur :=
  rfl

/-- **External axiom (Wenzl 1988):** y_λ recipe matches the canonical
    Jones-Markov coefficient via Macdonald hook telescope. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see folio/bib-qa-verifications.json
axiom y_lambda_recipe_correct_axiom :
    ∀ {R : Type u} [Field R] (q : R) (lam : List ℕ),
      (∀ p ∈ lam, 0 < p) → List.Sorted (· ≥ ·) lam →
      JonesMarkovCoefficient q lam = yLambdaRecipe lam q

theorem y_lambda_recipe_correct {R : Type u} [Field R]
    (q : R) (lam : List ℕ)
    (_hpos : ∀ p ∈ lam, 0 < p)
    (_hnonincr : List.Sorted (· ≥ ·) lam) :
    JonesMarkovCoefficient q lam = yLambdaRecipe lam q :=
  y_lambda_recipe_correct_axiom q lam _hpos _hnonincr

/-- **External axiom (Wenzl 1988):** Plancherel completeness
    `Σ_λ⊢n d_λ · y_λ(q) = 1`. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see folio/bib-qa-verifications.json
axiom plancherel_via_recipe_axiom :
    ∀ {R : Type u} [Field R] (q : R) (n : ℕ)
      (parts : List (List ℕ)),
      (∀ lam : List ℕ, lam.foldr (· + ·) 0 = n → lam ∈ parts) →
      parts.Nodup →
      (parts.map (fun lam => (hookDim lam : R) * yLambdaRecipe lam q)).sum
        = (1 : R)

/-- **Plancherel completeness**: Σ_λ⊢n d_λ · y_λ(q) = 1 for every n. -/
theorem plancherel_via_recipe {R : Type u} [Field R]
    (q : R) (n : ℕ)
    (parts : List (List ℕ))
    (_parts_complete : ∀ lam : List ℕ,
      lam.foldr (· + ·) 0 = n → lam ∈ parts)
    (_parts_nodup : parts.Nodup) :
    (parts.map
      (fun lam => (hookDim lam : R) * yLambdaRecipe lam q)).sum
        = (1 : R) :=
  plancherel_via_recipe_axiom q n parts _parts_complete _parts_nodup

/-- **Cyclotomic factorisation**: the recipe output factors as
    P_λ(v) / D_n(v) where D_n is a pure product of cyclotomic
    polynomials Φ_d(v). -/
opaque YLambdaRecipeCyclotomicFactor : Prop

/-- **External axiom (Wenzl 1988):** cyclotomic factorisation of the
    y_λ recipe denominator. -/
-- Ref: [wenzl1988] Wenzl, "Hecke algebras of type A_n and subfactors," Invent. Math. 92 (1988). Verified-clean — see folio/bib-qa-verifications.json
axiom y_lambda_cyclotomic_via_recipe_axiom :
    ∀ {R : Type u} [Field R] (q : R) (lam : List ℕ),
      YLambdaRecipeCyclotomicFactor

theorem y_lambda_cyclotomic_via_recipe {R : Type u} [Field R]
    (q : R) (lam : List ℕ) :
    YLambdaRecipeCyclotomicFactor :=
  y_lambda_cyclotomic_via_recipe_axiom q lam

/-! ## Worked example: n = 2 -/

/-- **Worked example, `λ = (2)` at `n = 2`**, convention D.

With `X = q⁴` the recipe reduces through the two `n = 2` partitions
`{(2), (1,1)}` (both of dimension 1) to

    y_{(2)} = (q² − q + 1)(q² + q + 1) / (q² + 1)²,

whose numerator is `Φ₆(q)·Φ₃(q) = q⁴ + q² + 1` — the cyclotomic factorisation
of step 5, now visible over ℚ(q) rather than ℚ(√q).

The convention-C statement of this example was
`(q·v + q + 1)/((q + 1)(q² + 1))` with `v = √q`, and it needed five
hypotheses (`hq4`, `hp1`, `hX`, `hX1` and the derived `hXm`) purely to keep
the `X` denominator and the `1 − X` cancellation alive.  Under D, `X = q⁴` is
a polynomial, so those all disappear: only the two genuine hook denominators
`1 − q²` and `1 − q⁴` remain, and `q + 1 ≠ 0` is no longer needed at all.

`Z_2 = (1 + q²)²` here is the `n = 2` case of the closed form
`QOU.SchurWeyl.sum_dim_schurPrincipal` proves at every integer level. -/
theorem y_lambda_recipe_n2_partition_2 {R : Type u} [Field R]
    (q : R) (hq : q ≠ 0) (hq2 : q ^ 2 ≠ 1) (hq4 : q ^ 4 ≠ 1) (hp2 : q ^ 2 + 1 ≠ 0) :
    yLambdaRecipe [2] q
      = (q ^ 2 - q + 1) * (q ^ 2 + q + 1) / (q ^ 2 + 1) ^ 2 := by
  have hs2 : schurPrincipal [2] q
      = (q ^ 2) ^ (0 : ℕ) *
        (1 * ((1 * ((1 - universalX q * (q ^ 2) ^ (1 : ℤ)) / (1 - (q ^ 2) ^ (1 : ℕ)))) *
              ((1 - universalX q * (q ^ 2) ^ (0 : ℤ)) / (1 - (q ^ 2) ^ (2 : ℕ))))) := by
    rfl
  have hs11 : schurPrincipal [1, 1] q
      = (q ^ 2) ^ (1 : ℕ) *
        ((1 * (1 * ((1 - universalX q * (q ^ 2) ^ (-1 : ℤ)) / (1 - (q ^ 2) ^ (1 : ℕ))))) *
         (1 * ((1 - universalX q * (q ^ 2) ^ (0 : ℤ)) / (1 - (q ^ 2) ^ (2 : ℕ))))) := by
    rfl
  have hp : partitionsOf 2 = [[2], [1, 1]] := by decide
  have hd2 : hookDim [2] = 1 := by decide
  have hd11 : hookDim [1, 1] = 1 := by decide
  have hrec : ([2] : List ℕ).foldr (· + ·) 0 = 2 := rfl
  have hq2ne : q ^ 2 ≠ 0 := pow_ne_zero 2 hq
  have hd1 : (1 : R) - q ^ 2 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq2)
  have hd4' : (1 : R) - q ^ 4 ≠ 0 := sub_ne_zero.mpr (Ne.symm hq4)
  -- `Z_2 = (1 + q²)²`, the closed form, so in particular `Z_2 ≠ 0`.
  have hZval : schurPrincipal [1, 1] q + schurPrincipal [2] q = (1 + q ^ 2) ^ 2 := by
    rw [hs2, hs11, universalX]
    simp only [zpow_zero, zpow_one, zpow_neg_one, pow_zero, pow_one, mul_one, one_mul]
    field_simp
    ring
  have hZne : schurPrincipal [1, 1] q + schurPrincipal [2] q ≠ 0 := by
    rw [hZval]
    exact pow_ne_zero 2 (by rw [add_comm]; exact hp2)
  unfold yLambdaRecipe partitionFunctionZ
  rw [hrec, hp]
  simp only [List.foldr_cons, List.foldr_nil, hd2, hd11, Nat.cast_one, one_mul, zero_add]
  rw [div_eq_div_iff hZne (pow_ne_zero 2 hp2), hs2, hs11, universalX]
  field_simp
  ring

end QOU.BraidsAndKnots
