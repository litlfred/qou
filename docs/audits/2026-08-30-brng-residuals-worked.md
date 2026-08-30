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

**Open residual (stated, not hidden):** this proves the assignment at the additive crossing-energy
granularity. Lifting it to the substrate *mass observable* — where the self energy closes to the
q-dimension self-trace lw = (Σ_{λ⊢c+1} dim_q λ)/(c+1) and the archimedean dressing is
m = m_e·Vol·lw/ℏ_q² — is the remaining modelling step. It is a named identification (mass observable
= closed self-trace), not a fit; but it is not proved here.

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
- **R2** (mass=self, binding=mutual) — PROVED at the additive-energy level; residual is the
  mass-observable ↔ crossing-energy identification at Markov-trace granularity.
- **R3** (exact ℏ_q² saturation) — measured to be numerology-suspect; not a prediction.

The surviving genuinely-open item is the single modelling identification in R2 (mass observable =
closed self-trace at the archimedean boundary). Everything else is either proved or shown to be a
topological input / a numerical coincidence.
