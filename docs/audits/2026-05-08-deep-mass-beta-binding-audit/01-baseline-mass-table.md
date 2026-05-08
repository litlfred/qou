# 01 — Baseline Mass / B / β Table (frozen reference)

**Purpose:** A single-source frozen baseline of every numerical prediction at the head of `copilot/audit-mass-beta-decay-computation`. Subsequent improvement PRs amend [09 — improvement tracker](09-baseline-and-improvement-tracker.md) with a new row each; baseline values here do not change.

**Frozen at:** commit `f96b8b2` (HEAD as of 2026-05-08).
**Substrate:** `q_0 = 1.10997859555418...` (50-digit pinned via Vol(4₁) and m_μ/m_e — see `q_parameter.py` and `q-pinning-50-digit.witness.json`).
**Calibration constants (FITTED):** `m_e = 0.51099895 MeV` (CODATA 2022), `Vol(4₁)` (SnapPy verified), `m_μ/m_e = 206.7682830` (CODATA 2022), `Q_n = 0.78233 MeV` (CODATA 2022, used as `E_0` anchor in mass-formula-6term).

## A. Hadron masses

| Particle | Predicted | CODATA / PDG | Δ / target | Compute script | Witness | Class |
|----------|-----------|--------------|-----------:|----------------|---------|-------|
| m_e | (anchor) | 0.51099895 MeV | 0 (FIT anchor) | `q_parameter.py` | `q-parameter.witness.json` | FITTED anchor |
| m_p / m_e | **1869.851** | 1836.152 | **+1.835%** | `mass_endomorphism.py` | `mass-endomorphism.witness.json` | DERIVED but ⚠ 1.84% |
| m_n / m_e | **1874.6** (approx) | 1838.683 | ~+1.96% | `mass_endomorphism.py` | same | DERIVED but ⚠ |
| m_p (β-calibrated) | (set to CODATA by construction) | — | 0 (calibrated) | `mass_formula_6term.py` | `mass-formula-6term.witness.json` | calibration absorbs the 1.84% |
| m_n (β-calibrated) | (set to CODATA by construction) | — | 0 (calibrated) | `mass_formula_6term.py` | same | calibration absorbs |

**Observation:** m_p/m_e raw `mass_endomorphism` chain is off by 1.84%. The mass-formula-6term chain "predicts" CODATA values for p and n only because Q_n is used as the `E_0` calibration. **This is not a zero-parameter prediction for nucleon masses**. Only p−n splitting (and isotopes downstream) are predictions in that scheme.

[AUDIT-FLAG severity=high id=DEEP-2026-05-08-001] — m_p/m_e raw chain at 1.84% deviation; root cause in §03.

## B. Light nuclei binding (mass_table_ppb)

From `mass-table-ppb.witness.json` (Kashaev law `B = ρ_F · Vol_hyp(K)`, `ρ_F ∈ {m_e, 2 m_e}`):

| Atom | Z | N | A | B_AME (MeV) | B_pred (MeV) | err % | err ppb | knot | ρ_F | origin |
|------|--:|--:|--:|------------:|-------------:|------:|--------:|------|-----|--------|
| ²H (D) | 1 | 1 | 2 | 2.22457 | **2.24882** | +1.090% | +1.09e7 | 6₂ | 1·m_e | **hyp: census-assigned** |
| ³H (T) | 1 | 2 | 3 | 8.48180 | **8.46860** | −0.156% | −1.56e6 | 8₁₁ | 2·m_e | **hyp: census-assigned** |
| ³He | 2 | 1 | 3 | 7.71804 | **7.48892** | **−2.969%** | −2.97e7 | L6a4 | 2·m_e | **hyp: census-assigned** |
| ⁴He | 2 | 2 | 4 | 28.29569 | **29.95568** | **+5.867%** | +5.87e7 | (4·8G) | 2·m_e | framework: A·8G magic rule |
| ¹²C | 6 | 6 | 12 | 92.16175 | (anchor) | 0 (set) | — | (3α + 3·c_αα) | — | α-cluster anchor |
| ¹⁶O | 8 | 8 | 16 | 127.61933 | 127.732 (≈) | +0.09% | +9e5 | (4α + 6·c_αα) | — | α-cluster prediction |

**Critical observations:**
1. D, T, ³He are **census-assigned** — the "knot ↔ atom" map is a SnapPy nearest-volume search, **not derived from (Z,N)**. [DEEP-2026-05-08-002 severity=critical]
2. ⁴He at +5.87% is the **single biggest residual** in light nuclei. Memory verified: tied to the N_v / weak-sector gap. [DEEP-2026-05-08-003 severity=critical]
3. ¹²C is the **calibration anchor** for `c_αα`. ¹⁶O at +0.09% is therefore **not zero-parameter** — it is an interpolation between ⁴He and ¹²C with one fitted coefficient. [DEEP-2026-05-08-004 severity=critical] (See [05 §B.3](05-binding-audit-findings.md) for the full circularity analysis.)
4. The α-cluster knot 7²₁ choice (Vol = 4.7495) — derivation status: **TOPOLOGICAL_HEURISTIC at best, EMPIRICAL_FIT at worst**. [DEEP-2026-05-08-005 severity=critical]

## C. Mass-formula 6-term predictions (light isotopes, β-calibrated)

From `mass-formula-6term.witness.json` (term1 + term4 with `per-3A canonical` Wedderburn convention):

| Atom | A | term1+term4 (MeV) | B_AME (MeV) | err % | status |
|------|--:|------------------:|------------:|------:|--------|
| D | 2 | 2.272 | 2.225 | +2.12% | term2/3 near-pole (max\|V\| = 0.989, very close to 1) — see DEEP-2026-05-08-006 |
| T | 3 | (near-pole) | 8.482 | — | T2/T3 tower diverges; Φ_q evaluation unstable |
| ⁴He | 4 | (use mass_table_ppb) | 28.30 | — | A1 calibration only |

[AUDIT-FLAG severity=high id=DEEP-2026-05-08-006] — Φ_q tower evaluation has `max|V| > 0.989` for D, T, ³He, ⁴He at q_0 ⇒ near-pole; "term23_tower_free": T2 = 1.6e6 MeV. The mass-formula-6term Φ_q chain is **numerically unstable** at q_0. Only term1+term4 is usable; term2/3 require Demazure/level-k truncation.

## D. β-decay observables

From `borromean-axial-coupling.py` (post fix; LP-dual implementation), `c_alpha_from_Q_beta_trace.py`, `free-neutron-decay.py`:

| Observable | Predicted | PDG | Δ | Class | Notes |
|------------|-----------|-----|---:|-------|-------|
| g_A | (q-dependent, current value ≈ 1.27 ± LP shadow) | 1.2754 | <5% | DERIVED via Frobenius reciprocity | Backed by `prop:confinement-frobenius-reciprocity`; isospin-projector tightening ⇒ tighter |
| V_ud | **NOT IN CODEBASE** | 0.97370 | — | MISSING | [DEEP-2026-05-08-007 severity=critical] CKM matrix absent |
| G_F | (used to extract N_v) | 1.166e-11 MeV⁻² | calibration | FITTED | [DEEP-2026-05-08-008] G_F → N_v inversion is the gate |
| N_v | (extracted from G_F) | — | — | HEURISTIC (W-2 closed null result) | `conj:n-v-bring-action` UNPROVED |
| Q_n (free n β⁻) | (anchor — calibrates E_0) | 0.78233 MeV | 0 | FITTED anchor | |
| Q_β(³H → ³He) | derived | 0.018592 MeV | small | DERIVED (modulo 7²₁ knot for ³He) | err propagates from 7²₁ |
| sin²θ_W | EW eigenvalue search → 0.13% gap | 0.23122 | <1% | EMPIRICAL_FIT (pattern-match) | `conj:hoefsmit-ew-cell-content` UNPROVED; "close-321-weinberg-gap" applies q^(1/h_corner) correction |

[AUDIT-FLAG severity=critical id=DEEP-2026-05-08-007] — V_ud (CKM) is missing entirely from the framework. Either compute it from categorical EW structure or document this scope limitation explicitly.

## E. Convention parameters (used as inputs across multiple scripts)

| Symbol | Value at q_0 | Meaning | Backing | Audit flag |
|--------|--------------|---------|---------|------------|
| z_markov | 0.49932... | Markov parameter `z = 1/(q^(1/2)+q^(-1/2))` | DERIVED (Hecke std convention) | — |
| z² | 0.24932... | Cross-term weight | DERIVED | — |
| w_sym | 0.16546... | Wedderburn sym weight (mass_endomorphism) | **3 different formulas in 11 scripts** | DEEP-2026-05-08-009 critical |
| w_std | 0.66908... | Wedderburn std weight | same inconsistency | DEEP-2026-05-08-009 |
| w_alt | 0.16546... | Wedderburn alt weight | same | DEEP-2026-05-08-009 |
| E_0 | 3.13253 MeV | Energy scale (mass-formula-6term) | FITTED via Q_n | OK as anchor |
| frob_n3 | 1.27611 MeV | Frobenius per-vortex at n=3 | DERIVED at q_0 | needs Lean (§02 link 6) |
| ρ_F | m_e (bonds) / 2·m_e (matter) | Frobenius scale | HEURISTIC | DEEP-2026-05-08-010 critical |
| n_chir(P) | 1 or 2 per JSJ piece | Active chirality blocks | HEURISTIC | DEEP-2026-05-08-011 critical |

## F. Lean-formalization status (extract from `proof-objects.json`, sample)

Of the named blocks in this audit:

- `prop:confinement-frobenius-reciprocity` — **stated**, has `sorry`
- `prop:bw-coefficient-shadow-price` — **stated**, has `sorry` (LP-dual master formula)
- `prop:operator-selection-lp` — **stated**, has `sorry`
- `prop:knot-operator-lp-selection` — open prop, Lean class with concrete LP-witness predicates
- `prop:weak-symmetric-normalization` — **demoted** (Plancherel-degenerate) 2026-05-05
- `conj:hoefsmit-ew-cell-content` — open conj, n=6 disjoint-strand-pair identification
- `conj:categorical-higgs-mechanism` — skeleton, four open inputs
- `conj:weinberg-angle-categorical` — open, gated on linking + Hoefsmit + Higgs-vev
- `conj:n-v-bring-action` — UNPROVED (gates entire weak sector)
- `conj:brane-tower-z-habiro` — UNPROVED, has `sorry` for `tower(T_w)` in `MassIdentity.lean`
- `conj:canonical-knot-id-sdp` — open problem, no Lean file
- `prop:gb-spectral-sequence` — stated, **should be downgraded to conj:** (no formal proof)

## G. Zero-parameter claim audit

The repository implicitly claims many predictions are "zero-parameter" / "ab initio". Per this baseline:

| Prediction | Truly zero-parameter? | Why not |
|------------|:---------------------:|---------|
| q_0 from Vol(4₁), m_μ/m_e | ✅ (modulo 2 fitted constants) | OK |
| m_p, m_n via mass_endomorphism | ⚠ DERIVED but +1.84% err | OK as derived; not "predicted at CODATA" |
| m_p, m_n via mass_formula_6term | ❌ | β-calibrated to Q_n |
| D binding via 6_2 | ❌ | knot is census-assigned (nearest-volume search) |
| T binding via 8_11 | ❌ | knot is census-assigned |
| ³He binding via L6a4 | ❌ | knot is census-assigned |
| ⁴He binding | ❌ | A·8G "magic rule" + ρ_F = 2 are heuristic; +5.87% err |
| ¹²C binding | ❌ | calibration anchor for c_αα |
| ¹⁶O binding | ❌ | interpolation between ⁴He and ¹²C-calibrated c_αα |
| g_A | ✅ (post fix) | DERIVED via Frobenius reciprocity |
| sin²θ_W | ❌ | EMPIRICAL_FIT (eigenvalue pattern-match) |

## H. Frozen baseline checksum

For per-improvement re-eval, the values that MUST be re-computed in [09](09-baseline-and-improvement-tracker.md) after any pipeline change:

```
B(D)/MeV        = 2.2488207948647343
B(T)/MeV        = 8.46859838653302
B(³He)/MeV      = 7.48891930977096
B(⁴He)/MeV      = 29.95567723908384
m_p_raw/m_e     = 1869.850592337583
m_p_err_pct     = 1.8352833718332153
err_4He_pct     = 5.866568260696314
err_3He_pct     = -2.968606854126327
g_A             = (q-dep; current ≈ 1.27, see borromean-axial-coupling.witness.json)
```

A regression in any of these by > 0.5 percentage points without a documented cause **must be flagged in the corresponding improvement PR**.
