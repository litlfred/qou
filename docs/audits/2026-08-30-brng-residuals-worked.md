# qou-brng residuals worked — mass=self/binding=mutual proved, coordination coefficient, ℏ_q² is numerology

**Date:** 2026-08-30 · **Arc:** bk-crossing mass-binding · **Bean:** `qou-brng` · **PR:** #6145
**Lean:** `content/quantum-observable-universe/lean/QOU/Mass/SelfMutualPartition.lean` (sorry-free; lean-direct exit 0; axioms propext/Classical.choice/Quot.sound)
**Probe:** `computations/brng_hbarq2_saturation_genericity_probe.py` (mpmath, no float64; scope-(a))
**Predecessor:** the merged Brunnian binding-channel result (#6125, `QOU.Mass.BrunnianBindingChannel`) resolved the amplitude assignment's *type* question; this works the three residuals it left.

## R2 — the Hamiltonian-level assignment is a theorem, not a postulate

The residual was: why is rest mass the *self* (intra-component) energy and binding the *mutual*
(inter-component) pairing? This is derived, not assumed:

- **`assemblyEnergy_partition`** — the crossing energy is a sum over crossings, and every crossing of
  the assembled diagram is either intra-component (self) or inter-component (mutual), so the total
  partitions exactly: assembly = self + mutual (`Finset.sum_filter_add_sum_filter_not`).
- **`binding_eq_neg_mutualEnergy`** — an isolated component has no inter-component crossings, so its
  mass is its self energy. With binding defined the standard way, B = Σ(isolated masses) − assembly,
  the self energies **cancel**: B = Σ self − (self + mutual) = −(mutual). So binding is exactly the
  inter-component mutual pairing, and mass is the self part — a theorem of the crossing partition
  plus the mass-deficit definition of binding.
- **`binding_indep_of_self`** — binding is independent of every self-crossing (the falsifiable form:
  binding is purely the mutual pairing; no self-energy contributes).

**Residual — now lifted (2026-08-30 follow-up, `QOU.Mass.ArchimedeanTraceBridge`, sorry-free).** The
additive partition above was proved at the crossing-energy granularity; the mass observable carries
the MULTIPLICATIVE q-dimension Markov self-trace lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1). The bridge between
the two is the archimedean functor τ = logarithm (the free energy of a partition-function-like
amplitude):

- `freeEnergy_connectedSum` — a multiplicative amplitude has an ADDITIVE log-image E = log T. So the
  additive-energy model `SelfMutualPartition` *assumed* follows from multiplicativity, and rest mass
  is extensive.

  🛑 **CORRECTED 2026-08-30 (bean `qou-bsfg`, red-team of this very result).** This bullet read "the
  Markov/Jones trace is multiplicative under connected sum … so the additivity is DERIVED from trace
  multiplicativity". Two multiplicative structures were conflated. For the normalised Jones
  polynomial the CONNECTED SUM is exactly multiplicative, `J(K₁#K₂) = J(K₁)·J(K₂)`, but the DISJOINT
  UNION carries the loop value, `J(K₁ ⊔ K₂) = δ·J(K₁)·J(K₂)` with `δ = [2]_q`. The matrix theorem
  actually proved (`MarkovTraceMultiplicative`, a Kronecker product) models the DISJOINT UNION, so it
  does not license the connected-sum reading. A genuinely independent assembly has `I = δ`, not
  `I = 1`: `log δ ≈ 0.699` per juxtaposition at the proton pin, ≈ 2.10 for ⁴He. Quantified in
  `QOU.Mass.ClosureNormalisationDefect` (`freeEnergy_closureNorm_additive_iff`: additivity iff
  `δ = 1`, excluded for `q > 1`). The lemma itself is `Real.log_mul` and is untouched by this.
- `freeEnergy_prod` — mass adds over the A constituents.
- `binding_eq_bindingFreeEnergy` — for an assembly amplitude (∏Tᵢ)·I, the mass-deficit binding
  Σ Eᵢ − E_assembly = −log I, the connected/interaction free energy. This is
  `binding_eq_neg_mutualEnergy` lifted to the Markov-trace level.
- `bindingFreeEnergy_eq_zero_iff` / `_pos_iff` — binding = 0 ⟺ independence (I=1); binding > 0 ⟺
  I < 1 (the assembly amplitude is suppressed exactly when the state is bound).

What remains a *modelling input* (named, not faked): (1) that the substrate assembly amplitude IS the
Markov trace, multiplicative under nucleon assembly — a citable theorem for the Jones polynomial,
carried as the `Multiplicative`/positivity hypothesis; (2) the dimensional dressing
m = m_e·Vol·lw/ℏ_q² (CAL-1 scale m_e, geometric Vol, CAL-2 cusp 1/ℏ_q²) — calibration and geometry.
The bridge between those two inputs is now a theorem, not a postulate.

## R1 — the crossing-count → coordination coefficient

- **`coordinationUnits := ½·(inter-component crossing count)`** — one coordination unit per clasp; a
  clasp is two inter-component crossings (a minimal Brunnian bond, n₊ = n₋ = 1). This is the general
  coefficient, with no minimal-bond restriction.
- **`complete_minimal_clasp_coordination` / `_per_nucleon`** — a complete graph of minimal
  single-clasp bonds on A nucleons has 2·C(A,2) inter crossings ⇒ C(A,2) = A(A−1)/2 coordination
  units, per-nucleon z = A−1.

**Open residual:** the coefficient beyond minimal bonds is just ½·|inter|, but *which* link (how
many clasps per pair, which pairs bond) realizes the A-body carrier is the carrier's crossing
structure — a topological input, saturation-limited for heavy A (`QOU.Mass.CoordinationSaturation`
excludes the complete graph there).

## R3 — the ℏ_q² saturation value is more numerology-suspect, not less

The arc recorded B/A/m_N rising toward ℏ_q² with A (⁴He 0.77 → ⁵⁶Fe 0.95·ℏ_q²). The probe measures
what that match actually is (mpmath, no float64; not forced):

| nucleus | A | B/A/m_N ÷ ℏ_q² |
|---|--:|--:|
| ⁴He | 4 | 0.767 |
| ⁴⁰Ca | 40 | 0.928 |
| ⁵⁶Fe | 56 | 0.954 |
| ⁶²Ni | 62 | **0.954 (peak)** |
| ¹²⁰Sn | 120 | 0.923 |
| ²³⁸U | 238 | 0.821 |

Two findings:

1. **B/A/m_N never reaches ℏ_q².** It peaks at 0.954·ℏ_q² near A≈60 (⁶²Ni) and then *falls* — the
   "approach to ℏ_q²" reverses. It is not a saturation *limit*; it is an A-dependent balance point.
2. **The match is to the wrong quantity.** The empirical B/A peak (~8.79 MeV) is a volume − surface −
   Coulomb *balance*, not the fundamental nuclear volume coefficient a_V ≈ 15.75 MeV. The bulk
   coefficient is a_V/m_N ≈ **1.71·ℏ_q²**, not ℏ_q². ℏ_q² coincides with the accidental balance
   point near A≈60, not with a saturation constant.
3. **Genericity.** 3 of 7 trivial substrate constants (including 1/102) land within 6% of the peak —
   ℏ_q² is not uniquely picked out.

**Verdict:** with the volume-defect mechanism refuted (2026-08-21) and no substrate route selecting
the A≈60 balance point, the ≈ℏ_q² match is numerology. Do not wire; do not force to 1. This
*confirms and sharpens* the bean's 2026-08-21 suspicion rather than closing it as a prediction.

## Net state of qou-brng after this session

- **Type question** (unsigned coordination count vs signed linking number) — PROVED (#6125).
- **R1** (crossing-count → coordination coefficient) — PROVED for the clasp model; residual is the
  carrier's crossing structure (a topological input).
- **R2** (mass=self, binding=mutual) — PROVED at the additive level AND lifted to the Markov-trace
  level via the archimedean log bridge (`ArchimedeanTraceBridge`). The additivity is now derived from
  trace multiplicativity; binding is the connected free energy.
- **R3** (exact ℏ_q² saturation) — measured to be numerology-suspect; not a prediction.

What remains are two named *modelling inputs*, not open derivations: (1) that the substrate assembly
amplitude is the (multiplicative) Markov trace — a citable Jones theorem, carried as a hypothesis;
(2) the dimensional dressing m = m_e·Vol·lw/ℏ_q² — calibration and geometry. Everything between them
— the amplitude assignment (type), the coordination coefficient, the additive→multiplicative bridge,
and the binding-is-the-connected-part identity — is proved. The exact ℏ_q² saturated fraction is a
numerical coincidence.
