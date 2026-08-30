/-
# The Taylor expansion about `α`, and the bound that makes its tail small

`RothRationalIndex` reduces step 2 of Roth's theorem to one hypothesis: that the low-weight
translated coefficients of `P` at the rational point `β` are smaller than `1/∏ q_h^{r_h}`.  This
file proves the two facts that hypothesis is built from.

**The expansion.**  `translate_translate` — translating by `α` and then by `γ` is translating by
`α + γ`.  Composed with `coeff_translate_eq_sum` this is `coeff_translate_add`: the coefficients
of `P` at `α + γ` are a `translateMatrix γ`-combination of its coefficients at `α`.  That is
Taylor's theorem in the only form the argument needs, and it is why an index hypothesis at `α`
constrains the values at `β = α + γ` at all: every term of the sum with `idxWeight r n` below the
index is simply absent.

**The bound.**  `seminorm_translateMatrix_le_pow` — `f (translateMatrix γ i n) ≤ 2^{|n|}·G^{|n|−|i|}`
whenever `f ∘ γ ≤ G ≤ 1`.  The truncated subtraction is not a convenience: when `|i| > |n|` the
matrix entry is genuinely `0`, and the bound degrades to `2^{|n|}`, which is what the induction
can prove without a separate vanishing lemma.

## Why not reuse `seminorm_translateMatrix_le`

`RothAuxiliaryPolynomial` already bounds the same entries by `(2B)^{|n|}` with `B ≥ 1` bounding
`f ∘ α`.  That is the right shape for step 1, where `α` is a fixed algebraic number and the point
is that the *matrix* is small.  It is the wrong shape here: the whole content of step 2 is that
`γ = β − α` is **tiny**, and `(2G)^{|n|}` throws that away by not separating the `|i|` that the
factor `γ^{n−i}` does not carry.  The two bounds are proved by the same peeling and differ only
in what is tracked through it — which is exactly the kind of place where reusing the existing
lemma "because it is about the same object" would have silently cost the argument its exponent.

## `G ≤ 1` is load-bearing

Without it the induction fails at `|i| = |n|`: the surviving term is `f(γ_j)·f(T(i,n'))` with
`T(i,n') = 0`, and the truncated exponent has already collapsed to `G^0 = 1`, so the step needs
`1 + G ≤ 2` rather than the equality it gets when `|i| < |n|`.  The alternative is a separate
`translateMatrix_eq_zero_of_lt`; `G ≤ 1` is free in every application (`|β_h − α| ≤ q_h^{−(2+δ)}`)
and costs one hypothesis instead of a second induction.
-/
import QOU.Mathlib.RothRationalIndex

namespace MvPolynomial

open Finset

variable {σ R : Type*} [CommRing R]

/-- **Translating twice is translating by the sum.**  `P(x + α + γ) = (P(x + α))(x + γ)`. -/
theorem translate_translate (α γ : σ → R) (P : MvPolynomial σ R) :
    translate γ (translate α P) = translate (fun j => α j + γ j) P := by
  have h : (aeval (fun j => X j + C (γ j)) : MvPolynomial σ R →ₐ[R] MvPolynomial σ R).comp
      (aeval (fun j => X j + C (α j))) = aeval (fun j => X j + C (α j + γ j)) := by
    rw [comp_aeval]
    congr 1
    funext j
    simp [add_comm, add_left_comm]
  have := congrArg (fun φ => φ P) h
  simpa [translate] using this

/-- **Taylor's theorem, in the only form Roth's theorem needs.**  The coefficients at `α + γ` are
a `translateMatrix γ`-combination of the coefficients at `α`; an index hypothesis at `α` deletes
every low-weight term of the sum. -/
theorem coeff_translate_add [DecidableEq σ] (α γ : σ → R) (P : MvPolynomial σ R) (i : σ →₀ ℕ) :
    coeff i (translate (fun j => α j + γ j) P)
      = ∑ n ∈ (translate α P).support,
          coeff n (translate α P) * translateMatrix γ i n := by
  rw [← translate_translate α γ P, coeff_translate_eq_sum]

/-- The step inequality behind `seminorm_translateMatrix_le_pow`.  `G ≤ 1` is exactly what is
needed once the truncated exponent has collapsed — and it is the *only* hypothesis: below the
collapse the two sides are equal, so no sign condition on `G` is required.  The linter caught
that `0 ≤ G` was never used, and the stronger statement is kept rather than the tidier one. -/
theorem mul_pow_sub_le {G : ℝ} (hG1 : G ≤ 1) (N Ni : ℕ) :
    G * G ^ (N - Ni) ≤ G ^ ((N + 1) - Ni) := by
  rcases le_or_gt Ni N with h | h
  · have he : (N + 1) - Ni = (N - Ni) + 1 := by omega
    rw [he, pow_succ]
    ring_nf
    exact le_of_eq rfl
  · have h1 : N - Ni = 0 := by omega
    have h2 : (N + 1) - Ni = 0 := by omega
    rw [h1, h2, pow_zero, mul_one]
    exact hG1

/-- **The translate matrix is small when the translation is.**  `f(binom(n,i)·γ^{n−i}) ≤
2^{|n|}·G^{|n|−|i|}` for `f ∘ γ ≤ G ≤ 1` — the same peeling as `seminorm_translateMatrix_le`, but
tracking the power of `γ` that the entry actually carries instead of discarding it.

That difference is the whole of step 2: `γ = β − α` is tiny, and a bound of the form `(2G)^{|n|}`
would be true and useless. -/
theorem seminorm_translateMatrix_le_pow [DecidableEq σ] {f : R → ℝ} (hf : SubmultSeminorm f)
    (γ : σ → R) {G : ℝ} (hG0 : 0 ≤ G) (hG1 : G ≤ 1) (hγ : ∀ h, f (γ h) ≤ G) :
    ∀ (N : ℕ) (n : σ →₀ ℕ), (n.sum fun _ e => e) = N → ∀ i : σ →₀ ℕ,
      f (translateMatrix γ i n) ≤ 2 ^ N * G ^ (N - (i.sum fun _ e => e)) := by
  intro N
  induction N with
  | zero =>
      intro n hn i
      rw [Finsupp.sum] at hn
      have hn0 : n = 0 := by
        ext a
        by_contra hc
        have hmem : a ∈ n.support := Finsupp.mem_support_iff.mpr (by simpa using hc)
        exact (Finsupp.mem_support_iff.mp hmem) ((Finset.sum_eq_zero_iff.mp hn) a hmem)
      subst hn0
      rw [translateMatrix, monomial_zero', map_one, translate, map_one, coeff_one]
      simp only [Nat.zero_sub, pow_zero, one_mul]
      split_ifs
      · exact hf.one_le
      · rw [hf.map_zero]; norm_num
  | succ N ih =>
      intro n hn i
      have hne : n ≠ 0 := by intro h; rw [h] at hn; simp at hn
      obtain ⟨j, hj⟩ : ∃ j, n j ≠ 0 := by
        by_contra hc; push_neg at hc; exact hne (Finsupp.ext hc)
      set n' : σ →₀ ℕ := n - Finsupp.single j 1 with hn'
      have hle : Finsupp.single j 1 ≤ n :=
        Finsupp.single_le_iff.mpr (Nat.one_le_iff_ne_zero.mpr hj)
      have hsplit : Finsupp.single j 1 + n' = n := add_tsub_cancel_of_le hle
      have hsum' : (n'.sum fun _ e => e) = N := by
        have hadd : ((Finsupp.single j 1 + n').sum fun _ e => e)
            = ((Finsupp.single j 1).sum fun _ e => e) + (n'.sum fun _ e => e) :=
          Finsupp.sum_add_index' (fun _ => rfl) (fun _ _ _ => rfl)
        rw [hsplit, Finsupp.sum_single_index rfl] at hadd
        omega
      set Ni : ℕ := i.sum (fun _ e => e) with hNi
      have hmono : (monomial n 1 : MvPolynomial σ R) = X j * monomial n' 1 := by
        rw [X, monomial_mul, hsplit, one_mul]
      have htr : translate γ (monomial n 1)
          = (X j + C (γ j)) * translate γ (monomial n' 1) := by
        rw [hmono, translate, map_mul, aeval_X, ← translate]
      have hcoeff : translateMatrix γ i n
          = coeff i (X j * translate γ (monomial n' 1))
            + (γ j) * coeff i (translate γ (monomial n' 1)) := by
        rw [translateMatrix, htr, add_mul, coeff_add, coeff_C_mul]
      -- the `X j` term: one occurrence of `γ` is *not* spent, so the exponent drops by one
      have h1 : f (coeff i (X j * translate γ (monomial n' 1)))
          ≤ 2 ^ N * G ^ ((N + 1) - Ni) := by
        rw [coeff_X_mul']
        split_ifs with hmem
        · have hij : i j ≠ 0 := Finsupp.mem_support_iff.mp hmem
          have hile : Finsupp.single j 1 ≤ i :=
            Finsupp.single_le_iff.mpr (Nat.one_le_iff_ne_zero.mpr hij)
          have hisplit : Finsupp.single j 1 + (i - Finsupp.single j 1) = i :=
            add_tsub_cancel_of_le hile
          have hisum : ((i - Finsupp.single j 1).sum fun _ e => e) = Ni - 1 := by
            have hadd : ((Finsupp.single j 1 + (i - Finsupp.single j 1)).sum fun _ e => e)
                = ((Finsupp.single j 1).sum fun _ e => e)
                  + ((i - Finsupp.single j 1).sum fun _ e => e) :=
              Finsupp.sum_add_index' (fun _ => rfl) (fun _ _ _ => rfl)
            rw [hisplit, Finsupp.sum_single_index rfl] at hadd
            omega
          have hNi1 : 1 ≤ Ni := by
            rw [hNi, Finsupp.sum]
            exact le_trans (Nat.one_le_iff_ne_zero.mpr hij)
              (Finset.single_le_sum (f := fun a => i a) (fun _ _ => Nat.zero_le _) hmem)
          have hexp : N - (Ni - 1) = (N + 1) - Ni := by omega
          have := ih n' hsum' (i - Finsupp.single j 1)
          rw [hisum, hexp] at this
          exact this
        · rw [hf.map_zero]
          positivity
      -- the constant term: one occurrence of `γ` *is* spent
      have h2 : f ((γ j) * coeff i (translate γ (monomial n' 1)))
          ≤ G * (2 ^ N * G ^ (N - Ni)) := by
        refine le_trans (hf.mul_le _ _) (mul_le_mul (hγ j) (ih n' hsum' i)
          (hf.nonneg _) hG0)
      have hstep : G * (2 ^ N * G ^ (N - Ni)) ≤ 2 ^ N * G ^ ((N + 1) - Ni) := by
        have := mul_pow_sub_le hG1 N Ni
        nlinarith [pow_nonneg (by norm_num : (0:ℝ) ≤ 2) N, pow_nonneg hG0 (N - Ni),
          pow_nonneg hG0 ((N + 1) - Ni)]
      rw [hcoeff]
      refine le_trans (hf.add_le _ _) ?_
      calc f (coeff i (X j * translate γ (monomial n' 1)))
            + f ((γ j) * coeff i (translate γ (monomial n' 1)))
          ≤ 2 ^ N * G ^ ((N + 1) - Ni) + 2 ^ N * G ^ ((N + 1) - Ni) :=
            add_le_add h1 (le_trans h2 hstep)
        _ = 2 ^ (N + 1) * G ^ ((N + 1) - Ni) := by rw [pow_succ]; ring

/-- `|·|` on `ℝ` is a submultiplicative seminorm. -/
theorem submultSeminorm_abs_real : SubmultSeminorm (abs : ℝ → ℝ) :=
  ⟨fun a => abs_nonneg a, abs_zero, le_of_eq abs_one, abs_add_le, fun a b => le_of_eq (abs_mul a b)⟩

/-- **The real instance.**  `|binom(n,i)·γ^{n−i}| ≤ 2^{|n|}·G^{|n|−|i|}` for real `γ` bounded by
`G ≤ 1`. -/
theorem abs_translateMatrix_le_pow [DecidableEq σ] (γ : σ → ℝ) {G : ℝ}
    (hG0 : 0 ≤ G) (hG1 : G ≤ 1) (hγ : ∀ h, |γ h| ≤ G) (n i : σ →₀ ℕ) :
    |translateMatrix γ i n|
      ≤ 2 ^ (n.sum fun _ e => e) * G ^ ((n.sum fun _ e => e) - (i.sum fun _ e => e)) :=
  seminorm_translateMatrix_le_pow submultSeminorm_abs_real γ hG0 hG1 hγ _ n rfl i

/-- **The tail of the Taylor expansion, bounded.**  Every coefficient of `P` at `α + γ` is at most
`(#terms)·(max coefficient at `α`)·2^{max degree}·G^{…}` — stated as a single sum bound so that the
index hypothesis at `α`, which restricts *which* `n` survive, can be applied to it directly. -/
theorem abs_coeff_translate_add_le [DecidableEq σ] (α γ : σ → ℝ) {G : ℝ}
    (hG0 : 0 ≤ G) (hG1 : G ≤ 1) (hγ : ∀ h, |γ h| ≤ G) (P : MvPolynomial σ ℝ) (i : σ →₀ ℕ) :
    |coeff i (translate (fun j => α j + γ j) P)|
      ≤ ∑ n ∈ (translate α P).support, |coeff n (translate α P)|
          * (2 ^ (n.sum fun _ e => e) * G ^ ((n.sum fun _ e => e) - (i.sum fun _ e => e))) := by
  rw [coeff_translate_add]
  refine le_trans (Finset.abs_sum_le_sum_abs _ _) (Finset.sum_le_sum (fun n _ => ?_))
  rw [abs_mul]
  exact mul_le_mul_of_nonneg_left (abs_translateMatrix_le_pow γ hG0 hG1 hγ n i) (abs_nonneg _)

end MvPolynomial
