import Mathlib.Tactic
import QOU.FluidDynamics.physical_layer_leray

/-!
# `QOU.FluidDynamics.q_ns_part_a_paths` — three parallel attacks on Part A

Bean `qou-innq` (Part A of `conj:regularity-breakdown`). Owner pick
(Carl, 2026-11-27): run vectors V2, V3 and V4 of the attack-vector survey
in parallel, with Part A's data fixed in the **substrate** layer
(`def:qns-unit-layers`). Only QOU-formalised inputs are used, and no
empirical value enters any proof.

Everything here is algebra over a generic linearly ordered field (§7c)
unless a step genuinely needs `ℝ`.

## V2 — the algebraic upper envelope (`substrate_envelope`)

The layer conversion in `qns-unit-layers.lean` (`kPhys_sq_mul`) rescales
wavenumbers and **keeps each mode's energy `e_k` unchanged**. So in the
modal convention the energy is the same number in both layers, and only
the enstrophy converts: `Ω_phys = (q−1)²·Ω_sub`. This answers the survey's
open question 0c ("how does energy convert?") *within that convention*. If
energy were instead integrated over the rescaled physical volume, it would
pick up a volume factor; the corpus does not use that convention.

Consequence. Take a datum held fixed in the substrate layer: `E₀` and
`Ω_sub(0)` do not depend on `q`. Then `Ω_phys(0) = (q−1)²·Ω_sub(0) → 0`,
and the smallness hypotheses of `energy_small_global` (`hcast`, `hhor`,
`Nbad + 1 ≤ H`) involve `E₀` and the model constants `δ, c` only. So
whenever the physical-layer discrete dynamics hold with `q`-uniform
constants, a datum that is energy-small once is energy-small for every `q`
near `1`. On that class
`Ω_sub(n) ≤ 2L/(q−1)²` for every step `n`, with `L` free of `q`. Part A
then holds with exponent **at most 2** there, and `α > 2` is excluded.

Scope: an upper bound on a hypothesis-carrying class. The physical
dissipation step and the damped quadratic step remain the consumer's
hypotheses, exactly as in `energy_small_global`. Nothing here proves
Part A.

## V3 — cascade-depth threshold (`hecke_raise_threshold_*`)

From `thm:groebner-shirshov-energy` item 3, a Hecke step on a monomial of
word length `ℓ` changes the word-length energy by `|c|·(|h|(ℓ−1) − 2)`,
`h = q − q⁻¹`. The step **raises** the energy only when `ℓ > 1 + 2/h`. We
show that threshold is at least `1 + c_q`, with `c_q = 1/(q−1)`, so it
diverges as `q → 1⁺`.

**Not established:** any link between word length `ℓ` and Fourier
wavenumber, or between the word-length energy and the enstrophy. This
section is a combinatorial fact about the braid side only.

## V4 — data exclusions

* `quadratic_decay_le_initial`: if a flow is an exact exponential rescaling
  `U(t) = e^{−νμt}·u` (this is `beltrami_eigen_ns` for Beltrami
  eigenfields, Lamb vector zero) then every quadratic functional, the
  enstrophy included, is maximised at `t = 0`. Beltrami eigen-data held
  fixed in the substrate layer therefore cannot be Part A data.
* `helicity_enstrophy_floor`: Cauchy–Schwarz on modal sums gives
  `H² ≤ E·Ω`. So nonzero helicity gives a **floor** `Ω ≥ H²/E`, not a
  ceiling. This is a scope-(a) negative for the idea that helicity
  conservation bounds Part A growth: it bounds the wrong side.
-/

namespace QOU.FluidDynamics.PartAPaths

open QOU.FluidDynamics.PhysicalLayerLeray

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-! ## V2 — substrate-layer envelope from the physical-layer bound -/

/-- **V2.** Let `Ωs` be the substrate-layer enstrophy along the discrete
    dynamics, and suppose the physical-layer image `Ω_phys = (q−1)²·Ωs`
    satisfies the hypotheses of `energy_small_global` with a `q`-free
    level `L` (the energy is the same in both layers in the modal
    convention). Then for every step `n`,

      `Ωs n ≤ 2·L / (q−1)²`.

    The level `L` is `q`-free, so the envelope has exponent 2 in
    `c_q = 1/(q−1)`. -/
theorem substrate_envelope (E Ωs : ℕ → K) (δ q c d L : K) (Nbad H : ℕ)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2) (hc : 0 ≤ c) (hd : 0 ≤ d)
    (hL : 0 < L)
    (hΩ : ∀ n, 0 ≤ Ωs n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * ((q - 1) ^ 2 * Ωs n))
    (hE : ∀ n, 0 ≤ E n)
    (hstep : ∀ n, (q - 1) ^ 2 * Ωs (n + 1) ≤ (q - 1) ^ 2 * Ωs n
      + δ * ((q - 1) ^ 2 * Ωs n) * (c * ((q - 1) ^ 2 * Ωs n) - d))
    (h0 : (q - 1) ^ 2 * Ωs 0 ≤ L)
    (hcast : 4 / δ * E 0 ≤ (Nbad : K) * L)
    (hhor : (H : K) * (δ * c * L) ≤ 1 / 4)
    (hHN : Nbad + 1 ≤ H) :
    ∀ n, Ωs n ≤ 2 * L / (q - 1) ^ 2 := by
  have hpos : (0 : K) < (q - 1) ^ 2 := by
    have : (0 : K) < q - 1 := sub_pos.mpr hq1
    positivity
  have key := energy_small_global E (fun n => (q - 1) ^ 2 * Ωs n) δ q c d L
    Nbad H hδ hq1 hq2 hc hd hL (fun n => mul_nonneg hpos.le (hΩ n)) hdiss hE
    hstep h0 hcast hhor hHN
  intro n
  rw [le_div_iff₀ hpos]
  have := key n
  simpa [mul_comm] using this

/-- **V2, the data class is `q`-stable.** For a substrate-fixed datum
    (`Ωs₀` independent of `q`) the initial hypothesis `h0` of
    `substrate_envelope` holds for every `q` with `(q−1)²·Ωs₀ ≤ L`; in
    particular it holds on `1 < q ≤ 1 + √(L/Ωs₀)`. Stated without square
    roots: if `(q₀−1)²·Ωs₀ ≤ L` then the same holds for every
    `1 ≤ q ≤ q₀`. -/
theorem initial_level_stable {Ωs₀ L q q₀ : K} (hΩ : 0 ≤ Ωs₀) (hq : 1 ≤ q)
    (hqq₀ : q ≤ q₀) (h : (q₀ - 1) ^ 2 * Ωs₀ ≤ L) :
    (q - 1) ^ 2 * Ωs₀ ≤ L := by
  have h1 : 0 ≤ q - 1 := sub_nonneg.mpr hq
  have h2 : (q - 1) ^ 2 ≤ (q₀ - 1) ^ 2 := by
    apply pow_le_pow_left₀ h1; linarith
  exact le_trans (mul_le_mul_of_nonneg_right h2 hΩ) h

/-! ## V3 — the Hecke-step energy threshold diverges as `q → 1⁺` -/

/-- `h = q − q⁻¹ = (q² − 1)/q` is positive for `q > 1`. -/
theorem hecke_h_pos {q : K} (hq : 1 < q) : 0 < q - q⁻¹ := by
  have h0 : 0 < q := lt_trans one_pos hq
  have : q⁻¹ < 1 := inv_lt_one_of_one_lt₀ hq
  linarith

/-- **V3, sign rule.** For `h > 0` and `c ≠ 0`, the single-step change
    `|c|·(h(ℓ−1) − 2)` of `thm:groebner-shirshov-energy` item 3 is positive
    exactly when `ℓ > 1 + 2/h`. -/
theorem hecke_step_raises_iff {c h ℓ : K} (hc : c ≠ 0) (hh : 0 < h) :
    0 < |c| * (h * (ℓ - 1) - 2) ↔ 1 + 2 / h < ℓ := by
  have hca : 0 < |c| := abs_pos.mpr hc
  rw [mul_pos_iff_of_pos_left hca, sub_pos]
  constructor
  · intro h'
    have : 2 / h < ℓ - 1 := (div_lt_iff₀ hh).mpr (by linarith)
    linarith
  · intro h'
    have : 2 < (ℓ - 1) * h := (div_lt_iff₀ hh).mp (by linarith)
    linarith

/-- **V3, the threshold dominates `1 + c_q`.** For `q > 1`,
    `1 + 1/(q−1) ≤ 1 + 2/(q − q⁻¹)`. So every energy-raising Hecke step
    acts on a word longer than `1 + c_q`. -/
theorem hecke_threshold_ge {q : K} (hq : 1 < q) :
    1 + 1 / (q - 1) ≤ 1 + 2 / (q - q⁻¹) := by
  have h0 : 0 < q := lt_trans one_pos hq
  have hq1 : 0 < q - 1 := sub_pos.mpr hq
  have hh : 0 < q - q⁻¹ := hecke_h_pos hq
  have hrw : q - q⁻¹ = (q - 1) * (q + 1) / q := by
    field_simp; ring
  rw [add_le_add_iff_left, hrw, div_div_eq_mul_div,
    div_le_div_iff₀ hq1 (by positivity)]
  nlinarith

/-- **V3, divergence.** The energy-raising threshold `1 + 2/(q − q⁻¹)`
    tends to `+∞` as `q → 1⁺`. Purely combinatorial; see the module
    docstring for what is *not* established. -/
theorem hecke_threshold_tendsto :
    Filter.Tendsto (fun q : ℝ => 1 + 2 / (q - q⁻¹))
      (nhdsWithin 1 (Set.Ioi 1)) Filter.atTop := by
  have hc : Filter.Tendsto (fun q : ℝ => 1 + 1 / (q - 1))
      (nhdsWithin 1 (Set.Ioi 1)) Filter.atTop := by
    have h1 : Filter.Tendsto (fun q : ℝ => q - 1)
        (nhdsWithin 1 (Set.Ioi 1)) (nhdsWithin 0 (Set.Ioi 0)) := by
      have hc0 : Filter.Tendsto (fun q : ℝ => q - 1) (nhds 1) (nhds 0) := by
        have := (Filter.tendsto_id (x := nhds (1 : ℝ))).sub_const 1
        simpa using this
      refine tendsto_nhdsWithin_of_tendsto_nhds_of_eventually_within _
        (hc0.mono_left nhdsWithin_le_nhds) ?_
      filter_upwards [self_mem_nhdsWithin] with q hq
      exact sub_pos.mpr (show (1 : ℝ) < q from hq)
    have h2 := h1.inv_tendsto_nhdsGT_zero
    refine Filter.tendsto_atTop_add_const_left _ 1 ?_
    simpa [one_div] using h2
  refine Filter.tendsto_atTop_mono' _ ?_ hc
  filter_upwards [self_mem_nhdsWithin] with q hq
  exact hecke_threshold_ge (show (1 : ℝ) < q from hq)

/-! ## V4 — exclusions and the helicity floor -/

/-- **V4, exact exponential decay.** If a quadratic functional `Q`
    (enstrophy, energy, ...) scales as `Q(s·u) = s²·Q(u)` and the flow is
    the exact rescaling `U(t) = e^{−νμt}·u` with `νμ ≥ 0` (the Beltrami
    eigen-solution `beltrami_eigen_ns`), then `Q(U(t)) ≤ Q(u)` for every
    `t ≥ 0`. So the supremum over time is attained at `t = 0`, and
    Beltrami eigen-data held fixed in the substrate layer are not Part A
    data. -/
theorem quadratic_decay_le_initial {V : Type*} [SMul ℝ V] (Q : V → ℝ)
    (hQ : ∀ (s : ℝ) (u : V), Q (s • u) = s ^ 2 * Q u)
    (hQnn : ∀ u, 0 ≤ Q u) (u : V) {νμ t : ℝ} (hνμ : 0 ≤ νμ) (ht : 0 ≤ t) :
    Q (Real.exp (-(νμ * t)) • u) ≤ Q u := by
  rw [hQ]
  have he : Real.exp (-(νμ * t)) ≤ 1 := by
    apply Real.exp_le_one_iff.mpr
    have : 0 ≤ νμ * t := mul_nonneg hνμ ht
    linarith
  have he0 : 0 ≤ Real.exp (-(νμ * t)) := (Real.exp_pos _).le
  have hsq : Real.exp (-(νμ * t)) ^ 2 ≤ 1 := by
    calc Real.exp (-(νμ * t)) ^ 2 ≤ 1 ^ 2 := pow_le_pow_left₀ he0 he 2
      _ = 1 := one_pow 2
  calc Real.exp (-(νμ * t)) ^ 2 * Q u ≤ 1 * Q u :=
        mul_le_mul_of_nonneg_right hsq (hQnn u)
    _ = Q u := one_mul _

/-- **V4, helicity gives a floor, not a ceiling.** On a finite set of
    modes with energies `a_k²`, wavenumbers `w_k` (e.g. `[k]_q`) and
    helical signs `s_k ∈ {±1}`, the helicity `H = Σ s_k w_k a_k²`, energy
    `E = Σ a_k²` and enstrophy `Ω = Σ w_k² a_k²` satisfy `H² ≤ E·Ω`.
    Hence `Ω ≥ H²/E`: helicity bounds the enstrophy from **below**. -/
theorem helicity_enstrophy_floor {ι : Type*} (S : Finset ι) (a w s : ι → K)
    (hs : ∀ i ∈ S, s i ^ 2 = 1) :
    (∑ i ∈ S, s i * w i * a i ^ 2) ^ 2
      ≤ (∑ i ∈ S, a i ^ 2) * (∑ i ∈ S, w i ^ 2 * a i ^ 2) := by
  have hcs := Finset.sum_mul_sq_le_sq_mul_sq S a (fun i => s i * w i * a i)
  have h1 : ∑ i ∈ S, a i * (s i * w i * a i) = ∑ i ∈ S, s i * w i * a i ^ 2 :=
    Finset.sum_congr rfl (fun i _ => by ring)
  have h2 : ∑ i ∈ S, (s i * w i * a i) ^ 2 = ∑ i ∈ S, w i ^ 2 * a i ^ 2 :=
    Finset.sum_congr rfl (fun i hi => by
      have := hs i hi
      calc (s i * w i * a i) ^ 2 = s i ^ 2 * (w i ^ 2 * a i ^ 2) := by ring
        _ = w i ^ 2 * a i ^ 2 := by rw [this, one_mul])
  rw [h1, h2] at hcs
  exact hcs

end QOU.FluidDynamics.PartAPaths
