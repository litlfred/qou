import QOU.Mathlib.ExponentOfConvergence
import QOU.Mathlib.CanonicalProductGrowth
import QOU.Mathlib.HadamardZeroFree
import Mathlib.Analysis.NormedSpace.MultipliableUniformlyOn
import Mathlib.Analysis.Complex.LocallyUniformLimit
import Mathlib.Analysis.Meromorphic.NormalForm

/-!
# The Hadamard quotient: enumeration, zeros of the canonical product, `f / P`

Beans `qou-n4pv` / `qou-kp89`. The bookkeeping half of Hadamard's factorization theorem
(`QOU.Mathlib.HadamardFactorization.HasHadamardFactorization`).

## Proved here (sorry-free)

* **Canonical products over an arbitrary index type.** `canonicalProduct p a z =
  ∏' i, Eₚ(z / aᵢ)` for `a : ι → ℂ`, all `aᵢ ≠ 0`, `∑ ‖aᵢ‖^{-σ} < ∞`, `0 < σ ≤ p + 1`:
  it is multipliable at every `z` (`multipliable_canonicalProduct`) and entire
  (`differentiable_canonicalProduct`, via `differentiable_tprod_one_add`, the
  arbitrary-index version of the `ℕ`-indexed lemma in `HadamardApplicability`).
* **Local factorization** (`exists_local_factor`): if `T` is exactly the finite set of
  indices with `aᵢ = u`, then `P z = (z - u)^{#T} · h z` for all `z`, with `h` analytic at
  `u` and `h u ≠ 0`. So `P` vanishes at `u` to order exactly `#T`.
* **Enumeration with multiplicity.** `zeroIndex f = {(u, k) : ℂ × ℕ // k < ord_u f}`,
  `zeroSeq f (u, k) = u`, where `ord_u f` is `MeromorphicOn.divisor f univ u`
  (`ExponentOfConvergence.zeroDivisor`). For `f` entire with `f 0 ≠ 0`: the index type is
  countable (`countable_zeroIndex`), every `zeroSeq f i ≠ 0`, `f (zeroSeq f i) = 0`, the
  fibre over `u` has exactly `ord_u f` elements (`card_fiber`, `mem_fiber`),
  `analyticOrderAt f u = ord_u f` (`analyticOrderAt_eq_toNat`), and summability of
  `∑_u ord_u(f)‖u‖^{-σ}` transfers to `∑_i ‖zeroSeq f i‖^{-σ}` (`summable_zeroSeq_rpow`).
* **Zeros of the product = zeros of `f`, with multiplicity**
  (`analyticOrderAt_zeroProduct`).
* **The quotient.** `hadamardQuotient p f` (the meromorphic normal form of `f / P` on
  `ℂ`) is entire, nowhere zero, and `f z = q z · ∏' i, Eₚ(z / zeroSeq f i)` for every `z`
  (`hadamardQuotient_spec`; from the order hypothesis with `p = ⌊ρ⌋₊`:
  `hadamardQuotient_spec_of_order`, using `summable_divisor_mul_rpow_neg`).
* **Hadamard, conditional on the order of the quotient** (`hadamard_of_quotient_order`):
  if additionally `IsEntireOfOrderLE (hadamardQuotient ⌊ρ⌋₊ f) ρ`, the full conclusion of
  `HasHadamardFactorization` holds for `f` (via `HadamardZeroFree.exists_polynomial_of_zeroFree`).

## NOT proved here

* That the quotient `q = f / P` satisfies `IsEntireOfOrderLE q ρ` — the minimum-modulus
  lower bound on `|P|` off small discs around the zeros. This is the one remaining input
  to Hadamard's theorem; it is carried as the explicit hypothesis `hq` of
  `hadamard_of_quotient_order`, NOT assumed anywhere else. It is also necessary: if
  `f = exp(g)·P` with `deg g ≤ ρ` then `q = exp ∘ g` satisfies it.
* Consequently `HasHadamardFactorization` is still not instantiated.

§7c: archimedean (norms, `Real.rpow`, complex analysis on `ℂ`).

-- Ref: [leitner2026] standard: Conway, Functions of One Complex Variable I, VII §5–6 (Weierstrass factorization), XI §3
-/

open Filter Topology Set Function

namespace QOU.Mathlib.HadamardQuotient

open QOU.Mathlib.HadamardFactorization

/-! ## Canonical products over an arbitrary index type -/

section Product

variable {ι : Type*}

/-- Entirety of `∏' i, (1 + F i z)` over an arbitrary index type, from a summable
dominant on every ball (cofinitely). -/
theorem differentiable_tprod_one_add {F : ι → ℂ → ℂ} (hF : ∀ i, Differentiable ℂ (F i))
    (hdom : ∀ R : ℝ, 0 < R → ∃ u : ι → ℝ, Summable u ∧
      ∀ᶠ i in cofinite, ∀ z ∈ Metric.ball (0 : ℂ) R, ‖F i z‖ ≤ u i) :
    Differentiable ℂ (fun z => ∏' i, (1 + F i z)) := by
  intro z
  have hR : (0 : ℝ) < ‖z‖ + 1 := by positivity
  obtain ⟨u, hu, hdomR⟩ := hdom (‖z‖ + 1) hR
  have hopen : IsOpen (Metric.ball (0 : ℂ) (‖z‖ + 1)) := Metric.isOpen_ball
  have hprod := Summable.hasProdLocallyUniformlyOn_one_add hopen hu hdomR
    (fun i => (hF i).continuous.continuousOn)
  have hdiff : DifferentiableOn ℂ (fun x => ∏' i, (1 + F i x))
      (Metric.ball (0 : ℂ) (‖z‖ + 1)) := by
    refine TendstoLocallyUniformlyOn.differentiableOn hprod ?_ hopen
    filter_upwards with s
    have h1 : DifferentiableOn ℂ (∏ i ∈ s, ((fun _ => (1 : ℂ)) + F i))
        (Metric.ball (0 : ℂ) (‖z‖ + 1)) :=
      DifferentiableOn.finset_prod
        (fun i _ => ((differentiable_const (1 : ℂ)).add (hF i)).differentiableOn)
    have h2 : (∏ i ∈ s, ((fun _ => (1 : ℂ)) + F i))
        = fun b => ∏ i ∈ s, (1 + F i b) := by
      funext b; simp [Finset.prod_apply]
    rwa [h2] at h1
  refine hdiff.differentiableAt (hopen.mem_nhds ?_)
  simp only [Metric.mem_ball, dist_zero_right]
  linarith

variable {a : ι → ℂ} {σ : ℝ}

/-- Summability of `‖aᵢ‖^{-σ}` (`σ > 0`, all `aᵢ ≠ 0`) forces `‖aᵢ‖ ≥ M` cofinitely. -/
theorem eventually_le_norm (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ)
    (hs : Summable (fun i => ‖a i‖ ^ (-σ))) (M : ℝ) :
    ∀ᶠ i in cofinite, M ≤ ‖a i‖ := by
  set M' := max M 1
  have hM'pos : 0 < M' := lt_of_lt_of_le one_pos (le_max_right _ _)
  have hc : 0 < M' ^ (-σ) := Real.rpow_pos_of_pos hM'pos _
  filter_upwards [hs.tendsto_cofinite_zero.eventually_lt_const hc] with i hi
  have hpos : 0 < ‖a i‖ := norm_pos_iff.mpr (ha i)
  have : M' ≤ ‖a i‖ := by
    by_contra h
    push_neg at h
    have := Real.rpow_lt_rpow_of_exponent_neg hpos h (by linarith : -σ < 0)
    linarith
  exact le_trans (le_max_left _ _) this

/-- The basic estimate: if `‖z‖ ≤ ‖aᵢ‖`, then `‖Eₚ(z/aᵢ) - 1‖ ≤ ‖z‖^σ ‖aᵢ‖^{-σ}`. -/
theorem norm_factor_sub_one_le (p : ℕ) (ha : ∀ i, a i ≠ 0) (hσ0 : 0 ≤ σ)
    (hσp : σ ≤ (p : ℝ) + 1) {z : ℂ} {i : ι} (hz : ‖z‖ ≤ ‖a i‖) :
    ‖weierstrassFactor p (z / a i) - 1‖ ≤ ‖z‖ ^ σ * ‖a i‖ ^ (-σ) := by
  have hpos : 0 < ‖a i‖ := norm_pos_iff.mpr (ha i)
  have h1 : ‖z / a i‖ ≤ 1 := by rw [norm_div]; exact (div_le_one hpos).mpr hz
  rw [← QOU.Mathlib.CanonicalProductGrowth.norm_div_rpow]
  exact QOU.Mathlib.CanonicalProductGrowth.norm_weierstrassFactor_sub_one_le_rpow p hσ0 hσp h1

/-- The deviation from `1` of the factor indexed by `i`, with the factors in a finite set
`T` replaced by `1`. -/
noncomputable def dev (p : ℕ) (a : ι → ℂ) (T : Set ι) [DecidablePred (· ∈ T)]
    (i : ι) (z : ℂ) : ℂ :=
  if i ∈ T then 0 else weierstrassFactor p (z / a i) - 1

theorem norm_dev_le (p : ℕ) (T : Set ι) [DecidablePred (· ∈ T)] (ha : ∀ i, a i ≠ 0)
    (hσ0 : 0 ≤ σ) (hσp : σ ≤ (p : ℝ) + 1) {z : ℂ} {i : ι} (hz : ‖z‖ ≤ ‖a i‖) :
    ‖dev p a T i z‖ ≤ ‖z‖ ^ σ * ‖a i‖ ^ (-σ) := by
  unfold dev
  split_ifs
  · simp only [norm_zero]; positivity
  · exact norm_factor_sub_one_le p ha hσ0 hσp hz

theorem summable_norm_dev (p : ℕ) (T : Set ι) [DecidablePred (· ∈ T)] (ha : ∀ i, a i ≠ 0)
    (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1) (hs : Summable (fun i => ‖a i‖ ^ (-σ))) (z : ℂ) :
    Summable (fun i => ‖dev p a T i z‖) := by
  refine Summable.of_norm_bounded_eventually (hs.mul_left (‖z‖ ^ σ)) ?_
  filter_upwards [eventually_le_norm ha hσ0 hs ‖z‖] with i hi
  rw [norm_norm]
  exact norm_dev_le p T ha hσ0.le hσp hi

theorem differentiable_dev (p : ℕ) (T : Set ι) [DecidablePred (· ∈ T)] (i : ι) :
    Differentiable ℂ (dev p a T i) := by
  unfold dev
  split_ifs
  · exact differentiable_const 0
  · exact ((differentiable_weierstrassFactor p).comp
      (differentiable_id.div_const (a i))).sub_const 1

theorem differentiable_tprod_dev (p : ℕ) (T : Set ι) [DecidablePred (· ∈ T)]
    (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable (fun i => ‖a i‖ ^ (-σ))) :
    Differentiable ℂ (fun z => ∏' i, (1 + dev p a T i z)) := by
  refine differentiable_tprod_one_add (differentiable_dev p T) fun R hR => ?_
  refine ⟨fun i => R ^ σ * ‖a i‖ ^ (-σ), hs.mul_left _, ?_⟩
  filter_upwards [eventually_le_norm ha hσ0 hs R] with i hi z hz
  have hzR : ‖z‖ < R := by simpa using hz
  calc ‖dev p a T i z‖ ≤ ‖z‖ ^ σ * ‖a i‖ ^ (-σ) := norm_dev_le p T ha hσ0.le hσp (by linarith)
    _ ≤ R ^ σ * ‖a i‖ ^ (-σ) := by
        gcongr

theorem one_add_dev (p : ℕ) (T : Set ι) [DecidablePred (· ∈ T)] (i : ι) (z : ℂ) :
    1 + dev p a T i z = if i ∈ T then 1 else weierstrassFactor p (z / a i) := by
  unfold dev; split_ifs <;> simp

/-- The **canonical product** over an arbitrary index type. -/
noncomputable def canonicalProduct (p : ℕ) (a : ι → ℂ) (z : ℂ) : ℂ :=
  ∏' i, weierstrassFactor p (z / a i)

theorem canonicalProduct_eq_tprod_dev (p : ℕ) (a : ι → ℂ) (z : ℂ) :
    canonicalProduct p a z = ∏' i, (1 + dev p a (∅ : Set ι) i z) := by
  unfold canonicalProduct
  congr 1; funext i; rw [one_add_dev]; simp

theorem multipliable_canonicalProduct (p : ℕ) (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ)
    (hσp : σ ≤ (p : ℝ) + 1) (hs : Summable (fun i => ‖a i‖ ^ (-σ))) (z : ℂ) :
    Multipliable (fun i => weierstrassFactor p (z / a i)) := by
  have := Complex.multipliable_one_add_of_summable
    (summable_norm_dev p (∅ : Set ι) ha hσ0 hσp hs z).of_norm
  simpa [one_add_dev] using this

theorem differentiable_canonicalProduct (p : ℕ) (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ)
    (hσp : σ ≤ (p : ℝ) + 1) (hs : Summable (fun i => ‖a i‖ ^ (-σ))) :
    Differentiable ℂ (canonicalProduct p a) := by
  have h := differentiable_tprod_dev p (∅ : Set ι) ha hσ0 hσp hs
  have he : canonicalProduct p a = fun z => ∏' i, (1 + dev p a (∅ : Set ι) i z) :=
    funext (canonicalProduct_eq_tprod_dev p a)
  rwa [he]

/-- **Local factorization of the canonical product.** If `T` is exactly the (finite) set of
indices with `aᵢ = u`, then `∏' i, Eₚ(z/aᵢ) = (z - u)^{#T} · h z` for an `h` analytic at `u`
with `h u ≠ 0`. So the canonical product has analytic order exactly `#T` at `u`. -/
theorem exists_local_factor (p : ℕ) (ha : ∀ i, a i ≠ 0) (hσ0 : 0 < σ)
    (hσp : σ ≤ (p : ℝ) + 1) (hs : Summable (fun i => ‖a i‖ ^ (-σ))) (u : ℂ)
    (T : Finset ι) (hT : ∀ i, a i = u ↔ i ∈ T) :
    ∃ h : ℂ → ℂ, AnalyticAt ℂ h u ∧ h u ≠ 0 ∧
      ∀ z, canonicalProduct p a z = (z - u) ^ T.card * h z := by
  classical
  set Q : ℂ → ℂ := fun z => ∏' i, (1 + dev p a (↑T : Set ι) i z) with hQ
  set c : ℂ → ℂ := fun z =>
    -(u⁻¹) * Complex.exp (∑ k ∈ Finset.range p, (z / u) ^ (k + 1) / ((k : ℂ) + 1)) with hc
  have hQd : Differentiable ℂ Q := differentiable_tprod_dev p (↑T : Set ι) ha hσ0 hσp hs
  have hcd : Differentiable ℂ c := by rw [hc]; fun_prop
  refine ⟨fun z => c z ^ T.card * Q z, ((hcd.pow T.card).mul hQd).analyticAt u, ?_, ?_⟩
  · refine mul_ne_zero ?_ ?_
    · rcases T.eq_empty_or_nonempty with hTe | ⟨i, hi⟩
      · simp [hTe]
      · have hu : u ≠ 0 := by rw [← (hT i).mpr hi]; exact ha i
        refine pow_ne_zero _ (mul_ne_zero (neg_ne_zero.mpr (inv_ne_zero hu))
          (Complex.exp_ne_zero _))
    · refine tprod_one_add_ne_zero_of_summable (f := fun i => dev p a (↑T : Set ι) i u)
        (fun i => ?_) (summable_norm_dev p (↑T : Set ι) ha hσ0 hσp hs u)
      simp only [one_add_dev]
      split_ifs with hi
      · exact one_ne_zero
      · rw [Ne, weierstrassFactor_eq_zero_iff, div_eq_one_iff_eq (ha i)]
        intro h; exact hi ((hT i).mp h.symm)
  · intro z
    set A : ι → ℂ := fun i => if i ∈ T then weierstrassFactor p (z / a i) else 1 with hA
    have hsplit : (fun i => weierstrassFactor p (z / a i))
        = fun i => A i * (1 + dev p a (↑T : Set ι) i z) := by
      funext i; rw [one_add_dev, hA]; simp only [Finset.mem_coe]; split_ifs <;> simp
    have hAm : Multipliable A := by
      refine multipliable_of_finite_mulSupport (T.finite_toSet.subset ?_)
      intro i hi
      by_contra h
      exact hi (by simp only [hA, if_neg (show i ∉ T from h)])
    have hBm : Multipliable (fun i => 1 + dev p a (↑T : Set ι) i z) :=
      Complex.multipliable_one_add_of_summable
        (summable_norm_dev p (↑T : Set ι) ha hσ0 hσp hs z).of_norm
    have hAprod : ∏' i, A i = weierstrassFactor p (z / u) ^ T.card := by
      rw [tprod_eq_prod (s := T) (fun i hi => by simp [hA, hi])]
      rw [← Finset.prod_const]
      refine Finset.prod_congr rfl fun i hi => ?_
      simp [hA, hi, (hT i).mpr hi]
    rw [canonicalProduct, hsplit, hAm.tprod_mul hBm, hAprod]
    show weierstrassFactor p (z / u) ^ T.card * Q z = (z - u) ^ T.card * (c z ^ T.card * Q z)
    rcases T.eq_empty_or_nonempty with hTe | ⟨i, hi⟩
    · simp [hTe]
    · have hu : u ≠ 0 := by rw [← (hT i).mpr hi]; exact ha i
      have key : weierstrassFactor p (z / u) = (z - u) * c z := by
        rw [hc]; unfold weierstrassFactor
        have : (1 - z / u) = (z - u) * (-(u⁻¹)) := by field_simp; ring
        rw [this]; ring
      rw [key, mul_pow]; ring

end Product

/-! ## Enumerating the zeros of an entire function with multiplicity -/

section Enumeration

open QOU.Mathlib.ExponentOfConvergence (zeroDivisor zeroDivisor_nonneg divisor_ball_eq)

/-- The index type of the zeros of `f`, with multiplicity: a pair `(u, k)` with
`k < ord_u(f)`. -/
def zeroIndex (f : ℂ → ℂ) : Type := {x : ℂ × ℕ // x.2 < (zeroDivisor f x.1).toNat}

/-- The zero sequence: `(u, k) ↦ u`. Each zero `u` is listed `ord_u(f)` times. -/
def zeroSeq (f : ℂ → ℂ) : zeroIndex f → ℂ := fun i => i.1.1

/-- The (finite) set of indices listing the zero `u`. -/
noncomputable def fiber (f : ℂ → ℂ) (u : ℂ) : Finset (zeroIndex f) :=
  ((Finset.range (zeroDivisor f u).toNat).map
    ⟨fun k => (u, k), fun k l h => by simpa using h⟩).subtype _

theorem mem_fiber {f : ℂ → ℂ} {u : ℂ} {i : zeroIndex f} :
    i ∈ fiber f u ↔ zeroSeq f i = u := by
  obtain ⟨⟨v, k⟩, hk⟩ := i
  rw [fiber, Finset.mem_subtype, Finset.mem_map]
  simp only [Finset.mem_range, Function.Embedding.coeFn_mk, Prod.mk.injEq, zeroSeq]
  constructor
  · rintro ⟨l, -, rfl, -⟩; rfl
  · rintro rfl; exact ⟨k, hk, rfl, rfl⟩

theorem card_fiber (f : ℂ → ℂ) (u : ℂ) : (fiber f u).card = (zeroDivisor f u).toNat := by
  classical
  rw [fiber, Finset.card_subtype, Finset.filter_true_of_mem, Finset.card_map,
    Finset.card_range]
  intro x hx
  simp only [Finset.mem_map, Finset.mem_range, Function.Embedding.coeFn_mk] at hx
  obtain ⟨k, hk, rfl⟩ := hx
  exact hk

variable {f : ℂ → ℂ}

/-- The support of the zero divisor of an entire function is countable. -/
theorem countable_support_zeroDivisor (hf : Differentiable ℂ f) :
    (Function.support (zeroDivisor f)).Countable := by
  have hsub : Function.support (zeroDivisor f) ⊆
      ⋃ n : ℕ, Function.support (MeromorphicOn.divisor f (Metric.closedBall (0 : ℂ) n)) := by
    intro u hu
    refine mem_iUnion.mpr ⟨⌈‖u‖⌉₊, ?_⟩
    have hmem : u ∈ Metric.closedBall (0 : ℂ) (⌈‖u‖⌉₊ : ℕ) := by
      simpa using Nat.le_ceil ‖u‖
    rw [Function.mem_support, divisor_ball_eq hf hmem]
    exact hu
  refine Countable.mono hsub (countable_iUnion fun n => ?_)
  exact ((MeromorphicOn.divisor f (Metric.closedBall (0 : ℂ) n)).finiteSupport
    (isCompact_closedBall 0 _)).countable

/-- The zero index type of an entire function is countable. -/
theorem countable_zeroIndex (hf : Differentiable ℂ f) : Countable (zeroIndex f) := by
  have hS : {x : ℂ × ℕ | x.2 < (zeroDivisor f x.1).toNat}.Countable := by
    refine ((countable_support_zeroDivisor hf).prod (countable_univ (α := ℕ))).mono ?_
    intro x hx
    simp only [mem_setOf_eq] at hx
    refine ⟨?_, mem_univ _⟩
    intro h
    simp [h] at hx
  exact hS.to_subtype

/-- For entire `f` with `f 0 ≠ 0`, the analytic order at `u` is `ord_u(f)` (finite). -/
theorem analyticOrderAt_eq_toNat (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (u : ℂ) :
    analyticOrderAt f u = ((zeroDivisor f u).toNat : ℕ∞) := by
  have hanf : AnalyticOnNhd ℂ f univ := fun z _ => hf.analyticAt z
  have h0 : analyticOrderAt f 0 ≠ ⊤ := by
    rw [analyticOrderAt_eq_zero.mpr (Or.inr hf0)]; exact ENat.zero_ne_top
  have hne : analyticOrderAt f u ≠ ⊤ :=
    hanf.analyticOrderAt_ne_top_of_isPreconnected isPreconnected_univ (mem_univ 0)
      (mem_univ u) h0
  obtain ⟨n, hn⟩ := ENat.ne_top_iff_exists.mp hne
  have hdiv : zeroDivisor f u = (meromorphicOrderAt f u).untop₀ :=
    MeromorphicOn.divisor_apply hanf.meromorphicOn (mem_univ u)
  rw [hdiv, (hf.analyticAt u).meromorphicOrderAt_eq, ← hn, ENat.map_coe]
  rfl

theorem zeroSeq_ne_zero (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (i : zeroIndex f) :
    zeroSeq f i ≠ 0 := by
  obtain ⟨⟨v, k⟩, hk⟩ := i
  simp only [zeroSeq]
  rintro rfl
  have h := analyticOrderAt_eq_toNat hf hf0 0
  rw [analyticOrderAt_eq_zero.mpr (Or.inr hf0)] at h
  have : (zeroDivisor f 0).toNat = 0 := by exact_mod_cast h.symm
  simp only at hk
  omega

theorem apply_zeroSeq (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (i : zeroIndex f) :
    f (zeroSeq f i) = 0 := by
  obtain ⟨⟨v, k⟩, hk⟩ := i
  simp only [zeroSeq]
  refine apply_eq_zero_of_analyticOrderAt_ne_zero ?_
  rw [analyticOrderAt_eq_toNat hf hf0 v]
  simp only at hk
  exact_mod_cast (show (zeroDivisor f v).toNat ≠ 0 by omega)

/-- Summability transfers from the divisor to the enumeration. -/
theorem summable_zeroSeq_rpow (hf : Differentiable ℂ f) {σ : ℝ}
    (hs : Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)) :
    Summable fun i : zeroIndex f => ‖zeroSeq f i‖ ^ (-σ) := by
  classical
  have hnn : ∀ u : ℂ, (0 : ℝ) ≤ zeroDivisor f u * ‖u‖ ^ (-σ) := fun u =>
    mul_nonneg (zeroDivisor_nonneg hf u) (Real.rpow_nonneg (norm_nonneg _) _)
  refine summable_of_sum_le (c := ∑' u, (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ))
    (fun i => Real.rpow_nonneg (norm_nonneg _) _) fun s => ?_
  rw [Finset.sum_comp (fun u : ℂ => ‖u‖ ^ (-σ)) (zeroSeq f)]
  calc ∑ v ∈ s.image (zeroSeq f), (s.filter (fun i => zeroSeq f i = v)).card • ‖v‖ ^ (-σ)
      ≤ ∑ v ∈ s.image (zeroSeq f), (zeroDivisor f v : ℝ) * ‖v‖ ^ (-σ) := by
        refine Finset.sum_le_sum fun v _ => ?_
        rw [nsmul_eq_mul]
        refine mul_le_mul_of_nonneg_right ?_ (Real.rpow_nonneg (norm_nonneg _) _)
        have hc : (s.filter (fun i => zeroSeq f i = v)).card ≤ (fiber f v).card := by
          refine Finset.card_le_card fun i hi => ?_
          rw [mem_fiber]; exact (Finset.mem_filter.mp hi).2
        rw [card_fiber] at hc
        have hD : ((zeroDivisor f v).toNat : ℝ) = zeroDivisor f v := by
          have := zeroDivisor_nonneg hf v
          exact_mod_cast Int.toNat_of_nonneg (by exact_mod_cast this)
        rw [← hD]; exact_mod_cast hc
    _ ≤ ∑' u, (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ) := hs.sum_le_tsum _ fun u _ => hnn u

end Enumeration

/-! ## The quotient `f / P` is entire and zero-free -/

section Quotient

open QOU.Mathlib.ExponentOfConvergence (zeroDivisor)

variable {f : ℂ → ℂ}

/-- The canonical product of genus `p` over the zeros of `f`, with multiplicity. -/
noncomputable def zeroProduct (p : ℕ) (f : ℂ → ℂ) : ℂ → ℂ :=
  canonicalProduct p (zeroSeq f)

/-- The **Hadamard quotient** `f / P`, with its removable singularities filled in
(the meromorphic normal form of `z ↦ f z / P z` on `ℂ`). -/
noncomputable def hadamardQuotient (p : ℕ) (f : ℂ → ℂ) : ℂ → ℂ :=
  toMeromorphicNFOn (fun z => f z / zeroProduct p f z) univ

/-- **Local structure at a point.** Under the hypotheses, at every `u` the product
`P = zeroProduct p f` has a zero of exactly the order of `f`, and the Hadamard quotient is
analytic and nonzero at `u` with `f u = q u · P u`. -/
theorem hadamardQuotient_local (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (p : ℕ) {σ : ℝ}
    (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)) (u : ℂ) :
    AnalyticAt ℂ (hadamardQuotient p f) u ∧ hadamardQuotient p f u ≠ 0 ∧
      f u = hadamardQuotient p f u * zeroProduct p f u := by
  set q := hadamardQuotient p f with hqdef
  set P := zeroProduct p f with hPdef
  have ha := zeroSeq_ne_zero hf hf0
  have hsa := summable_zeroSeq_rpow hf hs
  have hPd : Differentiable ℂ P := differentiable_canonicalProduct p ha hσ0 hσp hsa
  -- local form of `P`
  obtain ⟨h, hh, hhu, hPh⟩ := exists_local_factor p ha hσ0 hσp hsa u (fiber f u)
    (fun i => mem_fiber.symm)
  rw [card_fiber] at hPh
  have hPh' : ∀ z, P z = (z - u) ^ (zeroDivisor f u).toNat * h z := hPh
  -- local form of `f`
  obtain ⟨g, hg, hgu, hfg⟩ :=
    (hf.analyticAt u).analyticOrderAt_eq_natCast.mp (analyticOrderAt_eq_toNat hf hf0 u)
  set r : ℂ → ℂ := fun z => g z / h z with hr
  have hra : AnalyticAt ℂ r u := hg.div hh hhu
  have hru : r u ≠ 0 := div_ne_zero hgu hhu
  have hmero : MeromorphicOn (fun z => f z / P z) univ := fun z _ =>
    (hf.analyticAt z).meromorphicAt.fun_div (hPd.analyticAt z).meromorphicAt
  -- `f / P = r` on a punctured neighbourhood of `u`
  have hhne : ∀ᶠ z in 𝓝 u, h z ≠ 0 := hh.continuousAt.eventually_ne hhu
  have hfPr : (fun z => f z / P z) =ᶠ[𝓝[≠] u] r := by
    filter_upwards [nhdsWithin_le_nhds hfg, nhdsWithin_le_nhds hhne, self_mem_nhdsWithin]
      with z hz hhz hzu
    have hzu' : (z - u) ^ (zeroDivisor f u).toNat ≠ 0 := pow_ne_zero _ (sub_ne_zero.mpr hzu)
    simp only [hr, hPh' z, hz, smul_eq_mul]
    field_simp
  have hqf : q =ᶠ[𝓝[≠] u] (fun z => f z / P z) :=
    hmero.toMeromorphicNFOn_eq_self_on_nhdsNE (mem_univ u)
  have hqNF : MeromorphicNFAt q u := meromorphicNFOn_toMeromorphicNFOn _ _ (mem_univ u)
  have hqr : q =ᶠ[𝓝 u] r :=
    (hqNF.eventuallyEq_nhdsNE_iff_eventuallyEq_nhds hra.meromorphicNFAt).mp (hqf.trans hfPr)
  have hqu : q u = r u := hqr.eq_of_nhds
  refine ⟨hra.congr hqr.symm, hqu ▸ hru, ?_⟩
  rw [hqu, hPh' u, hfg.self_of_nhds, hr, smul_eq_mul]
  field_simp

/-- **The Hadamard quotient (bookkeeping half of Hadamard's theorem).** Let `f` be entire
with `f 0 ≠ 0`, and suppose `∑_u ord_u(f)·‖u‖^{-σ} < ∞` for some `0 < σ ≤ p + 1`. Enumerate
the zeros of `f` with multiplicity (`zeroSeq f`, over the countable type `zeroIndex f`).
Then the canonical product `P(z) = ∏' i, Eₚ(z / aᵢ)` converges and is entire, and
`q = hadamardQuotient p f` is entire, zero-free, and `f = q · P` everywhere. -/
theorem hadamardQuotient_spec (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (p : ℕ) {σ : ℝ}
    (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)) :
    Differentiable ℂ (hadamardQuotient p f) ∧ (∀ z, hadamardQuotient p f z ≠ 0) ∧
      ∀ z, Multipliable (fun i => weierstrassFactor p (z / zeroSeq f i)) ∧
        f z = hadamardQuotient p f z * ∏' i, weierstrassFactor p (z / zeroSeq f i) := by
  refine ⟨fun z => (hadamardQuotient_local hf hf0 p hσ0 hσp hs z).1.differentiableAt,
    fun z => (hadamardQuotient_local hf hf0 p hσ0 hσp hs z).2.1, fun z => ⟨?_, ?_⟩⟩
  · exact multipliable_canonicalProduct p (zeroSeq_ne_zero hf hf0) hσ0 hσp
      (summable_zeroSeq_rpow hf hs) z
  · exact (hadamardQuotient_local hf hf0 p hσ0 hσp hs z).2.2

/-- The zeros of the canonical product over the zeros of `f` are exactly the zeros of `f`,
with the same multiplicities. -/
theorem analyticOrderAt_zeroProduct (hf : Differentiable ℂ f) (hf0 : f 0 ≠ 0) (p : ℕ)
    {σ : ℝ} (hσ0 : 0 < σ) (hσp : σ ≤ (p : ℝ) + 1)
    (hs : Summable fun u : ℂ => (zeroDivisor f u : ℝ) * ‖u‖ ^ (-σ)) (u : ℂ) :
    analyticOrderAt (zeroProduct p f) u = analyticOrderAt f u := by
  have ha := zeroSeq_ne_zero hf hf0
  have hsa := summable_zeroSeq_rpow hf hs
  obtain ⟨h, hh, hhu, hPh⟩ := exists_local_factor p ha hσ0 hσp hsa u (fiber f u)
    (fun i => mem_fiber.symm)
  rw [card_fiber] at hPh
  rw [analyticOrderAt_eq_toNat hf hf0 u]
  have hPd : Differentiable ℂ (zeroProduct p f) :=
    differentiable_canonicalProduct p ha hσ0 hσp hsa
  refine (hPd.analyticAt u).analyticOrderAt_eq_natCast.mpr ⟨h, hh, hhu, ?_⟩
  filter_upwards with z
  rw [smul_eq_mul]; exact hPh z

end Quotient

/-! ## From the order hypothesis -/

section Order

open QOU.Mathlib.ExponentOfConvergence (summable_divisor_mul_rpow_neg)

variable {f : ℂ → ℂ} {ρ : ℝ}

/-- The genus and exponent used for an entire function of order `≤ ρ`:
`p = ⌊ρ⌋₊` and `σ = (ρ + p + 1)/2 ∈ (ρ, p + 1]`. -/
theorem exists_sigma (hρ : 0 ≤ ρ) :
    ∃ σ : ℝ, ρ < σ ∧ 0 < σ ∧ σ ≤ ((⌊ρ⌋₊ : ℕ) : ℝ) + 1 := by
  have h := Nat.lt_floor_add_one ρ
  exact ⟨(ρ + ⌊ρ⌋₊ + 1) / 2, by linarith, by linarith, by linarith⟩

/-- **Bookkeeping half of Hadamard, from the order hypothesis.** For `f` entire of order
`≤ ρ` (`IsEntireOfOrderLE`), `0 ≤ ρ`, `f 0 ≠ 0`, with genus `p = ⌊ρ⌋₊ ≤ ρ`: the canonical
product over the zeros of `f` (with multiplicity) converges, and `f = q · P` with `q`
entire and zero-free. -/
theorem hadamardQuotient_spec_of_order (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0)
    (hρ : 0 ≤ ρ) :
    Countable (zeroIndex f) ∧ (∀ i, zeroSeq f i ≠ 0) ∧ (∀ i, f (zeroSeq f i) = 0) ∧
      Differentiable ℂ (hadamardQuotient ⌊ρ⌋₊ f) ∧ (∀ z, hadamardQuotient ⌊ρ⌋₊ f z ≠ 0) ∧
      ∀ z, Multipliable (fun i => weierstrassFactor ⌊ρ⌋₊ (z / zeroSeq f i)) ∧
        f z = hadamardQuotient ⌊ρ⌋₊ f z * ∏' i, weierstrassFactor ⌊ρ⌋₊ (z / zeroSeq f i) := by
  obtain ⟨σ, hρσ, hσ0, hσp⟩ := exists_sigma hρ
  have hs := summable_divisor_mul_rpow_neg hf hf0 hρ hρσ
  obtain ⟨h1, h2, h3⟩ := hadamardQuotient_spec hf.1 hf0 ⌊ρ⌋₊ hσ0 hσp hs
  exact ⟨countable_zeroIndex hf.1, zeroSeq_ne_zero hf.1 hf0, apply_zeroSeq hf.1 hf0, h1, h2, h3⟩

/-- **Hadamard's theorem, conditional on the order of the quotient.** If, in addition, the
Hadamard quotient `q = f / P` satisfies `IsEntireOfOrderLE q ρ` (the minimum-modulus step,
NOT proved here), then the conclusion of `HasHadamardFactorization` holds for `f`.

The extra hypothesis is necessary as well as sufficient for the `g` part: if
`f = exp(g)·P` with `deg g ≤ ρ` then `q = exp ∘ g` does satisfy it. -/
theorem hadamard_of_quotient_order (hf : IsEntireOfOrderLE f ρ) (hf0 : f 0 ≠ 0)
    (hρ : 0 ≤ ρ) (hq : IsEntireOfOrderLE (hadamardQuotient ⌊ρ⌋₊ f) ρ) :
    ∃ (p : ℕ) (g : Polynomial ℂ) (ι : Type) (_ : Countable ι) (a : ι → ℂ),
      (p : ℝ) ≤ ρ ∧
      (g.natDegree : ℝ) ≤ ρ ∧
      (∀ i, a i ≠ 0) ∧
      (∀ i, f (a i) = 0) ∧
      (∀ z, Multipliable (fun i => weierstrassFactor p (z / a i)) ∧
            f z = Complex.exp (g.eval z) * ∏' i, weierstrassFactor p (z / a i)) := by
  obtain ⟨hc, ha, hz, -, hq0, hfac⟩ := hadamardQuotient_spec_of_order hf hf0 hρ
  obtain ⟨g, hg, hqg⟩ :=
    QOU.Mathlib.HadamardZeroFree.exists_polynomial_of_zeroFree hq hρ hq0
  refine ⟨⌊ρ⌋₊, g, zeroIndex f, hc, zeroSeq f, Nat.floor_le hρ, hg, ha, hz, fun z => ?_⟩
  refine ⟨(hfac z).1, ?_⟩
  rw [(hfac z).2, hqg z]

end Order

end QOU.Mathlib.HadamardQuotient
