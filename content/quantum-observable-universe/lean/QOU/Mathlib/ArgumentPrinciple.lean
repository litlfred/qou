import Mathlib.Analysis.Meromorphic.Divisor
import Mathlib.Analysis.Meromorphic.Order
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
zero-counting BOTH reduce to it (`elliptic_divisor_degree_zero` names the argument
principle as its explicit open core; a canonical product's zero count is this
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

**Now DERIVED sorry-free (2026-07-20 — the global statements, modulo one gap):**

* `argument_principle` — the global statement (contour integral = divisor sum), now
  **proved sorry-free** by composing `contour_deformation_sum` (the topological
  residual, below) with the *proved* per-puncture residue `residue_logDeriv_eq_order`.
  Its per-puncture hypotheses (`f` meromorphic at `w`, analytic + nonvanishing on
  `B(c,R) \ S`, `ord_w f = divisor value`) are discharged from the global hypotheses
  via `MeromorphicOn.divisor_apply` + `WithTop.coe_untop₀_of_ne_top`.
* `entire_zero_count` — the PI-3 **canonical-product application**, now **proved
  sorry-free** by specializing `argument_principle` to entire `f`: no poles ⇒
  `divisor ≥ 0` (`AnalyticAt.meromorphicOrderAt_nonneg`), so `Σ ord = zeroCount`.

**The contour-deformation layer — REDUCED (2026-07-20) to a single topological `sorry`:**

* `exists_puncture_radii` — the **geometric half**: a choice of positive radii whose
  closed small discs lie in `B(c,R)` and avoid every *other* puncture. **PROVED
  sorry-free** (metric topology: `B(c,R) \ (S\{w})` is open and contains `w`).
* `contour_deformation_sum` — the packaged statement (existential radii + the deformation
  identity), now **assembled** from the radius selection, the `|S| = 0` **base case**
  (Cauchy–Goursat on the whole disc — **proved sorry-free here**, so the empty-puncture
  instance of the argument principle is fully closed), and the topological core below.
* `residue_theorem_deformation` — the **single remaining `sorry`**: the multiply-connected
  Cauchy theorem for `|S| ≥ 1` (`∮_{C(c,R)} h = Σ_{w∈S} ∮_{C(w,ρ w)} h`, given the radii).
  Pure topology — the off-centre / multi-hole **homology** deformation at the heart of
  the residue theorem, fully isolated from the analysis (everything analytic is proved).
  Carries a cited `-- Ref:`. **Not** vacuous `True`, **not** axiomatized as proved
  (§Axiomatization-is-NOT-a-Proof): the real topological statement, left open. Mathlib
  v4.24.0 has only the *concentric* annulus deformation (puncture at the centre) and the
  on-disc Cauchy integral formula — neither covers an off-centre or multiple puncture,
  so even `|S| = 1` with `w ≠ c` is absent.

## Mathlib v4.24.0 gap — exactly what is present vs. absent

Present: `Complex.CauchyIntegral` (`circleIntegral_sub_center_inv_smul_of_…`,
the Cauchy integral / residue of a *simple explicit* pole `(z-c)⁻¹`),
`MeromorphicOn.divisor` (the ℤ-valued zeros-minus-poles counting function, with
`divisor_apply`, `divisor_mul`, `divisor_inv`, `divisor_nonneg`),
`meromorphicOrderAt` (per-point order), `logDeriv` (`= f'/f`, with `logDeriv_mul`,
`logDeriv_zpow`), Jensen's formula (`Analysis/Complex/JensenFormula`,
`extract_zeros_poles`), and the Nevanlinna value-distribution cone
(`Analysis/Complex/ValueDistribution/`, `logCounting`, First Main Theorem).

Absent: the **residue-SUM engine** — the contour-deformation that sums the local
residues over the interior divisor points. The *local* half (`f'/f` develops a simple
pole of residue `ord_w f` at each zero/pole `w`) is now **proved here** as
`residue_logDeriv_eq_order`, assembled from the Cauchy formula for a bare `(z-c)⁻¹`
factor (present) plus the germ factorization (`meromorphicOrderAt_eq_int_iff`, present).
What remains absent is the *global* half: `Complex.residue`, a general residue theorem,
and `windingNumber` are all missing (re-verified 2026-07-20 by `#check` — only the
single-puncture Cauchy integral formula
`circleIntegral_sub_inv_smul_of_differentiable_on_off_countable` and the rectangle
vanishing `integral_boundary_rect_eq_zero_of_differentiable_on_off_countable` are
present), so deforming the big contour `C(c,R)` onto small circles around each divisor
point and summing has no Mathlib engine. The residual gap is now **exactly** that pure
topological deformation, isolated as `contour_deformation_sum`; the residue-sum
*assembly* (`argument_principle`, `entire_zero_count`) is derived from it sorry-free.

-- Ref: [manuscript] Argument principle / residue of the logarithmic derivative;
--   standard complex analysis (Ahlfors, *Complex Analysis*, Ch. 5 §2; Conway
--   VI.1). Absent from Mathlib v4.24.0. See
--   docs/audits/2026-07-20-argument-principle-scaffold.md.

## VERIFICATION STATUS (STRICT, honest)

**COMPILE-VERIFIED `lean`-direct, exit 0** (2026-07-20, this environment; the
Analysis oleans present — `Complex.CauchyIntegral`, `CircleIntegral`,
`Meromorphic/*`, `Calculus/LogDeriv` — turned out sufficient to elaborate the import
cone via `LEAN_PATH` over the package olean dirs). Sorry-free bricks:
`toNat_sub_toNat_neg`, `zeroCount_sub_poleCount_eq_sum_divisor`, `two_pi_I_ne_zero'`,
and the three new analytic bricks `logDeriv_zpow_sub_mul_split`,
`inv_two_pi_I_mul_integral_nat_sub_center_inv`,
`circleIntegral_logDeriv_eq_zero_of_analyticOnNhd`. `residue_logDeriv_eq_order` is now
**fully sorry-free** (2026-07-20); the geometric brick `exists_puncture_radii` and the
`|S| = 0` base case inside `contour_deformation_sum` are **also sorry-free** (2026-07-20);
and `contour_deformation_sum` + `argument_principle` + `entire_zero_count` compile,
*derived* from the single remaining topological gap `residue_theorem_deformation`
(the `|S| ≥ 1` multiply-connected Cauchy deformation). The only warning is one intended
`declaration uses 'sorry'` (`residue_theorem_deformation`), with a cited `-- Ref:` — the
off-centre / multi-hole homology contour-deformation engine still absent from Mathlib
v4.24.0. Not vacuous `True`, not axiomatized as proved. A full `lake build QOU` on a
host with the complete Analysis cone remains the CI gate.
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

/-! ### The residue-SUM engine — the single remaining topological gap

The one genuine Mathlib v4.24.0 gap. The *analytic* per-puncture residue is proved
(`residue_logDeriv_eq_order`); what remains is the *topological* deformation of the
big contour onto small circles around each puncture. `Complex.residue`,
`windingNumber`, and every annulus/keyhole contour-deformation lemma are **absent**
from Mathlib v4.24.0 (verified 2026-07-20 by `#check`), so this deformation has no
engine and is stated with a single cited `sorry`, isolated from the proved analysis. -/

/-- **Radius selection for the punctures (metric-topology brick — sorry-free).**
For a finite puncture set `S ⊆ B(c,R)`, there is a choice of positive radii `ρ w`
whose *closed* small discs `\overline B(w, ρ w)` each lie inside the open disc
`B(c,R)` and avoid every *other* puncture: `closedBall w (ρ w) ⊆ B(c,R) \ (S \ {w})`.

This is the geometric half of `contour_deformation_sum` and is **fully proved**: for
each `w ∈ S` the region `B(c,R) \ (S \ {w})` is open (an open ball minus a finite,
hence closed, set) and contains `w`, so a small enough closed ball around `w` sits
inside it. The radii are extracted pointwise with `choose!`. No disjointness of the
small discs is required — the residue identity is a winding-number (homology)
statement, so it suffices that each closed disc contains *no other* puncture; two
discs may overlap as long as neither swallows the other's centre. -/
theorem exists_puncture_radii {c : ℂ} {R : ℝ}
    (S : Finset ℂ) (hSball : ∀ w ∈ S, w ∈ Metric.ball c R) :
    ∃ ρ : ℂ → ℝ,
      (∀ w ∈ S, 0 < ρ w) ∧
      (∀ w ∈ S, Metric.closedBall w (ρ w) ⊆ Metric.ball c R \ ((S : Set ℂ) \ {w})) := by
  classical
  have key : ∀ w ∈ S, ∃ r : ℝ, 0 < r ∧
      Metric.closedBall w r ⊆ Metric.ball c R \ ((S : Set ℂ) \ {w}) := by
    intro w hw
    have hopen : IsOpen (Metric.ball c R \ ((S : Set ℂ) \ {w})) :=
      Metric.isOpen_ball.sdiff (S.finite_toSet.diff).isClosed
    have hmem : w ∈ Metric.ball c R \ ((S : Set ℂ) \ {w}) := ⟨hSball w hw, by simp⟩
    obtain ⟨ε, hε, hball⟩ := Metric.isOpen_iff.mp hopen w hmem
    exact ⟨ε / 2, by positivity, (Metric.closedBall_subset_ball (by linarith)).trans hball⟩
  choose! ρ hρpos hρsub using key
  exact ⟨ρ, hρpos, hρsub⟩

/-- **Multi-punctured residue deformation (the topological core — the single gap).**
Given a finite puncture set `S ⊆ B(c,R)`, radii `ρ w > 0` whose closed small discs lie
in `B(c,R)` and avoid every *other* puncture, and `h` analytic on `\overline B(c,R) \ S`,
the big contour integral equals the sum of the small ones:
`∮_{C(c,R)} h = Σ_{w∈S} ∮_{C(w,ρ w)} h`.

**OPEN — the single remaining topological `sorry`.** This is the homological
deformation at the heart of the residue theorem: the big circle is homologous, in
`\overline B(c,R) \ S`, to the formal sum of the small circles (each of winding number
`1` about its own puncture and `0` about the others), so their integrals of the
holomorphic `h` agree. Every *analytic* ingredient of the argument principle is proved
sorry-free (`residue_logDeriv_eq_order`, the divisor bookkeeping); the *geometric*
half (`exists_puncture_radii`) and the `|S| = 0` base case (Cauchy–Goursat, proved
inside `contour_deformation_sum`) are also discharged. What remains absent from
Mathlib v4.24.0 is exactly this multiply-connected Cauchy theorem: `Complex.residue`,
`windingNumber`, and every annulus/keyhole/homology contour-deformation lemma are
missing (only the *concentric* annulus deformation
`circleIntegral_eq_of_differentiable_on_annulus_off_countable` — puncture at the
centre — and the single on-disc Cauchy integral formula are present, neither of which
covers off-centre or multiple punctures). Not vacuous `True`, not axiomatized as
proved (§Axiomatization-is-NOT-a-Proof): the real topological statement, left open
with a cited `-- Ref:`. -/
theorem residue_theorem_deformation {h : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
    (S : Finset ℂ) (hSball : ∀ w ∈ S, w ∈ Metric.ball c R)
    (hh : AnalyticOnNhd ℂ h (Metric.closedBall c R \ (S : Set ℂ)))
    (ρ : ℂ → ℝ) (hρpos : ∀ w ∈ S, 0 < ρ w)
    (hρsub : ∀ w ∈ S, Metric.closedBall w (ρ w) ⊆ Metric.ball c R \ ((S : Set ℂ) \ {w})) :
    (∮ z in C(c, R), h z) = ∑ w ∈ S, (∮ z in C(w, ρ w), h z) := by
  -- Ref: [manuscript] residue theorem = deform the big contour onto small circles
  --   around each interior puncture and sum (Ahlfors, *Complex Analysis*, Ch. 5 §1,
  --   Cauchy's theorem for multiply-connected regions; Conway VI.2). Absent from
  --   Mathlib v4.24.0: no `Complex.residue`, no winding number, no general (off-centre
  --   / multi-hole) homology contour-deformation. See
  --   docs/audits/2026-07-20-argument-principle-scaffold.md.
  sorry

/-- **Multi-punctured contour deformation (the residue theorem's topological core).**
For `h` analytic on the closed disc `\overline B(c,R)` minus a finite puncture set
`S ⊆ B(c,R)`, the big contour integral equals the sum of the small contour integrals
around the punctures. Concretely there is a choice of radii `ρ w > 0` whose closed
small discs lie in `B(c,R)` and avoid every *other* puncture (`closedBall w (ρ w) ⊆
B(c,R) \ (S \ {w})`), for which
`∮_{C(c,R)} h = Σ_{w∈S} ∮_{C(w,ρ w)} h`.

**REDUCED (2026-07-20).** Now assembled from three separated pieces:

* the radius selection `exists_puncture_radii` (metric topology) — **proved
  sorry-free**;
* the `|S| = 0` base case (Cauchy–Goursat on the whole disc,
  `circleIntegral_eq_zero_of_differentiable_on_off_countable`) — **proved sorry-free
  here**, so the empty-puncture instance of the argument principle is fully closed;
* the pure-topology core `residue_theorem_deformation` for `|S| ≥ 1` — the **single
  remaining cited `sorry`**, the multiply-connected Cauchy theorem (off-centre,
  multi-hole homology deformation) absent from Mathlib v4.24.0.

Every analytic ingredient downstream — the per-puncture residue
`residue_logDeriv_eq_order` and the divisor bookkeeping — is proved sorry-free, and
`argument_principle` / `entire_zero_count` are *derived* from this lemma with no
further `sorry`. -/
theorem contour_deformation_sum {h : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
    (S : Finset ℂ) (hSball : ∀ w ∈ S, w ∈ Metric.ball c R)
    (hh : AnalyticOnNhd ℂ h (Metric.closedBall c R \ (S : Set ℂ))) :
    ∃ ρ : ℂ → ℝ,
      (∀ w ∈ S, 0 < ρ w) ∧
      (∀ w ∈ S, Metric.closedBall w (ρ w) ⊆ Metric.ball c R \ ((S : Set ℂ) \ {w})) ∧
      (∮ z in C(c, R), h z) = ∑ w ∈ S, (∮ z in C(w, ρ w), h z) := by
  classical
  obtain ⟨ρ, hρpos, hρsub⟩ := exists_puncture_radii S hSball
  refine ⟨ρ, hρpos, hρsub, ?_⟩
  rcases S.eq_empty_or_nonempty with rfl | hSne
  · -- Base `|S| = 0`: `h` analytic on the whole closed disc ⇒ Cauchy–Goursat ⇒ `∮ = 0`,
    -- and the RHS is the empty sum. Fully sorry-free.
    simp only [Finset.coe_empty, Set.diff_empty, Finset.sum_empty] at hh ⊢
    refine Complex.circleIntegral_eq_zero_of_differentiable_on_off_countable hR.le
      Set.countable_empty hh.continuousOn ?_
    intro z hz
    exact (hh z (Metric.ball_subset_closedBall (by simpa using hz))).differentiableAt
  · -- `|S| ≥ 1`: the isolated topological core (the single residual `sorry`).
    exact residue_theorem_deformation hR S hSball hh ρ hρpos hρsub

/-! ### The global argument principle — DERIVED (sorry-free modulo `contour_deformation_sum`) -/

/-- **The argument principle.** For `f` meromorphic on the closed disc
`\overline B(c,R)`, analytic and nonvanishing off a finite set `S ⊆ B(c,R)` of
zeros/poles (`hfU`, `hfne` — the precise "no zeros or poles other than `S`, and none
on the boundary circle" hypotheses), the contour integral of `f'/f` counts the
interior divisor:
`(2πi)⁻¹ ∮_{C(c,R)} logDeriv f = Σ_{w∈S} ord_w f`,
where `S` enumerates the finitely many interior points where the divisor is nonzero.
Combined with `zeroCount_sub_poleCount_eq_sum_divisor`, the RHS is `#zeros − #poles`
with multiplicity.

**PROVED sorry-free modulo the single topological gap `contour_deformation_sum`.**
The deformation supplies the small-circle radii and the identity
`∮_{C(c,R)} logDeriv f = Σ_w ∮_{C(w,ρ w)} logDeriv f`; each small-circle term is then
evaluated by the *proved* local residue `residue_logDeriv_eq_order`
(`(2πi)⁻¹ ∮_{C(w,ρ w)} logDeriv f = ord_w f`), whose per-puncture hypotheses (`f`
meromorphic at `w`, analytic + nonvanishing on `U \ {w}` for `U = B(c,R) \ (S\{w})`,
`ord_w f = divisor value`) are all discharged from `hf`, `hfU`, `hfne`, `hS` here.
The `sorry` lives only in `contour_deformation_sum`. -/
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
  -- Each puncture is interior to the disc.
  have hSball : ∀ w ∈ S, w ∈ Metric.ball c R := by
    intro w hw
    have hmem : w ∈ {z | z ∈ Metric.ball c R ∧
        (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0} := hS ▸ Finset.mem_coe.mpr hw
    exact hmem.1
  -- `logDeriv f = f'/f` is analytic on the disc minus the punctures.
  have hlog : AnalyticOnNhd ℂ (logDeriv f) (Metric.closedBall c R \ (S : Set ℂ)) := by
    have hne : ∀ z ∈ Metric.closedBall c R \ (S : Set ℂ), f z ≠ 0 := fun z hz =>
      hfne z hz.1 (by simpa using hz.2)
    simpa only [logDeriv] using (hfU.deriv).div hfU hne
  -- Deform the big contour onto small circles around the punctures.
  obtain ⟨ρ, hρpos, hρsub, hdef⟩ := contour_deformation_sum hR S hSball hlog
  rw [hdef, Finset.mul_sum, Int.cast_sum]
  refine Finset.sum_congr rfl (fun w hw => ?_)
  -- Per puncture: apply the local residue over `U = B(c,R) \ (S \ {w})`.
  have hwball : w ∈ Metric.ball c R := hSball w hw
  have hwcb : w ∈ Metric.closedBall c R := Metric.ball_subset_closedBall hwball
  have hUopen : IsOpen (Metric.ball c R \ ((S : Set ℂ) \ {w})) :=
    Metric.isOpen_ball.sdiff (S.finite_toSet.diff.isClosed)
  have hUsub : Metric.closedBall w (ρ w) ⊆ Metric.ball c R \ ((S : Set ℂ) \ {w}) := hρsub w hw
  -- order at `w` equals the (nonzero) divisor value there
  have hdivne : (MeromorphicOn.divisor f (Metric.closedBall c R)) w ≠ 0 := by
    have hmem : w ∈ {z | z ∈ Metric.ball c R ∧
        (MeromorphicOn.divisor f (Metric.closedBall c R)) z ≠ 0} := hS ▸ Finset.mem_coe.mpr hw
    exact hmem.2
  have hdiv : (MeromorphicOn.divisor f (Metric.closedBall c R)) w
      = (meromorphicOrderAt f w).untop₀ := hf.divisor_apply hwcb
  have hordne : meromorphicOrderAt f w ≠ ⊤ := by
    intro htop; apply hdivne; rw [hdiv, htop]; simp
  have horder : meromorphicOrderAt f w
      = (((MeromorphicOn.divisor f (Metric.closedBall c R)) w : ℤ) : WithTop ℤ) := by
    rw [hdiv]; exact (WithTop.coe_untop₀_of_ne_top hordne).symm
  -- analytic + nonvanishing on `U \ {w} = B(c,R) \ S`
  have hfU' : AnalyticOnNhd ℂ f ((Metric.ball c R \ ((S : Set ℂ) \ {w})) \ {w}) := by
    intro z hz
    have hzw : z ≠ w := by simpa using hz.2
    have hznotS : z ∉ (S : Set ℂ) := fun hzin => hz.1.2 ⟨hzin, by simpa using hzw⟩
    exact hfU z ⟨Metric.ball_subset_closedBall hz.1.1, hznotS⟩
  have hfne' : ∀ z ∈ Metric.ball c R \ ((S : Set ℂ) \ {w}), z ≠ w → f z ≠ 0 := by
    intro z hzU hzw
    have hznotS : z ∉ (S : Set ℂ) := fun hzin => hzU.2 ⟨hzin, by simpa using hzw⟩
    exact hfne z (Metric.ball_subset_closedBall hzU.1) (by simpa using hznotS)
  exact residue_logDeriv_eq_order (hf w hwcb) (hρpos w hw) hUopen hUsub horder hfU' hfne'

/-! ### PI-3 canonical-product application: zero-counting for entire `f` -/

/-- **Zero count of an entire function (canonical-product application).** For `f`
entire (`Differentiable ℂ f`) — in particular a Hadamard canonical product (PI-1) —
there are no poles, so `divisor ≥ 0` and the argument principle counts *zeros*:
`(2πi)⁻¹ ∮_{C(c,R)} f'/f = zeroCount = #zeros in B(c,R)` with multiplicity.

This is the PI-3 payload for the pentagon program: it makes the number of zeros of
the canonical minimal Faddeev product `phiBProd` inside a disc an explicit contour
integral, the tool that pins `phiBProd` among its elliptic multiples.

**PROVED sorry-free modulo `contour_deformation_sum`** — a specialization of
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
