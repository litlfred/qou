import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Meromorphic.Order
import Mathlib.Analysis.Meromorphic.FactorizedRational
import Mathlib.Analysis.Calculus.LogDeriv
import Mathlib.Analysis.Complex.Basic
import Mathlib.Analysis.Complex.CauchyIntegral
import Mathlib.MeasureTheory.Integral.CircleIntegral

/-!
# The argument principle — scaffold (PI-3, bean `qou-bmyx`)

For `f` meromorphic on a closed disc `\overline{B}(c,R)` with **no zeros or poles
on the bounding circle**, the contour integral of the logarithmic derivative
counts zeros minus poles with multiplicity:

$$\frac{1}{2\pi i}\oint_{|z-c|=R} \frac{f'(z)}{f(z)}\,dz
   \;=\; \sum_{w\in B(c,R)} \operatorname{ord}_w f
   \;=\; \#\{\text{zeros}\} - \#\{\text{poles}\}\quad(\text{with multiplicity}).$$

This is the **argument principle**. It is the least-Analysis-blocked of the three
`PentagonRigidity` infra walls (PI-1 Hadamard factorization, PI-2 elliptic
divisor-degree, PI-3 here): PI-2's degree-zero theorem and PI-1's canonical-product
zero-counting BOTH reduce to it (`elliptic_divisor_degree_zero` is now proved in
`QOU.Mathlib.LiouvilleThird` via the annulus version of this theorem,
`QOU.Mathlib.ArgumentPrincipleAnnulus`; a canonical product's zero count is this
integral applied to an entire `f`). The `f'/f`-integrand carries the *analytic*
content; the RHS is the purely-combinatorial divisor sum.

MOTIVATION (epic `qou-lbth`). The residual analytic leg of
`PentagonRigidity.uniqueUpToScalar` needs to pin the canonical minimal Faddeev
solution `phiBProd` among its elliptic multiples by counting zeros; the
argument principle is the tool that turns "a contour integral of `f'/f`" into
"an integer count of zeros", and is the shared engine under both PI-1 and PI-2.

## What is authored here — bricks vs. open core

**Elementary bricks (full proofs, Mathlib-only cone — see the verification caveat):**

* `toNat_sub_toNat_neg` — the integer identity `n.toNat - (-n).toNat = n`.
* `zeroCount` / `poleCount` and `zeroCount_sub_poleCount_eq_sum_divisor` — the
  RHS bookkeeping: `#zeros - #poles = Σ ord`, decomposing the divisor sum into its
  positive (zero) and negative (pole) parts. This is the combinatorial half of the
  argument principle, complete and independent of any analysis.
* `two_pi_I_ne_zero'` — the normalization `2πi ≠ 0`, making the `(2πi)⁻¹` factor
  well-defined (Mathlib also has `Complex.two_pi_I_ne_zero`; reproved locally to
  keep the cone explicit).
* `logDeriv_zpow_sub_mul_split` — **brick 1**: the log-derivative split
  `logDeriv ((·-w)^n·g) = n·(z-w)⁻¹ + logDeriv g` (pure `logDeriv` algebra).
* `inv_two_pi_I_mul_integral_nat_sub_center_inv` — **brick 2**: the Cauchy simple-pole
  term `(2πi)⁻¹ ∮_{C(w,r)} n·(z-w)⁻¹ = n`.
* `circleIntegral_logDeriv_eq_zero_of_analyticOnNhd` — **brick 3**: the Cauchy–Goursat
  vanishing `∮_{C(w,r)} logDeriv g = 0` for `g` analytic + nonvanishing on the disc.

**Now PROVED sorry-free (the full local argument principle):**

* `residue_logDeriv_eq_order` — the **local** argument principle: for `f`
  meromorphic at `w` and analytic + nonvanishing on the punctured open neighborhood
  `U \ {w}` of the closed disc, the small-circle integral `(2πi)⁻¹ ∮_{C(w,r)} f'/f`
  equals the order `ord_w f`. **Fully sorry-free (2026-07-20):** the residue-
  computation (bricks 1–3) plus the global factorization `f = (·-w)^n·g` are both
  discharged. The factor is built explicitly, `g := (·-w)^(-n)·f` off `w` patched to
  the germ value `g₀ w` at `w` (`meromorphicOrderAt_eq_int_iff` supplies `g₀`); it
  agrees with `g₀` on a full neighborhood of `w` (removable singularity ⇒ analytic
  at `w`) and is a product of analytic nonvanishing factors away from `w`. The
  earlier pointwise-`hsmall` hypothesis was too weak to build an OPEN-neighborhood
  factor and is replaced by the honest `AnalyticOnNhd`/no-other-zeros pair — exactly
  what a real argument-principle setup provides.

**Now PROVED sorry-free (2026-07-20 — the global statements, via factorization):**

* `argument_principle` — the global statement (contour integral = divisor sum), **proved
  fully sorry-free** via the **global Weierstrass factorization**
  `MeromorphicOn.extract_zeros_poles`: on the closed disc,
  `f = (∏ᶠ_w (·-w)^{ord_w f}) · g` with `g` analytic and nonvanishing, so
  `logDeriv f = Σ_w (ord_w f)·(·-w)⁻¹ + logDeriv g` on the bounding circle `C(c,R)`.
  Then `∮_{C(c,R)} logDeriv f = Σ_w (ord_w f)·2πi + 0` — the analytic part vanishes by
  Cauchy–Goursat (`circleIntegral_logDeriv_eq_zero_of_analyticOnNhd`) and each bare simple
  pole gives `∮_{C(c,R)} (z-w)⁻¹ = 2πi` for **every interior** `w`
  (`circleIntegral.integral_sub_inv_of_mem_ball`). This route needs **no** contour
  deformation, so the off-centre / multi-puncture difficulty never arises. The
  hypotheses `∀ u, ord_u f ≠ ⊤` and `divisor.support.Finite` (needed by
  `extract_zeros_poles`) are discharged from `hf` + a boundary witness + connectedness
  (`exists_meromorphicOrderAt_ne_top_iff_forall`) and disc compactness
  (`locallyFinsuppWithin.finiteSupport`).
* `entire_zero_count` — the PI-3 **canonical-product application**, **proved sorry-free**
  by specializing `argument_principle` to entire `f`: no poles ⇒ `divisor ≥ 0`
  (`AnalyticAt.meromorphicOrderAt_nonneg`), so `Σ ord = zeroCount`.

**Supporting lemmas (all sorry-free):**

* `residue_logDeriv_eq_order` — the **local** argument principle (per-puncture residue
  `(2πi)⁻¹ ∮_{C(w,r)} f'/f = ord_w f`). Retained as an independently useful lemma; it is
  no longer needed by `argument_principle`, which now factors globally rather than
  deforming onto small circles.
* `circleIntegrable_sum_simple_poles` / `circleIntegral_sum_simple_poles` — the sum side:
  a finite sum of interior simple poles is circle-integrable and integrates to
  `Σ_u a_u·2πi` (off-centre Cauchy pole integral, applied term by term).

## Why the contour-deformation gap was dissolved, not closed

An earlier revision isolated a single `sorry` — `residue_theorem_deformation`, the
multiply-connected (off-centre / multi-hole homology) contour deformation
`∮_{C(c,R)} h = Σ_w ∮_{C(w,ρ w)} h` for *general* analytic `h`. That deformation is a
**genuine Mathlib v4.24.0 gap** (below), and it is **not** needed for the argument
principle: `logDeriv f` is not an arbitrary `h`, and the global factorization route
above computes `∮_{C(c,R)} logDeriv f` directly. The deformation lemma was therefore
**removed** in favour of the factorization proof, and the file is now sorry-free. (The
general-`h` residue-sum deformation remains genuinely absent from Mathlib and would still
require a winding-number / homology engine to state and prove; it is simply unnecessary
here. The same factorization route is boundary-shape-agnostic: a *rectangular* outer
contour argument principle follows identically via the rectangle Cauchy integral formula
+ `integral_boundary_rect_eq_zero_of_differentiable_on_off_countable`, with no crosscut
deformation.)

## Mathlib v4.24.0 gap — exactly what is present vs. absent

Present (and used here): the Cauchy integral formula and the off-centre bare-pole integral
`circleIntegral.integral_sub_inv_of_mem_ball` (`∮_{C(c,R)} (z-w)⁻¹ = 2πi`, any interior
`w`), Cauchy–Goursat `circleIntegral_eq_zero_of_differentiable_on_off_countable`, the
global Weierstrass factorization `MeromorphicOn.extract_zeros_poles`
(`Analysis/Meromorphic/FactorizedRational`), `MeromorphicOn.divisor`
(`divisor_apply`, `finiteSupport`), `meromorphicOrderAt`
(`exists_meromorphicOrderAt_ne_top_iff_forall`), and `logDeriv`
(`logDeriv_prod`, `logDeriv_fun_zpow`). The *concentric* annulus deformation
`circleIntegral_eq_of_differentiable_on_annulus_off_countable` is present but **not
needed** by this route.

Absent (and now avoided): `Complex.residue`, `windingNumber`, and every off-centre /
keyhole / multi-hole **homology** contour-deformation lemma (re-verified 2026-07-20 by
`#check` and an olean declaration sweep of `Analysis/Complex/CauchyIntegral` +
`MeasureTheory/Integral/CircleIntegral`: only the concentric annulus deformation, the
single on-disc Cauchy integral formula, and the rectangle vanishing are present).
The earlier design routed the argument principle through this missing engine; the
factorization route removes that dependence entirely.

-- Ref: [leitner2026] Argument principle / residue of the logarithmic derivative;
--   standard complex analysis (Ahlfors, *Complex Analysis*, Ch. 5 §2; Conway
--   VI.1). Proved here via the Weierstrass zero/pole factorization route. See
--   docs/audits/2026-07-20-argument-principle-scaffold.md.

## VERIFICATION STATUS (STRICT, honest)

**COMPILE-VERIFIED `lean`-direct, exit 0, SORRY-FREE** (2026-07-20, this environment;
the Analysis oleans present — `Complex.CauchyIntegral`, `CircleIntegral`,
`Meromorphic/*` incl. `FactorizedRational`, `Calculus/LogDeriv` — suffice to elaborate
the import cone via `LEAN_PATH` over the package olean dirs). **Every declaration in this
file is sorry-free**; `#print axioms argument_principle` and
`#print axioms entire_zero_count` report only `[propext, Classical.choice, Quot.sound]`
(no `sorryAx`). The former single topological `sorry` (`residue_theorem_deformation`) was
**eliminated** by re-proving `argument_principle` through the global factorization
`MeromorphicOn.extract_zeros_poles` rather than a contour deformation; the deformation
lemma is gone. A full `lake build QOU` on a host with the complete Analysis cone remains
the CI gate.
-/

open Filter Topology Complex

namespace QOU.Mathlib.ArgumentPrinciple

/-! ### Combinatorial brick: `#zeros − #poles = Σ ord` (analysis-free) -/

/-- **The integer split identity** `n = n⁺ − n⁻`, i.e. `n.toNat − (−n).toNat = n`.
For `n ≥ 0` this is `n − 0`; for `n < 0` it is `0 − (−n)`. This is the per-point
statement that a divisor value (zero-order minus pole-order) decomposes into a
zero contribution and a pole contribution. -/
theorem toNat_sub_toNat_neg (n : ℤ) : (n.toNat : ℤ) - ((-n).toNat : ℤ) = n := by
  omega

/-- **Zero count**: the sum of positive divisor values (orders of zeros) over a
finite set `S` of points. With `S` = the divisor's support inside a region, this is
`#zeros` counted with multiplicity. -/
def zeroCount (D : ℂ → ℤ) (S : Finset ℂ) : ℕ := ∑ w ∈ S, (D w).toNat

/-- **Pole count**: the sum of the magnitudes of negative divisor values (orders of
poles). With `S` = the divisor support inside a region, this is `#poles` counted
with multiplicity. -/
def poleCount (D : ℂ → ℤ) (S : Finset ℂ) : ℕ := ∑ w ∈ S, ((-(D w)).toNat)

/-- **The RHS of the argument principle, combinatorially.** For any ℤ-valued
divisor `D` and finite support set `S`, `#zeros − #poles = Σ ord`:
`(zeroCount D S) − (poleCount D S) = ∑_{w∈S} D w`. This is the whole right-hand
side, complete and analysis-free — the argument principle's remaining content is
entirely the *left*-hand (contour-integral) side. -/
theorem zeroCount_sub_poleCount_eq_sum_divisor (D : ℂ → ℤ) (S : Finset ℂ) :
    (zeroCount D S : ℤ) - (poleCount D S : ℤ) = ∑ w ∈ S, D w := by
  simp only [zeroCount, poleCount, Nat.cast_sum]
  rw [← Finset.sum_sub_distrib]
  exact Finset.sum_congr rfl (fun w _ => toNat_sub_toNat_neg (D w))

/-! ### Normalization brick: `2πi ≠ 0` -/

/-- **The Cauchy normalization `2πi ≠ 0`.** Makes the `(2πi)⁻¹` prefactor of the
argument principle a genuine inverse (Mathlib: `Complex.two_pi_I_ne_zero`; reproved
locally to keep this file's cited API explicit). -/
theorem two_pi_I_ne_zero' : (2 * (Real.pi : ℂ) * Complex.I) ≠ 0 := by
  have hpi : (Real.pi : ℂ) ≠ 0 := by
    exact_mod_cast Real.pi_ne_zero
  exact mul_ne_zero (mul_ne_zero two_ne_zero hpi) Complex.I_ne_zero

/-! ### The local argument principle (deep core — stated open)

The single missing Mathlib brick: the residue of the logarithmic derivative at a
point equals the meromorphic order there. Everything global is this, summed.

The three lemmas below are the **sorry-free** analytic bricks the local argument
principle assembles from — the log-derivative split, the Cauchy simple-pole term,
and the Cauchy–Goursat vanishing of the analytic part. Only the *global
factorization on the closed disc* (extending the germ `meromorphicOrderAt_eq_int_iff`
gives to a nonvanishing analytic `g` on a neighborhood of the disc) remains open. -/

/-- **Log-derivative split at a zero/pole (brick 1).** If `f = (·−w)^n · g` locally
with `g` differentiable and nonvanishing at `z` and `z ≠ w`, then the logarithmic
derivative splits into the simple-pole part `n·(z−w)⁻¹` and the analytic part
`logDeriv g`. Pure `logDeriv` algebra — sorry-free. -/
lemma logDeriv_zpow_sub_mul_split {g : ℂ → ℂ} {w z : ℂ} {n : ℤ}
    (hz : z ≠ w) (hg : DifferentiableAt ℂ g z) (hgz : g z ≠ 0) :
    logDeriv (fun ζ => (ζ - w) ^ n * g ζ) z = (n : ℂ) * (z - w)⁻¹ + logDeriv g z := by
  have hzw : z - w ≠ 0 := sub_ne_zero.2 hz
  have hdf : DifferentiableAt ℂ (fun ζ => ζ - w) z := (differentiableAt_id).sub_const w
  have hdpow : DifferentiableAt ℂ (fun ζ => (ζ - w) ^ n) z := hdf.zpow (Or.inl hzw)
  have hpne : ((z - w) ^ n) ≠ 0 := zpow_ne_zero n hzw
  rw [logDeriv_mul z hpne hgz hdpow hg]
  congr 1
  rw [logDeriv_fun_zpow hdf n]
  have h2 : logDeriv (fun ζ => ζ - w) z = (z - w)⁻¹ := by
    rw [logDeriv_apply]
    have hd1 : deriv (fun ζ : ℂ => ζ - w) z = 1 :=
      ((hasDerivAt_id z).sub_const w).deriv
    rw [hd1, one_div]
  rw [h2]

/-- **Cauchy simple-pole term (brick 2).** The normalized small-circle integral of
the simple pole `n·(z−w)⁻¹` recovers the integer `n`:
`(2πi)⁻¹ ∮_{C(w,r)} n·(z−w)⁻¹ = n`. Direct from `circleIntegral.integral_sub_center_inv`
— sorry-free. -/
lemma inv_two_pi_I_mul_integral_nat_sub_center_inv {w : ℂ} {r : ℝ} (hr : 0 < r) (n : ℤ) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(w, r), (n : ℂ) * (z - w)⁻¹) = (n : ℂ) := by
  rw [circleIntegral.integral_const_mul, circleIntegral.integral_sub_center_inv w hr.ne',
    mul_comm (n : ℂ) (2 * (Real.pi : ℂ) * Complex.I), ← mul_assoc,
    inv_mul_cancel₀ two_pi_I_ne_zero', one_mul]

/-- **Cauchy–Goursat vanishing of the analytic part (brick 3).** For `g` analytic and
nonvanishing on a neighborhood of the closed disc `\overline B(w,r)`, its logarithmic
derivative `logDeriv g = g'/g` is analytic there, hence integrates to `0` over the
bounding circle (Cauchy–Goursat). Sorry-free, via
`circleIntegral_eq_zero_of_differentiable_on_off_countable`. -/
lemma circleIntegral_logDeriv_eq_zero_of_analyticOnNhd {g : ℂ → ℂ} {w : ℂ} {r : ℝ}
    (hr : 0 ≤ r) (hg : AnalyticOnNhd ℂ g (Metric.closedBall w r))
    (hgne : ∀ z ∈ Metric.closedBall w r, g z ≠ 0) :
    (∮ z in C(w, r), logDeriv g z) = 0 := by
  have hA : AnalyticOnNhd ℂ (logDeriv g) (Metric.closedBall w r) := by
    have hd := (hg.deriv).div hg hgne
    exact hd
  refine Complex.circleIntegral_eq_zero_of_differentiable_on_off_countable hr Set.countable_empty
    hA.continuousOn ?_
  intro z hz
  exact (hA z (Metric.ball_subset_closedBall hz.1)).differentiableAt

/-- **Residue of the logarithmic derivative = order** (the local argument
principle). For `f` meromorphic at `w` with finite order `n = ord_w f`, and all
sufficiently small circles `C(w,r)` avoiding other zeros/poles, the small-circle
average of `f'/f` recovers the integer order:
`(2πi)⁻¹ ∮_{C(w,r)} logDeriv f = n`.

Reason: near `w`, `f(z) = (z-w)^n·g(z)` with `g` analytic and nonvanishing
(`meromorphicOrderAt_eq_int_iff`), so `logDeriv f = n/(z-w) + logDeriv g`; the
analytic `logDeriv g` integrates to `0` (Cauchy), and `∮ (z-w)⁻¹ = 2πi`
(`circleIntegral_sub_center_inv_smul_of_differentiable_on_off_countable`), leaving
`n`. Mathlib has BOTH ingredients but not this composition.

**PROVED (sorry-free).** The factorization core is now discharged from the standard
argument-principle hypotheses: `f` meromorphic at `w`, analytic and nonvanishing on
the punctured open neighborhood `U \ {w}` of the closed disc. These are exactly the
hypotheses a real argument-principle setup provides; the earlier pointwise-`hsmall`
formulation was too weak to build an OPEN-neighborhood factor (an open `U ⊇
closedBall w r` necessarily reaches points outside the disc, where a pointwise-order
hypothesis says nothing), so it is replaced here by the honest `AnalyticOnNhd`/
no-other-zeros pair. -/
theorem residue_logDeriv_eq_order {f : ℂ → ℂ} {w : ℂ} {r : ℝ} {n : ℤ} {U : Set ℂ}
    (hf : MeromorphicAt f w) (hr : 0 < r)
    (hU_open : IsOpen U) (hball_sub : Metric.closedBall w r ⊆ U)
    (horder : meromorphicOrderAt f w = (n : WithTop ℤ))
    (hfU : AnalyticOnNhd ℂ f (U \ {w}))
    (hfne : ∀ z ∈ U, z ≠ w → f z ≠ 0) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(w, r), logDeriv f z) = (n : ℂ) := by
  -- === The analytic core: global factorization `f = (·-w)^n·g` on `U`, now PROVED. ===
  -- From `meromorphicOrderAt f w = n` (`meromorphicOrderAt_eq_int_iff` supplies the
  -- germ `f = (·-w)^n • g₀` in `𝓝[≠] w`) together with `hfU` (analytic away from `w`)
  -- and `hfne` (no other zeros), build the single nonvanishing analytic factor
  -- `g := (·-w)^(-n)·f` off `w`, patched to `g₀ w` at `w`. It agrees with the germ
  -- `g₀` on a full neighborhood of `w` (removable singularity), giving analyticity at
  -- `w`; away from `w` it is a product of analytic nonvanishing factors.
  obtain ⟨g, hg_an, hg_ne, hf_eq⟩ :
      ∃ (g : ℂ → ℂ), AnalyticOnNhd ℂ g U ∧ (∀ z ∈ U, g z ≠ 0) ∧
        Set.EqOn f (fun z => (z - w) ^ n * g z) (U \ {w}) := by
    obtain ⟨g₀, hg₀_an, hg₀_ne, hg₀_eq⟩ := (meromorphicOrderAt_eq_int_iff hf).mp horder
    set G : ℂ → ℂ := Function.update (fun z => (z - w) ^ (-n) * f z) w (g₀ w) with hG
    have hGaway : ∀ z, z ≠ w → G z = (z - w) ^ (-n) * f z := by
      intro z hz; rw [hG, Function.update_of_ne hz]
    have hGw : G w = g₀ w := by rw [hG, Function.update_self]
    refine ⟨G, ?_, ?_, ?_⟩
    · -- `AnalyticOnNhd ℂ G U`
      intro z hz
      by_cases hzw : z = w
      · -- at `w`: `G =ᶠ[𝓝 w] g₀`, and `g₀` is analytic at `w`
        have hpunc : G =ᶠ[𝓝[≠] w] g₀ := by
          filter_upwards [hg₀_eq, self_mem_nhdsWithin] with x hx hxne
          have hxw : x ≠ w := hxne
          rw [hGaway x hxw, hx]
          show (x - w) ^ (-n) * ((x - w) ^ n * g₀ x) = g₀ x
          rw [← mul_assoc, ← zpow_add₀ (sub_ne_zero.2 hxw), neg_add_cancel, zpow_zero, one_mul]
        have hEq : G =ᶠ[𝓝 w] g₀ := eventuallyEq_nhds_of_eventuallyEq_nhdsNE hpunc hGw
        rw [hzw]
        exact (analyticAt_congr hEq).mpr hg₀_an
      · -- away from `w`: product of analytic factors
        have hUz : z ∈ U \ {w} := ⟨hz, by simpa using hzw⟩
        have hfz : AnalyticAt ℂ f z := hfU z hUz
        have hne_nhds : G =ᶠ[𝓝 z] (fun x => (x - w) ^ (-n) * f x) := by
          have hmem : {w}ᶜ ∈ 𝓝 z := isClosed_singleton.isOpen_compl.mem_nhds (by simpa using hzw)
          filter_upwards [hmem] with x hx
          exact hGaway x (by simpa using hx)
        rw [analyticAt_congr hne_nhds]
        have hbase : AnalyticAt ℂ (fun x : ℂ => x - w) z := analyticAt_id.sub analyticAt_const
        exact (AnalyticAt.fun_zpow hbase (sub_ne_zero.2 hzw)).mul hfz
    · -- nonvanishing on `U`
      intro z hz
      by_cases hzw : z = w
      · rw [hzw, hGw]; exact hg₀_ne
      · rw [hGaway z hzw]
        exact mul_ne_zero (zpow_ne_zero _ (sub_ne_zero.2 hzw)) (hfne z hz hzw)
    · -- factorization on `U \ {w}`
      intro z hz
      have hzw : z ≠ w := by simpa using hz.2
      show f z = (z - w) ^ n * G z
      rw [hGaway z hzw, ← mul_assoc, ← zpow_add₀ (sub_ne_zero.2 hzw), add_neg_cancel, zpow_zero,
        one_mul]
  -- === Everything below is sorry-free: the three bricks assembled. ===
  have hg_an_cb : AnalyticOnNhd ℂ g (Metric.closedBall w r) := hg_an.mono hball_sub
  have hg_ne_cb : ∀ z ∈ Metric.closedBall w r, g z ≠ 0 := fun z hz => hg_ne z (hball_sub hz)
  have hopen : IsOpen (U \ {w}) := hU_open.sdiff isClosed_singleton
  have hsphere_ne : ∀ z ∈ Metric.sphere w r, z ≠ w := by
    intro z hz h
    rw [h, Metric.mem_sphere, dist_self] at hz
    exact hr.ne' hz.symm
  -- The integrand splits on the sphere: `logDeriv f = n·(z-w)⁻¹ + logDeriv g`.
  have hEqOn : Set.EqOn (logDeriv f)
      (fun z => (n : ℂ) * (z - w)⁻¹ + logDeriv g z) (Metric.sphere w r) := by
    intro z hz
    have hzU : z ∈ U := hball_sub (Metric.sphere_subset_closedBall hz)
    have hzw : z ≠ w := hsphere_ne z hz
    have hmem : z ∈ U \ {w} := ⟨hzU, by simpa using hzw⟩
    have hev : f =ᶠ[nhds z] fun ζ => (ζ - w) ^ n * g ζ :=
      hf_eq.eventuallyEq_of_mem (hopen.mem_nhds hmem)
    have hgz : DifferentiableAt ℂ g z := (hg_an z hzU).differentiableAt
    have hgnz : g z ≠ 0 := hg_ne z hzU
    have step : logDeriv f z = logDeriv (fun ζ => (ζ - w) ^ n * g ζ) z := by
      unfold logDeriv
      rw [Pi.div_apply, Pi.div_apply, hev.deriv_eq, hev.eq_of_nhds]
    rw [step]
    exact logDeriv_zpow_sub_mul_split hzw hgz hgnz
  -- Both pieces are circle-integrable (continuous on the sphere).
  have hInt1 : CircleIntegrable (fun z => (n : ℂ) * (z - w)⁻¹) w r := by
    apply ContinuousOn.circleIntegrable hr.le
    apply continuousOn_const.mul
    apply ContinuousOn.inv₀ (continuousOn_id.sub continuousOn_const)
    intro z hz
    exact sub_ne_zero.2 (hsphere_ne z hz)
  have hlogA : AnalyticOnNhd ℂ (logDeriv g) (Metric.closedBall w r) := by
    have hd := (hg_an_cb.deriv).div hg_an_cb hg_ne_cb
    exact hd
  have hInt2 : CircleIntegrable (logDeriv g) w r :=
    ContinuousOn.circleIntegrable hr.le
      (hlogA.continuousOn.mono Metric.sphere_subset_closedBall)
  -- Compute the split integral: Cauchy term gives `n·2πi`, Goursat term gives `0`.
  have hint : (∮ z in C(w, r), ((n : ℂ) * (z - w)⁻¹ + logDeriv g z))
      = (n : ℂ) * (2 * (Real.pi : ℂ) * Complex.I) := by
    rw [circleIntegral.integral_add hInt1 hInt2,
      circleIntegral.integral_const_mul, circleIntegral.integral_sub_center_inv w hr.ne',
      circleIntegral_logDeriv_eq_zero_of_analyticOnNhd hr.le hg_an_cb hg_ne_cb, add_zero]
  rw [circleIntegral.integral_congr hr.le hEqOn, hint,
    mul_comm (n : ℂ) (2 * (Real.pi : ℂ) * Complex.I), ← mul_assoc,
    inv_mul_cancel₀ two_pi_I_ne_zero', one_mul]

/-! ### The residue-SUM engine — via global zero/pole extraction (no contour deformation)

The argument principle is assembled here **without** any multiply-connected contour
deformation. The classical "deform the big contour onto small circles around each
puncture" route needs a homology/winding engine that Mathlib v4.24.0 lacks
(`Complex.residue`, `windingNumber`, and every off-centre / keyhole contour-deformation
lemma are absent — verified 2026-07-20 by `#check`; only the *concentric* annulus
deformation `circleIntegral_eq_of_differentiable_on_annulus_off_countable` and the
on-disc Cauchy integral formula are present). Instead we use the **global Weierstrass
factorization** `MeromorphicOn.extract_zeros_poles`: on the closed disc,
`f = (∏ᶠ_w (·-w)^{ord_w f}) · g` with `g` analytic and nonvanishing, so
`logDeriv f = Σ_w (ord_w f)·(·-w)⁻¹ + logDeriv g` on the bounding circle. The
off-centre difficulty dissolves because the Cauchy integral of a *bare* simple pole
`∮_{C(c,R)} (z-w)⁻¹ = 2πi` holds for **every** interior `w ∈ B(c,R)`
(`circleIntegral.integral_sub_center_inv`'s off-centre companion
`circleIntegral.integral_sub_inv_of_mem_ball`), and the analytic part integrates to `0`
by Cauchy–Goursat. Summing over the finite divisor support gives the argument principle
directly — **fully sorry-free**. -/

/-- **Integrability of a Finset of simple poles on the bounding circle (sorry-free).**
For radii-free simple poles `Σ_{u∈T} a u·(z-u)⁻¹` with every `u ∈ T` interior to the
disc `B(c,R)`, the integrand is continuous on the bounding circle `C(c,R)` (no `u` lies
on it), hence circle-integrable. -/
lemma circleIntegrable_sum_simple_poles {c : ℂ} {R : ℝ} (hR : 0 ≤ R) (T : Finset ℂ)
    (a : ℂ → ℂ) (hT : ∀ u ∈ T, u ∈ Metric.ball c R) :
    CircleIntegrable (fun z => ∑ u ∈ T, a u * (z - u)⁻¹) c R := by
  apply ContinuousOn.circleIntegrable hR
  apply continuousOn_finset_sum
  intro u hu
  apply continuousOn_const.mul
  apply ContinuousOn.inv₀ (continuousOn_id.sub continuousOn_const)
  intro z hz
  have hne : z ≠ u := by
    intro h
    have hzc : dist z c = R := by simpa using hz
    have huc : dist u c < R := hT u hu
    rw [h] at hzc
    exact absurd hzc (by linarith)
  exact sub_ne_zero.mpr hne

/-- **Sum-swap for a Finset of interior simple poles (sorry-free).** The contour integral
of `Σ_{u∈T} a u·(z-u)⁻¹` over `C(c,R)` is `Σ_{u∈T} a u·2πi`, by
`circleIntegral.integral_sub_inv_of_mem_ball` (the off-centre Cauchy pole integral) applied
term by term. This is the sum side of the argument principle's contour integral. -/
lemma circleIntegral_sum_simple_poles {c : ℂ} {R : ℝ} (hR : 0 ≤ R) (T : Finset ℂ)
    (a : ℂ → ℂ) (hT : ∀ u ∈ T, u ∈ Metric.ball c R) :
    (∮ z in C(c, R), ∑ u ∈ T, a u * (z - u)⁻¹)
      = ∑ u ∈ T, a u * (2 * (Real.pi : ℂ) * Complex.I) := by
  classical
  have hci : ∀ (T' : Finset ℂ), (∀ u ∈ T', u ∈ Metric.ball c R) →
      CircleIntegrable (fun z => ∑ u ∈ T', a u * (z - u)⁻¹) c R :=
    fun T' hT' => circleIntegrable_sum_simple_poles hR T' a hT'
  induction T using Finset.induction with
  | empty =>
      simp only [Finset.sum_empty]
      simp only [circleIntegral, smul_zero, intervalIntegral.integral_zero]
  | @insert x s hx ih =>
      have hxb : x ∈ Metric.ball c R := hT x (Finset.mem_insert_self x s)
      have hsb : ∀ u ∈ s, u ∈ Metric.ball c R := fun u hu => hT u (Finset.mem_insert_of_mem hu)
      have hInt1 : CircleIntegrable (fun z => a x * (z - x)⁻¹) c R := by
        have := hci {x} (by simpa using hxb)
        simpa using this
      have hInt2 : CircleIntegrable (fun z => ∑ u ∈ s, a u * (z - u)⁻¹) c R := hci s hsb
      have hfun : (fun z => ∑ u ∈ insert x s, a u * (z - u)⁻¹)
          = (fun z => a x * (z - x)⁻¹ + ∑ u ∈ s, a u * (z - u)⁻¹) := by
        funext z; rw [Finset.sum_insert hx]
      rw [hfun, circleIntegral.integral_add hInt1 hInt2]
      rw [circleIntegral.integral_const_mul, circleIntegral.integral_sub_inv_of_mem_ball hxb]
      rw [ih hsb]
      rw [Finset.sum_insert hx]

/-! ### The global argument principle — PROVED sorry-free (via global factorization) -/

/-- **The argument principle.** For `f` meromorphic on the closed disc
`\overline B(c,R)`, analytic and nonvanishing off a finite set `S ⊆ B(c,R)` of
zeros/poles (`hfU`, `hfne` — the precise "no zeros or poles other than `S`, and none
on the boundary circle" hypotheses), the contour integral of `f'/f` counts the
interior divisor:
`(2πi)⁻¹ ∮_{C(c,R)} logDeriv f = Σ_{w∈S} ord_w f`,
where `S` enumerates the finitely many interior points where the divisor is nonzero.
Combined with `zeroCount_sub_poleCount_eq_sum_divisor`, the RHS is `#zeros − #poles`
with multiplicity.

**PROVED fully sorry-free** via the global Weierstrass factorization
`MeromorphicOn.extract_zeros_poles`: `f = (∏ᶠ_w (·-w)^{ord_w f}) · g` on the closed disc
with `g` analytic nonvanishing, so on the bounding circle
`logDeriv f = Σ_{w∈S} (ord_w f)·(·-w)⁻¹ + logDeriv g`. Integrating,
`∮_{C(c,R)} logDeriv f = Σ_{w∈S} (ord_w f)·2πi + 0`: each bare simple pole gives
`∮_{C(c,R)} (z-w)⁻¹ = 2πi` for every interior `w`
(`circleIntegral.integral_sub_inv_of_mem_ball` — off-centre, no deformation needed) and
the analytic remainder `logDeriv g` integrates to `0` by Cauchy–Goursat
(`circleIntegral_logDeriv_eq_zero_of_analyticOnNhd`). Multiplying by `(2πi)⁻¹` gives the
divisor sum. No contour deformation is used. -/
theorem argument_principle {f : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
    (hf : MeromorphicOn f (Metric.closedBall c R))
    (S : Finset ℂ)
    (hfU : AnalyticOnNhd ℂ f (Metric.closedBall c R \ (S : Set ℂ)))
    (hfne : ∀ z ∈ Metric.closedBall c R, z ∉ S → f z ≠ 0)
    (hS : (S : Set ℂ) =
      {z | z ∈ Metric.ball c R ∧ (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0}) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(c, R), logDeriv f z)
      = ((∑ w ∈ S, (MeromorphicOn.divisor f (Metric.closedBall c R)) w : ℤ) : ℂ) := by
  classical
  set U : Set ℂ := Metric.closedBall c R with hUdef
  set D : ℂ → ℤ := fun z => (MeromorphicOn.divisor f U) z with hDdef
  -- Each puncture interior.
  have hSball : ∀ w ∈ S, w ∈ Metric.ball c R := by
    intro w hw
    have : w ∈ {z | z ∈ Metric.ball c R ∧ (MeromorphicOn.divisor f U) z ≠ 0} :=
      hS ▸ Finset.mem_coe.mpr hw
    exact this.1
  -- U compact & connected.
  have hUcompact : IsCompact U := isCompact_closedBall c R
  have hUconn : IsConnected U :=
    (convex_closedBall c R).isConnected ⟨c, Metric.mem_closedBall_self hR.le⟩
  -- Divisor value 0 at analytic-nonvanishing points.
  have hD0 : ∀ z ∈ U, z ∉ S → D z = 0 := by
    intro z hzU hznS
    have haz : AnalyticAt ℂ f z := hfU z ⟨hzU, by simpa using hznS⟩
    have hne : f z ≠ 0 := hfne z hzU hznS
    have hord : meromorphicOrderAt f z = 0 := by
      rw [haz.meromorphicOrderAt_eq, analyticOrderAt_eq_zero.mpr (Or.inr hne)]; rfl
    show (MeromorphicOn.divisor f U) z = 0
    rw [hf.divisor_apply hzU, hord]; rfl
  -- Order ≠ ⊤ everywhere (from a boundary witness + connectedness).
  have horder_ne : ∀ u : U, meromorphicOrderAt f (u : ℂ) ≠ ⊤ := by
    have hz0dist : dist (c + (R : ℂ)) c = R := by
      rw [Complex.dist_eq, add_sub_cancel_left]; simp [abs_of_pos hR]
    have hz0U : (c + (R : ℂ)) ∈ U := by
      rw [hUdef, Metric.mem_closedBall, hz0dist]
    have hz0nS : (c + (R : ℂ)) ∉ S := by
      intro h; have := hSball _ h; rw [Metric.mem_ball, hz0dist] at this; exact lt_irrefl R this
    have hz0order : meromorphicOrderAt f (c + (R : ℂ)) ≠ ⊤ := by
      have haz : AnalyticAt ℂ f (c + (R : ℂ)) := hfU _ ⟨hz0U, by simpa using hz0nS⟩
      have hne : f (c + (R : ℂ)) ≠ 0 := hfne _ hz0U hz0nS
      rw [haz.meromorphicOrderAt_eq, analyticOrderAt_eq_zero.mpr (Or.inr hne)]
      simp
    exact (hf.exists_meromorphicOrderAt_ne_top_iff_forall hUconn).mp ⟨⟨_, hz0U⟩, hz0order⟩
  -- Divisor support finite.
  have hDsupp_fin : (MeromorphicOn.divisor f U).support.Finite :=
    (MeromorphicOn.divisor f U).finiteSupport hUcompact
  -- Global factorization `f = (∏ᶠ (·-u)^(ord u)) • g` on `U`.
  obtain ⟨g, hg_an, hg_ne, hfeq⟩ := hf.extract_zeros_poles horder_ne hDsupp_fin
  have hg_ne_cb : ∀ z ∈ U, g z ≠ 0 := fun z hz => hg_ne ⟨z, hz⟩
  -- The factor family is supported inside `S`.
  have hmulsub : Function.mulSupport (fun u => (fun x : ℂ => x - u) ^ (D u)) ⊆ (S : Set ℂ) := by
    intro u hu
    by_contra hnS
    apply hu
    have hDu : D u = 0 := by
      by_cases hUu : u ∈ U
      · exact hD0 u hUu hnS
      · exact (MeromorphicOn.divisor f U).apply_eq_zero_of_notMem hUu
    show (fun x : ℂ => x - u) ^ (D u) = 1
    rw [hDu]; funext x; simp
  -- Explicit Finset-product factorization.
  set P : ℂ → ℂ := fun z => ∏ u ∈ S, (z - u) ^ (D u) with hPdef
  set F : ℂ → ℂ := fun z => P z * g z with hFdef
  have hFeq : f =ᶠ[Filter.codiscreteWithin U] F := by
    have hRHS : ((∏ᶠ (u : ℂ), (fun x : ℂ => x - u) ^ (D u)) • g) = F := by
      funext z
      rw [Pi.smul_apply', smul_eq_mul, finprod_eq_prod_of_mulSupport_subset _ hmulsub,
        Finset.prod_apply]
      rfl
    rw [← hRHS]; exact hfeq
  -- Logarithmic derivative agrees on the bounding circle with the pole-sum + `logDeriv g`.
  have hEqOn : Set.EqOn (logDeriv f)
      (fun z => (∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) + logDeriv g z) (Metric.sphere c R) := by
    intro z hz
    have hzU : z ∈ U := by simpa only [hUdef] using Metric.sphere_subset_closedBall hz
    have hzdist : dist z c = R := by simpa using hz
    have hznS : z ∉ S := by
      intro h; have := hSball z h; rw [Metric.mem_ball, hzdist] at this; exact lt_irrefl R this
    have hzu : ∀ u ∈ S, z ≠ u := by
      intro u hu h; have := hSball u hu
      rw [Metric.mem_ball, ← h, hzdist] at this; exact lt_irrefl R this
    -- Differentiability / analyticity of the explicit factorization at `z`.
    have hgz : g z ≠ 0 := hg_ne_cb z hzU
    have hgdiff : DifferentiableAt ℂ g z := (hg_an z hzU).differentiableAt
    have hPeq : P = ∏ u ∈ S, (fun z : ℂ => (z - u) ^ (D u)) := by
      funext w; rw [hPdef, Finset.prod_apply]
    have hPdiff : DifferentiableAt ℂ P z := by
      rw [hPeq]
      exact DifferentiableAt.finset_prod
        (fun u hu => (differentiableAt_id.sub_const u).zpow (Or.inl (sub_ne_zero.2 (hzu u hu))))
    have hFana : AnalyticAt ℂ F z := by
      have hPana : AnalyticAt ℂ P z := by
        rw [hPeq]
        exact Finset.analyticAt_prod _
          (fun u hu => (analyticAt_id.sub analyticAt_const).zpow (sub_ne_zero.2 (hzu u hu)))
      exact hPana.mul (hg_an z hzU)
    -- `f =ᶠ[𝓝 z] F` at the boundary point `z`.
    have hfmero : MeromorphicAt f z := hf z hzU
    have hFmero : MeromorphicAt F z := hFana.meromorphicAt
    have hznotball : z ∉ Metric.ball c R := by
      rw [Metric.mem_ball, hzdist]; exact lt_irrefl R
    have hacc : AccPt z (Filter.principal U) := by
      rw [hUdef, accPt_principal_iff_nhdsWithin]
      have hbase : (nhdsWithin z (Metric.ball c R)).NeBot := by
        rw [← mem_closure_iff_nhdsWithin_neBot, closure_ball c hR.ne']
        exact hzU
      refine hbase.mono (nhdsWithin_mono z ?_)
      intro w hw
      exact ⟨Metric.ball_subset_closedBall hw, fun hwz => hznotball (hwz ▸ hw)⟩
    have hne1 : f =ᶠ[nhdsWithin z {z}ᶜ] F :=
      hfmero.eventuallyEq_nhdsNE_of_eventuallyEq_codiscreteWithin hFmero hzU hacc hFeq
    -- value equality via continuity
    have hval : f z = F z := by
      have hfcont : ContinuousAt f z :=
        (hfU z ⟨hzU, by simpa using hznS⟩).continuousAt
      have hFcont : ContinuousAt F z := hFana.continuousAt
      have h1 : Filter.Tendsto f (nhdsWithin z {z}ᶜ) (nhds (f z)) := hfcont.continuousWithinAt
      have h2 : Filter.Tendsto F (nhdsWithin z {z}ᶜ) (nhds (F z)) := hFcont.continuousWithinAt
      exact tendsto_nhds_unique h1 (h2.congr' hne1.symm)
    have hnhds : f =ᶠ[nhds z] F := eventuallyEq_nhds_of_eventuallyEq_nhdsNE hne1 hval
    have hstep : logDeriv f z = logDeriv F z := by
      unfold logDeriv
      rw [Pi.div_apply, Pi.div_apply, hnhds.deriv_eq, hnhds.eq_of_nhds]
    rw [hstep]
    -- logDeriv F z = (∑ ...) + logDeriv g z
    have hPz : P z ≠ 0 := by
      rw [hPdef]
      exact Finset.prod_ne_zero_iff.mpr (fun u hu => zpow_ne_zero _ (sub_ne_zero.2 (hzu u hu)))
    have hsplit : logDeriv F z = logDeriv P z + logDeriv g z := by
      rw [hFdef]; exact logDeriv_mul z hPz hgz hPdiff hgdiff
    rw [hsplit]
    -- logDeriv P z = ∑ u ∈ S, D u * (z - u)⁻¹
    have hlogP : logDeriv P z = ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹ := by
      rw [hPdef]
      rw [logDeriv_prod S (fun u z => (z - u) ^ (D u)) z
        (fun u hu => zpow_ne_zero _ (sub_ne_zero.2 (hzu u hu)))
        (fun u hu => (differentiableAt_id.sub_const u).zpow (Or.inl (sub_ne_zero.2 (hzu u hu))))]
      refine Finset.sum_congr rfl (fun u hu => ?_)
      have hd : DifferentiableAt ℂ (fun x : ℂ => x - u) z := differentiableAt_id.sub_const u
      rw [logDeriv_fun_zpow hd (D u)]
      have hlz : logDeriv (fun x : ℂ => x - u) z = (z - u)⁻¹ := by
        have hd : deriv (fun x : ℂ => x - u) z = 1 := ((hasDerivAt_id z).sub_const u).deriv
        rw [logDeriv_apply, hd]; simp
      rw [hlz]
    rw [hlogP]
  -- Assemble the integral.
  have hIntSum : CircleIntegrable (fun z => ∑ u ∈ S, (D u : ℂ) * (z - u)⁻¹) c R :=
    circleIntegrable_sum_simple_poles hR.le S (fun u => (D u : ℂ)) hSball
  have hlogA : AnalyticOnNhd ℂ (logDeriv g) U := (hg_an.deriv).div hg_an hg_ne_cb
  have hIntLog : CircleIntegrable (logDeriv g) c R :=
    ContinuousOn.circleIntegrable hR.le
      (hlogA.continuousOn.mono (by simpa only [hUdef] using Metric.sphere_subset_closedBall))
  rw [circleIntegral.integral_congr hR.le hEqOn,
    circleIntegral.integral_add hIntSum hIntLog,
    circleIntegral_sum_simple_poles hR.le S (fun u => (D u : ℂ)) hSball,
    circleIntegral_logDeriv_eq_zero_of_analyticOnNhd hR.le
      (by simpa only [hUdef] using hg_an) (by simpa only [hUdef] using hg_ne_cb),
    add_zero, ← Finset.sum_mul,
    mul_comm (∑ u ∈ S, (D u : ℂ)) (2 * (Real.pi : ℂ) * Complex.I), ← mul_assoc,
    inv_mul_cancel₀ two_pi_I_ne_zero', one_mul, ← Int.cast_sum]

/-! ### PI-3 canonical-product application: zero-counting for entire `f` -/

/-- **Zero count of an entire function (canonical-product application).** For `f`
entire (`Differentiable ℂ f`) — in particular a Hadamard canonical product (PI-1) —
there are no poles, so `divisor ≥ 0` and the argument principle counts *zeros*:
`(2πi)⁻¹ ∮_{C(c,R)} f'/f = zeroCount = #zeros in B(c,R)` with multiplicity.

This is the PI-3 payload for the pentagon program: it makes the number of zeros of
the canonical minimal Faddeev product `phiBProd` inside a disc an explicit contour
integral, the tool that pins `phiBProd` among its elliptic multiples.

**PROVED fully sorry-free** — a specialization of
`argument_principle` to the entire (pole-free) case. `f` entire ⇒ analytic
everywhere (so the `hfU` hypothesis is free) and `meromorphicOrderAt f w ≥ 0` at
every `w` (`AnalyticAt.meromorphicOrderAt_nonneg`), hence `divisor f ≥ 0` on `S`, so
`Σ_{w∈S} divisor w = zeroCount`. `hfne` (no zeros off `S`) is passed through — it is
the precise "`S` enumerates all zeros in the disc" hypothesis. -/
theorem entire_zero_count {f : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
    (hf : Differentiable ℂ f)
    (S : Finset ℂ)
    (hfne : ∀ z ∈ Metric.closedBall c R, z ∉ S → f z ≠ 0)
    (hS : (S : Set ℂ) =
      {z | z ∈ Metric.ball c R ∧
        (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0}) :
    (2 * (Real.pi : ℂ) * Complex.I)⁻¹ * (∮ z in C(c, R), logDeriv f z)
      = (zeroCount (fun z => (MeromorphicOn.divisor f (Metric.closedBall c R)) z) S : ℂ) := by
  classical
  have hAuniv : AnalyticOnNhd ℂ f Set.univ := hf.differentiableOn.analyticOnNhd isOpen_univ
  have hMero : MeromorphicOn f (Metric.closedBall c R) :=
    (hAuniv.mono (Set.subset_univ _)).meromorphicOn
  have hfU : AnalyticOnNhd ℂ f (Metric.closedBall c R \ (S : Set ℂ)) :=
    hAuniv.mono (Set.subset_univ _)
  have key := argument_principle hR hMero S hfU hfne hS
  -- Entire ⇒ no poles ⇒ divisor ≥ 0 on `S`, so `Σ divisor = zeroCount`.
  have hnn : ∀ w ∈ S, 0 ≤ (MeromorphicOn.divisor f (Metric.closedBall c R)) w := by
    intro w hw
    have hwcb : w ∈ Metric.closedBall c R := by
      have hmem : w ∈ {z | z ∈ Metric.ball c R ∧
          (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0} := hS ▸ Finset.mem_coe.mpr hw
      exact Metric.ball_subset_closedBall hmem.1
    rw [hMero.divisor_apply hwcb]
    exact WithTop.untop₀_nonneg.mpr ((hAuniv w (Set.mem_univ w)).meromorphicOrderAt_nonneg)
  have hZ : (∑ w ∈ S, (MeromorphicOn.divisor f (Metric.closedBall c R)) w)
      = ((zeroCount (fun z => (MeromorphicOn.divisor f (Metric.closedBall c R)) z) S : ℕ) : ℤ) := by
    rw [zeroCount, Nat.cast_sum]
    exact (Finset.sum_congr rfl (fun w hw => (Int.toNat_of_nonneg (hnn w hw)).symm))
  rw [key, hZ, Int.cast_natCast]

end QOU.Mathlib.ArgumentPrinciple
