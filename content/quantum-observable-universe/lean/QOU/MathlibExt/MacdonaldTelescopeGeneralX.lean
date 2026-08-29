import QOU.MathlibExt.WenzlSchurElement
import QOU.MathlibExt.WenzlSchurElementBridge
import QOU.MathlibExt.WenzlJonesMarkovNormalisation
import QOU.SchurWeyl.WenzlNormalisation
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

/-- **Brick 3 — the un-normalised agreement at `X = Q^r`.** Summed over the
SYT-weighted diagrams of size `n`, the List-carrier Schur elements at the
principal specialisation equal `((1 − Q^r)/(1 − Q))^n`. Each term is
`f_ν · wenzlWeight r Q ν · [r]_Q^n` (carrier bridge + `schurPrincipal = wenzlWeight
· [r]_Q^{|ν|}`), and `Σ f_ν · wenzlWeight = 1` (the proved general telescope
`sum_dim_wenzlWeight_eq_one`), leaving `[r]_Q^n = ((1−Q^r)/(1−Q))^n`. -/
theorem sum_dim_schurElement_rowLens_eq (r n : ℕ) (Q : ℝ) (hQ0 : Q ≠ 0)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1)
    (hbr : QOU.SchurWeyl.levelBracket r Q ≠ 0) (hQ1 : Q ≠ 1) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
          * schurElement Q (Q ^ r) ν.1.rowLens)
      = ((1 - Q ^ r) / (1 - Q)) ^ n := by
  have hterm : ∀ ν : {ν : YoungDiagram // ν.cells.card = n},
      (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
          * schurElement Q (Q ^ r) ν.1.rowLens
        = ((QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ)
            * QOU.SchurWeyl.wenzlWeight r Q ν.1)
          * QOU.SchurWeyl.levelBracket r Q ^ n := by
    intro ν
    have hZn : QOU.SchurWeyl.levelBracket r Q ^ ν.1.cells.card ≠ 0 := pow_ne_zero _ hbr
    have hsch : schurElement Q (Q ^ r) ν.1.rowLens
        = QOU.QBeta.WenzlWeight.schurPrincipal r Q ν.1 := by
      rw [WenzlSchurElementBridge.schurElement_eq_schurPrincipal r Q hQ0 ν.1.rowLens
            ν.1.rowLens_sorted ν.1.pos_of_mem_rowLens,
          YoungDiagram.ofRowLens_to_rowLens_eq_self]
    have hwz : QOU.SchurWeyl.wenzlWeight r Q ν.1
        * QOU.SchurWeyl.levelBracket r Q ^ ν.1.cells.card
        = QOU.QBeta.WenzlWeight.schurPrincipal r Q ν.1 := by
      rw [QOU.SchurWeyl.wenzlWeight]
      exact div_mul_cancel₀ _ hZn
    rw [hsch, ← hwz, ν.2]
    ring
  rw [Finset.sum_congr rfl (fun ν _ => hterm ν), ← Finset.sum_mul,
      QOU.SchurWeyl.sum_dim_wenzlWeight_eq_one Q hQ0 hgen hbr hQ1 n, one_mul,
      WenzlJonesMarkovNormalisation.levelBracket_eq r Q hQ1]

/-- `[r+1]_Q ≠ 0` for `Q > 0`: the level bracket over a nonempty range is a sum of
positive powers, hence positive. (Used to invoke brick 3 at `r ≥ 1`, where the
telescope agrees; `r = 0` gives `[0]_Q = 0` and is excluded.) -/
theorem levelBracket_succ_ne_zero (r : ℕ) (Q : ℝ) (hQ : 0 < Q) :
    QOU.SchurWeyl.levelBracket (r + 1) Q ≠ 0 := by
  have hpos : 0 < QOU.SchurWeyl.levelBracket (r + 1) Q := by
    unfold QOU.SchurWeyl.levelBracket
    apply Finset.sum_pos
    · intro i _; exact pow_pos hQ i
    · exact ⟨0, Finset.mem_range.mpr (Nat.succ_pos r)⟩
  exact ne_of_gt hpos

/-- Polynomial-in-`X` lift of the telescope's left-hand side. -/
noncomputable def telescopeLHSPoly (Q : ℝ) (n : ℕ) : ℝ[X] :=
  ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
    C (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ) * schurElementPoly Q ν.1.rowLens

/-- Polynomial-in-`X` lift of the telescope's right-hand side, `((1−X)/(1−Q))^n`. -/
noncomputable def telescopeRHSPoly (Q : ℝ) (n : ℕ) : ℝ[X] :=
  (C ((1 - Q)⁻¹) * (C 1 - X)) ^ n

theorem eval_telescopeLHSPoly (Q X0 : ℝ) (n : ℕ) :
    (telescopeLHSPoly Q n).eval X0
      = ∑ ν : {ν : YoungDiagram // ν.cells.card = n},
          (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ) * schurElement Q X0 ν.1.rowLens := by
  unfold telescopeLHSPoly
  rw [Polynomial.eval_finset_sum]
  apply Finset.sum_congr rfl
  intro ν _
  rw [Polynomial.eval_mul, Polynomial.eval_C, eval_schurElementPoly]

theorem eval_telescopeRHSPoly (Q X0 : ℝ) (n : ℕ) :
    (telescopeRHSPoly Q n).eval X0 = ((1 - X0) / (1 - Q)) ^ n := by
  unfold telescopeRHSPoly
  rw [Polynomial.eval_pow]
  simp only [Polynomial.eval_mul, Polynomial.eval_C, Polynomial.eval_sub, Polynomial.eval_X]
  rw [show (1 - Q)⁻¹ * (1 - X0) = (1 - X0) / (1 - Q) from by ring]

/-- **Brick 4 / the general-`X` hook telescope.** For the substrate regime
`Q > 1`, the Macdonald hook telescope holds for **all** `X`:

  `Σ_{|ν|=n} f^ν · schurElement Q X ν.rowLens = ((1 − X)/(1 − Q))^n`.

Both sides are `eval X` of polynomials in `X` (bricks 2, and the `RHSPoly`); they
agree at every `X = Q^r`, `r ≥ 1` (brick 3), and `{Q^{r+1} : r}` is infinite
(brick 1's argument), so `Polynomial.eq_of_infinite_eval_eq` forces the two
polynomials equal — hence they agree at the arbitrary `X`. -/
theorem telescope_generalX (n : ℕ) (Q X0 : ℝ) (hQ : 1 < Q)
    (hgen : ∀ k : ℤ, k ≠ 0 → Q ^ k ≠ 1) :
    (∑ ν : {ν : YoungDiagram // ν.cells.card = n},
        (QOU.Mathlib.numStandardYoungTableaux ν.1 : ℝ) * schurElement Q X0 ν.1.rowLens)
      = ((1 - X0) / (1 - Q)) ^ n := by
  have hQ0 : Q ≠ 0 := ne_of_gt (lt_trans one_pos hQ)
  have hQ1 : Q ≠ 1 := ne_of_gt hQ
  -- the two polynomials agree on the infinite set {Q^{r+1} : r}
  have hsub : Set.range (fun r : ℕ => Q ^ (r + 1))
      ⊆ {x : ℝ | (telescopeLHSPoly Q n).eval x = (telescopeRHSPoly Q n).eval x} := by
    rintro x ⟨r, rfl⟩
    simp only [Set.mem_setOf_eq]
    rw [eval_telescopeLHSPoly, eval_telescopeRHSPoly,
        sum_dim_schurElement_rowLens_eq (r + 1) n Q hQ0 hgen
          (levelBracket_succ_ne_zero r Q (lt_trans one_pos hQ)) hQ1]
  have hinf : (Set.range (fun r : ℕ => Q ^ (r + 1))).Infinite := by
    apply Set.infinite_range_of_injective
    intro a b hab
    have hmono : StrictMono (fun r : ℕ => Q ^ (r + 1)) := fun i j h => by
      simpa using pow_lt_pow_right₀ hQ (Nat.add_lt_add_right h 1)
    exact hmono.injective hab
  have hPR : telescopeLHSPoly Q n = telescopeRHSPoly Q n :=
    Polynomial.eq_of_infinite_eval_eq _ _ (hinf.mono hsub)
  rw [← eval_telescopeLHSPoly Q X0 n, hPR, eval_telescopeRHSPoly]

end QOU.MathlibExt.MacdonaldTelescopeGeneralX
