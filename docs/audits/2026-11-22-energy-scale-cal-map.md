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
   the same size as ℏ_q² (ratio 1/2 at q = 1, 0.7528 at q₀), but it is not what the trace
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

## 9. One object for both electron and muon (owner choice 2026-11-23)

The owner chose to look for one derived weight that gives the electron a finite value and the muon
Vol(4₁)/ℏ_q². Lean: `QOU/Observations/QVolumeCarrier.lean`, sorry-free under
`lean -DautoImplicit=false`, axioms `propext`, `Classical.choice` and `Quot.sound` only. Probe:
`computations/probes/q_volume_carrier_probe.py`, mpmath 70 dps, 6/6 checks, proton pin
default and muon pin as a comparison arm. Precision gates: none of the red ratchets names the
probe, and they are the same reds as on main.

### A q-volume derives the muon's Vol/ℏ_q² shape

Take G(z; q) = Σ_{n≥1} zⁿ/(1 − q⁻ⁿ)², summed over the ideal tetrahedra of the knot complement.
The denominator factors exactly as 1 − q⁻ⁿ = ℏ_q·[n]′, with [n]′ = Σ_{k<n} q⁻ᵏ
(`one_sub_inv_pow_eq`). So ℏ_q²·G → Li₂(z) as q → 1. The figure-eight is two regular
tetrahedra of shape e^{iπ/3}, and it gives

  W_μ = 2 Im G(e^{iπ/3}; q) ~ Vol(4₁)/ℏ_q².

This gives a reason why the carrier uses ℏ_q = 1 − q⁻¹ rather than log q or (q − q⁻¹)/2: ℏ_q is the
factor of 1 − q⁻ⁿ. At |z| = 1 the n-series does not converge at finite q. The probe uses the
exact rearrangement Σ_{m≥0}(m+1)·z q⁻ᵐ/(1 − z q⁻ᵐ), which converges absolutely. It checks the
rearrangement against the direct series at |z| < 1, and it checks the q₀ value by direct summation
to 10⁻⁵⁵.

| at the proton pin | value |
|---|---|
| V_q = ℏ_q²·W_μ | 2.034559016 (Vol(4₁) = 2.029883213, +0.230 %) |
| same with log q in place of ℏ_q | +11.15 % |
| same with (q − q⁻¹)/2 | +11.56 % |
| W_μ = 2 Im G | 207.2446139 |
| Vol(4₁)/ℏ_q² (the carrier) | 206.7683264 |
| W_μ against CODATA m_μ/m_e | +0.2304 % |

The approach to Vol is linear in ℏ_q: the relative gap is 3.07e-4 at q = 1.01 and 3.17e-5 at
q = 1.001.

So this object gives the carrier's shape exactly as q → 1 and a definite correction at q₀. At q₀ the
correction is +0.23 %, which is the kind of correction bean `qou-6gf9` asks for. It is not a fit:
nothing in G was chosen against m_μ/m_e. It is still not adopted. CAL-2 defines q₀ through the
carrier, so using W_μ in its place would re-solve q₀, and that is an owner decision.

### But it gives the electron 0

The ruled electron closes to the Hopf link, which has no ideal tetrahedra, so its q-volume is the
empty sum 0. This is the same gap as the mass formula (§8).

### The sum family does not close it

The obvious joint object is W = T + c·G: trace plus q-volume. Its leading carrier is
c·Vol/(T_e(1)·ℏ_q²) (`sum_family_leading`), so the carrier forces c = T_e(1) = 1/2
(`sum_family_forces_c`). That is a necessary condition; neither family produces c. With
c = 1/2 the full ratio at q₀ is

  (τ(4₁) + G_μ/2)/τ_e = (0.2802 + 103.62)/0.6912 = 150.33,

which is −27.3 % from 206.77. The miss is not small, and its source is visible: c is fixed at
q = 1, where τ_e = 1/2, while τ_e(q₀) = 0.6912. This is a scope-(a) negative. The simplest sum,
with the only coefficient the leading order allows, does not reproduce the carrier at q₀. It does
not exclude a sum with a derived q-dependent coefficient.

### What is still open

No single derived object gives both particles. The q-volume gives the muon and misses the electron;
the trace gives the electron and misses the muon. A joint object needs a derived reason for the
relative weight of its trace part and its volume part. Here that weight is forced only at q = 1.

## 10. Is there a canonical Hecke or trace chart for the muon? (added 2026-11-27)

Bean `qou-91w7`, open item "canonical chart". Lean:
`QOU/Transcendental/MassTheory/MuonCarrierHeckeObstruction.lean` (sorry-free; `#print axioms`
gives only `propext`, `Classical.choice`, `Quot.sound`; behind the transcendental boundary because
it uses limits). Probe: `computations/probes/muon_carrier_hecke_probe.py` (5/5, proton pin, nothing
fitted). Short answer: **no finite Hecke chart can be shown to carry the muon, and the one
canonical infinite reading found is off by the electron's writhe.** Three findings.

### 10.1 Finite Hecke charts: a rationality obstruction (structural, scope (b) relative to an open problem)

Every convention-D or HOMFLY-normalised Markov trace of a word in H_n(q) is an element of ℚ(q):
the Ocneanu weights, the seminormal matrices and the HOMFLY unknot factor δ all have entries in
ℚ(q). So is every finite sum, product or quotient of such traces, at any braid index. The Lean
proves (`rational_chart_leading_coeff`, and `_hbar` for ℏ_q = 1 − q⁻¹): if f = P/Q with
P, Q ∈ K[X] and ℏ_q²·f(q) → V ≠ 0 as q → 1, then V ∈ K. The proof factors out the root at 1 from
P and Q and compares orders; no numerics enter.

Consequence: a finite Hecke chart with rational structure constants whose weight ratio behaves
like Vol(4₁)/ℏ_q² would prove Vol(4₁) ∈ ℚ; with algebraic constants, Vol(4₁) algebraic. Both are
open (Vol(4₁) = 6·Λ(π/3) is a rational multiple of √3·L(χ₋₃, 2), whose irrationality is not
known) and are believed false. So this is not an unconditional exclusion. It says that any such
chart would settle an open problem in number theory, and it explains audit §8's "510× short":
the single trace τ(4₁)/τ_e is finite at q = 1, and no finite combination can do better unless
Vol(4₁) is rational. The volume can only enter through an infinite sum or a limit.

### 10.2 The canonical infinite object: the q-volume is the ℏ-derivative of the quantum dilogarithm

The Hecke-side source of hyperbolic volume is the quantum dilogarithm
P(z; q) = ∏_{k≥0}(1 − z q⁻ᵏ). Kashaev and colored-Jones state sums of 4₁ are built from its
factors, and log P ~ −Li₂(z)/ℏ_q: the volume sits at order 1/ℏ, in the exponent. The probe
confirms this for the Kashaev invariant: d log⟨4₁⟩_N/dN → Vol(4₁)/2π (1.016 at N = 200 → 400,
the residue being the known (3/2) log N term).

The order-two carrier appears canonically as the q-log-derivative of this object:

  G(z; q) = (q ∂_q log P)(zq; q),

termwise exact in Lean (`qvolume_term_log_deriv`) and checked to 10⁻⁶⁹ at q₀ for the full sum.
This explains §9's q-volume G: it is not an ad hoc series but the "energy" w = q ∂_q log Z of the
quantum dilogarithm, and it is why ℏ_q = 1 − q⁻¹ and not log q.

### 10.3 But the same reading puts the electron at its writhe (scope (a) negative)

Applied to the electron's own trace τ_e = q³(q⁴+1)/(q²+1)², the same reading gives
q ∂_q log τ_e → 3 at q = 1 (`tau_electron_log_deriv_at_one`: τ_e(1) = 1/2, τ_e'(1) = 3/2). The 3
is the writhe of σ₀σ₁σ₀; the Ocneanu factor y₍₃₎ is bar-invariant and contributes 0. Then the
carrier of this reading is ℏ²·w_μ/w_e → Vol/3, not Vol (`energy_reading_ne_carrier`). At q₀ the
ratio w_μ/w_e = 64.69, which is 0.313 of the carrier 206.77. Without framing, the electron's energy
weight vanishes at q = 1 and the pole order becomes 3. Dividing by the writhe to recover Vol would
be a fit and is not done.

This is a scope-(a) negative: the energy reading, applied uniformly to both particles, does not
give the carrier. It does not exclude a reading that weighs the electron differently for a derived
reason.

### 10.4 What this leaves open

- The carrier's ℏ_q-shape and the role of G are now explained (10.2). The coefficient is not: the
  natural uniform reading gives 1/3 (10.3), and §9's sum family needs the unexplained c = 1/2.
  Both are statements about the electron's weight, so the open item narrows again to "derive 𝔈_e",
  as §5 already said.
- A canonical chart, if one exists, has to be transcendental (10.1). It belongs in
  `QOU/Transcendental/`, and it cannot be a finite Hecke trace without settling the irrationality
  of L(χ₋₃, 2).
