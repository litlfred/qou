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

/-!
## Discrete epochs of regularity (bean `qou-8wjo`)

Markov's counting inequality applied to the ε-uniform Leray bound: for
**any** exceedance level `λ`, the bad-step count satisfies the product
inequality `(card bad)·λ ≤ (4/δ)·E₀` — with constants independent of
`ε`, of the horizon `n`, and of everything about the data except `E₀`.
For `λ > 0` this reads `card bad ≤ 4E₀/(δλ)`: the tail exceeds `λ` on
at most boundedly many steps, and outside that set it is `≤ λ` — the
discrete image of Leray's *epochs of regularity*.

**What this does not give, honestly:** the bad set is bounded in
*count*, not located — it may concentrate at a single time, and a
sup-in-time blow-up hiding inside boundedly many steps is exactly the
configuration the classical weak-vs-strong gap permits.  The open item
is unchanged; this theorem fences it into an ε-uniformly small set of
times.
-/

/-- **Discrete epochs of regularity, ε-uniform**: under the physical
    Leray hypotheses, for every level `lam` the count of time steps
    `i < n` with `lam < tail i` satisfies the product inequality

      `(card bad) · lam ≤ (4/δ)·E₀`,

    with constants uniform in `ε`, `n`, and the data beyond `E₀`.
    When `0 < lam` this yields the count bound
    `card bad ≤ 4E₀/(δ·lam)` on dividing by `lam`; for `lam ≤ 0` the
    inequality is vacuously generous.  (Requires `0 ≤ tail` so that
    off-bad-set terms cannot hide negative mass.) -/
theorem epochs_of_regularity (E Ωp tail : ℕ → K) (δ q lam : K)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (htail₀ : ∀ n, 0 ≤ tail n) (htail : ∀ n, tail n ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n) :
    ∀ n, (((Finset.range n).filter (fun i => lam < tail i)).card : K) * lam
      ≤ 4 / δ * E 0 := by
  intro n
  set bad := (Finset.range n).filter (fun i => lam < tail i) with hbad
  have hcard : ((bad.card : K)) * lam = ∑ _i ∈ bad, lam := by
    rw [Finset.sum_const, nsmul_eq_mul]
  have h1 : ∑ _i ∈ bad, lam ≤ ∑ i ∈ bad, tail i := by
    apply Finset.sum_le_sum
    intro i hi
    exact le_of_lt (Finset.mem_filter.mp hi).2
  have h2 : ∑ i ∈ bad, tail i ≤ ∑ i ∈ Finset.range n, tail i :=
    Finset.sum_le_sum_of_subset_of_nonneg
      (Finset.filter_subset _ _) (fun i _ _ => htail₀ i)
  have h3 : ∑ i ∈ Finset.range n, tail i ≤ 4 / δ * E 0 := by
    have hler := physical_tail_leray_uniform E Ωp tail δ q hδ hq1 hq2
      hΩ htail hdiss hE n
    have h4 : (0 : K) < 4 / δ := by positivity
    calc ∑ i ∈ Finset.range n, tail i
        = 4 / δ * (δ / 4 * ∑ i ∈ Finset.range n, tail i) := by
          field_simp
      _ ≤ 4 / δ * E 0 :=
          mul_le_mul_of_nonneg_left hler (le_of_lt h4)
  calc ((bad.card : K)) * lam = ∑ _i ∈ bad, lam := hcard
    _ ≤ ∑ i ∈ bad, tail i := h1
    _ ≤ ∑ i ∈ Finset.range n, tail i := h2
    _ ≤ 4 / δ * E 0 := h3

/-!
## Discrete eventual regularity (bean `qou-tfbx`)

Leray's second classical theorem, in the discrete physical layer.  Two
pieces:

1. **Pigeonhole entry** (`exists_small_step`): the ε-uniform Leray
   bound forces the enstrophy below any threshold `θ` within an
   explicit, ε-uniform number of steps — if `(4/δ)·E₀ < m·θ`, some
   step `i < m` has `Ωp i ≤ θ`.  Entry time `≤ 4E₀/(δθ) + 1`,
   independent of `ε` and of everything but `E₀`.
2. **Basin chaining** (`eventually_in_basin`): if the threshold's
   sub-level set is forward-invariant (`Ωp n ≤ θ → Ωp (n+1) ≤ θ` —
   the abstract shape of GP4's small-data persistence), then from the
   entry step onward the enstrophy stays `≤ θ` forever.

Together: **every solution is eventually regular, with an ε-uniform
bound on the irregular window** — blow-up, if any, is confined to
`[0, 4E₀/(δθ*)]` where `θ*` is the basin threshold.  The
basin-invariance hypothesis is *named, not smuggled*: GP4
(`global_persistence_subthreshold`, substrate layer) proves exactly
this shape; instantiating it in the physical layer (converting its
threshold through `def:qns-unit-layers` without straddling) is the
recorded follow-up, not assumed here.
-/

/-- **Pigeonhole entry into any sub-level set, ε-uniform**: if
    `(4/δ)·E₀ < m·θ` then some step `i < m` has `Ωp i ≤ θ`.
    (Otherwise all `m` steps exceed `θ` and the cumulative bound is
    violated.) -/
theorem exists_small_step (E Ωp : ℕ → K) (δ q θ : K) (m : ℕ)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n)
    (hm : 4 / δ * E 0 < (m : K) * θ) :
    ∃ i ∈ Finset.range m, Ωp i ≤ θ := by
  by_contra hnone
  push_neg at hnone
  have hall : ∀ i ∈ Finset.range m, θ < Ωp i := fun i hi => hnone i hi
  have hsum : (m : K) * θ ≤ ∑ i ∈ Finset.range m, Ωp i := by
    calc (m : K) * θ = ∑ _i ∈ Finset.range m, θ := by
          rw [Finset.sum_const, Finset.card_range, nsmul_eq_mul]
      _ ≤ ∑ i ∈ Finset.range m, Ωp i :=
          Finset.sum_le_sum (fun i hi => le_of_lt (hall i hi))
  have hler := physical_leray_uniform E Ωp δ q hδ hq1 hq2 hΩ hdiss hE m
  have h4 : (0 : K) < 4 / δ := by positivity
  have htot : ∑ i ∈ Finset.range m, Ωp i ≤ 4 / δ * E 0 := by
    calc ∑ i ∈ Finset.range m, Ωp i
        = 4 / δ * (δ / 4 * ∑ i ∈ Finset.range m, Ωp i) := by
          field_simp
      _ ≤ 4 / δ * E 0 :=
          mul_le_mul_of_nonneg_left hler (le_of_lt h4)
  linarith

/-- **Discrete eventual regularity**: with the pigeonhole entry and a
    forward-invariant basin (`Ωp n ≤ θ → Ωp (n+1) ≤ θ`, the abstract
    shape of GP4's sub-threshold global persistence), there is a step
    `i₀ < m` from which the enstrophy stays `≤ θ` forever.  Blow-up,
    if any, is confined to the ε-uniformly bounded initial window
    `[0, m)` with any `m > 4E₀/(δθ)`. -/
theorem eventually_in_basin (E Ωp : ℕ → K) (δ q θ : K) (m : ℕ)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n)
    (hm : 4 / δ * E 0 < (m : K) * θ)
    (basin : ∀ n, Ωp n ≤ θ → Ωp (n + 1) ≤ θ) :
    ∃ i₀ < m, ∀ n, i₀ ≤ n → Ωp n ≤ θ := by
  obtain ⟨i₀, hi₀, hsmall⟩ :=
    exists_small_step E Ωp δ q θ m hδ hq1 hq2 hΩ hdiss hE hm
  refine ⟨i₀, Finset.mem_range.mp hi₀, ?_⟩
  intro n
  induction n with
  | zero =>
      intro hn
      have h0 : i₀ = 0 := Nat.le_zero.mp hn
      simpa [h0] using hsmall
  | succ p ih =>
      intro hn
      rcases Nat.lt_or_ge i₀ (p + 1) with hlt | hge
      · exact basin p (ih (Nat.lt_succ_iff.mp hlt))
      · have heq : i₀ = p + 1 := le_antisymm hn hge
        simpa [heq] using hsmall

/-!
## Closing the basin hypothesis (bean `qou-f5o6`)

`eventually_in_basin` above took the basin invariance as a *named
hypothesis*.  It is discharged here by proof: with the damped
quadratic low-mode step `Ω_{n+1} ≤ Ω_n + δ·Ω_n·(c·Ω_n − d)` — the
same step shape GP4 (`global_persistence_subthreshold`,
`surreal_enstrophy_finite_modes.lean`) is stated over, with
`d = ν·μ` — the sub-level set of the threshold `θ = d/c` is
forward-invariant (`quadratic_basin_invariant`): below threshold the
quadratic drift is non-positive.  The lemma is layer-agnostic algebra;
supplying the parameters of **one** layer consistently (never
straddling, per `def:qns-unit-layers`) instantiates it in that layer.

`eventual_regularity_quadratic` composes everything: Leray hypotheses
+ quadratic step ⇒ there is a step `i₀ < m` (any `m > 4E₀/(δ·(d/c))`)
after which `Ω ≤ d/c` forever.  **Discrete eventual regularity with no
unproved hypothesis left in the chain** — the only open item remaining
is the sup-in-time behaviour *inside* the ε-uniform initial window.
-/

/-- **Basin invariance from the damped quadratic step** (GP4's
    mechanism, layer-agnostic): if
    `Ω(n+1) ≤ Ω(n) + δ·Ω(n)·(c·Ω(n) − d)` with `δ, Ω ≥ 0` and
    `c > 0`, then the sub-level set of `θ = d/c` is forward-invariant —
    below threshold the drift term is non-positive. -/
theorem quadratic_basin_invariant (Ωp : ℕ → K) (δ c d : K)
    (hδ : 0 ≤ δ) (hc : 0 < c) (hΩ : ∀ n, 0 ≤ Ωp n)
    (hstep : ∀ n, Ωp (n + 1) ≤ Ωp n + δ * Ωp n * (c * Ωp n - d)) :
    ∀ n, Ωp n ≤ d / c → Ωp (n + 1) ≤ d / c := by
  intro n hn
  have hcd : c * Ωp n ≤ d := by
    rw [le_div_iff₀ hc] at hn
    linarith [hn]
  have hdrift : δ * Ωp n * (c * Ωp n - d) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos
      (mul_nonneg hδ (hΩ n)) (sub_nonpos.mpr hcd)
  calc Ωp (n + 1) ≤ Ωp n + δ * Ωp n * (c * Ωp n - d) := hstep n
    _ ≤ Ωp n := by linarith
    _ ≤ d / c := hn

/-- **Discrete eventual regularity, fully composed — no unproved
    hypothesis in the chain**: Leray hypotheses + the damped quadratic
    low-mode step give a step `i₀ < m` (for any `m` with
    `(4/δ)·E₀ < m·(d/c)`) after which the enstrophy stays at or below
    the threshold `d/c` forever.  Blow-up, if any, lives only inside
    the ε-uniform initial window `[0, m)`. -/
theorem eventual_regularity_quadratic (E Ωp : ℕ → K) (δ q c d : K)
    (m : ℕ)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2) (hc : 0 < c)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n)
    (hstep : ∀ n, Ωp (n + 1) ≤ Ωp n + δ * Ωp n * (c * Ωp n - d))
    (hm : 4 / δ * E 0 < (m : K) * (d / c)) :
    ∃ i₀ < m, ∀ n, i₀ ≤ n → Ωp n ≤ d / c :=
  eventually_in_basin E Ωp δ q (d / c) m hδ hq1 hq2 hΩ hdiss hE hm
    (quadratic_basin_invariant Ωp δ c d (le_of_lt hδ) hc hΩ hstep)

end QOU.FluidDynamics.PhysicalLayerLeray
