# Deep Mass / Beta-Decay / Binding-Energy Audit — 2026-05-08

**Branch:** `copilot/audit-mass-beta-decay-computation`
**Scope:** Every mass, beta-decay, and binding-energy computation in `folio-assistant/computations/`; full pre-archimedean derivation chain; convention/weight inconsistencies; crystal-base compute-optimization opportunities; revised 1-ppb workplan; per-improvement re-eval baseline.

**Method:** Four parallel sub-agents read the entire compute pipeline + content blocks + Lean files + `proof-objects.json` and returned classified findings. This document set consolidates their findings, removes overlap, and assigns severities.

## Documents

| # | Document | What it answers |
|---|----------|-----------------|
| 00 | [Workplan](00-workplan.md) | Scope, severity legend, success criteria, contract |
| 01 | [Baseline mass / B / β table](01-baseline-mass-table.md) | Frozen reference: every prediction at HEAD with citations |
| 02 | [Pre-archimedean derivation chain](02-pre-archimedean-derivation-chain.md) | Step-by-step: categorical action → non-abelian Stokes → knot decomposition → Wedderburn → partitions/weights → Frobenius pairing → Gröbner-Shirshov → jet order → Hecke energy. Per-link status badge. |
| 03 | [Mass audit findings](03-mass-audit-findings.md) | Per-script classification (DERIVED / FITTED / HEURISTIC / EMPIRICAL_FIT) for every mass computation |
| 04 | [Beta-decay audit findings](04-beta-decay-audit-findings.md) | g_A, V_ud, G_F, θ_W, N_v, Q-values; gating chain |
| 05 | [Binding-energy audit findings](05-binding-audit-findings.md) | JSJ pieces, ρ_F, c_αα, α-cluster formula, Frobenius pairing in B |
| 06 | [Convention / weight inconsistencies](06-conventions-weights-inconsistencies.md) | Wedderburn weights, Markov normalisations, σ vs T, q-bracket, ρ_F, y_λ vs u_λ, energy notation |
| 07 | [Crystal bases / KLR / Kashiwara optimizations](07-crystal-bases-optimizations.md) | Type-B folding, KL bases, Demazure, RSK-accelerated GS reduction |
| 08 | [Revised 1-ppb workplan](08-1ppb-workplan-revised.md) | Gating gaps, dependency DAG, phased milestones |
| 09 | [Baseline + improvement tracker](09-baseline-and-improvement-tracker.md) | Per-improvement re-eval table; small-regression policy |

## Top-level findings (TL;DR)

1. **45% of mass-computation inputs are HEURISTIC** (lack categorical backing). Top critical gaps: proton/neutron crossing tables, ρ_F = m_e vs 2 m_e rule, α-cluster knot 7²₁, Δ_I coupling form.
2. **The `7²₁ ↔ α-α coupling` choice may be reverse-engineered from ¹²C** (circular). If so, ¹²C / ¹⁶O / ²⁰Ne are not predictions — they are interpolations between ⁴He and the calibration knot. **[CRITICAL]** — see [05 §B.3](05-binding-audit-findings.md).
3. **N_v gap gates the entire weak sector.** `conj:n-v-bring-action` is unproved; every G_F-dependent prediction (β-decay rate, CKM, EW precision) is conditional.
4. **⁴He at +5.87% deviation** is structurally tied to N_v (memory verified) AND used as the α-cluster anchor. It is **input** to the α-cluster formula, not a prediction.
5. **Wedderburn-weight scheme is inconsistent across 11 scripts** (3 distinct formulas: `H_3 normalised`, `Plancherel`, `Wenzl`). `hecke_core.wedderburn_weight()` returns Plancherel weights that **do not sum to 1** — violates `tr_M(𝟏) = 1`.
6. **58 of 58 historical LP/SDP witnesses lacked dual variables** before the 2026-05-07/08 backfill. The CI gate (`lp_dual_witness_validator.py --strict`) is now in place but has not been turned on by default.
7. **The pre-archimedean chain has 6 of 13 critical-severity gaps** (46%): Yekutieli Stokes (remark, not theorem), JSJ ↔ Wedderburn (no block), GB spectral-sequence collapse (asserted, no proof), Frobenius–LP duality (no master-formula block), brane-tower correction (defined to absorb leptonic/hadronic 0.75% gap), canonical knot identification SDP (retrodiction not prediction).
8. **The "three-constant calibration" framing understates the inputs.** Actual experimental inputs: `m_e`, `Vol(4₁)`, `m_μ/m_e`, `Q_n`, `B(⁴He)` (α-cluster anchor), census knot volumes for D/T/³He. That is **5+** experimental inputs.
9. **Crystal-base optimization is high-leverage.** RSK + Lascoux–Schützenberger charge → crystal normal form would give **3–10× speedup** on atomic-braid GS reduction (called by 67 scripts).
10. **g_A bug fix is a clean win.** Old `borromean-axial-coupling.py` β·σ₁·β⁻¹ was cyclic-trivial; new implementation uses Frobenius reciprocity with LP duals and is q-dependent. Trail preserved in `_deprecated/`.

## Severity legend

| Badge | Severity | Meaning |
|-------|----------|---------|
| 🔴 | **CRITICAL** | Gates a primary claim of the paper; or no backing conjecture exists; or risks circularity |
| 🟠 | **HIGH** | Backing conjecture exists but is unproved (`sorry` / `conj:`); paper must label downstream as conditional |
| 🟡 | **MEDIUM** | Convention drift, or "obvious" formula lacking a content block; doesn't gate predictions |
| 🟢 | **LOW** | Formatting, doc, or low-impact cleanup |

## Audit flag count

| Doc | 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low |
|-----|------------:|--------:|----------:|-------:|
| 02 — Derivation chain | 6 | 2 | 3 | 2 |
| 03 — Mass | 16 | 12 | 15 | 6 |
| 04 — Beta-decay | 7 | 5 | 4 | 2 |
| 05 — Binding | 4 | 6 | 5 | 2 |
| 06 — Conventions | 3 | 4 | 8 | 5 |
| 07 — Crystal optimization | 0 | 1 (highest payoff) | 3 | 2 |
| **Total** | **36** | **30** | **38** | **19** |

## Cross-references to existing audits

This audit reads, deduplicates against, and supersedes (where applicable) these recent threads — but does not re-litigate their conclusions:

- `2026-05-06-frobenius-pairing-compute-audit.md` (g_A cyclic-trivial fix; bound-state master formula)
- `2026-05-06-refocused-1ppb-workplan-v2.md` (N_v / Hoefsmit / Higgs gating chain)
- `2026-05-07-borromean-axial-coupling-fix.md` (g_A LP-dual implementation)
- `2026-05-07-lp-dual-backfill.md`, `2026-05-08-lp-dual-wired-audit.md` (LP-dual CI infra)
- `derivation-chain-mass-tower.md`, `derivation-tracking-methodology.md` (predecessors of [02](02-pre-archimedean-derivation-chain.md))
- `path-to-1ppb*.md`, `mass-1ppm-workplan.md`, `qou-algebraic-refactor-workplan.md` (predecessor workplans of [08](08-1ppb-workplan-revised.md))

The "supersedes" relation is documented per file, not at folder level. No previous audit is silently invalidated.
