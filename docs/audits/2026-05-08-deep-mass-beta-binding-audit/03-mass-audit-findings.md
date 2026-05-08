# 03 — Mass Audit Findings

**Scope:** Every mass-computation script in `folio-assistant/computations/`. Per-script classification of every numerical input as DERIVED / FITTED / HEURISTIC / EMPIRICAL_FIT (definitions in [00 §4.1](00-workplan.md)).

**Total scripts read:** 23 active mass scripts + 15 witness JSONs + content blocks for ~30 conjectures/propositions.

**Headline:** **45% of mass-computation inputs are HEURISTIC** (lack categorical backing). Top critical gaps: proton/neutron crossing tables, ρ_F rule, α-cluster knot 7²₁, Δ_I form, Wedderburn weight scheme.

## §A. Substrate / global inputs

### A.1 `q_parameter.py` — the substrate parameter

**Inputs:**
- `Vol(4₁) = 2.02988321...` — DERIVED (SnapPy verified hyperbolic volume of figure-eight; topological invariant)
- `m_μ/m_e = 206.7682830` — FITTED (CODATA 2022)
- `q_0` is computed by inverting the relation `2π · ln(q_0) · ζ_q(2) = (m_μ/m_e)·Vol(4₁)/π` (or equivalent — see script for exact closed form)

**Classification:** DERIVED (modulo two FITTED inputs).

**Audit:** OK. The two fitted inputs are the *advertised* calibration constants. No flag.

### A.2 `experimental_constants.py` — CODATA constants

All entries are FITTED by definition. No flag.

## §B. Hadron-mass scripts

### B.1 `mass_endomorphism.py` — `m_p`, `m_n` via Φ_q tower

**Compute path:**
- Crossings table `crossings = "3σ(B₃)+1σ(uu)+1½(ud)+2σ(gluon) | 3σ⁻¹(B₃)+1½(ud)"` for the proton — **no derivation cited**.
- Wedderburn weights `w_sym = w_alt = 0.16546`, `w_std = 0.66908` — formula B (Plancherel-style, see [06 §A.1](06-conventions-weights-inconsistencies.md)).
- Markov parameter `z = 0.49932` — DERIVED.
- Φ_q tower with cross-term weight `z²` — DERIVED.

**Outputs:** `m_p/m_e = 1869.851` (CODATA 1836.152, +1.84%); `m_n/m_e ≈ 1874.6` (+1.96%).

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-301]**
- file: `folio-assistant/computations/mass_endomorphism.py:proton_crossings_table`
- description: Proton/neutron crossing assignments are HEURISTIC; no content block formalises why proton has `3σ + 1σ(uu) + 1½(ud) + 2σ(gluon)`. Risk of post-hoc tuning to match CODATA.
- backing: NONE (`conj:nucleon-braid-word` does not exist)
- remediation: Author `conj:proton-crossing-assignment` and `conj:neutron-crossing-assignment` deriving the crossing tables from quark-content categorical principles.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-302]** — Wedderburn weight scheme used here (formula B) does not match `wedderburn_pair_volumes.py` or `mass_at_3A_proper.py` (formulas A/C). See [06 §A](06-conventions-weights-inconsistencies.md).

### B.2 `mass_formula_6term.py` — the integrated 6-term formula

**Inputs:**
- `q_0` — DERIVED.
- `E_0 = 3.13253 MeV` — FITTED (calibrated to `Q_n = 0.78233 MeV` via `E_0 = Q_n / |Δ(net)|`).
- Per-vortex Frobenius `frob_n3 = 1.27611 MeV` — DERIVED at q_0.
- `term1` (descended free): closed-form q-expression — DERIVED.
- `term2`/`term3` (Φ_q single/pair towers): "near-pole" status with `max|V| > 0.989` — **numerically unstable** at q_0. T2 = 1.6e6 MeV reported.
- `term4` (Frobenius per-3A canonical): three different conventions exist in the script (`per-vortex`, `per-A`, `per-3A canonical`) — **inconsistency**.
- `term5` (BW chirality): closed-form — DERIVED.
- `term6` (jet corrections): **not implemented**.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-303]** — `term2/term3` numerical pole at q_0; predictions for D, T, ⁴He using these terms are unreliable. Either (a) implement Demazure / level-k truncation; or (b) document the term2/term3 truncation convention used.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-304]** — `term4` has 3 conventions: `per-vortex`, `per-A`, `per-3A canonical`. Per-A gives D err = 2.12%; per-3A gives 18.31%. **Convention choice changes predictions by an order of magnitude.** Pin the canonical choice.

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-305]** — `term6` (jet corrections) is the planned closure for ~100 ppm → ~1 ppm precision. Not implemented at HEAD.

### B.3 `hadron_knot_table.py` — π / K / proton / neutron / hyperons

Each row asserts a (knot, hadron) assignment. The script computes Vol from SnapPy and reports it — **the assignment itself is asserted, not derived**.

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-306]**
- description: Every row in the hadron-knot table is HEURISTIC: π → 3₁, K → 4₁, proton → (multi-knot), neutron → (multi-knot), hyperons → (catalog). No content block derives any assignment.
- backing: NONE (12 missing conjectures listed in the sub-agent report; e.g. `conj:pion-trefoil`, `conj:kaon-figure-eight`, etc.)
- remediation: Either author the 12 missing conjectures, or admit the table as "hypothesis for fit" and label the entire table as EMPIRICAL_FIT.

## §C. Atom-/isotope-mass scripts

### C.1 `mass_table_ppb.py` — Kashaev law light-isotope predictions (ZERO-FREE-PARAMETER claim)

Per [01 §B](01-baseline-mass-table.md):

| Atom | knot | rho_F | origin |
|------|------|-------|--------|
| D | 6_2 | 1·m_e | **hyp: census-assigned** |
| T | 8_11 | 2·m_e | **hyp: census-assigned** |
| ³He | L6a4 | 2·m_e | **hyp: census-assigned** |
| ⁴He | (4·8G) | 2·m_e | framework: A·8G magic rule |
| ¹²C | (3α + 3·c_αα) | — | α-cluster anchor |
| ¹⁶O | (4α + 6·c_αα) | — | α-cluster prediction |

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-307]** — The witness file's own `origin` field admits "hyp: census-assigned" for D, T, ³He. **The "zero-free-parameter" claim in the script's `description` field is contradicted by its own data.** Either remove the "no AME-derived calibrations" claim, or replace census assignment with a derivation.

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-308]** — A·8G "magic rule" for ⁴He (`B = 4 · 2·m_e · Vol(8G)`) — not derived. The formula is post-hoc; with `8G ≡ Vol(Borromean)/2`, this is fitting via choice of "8G".

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-309]** — `c_αα = m_e · Vol(7²₁)` — knot 7²₁ assignment to α-α coupling lacks derivation. **If 7²₁ was selected to make ¹²C come out right**, then ¹⁶O at +0.09% is an interpolation, not a prediction. Confirm the order of authoring (c_αα first, ¹²C check) or admit ¹²C as anchor.

### C.2 `low_isotope_mass_table.py`, `low_isotope_binding_sweep.py` — Z ≤ 10

Uses HEURISTIC ladder coefficients `α_k` fit per isotope; spans an order of magnitude across isotopes.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-310]** — `α_k` ladder coefficients are EMPIRICAL_FIT, vary 10× across isotopes; no universality. Either derive a universal form or label as EMPIRICAL_FIT.

### C.3 `mass_at_3A_proper.py` — alternative Wedderburn scheme

Uses formula B/C switchable. Predictions diverge from `atomic_braid_mass_table.py` predictions by ~1.3% at q_0 due to weight-scheme difference.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-311]** — Cross-script Wedderburn weight scheme inconsistency (formula B vs C). 1.3% effect on predictions. See [06 §A.1](06-conventions-weights-inconsistencies.md).

### C.4 `atomic_braid_mass_table.py`, `atomic_braid_mass_table_modes_sweep.py`

`atomic_braid_word_3A` for atoms — uses Jones-quotient fallback (lines 95-142) when full reduction is too slow.

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-312]** — Jones-quotient fallback is HEURISTIC; not equivalent to full Hecke reduction. Document when fallback is invoked and quantify error.

## §D. Witness-file inconsistencies

`mass_table_ppb.witness.json` reports `LP_stable: FAIL` for ¹²C, ¹⁶O, ²⁰Ne, ²⁸Si, ⁴⁰Ca — **the LP positivity constraint is violated** for all heavy α-nuclei.

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-313]** — LP-stability failures for heavy α-nuclei are a **structural breakdown of the formalism**. Currently silently ignored. Either:
- (a) Diagnose the failure (likely the α-cluster c_αα convention is over-constrained for `n_α ≥ 3`); or
- (b) Document the breakdown threshold (e.g. "α-cluster scheme valid for `Z ≤ 8`").

## §E. Missing conjectures (essential infrastructure)

The mass-computation pipeline asserts the following without any content block. Each MUST be authored before "zero-parameter" or "ab initio" claims are valid:

| # | Missing conjecture | Used by |
|---|--------------------|---------|
| 1 | `conj:volume-muon-relation` (q_0 from Vol(4₁) and m_μ/m_e) | `q_parameter.py` |
| 2 | `conj:proton-crossing-assignment` | `mass_endomorphism.py` |
| 3 | `conj:neutron-crossing-assignment` | same |
| 4 | `conj:frobenius-energy-scale` (ρ_F normalisation) | `mass_table_ppb.py`, all binding scripts |
| 5 | `conj:alpha-cluster-knot` (⁴He → 4·8G) | `mass_table_ppb.py` |
| 6 | `conj:alpha-alpha-coupling-knot` (c_αα → 7²₁) | same |
| 7 | `conj:pion-trefoil` (π → 3₁) | `hadron_knot_table.py` |
| 8 | `conj:kaon-figure-eight` (K → 4₁) | same |
| 9 | `conj:nf-basis-choice` (basis {γ, σ₀, σ₁, L₊, L₋, e⁻}) | `hadron_knot_table.py` |
| 10 | `conj:isospin-coupling` (Δ_I functional form) | `mass_formula_6term.py` |
| 11 | `conj:nucleon-braid-word` (proton/neutron word assignments) | `mass_endomorphism.py` |
| 12 | `conj:volume-mass-scaling` (E = m_e · Vol(K)) | `mass_table_ppb.py`, all Kashaev-law scripts |

**[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-314]** — 12 essential conjectures missing. Without them, the predictive predictions cannot be traced to categorical principles.

## §F. Calibration vs prediction confusion

Several scripts use a calibration anchor and then compute "predictions" for nearby isotopes — this is correct methodology but the **scripts do not flag** which inputs are calibrations.

**[AUDIT-FLAG severity=high id=DEEP-2026-05-08-315]** — Add `"input_type": "DERIVED" / "FITTED" / "HEURISTIC" / "EMPIRICAL_FIT" / "CALIBRATION_ANCHOR"` field to every witness JSON. CI gate to require it.

## §G. Reproducibility

All scripts are deterministic (no random seeds). Witness files include `commitSha`, `scriptHash`, `computedAt`. **Good.**

Missing: `model_uncertainty` field. Currently witness files report only the prediction; the systematic-error envelope (from HEURISTIC inputs) is not propagated.

**[AUDIT-FLAG severity=medium id=DEEP-2026-05-08-316]** — Add `model_uncertainty` field with conservative envelope from HEURISTIC input variations.

## §H. Top-15 critical gaps (mass)

| # | Flag | Gap | Severity |
|---|------|-----|---------:|
| 1 | DEEP-2026-05-08-309 | `c_αα = m_e · Vol(7²₁)` — knot may be reverse-engineered from ¹²C ⇒ circularity | critical |
| 2 | DEEP-2026-05-08-307 | `mass_table_ppb` "zero-free-parameter" claim contradicted by "hyp: census-assigned" origin field | critical |
| 3 | DEEP-2026-05-08-308 | A·8G "magic rule" for ⁴He has no derivation | critical |
| 4 | DEEP-2026-05-08-301 | Proton/neutron crossing tables HEURISTIC | critical |
| 5 | DEEP-2026-05-08-306 | Hadron-knot table assignments all HEURISTIC | critical |
| 6 | DEEP-2026-05-08-313 | LP-stability fail for ¹²C, ¹⁶O, ²⁰Ne, ²⁸Si, ⁴⁰Ca | critical |
| 7 | DEEP-2026-05-08-314 | 12 essential conjectures missing | critical |
| 8 | DEEP-2026-05-08-302 | Wedderburn weight scheme inconsistency (3 formulas) | high |
| 9 | DEEP-2026-05-08-303 | term2/term3 Φ_q tower numerical pole at q_0 | high |
| 10 | DEEP-2026-05-08-304 | term4 has 3 conventions; choice changes D err 2% → 18% | high |
| 11 | DEEP-2026-05-08-310 | α_k ladder coefficients EMPIRICAL_FIT, no universality | high |
| 12 | DEEP-2026-05-08-311 | mass_at_3A_proper vs atomic_braid_mass_table 1.3% disagreement | high |
| 13 | DEEP-2026-05-08-315 | Witness JSONs lack `input_type` classification field | high |
| 14 | DEEP-2026-05-08-305 | term6 (jet corrections) not implemented | medium |
| 15 | DEEP-2026-05-08-312 | Jones-quotient fallback in atomic_braid_mass_table | medium |

## §I. Reclassification of paper claims (recommended)

Current implicit framing → recommended honest framing:

- ❌ "Zero-parameter ab initio mass predictions"
- ✅ "Categorical mass framework with three calibration constants (`m_e`, `Vol(4₁)`, `m_μ/m_e`) plus β-decay anchor `Q_n` and α-cluster anchor `B(⁴He)`; 5 calibration inputs total."
- ❌ "Light isotopes D, T, ³He, ⁴He predicted from q_0 alone"
- ✅ "Light isotopes' canonical knot is currently assigned by SnapPy nearest-volume search (D, T, ³He) or by the A·8G heuristic (⁴He); the `Vol → B` map is then categorical."
- ❌ "¹⁶O at 0.09% is a prediction"
- ✅ "¹⁶O is computed by α-cluster interpolation between ⁴He (heuristic A·8G) and ¹²C (anchor for c_αα); the closeness is interpolation, not extrapolation."

These reclassifications cost nothing scientifically — they describe the work accurately and clarify what remains to derive.
