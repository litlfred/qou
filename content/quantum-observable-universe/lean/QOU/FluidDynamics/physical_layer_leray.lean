import Mathlib.Tactic
import Mathlib.Algebra.BigOperators.Ring.Finset
import QOU.FluidDynamics.low_mode_block_global
import QOU.FluidDynamics.surreal_enstrophy_finite_modes

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

/-!
## Inside the initial window: good-step chaining (bean `qou-g1kj`)

The one place blow-up could still live is the ε-uniform initial window.
This section closes it for a **larger data class than GP4's basin** by
combining the two uniform controls already proved:

- **epochs** bound the *total* number of bad steps (`Ω > lam`) by an
  ε-free count `Nbad`;
- the **bootstrap** (GP3's shape: from any good step, `Ω ≤ 2·lam` for
  the next `H` steps — taken as a named hypothesis here, exactly as
  the basin was before `qou-f5o6`) covers `H` steps after each good
  step.

If every bad run is shorter than the bootstrap horizon
(`Nbad + 1 ≤ H`), the good steps chain: the *latest* good step before
any time `n` is at most `Nbad` steps back (else the interval in
between would contain more bad steps than exist in total), so the
bootstrap from it covers `n` — and `Ω ≤ 2·lam` **everywhere**
(`sup_bound_of_chaining`).  No induction is needed; the latest-good-
step argument is a single pigeonhole.

Reading of the arithmetic side condition (docstring only, not
formalized): with `Nbad ≈ 4E₀/(δ·lam)` and `H ≈ 1/(2δc·lam)` the
condition `Nbad + 1 ≤ H` is `8cE₀ ≲ 1` — an **energy**-smallness
condition, ε-uniform, strictly weaker than GP4's enstrophy-smallness
`c·Ω₀ ≤ νμ`.  In-model, scope (a): the model's transfer constant `c`
is fixed, whereas the classical supercriticality lives exactly in `c`
growing with resolution — that distinction is the honest boundary of
this result, stated, not blurred.  Large data with `8cE₀ > 1` remains
the open core.
-/

/-- Convert the epochs product inequality into a natural-number bad
    count: if `(4/δ)·E₀ ≤ Nbad·lam` (with `lam > 0`), then at most
    `Nbad` steps of any horizon are bad. -/
theorem bad_count_le (E Ωp tail : ℕ → K) (δ q lam : K) (Nbad : ℕ)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2) (hlam : 0 < lam)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (htail₀ : ∀ n, 0 ≤ tail n) (htail : ∀ n, tail n ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n)
    (hcast : 4 / δ * E 0 ≤ (Nbad : K) * lam) :
    ∀ n, ((Finset.range n).filter (fun i => lam < tail i)).card ≤ Nbad := by
  intro n
  have hprod := epochs_of_regularity E Ωp tail δ q lam hδ hq1 hq2
    hΩ htail₀ htail hdiss hE n
  have hK : ((((Finset.range n).filter (fun i => lam < tail i)).card : K))
      ≤ (Nbad : K) := by
    have := le_trans hprod hcast
    exact le_of_mul_le_mul_right this hlam
  exact_mod_cast hK

omit [IsStrictOrderedRing K] in
/-- **Sup bound by good-step chaining**: if at most `Nbad` steps in any
    horizon are bad (`lam < Ωp`), the origin is good (`Ωp 0 ≤ lam`),
    the bootstrap covers `H` steps from every good step
    (`Ωp g ≤ lam → Ωp (g + j) ≤ 2·lam` for `j ≤ H`), and every bad run
    fits under the horizon (`Nbad + 1 ≤ H`), then `Ωp n ≤ 2·lam` for
    **every** `n`.  Latest-good-step pigeonhole: the newest good step
    `g ≤ n` is at most `Nbad` back, since the strictly-later steps up
    to `n` are all bad and there are at most `Nbad` of those in total;
    the bootstrap from `g` then covers `n`. -/
theorem sup_bound_of_chaining (Ωp : ℕ → K) (lam : K) (Nbad H : ℕ)
    (hcount : ∀ n, ((Finset.range n).filter (fun i => lam < Ωp i)).card ≤ Nbad)
    (h0 : Ωp 0 ≤ lam)
    (hboot : ∀ g, Ωp g ≤ lam → ∀ j, j ≤ H → Ωp (g + j) ≤ 2 * lam)
    (hHN : Nbad + 1 ≤ H) :
    ∀ n, Ωp n ≤ 2 * lam := by
  intro n
  set S := (Finset.range (n + 1)).filter (fun i => Ωp i ≤ lam) with hS
  have hne : S.Nonempty := by
    refine ⟨0, ?_⟩
    simp [hS, h0]
  set g := S.max' hne with hg
  have hgmem := S.max'_mem hne
  have hgle : g ≤ n := by
    have := (Finset.mem_filter.mp hgmem).1
    exact Nat.lt_succ_iff.mp (Finset.mem_range.mp this)
  have hggood : Ωp g ≤ lam := (Finset.mem_filter.mp hgmem).2
  -- every step strictly between g and n (inclusive) is bad
  have hbad : ∀ i, g < i → i ≤ n → lam < Ωp i := by
    intro i hgi hin
    by_contra hnot
    push_neg at hnot
    have himem : i ∈ S := by
      refine Finset.mem_filter.mpr ⟨Finset.mem_range.mpr ?_, hnot⟩
      exact Nat.lt_succ_of_le hin
    exact absurd (S.le_max' i himem) (not_le.mpr hgi)
  -- so the run (g, n] injects into the bad set of range (n+1)
  have hrun : n - g ≤ Nbad := by
    have hsub : Finset.Ico (g + 1) (n + 1)
        ⊆ (Finset.range (n + 1)).filter (fun i => lam < Ωp i) := by
      intro i hi
      obtain ⟨h1, h2⟩ := Finset.mem_Ico.mp hi
      exact Finset.mem_filter.mpr
        ⟨Finset.mem_range.mpr h2,
         hbad i (Nat.lt_of_succ_le h1) (Nat.lt_succ_iff.mp h2)⟩
    have hcardIco : (Finset.Ico (g + 1) (n + 1)).card = n - g := by
      rw [Nat.card_Ico]
      omega
    calc n - g = (Finset.Ico (g + 1) (n + 1)).card := hcardIco.symm
      _ ≤ ((Finset.range (n + 1)).filter (fun i => lam < Ωp i)).card :=
          Finset.card_le_card hsub
      _ ≤ Nbad := hcount (n + 1)
  -- the bootstrap from g covers n
  have hn : n = g + (n - g) := by omega
  rw [hn]
  exact hboot g hggood (n - g) (le_trans hrun (by omega))

/-!
## Wiring GP3 into the chain (bean `qou-c637`)

The chaining theorem above took the bootstrap as the named hypothesis
`hboot`.  It is discharged here from GP3's actual statement
(`local_bootstrap`, `surreal_enstrophy_finite_modes.lean`): applying
GP3 to the sequence *shifted to start at each good step* — the shifted
sequence inherits the quadratic step — gives
`Ωp (g+j) ≤ 2·Ωp g ≤ 2·lam` for `j ≤ H`, provided the horizon
condition `H·δc·lam ≤ 1/4` holds at the level `lam`
(`hboot_of_local_bootstrap`).  The damped step of the basin section
implies GP3's undamped step (`d ≥ 0` drops the damping term), so one
step hypothesis serves the whole file
(`quadratic_step_of_damped`).

`energy_small_global` is the full composition — Leray + damped
quadratic step + the two arithmetic side conditions ⇒
`Ωp n ≤ 2·lam` for **all** `n`.  Every link in the chain is now a
theorem; the only assumptions left are the model step inequalities
themselves (the discrete dynamics) and the arithmetic smallness
`Nbad + 1 ≤ H` (≈ `8cE₀ ≲ 1`, the energy-smallness reading).
-/

/-- The damped quadratic step implies GP3's undamped step: for
    `d, Ω ≥ 0`, `δ·Ω·(c·Ω − d) ≤ δ·c·Ω²`. -/
theorem quadratic_step_of_damped (Ωp : ℕ → K) (δ c d : K)
    (hδ : 0 ≤ δ) (hd : 0 ≤ d) (hΩ : ∀ n, 0 ≤ Ωp n)
    (hstep : ∀ n, Ωp (n + 1) ≤ Ωp n + δ * Ωp n * (c * Ωp n - d)) :
    ∀ n, Ωp (n + 1) ≤ Ωp n + δ * c * (Ωp n) ^ 2 := by
  intro n
  have h := hstep n
  nlinarith [mul_nonneg hδ (hΩ n), mul_nonneg (mul_nonneg hδ (hΩ n)) hd]

/-- **`hboot` discharged from GP3**: applying `local_bootstrap` to the
    sequence shifted to start at a good step `g` (the shift inherits
    the quadratic step) gives the bootstrap cover
    `Ωp (g+j) ≤ 2·lam` for `j ≤ H`, under the horizon condition
    `H·(δc·lam) ≤ 1/4`. -/
theorem hboot_of_local_bootstrap (Ωp : ℕ → K) (δ c lam : K) (H : ℕ)
    (hδ : 0 ≤ δ) (hc : 0 ≤ c)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (hqstep : ∀ n, Ωp (n + 1) ≤ Ωp n + δ * c * (Ωp n) ^ 2)
    (hhor : (H : K) * (δ * c * lam) ≤ 1 / 4) :
    ∀ g, Ωp g ≤ lam → ∀ j, j ≤ H → Ωp (g + j) ≤ 2 * lam := by
  intro g hg j hj
  have hδc : (0 : K) ≤ δ * c := mul_nonneg hδ hc
  have hHnn : (0 : K) ≤ (H : K) := Nat.cast_nonneg H
  have hh : (H : K) * (δ * c * Ωp g) ≤ 1 / 4 := by
    have h1 : (H : K) * (δ * c * Ωp g) ≤ (H : K) * (δ * c * lam) := by
      apply mul_le_mul_of_nonneg_left _ hHnn
      exact mul_le_mul_of_nonneg_left hg hδc
    linarith
  have hshift := QOU.FluidDynamics.local_bootstrap hδ hc
    (fun i => Ωp (g + i)) (fun i => hΩ (g + i))
    (fun i => by
      show Ωp (g + (i + 1)) ≤ Ωp (g + i) + δ * c * (Ωp (g + i)) ^ 2
      rw [Nat.add_succ]
      exact hqstep (g + i)) H
    (by
      show (H : K) * (δ * c * Ωp (g + 0)) ≤ 1 / 4
      simpa using hh)
  have h2 : Ωp (g + j) ≤ 2 * Ωp g := by simpa using hshift j hj
  linarith

/-- **Energy-small global regularity, fully composed — every link a
    theorem.**  Hypotheses: the physical Leray dissipation step, the
    damped quadratic low-mode step, good data (`Ωp 0 ≤ lam`), and the
    two arithmetic side conditions (`4E₀/δ ≤ Nbad·lam`, the bootstrap
    horizon `H·δc·lam ≤ 1/4`, and the gap condition `Nbad + 1 ≤ H` —
    jointly the `8cE₀ ≲ 1` energy-smallness reading).  Conclusion:
    `Ωp n ≤ 2·lam` for **every** `n`, uniformly in `ε`.  The only
    assumptions are the model's discrete dynamics and the smallness
    arithmetic; no bootstrap, basin, or counting hypothesis remains
    undischarged. -/
theorem energy_small_global (E Ωp : ℕ → K) (δ q c d lam : K)
    (Nbad H : ℕ)
    (hδ : 0 < δ) (hq1 : 1 < q) (hq2 : q ≤ 2) (hc : 0 ≤ c)
    (hd : 0 ≤ d) (hlam : 0 < lam)
    (hΩ : ∀ n, 0 ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δ * (1 / (2 * q)) * Ωp n)
    (hE : ∀ n, 0 ≤ E n)
    (hstep : ∀ n, Ωp (n + 1) ≤ Ωp n + δ * Ωp n * (c * Ωp n - d))
    (h0 : Ωp 0 ≤ lam)
    (hcast : 4 / δ * E 0 ≤ (Nbad : K) * lam)
    (hhor : (H : K) * (δ * c * lam) ≤ 1 / 4)
    (hHN : Nbad + 1 ≤ H) :
    ∀ n, Ωp n ≤ 2 * lam := by
  have hqstep := quadratic_step_of_damped Ωp δ c d (le_of_lt hδ) hd hΩ hstep
  have hcount := bad_count_le E Ωp Ωp δ q lam Nbad hδ hq1 hq2 hlam hΩ
    hΩ (fun n => le_refl _) hdiss hE hcast
  have hboot := hboot_of_local_bootstrap Ωp δ c lam H (le_of_lt hδ) hc
    hΩ hqstep hhor
  exact sup_bound_of_chaining Ωp lam Nbad H hcount h0 hboot hHN

/-!
## The energy-drain route and the infrared localization (bean `qou-qy5l`)

For large data (`8cE₀ > 1`) one natural route remains: energy is not
merely monotone — it *drains* at a rate proportional to the enstrophy,
and the discrete Poincaré bound `k²ₘᵢₙ·E ≤ Ω` (the lowest rung
dominates: `Ω = Σk²e ≥ k²ₘᵢₙ·Σe`) turns the drain into **geometric
decay** (`energy_geometric_decay`): `E_n ≤ (1 − δν·k²ₘᵢₙ)ⁿ·E₀`.
Wait long enough and any datum enters the energy-small class, where
`energy_small_global` takes over.

**The honest scaling — and why this does NOT close the core.**  The
decay rate is `δν·k²ₘᵢₙ`, and in the physical layer the lowest
wavenumber is `k_phys,1 = (q−1)·[1]_q = ε` (`def:qns-unit-layers`):
the spectral gap **vanishes in the continuum limit**, so the decay
rate is `~ δε²/4` — `ε`-NON-uniform, and the entry time into the
small-energy class diverges as `q → 1⁺`.  This is the correct
discrete image of the classical situation (no Poincaré inequality on
an unbounded domain; the physical-layer domain grows like `c_q`).

**Localization achieved:** the ultraviolet side of the uniformity
question was tamed (tail Leray, epochs, chaining — all `ε`-uniform);
the energy-drain route shows the surviving large-data obstruction is
**infrared** — the vanishing spectral gap of the continuum limit.
The open core of epic `qou-a3n3`, sharpest form: *large data,
`ε`-uniformly in time, against a spectral gap that closes like `ε`.*
Nothing here resolves it; the theorem quantifies exactly where it
lives.
-/

/-- **Geometric energy decay from the discrete Poincaré bound**: with
    the dissipation step `E(n+1) ≤ E(n) − δν·Ω(n)`, the spectral-gap
    bound `g·E(n) ≤ Ω(n)` (with `g = k²ₘᵢₙ`), nonnegative energy, and
    the step-size sanity `0 ≤ δν·g ≤ 1`, the energy decays
    geometrically: `E_n ≤ (1 − δν·g)ⁿ·E₀`.  The rate `δν·g` carries
    the `ε`-non-uniformity of the physical-layer infrared gap
    (`g = ε²`); see the section docstring. -/
theorem energy_geometric_decay (E Ωp : ℕ → K) (δν g : K)
    (hδν : 0 ≤ δν)
    (hr : δν * g ≤ 1)
    (hgap : ∀ n, g * E n ≤ Ωp n)
    (hdiss : ∀ n, E (n + 1) ≤ E n - δν * Ωp n) :
    ∀ n, E n ≤ (1 - δν * g) ^ n * E 0 := by
  intro n
  induction n with
  | zero => simp
  | succ p ih =>
      have hstep : E (p + 1) ≤ (1 - δν * g) * E p := by
        have h1 := hdiss p
        have h2 : δν * (g * E p) ≤ δν * Ωp p :=
          mul_le_mul_of_nonneg_left (hgap p) hδν
        nlinarith [h1, h2]
      have hfac : (0 : K) ≤ 1 - δν * g := by linarith
      calc E (p + 1) ≤ (1 - δν * g) * E p := hstep
        _ ≤ (1 - δν * g) * ((1 - δν * g) ^ p * E 0) :=
            mul_le_mul_of_nonneg_left ih hfac
        _ = (1 - δν * g) ^ (p + 1) * E 0 := by ring

/-!
## The damped-forced tail bound (bean `qou-80p8`)

The synthesis of the whole arc.  Seen from above the fixed band, the
tail is a **strongly damped system forced through a fixed boundary**:

- every tail mode has `k ≥ kB`, so the tail's own dissipation rate is
  `ν·kB²` — **`ε`-free**, because the band is fixed;
- the only input crosses the band boundary, where the banded bound
  (`banded_enstrophy_le`, `ε`-uniform) controls the amplitudes.

If the boundary flux is bounded by a uniform `Φ` — the **one named
hypothesis** — then the standard damped-forced invariant
(`tail_damped_forced_bound`) gives

  `Ω_tail(n) ≤ max(Ω_tail(0), Φ/(ν·kB²))`  for **every** `n`,

**all data, `ε`-uniform**: the sup-in-time tail bound that has been
the open item since the uniformity reduction — closed in-model,
conditional on `Φ`.

**Status of the flux hypothesis, honestly.**  In the shell models the
transfer is local in `k` by construction, and the boundary flux is a
function of amplitudes at rungs `~B` — controlled by the `ε`-uniform
band bound; deriving the explicit `Φ` from the band bound is
model-specific algebra recorded as the follow-up, not assumed done.
For full NS the flux across a wavenumber shell has a **nonlocal**
component — this is *the same* fidelity caveat the SF arc named
(nonlocal-in-`k` transfer), now carrying the entire remaining
uncertainty of the large-data question.  One hypothesis, one caveat,
in one place.
-/

/-- **The damped-forced invariant**: if the tail obeys
    `Ωt(n+1) ≤ Ωt(n) + δ·(Φ − D·Ωt(n))` (uniform input `Φ`, damping
    rate `D`), with `0 ≤ δD ≤ 1`, `Φ ≥ 0`, `D > 0`, then

      `Ωt(n) ≤ max(Ωt(0), Φ/D)`  for every `n`.

    Below the equilibrium `Φ/D` the state may rise but never past the
    equilibrium; above it the drift is downward.  All constants are
    those of the fixed band — `ε` does not appear. -/
theorem tail_damped_forced_bound (Ωt : ℕ → K) (δ Φ D : K)
    (hδ : 0 ≤ δ) (hD : 0 < D) (hδD : δ * D ≤ 1)
    (hstep : ∀ n, Ωt (n + 1) ≤ Ωt n + δ * (Φ - D * Ωt n)) :
    ∀ n, Ωt n ≤ max (Ωt 0) (Φ / D) := by
  intro n
  induction n with
  | zero => exact le_max_left _ _
  | succ p ih =>
      rcases le_or_gt (Ωt p) (Φ / D) with hlow | hhigh
      · -- below equilibrium: the step cannot overshoot `Φ/D`
        have key : Ωt (p + 1) ≤ Φ / D := by
          have h1 := hstep p
          have hDp : D * Ωt p ≤ D * (Φ / D) :=
            mul_le_mul_of_nonneg_left hlow (le_of_lt hD)
          have hDeq : D * (Φ / D) = Φ := by field_simp
          -- Ωt(p+1) ≤ (1 − δD)·Ωt p + δΦ ≤ (1 − δD)·(Φ/D) + δΦ = Φ/D
          have hfac : (0 : K) ≤ 1 - δ * D := by linarith
          have h2 : Ωt p + δ * (Φ - D * Ωt p)
              = (1 - δ * D) * Ωt p + δ * Φ := by ring
          have h3 : (1 - δ * D) * Ωt p ≤ (1 - δ * D) * (Φ / D) :=
            mul_le_mul_of_nonneg_left hlow hfac
          have h4 : (1 - δ * D) * (Φ / D) + δ * Φ = Φ / D := by
            field_simp
            ring
          linarith [h1, h3]
        exact le_trans key (le_max_right _ _)
      · -- above equilibrium: the drift is downward
        have key : Ωt (p + 1) ≤ Ωt p := by
          have h1 := hstep p
          have hneg : Φ - D * Ωt p ≤ 0 := by
            have : Φ / D < Ωt p := hhigh
            have hmul : Φ / D * D < Ωt p * D :=
              mul_lt_mul_of_pos_right this hD
            have heq : Φ / D * D = Φ := by field_simp
            nlinarith
          have : δ * (Φ - D * Ωt p) ≤ 0 :=
            mul_nonpos_of_nonneg_of_nonpos hδ hneg
          linarith
        exact le_trans key ih

/-!
## The in-model flux derivation (bean `qou-w9ja`)

`tail_damped_forced_bound` took a *constant* flux bound `Φ`.  The
honest in-model flux is not constant: the DN boundary coupling injects
`~ k_{B+1}·u_B²·u_{B+1}` — proportional to the **first tail
amplitude** `a(n) := u_{B+1}(n)`, with a coefficient `F` controlled by
the `ε`-uniform band bound (`u_B²` lives in the fixed band).  The
amplitude itself is tail-controlled: `kB²·a² ≤ Ω_tail`.

The absorption (`sqrt_forced_to_damped_forced`) is pure algebra — AM-GM
on squares, no square roots, so the file stays over a generic ordered
field: `F·a ≤ F²/(2·D·kB²) + (D/2)·Ω_t` (from `0 ≤ (F − D·kB²·a)²`
after the tail bound on `a²`), which folds the amplitude-proportional
forcing into half the damping.  The composed
`boundary_flux_tail_bound` then applies the damped-forced invariant
with `Φ = F²/(2DkB²)`, `D_eff = D/2`, giving

  `Ω_tail(n) ≤ max(Ω_tail(0), F²/(D²·kB²))`  for every `n`,

all data, `ε`-uniform.  **The constant-`Φ` hypothesis is discharged in
favour of the amplitude-form step** — which is the DN boundary
structure itself.

**Remainder, honestly:** (a) that the amplitude-form step *is* the DN
tail evolution (a model-specific inequality — probe-able, recorded as
the follow-up); (b) full-NS transfer nonlocality (the standing
fidelity caveat).  Nothing else.
-/

/-- **Absorption of amplitude-proportional forcing** (AM-GM, no square
    roots): if the tail obeys the amplitude-forced step
    `Ωt(n+1) ≤ Ωt(n) + δ·(F·a(n) − D·Ωt(n))` with the tail controlling
    its own boundary amplitude (`kB2·a(n)² ≤ Ωt(n)`), then it obeys
    the constant-forced step with `Φ = F²/(2·D·kB2)` and damping
    `D/2`. -/
theorem sqrt_forced_to_damped_forced (Ωt a : ℕ → K) (δ F D kB2 : K)
    (hδ : 0 ≤ δ) (hD : 0 < D) (hkB : 0 < kB2)
    (hamp : ∀ n, kB2 * (a n) ^ 2 ≤ Ωt n)
    (hstep : ∀ n, Ωt (n + 1) ≤ Ωt n + δ * (F * a n - D * Ωt n)) :
    ∀ n, Ωt (n + 1) ≤ Ωt n + δ * (F ^ 2 / (2 * D * kB2) - D / 2 * Ωt n) := by
  intro n
  have h1 := hstep n
  -- AM-GM with weight `m = D·kB2`:  F·a ≤ F²/(2m) + (m/2)·a²
  have hm : (0 : K) < D * kB2 := mul_pos hD hkB
  have hamgm : F * a n ≤ F ^ 2 / (2 * (D * kB2)) + D * kB2 / 2 * (a n) ^ 2 := by
    rw [div_add' _ _ _ (by positivity : (2 : K) * (D * kB2) ≠ 0)]
    rw [le_div_iff₀ (by positivity : (0 : K) < 2 * (D * kB2))]
    nlinarith [sq_nonneg (F - D * kB2 * a n)]
  -- fold the `a²` term into half the damping via the tail bound
  have habs : D * kB2 / 2 * (a n) ^ 2 ≤ D / 2 * Ωt n := by
    have h2 : D / 2 * (kB2 * (a n) ^ 2) ≤ D / 2 * Ωt n :=
      mul_le_mul_of_nonneg_left (hamp n) (by positivity)
    calc D * kB2 / 2 * (a n) ^ 2 = D / 2 * (kB2 * (a n) ^ 2) := by ring
      _ ≤ D / 2 * Ωt n := h2
  have hforce : F * a n ≤ F ^ 2 / (2 * D * kB2) + D / 2 * Ωt n := by
    have : F ^ 2 / (2 * (D * kB2)) = F ^ 2 / (2 * D * kB2) := by
      ring_nf
    linarith [hamgm, habs, this.symm.le, this.le]
  have hmul : δ * (F * a n - D * Ωt n)
      ≤ δ * (F ^ 2 / (2 * D * kB2) - D / 2 * Ωt n) := by
    apply mul_le_mul_of_nonneg_left _ hδ
    linarith
  linarith

/-- **The boundary-flux tail bound, in-model form**: with the
    amplitude-forced step (the DN boundary structure) and the tail's
    own control of its boundary amplitude, the sup-in-time tail bound
    holds for all data with the explicit `ε`-uniform equilibrium
    `F²/(D²·kB2)`:

      `Ω_tail(n) ≤ max(Ω_tail(0), F²/(D²·kB2))`.

    (Composition of the absorption with `tail_damped_forced_bound` at
    `Φ = F²/(2DkB2)`, damping `D/2`; the equilibrium is
    `Φ/(D/2) = F²/(D²kB2)`.) -/
theorem boundary_flux_tail_bound (Ωt a : ℕ → K) (δ F D kB2 : K)
    (hδ : 0 ≤ δ) (hD : 0 < D) (hkB : 0 < kB2)
    (hδD : δ * (D / 2) ≤ 1)
    (hamp : ∀ n, kB2 * (a n) ^ 2 ≤ Ωt n)
    (hstep : ∀ n, Ωt (n + 1) ≤ Ωt n + δ * (F * a n - D * Ωt n)) :
    ∀ n, Ωt n ≤ max (Ωt 0) (F ^ 2 / (D ^ 2 * kB2)) := by
  have habs := sqrt_forced_to_damped_forced Ωt a δ F D kB2 hδ hD hkB
    hamp hstep
  have hbound := tail_damped_forced_bound Ωt δ (F ^ 2 / (2 * D * kB2))
    (D / 2) hδ (by positivity) hδD habs
  have heq : F ^ 2 / (2 * D * kB2) / (D / 2) = F ^ 2 / (D ^ 2 * kB2) := by
    field_simp
  intro n
  have := hbound n
  rwa [heq] at this

/-!
## The amplitude repair (bean `qou-2y1i`)

SF6 (`qns-amplitude-step-probe`, PR #5063) refuted the *enstrophy*-form
step for small `ε`: the tail's aggregated interior transfer is not
sign-definite.  The repair is to change variables, not to weaken the
claim: **per amplitude**, the DN inflow into rung `n` comes *only from
below* (`k_n·u_{n-1}²`), and the interior outflow term
(`−k_{n+1}·u_n·u_{n+1}`) is **non-positive** for nonnegative
amplitudes — the sign-indefiniteness SF6 measured lives entirely in the
enstrophy aggregation.  Each tail rung is therefore a *scalar*
damped-forced system, and the already-proved invariant applies rung by
rung:

- `rung_equilibrium` — a rung starting empty and forced by the rung
  below stays at or under the equilibrium `P²/(ν·kn)` (where `P`
  bounds the previous rung's amplitude): `tail_damped_forced_bound`
  specialised to one rung.
- `amplitude_ladder_collapse` — the equilibria compose down the tail:
  if each rung's bound sits below the dissipation scale
  (`β j ≤ θ·ν·kk j`, `θ < 1` — "the band boundary is at or below the
  dissipation scale"), the bounds collapse geometrically,
  `β j ≤ θʲ·A`.

**ε-uniform reading (physical layer):** `ν_phys ≥ 1/4` and the active
block's top physical wavenumber is bounded (`k_phys = q^n − 1 ≤ e − 1`
for `n ≤ 1/ε`), so both the dissipation-scale condition and the
resulting geometric tail-enstrophy sum are `ε`-free.  The honest
remainder: the per-rung comparison uses the previous rung's *sup* as
constant forcing — composing sups across rungs at the trajectory level
(not just at the bounds level, as `amplitude_ladder_collapse` does) is
the recorded follow-up; and the band-boundary amplitude actually
sitting at the dissipation scale is the data/dynamics condition that
replaces SF6's refuted form — probe-able (SF7).
-/

/-- **Per-rung equilibrium**: a rung starting empty, forced by the rung
    below (`Φ = kn·P²`) and damped at its own dissipation rate
    (`D = ν·kn²`), never exceeds the equilibrium `P²/(ν·kn)`.
    (`tail_damped_forced_bound` specialised to one scalar rung;
    the DN per-amplitude step drops only a non-positive term.) -/
theorem rung_equilibrium (u : ℕ → K) (δ P ν kn : K)
    (hδ : 0 ≤ δ) (hν : 0 < ν) (hkn : 0 < kn)
    (hδD : δ * (ν * kn ^ 2) ≤ 1)
    (h0 : u 0 = 0)
    (hstep : ∀ t, u (t + 1) ≤ u t + δ * (kn * P ^ 2 - ν * kn ^ 2 * u t)) :
    ∀ t, u t ≤ P ^ 2 / (ν * kn) := by
  -- apply the damped-forced invariant with Φ = kn·P², D = ν·kn²
  have hbound := tail_damped_forced_bound u δ (kn * P ^ 2) (ν * kn ^ 2)
    hδ (by positivity) hδD hstep
  intro t
  have heq : kn * P ^ 2 / (ν * kn ^ 2) = P ^ 2 / (ν * kn) := by
    field_simp
  have := hbound t
  rw [h0, heq] at this
  have hmax : max (0 : K) (P ^ 2 / (ν * kn)) = P ^ 2 / (ν * kn) :=
    max_eq_right (by positivity)
  rwa [hmax] at this

/-- **Geometric collapse of the amplitude ladder**: with the per-rung
    recurrence `β(j+1) ≤ β(j)²/(ν·kk j)` (each rung's bound is the
    equilibrium forced by the previous) and the dissipation-scale
    condition `β j ≤ θ·ν·kk j`, the bounds collapse geometrically:
    `β j ≤ θʲ·β 0`.  One induction; the doubly-exponential collapse
    that actually occurs is stronger, but geometric suffices for the
    `ε`-uniform tail-enstrophy sum. -/
theorem amplitude_ladder_collapse (β kk : ℕ → K) (ν θ : K)
    (hθ : 0 ≤ θ) (hν : 0 < ν) (hkk : ∀ j, 0 < kk j)
    (hβ : ∀ j, 0 ≤ β j)
    (hrec : ∀ j, β (j + 1) ≤ β j ^ 2 / (ν * kk j))
    (hsub : ∀ j, β j ≤ θ * (ν * kk j)) :
    ∀ j, β j ≤ θ ^ j * β 0 := by
  intro j
  induction j with
  | zero => simp
  | succ p ih =>
      have hpos : (0 : K) < ν * kk p := mul_pos hν (hkk p)
      have hfrac : β p / (ν * kk p) ≤ θ := by
        rw [div_le_iff₀ hpos]
        linarith [hsub p]
      calc β (p + 1) ≤ β p ^ 2 / (ν * kk p) := hrec p
        _ = β p * (β p / (ν * kk p)) := by ring
        _ ≤ β p * θ :=
            mul_le_mul_of_nonneg_left hfrac (hβ p)
        _ ≤ (θ ^ p * β 0) * θ :=
            mul_le_mul_of_nonneg_right ih hθ
        _ = θ ^ (p + 1) * β 0 := by ring

/-!
### Trajectory-level composition (the recorded remainder (a))

`rung_equilibrium` bounds one rung forced by a *constant*; the honest
remainder was composing the per-rung sups **along the actual
trajectories** — rung `n+1` is forced by the trajectory `u n ·`, not
by a constant.  The composition is a rung-by-rung induction: a uniform
bound on rung `n`'s trajectory upgrades rung `n+1`'s step to the
constant-forced form, and `rung_equilibrium` then yields the uniform
bound on rung `n+1`.  The resulting bounds are exactly the
`rungBound` recursion, and `trajectory_tail_collapse` closes the loop
with `amplitude_ladder_collapse`: under the dissipation-scale
condition the trajectory bounds decay geometrically.
-/

/-- The composed per-rung bounds: `rungBound 0 = P` (the boundary
    datum), `rungBound (n+1) = (rungBound n)²/(ν·k (n+1))` (each rung
    at the equilibrium forced by the previous rung's bound). -/
def rungBound (ν P : K) (k : ℕ → K) : ℕ → K
  | 0 => P
  | n + 1 => (rungBound ν P k n) ^ 2 / (ν * k (n + 1))

/-- **Trajectory-level ladder composition**: for a rung family
    `u n t` (rung `n`, time `t`) with all tail rungs starting empty,
    each rung satisfying the per-amplitude DN step forced by the
    *actual trajectory* of the rung below, and the boundary rung
    uniformly bounded by `P`, every rung's whole trajectory obeys the
    composed bound: `u n t ≤ rungBound n`.  Rung-by-rung induction;
    each step is `rung_equilibrium` after upgrading the trajectory
    forcing to its constant bound. -/
theorem trajectory_ladder_bounds (u : ℕ → ℕ → K) (k : ℕ → K) (δ ν P : K)
    (hδ : 0 ≤ δ) (hν : 0 < ν) (hk : ∀ n, 0 < k n)
    (hnn : ∀ n t, 0 ≤ u n t)
    (hδD : ∀ n, δ * (ν * k (n + 1) ^ 2) ≤ 1)
    (h0 : ∀ n, u (n + 1) 0 = 0)
    (hP : ∀ t, u 0 t ≤ P)
    (hstep : ∀ n t, u (n + 1) (t + 1) ≤ u (n + 1) t
      + δ * (k (n + 1) * u n t ^ 2 - ν * k (n + 1) ^ 2 * u (n + 1) t)) :
    ∀ n t, u n t ≤ rungBound ν P k n := by
  intro n
  induction n with
  | zero => exact hP
  | succ m ih =>
      -- upgrade the trajectory forcing `u m t ^ 2` to the constant
      -- `(rungBound m) ^ 2` — the square is monotone on nonnegatives
      have hstep' : ∀ t, u (m + 1) (t + 1) ≤ u (m + 1) t
          + δ * (k (m + 1) * (rungBound ν P k m) ^ 2
                 - ν * k (m + 1) ^ 2 * u (m + 1) t) := by
        intro t
        have hsq : u m t ^ 2 ≤ (rungBound ν P k m) ^ 2 := by
          have h1 := hnn m t
          have h2 := ih t
          nlinarith
        have hmono : k (m + 1) * u m t ^ 2
            ≤ k (m + 1) * (rungBound ν P k m) ^ 2 :=
          mul_le_mul_of_nonneg_left hsq (le_of_lt (hk (m + 1)))
        have := hstep m t
        nlinarith [mul_le_mul_of_nonneg_left hmono hδ]
      have := rung_equilibrium (fun t => u (m + 1) t) δ
        (rungBound ν P k m) ν (k (m + 1)) hδ hν (hk (m + 1))
        (hδD m) (h0 m) hstep'
      intro t
      exact this t

/-- **Trajectory-level tail collapse**: adding the dissipation-scale
    condition on the composed bounds (`rungBound n ≤ θ·ν·k (n+1)`,
    with `θ ≥ 0` and `0 ≤ P`), the whole trajectory of rung `n` is
    geometrically small: `u n t ≤ θⁿ·P`.  This closes the amplitude
    repair's remainder (a) at the model level — the composition across
    rungs now holds along trajectories, not only at the bounds level. -/
theorem trajectory_tail_collapse (u : ℕ → ℕ → K) (k : ℕ → K) (δ ν P θ : K)
    (hδ : 0 ≤ δ) (hν : 0 < ν) (hk : ∀ n, 0 < k n)
    (hθ : 0 ≤ θ) (hP0 : 0 ≤ P)
    (hnn : ∀ n t, 0 ≤ u n t)
    (hδD : ∀ n, δ * (ν * k (n + 1) ^ 2) ≤ 1)
    (h0 : ∀ n, u (n + 1) 0 = 0)
    (hP : ∀ t, u 0 t ≤ P)
    (hstep : ∀ n t, u (n + 1) (t + 1) ≤ u (n + 1) t
      + δ * (k (n + 1) * u n t ^ 2 - ν * k (n + 1) ^ 2 * u (n + 1) t))
    (hsub : ∀ n, rungBound ν P k n ≤ θ * (ν * k (n + 1))) :
    ∀ n t, u n t ≤ θ ^ n * P := by
  have htraj := trajectory_ladder_bounds u k δ ν P hδ hν hk hnn hδD h0 hP hstep
  -- the composed bounds collapse geometrically
  have hbnn : ∀ n, 0 ≤ rungBound ν P k n := by
    intro n
    cases n with
    | zero => exact hP0
    | succ m =>
        have : (0 : K) < ν * k (m + 1) := mul_pos hν (hk (m + 1))
        exact div_nonneg (sq_nonneg _) (le_of_lt this)
  have hcollapse := amplitude_ladder_collapse
    (fun n => rungBound ν P k n) (fun n => k (n + 1)) ν θ
    hθ hν (fun j => hk (j + 1)) hbnn (fun j => le_of_eq rfl) hsub
  intro n t
  calc u n t ≤ rungBound ν P k n := htraj n t
    _ ≤ θ ^ n * rungBound ν P k 0 := hcollapse n
    _ = θ ^ n * P := rfl

/-!
### Nonlocal (two-source) generalization (SF8 arc)

Full NS transfer is nonlocal; the SF8 probe stress-tests the
per-amplitude route with an energy-conserving second-neighbor channel
of strength `γ` (inflow `γ·k_n·u_{n-2}²` paired with outflow
`−γ·k_{n+2}·u_n·u_{n+2}`, telescoping exactly in the energy sum).
The Lean side: the per-rung equilibrium, the ladder collapse, and the
trajectory composition all survive a second forcing source.

- `rung_equilibrium_two_source` — the damped-forced invariant with
  `Φ = kn·(P₁² + γ·P₂²)`.
- `two_source_ladder_collapse` — the pair-maximum induction: under
  the two-source dissipation-scale condition
  `(1+γ)·max(β j, β (j+1)) ≤ θ·ν·kk j` the pairwise maxima decay
  geometrically (rate `θ` per pair, i.e. `√θ` per rung).
- `rungBound2` + `trajectory_two_source_bounds` — the two-term
  composed bounds hold along whole trajectories (pair induction on
  rungs, each step through `rung_equilibrium_two_source`).

This covers the *second-neighbor* nonlocality class the probe tests —
not full NS triad structure, which remains the standing caveat.
-/

/-- Per-rung equilibrium with a second (nonlocal) source: forced by
    `Φ = kn·(P₁² + γ·P₂²)` and damped at `D = ν·kn²`, a rung starting
    empty never exceeds `(P₁² + γ·P₂²)/(ν·kn)`. -/
theorem rung_equilibrium_two_source (u : ℕ → K) (δ P₁ P₂ γ ν kn : K)
    (hδ : 0 ≤ δ) (hν : 0 < ν) (hkn : 0 < kn) (hγ : 0 ≤ γ)
    (hδD : δ * (ν * kn ^ 2) ≤ 1)
    (h0 : u 0 = 0)
    (hstep : ∀ t, u (t + 1) ≤ u t
      + δ * (kn * (P₁ ^ 2 + γ * P₂ ^ 2) - ν * kn ^ 2 * u t)) :
    ∀ t, u t ≤ (P₁ ^ 2 + γ * P₂ ^ 2) / (ν * kn) := by
  have hbound := tail_damped_forced_bound u δ
    (kn * (P₁ ^ 2 + γ * P₂ ^ 2)) (ν * kn ^ 2)
    hδ (by positivity) hδD hstep
  intro t
  have heq : kn * (P₁ ^ 2 + γ * P₂ ^ 2) / (ν * kn ^ 2)
      = (P₁ ^ 2 + γ * P₂ ^ 2) / (ν * kn) := by
    field_simp
  have := hbound t
  rw [h0, heq] at this
  have hmax : max (0 : K) ((P₁ ^ 2 + γ * P₂ ^ 2) / (ν * kn))
      = (P₁ ^ 2 + γ * P₂ ^ 2) / (ν * kn) :=
    max_eq_right (by positivity)
  rwa [hmax] at this

/-- **Two-source ladder collapse** (pair-maximum induction): with the
    two-term recurrence `β(j+2) ≤ (β(j+1)² + γ·β j²)/(ν·kk j)` and
    the two-source dissipation-scale condition
    `(1+γ)·max(β j, β(j+1)) ≤ θ·ν·kk j` (`θ ≤ 1`), the pairwise
    maxima decay geometrically:
    `max (β (2m)) (β (2m+1)) ≤ θᵐ·max (β 0) (β 1)`. -/
theorem two_source_ladder_collapse (β kk : ℕ → K) (ν θ γ : K)
    (hθ0 : 0 ≤ θ) (hθ1 : θ ≤ 1) (hν : 0 < ν) (hγ : 0 ≤ γ)
    (hkk : ∀ j, 0 < kk j) (hβ : ∀ j, 0 ≤ β j)
    (hrec : ∀ j, β (j + 2) ≤ (β (j + 1) ^ 2 + γ * β j ^ 2) / (ν * kk j))
    (hsub : ∀ j, (1 + γ) * max (β j) (β (j + 1)) ≤ θ * (ν * kk j)) :
    ∀ m, max (β (2 * m)) (β (2 * m + 1)) ≤ θ ^ m * max (β 0) (β 1) := by
  have hMnn : ∀ j, 0 ≤ max (β j) (β (j + 1)) :=
    fun j => le_trans (hβ j) (le_max_left _ _)
  have hstep : ∀ j, β (j + 2) ≤ θ * max (β j) (β (j + 1)) := by
    intro j
    have hpos : (0 : K) < ν * kk j := mul_pos hν (hkk j)
    have hb0 : β j ≤ max (β j) (β (j + 1)) := le_max_left _ _
    have hb1 : β (j + 1) ≤ max (β j) (β (j + 1)) := le_max_right _ _
    have hsq0 : β j ^ 2 ≤ max (β j) (β (j + 1)) ^ 2 := by
      nlinarith [hβ j, hMnn j]
    have hsq1 : β (j + 1) ^ 2 ≤ max (β j) (β (j + 1)) ^ 2 := by
      nlinarith [hβ (j + 1), hMnn j]
    have hnum : β (j + 1) ^ 2 + γ * β j ^ 2
        ≤ (1 + γ) * max (β j) (β (j + 1)) ^ 2 := by
      nlinarith [mul_le_mul_of_nonneg_left hsq0 hγ]
    have hlast : (β (j + 1) ^ 2 + γ * β j ^ 2) / (ν * kk j)
        ≤ θ * max (β j) (β (j + 1)) := by
      rw [div_le_iff₀ hpos]
      nlinarith [mul_le_mul_of_nonneg_right (hsub j) (hMnn j)]
    exact le_trans (hrec j) hlast
  have hmono : ∀ j, max (β (j + 1)) (β (j + 2)) ≤ max (β j) (β (j + 1)) := by
    intro j
    refine max_le (le_max_right _ _) ?_
    have h1 := hstep j
    nlinarith [hMnn j]
  have hdecay : ∀ j,
      max (β (j + 2)) (β (j + 3)) ≤ θ * max (β j) (β (j + 1)) := by
    intro j
    refine max_le (hstep j) ?_
    have h3 : β (j + 3) ≤ θ * max (β (j + 1)) (β (j + 2)) := hstep (j + 1)
    have h4 : θ * max (β (j + 1)) (β (j + 2)) ≤ θ * max (β j) (β (j + 1)) :=
      mul_le_mul_of_nonneg_left (hmono j) hθ0
    exact le_trans h3 h4
  intro m
  induction m with
  | zero => simp
  | succ p ih =>
      have hidx1 : 2 * (p + 1) = 2 * p + 2 := by ring
      rw [hidx1]
      calc max (β (2 * p + 2)) (β (2 * p + 3))
          ≤ θ * max (β (2 * p)) (β (2 * p + 1)) := hdecay (2 * p)
        _ ≤ θ * (θ ^ p * max (β 0) (β 1)) :=
            mul_le_mul_of_nonneg_left ih hθ0
        _ = θ ^ (p + 1) * max (β 0) (β 1) := by ring

/-- The two-source composed per-rung bounds: boundary data `P₀, P₁`
    on the first two rungs, then each rung at the two-source
    equilibrium forced by the previous two rungs' bounds. -/
def rungBound2 (ν P₀ P₁ γ : K) (k : ℕ → K) : ℕ → K
  | 0 => P₀
  | 1 => P₁
  | n + 2 => (rungBound2 ν P₀ P₁ γ k (n + 1) ^ 2
      + γ * rungBound2 ν P₀ P₁ γ k n ^ 2) / (ν * k (n + 2))

/-- **Trajectory-level two-source composition**: with every rung from
    the third onward starting empty and satisfying the two-source
    per-amplitude DN step forced by the *actual trajectories* of the
    two rungs below, and the first two rungs uniformly bounded, every
    rung's whole trajectory obeys the two-term composed bound.  Pair
    induction on rungs; each step is `rung_equilibrium_two_source`
    after upgrading the trajectory forcing to its uniform bounds. -/
theorem trajectory_two_source_bounds (u : ℕ → ℕ → K) (k : ℕ → K)
    (δ ν γ P₀ P₁ : K)
    (hδ : 0 ≤ δ) (hν : 0 < ν) (hγ : 0 ≤ γ) (hk : ∀ n, 0 < k n)
    (hnn : ∀ n t, 0 ≤ u n t)
    (hδD : ∀ n, δ * (ν * k (n + 2) ^ 2) ≤ 1)
    (h0 : ∀ n, u (n + 2) 0 = 0)
    (hP0 : ∀ t, u 0 t ≤ P₀) (hP1 : ∀ t, u 1 t ≤ P₁)
    (hstep : ∀ n t, u (n + 2) (t + 1) ≤ u (n + 2) t
      + δ * (k (n + 2) * (u (n + 1) t ^ 2 + γ * u n t ^ 2)
             - ν * k (n + 2) ^ 2 * u (n + 2) t)) :
    ∀ n t, u n t ≤ rungBound2 ν P₀ P₁ γ k n := by
  have key : ∀ n, (∀ t, u n t ≤ rungBound2 ν P₀ P₁ γ k n)
      ∧ (∀ t, u (n + 1) t ≤ rungBound2 ν P₀ P₁ γ k (n + 1)) := by
    intro n
    induction n with
    | zero => exact ⟨hP0, hP1⟩
    | succ p ih =>
        refine ⟨ih.2, ?_⟩
        have hstep' : ∀ t, u (p + 2) (t + 1) ≤ u (p + 2) t
            + δ * (k (p + 2) * (rungBound2 ν P₀ P₁ γ k (p + 1) ^ 2
                 + γ * rungBound2 ν P₀ P₁ γ k p ^ 2)
                 - ν * k (p + 2) ^ 2 * u (p + 2) t) := by
          intro t
          have hs1 : u (p + 1) t ^ 2
              ≤ rungBound2 ν P₀ P₁ γ k (p + 1) ^ 2 := by
            nlinarith [hnn (p + 1) t, ih.2 t]
          have hs0 : u p t ^ 2 ≤ rungBound2 ν P₀ P₁ γ k p ^ 2 := by
            nlinarith [hnn p t, ih.1 t]
          have hforc : u (p + 1) t ^ 2 + γ * u p t ^ 2
              ≤ rungBound2 ν P₀ P₁ γ k (p + 1) ^ 2
                + γ * rungBound2 ν P₀ P₁ γ k p ^ 2 := by
            nlinarith [mul_le_mul_of_nonneg_left hs0 hγ]
          have hmono := mul_le_mul_of_nonneg_left hforc
            (le_of_lt (hk (p + 2)))
          have := hstep p t
          nlinarith [mul_le_mul_of_nonneg_left hmono hδ]
        have hbnd := rung_equilibrium_two_source (fun t => u (p + 2) t) δ
          (rungBound2 ν P₀ P₁ γ k (p + 1)) (rungBound2 ν P₀ P₁ γ k p)
          γ ν (k (p + 2))
          hδ hν (hk (p + 2)) hγ (hδD p) (h0 p) hstep'
        intro t
        simpa [rungBound2] using hbnd t
  intro n
  exact (key n).1

/-!
### All-pairs (geometric N-source) generalization (SF9 arc)

The SF9 probe couples *every* rung pair `(m, n)`, `m < n`, with
geometric weight `λ^{n−m−1}` — the closest shell-model image of full
NS triad structure, each pair energy-conserving by construction.  The
Lean side: the per-rung equilibrium holds for *arbitrary* nonnegative
constant forcing (`rung_equilibrium_forced` — the all-pairs geometric
sum is a special case), and the ladder is uniformly `θ`-suppressed
under the all-pairs dissipation-scale condition
(`multi_source_ladder_uniform`, strong induction with the geometric
sum `∑ λ^j ≤ 1/(1−λ)`).  What is *not* claimed: a geometric-decay
version of the all-pairs collapse (the two-source pair-maximum
argument does not lift verbatim) — recorded follow-up; and sweeping
effects (phase decorrelation by distant scales), which a
real-amplitude shell model cannot represent at all — the irreducible
caveat.
-/

/-- Per-rung equilibrium with arbitrary nonnegative constant forcing
    `Φ = kn·F`: a rung starting empty never exceeds `F/(ν·kn)`.
    Generalizes `rung_equilibrium` (`F = P²`) and
    `rung_equilibrium_two_source` (`F = P₁² + γ·P₂²`); the SF9
    all-pairs geometric sum `F = ∑_{m<n} λ^{n−1−m}·P_m²` is the
    intended instance. -/
theorem rung_equilibrium_forced (u : ℕ → K) (δ F ν kn : K)
    (hδ : 0 ≤ δ) (hν : 0 < ν) (hkn : 0 < kn) (hF : 0 ≤ F)
    (hδD : δ * (ν * kn ^ 2) ≤ 1)
    (h0 : u 0 = 0)
    (hstep : ∀ t, u (t + 1) ≤ u t + δ * (kn * F - ν * kn ^ 2 * u t)) :
    ∀ t, u t ≤ F / (ν * kn) := by
  have hbound := tail_damped_forced_bound u δ (kn * F) (ν * kn ^ 2)
    hδ (by positivity) hδD hstep
  intro t
  have heq : kn * F / (ν * kn ^ 2) = F / (ν * kn) := by
    field_simp
  have := hbound t
  rw [h0, heq] at this
  have hmax : max (0 : K) (F / (ν * kn)) = F / (ν * kn) :=
    max_eq_right (by positivity)
  rwa [hmax] at this

/-- **All-pairs uniform suppression** (strong induction): with the
    geometric all-pairs recurrence
    `β n ≤ (∑_{m<n} λ^{n−1−m}·β m²)/(ν·k n)` for `n ≥ 1`, a band
    bound `β 0 ≤ B`, and the all-pairs dissipation-scale condition
    `B ≤ θ·(1−λ)·ν·k n` (`θ ≤ 1`, `0 ≤ λ < 1`), every rung beyond
    the band is uniformly `θ`-suppressed: `β n ≤ θ·B`.  The geometric
    weight sum is controlled by `∑_{j<n} λ^j ≤ 1/(1−λ)`. -/
theorem multi_source_ladder_uniform (β k : ℕ → K) (ν θ lam B : K)
    (hθ0 : 0 ≤ θ) (hθ1 : θ ≤ 1) (hν : 0 < ν)
    (hl0 : 0 ≤ lam) (hl1 : lam < 1)
    (hk : ∀ n, 0 < k n) (hβ : ∀ n, 0 ≤ β n)
    (hB0 : β 0 ≤ B) (hBnn : 0 ≤ B)
    (hrec : ∀ n, 1 ≤ n → β n
      ≤ (∑ m ∈ Finset.range n, lam ^ (n - 1 - m) * β m ^ 2) / (ν * k n))
    (hsub : ∀ n, 1 ≤ n → B ≤ θ * ((1 - lam) * (ν * k n))) :
    ∀ n, 1 ≤ n → β n ≤ θ * B := by
  intro n
  induction n using Nat.strong_induction_on with
  | _ n ih =>
    intro hn
    have hall : ∀ m, m < n → β m ≤ B := by
      intro m hm
      rcases Nat.eq_zero_or_pos m with h | h
      · rw [h]; exact hB0
      · have := ih m hm h
        nlinarith
    have hpos : (0 : K) < ν * k n := mul_pos hν (hk n)
    have h1l : (0 : K) < 1 - lam := by linarith
    -- termwise bound + reflect + geometric sum
    have hsum1 : ∑ m ∈ Finset.range n, lam ^ (n - 1 - m) * β m ^ 2
        ≤ ∑ m ∈ Finset.range n, lam ^ (n - 1 - m) * B ^ 2 := by
      apply Finset.sum_le_sum
      intro m hm
      have hmlt := Finset.mem_range.mp hm
      have hsq : β m ^ 2 ≤ B ^ 2 := by
        nlinarith [hβ m, hall m hmlt]
      exact mul_le_mul_of_nonneg_left hsq (pow_nonneg hl0 _)
    have hrefl : ∑ m ∈ Finset.range n, lam ^ (n - 1 - m) * B ^ 2
        = (∑ j ∈ Finset.range n, lam ^ j) * B ^ 2 := by
      rw [← Finset.sum_mul]
      congr 1
      exact Finset.sum_range_reflect (fun j => lam ^ j) n
    have hSnn : (0 : K) ≤ ∑ j ∈ Finset.range n, lam ^ j :=
      Finset.sum_nonneg fun j _ => pow_nonneg hl0 j
    have hgS : (∑ j ∈ Finset.range n, lam ^ j) * (1 - lam) ≤ 1 := by
      nlinarith [geom_sum_mul lam n, pow_nonneg hl0 n]
    -- assemble: β n ≤ S·B²/(ν·k n) ≤ θ·B
    have hlast : (∑ j ∈ Finset.range n, lam ^ j) * B ^ 2 / (ν * k n)
        ≤ θ * B := by
      rw [div_le_iff₀ hpos]
      have hs := mul_le_mul_of_nonneg_left (hsub n hn)
        (mul_nonneg hSnn hBnn)
      -- hs : S·B·B ≤ S·B·(θ·((1−λ)·ν·k n))
      have hfac : (∑ j ∈ Finset.range n, lam ^ j) * B
            * (θ * ((1 - lam) * (ν * k n)))
          = ((∑ j ∈ Finset.range n, lam ^ j) * (1 - lam))
            * (θ * B * (ν * k n)) := by ring
      have hcap : ((∑ j ∈ Finset.range n, lam ^ j) * (1 - lam))
            * (θ * B * (ν * k n))
          ≤ 1 * (θ * B * (ν * k n)) := by
        apply mul_le_mul_of_nonneg_right hgS
        positivity
      nlinarith [hs]
    calc β n ≤ (∑ m ∈ Finset.range n, lam ^ (n - 1 - m) * β m ^ 2)
        / (ν * k n) := hrec n hn
      _ ≤ (∑ j ∈ Finset.range n, lam ^ j) * B ^ 2 / (ν * k n) := by
          gcongr
          exact le_of_le_of_eq hsum1 hrefl
      _ ≤ θ * B := hlast

end QOU.FluidDynamics.PhysicalLayerLeray

