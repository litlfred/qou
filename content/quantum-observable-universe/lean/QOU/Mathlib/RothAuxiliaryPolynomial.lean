/-
# Towards the auxiliary polynomial: the index as a linear system, and the counting

Roth's theorem needs a polynomial `P ∈ ℤ[x₁,…,x_m]` of bounded degree and height whose index at
`(α,…,α)` is large.  It is built by **Siegel's lemma**: the index condition is a system of
linear equations in `P`'s coefficients, and a system with fewer equations than unknowns has a
small non-zero solution.  Mathlib supplies the engine —
`NumberTheory.NumberField.House.exists_ne_zero_int_vec_house_le`, Siegel over a number field,
with the `house` bound already proved — so what this file does is the two things the engine
cannot: say what the system *is*, and show it is underdetermined.

## Part 1 — the system

`le_index_iff_coeff_eq_zero` turns `c ≤ index d α P` into "every translate-coefficient of weight
below `c` vanishes", and `coeff_translate_eq_sum` shows each of those is linear in `P`'s
coefficients with matrix `translateMatrix`.

⚠ `translateMatrix` is defined as `coeff i (translate α (monomial n 1))` rather than by the
closed form `∏_h binom(n_h, i_h)·α_h^{n_h−i_h}`.  The closed form is a multivariate binomial
theorem and is **not needed for the system** — only for the `house` bound, which is the piece
still missing.  `RothIndex` records that `coeff_translate` does not exist at this Mathlib pin.

## Part 2 — the counting

The equations are indexed by the multi-indices of weight below the threshold, so the system is
underdetermined exactly when those are a small fraction of the box.  That is a variance
computation, and it is done here exactly:

* `sum_centred_eq_zero` / `sum_centred_sq` — the one-coordinate moments, `0` and
  `(r+1)(r+2)/(12r)`;
* `sum_piFinset_single` / `sum_piFinset_pair_eq_zero` — the product structure, giving the
  marginals and the vanishing of the cross terms;
* `sum_centredWeight_sq` — the second moment, **exactly**: only the `m` diagonal terms survive;
* `card_centredWeight_le` — Chebyshev.

⚠⚠ **The cross terms are load-bearing.**  Cauchy–Schwarz on `(∑_h u_h)² ≤ m·∑_h u_h²` bounds the
variance by `m²/4` instead of `m/4`, and with Roth's `λ = εm` that turns the conclusion from
`1/(4ε²m)` into `1/(4ε²)` — a constant, with no `m` left to grow.  Since the whole point is to
take `m` large enough that `deg α / (4ε²m) < 1`, the cheaper inequality destroys the argument
rather than weakening it.  This was checked before the product lemmas were written, not after.

⚠ `card_centredWeight_le` carries `0 ≤ lam` and is **false without it**: at negative `lam` the
filter `centredWeight ≤ -lam` is a *weaker* condition than the square bound it is compared
against.  Found by `nlinarith` refusing the step, which is the cheapest way this arc has yet
found a statement-stronger-than-the-truth defect.

## Part 3 — the system is underdetermined, and how large `m` must be

`card_lt_card_idxBox_of_eps`: at index threshold `m(½ − ε)` the vanishing conditions are strictly
fewer than the coefficients as soon as `m > 1/(4ε²)`.  That is Roth's "take `m` sufficiently
large" with the bound explicit, and it is what the variance computation was for — the threshold
scales with `m` while the standard deviation scales with `√m`.

⚠ **The degree of `α` does not appear.**  I expected it to: classically each `K`-linear equation
is `deg α` equations over `ℚ`, so the count should be `deg α · #conditions < #unknowns`.  But
Mathlib's `exists_ne_zero_int_vec_house_le` takes `p < q` with `p`, `q` the **`K`-counts**, and
discharges the `ℚ`-counts `p·h`, `q·h` internally (`h = finrank ℚ K`).  Since `p·h < q·h ⟺ p < q`,
the degree cancels out of the counting condition entirely.  It re-enters only through the
`house` bound on the matrix entries — which is the piece still missing, so this is a
simplification of the *counting*, not of the theorem.

## What remains

* the `house` bound on `translateMatrix`, which does need the closed form — and is where
  `deg α` actually enters;
* the bridge from `Fin m → ℕ` (used here) to `σ →₀ ℕ` (used by `index`);
* the application of Siegel itself, now that `p < q` is available.

⚠ Not Mathlib-only: imports `QOU/Mathlib/RothGammaProducer.lean`.
-/
import QOU.Mathlib.RothGammaProducer

namespace MvPolynomial

open Finset


variable {σ : Type*} {R : Type*} [CommRing R]

/-- **The index condition, as equations.**  `c ≤ index d α P` says exactly that every
translate-coefficient of weight below `c` vanishes — a finite set of linear conditions on `P`. -/
theorem le_index_iff_coeff_eq_zero [DecidableEq σ] (d : σ → ℕ) (α : σ → R)
    (P : MvPolynomial σ R) (c : ℚ) :
    ((c : ℚ) : WithTop ℚ) ≤ index d α P ↔
      ∀ i, idxWeight d i < c → coeff i (translate α P) = 0 := by
  rw [le_index_iff]
  constructor
  · intro h i hi
    by_contra hne
    have := h i (mem_support_iff.mpr hne)
    rw [WithTop.coe_le_coe] at this
    exact absurd hi (not_lt.mpr this)
  · intro h i hi
    rw [WithTop.coe_le_coe]
    by_contra hlt
    exact (mem_support_iff.mp hi) (h i (not_le.mp hlt))

/-- **The translate matrix.**  The entry at `(i, n)` is the coefficient of `x^i` in the
translate of the bare monomial `x^n` — Roth's `binom(n,i)·α^{n−i}`, defined without needing the
closed form. -/
noncomputable def translateMatrix (α : σ → R) (i n : σ →₀ ℕ) : R :=
  coeff i (translate α (monomial n 1))

/-- **The equations are linear in `P`'s coefficients**, with `translateMatrix` as the matrix.
This is the input Siegel's lemma takes. -/
theorem coeff_translate_eq_sum [DecidableEq σ] (α : σ → R) (P : MvPolynomial σ R) (i : σ →₀ ℕ) :
    coeff i (translate α P) = ∑ n ∈ P.support, coeff n P * translateMatrix α i n := by
  classical
  have hP : translate α P = ∑ v ∈ P.support, translate α (monomial v (coeff v P)) := by
    conv_lhs => rw [P.as_sum]
    simp only [translate, map_sum]
  rw [hP, coeff_sum]
  refine Finset.sum_congr rfl fun v _ => ?_
  have hmono : (monomial v (coeff v P) : MvPolynomial σ R) = C (coeff v P) * monomial v 1 := by
    rw [C_mul_monomial, mul_one]
  rw [hmono, translate, map_mul, aeval_C, ← translate, translateMatrix]
  simp [coeff_C_mul]


/-- Gauss, over `ℚ`. -/
theorem sum_range_cast (n : ℕ) : ∑ j ∈ range (n + 1), (j : ℚ) = n * (n + 1) / 2 := by
  induction n with
  | zero => simp
  | succ k ih => rw [sum_range_succ, ih]; push_cast; ring

theorem sum_range_sq_cast (n : ℕ) :
    ∑ j ∈ range (n + 1), (j : ℚ) ^ 2 = n * (n + 1) * (2 * n + 1) / 6 := by
  induction n with
  | zero => simp
  | succ k ih => rw [sum_range_succ, ih]; push_cast; ring

/-- **First moment, one coordinate: zero.**  This is what kills the cross terms. -/
theorem sum_centred_eq_zero {r : ℕ} (hr : r ≠ 0) :
    ∑ j ∈ range (r + 1), ((j : ℚ) / (r : ℚ) - 1 / 2) = 0 := by
  have hrQ : (r : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hr
  have hsplit : ∀ j : ℕ, ((j : ℚ) / (r : ℚ) - 1 / 2) = (1 / (r : ℚ)) * (j : ℚ) - 1 / 2 := by
    intro j; ring
  rw [Finset.sum_congr rfl (fun j _ => hsplit j), sum_sub_distrib, ← Finset.mul_sum,
    sum_range_cast]
  simp only [sum_const, card_range, nsmul_eq_mul]
  push_cast
  field_simp
  ring

/-- **Second moment, one coordinate.**  `(r+1)(r+2)/(12r)` — at `r = 1` and `r = 2` it is `1/2`
both times, which is the arithmetic check worth doing by hand. -/
theorem sum_centred_sq {r : ℕ} (hr : r ≠ 0) :
    ∑ j ∈ range (r + 1), ((j : ℚ) / (r : ℚ) - 1 / 2) ^ 2
      = ((r : ℚ) + 1) * ((r : ℚ) + 2) / (12 * (r : ℚ)) := by
  have hrQ : (r : ℚ) ≠ 0 := Nat.cast_ne_zero.mpr hr
  have hexp : ∀ j : ℕ, ((j : ℚ) / (r : ℚ) - 1 / 2) ^ 2
      = (1 / (r : ℚ) ^ 2) * (j : ℚ) ^ 2 - (1 / (r : ℚ)) * (j : ℚ) + 1 / 4 := by
    intro j; field_simp; ring
  rw [Finset.sum_congr rfl (fun j _ => hexp j), sum_add_distrib, sum_sub_distrib,
    ← Finset.mul_sum, ← Finset.mul_sum, sum_range_cast, sum_range_sq_cast]
  simp only [sum_const, card_range, nsmul_eq_mul]
  push_cast
  field_simp
  ring
/-- **A single-coordinate marginal over a product box.** -/
theorem sum_piFinset_single {m : ℕ} (t : Fin m → Finset ℕ) (g : ℕ → ℚ) (h : Fin m) :
    ∑ x ∈ Fintype.piFinset t, g (x h)
      = (∑ j ∈ t h, g j) * ∏ i ∈ univ.erase h, ((t i).card : ℚ) := by
  classical
  have key := Finset.prod_univ_sum t (fun i j => if i = h then g j else 1)
  have hin : ∀ x : Fin m → ℕ, (∏ i, if i = h then g (x i) else 1) = g (x h) := by
    intro x; simp
  have hout : ∀ i : Fin m, (∑ j ∈ t i, if i = h then g j else 1)
      = if i = h then (∑ j ∈ t h, g j) else ((t i).card : ℚ) := by
    intro i; split_ifs with hi
    · subst hi; rfl
    · simp
  simp only [hin] at key
  rw [← key, Finset.prod_congr rfl (fun i (_ : i ∈ univ) => hout i),
    ← Finset.prod_erase_mul univ _ (mem_univ h),
    Finset.prod_congr rfl (fun i hi => if_neg (Finset.ne_of_mem_erase hi))]
  simp
  ring

/-- **The cross terms vanish.**  Independence of the coordinates, in the only form the variance
computation needs: if one factor has zero marginal sum, the pair sum is zero. -/
theorem sum_piFinset_pair_eq_zero {m : ℕ} (t : Fin m → Finset ℕ) (f g : ℕ → ℚ)
    {h k : Fin m} (hne : h ≠ k) (hf : ∑ j ∈ t h, f j = 0) :
    ∑ x ∈ Fintype.piFinset t, f (x h) * g (x k) = 0 := by
  classical
  set F : Fin m → ℕ → ℚ := fun i j => if i = h then f j else if i = k then g j else 1 with hF
  have key := Finset.prod_univ_sum t F
  have hin : ∀ x : Fin m → ℕ, (∏ i, F i (x i)) = f (x h) * g (x k) := by
    intro x
    have hsub : ∏ i ∈ ({h, k} : Finset (Fin m)), F i (x i) = ∏ i, F i (x i) := by
      refine Finset.prod_subset (Finset.subset_univ _) ?_
      intro i _ hi
      simp only [Finset.mem_insert, Finset.mem_singleton, not_or] at hi
      simp [hF, hi.1, hi.2]
    rw [← hsub, Finset.prod_pair hne]
    simp [hF, Ne.symm hne]
  have hzero : (∏ i, ∑ j ∈ t i, F i j) = 0 := by
    refine Finset.prod_eq_zero (Finset.mem_univ h) ?_
    simpa [hF] using hf
  calc ∑ x ∈ Fintype.piFinset t, f (x h) * g (x k)
      = ∑ x ∈ Fintype.piFinset t, ∏ i, F i (x i) :=
        Finset.sum_congr rfl (fun x _ => (hin x).symm)
    _ = ∏ i, ∑ j ∈ t i, F i j := key.symm
    _ = 0 := hzero

/-- The box of multi-indices bounded by `r`. -/
def idxBox {m : ℕ} (r : Fin m → ℕ) : Finset (Fin m → ℕ) :=
  Fintype.piFinset (fun h => range (r h + 1))

/-- The **centred** Roth weight: `∑ x_h/r_h − m/2`. -/
def centredWeight {m : ℕ} (r : Fin m → ℕ) (x : Fin m → ℕ) : ℚ :=
  ∑ h, ((x h : ℚ) / (r h : ℚ) - 1 / 2)

theorem card_idxBox {m : ℕ} (r : Fin m → ℕ) :
    (idxBox r).card = ∏ h, (r h + 1) := by
  simp [idxBox, Fintype.card_piFinset]

/-- **The second moment, exactly.**  The cross terms are gone; only the `m` diagonal terms
survive, each a one-coordinate second moment times the size of the other coordinates. -/
theorem sum_centredWeight_sq {m : ℕ} (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0) :
    ∑ x ∈ idxBox r, (centredWeight r x) ^ 2
      = ∑ h, (∑ j ∈ range (r h + 1), ((j : ℚ) / (r h : ℚ) - 1 / 2) ^ 2)
          * ∏ i ∈ univ.erase h, ((r i : ℚ) + 1) := by
  classical
  have hexpand : ∀ x : Fin m → ℕ, (centredWeight r x) ^ 2
      = ∑ h, ∑ k, ((x h : ℚ) / (r h : ℚ) - 1 / 2) * ((x k : ℚ) / (r k : ℚ) - 1 / 2) := by
    intro x
    rw [centredWeight, sq, Finset.sum_mul_sum]
  rw [Finset.sum_congr rfl (fun x _ => hexpand x), Finset.sum_comm]
  refine Finset.sum_congr rfl fun h _ => ?_
  rw [Finset.sum_comm]
  rw [Finset.sum_eq_single h]
  · have hmarg := sum_piFinset_single (fun i => range (r i + 1))
      (fun j => ((j : ℚ) / (r h : ℚ) - 1 / 2) * ((j : ℚ) / (r h : ℚ) - 1 / 2)) h
    rw [idxBox, hmarg]
    congr 1
    · exact Finset.sum_congr rfl fun j _ => (sq _).symm
    · exact Finset.prod_congr rfl fun i _ => by simp
  · intro k _ hk
    rw [idxBox]
    exact sum_piFinset_pair_eq_zero (fun i => range (r i + 1))
      (fun j => ((j : ℚ) / (r h : ℚ) - 1 / 2))
      (fun j => ((j : ℚ) / (r k : ℚ) - 1 / 2))
      (Ne.symm hk) (sum_centred_eq_zero (hr h))
  · intro hcon; exact absurd (Finset.mem_univ h) hcon

/-- **Variance at most `m/4`.**  Each coordinate contributes `(r+2)/(12r) ≤ 1/4`, with equality
at `r = 1`; the true asymptote is `1/12`, and `1/4` is the price of allowing `r = 1`. -/
theorem sum_centredWeight_sq_le {m : ℕ} (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0) :
    ∑ x ∈ idxBox r, (centredWeight r x) ^ 2 ≤ (m : ℚ) / 4 * ((idxBox r).card : ℚ) := by
  classical
  rw [sum_centredWeight_sq r hr, card_idxBox]
  have hterm : ∀ h : Fin m,
      (∑ j ∈ range (r h + 1), ((j : ℚ) / (r h : ℚ) - 1 / 2) ^ 2)
        * ∏ i ∈ univ.erase h, ((r i : ℚ) + 1)
      ≤ 1 / 4 * ((∏ i, (r i + 1) : ℕ) : ℚ) := by
    intro h
    have hQ : ((∏ i, (r i + 1) : ℕ) : ℚ)
        = (∏ i ∈ univ.erase h, ((r i : ℚ) + 1)) * ((r h : ℚ) + 1) := by
      push_cast
      exact (Finset.prod_erase_mul univ (fun i => ((r i : ℚ) + 1)) (mem_univ h)).symm
    rw [sum_centred_sq (hr h), hQ]
    have hr1 : (1 : ℚ) ≤ (r h : ℚ) := by
      have := Nat.one_le_iff_ne_zero.mpr (hr h); exact_mod_cast this
    have hP : (0 : ℚ) ≤ ∏ i ∈ univ.erase h, ((r i : ℚ) + 1) :=
      Finset.prod_nonneg fun i _ => by positivity
    rw [div_mul_eq_mul_div, div_le_iff₀ (by linarith : (0:ℚ) < 12 * (r h : ℚ))]
    nlinarith [mul_nonneg hP (by linarith : (0:ℚ) ≤ (r h : ℚ) - 1),
      mul_nonneg (mul_nonneg hP (by linarith : (0:ℚ) ≤ (r h : ℚ) - 1))
        (by linarith : (0:ℚ) ≤ (r h : ℚ))]
  calc ∑ h, (∑ j ∈ range (r h + 1), ((j : ℚ) / (r h : ℚ) - 1 / 2) ^ 2)
          * ∏ i ∈ univ.erase h, ((r i : ℚ) + 1)
      ≤ ∑ _h : Fin m, 1 / 4 * ((∏ i, (r i + 1) : ℕ) : ℚ) :=
        Finset.sum_le_sum fun h _ => hterm h
    _ = (m : ℚ) / 4 * ((∏ i, (r i + 1) : ℕ) : ℚ) := by
        rw [Finset.sum_const, card_univ, Fintype.card_fin, nsmul_eq_mul]; ring

/-- **Chebyshev, for the Roth index distribution.**  The multi-indices of weight at least `λ`
below the mean `m/2` are a fraction at most `m/(4λ²)` of the box.

⚠ The `m` in the numerator is the whole point.  Cauchy–Schwarz on `(∑ u_h)² ≤ m ∑ u_h²` would
give `m²/(4λ²)`, and with Roth's `λ = εm` that reads `1/(4ε²)` — a constant, with no `m` left to
grow.  The variance being `O(m)` rather than `O(m²)` is exactly what lets `m` be chosen large
enough to beat the degree of `α`, so the vanishing cross terms are load-bearing and not a
tidiness. -/
theorem card_centredWeight_le {m : ℕ} (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    {lam : ℚ} (hlam : 0 ≤ lam) :
    ((((idxBox r).filter (fun x => centredWeight r x ≤ -lam)).card : ℚ)) * lam ^ 2
      ≤ (m : ℚ) / 4 * ((idxBox r).card : ℚ) := by
  classical
  set S := (idxBox r).filter (fun x => centredWeight r x ≤ -lam) with hS
  have hlow : ∀ x ∈ S, lam ^ 2 ≤ (centredWeight r x) ^ 2 := by
    intro x hx
    rw [hS, Finset.mem_filter] at hx
    nlinarith [mul_nonneg (by linarith [hx.2] : (0:ℚ) ≤ -centredWeight r x - lam)
      (by linarith [hx.2] : (0:ℚ) ≤ -centredWeight r x + lam)]
  have h1 : (S.card : ℚ) * lam ^ 2 ≤ ∑ x ∈ S, (centredWeight r x) ^ 2 := by
    calc (S.card : ℚ) * lam ^ 2 = ∑ _x ∈ S, lam ^ 2 := by
          rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ ∑ x ∈ S, (centredWeight r x) ^ 2 := Finset.sum_le_sum hlow
  have h2 : ∑ x ∈ S, (centredWeight r x) ^ 2 ≤ ∑ x ∈ idxBox r, (centredWeight r x) ^ 2 :=
    Finset.sum_le_sum_of_subset_of_nonneg (Finset.filter_subset _ _)
      (fun x _ _ => sq_nonneg _)
  exact le_trans h1 (le_trans h2 (sum_centredWeight_sq_le r hr))

/-- **Non-vacuity of the counting**, at `m = 1`, `r = 1`, `λ = 1/2`.  The box is `{0, 1}`, the
centred weights are `∓1/2`, so exactly one index sits at or below `−1/2` and the bound reads
`1 · ¼ ≤ ¼ · 2` — tight to within a factor `2`, which is the `r = 1` end of `(r+2)/(12r) ≤ ¼`. -/
theorem card_centredWeight_le_witness :
    ((((idxBox (fun _ : Fin 1 => 1)).filter
        (fun x => centredWeight (fun _ : Fin 1 => 1) x ≤ -(1 / 2 : ℚ))).card : ℚ))
        * (1 / 2 : ℚ) ^ 2
      ≤ ((1 : ℕ) : ℚ) / 4 * (((idxBox (fun _ : Fin 1 => 1)).card : ℚ)) :=
  card_centredWeight_le _ (fun _ => one_ne_zero) (by norm_num)

/-- …and the box in that witness really does have two elements, so the count is not `0 ≤ 0`. -/
theorem card_idxBox_witness : (idxBox (fun _ : Fin 1 => 1)).card = 2 := by
  rw [card_idxBox]; simp


theorem card_idxBox_pos {m : ℕ} (r : Fin m → ℕ) : 0 < (idxBox r).card := by
  rw [card_idxBox]
  exact Finset.prod_pos fun i _ => Nat.succ_pos _

/-- **The system is underdetermined.**  Fewer vanishing conditions than coefficients, as soon
as `m < 4λ²`. -/
theorem card_lt_card_idxBox {m : ℕ} (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    {lam : ℚ} (hlam : 0 < lam) (hm : (m : ℚ) < 4 * lam ^ 2) :
    ((idxBox r).filter (fun x => centredWeight r x ≤ -lam)).card < (idxBox r).card := by
  classical
  by_contra hcon
  push_neg at hcon
  have hsub : ((idxBox r).filter (fun x => centredWeight r x ≤ -lam)).card ≤ (idxBox r).card :=
    Finset.card_filter_le _ _
  have heq : ((idxBox r).filter (fun x => centredWeight r x ≤ -lam)).card = (idxBox r).card :=
    le_antisymm hsub hcon
  have hQpos : (0 : ℚ) < ((idxBox r).card : ℚ) := by
    exact_mod_cast card_idxBox_pos r
  have hch := card_centredWeight_le r hr hlam.le
  rw [heq] at hch
  nlinarith [hQpos, hch, hm]

/-- **Where `m` gets chosen.**  For an index threshold `m(½ − ε)` — i.e. `centredWeight ≤ −εm` —
the system is underdetermined as soon as `m > 1/(4ε²)`.

This is Roth's "take `m` sufficiently large", with the bound made explicit, and it is the whole
purpose of the variance computation: the threshold scales with `m` while the standard deviation
scales with `√m`, so the fraction below it goes to zero. -/
theorem card_lt_card_idxBox_of_eps {m : ℕ} (r : Fin m → ℕ) (hr : ∀ h, r h ≠ 0)
    {ε : ℚ} (hε : 0 < ε) (hm : 1 < 4 * ε ^ 2 * (m : ℚ)) :
    ((idxBox r).filter (fun x => centredWeight r x ≤ -(ε * (m : ℚ)))).card
      < (idxBox r).card := by
  have hmpos : (0 : ℚ) < (m : ℚ) := by nlinarith [sq_nonneg ε]
  refine card_lt_card_idxBox r hr (by positivity) ?_
  nlinarith [hmpos, hm]

/-- **Non-vacuity of the `ε` form**, at `ε = ¼`, `m = 5`, `r ≡ 1`: the threshold `1 < 4ε²m`
reads `1 < 5/4`.

The box has `2⁵ = 32` points (`card_idxBox_five_witness`, checked).  The filtered set is the
multi-indices with `∑ x_h ≤ 1`, since `centredWeight x = ∑ x_h − 5/2` and the threshold is
`−5/4`; that is **six** of them, and the strict inequality is not a near miss.

⚠ The `6` is a hand count, **not** checked by the build: `decide` gets stuck on this goal because
the filter's `Decidable` instance does not reduce (it goes through `Rat.instDecidableLe` and then
`Finset.filter` over `Fintype.piFinset` and stalls).  Recorded rather than quietly asserted —
a number in a docstring that the build has no opinion about is what corrections 17 and 24 in
this arc were both about. -/
theorem card_lt_card_idxBox_of_eps_witness :
    ((idxBox (fun _ : Fin 5 => 1)).filter
        (fun x => centredWeight (fun _ : Fin 5 => 1) x ≤ -((1 / 4 : ℚ) * ((5 : ℕ) : ℚ)))).card
      < (idxBox (fun _ : Fin 5 => 1)).card :=
  card_lt_card_idxBox_of_eps _ (fun _ => one_ne_zero) (by norm_num) (by norm_num)

/-- The box in the witness above really does have `2⁵ = 32` points, so the strict inequality is
not `0 < 0`.  ⚠ This part *is* checked; the count of the filtered set is not — see above. -/
theorem card_idxBox_five_witness : (idxBox (fun _ : Fin 5 => 1)).card = 32 := by
  rw [card_idxBox]; simp

end MvPolynomial
