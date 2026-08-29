import QOU.MathlibExt.WenzlSchurElement
import QOU.MathlibExt.WenzlSchurElementBridge
import Mathlib.Algebra.Polynomial.Roots

/-!
# QOU.MathlibExt.MacdonaldTelescopeGeneralX — the general-`X` hook telescope (research)

The Macdonald hook telescope

  `Σ_{λ ⊢ n} f_λ · schurElement Q X λ = ((1 − X)/(1 − Q))^n`

is proved in the corpus only at the **principal specialisation** `X = Q^r`
(`QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one`, transported to the List carrier by
`WenzlJonesMarkovNormalisation.sum_dim_jonesMarkovCoeff_eq_one`). The identity is
in fact true for **all** `X`; this file develops that generalisation.

## The route (polynomial identity in `X`)

`schurElement Q X λ = Q^{n(λ)} · ∏_x (1 − X·Q^{c(x)}) / (1 − Q^{h(x)})` has `X`
only in the numerator, so it is a **polynomial in `X`** of degree `|λ| = n` (over
the field `ℝ`, with `Q` fixed and generic). Hence:

* **LHS** `Σ_{λ⊢n} f_λ · schurElement Q X λ` is a polynomial in `X` of degree ≤ `n`;
* **RHS** `((1 − X)/(1 − Q))^n = (1 − Q)^{-n} · (1 − X)^n` is a polynomial in `X`
  of degree `n`.

Both polynomials agree at `X = Q^r` for every `r ≥ n` (the proved
specialisation, summed over the `f_λ`-weighted shapes of size `n`). For the
substrate regime `Q > 1` the set `{Q^r : r ∈ ℕ}` is **infinite**, so
`Polynomial.eq_of_infinite_eval_eq` forces the two polynomials equal — hence the
telescope holds for **all** `X`.

## Plan / status

This is a research tranche, developed brick by brick:

1. **`powers_infinite`** — `{x : ℝ | ∃ n, Q^n = x}` is infinite for `Q > 1`
   (this file; the infinite agreement set). ✓
2. **`schurElementPoly Q λ : ℝ[X]`** — lift `schurElement` to a formal
   polynomial in `X` with `eval X (schurElementPoly Q λ) = schurElement Q X λ`.
   [open]
3. **agreement at `X = Q^r`** — from the merged carrier bridge +
   `sum_dim_wenzlWeight_eq_one` (summed, un-normalised: `Σ f_λ s_λ(Q,Q^r) = Z_n`).
   [open]
4. **assembly** — `eq_of_infinite_eval_eq` on 2+3 over the infinite set of 1,
   then `eval` at an arbitrary `X`. [open]

Bricks 2–4 are the substantial part (formal-polynomial reformulation of the
nested product, degree bookkeeping); only brick 1 lands here so far.

## References

- [wenzl1988] Wenzl, "Hecke algebras of type $A_n$ and subfactors," Invent. Math. 92.
- [macdonald1995] Macdonald, *Symmetric Functions and Hall Polynomials*, §I.3.
-/

namespace QOU.MathlibExt.MacdonaldTelescopeGeneralX

/-- **The agreement set is infinite.** For `Q > 1` the powers `Q^n` are strictly
increasing, hence distinct, so `{x | ∃ n, Q^n = x}` is infinite — the infinite
set on which the two telescope polynomials agree, which
`Polynomial.eq_of_infinite_eval_eq` needs to force them equal. -/
theorem powers_infinite (Q : ℝ) (hQ : 1 < Q) :
    Set.Infinite {x : ℝ | ∃ n : ℕ, Q ^ n = x} := by
  have hmono : StrictMono (fun n : ℕ => Q ^ n) := fun a b h => by
    simpa using pow_lt_pow_right₀ hQ h
  have hset : {x : ℝ | ∃ n : ℕ, Q ^ n = x} = Set.range (fun n : ℕ => Q ^ n) := by
    ext x
    constructor
    · rintro ⟨n, rfl⟩; exact ⟨n, rfl⟩
    · rintro ⟨n, rfl⟩; exact ⟨n, rfl⟩
  rw [hset]
  exact Set.infinite_range_of_injective hmono.injective

open QOU.MathlibExt.WenzlSchurElement
open QOU.MathlibExt.QPartitionCombinatorics
open Polynomial

/-- Polynomial-in-`X` lift of a single cell factor. `cellFactor Q X λ i j` has
`X` only in the numerator `(1 − X·Q^{c})`; the denominator `(1 − Q^{h})` is
`X`-free and enters as the constant `C ((1 − Q^{h})⁻¹)`. -/
noncomputable def cellFactorPoly (Q : ℝ) (lam : Partition) (i j : ℕ) : ℝ[X] :=
  C ((1 - Q ^ (Partition.hookLength lam i j))⁻¹)
    * (C 1 - C (Q ^ (WenzlSchurElement.cellContent i j)) * X)

/-- Polynomial-in-`X` lift of the whole Schur element: `Q^{n(λ)}` (constant) times
the row/cell product of the `cellFactorPoly`s. -/
noncomputable def schurElementPoly (Q : ℝ) (lam : Partition) : ℝ[X] :=
  C (Q ^ (nLambda lam))
    * ∏ i ∈ Finset.range lam.length,
        ∏ j ∈ Finset.range ((lam[i]?).getD 0), cellFactorPoly Q lam i j

/-- **Brick 2 — the polynomial lift is faithful.** Evaluating `schurElementPoly`
at `X₀` recovers `schurElement Q X₀ λ`. This makes `schurElement Q · λ` a genuine
polynomial in its second argument, the premise the identity-theorem route needs. -/
theorem eval_schurElementPoly (Q X0 : ℝ) (lam : Partition) :
    (schurElementPoly Q lam).eval X0 = schurElement Q X0 lam := by
  rw [QOU.MathlibExt.WenzlSchurElementBridge.schurElement_eq_finset_prod]
  unfold schurElementPoly
  rw [Polynomial.eval_mul, Polynomial.eval_C]
  congr 1
  rw [Polynomial.eval_prod]
  apply Finset.prod_congr rfl
  intro i _
  rw [Polynomial.eval_prod]
  apply Finset.prod_congr rfl
  intro j _
  unfold cellFactorPoly cellFactor
  simp only [Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_sub,
    Polynomial.eval_X]
  ring

end QOU.MathlibExt.MacdonaldTelescopeGeneralX
