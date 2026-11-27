/-
  Borel resummation — Mathlib-gap scaffold (bean el8w; epic 08a2).

  HONEST SCOPE. Full Borel resummation (Borel transform + Laplace sum +
  Watson's theorem / Nevanlinna–Sokal uniqueness) is NOT in Mathlib and is a
  major multi-file formalization, ultimately destined for upstream mathlib4.
  This file scaffolds the CORE in qou's `QOU/Mathlib/` gap-infra namespace:

    * the Borel transform COEFFICIENT a_n/n! and the partial Borel transform —
      with the defining MECHANISM proved sorry-free: Borel division tames
      factorial divergence (B[Σ n! z^n] has unit coefficients → geometric);
    * NEW (el8w tranche 2, PR #3683 pickup): the Nevanlinna–Sokal hypothesis
      half (i) proved sorry-free — every Gevrey-1 sequence (|a_n| ≤ C·A^n·n!)
      has an absolutely convergent Borel transform on the disc A·|z| < 1, with
      the quantitative bound C/(1 − A|z|); `BorelTransformConverges` is now
      inhabited on its whole natural hypothesis class (`Gevrey1`,
      `borelTransformConverges_of_gevrey1`, `abs_borelTransformValue_le_of_gevrey1`);
    * NEW (el8w tranche 3, `QOU/Mathlib/BorelLaplace.lean`): the Laplace
      TERM-WISE engine proved sorry-free — `∫₀^∞ e^{−t} tⁿ dt = n!`
      (`laplace_pow_eq_factorial`) and the per-term Borel recovery
      `∫₀^∞ e^{−t} (aₙ/n!)(z t)ⁿ dt = aₙ zⁿ` (`laplace_borel_term`): the Borel
      division by `n!` and the Laplace multiplication by `n!` cancel exactly,
      term by term;
    * NEW (el8w tranche 4, `BorelLaplace.lean`): the ∑↔∫ interchange proved
      sorry-free as **regularity** — `borelSum_eq_tsum`: on the disc of
      convergence (`∑ₙ|aₙ||z|ⁿ < ∞`) the Borel sum reproduces the ordinary sum,
      via `integral_tsum`. (The earlier "Gevrey-1 dominating bound" framing was
      corrected: for a DIVERGENT Gevrey-1 series the interchange fails —
      `∑ₙ∫|·| = ∞` — which is the Borel-plane Stokes obstruction itself.)
    * the Watson / Nevanlinna–Sokal UNIQUENESS half (the divergent case: Borel
      sum IS the asymptotic function) remains the genuine Mathlib gap — next
      el8w tranche. NEVER `sorry`-faked.

  Why QOU needs it: Ohtsuki's PROOF of the volume conjecture for the figure-
  eight (the Vol(4_1) saddle, QOU/Knot/FigureEightVolume.VolumeConjecture41)
  goes through Borel resummation of the asymptotic series of the Kashaev sum.
  UPDATE (2026-07-26): `VolumeConjecture41` itself is now DISCHARGED
  sorry-free by the elementary Riemann-sum squeeze
  (`QOU/Knot/FigureEightVolumeSqueeze.lean`, milestone qou-cpfn) — no Borel
  resummation was needed for the 4₁ root-of-unity sum. This file's engine
  remains motivated by the GENERAL volume conjecture and the exact/alien
  calculus program (bean el8w), where Borel-plane methods are load-bearing.

  Pure-ℝ analysis where the integral appears; the coefficient algebra is
  generic. § the hard theorems are explicitly conditional, never `sorry`-faked.

  -- Ref: [leitner2026] bean el8w — Borel resummation Mathlib-gap
-/

import Mathlib.Analysis.SpecialFunctions.Log.Basic
import Mathlib.Topology.Algebra.InfiniteSum.Basic
import Mathlib.Analysis.SpecificLimits.Normed
import Mathlib.Tactic

namespace QOU.Mathlib.Borel

open scoped Nat
open Filter

/-- The Borel transform coefficient of a formal series `Σ aₙ zⁿ`: `aₙ / n!`. -/
noncomputable def borelCoeff (a : ℕ → ℝ) (n : ℕ) : ℝ := a n / (n ! : ℝ)

/-- The partial Borel transform `Σ_{n=0}^{N} (aₙ/n!) tⁿ`. -/
noncomputable def partialBorel (a : ℕ → ℝ) (N : ℕ) (t : ℝ) : ℝ :=
  ∑ n ∈ Finset.range (N + 1), borelCoeff a n * t ^ n

/-- **The Borel mechanism: division by n! tames factorial divergence.**
    The (everywhere-divergent) series `Σ n! zⁿ` has unit Borel coefficients —
    its Borel transform is the geometric series `Σ tⁿ = 1/(1−t)`. -/
theorem borel_tames_factorial (n : ℕ) :
    borelCoeff (fun k => (k ! : ℝ)) n = 1 := by
  unfold borelCoeff
  exact div_self (by positivity)

/-- Consequently the partial Borel transform of `Σ n! zⁿ` is the geometric
    partial sum `Σ_{n=0}^{N} tⁿ`. -/
theorem partialBorel_factorial (N : ℕ) (t : ℝ) :
    partialBorel (fun k => (k ! : ℝ)) N t = ∑ n ∈ Finset.range (N + 1), t ^ n := by
  unfold partialBorel
  refine Finset.sum_congr rfl (fun n _ => ?_)
  rw [borel_tames_factorial, one_mul]

/-- Borel coefficients are linear in the source sequence. -/
theorem borelCoeff_add (a b : ℕ → ℝ) (n : ℕ) :
    borelCoeff (fun k => a k + b k) n = borelCoeff a n + borelCoeff b n := by
  unfold borelCoeff; rw [add_div]

/-- **Borel-transform convergence** — the first half of Borel summability, with
    genuine content: the partial Borel transforms `Σ_{n≤N}(aₙ/n!)zⁿ` converge as
    `N → ∞` to `value`. (The *second* half — the Laplace resummation
    `∫₀^∞ e^{−t} φ(z t) dt` and Watson / Nevanlinna–Sokal UNIQUENESS — is the
    substantial analysis NOT yet in Mathlib; it is documented in the file
    header as the gap, deliberately not stated with measure-theory imports
    absent from the cache, and NEVER `sorry`-faked.) -/
class BorelTransformConverges (a : ℕ → ℝ) (z : ℝ) : Prop where
  /-- the partial Borel transforms converge to some limit at `z`. -/
  converges :
    ∃ L : ℝ, Filter.Tendsto (fun N => partialBorel a N z) Filter.atTop (nhds L)

/-- The Borel-transform value at `z` (the limit), available once
    `[BorelTransformConverges a z]` is supplied. -/
noncomputable def borelTransformValue (a : ℕ → ℝ) (z : ℝ)
    [h : BorelTransformConverges a z] : ℝ := h.converges.choose

/-- The Borel transform indeed converges to `borelTransformValue`. -/
theorem borelTransform_tendsto (a : ℕ → ℝ) (z : ℝ) [h : BorelTransformConverges a z] :
    Filter.Tendsto (fun N => partialBorel a N z) Filter.atTop
      (nhds (borelTransformValue a z)) :=
  h.converges.choose_spec

/-- **The conditional class is genuinely inhabited** — a sorry-free witness.
    The Borel transform of the series `Σ n! zⁿ` (radius of convergence `0`;
    divergent for every `z ≠ 0`) is the geometric series `Σ zⁿ`, which
    converges on `|z| < 1` to `(1 − z)⁻¹`. This is the concrete analytic
    content that pins `BorelTransformConverges` down to a real convergence
    statement (as opposed to an empty marker): the partial Borel transforms
    of the factorial series tend to `(1 − z)⁻¹`. -/
theorem borelTransform_factorial_tendsto {z : ℝ} (hz : |z| < 1) :
    Filter.Tendsto (fun N => partialBorel (fun k => (k ! : ℝ)) N z) Filter.atTop
      (nhds (1 - z)⁻¹) := by
  have hsum : HasSum (fun n => z ^ n) (1 - z)⁻¹ :=
    hasSum_geometric_of_norm_lt_one (by rwa [Real.norm_eq_abs])
  have h1 : Filter.Tendsto (fun N => ∑ n ∈ Finset.range (N + 1), z ^ n)
      Filter.atTop (nhds (1 - z)⁻¹) :=
    hsum.tendsto_sum_nat.comp (tendsto_add_atTop_nat 1)
  simpa only [partialBorel_factorial] using h1

/-- The factorial series `Σ n! zⁿ` has a convergent Borel transform on the unit
    disc — a nonvacuous instance of the conditional class. -/
instance instBorelTransformConverges_factorial {z : ℝ} (hz : |z| < 1) :
    BorelTransformConverges (fun k => (k ! : ℝ)) z where
  converges := ⟨(1 - z)⁻¹, borelTransform_factorial_tendsto hz⟩

/-- The Borel-transform value of the factorial series is `(1 − z)⁻¹` on the
    unit disc, confirming `borelTransformValue` computes the geometric sum. -/
theorem borelTransformValue_factorial {z : ℝ} (hz : |z| < 1) :
    @borelTransformValue (fun k => (k ! : ℝ)) z (instBorelTransformConverges_factorial hz)
      = (1 - z)⁻¹ :=
  tendsto_nhds_unique
    (@borelTransform_tendsto _ z (instBorelTransformConverges_factorial hz))
    (borelTransform_factorial_tendsto hz)

/-! ### Additivity of the Borel transform

    The Borel transform is a linear operation. At the partial-sum level this is
    `borelCoeff`'s linearity summed; at the limit level it upgrades to closure
    of the convergence class under addition and linearity of the value. -/

/-- The partial Borel transform is additive in the source sequence. -/
theorem partialBorel_add (a b : ℕ → ℝ) (N : ℕ) (t : ℝ) :
    partialBorel (fun k => a k + b k) N t = partialBorel a N t + partialBorel b N t := by
  unfold partialBorel
  rw [← Finset.sum_add_distrib]
  refine Finset.sum_congr rfl (fun n _ => ?_)
  rw [borelCoeff_add, add_mul]

/-- **The convergence class is closed under addition.** If the Borel transforms
    of `a` and `b` both converge at `z`, so does the transform of `a + b`. -/
instance instBorelTransformConverges_add (a b : ℕ → ℝ) (z : ℝ)
    [ha : BorelTransformConverges a z] [hb : BorelTransformConverges b z] :
    BorelTransformConverges (fun k => a k + b k) z where
  converges := by
    obtain ⟨La, hLa⟩ := ha.converges
    obtain ⟨Lb, hLb⟩ := hb.converges
    exact ⟨La + Lb, by simpa only [partialBorel_add] using hLa.add hLb⟩

/-- **The Borel-transform value is additive** — linearity at the limit level. -/
theorem borelTransformValue_add (a b : ℕ → ℝ) (z : ℝ)
    [BorelTransformConverges a z] [BorelTransformConverges b z] :
    borelTransformValue (fun k => a k + b k) z
      = borelTransformValue a z + borelTransformValue b z := by
  refine tendsto_nhds_unique (borelTransform_tendsto _ z) ?_
  simpa only [partialBorel_add] using
    (borelTransform_tendsto a z).add (borelTransform_tendsto b z)

/-- Borel coefficients are homogeneous under scalar multiplication. -/
theorem borelCoeff_smul (c : ℝ) (a : ℕ → ℝ) (n : ℕ) :
    borelCoeff (fun k => c * a k) n = c * borelCoeff a n := by
  unfold borelCoeff; rw [mul_div_assoc]

/-- The partial Borel transform is homogeneous in the source sequence. -/
theorem partialBorel_smul (c : ℝ) (a : ℕ → ℝ) (N : ℕ) (t : ℝ) :
    partialBorel (fun k => c * a k) N t = c * partialBorel a N t := by
  unfold partialBorel
  rw [Finset.mul_sum]
  refine Finset.sum_congr rfl (fun n _ => ?_)
  rw [borelCoeff_smul, mul_assoc]

/-- **The convergence class is closed under scalar multiplication.** -/
instance instBorelTransformConverges_smul (c : ℝ) (a : ℕ → ℝ) (z : ℝ)
    [ha : BorelTransformConverges a z] :
    BorelTransformConverges (fun k => c * a k) z where
  converges := by
    obtain ⟨L, hL⟩ := ha.converges
    exact ⟨c * L, by simpa only [partialBorel_smul] using hL.const_mul c⟩

/-- **The Borel-transform value is homogeneous** — the scalar leg of linearity. -/
theorem borelTransformValue_smul (c : ℝ) (a : ℕ → ℝ) (z : ℝ)
    [BorelTransformConverges a z] :
    borelTransformValue (fun k => c * a k) z = c * borelTransformValue a z := by
  refine tendsto_nhds_unique (borelTransform_tendsto _ z) ?_
  simpa only [partialBorel_smul] using (borelTransform_tendsto a z).const_mul c

/-! ### Gevrey-1 sequences — the hypothesis half of Nevanlinna–Sokal (bean el8w)

    Nevanlinna–Sokal Borel summability has two halves:

    * **(i) Gevrey-1 ⇒ Borel-disc convergence.** A factorial-type bound
      `|aₙ| ≤ C·Aⁿ·n!` forces the Borel-transformed series `Σ (aₙ/n!) zⁿ` to
      converge absolutely on the disc `A·|z| < 1`, with the quantitative bound
      `C/(1 − A·|z|)`. Proved sorry-free below: every Gevrey-1 sequence yields
      a `BorelTransformConverges` instance — the class is inhabited on its
      whole natural hypothesis class, not just the single factorial example.
      This is the growth class the bridge growth-obstruction audit assigns to
      the 4₁ even-channel Ohtsuki ladder ("Gevrey-1 divergent").
    * **(ii) Laplace resummation + uniqueness.** `∫₀^∞ e^{−t} φ(zt) dt`
      recovers the function, uniquely (Watson / Nevanlinna). The term-wise
      engine is `∫₀^∞ tⁿ e^{−t} dt = n!` — the Gamma/measure-theory cone,
      which is NOT in the current olean cache (`Mathlib.Analysis.
      SpecialFunctions.Gamma.Basic`, `Mathlib.MeasureTheory.Integral.
      ExpDecay` unavailable). It stays the documented gap; next el8w tranche
      after the cache cone is extended. NEVER `sorry`-faked here.

    -- Ref: [sokal1980] https://doi.org/10.1063/1.524408 -/

/-- Gevrey-1 (factorial-type) bound: `|aₙ| ≤ C·Aⁿ·n!` — the hypothesis class
    of the Nevanlinna–Sokal theorem. -/
def Gevrey1 (a : ℕ → ℝ) (C A : ℝ) : Prop :=
  ∀ n, |a n| ≤ C * A ^ n * (n ! : ℝ)

/-- The factorial series is Gevrey-1 with `C = A = 1`. -/
theorem gevrey1_factorial : Gevrey1 (fun k => (k ! : ℝ)) 1 1 := by
  intro n
  simp [abs_of_nonneg (by positivity : (0 : ℝ) ≤ (n ! : ℝ))]

/-- **Borel division turns a Gevrey-1 bound into a geometric one**: the Borel
    coefficients of a Gevrey-1 sequence are bounded by `C·Aⁿ`. This is the
    general form of `borel_tames_factorial`. -/
theorem abs_borelCoeff_le_of_gevrey1 {a : ℕ → ℝ} {C A : ℝ}
    (h : Gevrey1 a C A) (n : ℕ) : |borelCoeff a n| ≤ C * A ^ n := by
  have hn : (0 : ℝ) < (n ! : ℝ) := by positivity
  unfold borelCoeff
  rw [abs_div, abs_of_pos hn, div_le_iff₀ hn]
  exact h n

/-- Term-wise geometric domination of the Borel-transformed series on the
    disc: `|(aₙ/n!)·zⁿ| ≤ C·(A·|z|)ⁿ`. -/
theorem abs_borelCoeff_mul_pow_le_of_gevrey1 {a : ℕ → ℝ} {C A : ℝ}
    (h : Gevrey1 a C A) (z : ℝ) (n : ℕ) :
    |borelCoeff a n * z ^ n| ≤ C * (A * |z|) ^ n := by
  calc |borelCoeff a n * z ^ n| = |borelCoeff a n| * |z| ^ n := by
        rw [abs_mul, abs_pow]
    _ ≤ C * A ^ n * |z| ^ n :=
        mul_le_mul_of_nonneg_right (abs_borelCoeff_le_of_gevrey1 h n)
          (pow_nonneg (abs_nonneg z) n)
    _ = C * (A * |z|) ^ n := by rw [mul_pow]; ring

/-- **Gevrey-1 ⇒ absolute summability** of the Borel-transformed series on the
    disc `A·|z| < 1`. -/
theorem summable_abs_borel_of_gevrey1 {a : ℕ → ℝ} {C A z : ℝ}
    (h : Gevrey1 a C A) (hA : 0 ≤ A) (hz : A * |z| < 1) :
    Summable (fun n => |borelCoeff a n * z ^ n|) := by
  have hr : 0 ≤ A * |z| := mul_nonneg hA (abs_nonneg z)
  refine Summable.of_nonneg_of_le (fun n => abs_nonneg _)
    (fun n => abs_borelCoeff_mul_pow_le_of_gevrey1 h z n) ?_
  exact (summable_geometric_of_lt_one hr hz).mul_left C

/-- Gevrey-1 ⇒ summability of the Borel-transformed series itself. -/
theorem summable_borel_of_gevrey1 {a : ℕ → ℝ} {C A z : ℝ}
    (h : Gevrey1 a C A) (hA : 0 ≤ A) (hz : A * |z| < 1) :
    Summable (fun n => borelCoeff a n * z ^ n) :=
  (summable_abs_borel_of_gevrey1 h hA hz).of_abs

/-- The partial Borel transforms of a Gevrey-1 sequence converge on the disc,
    to the sum of the Borel-transformed series. -/
theorem borelTransform_tendsto_tsum_of_gevrey1 {a : ℕ → ℝ} {C A z : ℝ}
    (h : Gevrey1 a C A) (hA : 0 ≤ A) (hz : A * |z| < 1) :
    Filter.Tendsto (fun N => partialBorel a N z) Filter.atTop
      (nhds (∑' n, borelCoeff a n * z ^ n)) := by
  have hs := summable_borel_of_gevrey1 h hA hz
  have h1 := hs.hasSum.tendsto_sum_nat.comp (tendsto_add_atTop_nat 1)
  simpa only [partialBorel] using h1

/-- **Every Gevrey-1 sequence has a convergent Borel transform on its disc**
    (`A·|z| < 1`) — hypothesis half (i) of Nevanlinna–Sokal, sorry-free, as a
    producer of `BorelTransformConverges` instances. -/
theorem borelTransformConverges_of_gevrey1 {a : ℕ → ℝ} {C A z : ℝ}
    (h : Gevrey1 a C A) (hA : 0 ≤ A) (hz : A * |z| < 1) :
    BorelTransformConverges a z :=
  ⟨⟨_, borelTransform_tendsto_tsum_of_gevrey1 h hA hz⟩⟩

/-- Under summability, the class-chosen Borel value IS the sum of the
    Borel-transformed series. -/
theorem borelTransformValue_eq_tsum (a : ℕ → ℝ) (z : ℝ)
    [BorelTransformConverges a z]
    (hs : Summable (fun n => borelCoeff a n * z ^ n)) :
    borelTransformValue a z = ∑' n, borelCoeff a n * z ^ n :=
  tendsto_nhds_unique (borelTransform_tendsto a z)
    (by simpa only [partialBorel] using
      hs.hasSum.tendsto_sum_nat.comp (tendsto_add_atTop_nat 1))

/-- **Quantitative disc bound**: the Borel value of a Gevrey-1 sequence is
    bounded by `C/(1 − A·|z|)` on the disc. (The exponential-type control that
    feeds the Laplace-integrability step of the resummation half.) -/
theorem abs_borelTransformValue_le_of_gevrey1 {a : ℕ → ℝ} {C A z : ℝ}
    [BorelTransformConverges a z]
    (h : Gevrey1 a C A) (hA : 0 ≤ A) (hz : A * |z| < 1) :
    |borelTransformValue a z| ≤ C / (1 - A * |z|) := by
  have hr : 0 ≤ A * |z| := mul_nonneg hA (abs_nonneg z)
  have habs := summable_abs_borel_of_gevrey1 h hA hz
  rw [borelTransformValue_eq_tsum a z habs.of_abs]
  have h1 : |∑' n, borelCoeff a n * z ^ n| ≤ ∑' n, |borelCoeff a n * z ^ n| := by
    simpa only [Real.norm_eq_abs] using
      norm_tsum_le_tsum_norm (f := fun n => borelCoeff a n * z ^ n)
        (by simpa only [Real.norm_eq_abs] using habs)
  refine h1.trans ?_
  have hgeo : Summable (fun n : ℕ => C * (A * |z|) ^ n) :=
    (summable_geometric_of_lt_one hr hz).mul_left C
  have h2 : ∑' n, |borelCoeff a n * z ^ n| ≤ ∑' n : ℕ, C * (A * |z|) ^ n :=
    habs.tsum_le_tsum (fun n => abs_borelCoeff_mul_pow_le_of_gevrey1 h z n) hgeo
  refine h2.trans ?_
  rw [tsum_mul_left, tsum_geometric_of_lt_one hr hz, div_eq_mul_inv]

/-- The original factorial example is subsumed: `Σ n! zⁿ` gets its
    `BorelTransformConverges` instance from the general Gevrey-1 theorem. -/
example {z : ℝ} (hz : |z| < 1) : BorelTransformConverges (fun k => (k ! : ℝ)) z :=
  borelTransformConverges_of_gevrey1 gevrey1_factorial zero_le_one (by simpa using hz)

end QOU.Mathlib.Borel
