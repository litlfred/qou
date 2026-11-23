# The map from categorical energy 𝔈 to MeV, and the muon carrier (W6)

Date: 2026-11-22. Workstream W6 of the L2 1-ppQ plan. Beans `qou-91w7` (𝔈 → MeV) and
`qou-6gf9` (the muon carrier). Lean: `QOU/Observations/EnergyScaleMap.lean`, sorry-free,
`lean`-direct exit 0, `#print axioms` shows only `propext`, `Classical.choice`, `Quot.sound`.

Owner ruling of the same day: *"𝔈 is categorical energy. Needs scaling (coming from CAL123
hopefully)"*. This note says what CAL-1/2/3 can fix and what they cannot. No fourth constant is
added, nothing is fitted, and no measured value appears in the Lean.

## 1. Set-up

A chart is a unit Λ (MeV per categorical unit) and a categorical weight w(X) per object; the
physical value is Λ·w(X). As the model sees them, the calibrations are one dimensionful number
and two ratios: CAL-1 gives m_e; CAL-2's proxy m_μ/m_e defines q₀; CAL-3 gives m_π/m_e.

## 2. What CAL-1/2/3 fix

| Statement | Lean |
|---|---|
| Once the electron's categorical weight w_e is fixed and non-zero, CAL-1 forces Λ = m_e/w_e. | `Chart.unit_eq_of_matches` |
| Every prediction is then m_e · w(X)/w_e. The unit carries nothing beyond w_e. | `Chart.value_eq_electron_ratio` |
| The 𝔈 → MeV map is Φ(𝔈) = m_e · 𝔈/𝔈_e, evaluated at q₀. With 𝔈 = 𝔪·c_q² the factor c_q² cancels: Φ gives the same MeV whether one feeds it energies or masses. | `calMap`, `energy_map_eq_mass_map` |
| CAL-2 fixes q₀ (the point where the ratios are evaluated); CAL-3 fixes the meson weight at q₀. | (definition of q₀: `CalibrationTriple.q0_spec`) |

So, in the owner's words, the scaling does come from CAL-1/2/3: CAL-1 sets the MeV value of the
electron, CAL-2 sets the point q₀, and the map is "divide by the electron's categorical energy and
multiply by m_e". This is the only map the three calibrations allow; no other constant enters.

## 3. What they cannot fix

1. **The split between unit and weight** (`Chart.matches_rescale`,
   `Chart.calibration_does_not_fix_unit`). The rescaling (Λ, w) ↦ (tΛ, w/t) leaves every
   physical value unchanged, so calibration data never decide it.
2. **Whether c_q² is in the weights** (`Chart.energy_chart_value`). An energy chart and a mass
   chart give the same values exactly when their units differ by c_q². This is the reading A/B
   question of `qou-91w7`: the calibrations cannot see it, and a consistent map (§2) does not need
   it.
3. **Any dimensionful quantity from CAL-2 or CAL-3** (`Chart.ratio_unit_free`). Both are ratios.
4. **The electron's categorical weight w_e itself.** This is the one real open input. The corpus
   currently uses two different ones:
   - the trace pipeline: the convention-D trace of the electron word σ₀σ₁σ₀ with Hopf closure,
     finite and non-zero at q = 1 (`traceD_one`: value 2^{c−n});
   - the mass formula m(K) = m_e·Vol(K)·ρ(K)/ℏ_q²: unit m_e/ℏ_q² and electron weight ℏ_q²,
     which vanishes to order 2 at q = 1 (`massFormulaElectron`).

   These are different functions, so the two pipelines use different units. The calibrations
   cannot say which is canonical (item 1). Deriving w_e is the derivation the owner's ruling asks
   for.

**The "−99 %" reading explained** (`mixed_map`). Sending a categorical energy 𝔪_X·c_q² through a
map normalised by the electron's categorical mass 𝔪_e multiplies the answer by c_q²; reading it
the other way divides by c_q²(q₀) ≈ 82.7. That is the −99 % of `qou-91w7` reading A. A
consistent map uses the same kind of quantity for X and for the electron, and then c_q² cancels.

**E₀.** E₀ = m_e·c_q²·ℏ_q is the electron-normalised weight E₀/m_e = 1/(q(q − 1)). This ratio
has a simple pole at q = 1, so it is not a ratio of two framed braid-word traces
(`E0_not_trace_ratio`). This extends `traceD_ne_weight` (PR #9023) from "not a trace" to "not a
trace normalised by any electron trace".

## 4. The muon carrier m_μ = m_e·Vol(4₁)/ℏ_q²

**It is the definition of q₀, not a derivation.** In the mass-formula chart the carrier holds by
definition (`massFormula_carrier`), and at the CAL-2 point the unit m_e/ℏ_q² equals m_μ/Vol(4₁)
(`massFormula_unit`). `cal2_identity_pinned` (figure-8-muon-mass-cross-check.lean:44) proves
the identity from itself; it is a restatement, and this file does not make it more than that.

**What a derivation would need.** The carrier is a statement about the ratio w_μ/w_e, and that
ratio is unchanged by the gauge freedom of §3, so the following two obstructions are
chart-independent.

1. **Order of vanishing** (`electron_weight_vanishes`, `muon_carrier_not_trace_ratio`). If
   w_μ = (Vol/ℏ_q²)·w_e on q > 1 with both continuous at q = 1, then w_e(1) = 0. In particular
   no pair of framed braid-word traces, on any numbers of strands, with framing factors
   continuous at 1 (the electron's non-zero there) satisfies the carrier. The electron side must
   vanish to order exactly two more than the muon side at q = 1.
2. **Coefficient field** (`const_mem_of_poly_identity`, `carrier_const_mem_of_rational`). If
   both weights are rational functions with coefficients in a subfield K ⊆ ℝ, the carrier
   forces Vol ∈ K. For K = ℚ this would need Vol(4₁) = 2·Cl₂(π/3) rational. Its irrationality is,
   as far as I know, not proved, so this is stated as a conditional, not as an exclusion: a
   ℚ(q)-valued pair can carry Vol(4₁) only if Vol(4₁) ∈ ℚ. Read: Vol(4₁) has to enter through an
   analytic input (for example a volume-conjecture limit or a quantum dilogarithm), not through a
   finite Hecke trace at generic q.

Scope: (b) for the stated classes (single framed braid-word traces; rational functions over K),
(a) for everything else. Sums and towers of traces, which can vanish at q = 1, are not covered by
item 1. Item 2 covers them when they are rational.

## 5. Where this leaves the two beans

- `qou-91w7`: the 𝔈 → MeV map is fixed by CAL-1 up to one open input, the electron's categorical
  energy 𝔈_e, which must be derived in the same pipeline as the observable. The −99 % reading is
  a mixing error, not a second candidate map. The two scales in the corpus (E₀ with c_q², the
  step-9 binding m_e·ρ[...] without it) are two different electron normalisations; which one is
  right is decided by deriving 𝔈_e, not by the calibrations.
- `qou-6gf9`: the carrier is CAL-2 itself. Deriving it needs an electron-side object of vanishing
  order 2 relative to the muon side, and an analytic source of Vol(4₁). The 11.5 ppb μ–p residual
  work on this bean is unaffected.

## 6. Not done

- No content block was changed. The Lean is a library file; it has no `.qa.json` sidecar.
- `check-sidecars.sh` reports the authors-note Lean-coverage stats as stale. That is a drift on
  main unrelated to this change, and was not refreshed here.
- The calibrations cannot say which electron unit is canonical; that is still open (§3 item 4).

## 7. How far apart the two units are

Measured by `computations/probes/energy_scale_unit_ratio_probe.py` (mpmath, 70 dps,
witness `energy-scale-unit-ratio.witness.json`, 5/5 checks). The ratio of the mass-formula
unit m_e/ℏ_q² to the trace-pipeline unit m_e/τ_e is R = τ_e/ℏ_q², with
τ_e = q³(q⁴+1)/(q²+1)².

| pin | τ_e | ℏ_q² | R = τ_e/ℏ_q² |
|---|---|---|---|
| proton (default) | 0.691166478358 | 0.00981718645428 | **70.4037232641** |
| muon, CODATA 2022 (comparison) | 0.691166504074 | 0.00981718852772 | 70.4037110138 |

The pin moves R by 1.7e-7 relative. So a weight read in one pipeline and converted with the
other pipeline's unit is off by a factor of about 70. That is the size of the gap a
derivation of w_e has to close. It is not c_q² (82.68) and not E₀/m_e (8.19), so neither of
the two scales already in the corpus is this factor. No measured value enters R except
through q₀.

## 8. Where the factor 70 comes from (added 2026-11-23)

Lean: `QOU/Observations/ElectronUnitSplit.lean`. It is stated over a generic field, sorry-free, and `lean -DautoImplicit=false` exits 0. `#print axioms` shows only `propext`, `Classical.choice` and `Quot.sound`. The probe in §7 now also checks each identity numerically (11/11).

1. **The electron trace is one block.** The ruled electron word σ₀σ₁σ₀ has trace 0 in the
   (2,1) block (`electron_21_trace_zero`), and convention D gives y₍₁³₎ = 0. So
   τ_e = q³·y₍₃₎(q): the framing q³ (writhe 3) times the Ocneanu weight of the one-row block
   (`tau_electron_eq_framing_mul_y3`).
2. **That weight is a classical half plus an order-two remainder.**
   y₍₃₎ = 1/2 + h²/(2[2]²), with h = q − q⁻¹ and [2] = q + q⁻¹ (`y3_split`). The 1/2 is the classical value 2^{c−n}
   (`traceD_one`). The remainder is of order two because y₍₃₎ is bar-invariant (`y3_bar`).
   It equals ℏ_q²·q²(q+1)²/(2(q²+1)²) (`y3_quantum_part_eq`).
3. **So R splits exactly** (`unit_ratio_split`):
   R = τ_e/ℏ_q² = q³/(2ℏ_q²) + q⁵(q+1)²/(2(q²+1)²).
   At the proton pin the first term is 69.6509, the second 0.7528, total 70.4037. Almost all of
   the factor is the classical Hopf value 1/2 divided by ℏ_q². The two pipelines disagree
   because the trace pipeline gives the electron a weight that is finite at q = 1, while the
   mass formula gives it ℏ_q², which vanishes there. The order-two quantum part of the trace is
   the same size as ℏ_q² (ratio 1/2 at q = 1, 0.753·q⁻³ at q₀), but it is not what the trace
   pipeline uses as the electron's weight.

### The gap on the mass-formula side

The ruled electron closes to the Hopf link, which is a torus link of hyperbolic volume 0
(Thurston; the corpus already records this for torus leptons in
`lepton-mass-tower-canonical`). A chart whose weight is Vol·ρ therefore gives the electron the
value 0 for every finite ρ, and cannot match a non-zero CAL-1 (`product_weight_ne`). So the
mass formula's electron weight ℏ_q² is not given by the formula's own rule; it is the CAL-1
placement, made by hand. The trace pipeline's electron weight is the only one in the corpus
that comes from its own rule. This is a structural difference between the two charts. It does
not decide which chart is canonical, because the trace chart has its own gap (next paragraph).

### The gap on the trace side

In the trace chart the muon carrier would need w_μ/w_e = Vol(4₁)/ℏ_q² = 206.77. The
convention-D trace of the standard 3-braid of 4₁, (σ₀σ₁⁻¹)², gives
τ(4₁)/τ_e = 0.4054 at the proton pin (it is 1/2 at q = 1). That is short by a factor of
510, as the pole obstruction of §4 requires. So neither chart derives the muon carrier: the
mass chart builds it in through its unit, and the trace chart cannot reach it with a single trace.

### What is left open

- Which chart is canonical. The mass chart derives the muon and not the electron; the trace chart derives the electron and not the muon. Neither derives both.
- One candidate for joining them: take the electron's mass-chart weight to be the order-two part of its trace, q³·ℏ_q²·q²(q+1)²/(2(q²+1)²). That would replace ℏ_q² by ℏ_q² times a factor that is 1/2 at q = 1. This is an identification, not a derivation. It would also move q₀, because CAL-2 is defined in the mass chart, so it is not adopted here.
