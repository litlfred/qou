import Mathlib.Tactic

/-!
# QOU.FluidDynamics.pair_phase1_riccati

**Phase-1 closed-form calculus of the two-regime pair-collision model**
(the separated / Biot–Savart phase of the anti-parallel vortex pair,
`rem:townsend-biot-savart-strain`), theorem-grade and derivative-free.

The corpus two-regime ODE model has, in phase 1 (separation `d² > V₁`):
`(d²)' = −Γ/π` and `Ω' = (Γ/(π d²))·Ω`.  Its exact solution is
`d²(t) = d₀² − r·t` (with `r := Γ/π`) and `Ω(t) = Ω₀·d₀²/d²(t)`.  The
probe `computations/qns_pair_riccati_probe.py` (witness
`qns-pair-riccati-probe.witness.json`) found numerically that `d²·Ω` is
an exact invariant and the Riccati coefficient `c′` is exactly uniform
(`= 1/π` at unit parameters) throughout phase 1.  This file proves that
finding as algebra — no `deriv`, no limits: every statement is an exact
identity or inequality about the closed-form flow, over a generic
linearly ordered field (§7c: only field algebra and order are used).

Main results (all sorry-free):

- `d2_mul_Om_invariant` — `d²(t)·Ω(t) = d₀²·Ω₀` (the probe's exact
  invariant).
- `Om_closed_form` — `Ω(t) = Ω₀ / (1 − c′·Ω₀·t)` with
  `c′ = r/(d₀²·Ω₀)`: the *exact* solution of the uniform-coefficient
  Riccati equation `Ω' = c′·Ω²` — phase 1 IS a uniform Riccati flow.
- `one_div_Om_sub` — `1/Ω(t) − 1/Ω(t+s) = c′·s`: the derivative-free
  form of uniformity (the reciprocal decreases at exactly rate `c′`).
- `Om_mono` — `Ω` is monotone on the pre-collision interval.
- `discrete_riccati_lower` — `Ω(t+δ) ≥ Ω(t) + c′·δ·Ω(t)²`: the pair
  channel satisfies the **hypothesis of the GP5 blow-up lemma**
  `riccati_lower_growth` (`surreal_enstrophy_finite_modes.lean`) with
  the uniform constant `c′ = Γ/(π d₀² Ω₀)`, at every step size, on all
  of phase 1.
- `Om_hits_every_level` — for every `M > Ω₀` there is
  `t ∈ (0, d₀²/r)` with `Ω(t) = M`: the phase-1 flow is unbounded on
  approach to the inviscid collision time `t* = d₀²/r = π d₀²/Γ`.

**Scope (honest):** these are statements about the *corpus ODE model's
phase-1 closed form* — the in-QOU two-regime collision model — not
about the Navier–Stokes PDE.  The model-to-PDE step (uniformity of the
overlap engagement, `Γ` constancy during approach) is the named open
item; the sub-leading strain correction vanishing on approach is the
owner-proved `kappa_squared_tends_to_zero`
(`fluid-dynamics/townsend-biot-savart-strain.lean`).  Phase 2 (overlap
saturation) is exactly where this calculus *stops* being valid — the
saturation destroys the uniform `c′`, which is the regularizing cutoff
measured by the probe and the analytic race `overlap_race_strict`.
-/

namespace QOU.FluidDynamics.PairPhase1

variable {K : Type*} [Field K] [LinearOrder K] [IsStrictOrderedRing K]

/-- Phase-1 separation-squared: `d²(t) = d₀² − r·t`, where `r = Γ/π` is
    the constant Biot–Savart approach rate (`(d²)' = −Γ/π`). -/
def d2 (d0sq r t : K) : K := d0sq - r * t

/-- Phase-1 enstrophy along the closed-form flow:
    `Ω(t) = Ω₀·d₀²/d²(t)`. -/
def Om (Om0 d0sq r t : K) : K := Om0 * d0sq / d2 d0sq r t

/-- The uniform Riccati coefficient `c′ = r/(d₀²·Ω₀)`
    (`= Γ/(π d₀² Ω₀)`; `= 1/π` at unit parameters, the probe's value). -/
def cPrime (Om0 d0sq r : K) : K := r / (d0sq * Om0)

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **The exact invariant**: `d²(t)·Ω(t) = d₀²·Ω₀` throughout phase 1.
    (The probe's sharp finding: `(d²Ω)' = 0`, so `c′` cannot drift.) -/
theorem d2_mul_Om_invariant (Om0 d0sq r t : K) (hd : d2 d0sq r t ≠ 0) :
    d2 d0sq r t * Om Om0 d0sq r t = d0sq * Om0 := by
  unfold Om
  field_simp

/-- **Phase 1 is a uniform Riccati flow**: the closed form
    `Ω(t) = Ω₀ / (1 − c′·Ω₀·t)` — the exact solution of `Ω' = c′·Ω²`
    with constant `c′`. -/
theorem Om_closed_form (Om0 d0sq r t : K) (h0 : d0sq ≠ 0)
    (hd : d2 d0sq r t ≠ 0) :
    Om Om0 d0sq r t = Om0 / (1 - cPrime Om0 d0sq r * Om0 * t) := by
  have hOm0ne : (1 : K) - cPrime Om0 d0sq r * Om0 * t ≠ 0 := by
    unfold cPrime
    intro h
    apply hd
    unfold d2
    have h' : d0sq * ((1 : K) - r / (d0sq * Om0) * Om0 * t) = 0 := by
      rw [h]; ring
    by_cases hOm : Om0 = 0
    · -- with `Ω₀ = 0` the hypothesis `h` reads `1 − r/(d0sq·0)·0·t = 1 = 0`
      exfalso
      apply one_ne_zero (α := K)
      calc (1 : K) = 1 - r / (d0sq * Om0) * Om0 * t := by
            rw [hOm]; ring
        _ = 0 := h
    · calc d0sq - r * t
          = d0sq * ((1 : K) - r / (d0sq * Om0) * Om0 * t) := by
            field_simp
        _ = 0 := h'
  unfold Om d2 cPrime at *
  by_cases hOm : Om0 = 0
  · simp [hOm]
  · field_simp

omit [LinearOrder K] [IsStrictOrderedRing K] in
/-- **Derivative-free uniformity of `c′`**: the reciprocal enstrophy
    decreases at the exact constant rate `c′` —
    `1/Ω(t) − 1/Ω(t+s) = c′·s` for every `t, s`.  This is the identity
    behind the probe's "c′ exactly uniform in phase 1". -/
theorem one_div_Om_sub (Om0 d0sq r t s : K) (h0 : d0sq ≠ 0)
    (hOm0 : Om0 ≠ 0) :
    1 / Om Om0 d0sq r t - 1 / Om Om0 d0sq r (t + s)
      = cPrime Om0 d0sq r * s := by
  unfold Om d2 cPrime
  field_simp
  ring

/-- `Ω` is positive on the pre-collision interval. -/
theorem Om_pos (Om0 d0sq r t : K) (hOm0 : 0 < Om0) (h0 : 0 < d0sq)
    (hd : 0 < d2 d0sq r t) : 0 < Om Om0 d0sq r t :=
  div_pos (mul_pos hOm0 h0) hd

/-- **Monotonicity**: `Ω(t) ≤ Ω(t+s)` whenever both times precede the
    collision (`d² > 0` at the later time) and `r·s ≥ 0`. -/
theorem Om_mono (Om0 d0sq r t s : K) (hOm0 : 0 < Om0) (h0 : 0 < d0sq)
    (hd2 : 0 < d2 d0sq r (t + s)) (hrs : 0 ≤ r * s) :
    Om Om0 d0sq r t ≤ Om Om0 d0sq r (t + s) := by
  have hstep : d2 d0sq r (t + s) ≤ d2 d0sq r t := by
    unfold d2; nlinarith
  have hd1 : 0 < d2 d0sq r t := lt_of_lt_of_le hd2 hstep
  unfold Om
  rw [div_le_div_iff₀ hd1 hd2]
  have hA : 0 ≤ Om0 * d0sq := le_of_lt (mul_pos hOm0 h0)
  exact mul_le_mul_of_nonneg_left hstep hA

/-- **The pair channel satisfies the GP5 Riccati-lower-bound hypothesis
    with uniform `c′`**: `Ω(t+δ) ≥ Ω(t) + c′·δ·Ω(t)²` for every step
    `δ ≥ 0` inside phase 1.  (From `one_div_Om_sub`,
    `Ω(t+δ) − Ω(t) = c′·δ·Ω(t)·Ω(t+δ) ≥ c′·δ·Ω(t)²` by monotonicity.)
    This is the mechanism-level branch-A statement *during the
    approach*: while separated, the pair's enstrophy self-amplifies at
    the exact uniform Riccati rate. -/
theorem discrete_riccati_lower (Om0 d0sq r t δ : K) (hOm0 : 0 < Om0)
    (h0 : 0 < d0sq) (hr : 0 ≤ r) (hδ : 0 ≤ δ)
    (hd2 : 0 < d2 d0sq r (t + δ)) :
    Om Om0 d0sq r t + cPrime Om0 d0sq r * δ * (Om Om0 d0sq r t) ^ 2
      ≤ Om Om0 d0sq r (t + δ) := by
  have hstep : d2 d0sq r (t + δ) ≤ d2 d0sq r t := by
    unfold d2; nlinarith
  have hd1 : 0 < d2 d0sq r t := lt_of_lt_of_le hd2 hstep
  have hO1 : 0 < Om Om0 d0sq r t := Om_pos _ _ _ _ hOm0 h0 hd1
  -- `hO2` is consumed implicitly by the `field_simp` in `h1` below (it
  -- clears the `1/Ω(t+δ)` denominator); removing it leaves `h1` unprovable
  have hO2 : 0 < Om Om0 d0sq r (t + δ) := Om_pos _ _ _ _ hOm0 h0 hd2
  have hmono : Om Om0 d0sq r t ≤ Om Om0 d0sq r (t + δ) :=
    Om_mono _ _ _ _ _ hOm0 h0 hd2 (mul_nonneg hr hδ)
  have hrecip := one_div_Om_sub Om0 d0sq r t δ (ne_of_gt h0)
    (ne_of_gt hOm0)
  -- multiply the reciprocal identity through by `Ω(t)·Ω(t+δ) > 0`
  have hprod : Om Om0 d0sq r (t + δ) - Om Om0 d0sq r t
      = cPrime Om0 d0sq r * δ * (Om Om0 d0sq r t * Om Om0 d0sq r (t + δ)) := by
    have h1 : (1 / Om Om0 d0sq r t - 1 / Om Om0 d0sq r (t + δ))
        * (Om Om0 d0sq r t * Om Om0 d0sq r (t + δ))
        = Om Om0 d0sq r (t + δ) - Om Om0 d0sq r t := by
      field_simp
    calc Om Om0 d0sq r (t + δ) - Om Om0 d0sq r t
        = (1 / Om Om0 d0sq r t - 1 / Om Om0 d0sq r (t + δ))
            * (Om Om0 d0sq r t * Om Om0 d0sq r (t + δ)) := h1.symm
      _ = cPrime Om0 d0sq r * δ
            * (Om Om0 d0sq r t * Om Om0 d0sq r (t + δ)) := by rw [hrecip]
  have hc : 0 ≤ cPrime Om0 d0sq r := by
    unfold cPrime
    exact div_nonneg hr (le_of_lt (mul_pos h0 hOm0))
  nlinarith [mul_le_mul_of_nonneg_left hmono
    (mul_nonneg (mul_nonneg hc hδ) (le_of_lt hO1))]

/-- **Unboundedness on approach**: for every level `M > Ω₀` there is a
    time `0 < t < d₀²/r` (strictly before the inviscid collision time
    `t* = d₀²/r = π d₀²/Γ`) with `Ω(t) = M`.  Phase 1 alone drives the
    enstrophy through every finite level — blow-up in the model is
    prevented only by the phase-2 overlap cutoff engaging first
    (`overlap_race_strict`). -/
theorem Om_hits_every_level (Om0 d0sq r M : K) (hOm0 : 0 < Om0)
    (h0 : 0 < d0sq) (hr : 0 < r) (hM : Om0 < M) :
    ∃ t : K, 0 < t ∧ t < d0sq / r ∧ Om Om0 d0sq r t = M := by
  have hMpos : 0 < M := lt_trans hOm0 hM
  refine ⟨d0sq / r * (1 - Om0 / M), ?_, ?_, ?_⟩
  · have h1 : 0 < 1 - Om0 / M := by
      have : Om0 / M < 1 := (div_lt_one hMpos).mpr hM
      linarith
    exact mul_pos (div_pos h0 hr) h1
  · have h1 : 1 - Om0 / M < 1 := by
      have : 0 < Om0 / M := div_pos hOm0 hMpos
      linarith
    calc d0sq / r * (1 - Om0 / M) < d0sq / r * 1 :=
          mul_lt_mul_of_pos_left h1 (div_pos h0 hr)
      _ = d0sq / r := mul_one _
  · unfold Om d2
    have hd : d0sq - r * (d0sq / r * (1 - Om0 / M)) = d0sq * Om0 / M := by
      field_simp
      ring
    rw [hd]
    field_simp

/-!
## Γ-robustness of the overlap race (the lock-uniformity caveat)

The campaign ledger names one candidate flaw in the pair-channel
regularisation: *"`Γ` growth during collision"* — if the circulation
strengthens as the pair approaches, could the approach outrun the
stretching and reach `d = 0` before the overlap cutoff engages?

**No — in the two-regime model the race is `Γ(t)`-free.**  Reparametrize
time by the consumed circulation `τ` with `dτ = Γ(t)·dt/π` (monotone for
any positive circulation history).  Then phase 1 reads `d(d²)/dτ = −1`
and `dV₁/dτ = V₁/(2d²)`, so `W := V₁²` satisfies `dW/dτ = W/d²` — the
*same* closed form as `Ω` above: `W(τ) = W₀·d₀²/(d₀² − τ)` (take
`Om W₀ d₀² 1 τ` with rate `r = 1`), and `W·d²` is an exact invariant.
`Γ` has been eliminated: every positive circulation history traverses
the same phase-plane curve, only at a different speed.  The overlap
condition `V₁ ≥ d²` (`W ≥ (d²)²`) therefore engages exactly when
`(d²)³ ≤ W₀·d₀²`, i.e. at separation `d² = (V₁₀·d₀)^{2/3} > 0` —
strictly before collision, for **any** `Γ(t) > 0`.

`overlap_at_small_separation` below is the algebraic content (the
phase-plane inequality); the `Γ`-elimination step is the one-line chain
rule above (a modeling identity about the ODE system, stated here, not
formalized — `deriv`-level calculus).  Scope: the two-regime ODE model;
the model-to-PDE uniformity question remains the named open item.
-/

/-- **The overlap race is won before collision, `Γ`-free**: along the
    `τ`-parametrized phase-1 flow (`W(τ) = Om W₀ d₀² 1 τ`, `d²(τ) =
    d₀² − τ = x`), overlap `W ≥ x²` holds as soon as `x³ ≤ W₀·d₀²`.
    Since `W₀·d₀² > 0`, such `x > 0` exist: the cutoff engages at
    positive separation for every positive circulation history. -/
theorem overlap_at_small_separation (W0 d0sq x : K) (hx : 0 < x) (hcube : x ^ 3 ≤ W0 * d0sq) :
    x ^ 2 ≤ Om W0 d0sq 1 (d0sq - x) := by
  have hd2 : d2 d0sq 1 (d0sq - x) = x := by unfold d2; ring
  unfold Om
  rw [hd2, le_div_iff₀ hx]
  calc x ^ 2 * x = x ^ 3 := by ring
    _ ≤ W0 * d0sq := hcube

end QOU.FluidDynamics.PairPhase1
