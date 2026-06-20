# `docs/` — orientation for agents and reviewers

> If you're an agent picking up QOU work, **read in this order**:
> 1. [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md) — the canonical chain (substrate → observables), per-step math, scripts, Phase 5 findings, and the open framing-rules
> 2. [`precision-goals.md`](precision-goals.md) — what "1 ppb" means; L1 vs L2 distinction
> 3. The current-PR's `docs/coordination/` ledger (if one exists)
> 4. This README's "What's where" map below.

---

## ⚠ One absolute framing rule (agents recurrently get this wrong)

**`λ_scale` is NOT a separate object.** It was **absorbed** into the per-knot `VolDensity(K)` evaluation on 2026-05-23 (commit `ffdd84409`). The canonical mass formula is:

```
m(K) = m_e × VolDensity(K, q₀)
```

— a **single** Geom call per knot/link, per `prop:geom-universality`. The numerical factor that older docs call `λ_scale` is *what `VolDensity(K)` produces for that K*. There is no separate constant to derive, calibrate, or "close". The ~2.89% m_p residual is the gap between the framework's current categorical `VolDensity(𝓑₃)` computation and its categorically-exact value — open R&D for **refining `VolDensity`**, NOT for "deriving λ_scale".

Canonical reference (cite this in any audit/coord that touches λ_scale): [`lambda-scale-absorbed-into-vol-density.md`](lambda-scale-absorbed-into-vol-density.md). The original numerical demonstration is in [`coordination/2026-05-23-algebraic-geometric-observable-consistency.md`](coordination/2026-05-23-algebraic-geometric-observable-consistency.md) §"λ_scale is NOT a separate object".

---

## What's where

### Active canonical references (read these)

| File | Purpose |
|---|---|
| [`canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md) | Substrate → observables chain, per-step math, canonical scripts, Phase 5 findings, migration backlog (all 5 items closed) |
| [`precision-goals.md`](precision-goals.md) | L1 (1 ppb compute precision) vs L2 (100× experimental accuracy) discipline |
| [`ilp-sdp-audit.md`](ilp-sdp-audit.md) | LP/SDP dual conventions — referenced by canonical-watcher CI |
| [`witness-architecture.md`](witness-architecture.md) | Witness-pipeline architecture (WitnessBuilder, scriptCommitSha, drift detection) |
| [`copilot-lean-mcp-quickstart.md`](copilot-lean-mcp-quickstart.md) | Setting up the Lean MCP server |
| [`derivation-tracking-methodology.md`](derivation-tracking-methodology.md) | DerivationChain methodology (every observable traces to first principles) |

### Per-isotope / per-observable analysis (active)

| File | Purpose |
|---|---|
| [`d-error-budget.md`](d-error-budget.md) | Deuteron error-budget (still cited in compute) |
| [`b-over-a-error-budget.md`](b-over-a-error-budget.md) | B/A binding-energy ratio error budget |
| [`d-nf-knot-operators.md`](d-nf-knot-operators.md) | Deuteron Hecke-NF knot operators |
| [`d-mass-eq-density-vol-rederivation.md`](d-mass-eq-density-vol-rederivation.md) | Deuteron mass = density × volume re-derivation |
| [`fresh-derivation-pn-2026-04.md`](fresh-derivation-pn-2026-04.md) | Fresh p/n derivation (still cited) |

### Math/proof notes (active)

| File | Purpose |
|---|---|
| [`chi-std-pernucleon-theorem.md`](chi-std-pernucleon-theorem.md) | χ_std closed-form for per-nucleon braid words |
| [`chi-sym-alt-theorem.md`](chi-sym-alt-theorem.md) | χ_sym + χ_alt closed forms |
| [`crossing-graded-proof.md`](crossing-graded-proof.md) | Crossing-graded proof (cited by content) |
| [`locality-proof-attempt.md`](locality-proof-attempt.md) | Locality argument (cited by content) |
| [`hecke-formalization-requirements.md`](hecke-formalization-requirements.md) | Lean formalization requirements for Hecke algebra |

### Ongoing workplans (active)

| File | Purpose |
|---|---|
| [`path-to-1ppb-04-plan.md`](path-to-1ppb-04-plan.md) | 1ppb roadmap step 04 (cited; later docs in series archived) |
| [`path-to-1ppb-05-hints.md`](path-to-1ppb-05-hints.md) | 1ppb roadmap step 05 hints |
| [`mass-1ppm-workplan.md`](mass-1ppm-workplan.md) | Mass 1ppm workplan |
| [`pyhecke-optimization-workplan.md`](pyhecke-optimization-workplan.md) | pyhecke optimization roadmap |
| [`alpha-blend-derivation.md`](alpha-blend-derivation.md) | α-blend tower formula derivation |
| [`picard-lefschetz-plan.md`](picard-lefschetz-plan.md) | Picard-Lefschetz SW period plan |
| [`v-hat-within-level-candidates.md`](v-hat-within-level-candidates.md) | V̂ within-a-level improvement candidates |
| [`paper-formula-reconciliation-diagnostic.md`](paper-formula-reconciliation-diagnostic.md) | Paper formula reconciliation |
| [`canonicalization-review.md`](canonicalization-review.md) | Canonicalization review (1 ppb path) |

### Historical / dated audits (still in place; might be archived later)

| File | Purpose |
|---|---|
| [`infrastructure-audit-2026-04-20.md`](infrastructure-audit-2026-04-20.md) | Infrastructure audit (3 refs) |
| [`derivation-audit-2026-04-20.md`](derivation-audit-2026-04-20.md) | Derivation audit (3 refs) |
| [`mass-beta-decay-derivation-audit-2026-04-29.md`](mass-beta-decay-derivation-audit-2026-04-29.md) | Mass/β-decay derivation audit |
| [`session-summary-2026-04-20.md`](session-summary-2026-04-20.md) | Session summary (still cited) |
| [`reorganization-map.md`](reorganization-map.md) | Repo reorganization map (still cited) |

### Subdirectories

| Path | Contents |
|---|---|
| [`audits/`](audits/) | 352+ per-PR audit reports (chronological). Active references; do not bulk-move (227 scripts link in). |
| [`coordination/`](coordination/) | 50+ per-PR coordination ledgers. The most recent `1ppb-categorical-chain.md` and dated entries are the working log. |
| [`workplans/`](workplans/) | Workplans (small set). |
| [`plans/`](plans/) | Plans (small set). |
| [`agent-briefs/`](agent-briefs/) | Briefs for specific agent tasks. |
| [`qa/`](qa/) | QA sweep records. |
| [`handover/`](handover/), [`handoffs/`](handoffs/) | Inter-session handover notes. |
| [`_archive/orphan-top-level/`](_archive/orphan-top-level/) | 32 archived orphan docs (March / early-May session summaries, superseded migration plans, etc.) |

---

## Housekeeping (last sweep: 2026-05-24)

- 32 top-level orphan docs moved to `_archive/orphan-top-level/` (none referenced by code, content, or witnesses; all clearly historical session summaries / superseded workplans).
- Top-of-cheat-sheet absorption-framing banner added.
- AGENTS.md §"Canonical derivation chain" gets a one-line framing warning.
- `audits/`, `coordination/`, `workplans/` left intact — too many internal `auditOnly` references in witness JSONs to safely bulk-move.

If you find a stale doc here that should be archived, just `git mv` it to `_archive/orphan-top-level/` and append a line to that directory's README explaining why.
