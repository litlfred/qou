/-
  **The interface of Roth's induction step**, composed and checked in Lean.

  Bean `qou-4lbh`.

  ⚠ Not Mathlib-only: it imports `SeparatedWronskian`, `SeparatedIndex` and `SeparatedHeight`.

  ═══ WHY THIS MODULE EXISTS ═══

  This arc has repeatedly asserted, in module docstrings and bean entries, that its pieces
  "compose" — and has been wrong about that five times.  Prose is not evidence.  The cheap
  check is to write the composition down and let the elaborator decide, which is what this
  module is.

  Everything here is one or two lines given what already exists.  That is the point: if the
  claimed interface is real, the composition is trivial; if it is not, the composition does
  not typecheck.  Both halves below did compose, unchanged — so the claim survives its first
  actual test.

  ═══ WHAT THE STEP NEEDS ═══

  Roth's induction writes the auxiliary polynomial in separated form `∑ₖ φₖ(x)ψₖ(y)`, takes a
  generalized Wronskian of it, and uses that it factors as an `x`-Wronskian times a
  `y`-Wronskian (`det_separated_wronskian`).  To recurse it needs, of that factorisation:

  * the **index** to split — `index_sepW`, exactly additive;
  * the **height** of each factor to be controlled by the height of the whole —
    `abs_coeff_le_of_sepW_left` and `..._right`.

  ⚠ What is still **not** here is the recursion: the parameter conditions (`dⱼ/dⱼ₊₁` growth,
  `ε`, the `qⱼ` hypotheses) and the argument that feeds `RothBaseCase` and the `m−1` case back
  into the `m` case.  This module is its interface, not its proof.
-/
import QOU.Mathlib.SeparatedWronskian
import QOU.Mathlib.SeparatedIndex
import QOU.Mathlib.SeparatedHeight
import QOU.Mathlib.WronskianIndex

namespace MvPolynomial

variable {σ τ : Type*}

/-- The **separated Wronskian**: the generalized Wronskian of `∑ₖ φₖ(x)ψₖ(y)` taken with the
mixed operator family `(Dx i) ++ (Dy j)`.  Named so the statements below fit on a page. -/
noncomputable def sepW {K : Type*} [CommRing K] {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) : MvPolynomial (σ ⊕ τ) K :=
  (Matrix.of fun i j => pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
    (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))).det

/-- `det_separated_wronskian`, restated for `sepW`. -/
theorem sepW_eq {K : Type*} [CommRing K] {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) :
    sepW Dx Dy φ ψ = (rename Sum.inl (mvGenWronskian Dx φ) : MvPolynomial (σ ⊕ τ) K)
      * rename Sum.inr (mvGenWronskian Dy ψ) :=
  det_separated_wronskian Dx Dy φ ψ

/-- **The index half of the induction step:** the separated Wronskian's index is exactly the
sum of the two factors' indices.

One line from `det_separated_wronskian` and `index_separated`.  ⚠ `IsDomain` is used, and only
by `index_separated`'s `≤` half — see that module's header for why it is not removable. -/
theorem index_sepW {K : Type*} [CommRing K] [IsDomain K] {r : ℕ}
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → K) (β : τ → K)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) :
    index (Sum.elim d₁ d₂) (Sum.elim α β) (sepW Dx Dy φ ψ)
      = index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ) := by
  rw [sepW, det_separated_wronskian, index_separated]

/-- **The height half, `x` side:** a height bound on the separated Wronskian bounds the
`x`-Wronskian.

Needs the `y`-Wronskian to be non-zero — which is exactly what the bounded-order criterion
(`BoundedOrderWronskian`) is for. -/
theorem abs_coeff_le_of_sepW_left {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ ℤ) (ψ : Fin r → MvPolynomial τ ℤ)
    (hψ : mvGenWronskian Dy ψ ≠ 0) {B : ℤ}
    (hB : ∀ n, |coeff n (sepW Dx Dy φ ψ)| ≤ B) (i : σ →₀ ℕ) :
    |coeff i (mvGenWronskian Dx φ)| ≤ B := by
  refine abs_coeff_le_of_mul_separated hψ ?_ i
  intro n
  have h := hB n
  rwa [sepW, det_separated_wronskian] at h

/-- **The height half, `y` side.** -/
theorem abs_coeff_le_of_sepW_right {r : ℕ}
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ ℤ) (ψ : Fin r → MvPolynomial τ ℤ)
    (hφ : mvGenWronskian Dx φ ≠ 0) {B : ℤ}
    (hB : ∀ n, |coeff n (sepW Dx Dy φ ψ)| ≤ B) (j : τ →₀ ℕ) :
    |coeff j (mvGenWronskian Dy ψ)| ≤ B := by
  refine abs_coeff_le_of_mul_separated_right hφ ?_ j
  intro n
  have h := hB n
  rwa [sepW, det_separated_wronskian] at h

/-! ### The key inequality of the step -/

/-- **`r · index P ≤ index U + index V + r·C`** — the induction step's central inequality.

Read: differentiating `P` into its separated Wronskian costs at most `C` of index per entry,
and the Wronskian's index then splits exactly between the two factors.  So a *large* index for
`P` forces a large index for one of `U`, `V`, which is what the induction hypothesis
contradicts.

⚠ **An earlier version of this docstring called this "the inequality the recursion runs on."
That was an overclaim** — see `sum_index_le_index_sepW_concrete` below, which makes the cost
concrete and thereby exposes a reason to doubt that this is the form Roth's lemma needs.

Additive rather than `r·index P − r·C ≤ …` because `WithTop ℚ` has no subtraction, and `⊤`
must survive: a zero `P` gives `⊤` on the left and the statement stays true.

One line from `sum_index_le_index_det_pderivList_add` and `index_sepW`, because `sepW` **is**
that determinant — `rfl` bridges them.  That the composition is a `rfl` is the check that the
two modules were built to the same shape. -/
theorem sum_index_le_index_sepW_add {K : Type*} [CommRing K] [IsDomain K]
    [DecidableEq σ] [DecidableEq τ] {r : ℕ}
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → K) (β : τ → K)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) (C : ℚ)
    (hC : ∀ i j, (((Dx i).map Sum.inl ++ (Dy j).map Sum.inr).map
        (fun k => (1 : ℚ) / ((Sum.elim d₁ d₂) k : ℚ))).sum ≤ C) :
    ∑ _i : Fin r, index (Sum.elim d₁ d₂) (Sum.elim α β)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))
      ≤ (index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ))
        + (((r : ℚ) * C : ℚ) : WithTop ℚ) := by
  classical
  have h := sum_index_le_index_det_pderivList_add (Sum.elim d₁ d₂) (Sum.elim α β)
    (fun i j => (Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
    (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)) C hC
  have hsep : (Matrix.of fun i j =>
      pderivList ((Dx i).map Sum.inl ++ (Dy j).map Sum.inr)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))).det
      = sepW Dx Dy φ ψ := rfl
  rw [hsep, index_sepW] at h
  exact h

/-! ### Making the cost concrete -/

/-- The cost of a mixed operator list splits across the two variable groups. -/
theorem sum_map_inv_append_sumElim (d₁ : σ → ℕ) (d₂ : τ → ℕ) (l1 : List σ) (l2 : List τ) :
    ((l1.map Sum.inl ++ l2.map Sum.inr).map
        (fun k => (1 : ℚ) / ((Sum.elim d₁ d₂ k : ℕ) : ℚ))).sum
      = (l1.map (fun a => (1 : ℚ) / (d₁ a : ℚ))).sum
        + (l2.map (fun b => (1 : ℚ) / (d₂ b : ℚ))).sum := by
  rw [List.map_append, List.sum_append, List.map_map, List.map_map]
  rfl

/-- A concrete bound on the per-entry cost, given operator lists of bounded length and a floor
`D₁`, `D₂` on the two degree vectors. -/
theorem cost_bound_of_bounded_order {r : ℕ} {D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (hx : ∀ i, (Dx i).length ≤ r) (hy : ∀ j, (Dy j).length ≤ r) (i j : Fin r) :
    (((Dx i).map Sum.inl ++ (Dy j).map Sum.inr).map
        (fun k => (1 : ℚ) / ((Sum.elim d₁ d₂ k : ℕ) : ℚ))).sum
      ≤ (r : ℚ) / (D₁ : ℚ) + (r : ℚ) / (D₂ : ℚ) := by
  have hD₁Q : (0 : ℚ) < (D₁ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₁
  have hD₂Q : (0 : ℚ) < (D₂ : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hD₂
  rw [sum_map_inv_append_sumElim]
  refine add_le_add (le_trans (sum_map_inv_le_length_div hD₁ d₁ hd₁ _) ?_)
    (le_trans (sum_map_inv_le_length_div hD₂ d₂ hd₂ _) ?_)
  · exact div_le_div_of_nonneg_right (by exact_mod_cast hx i) hD₁Q.le
  · exact div_le_div_of_nonneg_right (by exact_mod_cast hy j) hD₂Q.le

/-- **The central inequality with the cost made concrete:**

    r · index P  ≤  index U + index V + r²·(1/D₁ + 1/D₂).

⚠⚠ **This is where a problem with the previous docstring's claim becomes visible, and it is
worth stating rather than hiding.**

`r` is the length of a minimal separated representation, so `r ≤ (number of distinct
`x`-monomials of `P`) ≤ d₁ + 1`.  Then `r²/D₁ ≈ d₁`, and the error term is of the same order
as the trivial bound on the index itself.  In that regime the inequality is **true but
useless**.

The classical proof does not have this problem, because it measures the Wronskian's index
against the **Wronskian's own** degree vector — `W` has degree `≤ r·d₁` in `x`, so the weights
used for `index W` are `r·d` rather than `d`.  Every statement in this arc uses one degree
vector `d` throughout, `index_sepW` included.

⚠ So: this inequality is **proved and correct**, and it is **not established** that it is the
form Roth's lemma needs.

The rescaling *tool* now exists — `idxWeight_scale_degree`, `le_index_scale_degree_iff` and
`index_scale_degree_le_iff` in `QOU/Mathlib/RothIndex.lean`, with scale factor `r` supplied by
`degreeOf_mvGenWronskian_le`.  ⚠ But having the tool is not the same as having used it:
nothing below is stated in rescaled weights, and whether the error term actually becomes small
is the recursion's arithmetic.  Nothing here should be read as "the index side of the
induction step is done". -/
theorem sum_index_le_index_sepW_concrete {K : Type*} [CommRing K] [IsDomain K]
    [DecidableEq σ] [DecidableEq τ] {r D₁ D₂ : ℕ} (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : τ → K)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (hx : ∀ i, (Dx i).length ≤ r) (hy : ∀ j, (Dy j).length ≤ r)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) :
    ∑ _i : Fin r, index (Sum.elim d₁ d₂) (Sum.elim α β)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))
      ≤ (index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ))
        + ((((r : ℚ) * ((r : ℚ) / (D₁ : ℚ) + (r : ℚ) / (D₂ : ℚ))) : ℚ) : WithTop ℚ) :=
  sum_index_le_index_sepW_add d₁ d₂ α β Dx Dy φ ψ _
    (cost_bound_of_bounded_order hD₁ hD₂ d₁ d₂ hd₁ hd₂ Dx Dy hx hy)

/-! ### Next

The statement is now written (`QOU/Mathlib/RothLemmaStatement.lean`), its `m = 1` case proved,
and the step's inputs are all constructible (`SeparatedRepresentation`).  With
`sum_index_le_index_sepW_add` above, the step's key *inequality* is proved too.

⚠ What remains is the **recursion**: choosing `ω(m, ε)`, choosing the operator families `Dx`,
`Dy` with bounded order, and doing the arithmetic that turns the inequality plus the induction
hypothesis into a contradiction.

⚠ And the **degree rescaling**, visible from `sum_index_le_index_sepW_concrete`.  The tool is
now in `RothIndex.lean` (`le_index_scale_degree_iff`, `index_scale_degree_le_iff`), but no
statement in this arc is yet phrased in rescaled weights — so the rescaling is *available*,
not *applied*. -/

end MvPolynomial
