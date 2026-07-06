# Low-isotope mass-error anatomy: where the residual actually lives

**Date:** 2026-05-24
**Branch:** `claude/great-galileo-ahGfj`
**PR:** [#1089](https://github.com/litlfred/qou/pull/1089)
**Status:** Diagnostic — surfaces hidden-fitting candidates + Lean-coverage gaps. No production change to the numerical predictions themselves.

## Question (owner, 2026-05-24)

> I want to see a detailed breakdown of each part of the mass of the low isotopes. Trace it all the way through the order and GB filtration for n and p. Validate each step is using canonical. Hidden fitting somewhere. Let's find it.
>
> KLR says all observables are ≥ 0 which is a help. If not, that points to definite issue. If under, then maybe missing terms or weighting is off. Triple-check weights — they have been all over the place. Should use canonical algebraic + geom/Bring's + archimedean.
>
> Make sure there is a Lean proof to back everything you are using. Flag where not as potential source of error.

## Per-isotope error table (from `low-isotope-mass-table.witness.json`)

| Atom | (Z, N, A) | tr_M(q₀)  | Pred (MeV) | AME / CODATA (MeV) | err_pct | Sign |
|------|-----------|-----------|------------|--------------------|---------|------|
| p    | (1, 0, 1) | 1.0653    | 965.384    | 938.272            | **+2.89%** | + |
| n    | (0, 1, 1) | 0.9232    | 966.715    | 939.565            | **+2.89%** | + |
| ²H   | (1, 1, 2) | 0.38828   | 2.2488     | 2.2246             | **+1.09%** | + |
| ³H   | (1, 2, 3) | 0.10405   | 8.4686     | 8.4818             | **−0.16%** | − |
| ³He  | (2, 1, 3) | 0.20654   | 7.4889     | 7.7180             | **−2.97%** | − |
| ⁴He  | (2, 2, 4) | 0.05535   | 29.956     | 28.296             | **+5.87%** | + |
| ⁵Li  | (3, 2, 5) | 0.02944   | **null**   | 26.328             | —          | — |
| ⁶Li  | (3, 3, 6) | 0.00789   | **null**   | 31.994             | —          | — |

The signs flip across A. This is the central observation.

## KLR-positivity check

| Layer | Status |
|------|--------|
| `tr_M(q₀)` values | ✅ all positive (KLR canonical-basis positivity holds at the trace level) |
| Prediction errors | ⚠️ 2 under-predictions (³H, ³He) + 4 over-predictions (p, n, ²H, ⁴He) |

Per the owner's framing: *under-prediction → missing positive contributions or wrong weighting*. The bidirectional swing argues for **channel-weight miscalibration**, not for a uniform VolDensity scale gap.

## Why PR [#1063](https://github.com/litlfred/qou/pull/1063)'s framing breaks for low isotopes

PR #1063 diagnoses the +2.89% gap as a `VolDensity(𝓑₃)` categorical-exactness refinement at h² order. That hypothesis predicts **every isotope** overshoots by the same fraction. The table above falsifies this for A ≥ 3 — ³H and ³He **under-predict**, ⁴He **over-predicts by 2× the proton offset**.

A single-knot VolDensity refinement cannot simultaneously fix p/n (where it would need a smaller scale) and ⁴He (where it would need a larger scale). The miscalibration is per-isotope, channel-dependent.

## Where the channels enter — and the hidden-fitting risk

The canonical braid word per atom (per [`isotope_record_schema.py:190-272`](../../computations/isotope_record_schema.py)) places **inter-nucleon Hecke generators** at positions `3k+2`. Their numerical (c, d) coefficients come from the Hecke quadratic:

| Channel | Crossing type | (c, d) at σ + d·𝟙 | Hecke meaning |
|---------|---------------|--------------------|---------------|
| pp | `SIGMA` | (1, 0) | bare σ — positive crossing |
| nn | `SIGMA_INV` | (1, −h) | σ⁻¹ = σ − h (Hecke quadratic identity) |
| pn | `AVERAGED` | (1, −h/2) | (σ + σ⁻¹)/2 — bar-symmetrization |

**The (c, d) numerics are canonical** — they unfold the Hecke quadratic σ² = (q − q⁻¹)σ + 1, which is in Mathlib. **What is NOT canonical** is the structural CHOICE of channel assignment:

> The rule "pp → σ (chirality +), nn → σ⁻¹ (chirality −), pn → σ_avg" is asserted in [`isotope_record_schema.py`](../../computations/isotope_record_schema.py) lines 176-178 + `build_knot_operator_catalogue()` lines 248-262.

This rule **has no `prop:` content block formalising it**, no Lean theorem, and no categorical-derivation pointer beyond an informal CPT-symmetry argument. **It is the most concrete hidden-fitting candidate surfaced by this audit.**

## Inter-nucleon channel counts vs error signs

| Atom | pp | pn | nn | err_pct |
|------|----|----|----|---------|
| p, n |  0 |  0 |  0 | +2.89%  |
| ²H   |  0 |  1 |  0 | +1.09%  |
| ³H   |  0 |  1 |  1 | −0.16%  |
| ³He  |  1 |  1 |  0 | −2.97%  |
| ⁴He  |  1 |  1 |  1 | +5.87%  |

Observations:
- Adding `pn` to a baryon (n → ²H) reduces err by ~1.8 pp.
- Adding `nn` on top (²H → ³H) reduces err by another ~1.25 pp.
- **Replacing nn with pp (³H → ³He) flips sign and increases magnitude** — a strong asymmetry signal.
- Adding nn back (³He → ⁴He) overshoots in the OTHER direction by ~8.8 pp.

The per-channel impacts are **not symmetric** (`pp` adds positive ~3%, `nn` adds negative ~1.2%, `pn` adds negative ~1.8%), which is consistent with the (c, d) = (1, 0) / (1, −h) / (1, −h/2) weights but the **sign pattern needs a categorical explanation** and currently doesn't have one.

Quantitative regression is in [`low_isotope_sign_flip_diagnostic.py`](../../computations/low_isotope_sign_flip_diagnostic.py) (`low-isotope-sign-flip-diagnostic.witness.json` once CI runs it).

## Production-chain Lean-coverage matrix

| Ingredient | Used by | Lean-proved? | Risk |
|---|---|---|---|
| `linking_weight = (3q²+4+3q⁻²)/4` (Family A) | every mass script | ✅ [`lambda-scale-substrate-form.lean`](../../content/quantum-observable-universe/braids-and-knots/lambda-scale-substrate-form.lean) | LOW |
| `Vol(𝓑₃) = 8·G` (Adams 1985) | every mass script | ❌ literature only; not in Mathlib | **MEDIUM** |
| `VolDensity(K)` per-knot decomposition (`prop:geom-universality`) | PR [#1080](https://github.com/litlfred/qou/pull/1080) framing | ❌ narrative only | **MEDIUM** |
| `Δm/M_N = ℏ_q²·h_q·[2]_q·(1+ℏ_q³)/3` (flavor split, PR #690) | p/n mass split | ⚠️ partial: the (1+ℏ_q³) 3-loop correction lacks Lean backing | **MEDIUM** |
| pp/pn/nn channel-assignment rule | every multi-nucleon | ❌ no `prop:` block | **MEDIUM** |
| q₀ substrate value (CAL-2) | every script | ❌ numerical anchor | LOW (acknowledged CAL anchor) |
| Hecke quadratic σ⁻¹ = σ − h | inter-nucleon weights | ✅ standard Hecke (Mathlib) | LOW |
| Atom → knot assignment (D ↔ 6₂, T ↔ 8₁₁, ³He ↔ L6a4, ⁴He ↔ "magic A·8G shell") | [`mass_table_ppb.py`](../../computations/mass_table_ppb.py) | ❌ census-derived (admittedly AME-driven for D, T, ³He per [`mass_table_ppb.py:18-21`](../../computations/mass_table_ppb.py)) | **HIGH** |
| Kashaev volume law `B = m_e · Vol(K)` | [`mass_table_ppb.py`](../../computations/mass_table_ppb.py) | ❌ density rule ρ_F ∈ {m_e, 2m_e} pending formal justification per the script's own line 23 | **HIGH** |

## ⁵Li / ⁶Li prediction gap

Both have `tr_M(q₀)` computed (0.02944, 0.00789) but `prediction_MeV_50dps` is null. The reason: `mass_table_ppb.py` covers `D, T, ³He, ⁴He` via census atom→knot assignments and then jumps to `A ≥ 8` for α-cluster, leaving `A ∈ {5, 6, 7}` without a prediction rule.

To wire ⁵Li / ⁶Li:
1. Either find atom→knot assignments via census on Kashaev `B/m_e ≈ Vol`:
   - ⁶Li: target Vol ≈ 31.994 / 0.511 = **62.6** — needs a knot/link census in that range
   - ⁵Li (unstable resonance): ~26.328 / 0.511 = **51.5** — same
2. Or extend the α-cluster rule below A=8 (deferred — α-cluster derivation `c_αα = m_e · Vol(7²_1)` is itself only partially proved per [`mass_table_ppb.py:23-26`](../../computations/mass_table_ppb.py)).

Deferred to a follow-up branch (`claude/wire-a5-a7-isotopes-<date>`). Filed as audit gap; not addressed by this PR.

## Three-substrate decomposition (per AGENTS.md cheat sheet)

| Substrate | Role | Status |
|---|---|---|
| **Algebraic** (Hecke / Wedderburn / Φ_q / Li_2^q) | linking_weight; flavor split | ✅ canonical (Family A proved, flavor split partial) |
| **Geometric** (Bring's surface / Borromean rings / hyperbolic Vol) | Vol(𝓑₃) = 8·G; per-knot atom→knot assignment | ⚠️ Vol(𝓑₃) trusted from Adams 1985 (no Mathlib); atom→knot is census (HIGH risk) |
| **Archimedean** (MeV calibration from m_e, m_μ/m_e, Q_β) | CAL-1 anchor; q₀ pinning; MeV conversion | ✅ clean (anchor only) |

No inappropriate substrate mixing was found in the production chain. The mixing risk lives in the **atom→knot assignment** step, where the census process used AME values implicitly when picking which knot to associate with D, T, ³He.

## Top hidden-fitting candidates (ranked by load-bearing-ness)

1. **🔴 atom → knot census assignments (D ↔ 6₂, T ↔ 8₁₁, ³He ↔ L6a4).** Explicitly admitted as AME-driven by [`mass_table_ppb.py:18-21`](../../computations/mass_table_ppb.py). This is the most defensible existing CAL-4-equivalent in production.
2. **🔴 Kashaev density rule `ρ_F ∈ {m_e, 2m_e}`.** Script itself flags this as pending formal justification ([`mass_table_ppb.py:23`](../../computations/mass_table_ppb.py)).
3. **🟠 pp/pn/nn channel-assignment convention.** The σ / σ⁻¹ / σ_avg choices in [`isotope_record_schema.py`](../../computations/isotope_record_schema.py) lack a `prop:` block. The categorical CPT-symmetry argument is unproved.
4. **🟠 ⁴He "magic A·8G shell" closure** ([`isotope_record_schema.py:186`](../../computations/isotope_record_schema.py)). Labelled "magic" with no knot citation; biggest error magnitude (+5.87%).
5. **🟡 The (1+ℏ_q³) 3-loop factor in flavor split** (PR #690). Substrate-Planck correction with partial Lean coverage.

## Recommended next actions

1. **Escalate via Rule 14** (13-driver menu) on candidates 1 and 2: their categorical derivation has been pending for too long.
2. **Author a `prop:` block** formalising the pp/pn/nn channel-assignment rule (or escalate as Rule 14 candidate if no categorical mechanism can be identified).
3. **Wire ⁵Li / ⁶Li** in a follow-up branch via knot-census + Kashaev (with explicit AME-fit caveat).
4. **Comment on PR [#1063](https://github.com/litlfred/qou/pull/1063)** noting that the "single VolDensity(𝓑₃) refinement" diagnosis is incompatible with the sign-flip pattern at A ≥ 3 — amendment needed.

## Cross-references

- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](2026-05-23-lambda-scale-canonical-unification.md) — 13-driver menu + Rule 14
- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — PR #1080 framing
- [`computations/low_isotope_sign_flip_diagnostic.py`](../../computations/low_isotope_sign_flip_diagnostic.py) — quantitative diagnostic
- [`computations/isotope_record_schema.py`](../../computations/isotope_record_schema.py) — channel-assignment definitions
- [`computations/mass_table_ppb.py`](../../computations/mass_table_ppb.py) — Kashaev prediction rule + atom→knot census
- PR [#1063](https://github.com/litlfred/qou/pull/1063) — Family A +2.89% gap audit (framing being challenged)
- PR [#1080](https://github.com/litlfred/qou/pull/1080) — λ_scale absorbed into VolDensity (merged)
- PR [#1089](https://github.com/litlfred/qou/pull/1089) — this PR (code-level cleanup + sign-flip diagnostic)
