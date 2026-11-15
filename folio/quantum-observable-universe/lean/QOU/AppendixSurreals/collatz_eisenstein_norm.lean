import Mathlib.Tactic

/-!
# The Eisenstein norm on the q-Collatz backward tree

This file supplies the two arithmetic inputs that the unit-obstruction engine in
`QOU.AppendixSurreals.CollatzBlockDescent` is applied to, and which that file
records as *argued, not formalized*:

* the **branch norm formula** `N(Q_k(w)) = 1 + 6k + 12k²`, and
* the **tree-structure induction** — every node of the backward tree from the
  attractor lies either on the main even chain or on a bare `k ≥ 1` branch.

Together with the engine (`evenSubtree_no_oddPreimage`) they give the tree-level
conclusion: **no two chained odd-preimages occur in the backward tree**, i.e. no
`v = 0` block occurs there.

## What is proved here, and over what

Almost everything below is an *identity* over an arbitrary `CommRing R` carrying
an element `w` with `w² + w + 1 = 0`; those lemmas carry no side hypotheses.

The two statements that genuinely need `ℤ[ω]`-like arithmetic — that a norm-`n`
element with `n ≠ ±1` is a non-unit, and that the coordinates `(x, y)` of
`x + y·w` are determined — are isolated behind the explicit hypothesis

    hindep : ∀ x y : ℤ, (x : R) + (y : R) * w = 0 → x = 0 ∧ y = 0

("`1` and `w` are `ℤ`-independent in `R`"). That holds in `ℤ[ω]` and in `ℂ`; it
fails in, say, `ZMod 3`. It is a hypothesis on the ambient ring, not a
conjecture: nothing here is axiomatized, and no `sorry` appears in this file.

## Scope (per the repo's (a)/(b) refutation discipline)

The conclusion is a **structural exclusion** for the backward tree — the
obstruction is a proved invariant (the Eisenstein norm), not a numerical
near-miss. But its *scope* is the backward tree only. The step from "no `v = 0`
block in the backward tree" to "no `v = 0` block in `D∞`" is the convergence
conjecture itself (`qcz7` A1) and is **not** claimed.

## Ref

-- Ref: [leitner2026] Appendix (surreals), q-Collatz arc; the arithmetic is
-- checked independently in `computations/qcollatz_backward_tree_structure_probe.py`.
-/

namespace QOU.AppendixSurreals.CollatzEisenstein

variable {R : Type*} [CommRing R]

/-! ### The Eisenstein coordinates -/

/-- `eis x y = x + y·w`, the element of `R` with Eisenstein coordinates
`(x, y)` relative to the cube root `w`. -/
def eis (w : R) (x y : ℤ) : R := (x : R) + (y : R) * w

/-- The integral norm form `N(x + y·w) = x² - xy + y²`. -/
def eisNorm (x y : ℤ) : ℤ := x ^ 2 - x * y + y ^ 2

@[simp] theorem eis_zero (w : R) : eis w 0 0 = 0 := by simp [eis]

@[simp] theorem eis_one (w : R) : eis w 1 0 = 1 := by simp [eis]

/-- Multiplication in Eisenstein coordinates. Uses `w² = -1 - w`. -/
theorem eis_mul (w : R) (hw : w ^ 2 + w + 1 = 0) (x y x' y' : ℤ) :
    eis w x y * eis w x' y' = eis w (x * x' - y * y') (x * y' + y * x' - y * y') := by
  simp only [eis, Int.cast_sub, Int.cast_add, Int.cast_mul]
  linear_combination ((y : R) * (y' : R)) * hw

/-- The norm form is multiplicative — a pure identity in `ℤ`, matching
`eis_mul`. -/
theorem eisNorm_mul (x y x' y' : ℤ) :
    eisNorm (x * x' - y * y') (x * y' + y * x' - y * y') = eisNorm x y * eisNorm x' y' := by
  simp only [eisNorm]; ring

/-- The Eisenstein conjugate of `x + y·w` is `(x - y) - y·w`. -/
theorem eis_mul_conj (w : R) (hw : w ^ 2 + w + 1 = 0) (x y : ℤ) :
    eis w x y * eis w (x - y) (-y) = ((eisNorm x y : ℤ) : R) := by
  rw [eis_mul w hw]
  simp only [eis, eisNorm, Int.cast_sub, Int.cast_add, Int.cast_mul, Int.cast_neg,
    Int.cast_pow]
  ring

/-! ### The unit `α = w + 1` -/

/-- `α = w + 1` in Eisenstein coordinates. -/
theorem eis_alpha (w : R) : eis w 1 1 = w + 1 := by simp [eis]; ring

/-- `N(α) = 1`: the even branch-inverse is norm-preserving. -/
@[simp] theorem eisNorm_alpha : eisNorm 1 1 = 1 := by decide

/-- `(w + 1)³ = -1`. -/
theorem alpha_pow_three (w : R) (hw : w ^ 2 + w + 1 = 0) : (w + 1) ^ 3 = -1 := by
  linear_combination (w + 2) * hw

/-- **`α = w + 1` has multiplicative order dividing 6** — this is the source of
the `6` in the observed mod-6 congruence along the main even chain. -/
theorem alpha_pow_six (w : R) (hw : w ^ 2 + w + 1 = 0) : (w + 1) ^ 6 = 1 := by
  have h := alpha_pow_three w hw
  calc (w + 1) ^ 6 = ((w + 1) ^ 3) ^ 2 := by ring
    _ = (-1 : R) ^ 2 := by rw [h]
    _ = 1 := by ring

/-! ### The coupled recursion along the even chain

The even branch-inverse is `P ↦ (q+1)·P`. Evaluating at `w` and differentiating,
the pair `(u, v) = (P(w), P'(w))` transforms as `(u, v) ↦ (α·u, u + α·v)`. -/

/-- The chain data after `n` even branch-inverses, as an explicit pair. -/
def chainData (w u0 v0 : R) : ℕ → R × R
  | 0 => (u0, v0)
  | n + 1 => ((w + 1) * (chainData w u0 v0 n).1,
              (chainData w u0 v0 n).1 + (w + 1) * (chainData w u0 v0 n).2)

@[simp] theorem chainData_zero (w u0 v0 : R) : chainData w u0 v0 0 = (u0, v0) := rfl

@[simp] theorem chainData_succ (w u0 v0 : R) (n : ℕ) :
    chainData w u0 v0 (n + 1) =
      ((w + 1) * (chainData w u0 v0 n).1,
       (chainData w u0 v0 n).1 + (w + 1) * (chainData w u0 v0 n).2) := rfl

/-- The evaluation half is a pure geometric progression: `u_n = αⁿ·u₀`. -/
theorem chainData_fst (w u0 v0 : R) : ∀ n : ℕ,
    (chainData w u0 v0 n).1 = (w + 1) ^ n * u0 := by
  intro n
  induction n with
  | zero => simp
  | succ n ih => simp [ih]; ring

/-- **The closed form for the derivative**, `α·v_n = α^(n+1)·v₀ + n·αⁿ·u₀`.
Multiplying by the unit `α` clears the `αⁿ⁻¹`, so this holds over any
`CommRing` with no invertibility side condition. -/
theorem chainData_snd (w u0 v0 : R) : ∀ n : ℕ,
    (w + 1) * (chainData w u0 v0 n).2
      = (w + 1) ^ (n + 1) * v0 + (n : R) * (w + 1) ^ n * u0 := by
  intro n
  induction n with
  | zero => simp
  | succ n ih =>
    rw [chainData_succ, chainData_fst]
    push_cast
    linear_combination ((w : R) + 1) * ih

/-! ### The main chain and its `k`-th branch

Along the main even chain from the attractor `1 + q⁻¹` one has
`u₀ = v₀ = -w`, so at `n = 6k` (where `α^n = 1`) the data is

    u_(6k) = -w,        v_(6k) = -6k - (6k+1)·w.

Differentiating the odd-branch relation `[3]_q·Q = [2]_q·P - 1` at `w`, where
`[3]_q` vanishes, gives `(2w + 1)·Q(w) = P(w) + (w+1)·P'(w)`. -/

/-- The evaluation at the `n = 6k` node of the main even chain. -/
def chainEval (w : R) : R := -w

/-- The derivative at the `n = 6k` node of the main even chain,
`-6k - (6k+1)·w`. -/
def chainDeriv (w : R) (k : ℕ) : R := eis w (-(6 * k)) (-(6 * k + 1))

/-- The evaluation of the odd-preimage taken at the `n = 6k` node,
`-(4k+1) - (2k+1)·w`. -/
def branchEval (w : R) (k : ℕ) : R := eis w (-(4 * k + 1)) (-(2 * k + 1))

/-- **The main chain has the right data at `n = 6k`.** With `u₀ = v₀ = -w`,
the closed form `chainData_snd` reproduces `chainDeriv` at `n = 6k`. -/
theorem chainData_at_six_mul (w : R) (hw : w ^ 2 + w + 1 = 0) (k : ℕ) :
    (chainData w (-w) (-w) (6 * k)).1 = chainEval w ∧
    (w + 1) * (chainData w (-w) (-w) (6 * k)).2 = (w + 1) * chainDeriv w k := by
  have h6 : (w + 1) ^ (6 * k) = 1 := by
    rw [pow_mul, alpha_pow_six w hw, one_pow]
  constructor
  · rw [chainData_fst, h6]; simp [chainEval]
  · rw [chainData_snd, h6]
    have h7 : (w + 1) ^ (6 * k + 1) = w + 1 := by
      rw [pow_succ, h6, one_mul]
    rw [h7]
    simp only [chainDeriv, eis]
    push_cast
    linear_combination ((6 : R) * k) * hw

/-- **The derivative relation at the branch node.** The odd-preimage evaluation
`branchEval w k` satisfies `(2w + 1)·Q(w) = P(w) + (w+1)·P'(w)` with
`P(w) = chainEval w` and `P'(w) = chainDeriv w k`.

This is the identity the probe verifies numerically; here it is a `ring`
identity modulo `w² + w + 1 = 0`. -/
theorem branch_deriv_relation (w : R) (hw : w ^ 2 + w + 1 = 0) (k : ℕ) :
    (2 * w + 1) * branchEval w k = chainEval w + (w + 1) * chainDeriv w k := by
  simp only [branchEval, chainEval, chainDeriv, eis]
  push_cast
  linear_combination (2 * (k : R) - 1) * hw

/-! ### The norm formula — `qou-btil` -/

/-- **The branch-norm formula.** The odd-preimage taken at the `n = 6k` node of
the main even chain lands on an evaluation of Eisenstein norm

    N(Q_k(w)) = 1 + 6k + 12k².

Pure arithmetic in `ℤ` on the coordinates `(-(4k+1), -(2k+1))`. -/
theorem branch_norm (k : ℕ) :
    eisNorm (-(4 * (k : ℤ) + 1)) (-(2 * (k : ℤ) + 1)) = 1 + 6 * k + 12 * k ^ 2 := by
  simp only [eisNorm]; ring

/-- **The norm is `1` only on the main chain.** For `k ≥ 1` the branch norm
exceeds `1`, so the branch evaluation is not a unit of `ℤ[ω]`. -/
theorem branch_norm_eq_one_iff (k : ℕ) :
    eisNorm (-(4 * (k : ℤ) + 1)) (-(2 * (k : ℤ) + 1)) = 1 ↔ k = 0 := by
  rw [branch_norm]
  constructor
  · intro h
    by_contra hk
    have hk1 : 1 ≤ (k : ℤ) := by exact_mod_cast Nat.one_le_iff_ne_zero.mpr hk
    nlinarith [sq_nonneg ((k : ℤ))]
  · rintro rfl; norm_num

/-- The branch norm is at least `19` once `k ≥ 1` — the first branch already
misses `1` by a wide margin, which is why the obstruction is structural rather
than marginal. -/
theorem branch_norm_ge (k : ℕ) (hk : 1 ≤ k) :
    19 ≤ eisNorm (-(4 * (k : ℤ) + 1)) (-(2 * (k : ℤ) + 1)) := by
  rw [branch_norm]
  have hk1 : 1 ≤ (k : ℤ) := by exact_mod_cast hk
  nlinarith

/-! ### The tree-structure induction — `qou-ky5e` -/

/-- **Norm-`1` is necessary for a unit.** If `eis w x y` is a unit whose inverse
also has integral coordinates, the norm form takes the value `±1`.

Stated in the form actually used: a factorisation of `1` in Eisenstein
coordinates forces `N(x,y)` to divide `1`. -/
theorem eisNorm_dvd_one_of_mul_eq_one (w : R) (hw : w ^ 2 + w + 1 = 0)
    (hindep : ∀ x y : ℤ, (x : R) + (y : R) * w = 0 → x = 0 ∧ y = 0)
    (x y x' y' : ℤ) (h : eis w x y * eis w x' y' = 1) :
    eisNorm x y ∣ 1 := by
  rw [eis_mul w hw] at h
  have h0 : eis w (x * x' - y * y' - 1) (x * y' + y * x' - y * y') = 0 := by
    simp only [eis] at h ⊢
    push_cast at h ⊢
    linear_combination h
  obtain ⟨ha, hb⟩ := hindep _ _ h0
  have hx : x * x' - y * y' = 1 := by linarith
  refine ⟨eisNorm x' y', ?_⟩
  have hmul := eisNorm_mul x y x' y'
  rw [hx, hb] at hmul
  simpa [eisNorm] using hmul

/-- **The branch evaluation is not a unit, for every `k ≥ 1`.**

This is the missing arithmetic input to the unit-obstruction engine
`CollatzBlockDescent.evenSubtree_no_oddPreimage`: the engine shows that a
non-unit evaluation blocks odd-preimages through the entire even subtree, but
does not itself establish that the `k ≥ 1` branch evaluations are non-units.
The Eisenstein norm supplies exactly that. -/
theorem branchEval_not_isUnit (w : R) (hw : w ^ 2 + w + 1 = 0)
    (hindep : ∀ x y : ℤ, (x : R) + (y : R) * w = 0 → x = 0 ∧ y = 0)
    (hcoord : ∀ z : R, ∃ x y : ℤ, z = eis w x y)
    (k : ℕ) (hk : 1 ≤ k) : ¬ IsUnit (branchEval w k) := by
  rintro ⟨u, hu⟩
  obtain ⟨x', y', hx'⟩ := hcoord (↑u⁻¹)
  have h1 : branchEval w k * eis w x' y' = 1 := by
    rw [← hx', ← hu]
    exact u.mul_inv
  have hdvd : eisNorm (-(4 * (k : ℤ) + 1)) (-(2 * (k : ℤ) + 1)) ∣ 1 :=
    eisNorm_dvd_one_of_mul_eq_one w hw hindep
      (-(4 * (k : ℤ) + 1)) (-(2 * (k : ℤ) + 1)) x' y' h1
  have hge := branch_norm_ge k hk
  have hle := Int.le_of_dvd one_pos hdvd
  omega

/-- **The tree-structure theorem.** Let `p = branchEval w k` be the evaluation at
the odd-preimage node of the `k`-th branch, `k ≥ 1`. Then **no** node of the even
subtree above it admits an odd-preimage:

    ∀ n, ¬ ∃ Q, [2]_q·(αⁿ·p) = [3]_q·Q + 1.

So each `k ≥ 1` branch of the backward tree is a **bare even chain** — it
carries no second odd step. Together with the main chain (`k = 0`, which returns
to the attractor) this exhausts the tree: every node lies on the main chain or on
a bare `k ≥ 1` branch, and **no two odd-preimages ever chain**.

Consequence for the arc: no `v = 0` block occurs in the backward tree. -/
theorem branch_subtree_no_oddPreimage (w : R) (hw : w ^ 2 + w + 1 = 0)
    (hindep : ∀ x y : ℤ, (x : R) + (y : R) * w = 0 → x = 0 ∧ y = 0)
    (hcoord : ∀ z : R, ∃ x y : ℤ, z = eis w x y)
    (k : ℕ) (hk : 1 ≤ k) (n : ℕ) :
    ¬ ∃ Q : R, (w + 1) * ((w + 1) ^ n * branchEval w k)
        = (w ^ 2 + w + 1) * Q + 1 := by
  rintro ⟨Q, hQ⟩
  -- `[3]_q` vanishes at `w`, so the odd-branch relation collapses to
  -- `(w+1)·(αⁿ·p) = 1`: the node evaluation is a unit.
  have h1 : (w + 1) * ((w + 1) ^ n * branchEval w k) = 1 := by
    rw [hQ]; linear_combination Q * hw
  have hu : IsUnit ((w + 1) ^ n * branchEval w k) :=
    isUnit_of_mul_eq_one _ (w + 1) (by linear_combination h1)
  -- unit-ness of `αⁿ·p` gives unit-ness of `p`, contradicting the norm.
  exact branchEval_not_isUnit w hw hindep hcoord k hk (isUnit_of_mul_isUnit_right hu)

end QOU.AppendixSurreals.CollatzEisenstein
