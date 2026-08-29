import QOU.Mathlib.SYTHookFormulaBetaMonoid
import QOU.Mathlib.SYTHookFormulaBetaProd

/-!
# QOU.Mathlib.SYTHookFormulaBetaProdMonoid — the full FRT hook product in any commutative monoid

`SYTHookFormulaBetaProd` assembles the per-row identity into the full divisor-free
Frame–Robinson–Thrall hook product over `ℕ`.  `SYTHookFormulaBetaMonoid` showed the per-row half is
arithmetic-free in shape.  The assembly is too: `colLen_eq_succ_add_cnt_drop`, `drop_sorted` and
`drop_le_getD` are facts about `ℕ` **indices** and are reused verbatim, so only the two product
statements need restating.

| | |
|---|---|
| `prodHooksF f l` | `∏_{c ∈ λ} f(h_λ(c))` — the corpus `prodHooks`, pushed through `f` |
| `prodHooksF_eq_prod_rowHookProdF` | it is the product of the per-row `rowHookProdF` |
| `prodHooksF_mul_betaGapProdF` | `prodHooksF f l · ∏_i betaGapProdF f (l[i]) (drop) = ∏_i descFactF f β_i` |
| `prodHooksF_one_sub_pow` | the same at `f n = 1 − Qⁿ` |

The last row is the q-analogue of `∏_c h_λ(c) = (∏_i β_i!) / ∏_{i<j}(β_i − β_j)`, cleared of its
denominator:

`∏_c (1 − Q^{h_λ(c)}) · ∏_i (β-gaps) = ∏_i ∏_{k=1}^{β_i} (1 − Q^k)`.

**What this is not yet.** It is the hook-length identity in *β-gap* form, not in *Vandermonde* form.
Recognising `∏_i betaGapProdF (fun n => 1 − Qⁿ) …` as `∏_{i<j}(1 − Q^{β_i − β_j})` — equivalently as
`∏_{i<j}(x_i − x_j)` up to a monomial, with `x_i = Q^{β_i}` — is the remaining step, and it is a
reindexing of a nested recursion into a pair product rather than a new identity.  Bean `qou-j7ln`;
the consumer is `QOU.Mathlib.LagrangeCoeffSum.sum_eq_bracket_mul_of_qratio_scaling`.

## Base ring (§7c)

Generic `[CommMonoid M]`; the q-instance is over `[CommRing R]`.  Arguments stay in `ℕ`.

LaTeX label: `lem:frt-hook-product-monoid`
-/

namespace QOU.Mathlib.SYTBeta

open QOU.BraidKnot.IdentityI (colLen prodHooks)

variable {M : Type*} [CommMonoid M]

/-- The corpus `prodHooks`, pushed through `f`: `∏_{c ∈ λ} f(h_λ(c))`. -/
def prodHooksF (f : ℕ → M) (l : List ℕ) : M :=
  ((List.range l.length).map (fun i =>
    ((List.range (l.getD i 0)).map
      (fun j => f ((l.getD i 0 - j) + (colLen l j - i) - 1))).prod)).prod

/-- Row `i` of `prodHooksF` is the per-row `rowHookProdF`.  Same leg simplification as the `ℕ`
version — `colLen_eq_succ_add_cnt_drop` is about indices and is reused verbatim. -/
theorem prodHooksF_row_eq_rowHookProdF (f : ℕ → M) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l)
    (i : ℕ) (hi : i < l.length) :
    ((List.range (l.getD i 0)).map
        (fun j => f ((l.getD i 0 - j) + (colLen l j - i) - 1))).prod
      = rowHookProdF f (l.getD i 0) (l.drop (i + 1)) := by
  unfold rowHookProdF
  rw [← list_range_map_prod']
  congr 1
  apply List.map_congr_left
  intro j hj
  rw [List.mem_range] at hj
  rw [colLen_eq_succ_add_cnt_drop l hl i j hi hj]
  congr 1
  omega

theorem prodHooksF_eq_prod_rowHookProdF (f : ℕ → M) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    prodHooksF f l
      = ((List.range l.length).map
          (fun i => rowHookProdF f (l.getD i 0) (l.drop (i + 1)))).prod := by
  unfold prodHooksF
  congr 1
  apply List.map_congr_left
  intro i hi
  rw [List.mem_range] at hi
  exact prodHooksF_row_eq_rowHookProdF f l hl i hi

/-- **The full divisor-free Frame–Robinson–Thrall hook product, in any commutative monoid.**

`prodHooksF f l · ∏_i betaGapProdF f (l[i]) (l.drop (i+1)) = ∏_i descFactF f (l[i] + |drop|)`.

At `f = id` over `(ℕ, ×)` this is `SYTBeta.prodHooks_mul_betaGapProd`. -/
theorem prodHooksF_mul_betaGapProdF (f : ℕ → M) (l : List ℕ) (hl : List.Sorted (· ≥ ·) l) :
    prodHooksF f l *
        ((List.range l.length).map
          (fun i => betaGapProdF f (l.getD i 0) (l.drop (i + 1)))).prod
      = ((List.range l.length).map
          (fun i => descFactF f (l.getD i 0 + (l.drop (i + 1)).length))).prod := by
  rw [prodHooksF_eq_prod_rowHookProdF f l hl, list_range_map_prod', list_range_map_prod',
    list_range_map_prod', ← Finset.prod_mul_distrib]
  apply Finset.prod_congr rfl
  intro i hi
  rw [Finset.mem_range] at hi
  exact rowHookProdF_mul_betaGapProdF f (l.getD i 0) (l.drop (i + 1))
    (drop_sorted l hl i) (drop_le_getD l hl i hi)

/-! ## Conservativity, and the q-analogue -/

theorem prodHooksF_id (l : List ℕ) : prodHooksF (M := ℕ) id l = prodHooks l := rfl

/-- **The q-analogue of the divisor-free FRT hook product.**

`∏_c (1 − Q^{h_λ(c)}) · ∏_i (β-gaps as 1 − Q^{gap}) = ∏_i ∏_{k=1}^{β_i} (1 − Q^k)`.

No separate proof: the assembly, like the per-row step, never touched the values. -/
theorem prodHooksF_one_sub_pow {R : Type*} [CommRing R] (Q : R) (l : List ℕ)
    (hl : List.Sorted (· ≥ ·) l) :
    prodHooksF (fun n => 1 - Q ^ n) l *
        ((List.range l.length).map
          (fun i => betaGapProdF (fun n => 1 - Q ^ n) (l.getD i 0) (l.drop (i + 1)))).prod
      = ((List.range l.length).map
          (fun i => descFactF (fun n => 1 - Q ^ n)
            (l.getD i 0 + (l.drop (i + 1)).length))).prod :=
  prodHooksF_mul_betaGapProdF (fun n => 1 - Q ^ n) l hl

end QOU.Mathlib.SYTBeta
