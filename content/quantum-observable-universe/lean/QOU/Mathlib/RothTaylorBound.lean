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

## ⚠ One `G` is not enough — `seminorm_translateMatrix_le_prod` is the usable form

`seminorm_translateMatrix_le_pow` bounds the entry by `2^{|n|}·G^{|n|−|i|}`, with a **single**
`G` and the **unweighted** degree difference.  I wrote it first and it cannot feed the argument.
The index hypothesis at `α` gives `idxWeight r n ≥ μ` and the conclusion is wanted for
`idxWeight r i < ν`, and `idxWeight` is weighted by `1/r_h`.  In Roth's regime the `r_h` are
wildly unequal by construction — `RothGrowth` forces `r_{h+1} ≪ r_h` — so a lower bound on the
*weighted* difference gives no lower bound whatever on `∑_h (n_h − i_h)`.  The single-`G` bound is
true and useless.

`seminorm_translateMatrix_le_prod` is the same induction tracking `∏_h G_h^{n_h − i_h}`, one `G_h`
per coordinate, which is what pairs with `|β_h − α| ≤ q_h^{−(2+δ)}` and `r_h·log q_h ≈ L`.  The
weaker statement is kept rather than deleted: it is what an honest record of the arc looks like,
and the gap between "the bound holds" and "the bound is the one the consumer needs" is precisely
the gap corrections 24 and 26 both lived in.

## `G ≤ 1` is load-bearing

Without it the induction fails at `|i| = |n|`: the surviving term is `f(γ_j)·f(T(i,n'))` with
`T(i,n') = 0`, and the truncated exponent has already collapsed to `G^0 = 1`, so the step needs
`1 + G ≤ 2` rather than the equality it gets when `|i| < |n|`.  The alternative is a separate
`translateMatrix_eq_zero_of_lt`; `G ≤ 1` is free in every application (`|β_h − α| ≤ q_h^{−(2+δ)}`)
and costs one hypothesis instead of a second induction.
-/
import QOU.Mathlib.RothRationalIndex
import QOU.Mathlib.WronskianHeight

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

section PerCoordinate

variable {m : ℕ}

/-- The step inequality, per coordinate: peeling `X_j` spends one `γ_j` exactly when the
coefficient index has not already outrun the monomial in that coordinate. -/
theorem mul_pow_sub_one_le {g : ℝ} (hg1 : g ≤ 1) {a b : ℕ} (ha : 1 ≤ a) :
    g * g ^ ((a - 1) - b) ≤ g ^ (a - b) := by
  have h := mul_pow_sub_le hg1 (a - 1) b
  have he : (a - 1) + 1 = a := by omega
  rwa [he] at h

/-- **The usable bound: one `G_h` per coordinate.**  `f(binom(n,i)·γ^{n−i}) ≤ 2^{|n|}·∏_h
G_h^{n_h−i_h}`.  Same peeling as `seminorm_translateMatrix_le_pow`, but the tracked quantity is
the product, which is what pairs with `|β_h − α| ≤ q_h^{−(2+δ)}` — see the ⚠ in the header for
why the single-`G` form cannot. -/
theorem seminorm_translateMatrix_le_prod {R : Type*} [CommRing R] {f : R → ℝ}
    (hf : SubmultSeminorm f) (γ : Fin m → R) {G : Fin m → ℝ}
    (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1) (hγ : ∀ h, f (γ h) ≤ G h) :
    ∀ (N : ℕ) (n : Fin m →₀ ℕ), (n.sum fun _ e => e) = N → ∀ i : Fin m →₀ ℕ,
      f (translateMatrix γ i n) ≤ 2 ^ N * ∏ h, (G h) ^ (n h - i h) := by
  classical
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
      have hprod : (∏ h, (G h) ^ ((0 : Fin m →₀ ℕ) h - i h)) = 1 := by
        refine Finset.prod_eq_one (fun h _ => ?_)
        simp
      rw [translateMatrix, monomial_zero', map_one, translate, map_one, coeff_one]
      rw [hprod, pow_zero, one_mul]
      split_ifs
      · exact hf.one_le
      · rw [hf.map_zero]; norm_num
  | succ N ih =>
      intro n hn i
      have hne : n ≠ 0 := by intro h; rw [h] at hn; simp at hn
      obtain ⟨j, hj⟩ : ∃ j, n j ≠ 0 := by
        by_contra hc; push_neg at hc; exact hne (Finsupp.ext hc)
      set n' : Fin m →₀ ℕ := n - Finsupp.single j 1 with hn'
      have hle : Finsupp.single j 1 ≤ n :=
        Finsupp.single_le_iff.mpr (Nat.one_le_iff_ne_zero.mpr hj)
      have hsplit : Finsupp.single j 1 + n' = n := add_tsub_cancel_of_le hle
      have hsum' : (n'.sum fun _ e => e) = N := by
        have hadd : ((Finsupp.single j 1 + n').sum fun _ e => e)
            = ((Finsupp.single j 1).sum fun _ e => e) + (n'.sum fun _ e => e) :=
          Finsupp.sum_add_index' (fun _ => rfl) (fun _ _ _ => rfl)
        rw [hsplit, Finsupp.sum_single_index rfl] at hadd
        omega
      have hn'j : n' j = n j - 1 := by
        rw [hn']; simp
      have hn'ne : ∀ h, h ≠ j → n' h = n h := by
        intro h hhj
        rw [hn']; simp [hhj]
      have hprodNonneg : ∀ (u v : Fin m →₀ ℕ), 0 ≤ ∏ h, (G h) ^ (u h - v h) :=
        fun u v => Finset.prod_nonneg (fun h _ => pow_nonneg (hG0 h) _)
      have hmono : (monomial n 1 : MvPolynomial (Fin m) R) = X j * monomial n' 1 := by
        rw [X, monomial_mul, hsplit, one_mul]
      have htr : translate γ (monomial n 1)
          = (X j + C (γ j)) * translate γ (monomial n' 1) := by
        rw [hmono, translate, map_mul, aeval_X, ← translate]
      have hcoeff : translateMatrix γ i n
          = coeff i (X j * translate γ (monomial n' 1))
            + (γ j) * coeff i (translate γ (monomial n' 1)) := by
        rw [translateMatrix, htr, add_mul, coeff_add, coeff_C_mul]
      -- the `X j` term: the exponent at `j` is unchanged, because both sides lost one
      have h1 : f (coeff i (X j * translate γ (monomial n' 1)))
          ≤ 2 ^ N * ∏ h, (G h) ^ (n h - i h) := by
        rw [coeff_X_mul']
        split_ifs with hmem
        · have hij : i j ≠ 0 := Finsupp.mem_support_iff.mp hmem
          set i' : Fin m →₀ ℕ := i - Finsupp.single j 1 with hi'
          have hi'j : i' j = i j - 1 := by
            rw [hi']; simp
          have hi'ne : ∀ h, h ≠ j → i' h = i h := by
            intro h hhj
            rw [hi']; simp [hhj]
          have heq : (∏ h, (G h) ^ (n' h - i' h)) = ∏ h, (G h) ^ (n h - i h) := by
            refine Finset.prod_congr rfl (fun h _ => ?_)
            by_cases hhj : h = j
            · subst hhj
              rw [hn'j, hi'j]
              congr 1
              omega
            · rw [hn'ne h hhj, hi'ne h hhj]
          have := ih n' hsum' i'
          rwa [heq] at this
        · rw [hf.map_zero]
          have := hprodNonneg n i
          positivity
      -- the constant term: one `γ_j` is spent, so the exponent at `j` drops
      have h2 : f ((γ j) * coeff i (translate γ (monomial n' 1)))
          ≤ (G j) * (2 ^ N * ∏ h, (G h) ^ (n' h - i h)) :=
        le_trans (hf.mul_le _ _)
          (mul_le_mul (hγ j) (ih n' hsum' i) (hf.nonneg _) (hG0 j))
      have hstep : (G j) * (2 ^ N * ∏ h, (G h) ^ (n' h - i h))
          ≤ 2 ^ N * ∏ h, (G h) ^ (n h - i h) := by
        have hrest : (∏ h ∈ Finset.univ.erase j, (G h) ^ (n' h - i h))
            = ∏ h ∈ Finset.univ.erase j, (G h) ^ (n h - i h) :=
          Finset.prod_congr rfl (fun h hh => by
            rw [hn'ne h (Finset.ne_of_mem_erase hh)])
        have hp' : (∏ h, (G h) ^ (n' h - i h))
            = (G j) ^ (n' j - i j) * ∏ h ∈ Finset.univ.erase j, (G h) ^ (n h - i h) := by
          rw [← hrest]
          exact (Finset.mul_prod_erase _ _ (Finset.mem_univ j)).symm
        have hp : (∏ h, (G h) ^ (n h - i h))
            = (G j) ^ (n j - i j) * ∏ h ∈ Finset.univ.erase j, (G h) ^ (n h - i h) :=
          (Finset.mul_prod_erase _ _ (Finset.mem_univ j)).symm
        have hQ : 0 ≤ ∏ h ∈ Finset.univ.erase j, (G h) ^ (n h - i h) :=
          Finset.prod_nonneg (fun h _ => pow_nonneg (hG0 h) _)
        have hcore : (G j) * (G j) ^ (n' j - i j) ≤ (G j) ^ (n j - i j) := by
          rw [hn'j]
          exact mul_pow_sub_one_le (hG1 j) (Nat.one_le_iff_ne_zero.mpr hj)
        rw [hp', hp]
        have h2N : (0:ℝ) ≤ 2 ^ N := pow_nonneg (by norm_num) N
        nlinarith [mul_nonneg hQ h2N]
      rw [hcoeff]
      refine le_trans (hf.add_le _ _) ?_
      calc f (coeff i (X j * translate γ (monomial n' 1)))
            + f ((γ j) * coeff i (translate γ (monomial n' 1)))
          ≤ 2 ^ N * (∏ h, (G h) ^ (n h - i h)) + 2 ^ N * ∏ h, (G h) ^ (n h - i h) :=
            add_le_add h1 (le_trans h2 hstep)
        _ = 2 ^ (N + 1) * ∏ h, (G h) ^ (n h - i h) := by rw [pow_succ]; ring

/-- **The real instance of the usable bound.** -/
theorem abs_translateMatrix_le_prod (γ : Fin m → ℝ) {G : Fin m → ℝ}
    (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1) (hγ : ∀ h, |γ h| ≤ G h) (n i : Fin m →₀ ℕ) :
    |translateMatrix γ i n|
      ≤ 2 ^ (n.sum fun _ e => e) * ∏ h, (G h) ^ (n h - i h) :=
  seminorm_translateMatrix_le_prod submultSeminorm_abs_real γ hG0 hG1 hγ _ n rfl i

/-- `f` of a finite sum is at most the sum of the `f`s.  The structure carries `add_le` only in
binary form; this is the iterated version every estimate here actually uses. -/
theorem SubmultSeminorm.sum_le {f : R → ℝ} (hf : SubmultSeminorm f)
    {ι : Type*} (s : Finset ι) (g : ι → R) : f (∑ i ∈ s, g i) ≤ ∑ i ∈ s, f (g i) := by
  classical
  induction s using Finset.induction with
  | empty => rw [Finset.sum_empty, Finset.sum_empty, hf.map_zero]
  | insert a s ha ih =>
      rw [Finset.sum_insert ha, Finset.sum_insert ha]
      exact le_trans (hf.add_le _ _) (add_le_add_left ih _)

/-- **The Taylor tail, bounded per coordinate.**  The form step 2 actually consumes: the index
hypothesis at `α` restricts which `n` appear in the sum, and each surviving term carries
`∏_h G_h^{n_h−i_h}` rather than a single power of a single `G`.

Stated against an arbitrary `SubmultSeminorm` rather than `|·|` on `ℝ`.  The `ℝ` instance is the
one step 2 uses over `ℤ`; the `ℂ` instance (`submultSeminorm_norm_complex`) is what the `𝓞 K` case
needs, because there the estimate has to run at a complex embedding.  Generalising was cheaper
than a second copy, and the `abs_` statements below are now one line each. -/
theorem seminorm_coeff_translate_add_le_prod {f : R → ℝ} (hf : SubmultSeminorm f)
    (α γ : Fin m → R) {G : Fin m → ℝ}
    (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1) (hγ : ∀ h, f (γ h) ≤ G h)
    (P : MvPolynomial (Fin m) R) (i : Fin m →₀ ℕ) :
    f (coeff i (translate (fun j => α j + γ j) P))
      ≤ ∑ n ∈ (translate α P).support, f (coeff n (translate α P))
          * (2 ^ (n.sum fun _ e => e) * ∏ h, (G h) ^ (n h - i h)) := by
  classical
  rw [coeff_translate_add]
  refine le_trans (hf.sum_le _ _) (Finset.sum_le_sum (fun n _ => ?_))
  exact le_trans (hf.mul_le _ _)
    (mul_le_mul_of_nonneg_left
      (seminorm_translateMatrix_le_prod hf γ hG0 hG1 hγ _ n rfl i) (hf.nonneg _))

/-- The real instance. -/
theorem abs_coeff_translate_add_le_prod (α γ : Fin m → ℝ) {G : Fin m → ℝ}
    (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1) (hγ : ∀ h, |γ h| ≤ G h)
    (P : MvPolynomial (Fin m) ℝ) (i : Fin m →₀ ℕ) :
    |coeff i (translate (fun j => α j + γ j) P)|
      ≤ ∑ n ∈ (translate α P).support, |coeff n (translate α P)|
          * (2 ^ (n.sum fun _ e => e) * ∏ h, (G h) ^ (n h - i h)) :=
  seminorm_coeff_translate_add_le_prod submultSeminorm_abs_real α γ hG0 hG1 hγ P i

end PerCoordinate

section Budget

variable {m : ℕ}

/-- The total degree of a multi-index, as a sum over all coordinates. -/
theorem finsuppSum_eq_sum_univ (n : Fin m →₀ ℕ) : (n.sum fun _ e => e) = ∑ h, n h :=
  Finsupp.sum_fintype _ _ (fun _ => rfl)

/-- **The height budget for a translate.**  `f (coeff n (translate α P)) ≤ #box · H · (2B)^{Σ r}`
— the multivariate analogue of `WronskianHeight`'s budget, against any submultiplicative
seminorm. -/
theorem seminorm_coeff_translate_le {f : R → ℝ} (hf : SubmultSeminorm f)
    (α : Fin m → R) {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, f (α h) ≤ B)
    {P : MvPolynomial (Fin m) R} {r : Fin m → ℕ} (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, f (coeff k P) ≤ H) (n : Fin m →₀ ℕ) :
    f (coeff n (translate α P))
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)) := by
  classical
  have hH0 : 0 ≤ H := le_trans (hf.nonneg _) (hH 0)
  have hB0 : (0:ℝ) ≤ 2 * B := by linarith
  have hB1' : (1:ℝ) ≤ 2 * B := by linarith
  have hterm : ∀ k ∈ P.support,
      f (coeff k P * translateMatrix α n k) ≤ H * (2 * B) ^ (∑ h, r h) := by
    intro k hk
    have hkr : ∀ h, k h ≤ r h := fun h => le_trans (monomial_le_degreeOf h hk) (hdeg h)
    have hksum : (k.sum fun _ e => e) ≤ ∑ h, r h := by
      rw [finsuppSum_eq_sum_univ]
      exact Finset.sum_le_sum (fun h _ => hkr h)
    have h1 : f (translateMatrix α n k) ≤ (2 * B) ^ (k.sum fun _ e => e) :=
      seminorm_translateMatrix_le hf α hB1 hα _ k rfl n
    have h2 : (2 * B) ^ (k.sum fun _ e => e) ≤ (2 * B) ^ (∑ h, r h) :=
      pow_le_pow_right₀ hB1' hksum
    exact le_trans (hf.mul_le _ _)
      (mul_le_mul (hH k) (le_trans h1 h2) (hf.nonneg _) hH0)
  calc f (coeff n (translate α P))
      = f (∑ k ∈ P.support, coeff k P * translateMatrix α n k) := by
        rw [coeff_translate_eq_sum]
    _ ≤ ∑ k ∈ P.support, f (coeff k P * translateMatrix α n k) := hf.sum_le _ _
    _ ≤ (P.support.card : ℝ) * (H * (2 * B) ^ (∑ h, r h)) := by
        rw [← nsmul_eq_mul]
        exact Finset.sum_le_card_nsmul _ _ _ hterm
    _ ≤ ((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)) := by
        refine mul_le_mul_of_nonneg_right ?_ (by positivity)
        exact_mod_cast card_support_le_prod_succ hdeg

/-- The real instance. -/
theorem abs_coeff_translate_le (α : Fin m → ℝ) {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |α h| ≤ B)
    {P : MvPolynomial (Fin m) ℝ} {r : Fin m → ℕ} (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, |coeff k P| ≤ H) (n : Fin m →₀ ℕ) :
    |coeff n (translate α P)|
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)) :=
  seminorm_coeff_translate_le submultSeminorm_abs_real α hB1 hα hdeg hH n

/-- **The Taylor tail with every budget folded in.**  Everything step 2 needs except the
arithmetic of the exponents: the index hypothesis at `α` restricts the sum, the degree bound
counts it, the height bound sizes each term, and `S` is whatever uniform bound the caller can
prove on `∏_h G_h^{n_h−i_h}` over the surviving multi-indices. -/
theorem seminorm_coeff_translate_add_le_index {f : R → ℝ} (hf : SubmultSeminorm f)
    (r : Fin m → ℕ) (α γ : Fin m → R)
    {G : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1) (hγ : ∀ h, f (γ h) ≤ G h)
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, f (α h) ≤ B)
    {P : MvPolynomial (Fin m) R} (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, f (coeff k P) ≤ H)
    {μ : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α P)
    (i : Fin m →₀ ℕ) {S : ℝ} (hS0 : 0 ≤ S)
    (hS : ∀ n : Fin m →₀ ℕ, (∀ h, n h ≤ r h) → μ ≤ idxWeight r n →
      (∏ h, (G h) ^ (n h - i h)) ≤ S) :
    f (coeff i (translate (fun j => α j + γ j) P))
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ)
        * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
            * ((2 : ℝ) ^ (∑ h, r h) * S)) := by
  classical
  have hH0 : 0 ≤ H := le_trans (hf.nonneg _) (hH 0)
  have hB0 : (0:ℝ) ≤ 2 * B := by linarith
  have hdegT : ∀ h, degreeOf h (translate α P) ≤ r h := by
    intro h
    rw [degreeOf_translate_eq]
    exact hdeg h
  set CH : ℝ := ((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)) with hCH
  have hCH0 : 0 ≤ CH := by rw [hCH]; positivity
  have hterm : ∀ n ∈ (translate α P).support,
      f (coeff n (translate α P)) * ((2:ℝ) ^ (n.sum fun _ e => e) * ∏ h, (G h) ^ (n h - i h))
        ≤ CH * ((2 : ℝ) ^ (∑ h, r h) * S) := by
    intro n hn
    have hnr : ∀ h, n h ≤ r h := fun h => le_trans (monomial_le_degreeOf h hn) (hdegT h)
    have hnsum : (n.sum fun _ e => e) ≤ ∑ h, r h := by
      rw [finsuppSum_eq_sum_univ]
      exact Finset.sum_le_sum (fun h _ => hnr h)
    have hμn : μ ≤ idxWeight r n := by
      have := (le_index_iff r α P _).mp hidx n hn
      exact_mod_cast this
    have h1 : f (coeff n (translate α P)) ≤ CH := seminorm_coeff_translate_le hf α hB1 hα hdeg hH n
    have h2 : (2:ℝ) ^ (n.sum fun _ e => e) ≤ (2:ℝ) ^ (∑ h, r h) :=
      pow_le_pow_right₀ (by norm_num) hnsum
    have h3 : (∏ h, (G h) ^ (n h - i h)) ≤ S := hS n hnr hμn
    have h4 : (0:ℝ) ≤ ∏ h, (G h) ^ (n h - i h) :=
      Finset.prod_nonneg (fun h _ => pow_nonneg (hG0 h) _)
    refine mul_le_mul h1 ?_ (by positivity) hCH0
    exact mul_le_mul h2 h3 h4 (by positivity)
  calc f (coeff i (translate (fun j => α j + γ j) P))
      ≤ ∑ n ∈ (translate α P).support, f (coeff n (translate α P))
          * ((2:ℝ) ^ (n.sum fun _ e => e) * ∏ h, (G h) ^ (n h - i h)) :=
        seminorm_coeff_translate_add_le_prod hf α γ hG0 hG1 hγ P i
    _ ≤ ((translate α P).support.card : ℝ) * (CH * ((2 : ℝ) ^ (∑ h, r h) * S)) := by
        rw [← nsmul_eq_mul]
        exact Finset.sum_le_card_nsmul _ _ _ hterm
    _ ≤ ((∏ h, (r h + 1) : ℕ) : ℝ) * (CH * ((2 : ℝ) ^ (∑ h, r h) * S)) := by
        refine mul_le_mul_of_nonneg_right ?_ (by positivity)
        exact_mod_cast card_support_le_prod_succ hdegT

/-- The real instance. -/
theorem abs_coeff_translate_add_le_index (r : Fin m → ℕ) (α γ : Fin m → ℝ)
    {G : Fin m → ℝ} (hG0 : ∀ h, 0 ≤ G h) (hG1 : ∀ h, G h ≤ 1) (hγ : ∀ h, |γ h| ≤ G h)
    {B : ℝ} (hB1 : 1 ≤ B) (hα : ∀ h, |α h| ≤ B)
    {P : MvPolynomial (Fin m) ℝ} (hdeg : ∀ h, degreeOf h P ≤ r h)
    {H : ℝ} (hH : ∀ k, |coeff k P| ≤ H)
    {μ : ℚ} (hidx : ((μ : ℚ) : WithTop ℚ) ≤ index r α P)
    (i : Fin m →₀ ℕ) {S : ℝ} (hS0 : 0 ≤ S)
    (hS : ∀ n : Fin m →₀ ℕ, (∀ h, n h ≤ r h) → μ ≤ idxWeight r n →
      (∏ h, (G h) ^ (n h - i h)) ≤ S) :
    |coeff i (translate (fun j => α j + γ j) P)|
      ≤ ((∏ h, (r h + 1) : ℕ) : ℝ)
        * ((((∏ h, (r h + 1) : ℕ) : ℝ) * (H * (2 * B) ^ (∑ h, r h)))
            * ((2 : ℝ) ^ (∑ h, r h) * S)) :=
  seminorm_coeff_translate_add_le_index submultSeminorm_abs_real r α γ hG0 hG1 hγ hB1 hα
    hdeg hH hidx i hS0 hS

end Budget

end MvPolynomial
