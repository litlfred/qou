# The κ closure via the continuum categorical EM: `split = (3/5)·α·ΔZ(Z−1)·m_π/A^{1/3}` — scaling matched across A=3–39 at coefficient 0.985 ± 0.069 with zero fitted constants; PARTIAL (the pion-Compton packing radius is a selection, not a derivation)

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FINDING (reproducible, no fit). The R2-c attack on the honest open
object of [`binding-scale-is-hyperbolic-volume.md` §3](../coordination/binding-scale-is-hyperbolic-volume.md)
("derive `~0.84·α·Z(Z−1)/R(A)` from the categorical EM — α_EM + a derived
radius law"), superseding both the A=3-only fixed κ = 1/3
([`2026-07-13-mirror-split-s3-em-functional-attempt.md`](2026-07-13-mirror-split-s3-em-functional-attempt.md))
and the A-independent pairwise `tanh(ln q₀)` route.

Probe: [`computations/deltalambda/mirror_split_continuum_em_probe.py`](../../computations/deltalambda/mirror_split_continuum_em_probe.py)
(witness [`mirror-split-continuum-em.witness.json`](../../computations/deltalambda/mirror-split-continuum-em.witness.json),
5/5 assertions pass, mpmath at the production floor, exit 0).

## The construction

The mirror-split systematics benchmark
([`2026-07-11-mirror-nuclei-coulomb-systematics.md`](2026-07-11-mirror-nuclei-coulomb-systematics.md)):
`split/ΔE_C = 0.838 ± 0.059` against the canonical uniform-sphere Coulomb with
the **empirical** `r₀ = 1.2 fm`. The R2-c question: can every factor be a
framework object? Writing the radius law with the **pion Compton wavelength**
(CAL-3 — an existing calibration input, no fourth calibration) as the packing
unit, `R(A) = λ̄_π·A^{1/3}` with `λ̄_π = ℏ/(m_π c) = 1.41382 fm`, the inverse
length is `ℏc/R(A) = m_π/A^{1/3}` — **no empirical length constant survives**:

$$ \mathrm{split}_{\rm pred}(A, Z_{\rm lo}, Z_{\rm hi}) \;=\; \tfrac{3}{5}\,\alpha_{EM}\,\bigl[Z_{\rm hi}(Z_{\rm hi}{-}1) - Z_{\rm lo}(Z_{\rm lo}{-}1)\bigr]\,\frac{m_\pi}{A^{1/3}} \quad \text{(MeV, zero fitted constants).} $$

## Decomposition table (factor → corpus source → tier)

| factor | corpus source | tier |
|---|---|---|
| `α_EM` | [`prop:alpha-em-categorical-trace-ratio`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-categorical-trace-ratio.md): bare `α = 1/(q₀[9]_q[10]_q)` = 1/136.823 (−0.155% vs CODATA; the archimedean `+2/(3π)` → −4.2 ppm is partially open, [`alpha-em-derivation-open-problems`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md)) | **derived** (bare); the 0.155% is asserted insensitive vs the 7% scatter |
| charge pair count `ΔZ(Z−1)/2` | exact discrete-proton combinatorics — the general-A orbit form of the S₃-functional D1 (**S2-closed** machinery of [`2026-07-13-mirror-split-s3-em-functional-attempt.md`](2026-07-13-mirror-split-s3-em-functional-attempt.md)): the charge bilinear `Σ_{i<j} q_iq_j` on Z unit protons is `C(Z,2)` exactly; for a T_z mirror the difference is exactly `Z_lo` (probe-verified in exact ints) | **exact** |
| `m_π` (the inverse-length unit) | CAL-3, `M_PI_PM_MEV_VALIDATION` (three-calibration discipline; the orthogonal meson class) | **calibration input** (permitted; not a fourth calibration) |
| `A^{1/3}` scaling | volume extensivity: the derived log-trace bond sum `B = Σ_bonds ε` ([#2089](2026-06-10-binding-bond-graph-compute-audit-and-derivation.md)) + Lean-proved chain multiplicity `M_n = n−1` (`QOU/Mass/LinearChainBondCount.lean`) + the ledger identification `B = m_e·Vol` make the categorical volume **extensive**, `Vol ∝ A`; fixed volume per nucleon ⇒ `R ∝ Vol^{1/3} ∝ A^{1/3}`. **Named weak step:** the hyperbolic volume of the link complement is a topological invariant, *not* a Euclidean spatial volume — "spatial nuclear volume ∝ categorical Vol" is an archimedean identification the corpus does not derive (and the ⁴He single-volume `Vol₄` reading is already NEGATIVE, `vol4_4he_snappy_falsification_probe`). | **conditional / partial** |
| `3/5` | classical uniform-sphere electrostatic self-energy (Euclidean, archimedean-side; standard, not fitted to these data) | **model assumption**, flagged — not categorical |
| packing coefficient (`R = 1·λ̄_π·A^{1/3}`) | **not derived.** Selected among the framework's four mass scales — required coefficients: m_e → 269.1, m_μ → 1.301, **m_π → 0.985**, m_p → 0.147. Selection entropy 2 bits; the pion is also the a-priori standard Yukawa-range scale. | **underived selection** — the single remaining gap |

## Probe numbers (8 T_z mirror pairs; nothing tuned)

| pair | A | split_AME | pred | **ratio** | (r₀=1.2 benchmark ratio) |
|---|--:|--:|--:|--:|--:|
| ³H/³He | 3 | 0.764 | 0.849 | 0.900 | 0.765 |
| ⁷Li/⁷Be | 7 | 1.644 | 1.920 | 0.857 | 0.728 |
| ¹¹B/¹¹C | 11 | 2.764 | 2.752 | 1.004 | 0.854 |
| ¹³C/¹³N | 13 | 3.003 | 3.124 | 0.961 | 0.817 |
| ¹⁵N/¹⁵O | 15 | 3.537 | 3.474 | 1.018 | 0.865 |
| ²³Na/²³Mg | 23 | 4.839 | 4.735 | 1.022 | 0.869 |
| ²⁷Al/²⁷Si | 27 | 5.595 | 5.304 | 1.055 | 0.897 |
| ³⁹K/³⁹Ca | 39 | 7.307 | 6.858 | 1.065 | 0.906 |

**`split_AME/split_pred = 0.985 ± 0.069`** (7% scatter, same as the benchmark —
the data are the same, algebraically rescaled by `(r₀/λ̄_π)·(α_der/α_CODATA)`;
consistency with the canonical `coulomb_energy` path probe-verified). The
content beyond the systematics audit is: **(i)** every factor now traces to a
framework object with an honest tier (table above) — in particular the
`0.84` benchmark coefficient is revealed to be `r₀/λ̄_π` in disguise: with the
CAL-3 length the predicted coefficient is **1** and measures **0.985**;
**(ii)** the supersession is quantified (below). The residual mild A-trend
(ratio 0.90 → 1.07, monotone) is the known light-nucleus deviation from
`R ∝ A^{1/3}` — flagged, not modeled.

## Supersession (the scaling criterion — the thing fixed-1/3 failed)

| candidate | A-dependence | ³H/³He | ⁷Li/⁷Be | ³⁹K/³⁹Ca |
|---|---|--:|--:|--:|
| **continuum EM (this)** | `Z(Z−1)/A^{1/3}` | 0.900 | **0.857** | 1.065 |
| fixed κ = 1/3 (`B_pp/3`) | none | 1.002 | **2.16×** | 9.59× |
| pairwise `tanh(ln q₀)·B_pp` | none | 3.21× | 6.92× | 30.7× |

The fixed 1/3 is a single-point A=3 coincidence (as the S3-attempt's
calibration constraint required); the derived pairwise tanh has the right
provenance but no A-scaling and the wrong magnitude everywhere. The continuum
EM object is within 15% at **every** pair. Per the S3-attempt's own criterion
("a κ closure that only reproduces the A=3 point is single-point and fails the
corpus calibration"), the L6a4-specific κ = 1/3 reading survives only as the
A=3 evaluation of this continuum object — at A=3 the continuum form gives
0.849 MeV (ratio 0.900), consistent with, and now superseding, both routes.

## Guarded near-matches (NOT used, NOT wired — numerology quarantine)

- With the **electron** Compton length as unit, the required coefficient is
  ≈ 269–324 depending on convention; `1/ℏ_q^{5/2} ≈ 323.8` sits within ~1% of
  the `λ̄_e/r₀` variant. Half-integer power, no structural reason, huge q₀
  expression entropy — **guarded, do not revive**.
- `r₀/λ̄_π = 0.849` vs the benchmark 0.838: this is the identity that makes the
  coefficient land at ≈1; it is *why* the construction works numerically, not
  an extra coincidence.

## Classification (anti-fit discipline, STRICT)

**(ii) PARTIAL.** Scope-(a) phrasing throughout.

- **Scaling: matched, by derived/exact factors.** The `Z(Z−1)` charge
  combinatorics is exact (S2-closed orbit counting at general A); α_EM is
  derived (bare, −0.155%); the `A^{1/3}` follows from volume extensivity
  *conditionally* (weak step: the hyperbolic→Euclidean volume identification,
  named above). RMS/mean = 7% < 15% across A=3–39 — the success criterion the
  fixed 1/3 fails.
- **Normalization: coefficient 0.985 with zero fitted constants — but only
  under two underived inputs:** the packing identification
  `R = 1·λ̄_π·A^{1/3}` (a 2-bit selection among the framework's mass scales,
  physically the Yukawa range — *not* derived from the categorical EM) and the
  uniform-sphere `3/5` (classical model geometry). Per the task's rule: the one
  overall constant is not *fitted* (it is predicted 1 by the selection and
  measured 0.985), but the selection itself is underived ⇒ **PARTIAL**, not
  derived.
- Nothing tuned per-pair; nothing tuned at all. Not derived ⇒ not wired: no
  production change, no tier change, no content-block edit.

## What would close it (for the next agent)

1. **Derive the packing radius**: show from the categorical EM / substrate
   that the per-nucleon Euclidean packing volume is the pion-Compton ball at
   coefficient 1 — equivalently derive the Yukawa-range identification
   `R_unit = ℏ/(m_π c)` from the CAL-3 meson class (the framework already owns
   `m_π`; what is missing is why *it* is the EM-relevant length, and why
   coefficient exactly 1 rather than the 0.985 ± 0.069 measured).
2. **Derive the volume→radius step**: an archimedean-functor statement mapping
   the extensive categorical `Vol ∝ A` (bond-count law, Lean-proved
   multiplicity) to Euclidean spatial volume — the named weak step. The ⁴He
   `Vol₄` NEGATIVE result bounds naive per-A volume identifications.
3. **Replace the `3/5`**: the uniform-sphere factor should emerge from the
   framework's charge distribution (the same object whose deviation from
   uniform-sphere explains the residual A-trend 0.90 → 1.07 and the
   Nolen–Schiffer ~0.07 MeV strong-CSB signal).

## Files

- probe: [`computations/deltalambda/mirror_split_continuum_em_probe.py`](../../computations/deltalambda/mirror_split_continuum_em_probe.py) (new)
- witness: [`computations/deltalambda/mirror-split-continuum-em.witness.json`](../../computations/deltalambda/mirror-split-continuum-em.witness.json) (new, audit-only, 5/5 pass)
- this audit: `docs/audits/2026-07-13-mirror-split-continuum-em-derivation-attempt.md`
- context consumed (unchanged):
  [`2026-07-11-mirror-nuclei-coulomb-systematics.md`](2026-07-11-mirror-nuclei-coulomb-systematics.md),
  [`2026-07-11-mirror-split-coulomb-diagnosis.md`](2026-07-11-mirror-split-coulomb-diagnosis.md),
  [`2026-07-13-mirror-split-s3-em-functional-attempt.md`](2026-07-13-mirror-split-s3-em-functional-attempt.md),
  [`2026-07-11-bond-extensivity-equal-weight-coordination.md`](2026-07-11-bond-extensivity-equal-weight-coordination.md),
  [`2026-06-10-alpha-em-legacy-empirical-forms.md`](2026-06-10-alpha-em-legacy-empirical-forms.md),
  [`binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md),
  [`computations/mirror_nuclei_coulomb_systematics.py`](../../computations/mirror_nuclei_coulomb_systematics.py),
  [`computations/coulomb_energy.py`](../../computations/coulomb_energy.py)
