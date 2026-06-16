# Improvement opportunities — paper / compute / exposition (2026-05-24)

**Branch**: `claude/gifted-feynman-U7ckD`  ·  **PR**: [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: owner directive "how can we improve paper/compute/exposition at this point?"
**Scope**: high-level brainstorm given current state of audits + Phase A v2 outcome (d) + SUPERSEDED ρ_q purge in progress

## Paper-side improvements

### P-1 — Surface the "ansatz vs derivation" distinction explicitly

The Q_β fitting finding revealed that several core derivations rest on POSTULATED (not derived) relations marked "by construction". The paper should adopt a **discipline marker** distinguishing:

- **Theorem** — proved end-to-end from substrate
- **Construction** — definitional, no claim of derivation
- **Ansatz** — postulated relation; empirically supported but not derived
- **Conjecture** — open mathematical claim

Currently the paper mostly uses "proposition" / "definition" / "remark" without distinguishing (b)/(c)/(d) above. The Q_β residual ambiguity comes from this lack of distinction. **Recommended action**: add an "Ansatz" block kind or a `status: "ansatz"` field on propositions.

### P-2 — Front-load the cohomological discipline statement

`prop:three-calibration-discipline` (H⁰/H¹/H² calibrations) and `prop:three-parameters-wedderburn` (3 channels) are foundational. They should appear **early in the introduction** as the framework's organizing principle, not buried in later chapters. The "3 inputs ↔ 3 channels" identity is the cleanest way to communicate the framework's parsimony.

### P-3 — Resolve the muon knot identification

[`docs/audits/2026-05-24-muon-knot-id-conflict.md`](../audits/2026-05-24-muon-knot-id-conflict.md) — the muon=4_1 (paper) vs muon=5_1 (compute scripts) vs muon=different (PR #1153) inconsistency confuses readers. Single canonical statement needed.

### P-4 — Audit author notes for status leaks

CLAUDE.md §4d formalizes `authorNotes` for status / refined-framing / caveats. A sweep of all `.md` blocks for status-banners-in-prose (especially "as of [date]", "currently", "open") + migrate to `authorNotes`. The `one-voice-audit` skill is designed for this.

### P-5 — Explicit bar-decomposition section

PR #1153's `P_m`/`Q_m` framework + PR #1196's Lean infrastructure are landing on main. The paper needs a single section in Ch 3 (or wherever bar involution is introduced) that walks through:
- bar = q ↦ q⁻¹ ↔ η = log q ↦ −η ↔ exp ↔ cosh/sinh
- P_avg (kept) vs P_skew (discarded)
- Per-particle bar-decomposition table (m_e, m_μ, m_p, m_n, Q_β all classified)
- Connection to EM channel / chirality / antimatter

## Compute-side improvements

### C-1 — Aggressive SUPERSEDED-ρ_q purge completion

11 content files + 0 (now) compute scripts still cite `ρ_q = 1/ℏ_q²` without the Phase 1 banner. Either:
- Add banners (low-effort, mechanical)
- Replace with canonical `prop:rho-k-graded-expansion` form (high-effort, requires per-file rework)

Phase 1 should be completed at minimum.

### C-2 — Reconcile lepton mass formulas with `prop:rho-k-graded-expansion`

`rho-k-graded-expansion` is framed for atomic braids (`Z·m_p + N·m_n + Z·m_e`) — LO piece is **zero for leptons**. Need a separate canonical statement for the lepton sector:
- electron from trefoil σ_1³ via per-braid mass tower
- muon from figure-eight (per resolution of P-3) via per-braid mass tower
- The ratio at operator level
- Identify where the "Vol/ℏ_q²" leading term emerges

**Concrete deliverable**: new content block `prop:lepton-mass-from-per-braid-tower` (companion to `prop:rho-k-graded-expansion`).

### C-3 — Wire production-vs-exploratory tags universally

CLAUDE.md §"Skill routing" has `production-vs-exploratory-discipline` skill. Apply it: every compute script should have an explicit **production** / **exploratory** / **diagnostic** tag in its docstring. Currently many are ambiguous. The audit tags from PR #1110 (`# archimedean_by_design`) are one model; extend to production/exploratory.

### C-4 — Witness-pipeline drift root-cause

22+ consecutive CI failures on PR #1127 (validate / Content pipeline) match inherited witness-pipeline drift from main. The drift detector flags substantive-field changes beyond the filtered set (computedAt, durationMs, …). Root cause is unclear; needs investigation as a separate audit. The auto-resolve script in `/prepare-merge` handles it for individual PRs but doesn't fix the underlying flake.

### C-5 — Consolidate the muon braid catalogue

Multiple files identify muon variously (P-3 above). Compute should have ONE canonical source:
- `computations/canonical_braid_catalog.py` (or similar) — single source of truth for: electron = σ_1³, muon = (σ_1 σ_2⁻¹)² [figure-eight], proton = [u,u,d], neutron = [u,d,d], W = T(2,5), etc.
- All other scripts consume this catalogue
- `knot-volumes.py` particle labels align with it

### C-6 — Operator-level mass-ratio probe (Phase 3)

The owner directive: re-derive `m_μ/m_e` at operator level (bypass SUPERSEDED ρ_q). Implementation:
- Compute `|tr_M(μ_braid)|` and `|tr_M(e_braid)|` directly at q_0 using `markov_peel.tr_M_atomic` or equivalent
- Express the ratio analytically + numerically
- Identify how `Vol(4_1)/ℏ_q²` emerges (or doesn't) from this calculation
- Report operator-correction size (= ratio − Skein LO)

**Status**: queued as P0.1 in [queued-work doc](2026-05-24-q-beta-pr1127-queued-work.md).

## Exposition improvements

### E-1 — Decision-tree intro per chapter

Each chapter should open with a 1-paragraph "what this chapter delivers" + "what the reader needs to read first" decision tree. The current chapter intros mostly assume linear reading; readers entering mid-paper get lost.

### E-2 — Audit-doc index page

`docs/audits/` has 50+ audit docs at this point. Need an index (`docs/audits/INDEX.md`) classifying:
- Open findings (gaps, conflicts, conjectures)
- Resolved findings (cite the resolution commit)
- Architectural decisions (no-action audits)

The audit-doc volume is becoming the framework's institutional memory; an index is essential.

### E-3 — "Status across observables" dashboard

`per-observable-100x-status.witness.json` is a dashboard but lives in compute. Need a paper-side equivalent: a single table listing every observable (m_e, m_μ, m_p, Q_β, etc.), its formula, its current predicted value, CODATA, residual, and which canonical / SUPERSEDED form generates each.

### E-4 — Glossary of bar-involution terminology

Per `bar-involution.md`'s "Anti-skew-vs-symmetric clarification": this terminology confuses readers. A dedicated glossary entry (Ch 8) for:
- bar / Lusztig bar / Hermitian bar (Q1 ↔ they're DIFFERENT for complex q per `prop:lusztig-vs-hermitian-bar`)
- P_avg / P_skew / bar-symmetric / bar-anti-symmetric
- cosh / sinh / EM channel / antimatter channel

### E-5 — Surface the historical-trajectory-of-ℂ doc

[`2026-05-24-complex-q-historical-trajectory.md`](../audits/2026-05-24-complex-q-historical-trajectory.md) places the framework's complex-q work in the 400-year arc of ℂ in physics. This is a substantial pedagogical contribution and should be:
- Cross-linked from the chapter that introduces the substrate (Ch 1 or Ch 5)
- Possibly elevated to an appendix or content block (currently audit-doc only)

## Cross-cutting / infrastructure

### X-1 — Sibling-coordination ledger maintenance

PR #1153, #1196 directly overlap with this PR. Coordination ledger needs continuous update; consider a `docs/coordination/INDEX.md` for live sibling tracking.

### X-2 — Test plan automation

PR #1127's test plan has 5+ unchecked items (Path A, Path B, Lean compilation, CI validate). Manual tracking is error-prone. Consider adding a `pr-test-plan-tracker.py` that diffs current state against the test-plan checklist.

### X-3 — Lean toolchain provisioning

Many session findings can't be Lean-verified because `lake` isn't in container. The `lean_setup` MCP tool exists (CLAUDE.md mentions it) — should be invoked at session start for any session that touches Lean. Alternatively, a CI workflow that runs `lake build` per-PR (already exists per `lean_ci.yml`).

## Priority ranking for next session

1. **C-6** Phase 3 operator-level m_μ/m_e (analytical heart) — 1-2 h
2. **P-3 + C-5** muon knot ID resolution — 30 min + 30 min
3. **C-1** SUPERSEDED-ρ_q purge completion (11 remaining banners) — 1 h
4. **P-5** explicit bar-decomposition paper section — 1-2 h
5. **C-2** lepton mass formula reconciliation — 2-3 h
6. **E-2** audit-doc index — 30 min
7. Everything else — multi-session

## Cross-references

- Related: [`2026-05-24-pr1127-prioritized-workplan.md`](2026-05-24-pr1127-prioritized-workplan.md) (tactical workplan)
- Related: [`2026-05-24-q-beta-pr1127-queued-work.md`](2026-05-24-q-beta-pr1127-queued-work.md) (P0/P1/P2 priorities)
- This doc: strategic improvement opportunities (vs the others' tactical execution plans)
