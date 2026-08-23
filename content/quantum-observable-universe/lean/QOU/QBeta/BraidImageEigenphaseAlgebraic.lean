/-
# The eigenphase exclusion extends from Laurent to ALGEBRAIC — closing the
# sub-case `BraidImageEigenphaseExclusion` explicitly left open

Bean `qou-cds1` (tranche S1).  Strict strengthening of
[`BraidImageEigenphaseExclusion.lean`](BraidImageEigenphaseExclusion.lean),
whose §"Three limits" (i) says:

> It closes the **character** case, not the **eigenvalue-pair** case … were `α`
> **one** eigenphase among several of a larger braid-image matrix, `2 cos α`
> would be **algebraic** rather than Laurent, and boundedness does not extend
> (an algebraic function can be bounded on `(0,∞)` and non-constant, e.g.
> `q/(q+1)`), so that sub-case still needs the transcendence argument.

That diagnosis of the obstruction is correct, and the remedy turns out **not**
to be a transcendence argument: boundedness is simply the wrong invariant to
push.  Replacing it with a *zero-counting* argument closes the algebraic case by
the same elementary means, from the **same hypothesis already proved there**
(`alphaC_surjective_nonpos` / `alphaD_neg_surjective_nonpos`), with no new
analytic input.

## Why boundedness stalls and zero-counting does not

`|2 cos α| ≤ 2` says one thing about the *size* of the function.  A Laurent
polynomial bounded on `(0,∞)` is constant, so size alone suffices there; an
algebraic function need not be, which is exactly the cited `q/(q+1)`.

But the hypothesis in hand is far stronger than boundedness.  `α` attains
**every** non-positive real on `[1,∞)`, so for each `c ∈ [−2,2]` the level set
`{s : 2 cos (α s) = c}` is **infinite** — take `α s = −(k·2π + arccos (c/2))`
for every `k : ℕ`.  Infinitely many solutions of a polynomial identity force the
polynomial to vanish, and that argument is indifferent to whether the relation
is Laurent or algebraic of any degree.

## The statement

Suppose `2 cos (α ·)` satisfies **any** polynomial relation over `ℝ[X]`:

    ∑_{j ≤ d} p_j(s) · (2 cos (α s))^j = 0     for every s ≥ 1

Then **every** `p_j` is the zero polynomial (`coeffs_zero_of_surjective_nonpos`),
so no non-trivial algebraic relation exists.  Three steps, each an application of
"a polynomial with infinitely many roots is zero":

1. Fix `c ∈ [−2,2]`.  The relation holds at infinitely many `s`, all with
   `2 cos (α s) = c`, so the `X`-polynomial `R_c = ∑_j p_j · c^j` has infinitely
   many roots, hence `R_c = 0`.
2. Fix `x`.  By step 1 the `Y`-polynomial `S_x = ∑_j p_j(x)·Y^j` vanishes on all
   of `[−2,2]`, an infinite set, hence `S_x = 0`; reading off coefficients gives
   `p_j(x) = 0` for every `j ≤ d`.
3. `p_j` vanishes at every real, hence `p_j = 0`.

## What this does and does not do

**Does.**  Closes branch 1 of the `EigenphaseCarrierVacuity` trichotomy in
full — character case *and* eigenvalue-pair case — because a sum of two
eigenvalues of a matrix with entries algebraic over `ℝ(s)` is itself algebraic
over `ℝ(s)` (the elementary symmetric functions of the characteristic
polynomial's roots lie in the base field), and is therefore covered by the
hypothesis above.  It **subsumes** `no_laurent_of_surjective_nonpos`: a Laurent
relation `2 cos α = P(s)/s^N` is the case `d = 1`, `p₀ = −P`, `p₁ = X^N`.

**Does not.**  It does not derive `α`, in either convention; it does not state a
D-frame ladder; and branch 3 (a holonomy of an independently-defined
KZ / Kohno–Drinfeld connection) is untouched and remains the only place a
derivation of `α` can live.  As before the argument **never reads `z`'s
formula**, so it is a property of the whole class of Markov parameters with
unbounded phase, not a fact about convention C or D.

**Scope-(b)** — a structural exclusion citing a proved invariant, per
AGENTS.md §"Before declaring refuted".

**One import of shape, unchanged from the predecessor.**  That a braid image's
matrix entries are algebraic over `ℝ(s)` is the standard `χ_λ(T_w) ∈ ℤ[q,q⁻¹]`
of Geck–Pfeiffer, taken here as the shape of the hypothesis, not proved here.
-/
import QOU.QBeta.BraidImageEigenphaseExclusion

namespace QOU.QBeta.BraidImageEigenphase

open Real Polynomial

/-! ## §1 — the two slices of a coefficient family -/

/-- `R_c(X) = ∑_{j ≤ d} p_j(X) · c^j`, the relation with `Y` frozen at `c`. -/
noncomputable def sliceX (p : ℕ → ℝ[X]) (d : ℕ) (c : ℝ) : ℝ[X] :=
  ∑ j ∈ Finset.range (d + 1), p j * C (c ^ j)

theorem sliceX_eval (p : ℕ → ℝ[X]) (d : ℕ) (c s : ℝ) :
    (sliceX p d c).eval s = ∑ j ∈ Finset.range (d + 1), (p j).eval s * c ^ j := by
  simp [sliceX, Polynomial.eval_finset_sum]

/-- `S_x(Y) = ∑_{j ≤ d} p_j(x) · Y^j`, the relation with `X` frozen at `x`. -/
noncomputable def sliceY (p : ℕ → ℝ[X]) (d : ℕ) (x : ℝ) : ℝ[X] :=
  ∑ j ∈ Finset.range (d + 1), monomial j ((p j).eval x)

theorem sliceY_eval (p : ℕ → ℝ[X]) (d : ℕ) (x c : ℝ) :
    (sliceY p d x).eval c = ∑ j ∈ Finset.range (d + 1), (p j).eval x * c ^ j := by
  simp [sliceY, Polynomial.eval_finset_sum, Polynomial.eval_monomial]

theorem sliceY_coeff (p : ℕ → ℝ[X]) (d : ℕ) (x : ℝ) {j : ℕ} (hj : j ≤ d) :
    (sliceY p d x).coeff j = (p j).eval x := by
  classical
  simp only [sliceY, Polynomial.finset_sum_coeff, Polynomial.coeff_monomial]
  rw [Finset.sum_ite_eq' (Finset.range (d + 1)) j fun i => (p i).eval x]
  simp [Finset.mem_range, Nat.lt_succ_of_le hj]

/-! ## §2 — the exclusion for an arbitrary algebraic relation -/

/-- **No non-trivial algebraic relation.**  If `2 cos (α ·)` satisfies a
polynomial relation over `ℝ[X]` on `[1,∞)`, and `α` attains every non-positive
real there, then every coefficient polynomial vanishes.

This strengthens `no_laurent_of_surjective_nonpos` from Laurent relations to
algebraic ones; see the module docstring. -/
theorem coeffs_zero_of_surjective_nonpos
    (α : ℝ → ℝ)
    (hsurj : ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ α s = y)
    (p : ℕ → ℝ[X]) (d : ℕ)
    (heq : ∀ s : ℝ, 1 ≤ s →
      ∑ j ∈ Finset.range (d + 1), (p j).eval s * (2 * Real.cos (α s)) ^ j = 0) :
    ∀ j, j ≤ d → p j = 0 := by
  classical
  -- STEP 1.  For every `c ∈ [−2,2]` the frozen-`Y` polynomial vanishes.
  have step1 : ∀ c : ℝ, -2 ≤ c → c ≤ 2 → sliceX p d c = 0 := by
    intro c hc1 hc2
    set θ : ℝ := Real.arccos (c / 2) with hθ
    have hcosθ : Real.cos θ = c / 2 := Real.cos_arccos (by linarith) (by linarith)
    have hθ0 : 0 ≤ θ := Real.arccos_nonneg _
    set y : ℕ → ℝ := fun k => -((k : ℝ) * (2 * π) + θ) with hy
    have hynonpos : ∀ k, y k ≤ 0 := by
      intro k
      have hk : (0 : ℝ) ≤ (k : ℝ) * (2 * π) := by positivity
      simp only [hy]
      linarith
    have hycos : ∀ k, Real.cos (y k) = c / 2 := by
      intro k
      simp only [hy, Real.cos_neg]
      rw [add_comm, Real.cos_add_nat_mul_two_pi, hcosθ]
    have hyinj : Function.Injective y := by
      intro a b hab
      have hpi : (0 : ℝ) < 2 * π := by positivity
      simp only [hy, neg_inj] at hab
      have hmul : (a : ℝ) * (2 * π) = (b : ℝ) * (2 * π) := by linarith
      exact_mod_cast mul_right_cancel₀ (ne_of_gt hpi) hmul
    choose f hf1 hf2 using fun k : ℕ => hsurj (y k) (hynonpos k)
    have hfinj : Function.Injective f := by
      intro a b hab
      exact hyinj (by rw [← hf2 a, ← hf2 b, hab])
    have hmem : ∀ k : ℕ, f k ∈ {x : ℝ | (sliceX p d c).IsRoot x} := by
      intro k
      have hval : 2 * Real.cos (α (f k)) = c := by
        rw [hf2 k, hycos k]; ring
      have hrel := heq (f k) (hf1 k)
      simp only [Polynomial.IsRoot, Set.mem_setOf_eq, sliceX_eval]
      rw [← hval]
      exact hrel
    exact Polynomial.eq_zero_of_infinite_isRoot _
      (Set.infinite_of_injective_forall_mem hfinj hmem)
  -- STEP 2.  Freeze `X` instead: the `Y`-polynomial vanishes on `[−2,2]`.
  have step2 : ∀ x : ℝ, ∀ j, j ≤ d → (p j).eval x = 0 := by
    intro x j hj
    have hroots : Set.Icc (-2 : ℝ) 2 ⊆ {c : ℝ | (sliceY p d x).IsRoot c} := by
      intro c hc
      have h1 := step1 c hc.1 hc.2
      have hx : (sliceX p d c).eval x = 0 := by rw [h1]; simp
      simp only [Polynomial.IsRoot, Set.mem_setOf_eq, sliceY_eval]
      rw [← sliceX_eval p d c x]
      exact hx
    have hinf : {c : ℝ | (sliceY p d x).IsRoot c}.Infinite :=
      Set.Infinite.mono hroots (Set.Icc_infinite (by norm_num))
    have hzero : sliceY p d x = 0 := Polynomial.eq_zero_of_infinite_isRoot _ hinf
    have hco := sliceY_coeff p d x hj
    rw [hzero] at hco
    simpa using hco.symm
  -- STEP 3.  A polynomial vanishing at every real is zero.
  intro j hj
  exact Polynomial.funext fun x => by simpa using step2 x j hj

/-! ### The Laurent case really is a special case

The module docstring claims this statement **subsumes**
`no_laurent_of_surjective_nonpos`.  That is a claim about the two theorems, so
it is checked here rather than asserted: the Laurent relation is the case
`d = 1`, `p₀ = −P`, `p₁ = X^N`, and re-deriving the predecessor from the new
statement is a two-line proof. -/

/-- **Subsumption, verified.**  `no_laurent_of_surjective_nonpos` re-derived as
the `d = 1` case of `coeffs_zero_of_surjective_nonpos`. -/
theorem no_laurent_of_algebraic
    (α : ℝ → ℝ)
    (hsurj : ∀ y : ℝ, y ≤ 0 → ∃ s : ℝ, 1 ≤ s ∧ α s = y)
    (P : ℝ[X]) (N : ℕ)
    (heq : ∀ s : ℝ, 1 ≤ s → 2 * Real.cos (α s) = P.eval s / s ^ N) :
    False := by
  classical
  set p : ℕ → ℝ[X] := fun j => if j = 0 then -P else (X : ℝ[X]) ^ N with hp
  have hne : p 1 ≠ 0 := by
    simp only [hp, if_neg (one_ne_zero)]
    exact pow_ne_zero _ Polynomial.X_ne_zero
  refine hne (coeffs_zero_of_surjective_nonpos α hsurj p 1 ?_ 1 le_rfl)
  intro s hs
  have hs0 : (0 : ℝ) < s := lt_of_lt_of_le zero_lt_one hs
  have hpow : (s : ℝ) ^ N ≠ 0 := pow_ne_zero _ (ne_of_gt hs0)
  have hval : 2 * Real.cos (α s) = P.eval s / s ^ N := heq s hs
  simp only [hp, Finset.sum_range_succ, Finset.sum_range_zero,
    if_neg (one_ne_zero), Polynomial.eval_pow,
    Polynomial.eval_X, pow_zero, pow_one, zero_add, mul_one]
  rw [hval]
  field_simp
  simp

/-! ## §3 — the two conventions -/

/-- **Branch 1 is closed for convention C, algebraic case included.** -/
theorem no_braid_algebraic_C (p : ℕ → ℝ[X]) (d j₀ : ℕ) (hj₀ : j₀ ≤ d)
    (hne : p j₀ ≠ 0)
    (heq : ∀ s : ℝ, 1 ≤ s →
      ∑ j ∈ Finset.range (d + 1),
        (p j).eval s * (2 * Real.cos (alphaOf zC s)) ^ j = 0) :
    False :=
  hne (coeffs_zero_of_surjective_nonpos _ alphaC_surjective_nonpos p d heq j₀ hj₀)

/-- **Branch 1 is closed for convention D — the canonical one — algebraic case
included.**  `cos` is even, so the negated phase carries the argument. -/
theorem no_braid_algebraic_D (p : ℕ → ℝ[X]) (d j₀ : ℕ) (hj₀ : j₀ ≤ d)
    (hne : p j₀ ≠ 0)
    (heq : ∀ s : ℝ, 1 ≤ s →
      ∑ j ∈ Finset.range (d + 1),
        (p j).eval s * (2 * Real.cos (alphaOf zD s)) ^ j = 0) :
    False := by
  refine hne (coeffs_zero_of_surjective_nonpos (fun t => -(alphaOf zD t))
    alphaD_neg_surjective_nonpos p d ?_ j₀ hj₀)
  intro s hs
  simpa [Real.cos_neg] using heq s hs

end QOU.QBeta.BraidImageEigenphase
