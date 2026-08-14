import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Ring.Finset
import QOU.FluidDynamics.low_mode_block_global

/-!
# QOU.FluidDynamics.physical_layer_leray

**ε-uniform Leray control in the physical layer — the time-averaged
no-pile-up bound, proved** (bean `qou-6xv8`, epic `qou-a3n3`; the
physical-layer face of the uniformity question after Option C,
`def:qns-unit-layers`).

In the physical (`c_q`-rescaled) layer the viscosity is
`ν_phys = 1/(2q)` exactly (`qns_unit_layers`), so for `1 < q ≤ 2` it
satisfies `ν_phys ≥ 1/4` — **bounded below uniformly in `ε`**.  The
discrete Leray inequality of `low_mode_block_global` therefore yields
`ε`-uniform constants in this layer:

- `physical_leray_uniform` — `(δ/4)·∑_{i<n} Ω_phys(i) ≤ E₀` for every
  `n`, every datum, every `1 < q ≤ 2`: the cumulative physical
  enstrophy is bounded by fixed, `ε`-free constants.
- `physical_tail_leray_uniform` — the same bound for the above-band
  tail: the tail can spike at an instant, but its **time integral** is
  `ε`-uniformly bounded.  This is the *time-averaged* form of the
  physical-layer no-pile-up hypothesis, **proved**.

**What remains, honestly.**  The SF5-supported open hypothesis is the
*sup-in-time* tail bound.  Time-integrated control does not imply
sup-in-time control — that implication gap is precisely the classical
weak-vs-strong (Leray-to-regularity) gap of the fixed-`ν`
Navier–Stokes problem.  After this file, the in-QOU millennium
remainder in the physical layer has **exactly the classical shape**:
energy bound uniform (trivial), Leray/time-averaged enstrophy uniform
(this file), sup-in-time enstrophy open — no more and no less.
Nothing here closes that gap; it localizes it.

Hypothesis-carrying discrete style over a generic ordered field (§7c);
the physical-layer dissipation step and the layer conversion are the
consumer's obligations, tagged per the never-straddle rule of
`def:qns-unit-layers`.
-/

namespace QOU.FluidDynamics.PhysicalLayerLeray

open QOU.FluidDynamics.LowModeBlock

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- The physical viscosity is uniformly bounded below on the substrate
    window: `1 < q ≤ 2` gives `1/4 ≤ 1/(2q)`.  (The whole campaign
    works at `q = 1 + ε` with small `ε > 0`, so `q ≤ 2` is not a
    restriction in practice; it is stated explicitly rather than
    hidden.) -/
theorem nu_phys_lower (q : K) (hq1 : 1 < q) (hq2 : q ≤ 2) :
    (1 : K) / 4 ≤ 1 / (2 * q) := by
  have h0 : (0 : K) < q := lt_trans one_pos hq1
  rw [div_le_div_iff₀ (by norm_num : (0 : K) < 4) (by positivity)]
  linarith

/-- **ε-uniform physical-layer Leray bound**: with the physical
    dissipation step `E(n+1) ≤ E(n) − δ·(1/(2q))·Ω_phys(n)` and
    `1 < q ≤ 2`, the cumulative physical enstrophy satisfies

      `(δ/4)·∑_{i<n} Ω_phys(i) ≤ E₀`

    for every `n` — all constants independent of `ε = q − 1`.  The
    fixed-`ν` frame's a-priori control survives the classical limit. -/
theorem physical_leray_uniform (E Ωp : ℕ → K) (δ q : K)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n) :
    ∀ n, δ / 4 * ∑ i ∈ Finset.range n, Ωp i ≤ E 0 := by
  intro n
  have hbase := cumulative_enstrophy_bound E Ωp (δ * (1 / (2 * q)))
    hdiss hE n
  have hsum : 0 ≤ ∑ i ∈ Finset.range n, Ωp i :=
    Finset.sum_nonneg (fun i _ => hΩ i)
  have hcoef : δ / 4 ≤ δ * (1 / (2 * q)) := by
    have := nu_phys_lower q hq1 hq2
    calc δ / 4 = δ * (1 / 4) := by ring
      _ ≤ δ * (1 / (2 * q)) :=
        mul_le_mul_of_nonneg_left this (le_of_lt hδ)
  calc δ / 4 * ∑ i ∈ Finset.range n, Ωp i
      ≤ δ * (1 / (2 * q)) * ∑ i ∈ Finset.range n, Ωp i :=
        mul_le_mul_of_nonneg_right hcoef hsum
    _ ≤ E 0 := hbase

/-- **ε-uniform time-averaged tail bound** — the proved half of the
    physical-layer no-pile-up hypothesis: any above-band tail sequence
    (`tail ≤ Ω_phys` pointwise in time) has `ε`-uniformly bounded
    cumulative sum, `(δ/4)·∑_{i<n} tail(i) ≤ E₀`.  The tail may spike
    at instants; its time integral cannot grow with `1/ε`.  The
    sup-in-time version is the open classical weak-vs-strong gap. -/
theorem physical_tail_leray_uniform (E Ωp tail : ℕ → K) (δ q : K)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (htail : ∀ n, tail n ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n) :
    ∀ n, δ / 4 * ∑ i ∈ Finset.range n, tail i ≤ E 0 := by
  intro n
  have hmain := physical_leray_uniform E Ωp δ q hδ hq1 hq2 hΩ hdiss hE n
  have hsumle : ∑ i ∈ Finset.range n, tail i
      ≤ ∑ i ∈ Finset.range n, Ωp i :=
    Finset.sum_le_sum (fun i _ => htail i)
  calc δ / 4 * ∑ i ∈ Finset.range n, tail i
      ≤ δ / 4 * ∑ i ∈ Finset.range n, Ωp i :=
        mul_le_mul_of_nonneg_left hsumle (by positivity)
    _ ≤ E 0 := hmain

end QOU.FluidDynamics.PhysicalLayerLeray
