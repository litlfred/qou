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
import QOU.Mathlib.RothRecursionArith

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

/-! ### The rescaling, applied -/

/-- **The induction step's inequality with the rescaling applied.**

Given upper bounds on the two factors' indices *in their own degree vectors* — which is the
shape the induction hypothesis produces, since `mvGenWronskian` of `r` functions of degree
`≤ d` has degree `≤ r·d` — and a lower bound `θ` on `index P`, this concludes

    θ ≤ εU + εV + (r/D₁ + r/D₂).

The rescaling is what makes the `εU`, `εV` terms come out un-divided: without it the induction
hypothesis simply does not apply to `U` and `V`, because they are not of degree `d`.

═══ ⚠ THIS CONFIRMS THE SIXTH CORRECTION RATHER THAN RESOLVING IT ═══

The error term is now `r/D₁ + r/D₂`, down a factor `r` from the unscaled
`sum_index_le_index_sepW_concrete`.  **It is still too large.**

`r` is the length of a minimal separated representation, so it is bounded by the number of
distinct monomials in the split-off variable group — of order `D₁`.  Then `r/D₁` is of order
`1`, and Roth's lemma needs a conclusion of the form `index ≤ m·ε` with `ε` small.  An error
of order `1` swamps it.  The `r/D₂` term is worse: under the growth condition the two degree
scales differ by a factor `ω`, so `r/D₂` is of order `ω`.

⚠ Two things to be clear about in that estimate:

* the bound `r ≲ D₁` is **not proved here** — it is a plausible bound on the length of a
  minimal representation, and the magnitude argument rests on it;
* the theorem below is **correct** regardless; what is in question is whether it is *strong
  enough*, which is a statement about constants, not about validity.

So the honest status is unchanged from the sixth correction: the arc has a proved inequality
that is **not established** to yield Roth's lemma, and applying the rescaling did not close
that.  Reconstructing the correct constant bookkeeping needs the actual argument, not more
lemmas — every ingredient here is tight given only "operators have order at most `r`", so the
loss is structural and must be repaired upstream of this statement. -/

theorem index_le_of_rescaled_factor_bounds {K : Type*} [CommRing K] [IsDomain K]
    [DecidableEq σ] [DecidableEq τ] {r D₁ D₂ : ℕ}
    (hr : r ≠ 0) (hD₁ : D₁ ≠ 0) (hD₂ : D₂ ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (hd₁ : ∀ k, D₁ ≤ d₁ k) (hd₂ : ∀ k, D₂ ≤ d₂ k)
    (α : σ → K) (β : τ → K)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (hx : ∀ i, (Dx i).length ≤ r) (hy : ∀ j, (Dy j).length ≤ r)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K)
    (εU εV θ : ℚ)
    (hU : index (fun j => r * d₁ j) α (mvGenWronskian Dx φ) ≤ ((εU : ℚ) : WithTop ℚ))
    (hV : index (fun j => r * d₂ j) β (mvGenWronskian Dy ψ) ≤ ((εV : ℚ) : WithTop ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index (Sum.elim d₁ d₂) (Sum.elim α β)
        (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k))) :
    θ ≤ εU + εV + ((r : ℚ) / (D₁ : ℚ) + (r : ℚ) / (D₂ : ℚ)) := by
  classical
  have hrQ : (0 : ℚ) < (r : ℚ) := by exact_mod_cast Nat.pos_of_ne_zero hr
  set C : ℚ := (r : ℚ) / (D₁ : ℚ) + (r : ℚ) / (D₂ : ℚ) with hC
  -- rescaled factor bounds, pushed back to the unscaled weights
  have hU' : index d₁ α (mvGenWronskian Dx φ) ≤ (((r : ℚ) * εU : ℚ) : WithTop ℚ) :=
    (index_scale_degree_le_iff hr d₁ α _ εU).mp hU
  have hV' : index d₂ β (mvGenWronskian Dy ψ) ≤ (((r : ℚ) * εV : ℚ) : WithTop ℚ) :=
    (index_scale_degree_le_iff hr d₂ β _ εV).mp hV
  -- the step's inequality
  have hkey := sum_index_le_index_sepW_concrete hD₁ hD₂ d₁ d₂ hd₁ hd₂ α β Dx Dy hx hy φ ψ
  -- the assumed lower bound, summed
  have hsum : (((r : ℚ) * θ : ℚ) : WithTop ℚ)
      ≤ ∑ _i : Fin r, index (Sum.elim d₁ d₂) (Sum.elim α β)
          (∑ k, (rename Sum.inl (φ k) : MvPolynomial (σ ⊕ τ) K) * rename Sum.inr (ψ k)) := by
    have h := Finset.sum_le_sum (s := (Finset.univ : Finset (Fin r)))
      (f := fun _ => ((θ : ℚ) : WithTop ℚ)) (fun _ _ => hθ)
    rwa [Finset.sum_const, Finset.card_univ, Fintype.card_fin, nsmul_coe_withTop] at h
  -- chain
  have hchain : (((r : ℚ) * θ : ℚ) : WithTop ℚ)
      ≤ ((((r : ℚ) * εU + (r : ℚ) * εV) + (r : ℚ) * C : ℚ) : WithTop ℚ) := by
    refine le_trans hsum (le_trans hkey ?_)
    rw [WithTop.coe_add, WithTop.coe_add]
    exact add_le_add (add_le_add hU' hV') le_rfl
  rw [WithTop.coe_le_coe] at hchain
  have : (r : ℚ) * θ ≤ (r : ℚ) * (εU + εV + C) := by linarith
  exact le_of_mul_le_mul_left this hrQ

/-! ### The square-root conclusion — what the sixth correction was missing

`index_le_of_rescaled_factor_bounds` above is the *linear* shape: it divides the summed
inequality through by `r` and reads off `θ ≤ εU + εV + C`.  The sixth correction recorded
that this is not strong enough, and the reading of Mahler §13 says why: dividing through
linearly throws away the fact that the per-column cost **grows with the column**.

Mahler's argument instead splits on the cut-off `N = ⌊(J(A) − t)·r⌋ + 1` — the column past
which `t + ν/r` already exceeds the index, so the column contributes nothing.  Keeping the
truncation gives a sum of `r` terms of which only the first `N` are positive, and estimating
*that* gives a bound on `(θ − t)²`, not on `θ − t`.  The square root is the whole gain.

`sq_index_le_of_det_bound` is that conclusion, assembled from two halves proved separately:

* `sum_max_le_index_det` (`QOU/Mathlib/WronskianIndex.lean`) — index side, `WithTop ℚ`,
  turns `index_det_ge` plus a growing per-column cost into `∑_{ν<r} max(0, θ−t−ν/rr)`;
* `RothArith.sq_mul_le_two_mul_of_sum_le` (`QOU/Mathlib/RothRecursionArith.lean`) — pure
  rational arithmetic, turns a bound on that truncated sum into `(θ−t)² · rr ≤ 2S`.

⚠ **Provenance caveat.**  The constants in `RothRecursionArith` were reconstructed from a
partly illegible scan of Mahler §13, and the numeric bookkeeping should still be re-derived
against a clean copy.  The *shape* — truncated sum, square-root conclusion — is what the
source shows and what is proved here.

The two downstream constants this used to defer are no longer open: §11 gives `ω = 1/t` and
§14 gives `c_m = 2^{m+1} − 3` with conclusion `Θ_m ≤ c_m·t^{2^{−(m−1)}}`, both read from the
page scans.  ⚠ The value recorded here, `2^m − 3`, was wrong.

⚠ This does **not** yet make the recursion run.  It replaces a shape that was known to be too
weak with one that is the right shape; whether the resulting constants close the induction is
the next thing to check, and is a question about `ω`, not about these two halves. -/

/-- **The square-root bound.**  With a lower bound `θ` on `index P`, per-column operator costs
bounded by `t + j/rr`, and an upper bound `S` on the index of the determinant, the excess
`θ − t` satisfies `(θ − t)² · rr ≤ 2S`.

The hypothesis `hn : (θ − t)·rr ≤ r` is Mahler's "the cut-off falls inside the matrix" — it
says the determinant has at least as many columns as the truncation needs.  Without it the
sum over `Fin r` is missing positive terms and the conclusion is false. -/
theorem sq_index_le_of_det_bound {R : Type*} [CommRing R] [DecidableEq σ] {r : ℕ}
    (d : σ → ℕ) (α : σ → R)
    (D : Fin r → Fin r → List σ) (P : MvPolynomial σ R) (θ t rr S : ℚ)
    (hrr : 0 < rr) (hθt : t ≤ θ) (hn : (θ - t) * rr ≤ (r : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P)
    (hc : ∀ i j : Fin r,
      ((D i j).map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ t + (j : ℚ) / rr)
    (hS : index d α (Matrix.of fun i j => pderivList (D i j) P).det
      ≤ ((S : ℚ) : WithTop ℚ)) :
    (θ - t) ^ 2 * rr ≤ 2 * S := by
  have hbridge := sum_max_le_index_det d α D P θ t rr hθ hc
  have hsum : (∑ j : Fin r, max 0 (θ - t - (j : ℚ) / rr) : ℚ) ≤ S := by
    have h := le_trans hbridge hS
    exact_mod_cast h
  rw [Fin.sum_univ_eq_sum_range (fun ν => max 0 (θ - t - (ν : ℚ) / rr)) r] at hsum
  exact RothArith.sq_mul_le_two_mul_of_sum_le hrr (by linarith) hn hsum



/-- **Satisfiability of `sq_index_le_of_det_bound`.**  One variable, unit weight, the origin,
`P = X₀`, a `1 × 1` matrix whose only operator list is empty: `θ = 1`, `t = 0`, `rr = 1`,
`S = 1`, and the conclusion reads `1 ≤ 2`.

⚠ Read this for what it is.  It certifies that the four hypotheses are **jointly
satisfiable** — a stack of side conditions that silently contradict each other would make the
theorem vacuous, and this rules that out.  It does **not** exercise the truncation: with
`r = 1` there is only one column and nothing is clipped.  The guard for the truncation itself
is `RothArith.sum_max_truncation_active`, where it is cheap to state exactly. -/
theorem sq_index_le_of_det_bound_witness : ((1 : ℚ) - 0) ^ 2 * 1 ≤ 2 * 1 :=
  sq_index_le_of_det_bound (σ := Fin 1) (R := ℚ) (r := 1)
    (fun _ => 1) (fun _ => (0 : ℚ)) (fun _ _ => []) (X 0) 1 0 1 1
    one_pos (by norm_num) (by norm_num)
    (by rw [index_X])
    (by intro i j; simp)
    (by
      rw [Matrix.det_fin_one]
      show index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        (pderivList ([] : List (Fin 1)) (X 0 : MvPolynomial (Fin 1) ℚ))
          ≤ (((1 : ℚ)) : WithTop ℚ)
      rw [pderivList_nil]
      show index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        (X 0 : MvPolynomial (Fin 1) ℚ) ≤ (((1 : ℚ)) : WithTop ℚ)
      rw [index_X])


/-- **Mahler §13, case (1).**  `θ ≤ t + S`, with no hypothesis relating `θ`, `rr` and `r`.

The source presents this as the case `n ≤ N`, which invites formalising a hypothesis that is
not needed: the bound is just the `j = 0` term of `sum_max_le_index_det`, and every other
term is non-negative.  It holds in **every** regime.  (What the case `n ≤ N` really says is
that in that regime this is the *best* bound available — a statement about strength, not
about validity.)

Needs `0 < r` only so that column `0` exists; at `r = 0` the determinant is `1` and carries
no information about `P`. -/
theorem index_le_add_of_det_bound {R : Type*} [CommRing R] [DecidableEq σ] {r : ℕ}
    (d : σ → ℕ) (α : σ → R)
    (D : Fin r → Fin r → List σ) (P : MvPolynomial σ R) (θ t rr S : ℚ)
    (hr : 0 < r)
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P)
    (hc : ∀ i j : Fin r,
      ((D i j).map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ t + (j : ℚ) / rr)
    (hS : index d α (Matrix.of fun i j => pderivList (D i j) P).det
      ≤ ((S : ℚ) : WithTop ℚ)) :
    θ ≤ t + S := by
  have hsum : (∑ j : Fin r, max 0 (θ - t - (j : ℚ) / rr) : ℚ) ≤ S := by
    have h := le_trans (sum_max_le_index_det d α D P θ t rr hθ hc) hS
    exact_mod_cast h
  have hfirst : max 0 (θ - t - ((⟨0, hr⟩ : Fin r) : ℚ) / rr)
      ≤ ∑ j : Fin r, max 0 (θ - t - (j : ℚ) / rr) :=
    Finset.single_le_sum (f := fun j : Fin r => max 0 (θ - t - (j : ℚ) / rr))
      (fun i _ => le_max_left _ _) (Finset.mem_univ _)
  have hz : ((⟨0, hr⟩ : Fin r) : ℚ) = 0 := by norm_num
  rw [hz] at hfirst
  have : θ - t ≤ max 0 (θ - t - 0 / rr) := by
    rw [zero_div, sub_zero]
    exact le_max_right _ _
  linarith

/-- **The reusable half of `index_le_of_rescaled_factor_bounds`.**

That theorem's *rescaling* is correct and is what the source's `p_h = n·r_h` does; only the
linear conclusion drawn from it was too weak (correction 6).  This isolates the rescaling:
bounds on the two Wronskians' indices **at the rescaled degrees** give a bound on their sum at
the unscaled ones, with the factor `r` the recursion needs.

⚠ The factor `r` in the conclusion is the source's `J(W) ≤ n·Φ_m`, and it is not slack: it
cancels against the `S/r` in §13's conclusion.  A version without it would be asking the
induction hypothesis for something strictly stronger than it can give. -/
theorem factor_bound_of_rescaled {K : Type*} [CommRing K] {r : ℕ} (hr : r ≠ 0)
    (d₁ : σ → ℕ) (d₂ : τ → ℕ) (α : σ → K) (β : τ → K)
    (Dx : Fin r → List σ) (Dy : Fin r → List τ)
    (φ : Fin r → MvPolynomial σ K) (ψ : Fin r → MvPolynomial τ K) (εU εV : ℚ)
    (hU : index (fun j => r * d₁ j) α (mvGenWronskian Dx φ) ≤ ((εU : ℚ) : WithTop ℚ))
    (hV : index (fun j => r * d₂ j) β (mvGenWronskian Dy ψ) ≤ ((εV : ℚ) : WithTop ℚ)) :
    index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ)
      ≤ ((((r : ℚ) * (εU + εV) : ℚ)) : WithTop ℚ) := by
  have hU' := (index_scale_degree_le_iff hr d₁ α _ εU).mp hU
  have hV' := (index_scale_degree_le_iff hr d₂ β _ εV).mp hV
  calc index d₁ α (mvGenWronskian Dx φ) + index d₂ β (mvGenWronskian Dy ψ)
      ≤ ((((r : ℚ) * εU : ℚ)) : WithTop ℚ) + ((((r : ℚ) * εV : ℚ)) : WithTop ℚ) :=
        add_le_add hU' hV'
    _ = ((((r : ℚ) * (εU + εV) : ℚ)) : WithTop ℚ) := by
        rw [← WithTop.coe_add]
        congr 1
        ring


/-! ### ⚠ Corrections eight and nine — the second one corrects the first

**Correction 8, as recorded:** §13's combined display, transcribed as `θ ≤ t + 2·max S q`,
says nothing, since `2·max S q ≥ 2S ≥ S` makes it a consequence of `index_le_add_of_det_bound`
(`θ ≤ t + S`).  `max_form_implied_by_case_one` below is that one-line proof and it stands.

**Correction 9: the transcription was wrong, and so was the conclusion drawn from it.**  The
source's first branch is not `J(W)` but **`J(W)/n`** — the combined display reads

    J(A) < t + 2 max( J(W)/n , √(J(W)/r_m) ).

Correction 8 concluded from the vacuous form that "Mahler's `max` is an artefact of his case
split" and that the strong branch should be extracted alone.  **That was wrong.**  With the
`1/n` restored:

* the combined statement is **not** implied by `θ ≤ t + S` — `2S/n` can be far smaller than
  `S`, and in the application it is: `S` is of size `n·Φ_m`, so `2S/n` is of size `Φ_m`;
* case (1) is genuinely useful, so the `max` is combining two *useful* bounds rather than
  hedging a useless one against a strong one;
* and the two branches are **complementary by construction**, so the combination needs no
  side condition at all.

The cost of the error was a real one: `index_le_of_det_bound` below carries the hypothesis
`S·rr ≤ r`, introduced to force the strong branch because case (1) looked worthless.  In the
recursion's regime that condition reads `Φ_m·r_m ≤ 1`, which is **false** — `Φ_m` is small but
`r_m` is a large degree.  So the theorem is sound and its hypothesis is unsatisfiable where it
matters.  `index_le_two_mul_max_of_det_bound` replaces it and assumes nothing of the kind.

⚠ How this was caught: by taking the *next* step seriously — "check `S·rr ≤ r` against the
parameter conditions" — instead of carrying it as a caveat.  The check failed, and tracing why
found the mis-transcription.  A side condition nobody tests is indistinguishable from a bug.

⚠ And what did **not** catch it: `lake build`, `#print axioms`, and the non-vacuity witnesses.
The witnesses were all at `r = 1` or `r = 2`, where `S·rr ≤ r` is satisfiable; the hypothesis
only becomes unsatisfiable in the asymptotic regime, which no finite witness reaches. -/

/-- The vacuous `max` form, derived from the unsharpened case (1) alone.

⚠ This is a record of correction 8, and correction 9 explains what it does **not** show: the
source's combined display has `J(W)/n` in the first branch, and *that* form is not derivable
this way.  Nothing should use this theorem; it exists so the mis-transcription stays visible
rather than being quietly deleted. -/
theorem max_form_implied_by_case_one {θ t S q : ℚ} (hS0 : 0 ≤ S) (h : θ ≤ t + S) :
    θ ≤ t + 2 * max S q := by
  have := le_max_left S q
  linarith

/-- ⚠ **Superseded by `index_le_two_mul_max_of_det_bound`.**  `θ ≤ t + 2q` whenever
`q ≥ √(S/rr)` (stated as `S ≤ q²·rr`) and `S·rr ≤ r`.

The theorem is true.  Its hypothesis `S·rr ≤ r` is the problem: it was introduced to force
§13's second branch, on the mistaken belief (correction 8) that the first branch was
worthless, and in the recursion's regime it reads `Φ_m·r_m ≤ 1` and is **false**.  Kept as the
record of correction 9; use the `max` form instead. -/
theorem index_le_of_det_bound {R : Type*} [CommRing R] [DecidableEq σ] {r : ℕ}
    (d : σ → ℕ) (α : σ → R)
    (D : Fin r → Fin r → List σ) (P : MvPolynomial σ R) (θ t rr S q : ℚ)
    (hr : 0 < r) (hrr : 0 < rr) (hθt : t ≤ θ) (hq0 : 0 ≤ q)
    (hq : S ≤ q ^ 2 * rr) (hSr : S * rr ≤ (r : ℚ))
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P)
    (hc : ∀ i j : Fin r,
      ((D i j).map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ t + (j : ℚ) / rr)
    (hS : index d α (Matrix.of fun i j => pderivList (D i j) P).det
      ≤ ((S : ℚ) : WithTop ℚ)) :
    θ ≤ t + 2 * q := by
  have h1 : θ - t ≤ S := by
    have := index_le_add_of_det_bound d α D P θ t rr S hr hθ hc hS
    linarith
  have hn : (θ - t) * rr ≤ (r : ℚ) :=
    le_trans (by nlinarith) hSr
  have h2 := sq_index_le_of_det_bound d α D P θ t rr S hrr hθt hn hθ hc hS
  have hsq : (θ - t) ^ 2 ≤ (2 * q) ^ 2 := by nlinarith
  nlinarith [sq_nonneg (θ - t - 2 * q)]

/-- **Satisfiability of `index_le_of_det_bound`.**  The same `1 × 1` instance as
`sq_index_le_of_det_bound_witness`, with `S = 1`, `rr = 1`, `r = 1`, `q = 1`: the side
condition `S·rr ≤ r` reads `1 ≤ 1` and the conclusion reads `1 ≤ 2`.

⚠ As before, this certifies joint satisfiability only — it does not exercise the truncation,
and at `q = S = 1` the two branches happen to agree. -/
theorem index_le_of_det_bound_witness : (1 : ℚ) ≤ 0 + 2 * 1 :=
  index_le_of_det_bound (σ := Fin 1) (R := ℚ) (r := 1)
    (fun _ => 1) (fun _ => (0 : ℚ)) (fun _ _ => []) (X 0) 1 0 1 1 1
    one_pos one_pos (by norm_num) (by norm_num) (by norm_num) (by norm_num)
    (by rw [index_X])
    (by intro i j; simp)
    (by
      rw [Matrix.det_fin_one]
      show index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        (pderivList ([] : List (Fin 1)) (X 0 : MvPolynomial (Fin 1) ℚ))
          ≤ (((1 : ℚ)) : WithTop ℚ)
      rw [pderivList_nil]
      show index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        (X 0 : MvPolynomial (Fin 1) ℚ) ≤ (((1 : ℚ)) : WithTop ℚ)
      rw [index_X])



/-- **Mahler §13, combined — the real form, and it needs no side condition.**

    θ ≤ t + 2 · max ( S/r , q )        for any `q` with `S ≤ q²·rr`.

Both branches are useful and they are complementary by construction:

* if `(r−1)/rr ≤ θ − t` the cut-off falls outside the matrix, every column contributes, and
  Gauss's sum eats half of them — `θ − t ≤ 2S/r`;
* otherwise `(θ−t)·rr < r`, which is exactly the hypothesis of `sq_index_le_of_det_bound`, and
  that gives `θ − t ≤ √(2S/rr) ≤ 2q`.

The `1/r` in the first branch is what makes it worth having: in the application `S` is of
size `r·Φ`, so `S/r` is of size `Φ`.  Dropping it — which is what `index_le_add_of_det_bound`
does, keeping only the `j = 0` term — gives a bound of size `r·Φ` and is useless.  That was
correction 9.

⚠ Compare `index_le_of_det_bound` above, which reaches `θ ≤ t + 2q` but needs `S·rr ≤ r`.
This needs nothing, and is weaker only by the `max` — which costs nothing, since `S/r` is
itself a good bound. -/
theorem index_le_two_mul_max_of_det_bound {R : Type*} [CommRing R] [DecidableEq σ] {r : ℕ}
    (d : σ → ℕ) (α : σ → R)
    (D : Fin r → Fin r → List σ) (P : MvPolynomial σ R) (θ t rr S q : ℚ)
    (hr : 0 < r) (hrr : 0 < rr) (hθt : t ≤ θ) (hq0 : 0 ≤ q) (hq : S ≤ q ^ 2 * rr)
    (hθ : ((θ : ℚ) : WithTop ℚ) ≤ index d α P)
    (hc : ∀ i j : Fin r,
      ((D i j).map (fun k => (1 : ℚ) / (d k : ℚ))).sum ≤ t + (j : ℚ) / rr)
    (hS : index d α (Matrix.of fun i j => pderivList (D i j) P).det
      ≤ ((S : ℚ) : WithTop ℚ)) :
    θ ≤ t + 2 * max (S / (r : ℚ)) q := by
  have hbridge := sum_max_le_index_det d α D P θ t rr hθ hc
  have hsum : (∑ j : Fin r, max 0 (θ - t - (j : ℚ) / rr) : ℚ) ≤ S := by
    have h := le_trans hbridge hS
    exact_mod_cast h
  rw [Fin.sum_univ_eq_sum_range (fun ν => max 0 (θ - t - (ν : ℚ) / rr)) r] at hsum
  have h := RothArith.le_two_mul_max_of_sum_le hrr (by linarith) hq0 hq hr hsum
  linarith

/-- **Satisfiability of the `max` form**, on the same `1 × 1` instance: `θ = 1`, `t = 0`,
`rr = 1`, `S = 1`, `q = 1`, conclusion `1 ≤ 0 + 2·max 1 1 = 2`.

⚠ Note what this cannot test.  The distinction between this theorem and the superseded
`index_le_of_det_bound` is asymptotic — the latter's `S·rr ≤ r` is satisfiable at every small
`r` and only fails in the regime the recursion runs in.  No finite witness separates them;
that is why correction 9 needed the parameter check rather than another example. -/
theorem index_le_two_mul_max_of_det_bound_witness : (1 : ℚ) ≤ 0 + 2 * max (1 / (1 : ℚ)) 1 :=
  index_le_two_mul_max_of_det_bound (σ := Fin 1) (R := ℚ) (r := 1)
    (fun _ => 1) (fun _ => (0 : ℚ)) (fun _ _ => []) (X 0) 1 0 1 1 1
    Nat.one_pos one_pos (by norm_num) (by norm_num) (by norm_num)
    (by rw [index_X])
    (by intro i j; simp)
    (by
      rw [Matrix.det_fin_one]
      show index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        (pderivList ([] : List (Fin 1)) (X 0 : MvPolynomial (Fin 1) ℚ))
          ≤ (((1 : ℚ)) : WithTop ℚ)
      rw [pderivList_nil]
      show index (fun _ : Fin 1 => 1) (fun _ : Fin 1 => (0 : ℚ))
        (X 0 : MvPolynomial (Fin 1) ℚ) ≤ (((1 : ℚ)) : WithTop ℚ)
      rw [index_X])

/-! ### Next

**§13 is complete.**  `index_le_of_det_bound` is its conclusion in a form the recursion can
apply: given a matrix of derivatives of `P` whose per-column cost is `t + j/rr`, an upper
bound `S` on the determinant's index with `S·rr ≤ r`, and a rational `q ≥ √(S/rr)`, the index
of `P` is at most `t + 2q`.  Every hypothesis is checkable without knowing the index of `P`.

What that leaves is **not** more inequalities.  It is two constructions and one check:

1. **The operator family.**  §13's matrix is `A_{μν} = Δ_{j_{μ1},…,j_{μ,m−1}, ν−1}` with
   `∑_{h<m} j_{μh} ≤ μ−1` and order exactly `ν−1` in the last variable.  Building that as a
   `D : Fin r → Fin r → List σ` and proving `hc` for it is a construction the arc does not
   have.  Note it is `t + j/rr` with the cost *uniform in the row* — which is what makes the
   permutation step in `sum_max_le_index_det` sound, so this is not a free choice.
2. **The determinant is non-zero.**  `hS` is unsatisfiable when `det = 0` (`index = ⊤`), so
   the generalized Wronskian's non-vanishing — `BoundedOrderWronskian`'s business — is a real
   precondition, not bookkeeping.
3. **`S·rr ≤ r` in the recursion's regime.**  With `S = n·Φ_m`, `rr = r_m`, `r = n` this is
   `Φ_m · r_m ≤ 1`.  Whether the parameter conditions of Roth's lemma deliver it is unchecked.

⚠ Provenance, still standing for `RothRecursionArith`'s numeric constants: reconstructed from
a partly illegible scan, and worth re-deriving against a clean copy.  §13's *structure* has
since been read directly and matches — the matrix shape, the uniform-in-row cost, and the
weakening of `√2` to `2` are all confirmed.

The surrounding parameter bookkeeping has now been read too: §11 gives `ω = 1/t`, §14 gives
`c_m = 2^{m+1} − 3` and the conclusion `Θ_m ≤ c_m·t^{2^{−(m−1)}}`.  ⚠ The `2^m − 3` this
paragraph recorded was wrong; `RothLemmaStatement.rothConstant` carries the right value with
its recurrence and base case checked against each other. -/

end MvPolynomial
