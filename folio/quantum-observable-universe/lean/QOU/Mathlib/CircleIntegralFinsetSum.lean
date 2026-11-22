import Mathlib.MeasureTheory.Integral.CircleIntegral
import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Analytic.IsolatedZeros
import Mathlib.Analysis.Meromorphic.FactorizedRational

/-!
# Two Mathlib gaps at our pinned revision

Both statements below exist in current Mathlib but not at the revision this
project pins (`f897ebcf`). They are stated here in Mathlib's own shape so that
the eventual pin bump deletes this file rather than requiring a rewrite.

* `integral_fun_sum` — linearity of the circle integral over a `Finset` sum.
  Upstream as `circleIntegral.integral_fun_sum`.
* `divisor_support_finite_of_subset` — a meromorphic function on a *compact* set
  has finitely many zeros and poles on any subset. Upstream as
  `MeromorphicOn.divisor_support_finite_of_subset`.

Together with `MeromorphicOn.extract_zeros_poles` — which *is* present at the pin
— these are what a `Finset`-indexed argument principle consumes: the
factorisation supplies the finitely many factors, this supplies their finiteness,
and the first lets the contour integral be taken term by term.

-- Ref: [leitner2026] bean `qou-argp` — the converse theta zero locus.
-/

open scoped Real
open MeasureTheory Filter Set Topology MeromorphicOn

namespace QOU.Mathlib

variable {E : Type*} [NormedAddCommGroup E] [NormedSpace ℂ E]

/-- Linearity of the circle integral over a `Finset` sum.

Mirrors Mathlib's own proof: unfold `circleIntegral` and apply
`intervalIntegral.integral_finset_sum`. -/
theorem integral_fun_sum {ι : Type*} {s : Finset ι} {f : ι → ℂ → E} {c : ℂ} {R : ℝ}
    (h : ∀ i ∈ s, CircleIntegrable (f i) c R) :
    (∮ z in C(c, R), ∑ i ∈ s, f i z) = ∑ i ∈ s, ∮ z in C(c, R), f i z := by
  simp only [circleIntegral, Finset.smul_sum,
    intervalIntegral.integral_finset_sum fun i hi ↦ (h i hi).out]

section Divisor

variable {𝕜 : Type*} [NontriviallyNormedField 𝕜] {F : Type*} [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] {U : Set 𝕜}

/-- If `f` is meromorphic on a compact `U` and `V ⊆ U`, the divisor of `f` on `V`
has finite support.

The support is discrete (isolated zeros) and closed in `U`; a discrete closed
subset of a compact set is finite. `divisor_restrict` transports that from `U`
to `V`. -/
theorem divisor_support_finite_of_subset {f : 𝕜 → F} {V : Set 𝕜}
    (hf : MeromorphicOn f U) (hU : IsCompact U) (hV : V ⊆ U) :
    (MeromorphicOn.divisor f V).support.Finite := by
  rw [← MeromorphicOn.divisor_restrict hf hV]
  refine ((MeromorphicOn.divisor f U).finiteSupport hU).subset ?_
  intro z hz
  rw [Function.mem_support] at hz ⊢
  by_cases hzV : z ∈ V
  · rwa [Function.locallyFinsuppWithin.restrict_apply, if_pos hzV] at hz
  · rw [Function.locallyFinsuppWithin.restrict_apply, if_neg hzV] at hz
    exact absurd rfl hz

end Divisor

section IdentityTheorem

/-- Analytic functions agreeing codiscretely on a preconnected set agree on it. -/
theorem eqOn_of_eventuallyEq_codiscreteWithin {f g : ℂ → ℂ} {U : Set ℂ}
    (hf : AnalyticOnNhd ℂ f U) (hg : AnalyticOnNhd ℂ g U) (hU : IsPreconnected U)
    [NeBot (codiscreteWithin U)]
    (h : f =ᶠ[codiscreteWithin U] g) : EqOn f g U := by
  rcases hf.eqOn_or_eventually_ne_of_preconnected hg hU with h' | h'
  · exact h'
  · exact absurd (eventually_false_iff_eq_bot.mp ((h.and h').mono fun _ hx => hx.2 hx.1))
      (NeBot.ne inferInstance)



section NeBot

open Topology

/-- For a nonempty open `U ⊆ ℂ`, the codiscrete-within filter is non-trivial.
Without this the lemma above is vacuous. -/
theorem codiscreteWithin_neBot {U : Set ℂ} (hU : IsOpen U) (hne : U.Nonempty) :
    NeBot (codiscreteWithin U) := by
  obtain ⟨x, hx⟩ := hne
  rw [neBot_iff]
  intro hbot
  have hmem : (∅ : Set ℂ) ∈ codiscreteWithin U := hbot ▸ Filter.mem_bot
  rw [mem_codiscreteWithin] at hmem
  have hdis := hmem x hx
  rw [Set.diff_empty, disjoint_iff] at hdis
  -- `𝓝[≠] x ⊓ 𝓟 U = 𝓝[{x}ᶜ ∩ U] x`, and restricting to the neighbourhood `U`
  -- does not change it, so it is `𝓝[≠] x` — non-trivial, as `ℂ` has no
  -- isolated points.
  rw [nhdsWithin, inf_assoc, inf_principal, ← nhdsWithin] at hdis
  have hUmem : U ∈ 𝓝[{x}ᶜ] x := nhdsWithin_le_nhds (hU.mem_nhds hx)
  have heq : 𝓝[{x}ᶜ ∩ U] x = 𝓝[≠] x := nhdsWithin_inter_of_mem' hUmem
  rw [heq] at hdis
  exact (PerfectSpace.not_isolated x).ne hdis

end NeBot

end IdentityTheorem

section Factorisation

/-- A `finprod` of `zpow` factors with a non-negative, finitely-supported
exponent is a `Finset.prod` of `npow` factors. -/
theorem finprod_zpow_eq_finset_prod_npow {D : ℂ → ℤ} (hD : ∀ x, 0 ≤ D x)
    (hfin : (Function.support D).Finite) (w : ℂ) :
    (∏ᶠ a, (w - a) ^ (D a)) = ∏ a ∈ hfin.toFinset, (w - a) ^ (D a).toNat := by
  classical
  have hsub : (Function.mulSupport fun a => (w - a) ^ (D a)) ⊆ hfin.toFinset := by
    intro a ha
    by_contra hcon
    simp only [Finset.mem_coe, Set.Finite.mem_toFinset, Function.mem_support,
      not_not] at hcon
    exact ha (by simp [hcon])
  rw [finprod_eq_prod_of_mulSupport_subset _ hsub]
  refine Finset.prod_congr rfl fun a _ => ?_
  conv_lhs => rw [show (D a) = ((D a).toNat : ℤ) from (Int.toNat_of_nonneg (hD a)).symm]
  rw [zpow_natCast]

open Filter Topology MeromorphicOn

/-- **An analytic function factorises over its zeros on a relatively compact,
connected open set.**

`extract_zeros_poles` gives this modulo a codiscrete set and in `finprod`/`zpow`
form; the identity theorem upgrades the equality and
`finprod_zpow_eq_finset_prod_npow` normalises the shape.

The multiplicities are strictly positive and `S ⊆ V`, so `S` is *exactly* the
zero set of `f` on `V` — without those, `a ∈ S` would carry no information and
the factorisation could not be read backwards. -/
theorem exists_finset_factorisation {V K : Set ℂ} (hV : IsOpen V)
    (hVconn : IsPreconnected V) (hVne : V.Nonempty) (hK : IsCompact K) (hVK : V ⊆ K)
    {f : ℂ → ℂ} (hf : AnalyticOnNhd ℂ f K)
    (hord : ∀ u : V, meromorphicOrderAt f u ≠ ⊤) :
    ∃ (S : Finset ℂ) (m : ℂ → ℕ) (g : ℂ → ℂ),
      AnalyticOnNhd ℂ g V ∧ (∀ u : V, g u ≠ 0) ∧ (∀ a ∈ S, 0 < m a) ∧
      (∀ a ∈ S, a ∈ V) ∧
      Set.EqOn f (fun z => (∏ a ∈ S, (z - a) ^ (m a)) * g z) V := by
  classical
  have hfV : AnalyticOnNhd ℂ f V := hf.mono hVK
  have hmV : MeromorphicOn f V := hfV.meromorphicOn
  -- finitely many zeros, because `K` is compact
  have hfinite : (divisor f V).support.Finite :=
    QOU.Mathlib.divisor_support_finite_of_subset hf.meromorphicOn hK hVK
  obtain ⟨g, hg, hgne, hEq⟩ := hmV.extract_zeros_poles hord hfinite
  -- the divisor is `≥ 0` because `f` is analytic
  have hDnn : ∀ x, 0 ≤ (divisor f V) x := fun x => hfV.divisor_nonneg x
  refine ⟨hfinite.toFinset, fun a => ((divisor f V) a).toNat, g, hg, hgne, ?_, ?_, ?_⟩
  · -- a point of the support has a nonzero, hence positive, divisor value
    intro a ha
    have hne0 : (divisor f V) a ≠ 0 := by
      have := (Set.Finite.mem_toFinset hfinite).1 ha
      rwa [Function.mem_support] at this
    have hnn := hDnn a
    -- `show` first: the goal is a beta-redex, which `omega` treats as opaque
    show 0 < ((divisor f V) a).toNat
    omega
  · -- a divisor is supported inside its domain
    exact fun a ha =>
      (divisor f V).supportWithinDomain ((Set.Finite.mem_toFinset hfinite).1 ha)
  -- upgrade the codiscrete equality to genuine equality
  haveI : NeBot (codiscreteWithin V) := QOU.Mathlib.codiscreteWithin_neBot hV hVne
  refine QOU.Mathlib.eqOn_of_eventuallyEq_codiscreteWithin hfV ?_ hVconn ?_
  · -- the right-hand side is analytic on `V`
    have : AnalyticOnNhd ℂ (fun z : ℂ => ∏ a ∈ hfinite.toFinset, (z - a) ^ (((divisor f V) a).toNat)) V := by
      refine Finset.analyticOnNhd_fun_prod _ (fun a _ => ?_)
      exact (analyticOnNhd_id.sub analyticOnNhd_const).pow _
    exact this.mul hg
  · filter_upwards [hEq] with z hz
    rw [hz, Pi.smul_apply', smul_eq_mul]
    congr 1
    have hms : (Function.mulSupport
        fun u : ℂ => (fun x : ℂ => x - u) ^ ((divisor f V) u)).Finite := by
      refine hfinite.subset fun u hu => ?_
      simp only [Function.mem_mulSupport] at hu
      simp only [Function.mem_support]
      intro h
      exact hu (by simp [h])
    rw [finprod_apply hms z]
    exact finprod_zpow_eq_finset_prod_npow hDnn hfinite z

/-- **In a `Finset` factorisation the exponent at a factor is the order of
vanishing there.**

Splitting `(· − a)^{m a}` off the product leaves an analytic function that does
not vanish at `a` — the two remaining kinds of factor, `(· − b)^{m b}` for
`b ≠ a` and the cofactor `g`, are both nonzero there — and that is exactly what
`analyticOrderAt f a = m a` says. -/
theorem analyticOrderAt_eq_of_finset_factorisation {V : Set ℂ} (hV : IsOpen V)
    {S : Finset ℂ} {m : ℂ → ℕ} {f g : ℂ → ℂ}
    (hg : AnalyticOnNhd ℂ g V) (hgne : ∀ z ∈ V, g z ≠ 0) (hSV : ∀ a ∈ S, a ∈ V)
    (hEq : Set.EqOn f (fun z => (∏ a ∈ S, (z - a) ^ (m a)) * g z) V)
    {a : ℂ} (ha : a ∈ S) : analyticOrderAt f a = m a := by
  classical
  have haV : a ∈ V := hSV a ha
  have hpow : ∀ T : Finset ℂ,
      AnalyticOnNhd ℂ (fun z : ℂ => ∏ b ∈ T, (z - b) ^ (m b)) V := fun T =>
    Finset.analyticOnNhd_fun_prod _ fun b _ => (analyticOnNhd_id.sub analyticOnNhd_const).pow _
  -- `f` is analytic at `a`, since it agrees with an analytic function near it
  have hfA : AnalyticAt ℂ f a :=
    (((hpow S) a haV).mul (hg a haV)).congr
      (Filter.eventuallyEq_of_mem (hV.mem_nhds haV) hEq).symm
  rw [hfA.analyticOrderAt_eq_natCast]
  refine ⟨fun z => (∏ b ∈ S.erase a, (z - b) ^ (m b)) * g z,
    ((hpow (S.erase a)) a haV).mul (hg a haV), ?_, ?_⟩
  · refine mul_ne_zero (Finset.prod_ne_zero_iff.2 fun b hb => ?_) (hgne a haV)
    exact pow_ne_zero _ (sub_ne_zero.2 (Ne.symm (Finset.ne_of_mem_erase hb)))
  · filter_upwards [hV.mem_nhds haV] with z hz
    have hval : f z = (∏ b ∈ S, (z - b) ^ (m b)) * g z := hEq hz
    rw [hval, smul_eq_mul, ← mul_assoc]
    congr 1
    exact (Finset.mul_prod_erase S (fun b => (z - b) ^ (m b)) ha).symm

end Factorisation

end QOU.Mathlib
