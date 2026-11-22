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
- No number was computed. The value of 𝔈_e(q₀)/ℏ_{q₀}² (the ratio of the two units) is a
  straightforward probe and is the natural next measurement.
