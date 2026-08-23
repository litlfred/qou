/-
  **The index of a generalized Wronskian**, composed end to end — the index counterpart of
  `QOU/Mathlib/WronskianHeight.lean`.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `QOU/Mathlib/MvGenWronskian.lean` and
  `QOU/Mathlib/RothIndex.lean`.  Both are Mathlib-only, so the three lift together.

  ═══ ⚠ WHAT THIS FIXES, AND WHY IT WAS MISSED ═══

  `QOU/Mathlib/RothBaseCase.lean` claimed, in prose, that "`abs_coeff_mvGenWronskian_le` and
  `index_det_ge` bound" the Wronskian.  **The index half of that was false when written.**

  `index_det_ge` bounds `index (det M)` from below by the indices of the matrix *entries*.
  For a generalized Wronskian the entries are `pderivList (D i) (f j)`, and nothing related
  those back to `index (f j)`.  The height side had exactly this composite
  (`abs_coeff_mvGenWronskian_le`); the index side did not, and the asymmetry went unnoticed
  because each half looked complete from its own end.

  That is the same failure this arc has now hit five times — a stack of true lemmas reading as
  a finished argument — and this instance was written *in the same commit* that warned about
  it.  The warning is not self-executing; only the audit is.

  ═══ THE RESULT ═══

      ∑ᵢ index (f i)  ≤  index (mvGenWronskian D f)  +  m · C

  whenever every operator list `D k` has differentiation cost `∑_{j ∈ D k} 1/dⱼ` at most `C`.

  Read it as "differentiating `m` times costs at most `m·C` of index": the Wronskian's index
  is at least the total index of the `f` minus the total cost.  It is stated additively
  because `WithTop ℚ` has no subtraction, and `⊤` must survive — a zero `f i` contributes `⊤`
  to the left and the statement stays true.

  ⚠ Note the direction, which is opposite to the height file: heights are bounded from
  *above* by their parts, indices from *below*.
-/
import QOU.Mathlib.MvGenWronskian
import QOU.Mathlib.RothIndex
import Mathlib.Algebra.Order.Field.Basic

namespace MvPolynomial

variable {σ R : Type*} [CommRing R]

/-- `WithTop ℚ` is not a semiring, so `nsmul_eq_mul` does not apply to it; this is the
replacement the `Finset.sum_const` step needs. -/
theorem nsmul_coe_withTop (k : ℕ) (c : ℚ) :
    k • ((c : ℚ) : WithTop ℚ) = (((k : ℚ) * c : ℚ) : WithTop ℚ) := by
  induction k with
  | zero => simp
  | succ n ih =>
      rw [succ_nsmul, ih, ← WithTop.coe_add]
      congr 1
      push_cast
      ring

/-- **Iterated differentiation costs at most `∑_{j ∈ l} 1/dⱼ` of index.**

The list form of `index_le_index_pderiv_add`.  Each step of `pderivList` can drop the index by
at most `1/dⱼ` for the variable `j` differentiated, and the costs add. -/
theorem index_le_index_pderivList_add [DecidableEq σ] (d : σ → ℕ) (α : σ → R)
    (l : List σ) (P : MvPolynomial σ R) :
    index d α P ≤ index d α (pderivList l P)
      + ((((l.map (fun j => (1 : ℚ) / (d j : ℚ))).sum) : ℚ) : WithTop ℚ) := by
  induction l generalizing P with
  | nil => simp [pderivList]
  | cons j l' ih =>
      have h1 := ih P
      have h2 := index_le_index_pderiv_add d α j (pderivList l' P)
      show index d α P ≤ index d α (pderiv j (pderivList l' P)) + _
      refine le_trans h1 ?_
      rw [List.map_cons, List.sum_cons, WithTop.coe_add]
      calc index d α (pderivList l' P)
            + (((l'.map (fun j => (1 : ℚ) / (d j : ℚ))).sum : ℚ) : WithTop ℚ)
          ≤ (index d α (pderiv j (pderivList l' P))
              + (((1 : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ))
            + (((l'.map (fun j => (1 : ℚ) / (d j : ℚ))).sum : ℚ) : WithTop ℚ) :=
            add_le_add_right h2 _
        _ = index d α (pderiv j (pderivList l' P))
              + ((((1 : ℚ) / (d j : ℚ) : ℚ) : WithTop ℚ)
                + (((l'.map (fun j => (1 : ℚ) / (d j : ℚ))).sum : ℚ) : WithTop ℚ)) :=
            add_assoc _ _ _

/-- **The index of a generalized Wronskian:**

    ∑ᵢ index (f i)  ≤  index (mvGenWronskian D f)  +  m · C

when every operator list has differentiation cost at most `C`.

The composite `index_det_ge` alone does not give: that bounds the determinant by the indices
of its *entries*, which are `pderivList (D i) (f j)`, and it is
`index_le_index_pderivList_add` that carries those back to the `f`.

The proof evaluates the infimum in `index_det_ge` at a permutation attaining it — `Perm (Fin m)`
is a non-empty fintype, so one exists — and then bounds that permutation's sum termwise.  It
is the same shape as `abs_coeff_mvGenWronskian_le`, run in the opposite order. -/
theorem sum_index_le_index_mvGenWronskian_add [DecidableEq σ] {m : ℕ}
    (d : σ → ℕ) (α : σ → R) (D : Fin m → List σ) (f : Fin m → MvPolynomial σ R) (C : ℚ)
    (hC : ∀ k, ((D k).map (fun j => (1 : ℚ) / (d j : ℚ))).sum ≤ C) :
    ∑ i, index d α (f i)
      ≤ index d α (mvGenWronskian D f) + (((m : ℚ) * C : ℚ) : WithTop ℚ) := by
  classical
  obtain ⟨p₀, -, hp₀⟩ := Finset.exists_mem_eq_inf (Finset.univ : Finset (Equiv.Perm (Fin m)))
    Finset.univ_nonempty (fun p => ∑ i : Fin m, index d α (mvWronskianMatrix D f (p i) i))
  have hdet : ∑ i : Fin m, index d α (mvWronskianMatrix D f (p₀ i) i)
      ≤ index d α (mvGenWronskian D f) := by
    rw [mvGenWronskian, ← hp₀]
    exact index_det_ge d α _
  have hterm : ∀ i : Fin m, index d α (f i)
      ≤ index d α (mvWronskianMatrix D f (p₀ i) i) + ((C : ℚ) : WithTop ℚ) := by
    intro i
    rw [mvWronskianMatrix_apply]
    refine le_trans (index_le_index_pderivList_add d α (D (p₀ i)) (f i)) ?_
    exact add_le_add_left (WithTop.coe_le_coe.mpr (hC (p₀ i))) _
  calc ∑ i : Fin m, index d α (f i)
      ≤ ∑ i : Fin m, (index d α (mvWronskianMatrix D f (p₀ i) i) + ((C : ℚ) : WithTop ℚ)) :=
        Finset.sum_le_sum (fun i _ => hterm i)
    _ = (∑ i : Fin m, index d α (mvWronskianMatrix D f (p₀ i) i))
          + (((m : ℚ) * C : ℚ) : WithTop ℚ) := by
        rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
          nsmul_coe_withTop]
    _ ≤ index d α (mvGenWronskian D f) + (((m : ℚ) * C : ℚ) : WithTop ℚ) :=
        add_le_add_right hdet _

/-- **The differentiation cost of a list is at most its length over the smallest degree.**

`∑_{k ∈ l} 1/dₖ ≤ |l| / D` when `D ≤ dₖ` for every `k`.  This is what turns the abstract cost
hypothesis of the bounds below into something concrete. -/
theorem sum_map_inv_le_length_div {D : ℕ} (hD : D ≠ 0) (d : σ → ℕ) (hd : ∀ k, D ≤ d k)
    (l : List σ) :
    (l.map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ (l.length : ℚ) / (D : ℚ) := by
  have hDQ : (0 : ℚ) < (D : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD
  induction l with
  | nil => simp
  | cons a t ih =>
      rw [List.map_cons, List.sum_cons, List.length_cons]
      have h1 : (1 : ℚ) / (d a : ℚ) ≤ 1 / (D : ℚ) :=
        one_div_le_one_div_of_le hDQ (by exact_mod_cast hd a)
      have hsplit : ((t.length + 1 : ℕ) : ℚ) / (D : ℚ)
          = (1 : ℚ) / (D : ℚ) + (t.length : ℚ) / (D : ℚ) := by
        push_cast; ring
      rw [hsplit]
      exact add_le_add h1 ih

/-- **The index of a determinant of operators applied to a single polynomial.**

`sum_index_le_index_mvGenWronskian_add` covers a *family* `f`, with one operator list per row.
The separated factorisation of `QOU/Mathlib/SeparatedWronskian.lean` produces something else:
a matrix whose `(i,j)` entry is a *mixed* operator `Dx i ++ Dy j` applied to **one**
polynomial `P`.  Nothing covered that, and it is what turns "`P` has large index" into "its
Wronskian has large index".

Same proof shape as the family version — evaluate `index_det_ge`'s infimum at a permutation
attaining it, then bound each entry by `index_le_index_pderivList_add`. -/
theorem sum_index_le_index_det_pderivList_add [DecidableEq σ] {r : ℕ}
    (d : σ → ℕ) (α : σ → R) (D : Fin r → Fin r → List σ) (P : MvPolynomial σ R) (C : ℚ)
    (hC : ∀ i j, ((D i j).map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ C) :
    ∑ _i : Fin r, index d α P
      ≤ index d α (Matrix.of fun i j => pderivList (D i j) P).det
        + (((r : ℚ) * C : ℚ) : WithTop ℚ) := by
  classical
  set M : Matrix (Fin r) (Fin r) (MvPolynomial σ R) :=
    Matrix.of fun i j => pderivList (D i j) P with hM
  obtain ⟨p₀, -, hp₀⟩ := Finset.exists_mem_eq_inf (Finset.univ : Finset (Equiv.Perm (Fin r)))
    Finset.univ_nonempty (fun p => ∑ i : Fin r, index d α (M (p i) i))
  have hdet : ∑ i : Fin r, index d α (M (p₀ i) i) ≤ index d α M.det := by
    rw [← hp₀]; exact index_det_ge d α _
  have hterm : ∀ i : Fin r,
      index d α P ≤ index d α (M (p₀ i) i) + ((C : ℚ) : WithTop ℚ) := by
    intro i
    have h : M (p₀ i) i = pderivList (D (p₀ i) i) P := rfl
    rw [h]
    exact le_trans (index_le_index_pderivList_add d α (D (p₀ i) i) P)
      (add_le_add_left (WithTop.coe_le_coe.mpr (hC _ _)) _)
  calc ∑ _i : Fin r, index d α P
      ≤ ∑ i : Fin r, (index d α (M (p₀ i) i) + ((C : ℚ) : WithTop ℚ)) :=
        Finset.sum_le_sum (fun i _ => hterm i)
    _ = (∑ i : Fin r, index d α (M (p₀ i) i)) + (((r : ℚ) * C : ℚ) : WithTop ℚ) := by
        rw [Finset.sum_add_distrib, Finset.sum_const, Finset.card_univ, Fintype.card_fin,
          nsmul_coe_withTop]
    _ ≤ index d α M.det + (((r : ℚ) * C : ℚ) : WithTop ℚ) := add_le_add_right hdet _

/-! ### Validation — the bound is attained

`RothIndex.lean` sets the standard that a validation should pin a value, since a wrong
constant would satisfy every structural lemma.  Here the risk is the *cost* factor: a bound
with `2·m·C`, or with the cost dropped entirely, would still be a true theorem in many
instances and would still typecheck.

This instance is **tight**, so it pins the constant.  Take `m = 1`, `f = X`, `D = ![[0]]` — one
derivative — with unit weight at the origin, so `C = 1`.  Then `index X = 1` on the left, the
Wronskian is `∂₀X = 1` with index `0`, and the right side is `0 + 1·1 = 1`.  Both sides are
`1`: a smaller cost factor would make the theorem false at this very instance. -/
theorem sum_index_mvGenWronskian_bound_tight :
    (∑ i : Fin 1, index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        ((fun _ : Fin 1 => (X 0 : MvPolynomial (Fin 1) ℚ)) i))
      = index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
          (mvGenWronskian (fun _ : Fin 1 => [(0 : Fin 1)])
            (fun _ : Fin 1 => (X 0 : MvPolynomial (Fin 1) ℚ)))
        + ((((1 : ℕ) : ℚ) * 1 : ℚ) : WithTop ℚ) := by
  have hW : mvGenWronskian (fun _ : Fin 1 => [(0 : Fin 1)])
      (fun _ : Fin 1 => (X 0 : MvPolynomial (Fin 1) ℚ)) = 1 := by
    rw [mvGenWronskian, Matrix.det_fin_one, mvWronskianMatrix_apply]
    show pderiv (0 : Fin 1) (X 0 : MvPolynomial (Fin 1) ℚ) = 1
    simp
  have h1 : index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
      (1 : MvPolynomial (Fin 1) ℚ) = 0 := by
    have ht : translate (fun _ : Fin 1 => (0 : ℚ)) (1 : MvPolynomial (Fin 1) ℚ) = 1 := by
      simp [translate]
    rw [index, ht, show (1 : MvPolynomial (Fin 1) ℚ) = monomial 0 1 by simp, support_monomial]
    norm_num [idxWeight]
  rw [hW, h1, Fin.sum_univ_one, index_X]
  norm_num

/-! ### Next

Both halves of what the induction needs from a Wronskian are now composites rather than
fragments: `abs_coeff_mvGenWronskian_le` bounds its height, this bounds its index, and
`index_separated` / `abs_coeff_le_of_mul_separated` carry both across the separated
factorization to the two factors.

⚠ What remains is the **recursion** — Roth's lemma's statement with its parameter conditions
(`dⱼ/dⱼ₊₁` growth, `ε`, the `qⱼ` hypotheses) and the step feeding `RothBaseCase` and the `m−1`
case back into the `m` case.

⚠ And a standing caution, earned: this module exists because a *prose* claim about what was
"bounded" turned out false.  The next such claim should be checked by writing Roth's lemma's
statement in Lean and matching each hypothesis to a named theorem — not to a module docstring
or a bean entry. -/

end MvPolynomial
