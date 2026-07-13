# The two underived steps of the continuum-EM mirror split: the pion packing radius (GAP 1 — scale-class now derived, coefficient open) and the volume→radius identification (GAP 2 — re-scoped to an energy exponent; cusp route partial)

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FINDING (reproducible, no fit, nothing wired). R2-e, owner-directed —
the derive-or-refute attack on the two gaps named by the parent audit
[`2026-07-13-mirror-split-continuum-em-derivation-attempt.md`](2026-07-13-mirror-split-continuum-em-derivation-attempt.md)
§"What would close it" items 1–2.

Probe: [`computations/deltalambda/pion_radius_and_cusp_volume_gap_probe.py`](../../computations/deltalambda/pion_radius_and_cusp_volume_gap_probe.py)
(witness [`pion-radius-and-cusp-volume-gaps.witness.json`](../../computations/deltalambda/pion-radius-and-cusp-volume-gaps.witness.json),
10/10 assertions pass, exit 0; `--live` re-verifies every baked cusp datum
against SnapPy 3.3.2). Corpus-grep run before declaring anything open
(`yukawa|compton|confinement length|meson range|pion exchange` over
`docs/audits/ content/ computations/`): no prior meson-range/packing-radius
derivation exists; the cusp-geometry lever was previously probed only for the
*asymmetry* question
([`2026-07-04-em-linking-cusp-geometry-excluded.md`](2026-07-04-em-linking-cusp-geometry-excluded.md)),
leaving the *symmetric packing* use unexamined.

## GAP 1 — the Yukawa packing radius `R_unit = λ̄_π` at coefficient 1

### Candidate table

| candidate | structural content | verdict |
|---|---|---|
| **(a) CAL-3 class selection** (W-plane annihilation on the bond channel) | (a1) the inter-nucleon bond of the bond-count law is a 2-body sub-link = **Hopf**, `Vol(Hopf) = 0` (geometric fact — [`binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md) ledger row; SnapPy-verified non-hyperbolic). (a2) The W-plane calibrations enter per-link binding only through `m_e·Vol(K)` (ledger identification) and the **dimensionless** modulus q₀ — so on the bond channel the W-plane contribution is `m_e·Vol(Hopf) = 0` **identically**. (a3) CAL-3 is corpus-defined as *exactly* "the `Vol(Hopf)=0` meson scale (independent of m_e, q₀)" ([`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md) §table); the meson binding channel is "Hopf link binding" ([`frobenius-lepton-meson-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/frobenius-lepton-meson-bridge.md)); the mass functional `𝔪 = m_e^a·m_π^c·Q(q₀)` has `c = 0` in the baryon sector, so m_μ and m_p are W-plane (`a=1, c=0`) objects. **Composition:** the unique calibration class with nonzero support on the Vol = 0 bond channel is CAL-3 ⇒ the bond length unit is `ℏc/(m_π·Q(q₀))`, `Q ∈ ℚ(q₀)`. | **PARTIAL — the strongest result of this audit.** The parent's "2-bit selection among 4 mass scales" collapses to a **0-bit class selection**: the same topological object (the Vol=0 Hopf 2-body class) independently characterises the CAL-3 calibration and the inter-nucleon bond, which is the categorical face of the Yukawa-range insight. **Conditional** on the `B = m_e·Vol` ledger identification (per-link volume-conjecture instances) — the same conditionality GAP 2 rides on. Assembled from corpus identifications; **not a Lean-proved theorem** (candidate formalization below). Does **not** fix the coefficient (see (c)). |
| **(b) 2-body channel energy → length** | deuteron energies: `ℏc/B_D` (B_D = 2.2246 MeV AME) = 88.7 fm = 62.7×λ̄_π; `ℏc/μ₀` (derived per-crossing scale μ₀ = m_e/(3(q₀−q₀⁻¹)/2) = 1.6295 MeV) = 121.1 fm = 85.7×λ̄_π | **NEGATIVE, scope-(a).** 2-body channel *energies* are binding scales, not range scales; their Compton inversions miss λ̄_π by 60–90×. This construction, alone, does not produce the packing length. |
| **(c) coefficient-1 status** (the 1-vs-0.985 confrontation, demanded head-on by the task) | measured coefficient 0.985 ± 0.069 (recomputed via the parent's exact code path). Discrimination table over 9 pre-named simple `Q(q₀)` (1, q₀, 1/q₀, √q₀, 1/√q₀, [2]_q/2, (1+1/q₀)/2, 1±ℏ_q²) | **coefficient 1 is CONSISTENT (0.21σ) but NOT SELECTED.** 8/9 candidates sit within 1.25σ (only `q₀` itself, at 1.80σ, is disfavoured); the nearest rival to 1 (`1−ℏ_q²`, at **0.07σ**) differs by Δ = 0.0054 — separating them at 3σ needs ≤ 0.18% scatter, **39× better** than the current 7% systematics. The honest statement: *coefficient = 1 within the model's own uncertainty band, with the band far too wide to certify "exactly 1"*. "One CAL-3 quantum per bond" is a minimality reading, not a derivation. The measured ratio's A-trend (0.900 → 1.065, broadly increasing though not strictly monotone — 0.857 at A=7) is the known light-A `A^{1/3}` deviation, unmodeled. |

**GAP 1 classification: PARTIAL, substantially narrowed.** The *scale class*
(why m_π and not m_e/m_μ/m_p — the required coefficients being 269.1 / 1.301 /
**0.985** / 0.147, recomputed) is now carried by a structural argument with a
falsifiable content (any inter-nucleon length must be `m_π·Q(q₀)`-valued; the
W-plane alternatives are excluded by the identically-vanishing `m_e·Vol(Hopf)`,
not by the numbers). The *coefficient* `Q(q₀) = 1` remains **underived** and is
**undiscriminable** at the current scatter. Anti-fit: every candidate value in
the tables is pinned in advance by a named structural object; no scan, no
post-hoc selection; consistent with the [`2026-05-31 CAL-3 = m_π corroboration`](2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md)
negative-derivability result (m_π is not an (m_e, q₀) expression — best miss
19,938 ppm — which is exactly what the orthogonal-class argument requires).

## GAP 2 — hyperbolic complement volume → Euclidean radius

### Candidate table

| candidate | structural content | verdict |
|---|---|---|
| **(d) archimedean-functor transport** | the functor-taxonomy audit ([`2026-07-11-archimedean-functor-taxonomy.md`](2026-07-11-archimedean-functor-taxonomy.md)) demotes every "archimedean functor" to an evaluation / ring hom into ℝ — there is **no** categorical volume→length transport in the corpus; every corpus length is a Compton inversion `ℏc/mass` | **NEGATIVE as a transport — but yields the useful RE-SCOPING.** `R = λ̄_π·A^{1/3}` is algebraically identical (probe-verified to 40 digits) to the pure-MeV statement `E_pack(A) = m_π·A^{−1/3}`. The "Euclidean radius" never needs to exist as a categorical object: the honest residual gap is the **`A^{−1/3}` energy exponent** — a statement inside the calibration discipline (`m_π^1 ×` a per-isotope combinatorial factor), not a geometry-type transport. This is the correct restatement of GAP 2 for the next attack. |
| **(e) cusp geometry** (maximal-cusp volumes; the route the task flagged as strongest) | SnapPy 3.3.2 (baked + `--live`): cusp cross-sections are genuinely **Euclidean tori** (horosphere geometry — theorem), so a cusp-based packing volume removes the "hyperbolic behaves like Euclidean" category error. Measured (unbiased maximal-cusp policy, volume = area/2): Borromean **per-cusp volume = 2 exactly** (area exactly 4); figure-8 √3 (density 0.853); 8₁₁ 5.007 (density 0.604); L8a21 4×√3; L6a5 3×√7/2 | **PARTIAL, negative-leaning.** What cusp-volume extensivity *requires*, tested: **(i) cusp count ∝ A — FAILS on the corpus's own links**: ³H = 8₁₁ is a *knot* (1 cusp for A = 3) while ³He = L6a4 has 3 — scope-(a), tied to the corpus's link identifications; a canonical A-component nuclear link family (the SDP knot-ID route) could restore it. **(ii)** per-nucleon maximal-cusp volume varies 1.32–2.01 (±20%) and cusp density 0.604–0.853 (×1.41) across the family — cusp volume is **not more uniformly extensive** than complement volume. **(iii)** face-value coefficients (no post-hoc normalization choice): per-nucleon cusp volume 2.0·λ̄_π³ ⇒ radius coefficient 0.782 (**2.9σ low**); whole-𝓑₃ cusp volume 6.0·λ̄_π³ ⇒ 1.127 (**2.0σ high**; 1.4σ in ratio-space); the measured coefficient needs 4.38·λ̄_π³ per nucleon — between the two pinned readings, matching neither. Selecting a normalization post-hoc to land on 1 would be the PSLQ-coincidence antipattern and was not done. |

**GAP 2 classification: OPEN, re-scoped.** The named weak step survives both
candidates, but its shape changed: per (d) the framework does not owe a
volume→length *functor* — it owes the **`A^{−1/3}` scaling of a CAL-3-class
energy**, which is a derivable-looking combinatorial statement (per-bond meson
energy diluted by an extensive object) rather than a geometry-type
identification. The cusp route contributes the one genuinely Euclidean object
in the corpus's geometry (flat cusp tori, with the striking exact per-cusp
volume 2 for the Borromean) but, at face value, neither closes the coefficient
nor improves extensivity; it is the natural *carrier* for a future derivation
if the canonical A-component link family lands.

## Probe numbers (nothing tuned)

- Measured packing coefficient (8 T_z mirror pairs, parent code path):
  **0.985 ± 0.069**; |1 − mean|/rms = **0.21σ**.
- Scale-selection coefficients: m_e → 269.104, m_μ → 1.301, **m_π → 0.985**,
  m_p → 0.147 (m_π the unique scale within ±25% of 1 *and* the unique
  non-W-plane class).
- `Q(q₀)` discrimination: 8/9 within 1.25σ; nearest rival `1−ℏ_q²` at 0.07σ;
  3σ discrimination needs ≤ 0.18% scatter (39× better than current).
- 2-body lengths: `ℏc/B_D` = 88.70 fm (62.7×λ̄_π), `ℏc/μ₀` = 121.10 fm
  (85.7×λ̄_π), vs λ̄_π = 1.4138 fm.
- Cusp geometry (SnapPy 3.3.2): L6a4 3 cusps × vol 2.000 (exact), density
  0.819; 8₁₁ 1 cusp, vol 5.007, density 0.604; 4₁ √3, density 0.853; L8a21
  4 × √3, density 0.683; L6a5 3 × 1.323, density 0.744. Density spread ×1.41.
- Face-value radius coefficients: 0.782 (per-cusp) / 1.127 (whole-𝓑₃) vs
  measured 0.985 — misses 2.9σ / 2.0σ (coefficient-space).

## What would close each gap next

**GAP 1 (coefficient):**
1. **Formalize the class-selection argument** (formalize-first §3.3): a small
   conditional Lean lemma — given (i) `Vol(Hopf) = 0`, (ii) the ledger class
   `B = m_e·Vol`, (iii) the 3-class exhaustiveness
   (`QOU.Mass.calibrations_eq_cohomology`), the bond channel's scale factors
   through the CAL-3 class. This would upgrade (a) from
   corpus-identification-composition to a §3b-cond conditional result.
2. **Derive `Q(q₀) = 1`** as a quantization statement ("one CAL-3 quantum per
   bond") from the Hopf channel's Hecke structure — e.g. the multiplicity-one
   Frobenius reciprocity of [`frobenius-lepton-meson-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/frobenius-lepton-meson-bridge.md)
   (`⟨Res V_(2,1), V_(2)⟩ = 1`) is the natural candidate for "exactly one".
3. **Sharpen the datum**: the 7% scatter is the binding-systematics floor; a
   per-pair Coulomb treatment replacing the uniform-sphere 3/5 (parent audit
   item 3) would shrink the band and make the `Q(q₀)` table discriminating.

**GAP 2 (exponent):**
1. Attack the re-scoped form: derive `E_pack(A) ∝ A^{−1/3}` as a pure-MeV /
   combinatorial statement (per-bond CAL-3 energy diluted by the extensive
   bond count), with no length object.
2. The cusp route's missing input is the **canonical A-component nuclear link
   family** (the SDP canonical knot-ID at H₁₂, already the named route from the
   ⁴He `Vol₄` negative) — with cusp count ∝ A restored, per-cusp volume
   constancy becomes a falsifiable prediction (Borromean value 2).
3. Do **not** re-run cusp-normalization scans: the two pinned readings are
   recorded above; any further normalization must be named in advance by a
   structural object.

## Files

- probe: [`computations/deltalambda/pion_radius_and_cusp_volume_gap_probe.py`](../../computations/deltalambda/pion_radius_and_cusp_volume_gap_probe.py) (new)
- witness: [`computations/deltalambda/pion-radius-and-cusp-volume-gaps.witness.json`](../../computations/deltalambda/pion-radius-and-cusp-volume-gaps.witness.json) (new, audit-only, 10/10 pass)
- this audit: `docs/audits/2026-07-13-pion-radius-and-vol-to-radius-gaps.md`
- context consumed (unchanged):
  [`2026-07-13-mirror-split-continuum-em-derivation-attempt.md`](2026-07-13-mirror-split-continuum-em-derivation-attempt.md) (parent),
  [`binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md),
  [`three-calibration-discipline.md`](../../content/quantum-observable-universe/observations/three-calibration-discipline.md),
  [`epistemic-status-of-calibrations.md`](../../content/quantum-observable-universe/observations/epistemic-status-of-calibrations.md),
  [`frobenius-lepton-meson-bridge.md`](../../content/quantum-observable-universe/braids-and-knots/frobenius-lepton-meson-bridge.md),
  [`inter-nucleon-channel-color-tube.md`](../../content/quantum-observable-universe/brings-surface/inter-nucleon-channel-color-tube.md) (checked: color-tube channel assignment, no meson-class identification — the (a) argument is new),
  [`2026-07-11-archimedean-functor-taxonomy.md`](2026-07-11-archimedean-functor-taxonomy.md),
  [`2026-07-04-em-linking-cusp-geometry-excluded.md`](2026-07-04-em-linking-cusp-geometry-excluded.md),
  [`2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md`](2026-05-31-cal-3-equals-m-pi-empirical-corroboration.md)
