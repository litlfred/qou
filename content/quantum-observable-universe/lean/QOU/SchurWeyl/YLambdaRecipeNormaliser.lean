import QOU.SchurWeyl.WenzlNormalisation

/-!
# QOU.SchurWeyl.YLambdaRecipeNormaliser — the `y_λ` recipe's `Z_n`, in closed form

`prop:y-lambda-recipe-from-partition`
([`y-lambda-recipe-from-partition.md`](../../../mass-theory/y-lambda-recipe-from-partition.md))
computes the Jones–Markov central coefficient in four steps.  Step 3 forms the
Schur principal specialisation, and step 4 divides by

`Z_n = ∑_{μ ⊢ n} f^μ · s_{μ,r}(Q)`,

a sum over **all** partitions of `n` — `p(n)` terms, which is what makes the
recipe's cost `O(p(n) · max hooks)`.

This file gives `Z_n` in closed form on the Wenzl lattice:

`Z_n = [r]_Q ^ n`.

So step 4 needs no sum at all, and `y_λ` is `wenzlWeight r Q λ` on the nose —
`QOU.SchurWeyl.wenzlWeight` is exactly the recipe's output, not merely something
shaped like it.

| | |
|---|---|
| `sum_dim_schurPrincipal` | **`∑_{|ν|=n} f^ν s_ν = [r]_Q^n`** — the recipe's `Z_n` |
| `wenzlWeight_eq_recipe` | `y_λ = s_λ / Z_n` is `wenzlWeight r Q λ` |

## Scope — this is the ON-LATTICE half, and the recipe is OFF it

`r` is the Wenzl level and is a positive integer; `Q^r = z_W/(1 − Q + z_W)` pins
the lattice.  **The recipe's own substitution is not at an integer `r`.**  It
fixes

`X := q^{3/2} / (1 + q − q² − q³ + q^{3/2})`

in place of `Q^r`, and inverting the lattice relation gives, exactly,

`X = z_W/(1 − Q + z_W)` at `Q = q²` with `z_W = q·z_C = q^{3/2}/(q+1)`

— the **convention-C** parameter, Wenzl-normalised.  At the substrate anchor
that is an effective level `r ≈ 2.5995`, not an integer.  So the theorems below
do **not** apply to the recipe as written; they apply to its integer-level
counterpart.  Two consequences, neither of them closed here:

* the recipe is convention-**C** frame, and the 2026-08-15 owner ruling makes D
  canonical — so it needs re-derivation, not a `z`-swap (bean `qou-cds1` records
  why substituting `z_D` into a C-frame ladder is not a valid move);
* the closed form appears to hold **off** the lattice too — `∑_{μ⊢n} f^μ s_μ(X)
  = ((1−X)/(1−Q))^n` for a general `X`, symbolically verified for `n = 1…6`,
  which specialises to `[r]_Q^n` at `X = Q^r`.  That general statement is
  **not proved here**: the proof below runs on the `r`-row β-coordinates and
  the `r`-element Lagrange sum, so it is tied to integer `r` and a general-`X`
  version needs a different argument.  Tracked as a bean.

## Base ring (§7c)

Generic `[Field F]` — division only, nothing archimedean.

LaTeX label: `lem:y-lambda-recipe-normaliser`
-/

namespace QOU.SchurWeyl

open YoungDiagram Finset QOU.Mathlib

variable {F : Type*} [Field F]

/-- **The recipe's `Z_n`, in closed form.**

`∑_{μ ⊢ n} f^μ · s_μ(1, Q, …, Q^{r−1}) = [r]_Q ^ n`.

Step 4 of `prop:y-lambda-recipe-from-partition` sums over every partition of `n`
to build its normaliser; on the Wenzl lattice that sum is `[r]_Q ^ n`.

This is `sum_dim_wenzlWeight_eq_one` with the normalisation cleared: the weight
divides by `[r]_Q ^ |μ|` per diagram, and every diagram in the sum has `|μ| = n`,
so the whole sum scales by the single factor `[r]_Q ^ n`. -/
theorem sum_dim_schurPrincipal (Q : F) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) {r : ℕ} (hbr : levelBracket r Q ≠ 0) (hQ1 : Q ≠ 1)
    (n : ℕ) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (numStandardYoungTableaux ν.1 : F) * QOU.QBeta.WenzlWeight.schurPrincipal r Q ν.1)
      = levelBracket r Q ^ n := by
  have hone := sum_dim_wenzlWeight_eq_one Q hQ0 hgen (r := r) hbr hQ1 n
  have hrw : ∀ ν : {ν : YoungDiagram // ν.cells.card = n},
      (numStandardYoungTableaux ν.1 : F) * wenzlWeight r Q ν.1
        = ((numStandardYoungTableaux ν.1 : F)
            * QOU.QBeta.WenzlWeight.schurPrincipal r Q ν.1) / levelBracket r Q ^ n := by
    intro ν
    rw [wenzlWeight, ν.2]
    ring
  rw [Finset.sum_congr rfl fun ν _ => hrw ν, ← Finset.sum_div, div_eq_one_iff_eq] at hone
  · exact hone
  · exact pow_ne_zero _ hbr

/-- **The recipe's output is `wenzlWeight`.**

`y_λ = s_λ / Z_n` — step 4 of the recipe — is `wenzlWeight r Q λ`, once `Z_n` is
the closed form above.  So the `y_lambda` field of `QOU.Hecke.WedderburnDecomp`,
whose docstring gives precisely this recipe, has a proved closed form on the
Wenzl lattice rather than only a prose one.

Stated per-diagram; `hν` is what ties the recipe's `n` to the diagram. -/
theorem wenzlWeight_eq_recipe (Q : F) {r n : ℕ} (hbr : levelBracket r Q ≠ 0)
    {ν : YoungDiagram} (hν : ν.cells.card = n) :
    wenzlWeight r Q ν
      = QOU.QBeta.WenzlWeight.schurPrincipal r Q ν / levelBracket r Q ^ n := by
  rw [wenzlWeight, hν]

end QOU.SchurWeyl
