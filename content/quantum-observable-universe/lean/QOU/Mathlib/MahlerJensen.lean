/-
  **The Mahler measure of a linear factor** — the cornerstone of the Jensen form.

  Bean `qou-4lbh`.  ⚠ Mathlib-style, Mathlib imports only, no QOU dependency: liftable
  verbatim.

  ═══ ⚠ THIS REVERSES A RECOMMENDATION ═══

  `qou-4lbh` recorded that the last open step of Roth's lemma — bounding the heights of the
  factors `φₖ, ψₖ` of a separated `P = ∑ₖ φₖ(x)ψₖ(y)` — needs Gelfond's inequality, and that
  the choice was between **filling Mathlib's missing Mahler bridges upstream** and a
  **bare-hands Gelfond inequality on `ℤ[X]`**.  The recommendation given was bare-hands, to
  avoid `ℂ[X]` and circle averages.

  **That was the wrong call, and measuring says so.**  Two things:

  * Gelfond's standard proof *goes through* the Mahler measure.  "Bare-hands" is not a
    shortcut around it; it is a re-derivation of it.
  * Mathlib already has the hard analytic content —
    `circleAverage_log_norm_sub_const_eq_posLog`, i.e. Jensen's formula for a single root.
    What was missing is only its connection to `mahlerMeasure`, which is the one theorem
    below.

  So the upstream route is much cheaper than it looked.  What remains for the Jensen form
  `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)` is the factorization of a complex polynomial into
  linear factors together with `mahlerMeasure_mul`, both of which Mathlib has.

  ═══ WHAT THIS DOES NOT YET GIVE ═══

  ⚠ The Jensen form is one of *two* bridges.  **Both are now here**, but with a caveat on
  the second that matters — read it before citing anything below.

  * **The Jensen form** `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)` — `mahlerMeasure_X_sub_C`
    below for one root, `mahlerMeasure_eq_leadingCoeff_mul_prod_roots` for the product.
    ✔ **done.**
  * **The coefficient bridge.**  `mahlerMeasure_le_max_one_sum_norm_coeff` below gives
    `M(p) ≤ max(1, ‖p‖₁)`.  ⚠ **That is weaker than Landau's inequality and must not be
    cited as it.**  Landau is `M(P) ≤ ‖P‖₂ ≤ √(deg+1) · H(P)`, proved through Parseval; the
    bound below goes through the crude sup bound on the circle, and `‖p‖₁ ≤ (deg+1) · H(p)`
    loses a factor `√(deg+1)` against it.

    It is nevertheless enough downstream.  Gelfond then reads `∏ H(pᵢ) ≤ 2^{deg}(deg+1)H(p)`
    rather than `2^{deg}√(deg+1)H(p)`, and that extra polynomial factor is invisible beside
    the exponential constants Roth's lemma already carries.
  * **The reverse bridge** `‖coeff k p‖ ≤ 2^{deg p} · M(p)` —
    `norm_coeff_le_two_pow_mul_mahlerMeasure`.  ✔ **done**, by Vieta over the Jensen form.

  With all three, Gelfond's inequality is assembly: `M` is multiplicative over a
  factorization (Mathlib's `mahlerMeasure_mul`), the reverse bridge takes each factor's
  measure up to its height, and the coefficient bound brings the product's measure down from
  its height.
-/
import Mathlib.Analysis.Polynomial.MahlerMeasure
import Mathlib.Analysis.SpecialFunctions.Integrals.PosLogEqCircleAverage
import Mathlib.Analysis.Complex.Polynomial.Basic
import Mathlib.RingTheory.Polynomial.Vieta
import Mathlib.Data.Nat.Choose.Bounds
import Mathlib.Algebra.Order.BigOperators.GroupWithZero.Multiset

open Real Finset

namespace Polynomial

/-- **The Mahler measure of a linear factor:** `M(X − a) = max(1, ‖a‖)`.

This is Jensen's formula for a single root.  Mathlib supplies the analytic content
(`circleAverage_log_norm_sub_const_eq_posLog`) but does not connect it to `mahlerMeasure`. -/
theorem mahlerMeasure_X_sub_C (a : ℂ) :
    (X - C a : ℂ[X]).mahlerMeasure = max 1 ‖a‖ := by
  have hne : (X - C a : ℂ[X]) ≠ 0 := X_sub_C_ne_zero a
  have hpos : (0 : ℝ) < max 1 ‖a‖ := lt_of_lt_of_le one_pos (le_max_left _ _)
  have hlog : (X - C a : ℂ[X]).logMahlerMeasure = Real.log (max 1 ‖a‖) := by
    rw [logMahlerMeasure_def]
    have heval : (fun x : ℂ => Real.log ‖eval x (X - C a : ℂ[X])‖)
        = fun x : ℂ => Real.log ‖x - a‖ := by
      funext x
      simp
    rw [heval, circleAverage_log_norm_sub_const_eq_posLog,
      posLog_eq_log_max_one (norm_nonneg a)]
  rw [mahlerMeasure, if_pos hne, hlog, Real.exp_log hpos]

/-! ### The Jensen form -/

/-- **The Jensen form of the Mahler measure:** `M(P) = ‖lead P‖ · ∏ max(1, ‖root‖)`, the
product running over the roots of `P` with multiplicity.

Assembly rather than analysis, exactly as predicted: `mahlerMeasure_X_sub_C` for a single
factor, Mathlib's `prod_mahlerMeasure_eq_mahlerMeasure_prod` for the product, and the
factorization `C (lead P) * ∏ (X − aᵢ) = P` which holds over `ℂ` because it is algebraically
closed.

No `P ≠ 0` hypothesis is needed: at `P = 0` the left side is `0` by definition and the right
side is `‖0‖ * 1 = 0`, since `(0 : ℂ[X]).roots` is the empty multiset. -/
theorem mahlerMeasure_eq_leadingCoeff_mul_prod_roots (p : ℂ[X]) :
    p.mahlerMeasure = ‖p.leadingCoeff‖ * (p.roots.map (fun a => max 1 ‖a‖)).prod := by
  have hroots : Multiset.card p.roots = p.natDegree :=
    splits_iff_card_roots.mp (IsAlgClosed.splits_codomain p)
  have hmap : (p.roots.map (fun a => (X - C a : ℂ[X]))).map (fun q => q.mahlerMeasure)
      = p.roots.map (fun a => max 1 ‖a‖) := by
    rw [Multiset.map_map]
    exact Multiset.map_congr rfl (fun a _ => mahlerMeasure_X_sub_C a)
  conv_lhs => rw [← C_leadingCoeff_mul_prod_multiset_X_sub_C hroots]
  rw [mahlerMeasure_mul, mahlerMeasure_const, prod_mahlerMeasure_eq_mahlerMeasure_prod, hmap]

/-- **`M(qX − a) = max(‖q‖, ‖a‖)`.**

This is the shape the `m = 1` case of Roth's lemma measures a rational `a/q` against, and
the bean recorded it as absent.  It is the Jensen form at a single root: `qX − a` is
`C q * (X − C (a/q))`, so its measure is `‖q‖ · max(1, ‖a‖/‖q‖) = max(‖q‖, ‖a‖)`. -/
theorem mahlerMeasure_C_mul_X_sub_C {q a : ℂ} (hq : q ≠ 0) :
    (C q * X - C a : ℂ[X]).mahlerMeasure = max ‖q‖ ‖a‖ := by
  have hfac : (C q * X - C a : ℂ[X]) = C q * (X - C (a / q)) := by
    rw [mul_sub, ← C_mul, mul_div_cancel₀ _ hq]
  have hqn : (0 : ℝ) < ‖q‖ := norm_pos_iff.mpr hq
  rw [hfac, mahlerMeasure_mul, mahlerMeasure_const, mahlerMeasure_X_sub_C, norm_div,
    mul_max_of_nonneg _ _ (le_of_lt hqn), mul_one, mul_div_cancel₀ _ (ne_of_gt hqn)]

/-! ### From the Jensen form to coefficient heights, by Vieta

The reverse of the bound in the next section: this one goes *up* from `M(p)` to the
coefficients, and it is the direction Gelfond applies to each factor. -/

/-- The norm of a multiset product is the product of the norms. -/
theorem _root_.Multiset.norm_prod {α : Type*} [NormedField α] (t : Multiset α) :
    ‖t.prod‖ = (t.map (fun a => ‖a‖)).prod := by
  simpa using (t.prod_hom (normHom : α →*₀ ℝ)).symm

/-- The `j`-th elementary symmetric function of a multiset of complex numbers is bounded by
`C(card, j)` times `∏ max(1, ‖a‖)`.

Two slacknesses, both deliberate.  A subset product `∏_{a ∈ t} ‖a‖` is bounded by
`∏_{a ∈ t} max(1,‖a‖)` termwise, and then that is extended from `t` to all of `s` — legal
precisely because every extra factor is `≥ 1`, so enlarging the index set only increases the
product.  With every summand bounded by the same `∏_{a ∈ s} max(1,‖a‖)`, the sum over
`powersetCard j s` costs a factor `card (powersetCard j s) = C(card s, j)`. -/
theorem _root_.Multiset.norm_esymm_le (s : Multiset ℂ) (j : ℕ) :
    ‖s.esymm j‖ ≤ ((Multiset.card s).choose j : ℝ)
      * (s.map (fun a => max 1 ‖a‖)).prod := by
  classical
  set f : ℂ → ℝ := fun a => max 1 ‖a‖ with hf
  set P := (s.map f).prod with hPdef
  have hf1 : ∀ a : ℂ, (1 : ℝ) ≤ f a := fun a => le_max_left _ _
  have hsub : ∀ t ∈ s.powersetCard j, ‖t.prod‖ ≤ P := by
    intro t ht
    obtain ⟨hts, -⟩ := Multiset.mem_powersetCard.mp ht
    have h1 : ‖t.prod‖ ≤ (t.map f).prod := by
      rw [Multiset.norm_prod]
      exact Multiset.prod_map_le_prod_map₀ _ _ (fun i _ => norm_nonneg i)
        (fun i _ => le_max_right _ _)
    have hnn : (0 : ℝ) ≤ (t.map f).prod :=
      Multiset.prod_nonneg (fun x hx => by
        obtain ⟨a, -, rfl⟩ := Multiset.mem_map.mp hx
        exact le_trans zero_le_one (hf1 a))
    have hone : (1 : ℝ) ≤ ((s - t).map f).prod :=
      Multiset.one_le_prod (fun x hx => by
        obtain ⟨a, -, rfl⟩ := Multiset.mem_map.mp hx
        exact hf1 a)
    have hst : s - t + t = s := tsub_add_cancel_of_le hts
    refine le_trans h1 ?_
    calc (t.map f).prod ≤ ((s - t).map f).prod * (t.map f).prod :=
          le_mul_of_one_le_left hnn hone
      _ = ((s - t + t).map f).prod := by rw [Multiset.map_add, Multiset.prod_add]
      _ = P := by rw [hst]
  rw [Multiset.esymm]
  refine le_trans (norm_multiset_sum_le _) ?_
  rw [Multiset.map_map]
  refine le_trans (Multiset.sum_le_card_nsmul _ P ?_) ?_
  · intro x hx
    obtain ⟨t, ht, rfl⟩ := Multiset.mem_map.mp hx
    exact hsub t ht
  · rw [Multiset.card_map, Multiset.card_powersetCard, nsmul_eq_mul]

/-- **The binomial form of the reverse bridge:** `‖coeff k p‖ ≤ C(n, n−k) · M(p)`, `n = deg p`.

Vieta writes `coeff k p` as `lead p` times an elementary symmetric function of the roots; the
Jensen form writes `M(p)` as `‖lead p‖` times `∏ max(1,‖root‖)`.  The two share the factor
`‖lead p‖`, so what is left is exactly `Multiset.norm_esymm_le`. -/
theorem norm_coeff_le_choose_mul_mahlerMeasure {p : ℂ[X]} {k : ℕ} (hk : k ≤ p.natDegree) :
    ‖p.coeff k‖ ≤ (p.natDegree.choose (p.natDegree - k) : ℝ) * p.mahlerMeasure := by
  have hroots : Multiset.card p.roots = p.natDegree :=
    splits_iff_card_roots.mp (IsAlgClosed.splits_codomain p)
  have hes := Multiset.norm_esymm_le p.roots (p.natDegree - k)
  rw [hroots] at hes
  rw [coeff_eq_esymm_roots_of_card hroots hk, mahlerMeasure_eq_leadingCoeff_mul_prod_roots,
    norm_mul, norm_mul, norm_pow, norm_neg, norm_one, one_pow, mul_one]
  calc ‖p.leadingCoeff‖ * ‖p.roots.esymm (p.natDegree - k)‖
      ≤ ‖p.leadingCoeff‖ * ((p.natDegree.choose (p.natDegree - k) : ℝ)
          * (p.roots.map (fun a => max 1 ‖a‖)).prod) :=
        mul_le_mul_of_nonneg_left hes (norm_nonneg _)
    _ = (p.natDegree.choose (p.natDegree - k) : ℝ)
          * (‖p.leadingCoeff‖ * (p.roots.map (fun a => max 1 ‖a‖)).prod) := by ring

/-- **The reverse bridge:** `H(p) ≤ 2^{deg p} · M(p)`, one coefficient at a time.

Since `H(p)` is the supremum of `‖coeff k p‖` over `k`, this *is* the height bound; stating it
per coefficient avoids having to fix a definition of `H` and is the form Gelfond consumes.

No hypothesis on `k`: above the degree the coefficient is zero and the bound is free. -/
theorem norm_coeff_le_two_pow_mul_mahlerMeasure (p : ℂ[X]) (k : ℕ) :
    ‖p.coeff k‖ ≤ 2 ^ p.natDegree * p.mahlerMeasure := by
  rcases le_or_gt k p.natDegree with hk | hk
  · refine le_trans (norm_coeff_le_choose_mul_mahlerMeasure hk) ?_
    refine mul_le_mul_of_nonneg_right ?_ (mahlerMeasure_nonneg p)
    exact_mod_cast Nat.choose_le_two_pow p.natDegree (p.natDegree - k)
  · rw [coeff_eq_zero_of_natDegree_lt hk, norm_zero]
    exact mul_nonneg (by positivity) (mahlerMeasure_nonneg p)

/-! ### A coefficient bound

The direction that turns a Mahler bound into a bound on coefficients.  See the ⚠ in the
module header: this is *not* Landau's inequality, only a cruder cousin of it. -/

/-- On the unit circle a polynomial is bounded by the sum of the norms of its
coefficients. -/
theorem norm_eval_le_sum_norm_coeff {p : ℂ[X]} {z : ℂ} (hz : ‖z‖ = 1) :
    ‖p.eval z‖ ≤ ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖ := by
  rw [eval_eq_sum_range]
  refine le_trans (norm_sum_le _ _) (le_of_eq (Finset.sum_congr rfl fun i _ => ?_))
  rw [norm_mul, norm_pow, hz, one_pow, mul_one]

/-- **A Landau-*type* bound:** `M(p) ≤ max(1, ‖p‖₁)`.

⚠ Weaker than Landau's inequality — see the module header.  This is the sup bound on the
circle, `M(p) = exp ∫ log‖p‖ ≤ sup‖p‖ ≤ ‖p‖₁`, not the Parseval one.

⚠ **The `max 1` is not slack, it is forced.**  The pointwise step is `log ‖p(z)‖ ≤ log S`
with `S = ‖p‖₁`, and that **fails** at a zero of `p` on the unit circle when `S < 1`:
Mathlib's `Real.log 0 = 0`, which exceeds `log S < 0`.  Bounding by `max 1 S` makes the
pointwise inequality hold at every point of the circle and so avoids an a.e. argument.

For a non-zero **integer** polynomial the distinction vanishes, since the leading
coefficient alone contributes at least one — that is `mahlerMeasure_le_sum_int`. -/
theorem mahlerMeasure_le_max_one_sum_norm_coeff (p : ℂ[X]) :
    p.mahlerMeasure ≤ max 1 (∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖) := by
  classical
  set S := ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖ with hS
  have hmax : (0 : ℝ) < max 1 S := lt_of_lt_of_le one_pos (le_max_left _ _)
  by_cases hp : p = 0
  · simp [hp, mahlerMeasure_zero, le_of_lt hmax]
  have hci : CircleIntegrable (fun z : ℂ => log ‖p.eval z‖) 0 1 := by
    rw [circleIntegrable_def]
    exact p.intervalIntegrable_mahlerMeasure
  have hbound : ∀ z ∈ Metric.sphere (0 : ℂ) |(1 : ℝ)|,
      log ‖p.eval z‖ ≤ log (max 1 S) := by
    intro z hz
    have hz1 : ‖z‖ = 1 := by simpa using hz
    rcases eq_or_lt_of_le (norm_nonneg (p.eval z)) with h0 | h0
    · -- `p` vanishes at `z`; here `Real.log 0 = 0`, and `0 ≤ log (max 1 S)`.
      rw [← h0, Real.log_zero]
      exact Real.log_nonneg (le_max_left _ _)
    · exact Real.log_le_log h0
        (le_trans (norm_eval_le_sum_norm_coeff hz1) (le_max_right _ _))
  have hlog : p.logMahlerMeasure ≤ log (max 1 S) := by
    rw [logMahlerMeasure_def]
    exact circleAverage_mono_on_of_le_circle hci hbound
  rw [mahlerMeasure, if_pos hp]
  calc rexp p.logMahlerMeasure ≤ rexp (log (max 1 S)) := Real.exp_le_exp.mpr hlog
    _ = max 1 S := Real.exp_log hmax

/-- When the coefficient sum is itself at least one, the `max` drops away. -/
theorem mahlerMeasure_le_sum_norm_coeff {p : ℂ[X]}
    (h : 1 ≤ ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖) :
    p.mahlerMeasure ≤ ∑ i ∈ range (p.natDegree + 1), ‖p.coeff i‖ :=
  le_trans (mahlerMeasure_le_max_one_sum_norm_coeff p) (max_le h le_rfl)

/-- A non-zero integer polynomial has coefficient sum at least one: its leading coefficient
is a non-zero integer, hence of absolute value at least one, and every other term of the sum
is non-negative. -/
theorem one_le_sum_norm_coeff_map_int {q : ℤ[X]} (hq : q ≠ 0) :
    1 ≤ ∑ i ∈ range ((q.map (Int.castRingHom ℂ)).natDegree + 1),
      ‖(q.map (Int.castRingHom ℂ)).coeff i‖ := by
  classical
  have hinj : Function.Injective (Int.castRingHom ℂ) := fun a b h => by simpa using h
  have hdeg : (q.map (Int.castRingHom ℂ)).natDegree = q.natDegree :=
    natDegree_map_eq_of_injective hinj q
  have hmem : q.natDegree ∈ range ((q.map (Int.castRingHom ℂ)).natDegree + 1) := by
    rw [hdeg]; exact self_mem_range_succ _
  have hlead : (1 : ℝ) ≤ ‖(q.map (Int.castRingHom ℂ)).coeff q.natDegree‖ := by
    rw [coeff_map]
    have : q.leadingCoeff ≠ 0 := leadingCoeff_ne_zero.mpr hq
    have h1 : (1 : ℤ) ≤ |q.leadingCoeff| := Int.one_le_abs (by omega)
    simpa [Int.cast_abs] using (by exact_mod_cast h1 : (1 : ℝ) ≤ |(q.leadingCoeff : ℝ)|)
  refine le_trans hlead (Finset.single_le_sum (f := fun i =>
    ‖(q.map (Int.castRingHom ℂ)).coeff i‖) (fun i _ => norm_nonneg _) hmem)

/-- **The coefficient bound over `ℤ`.**  For a non-zero integer polynomial, the Mahler
measure of its complex image is at most the sum of the absolute values of its coefficients.

This is the form the Roth's-lemma height bookkeeping consumes: over `ℤ` the `max 1` of
`mahlerMeasure_le_max_one_sum_norm_coeff` disappears.  ⚠ Still not Landau — see the
module header. -/
theorem mahlerMeasure_le_sum_int {q : ℤ[X]} (hq : q ≠ 0) :
    (q.map (Int.castRingHom ℂ)).mahlerMeasure
      ≤ ∑ i ∈ range ((q.map (Int.castRingHom ℂ)).natDegree + 1),
        ‖(q.map (Int.castRingHom ℂ)).coeff i‖ :=
  mahlerMeasure_le_sum_norm_coeff (one_le_sum_norm_coeff_map_int hq)

/-! ### Next

**Gelfond's inequality** `∏ₖ H(pₖ) ≤ 2^{deg p}(deg p + 1) · H(p)` for `p = ∏ₖ pₖ` over `ℤ`,
and then the height control on the factors `φₖ, ψₖ` that the induction step of Roth's lemma
needs.  Every ingredient is now in this file or in Mathlib:

* `mahlerMeasure_mul` / `prod_mahlerMeasure_eq_mahlerMeasure_prod` — `M` is multiplicative,
  so `∏ₖ M(pₖ) = M(p)` exactly.  This is what makes the argument work at all: heights are not
  multiplicative, Mahler measures are.
* `norm_coeff_le_two_pow_mul_mahlerMeasure` — up from each `M(pₖ)` to `H(pₖ)`.
* `mahlerMeasure_le_sum_int` — down from `H(p)` to `M(p)`.

⚠ The remaining work is genuinely bookkeeping, but it is not nothing: it has to move between
`ℤ[X]` and `ℂ[X]` along `Polynomial.map (Int.castRingHom ℂ)`, and `natDegree` and `coeff`
must be tracked across that map.  `natDegree_map_eq_of_injective` is the lemma that makes it
routine; `one_le_sum_norm_coeff_map_int` above is a worked example of the pattern.

Sharpening `mahlerMeasure_le_max_one_sum_norm_coeff` to Landau proper (`M(p) ≤ ‖p‖₂`, via
Parseval and Jensen's inequality for `exp`) is optional: the lost `√(deg+1)` is invisible
downstream, so this is worth doing only as an upstream contribution. -/

end Polynomial
