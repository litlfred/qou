# Strategic workplan review — post-2026-05-31 → 2026-06-09

**Authored:** 2026-06-09
**Branch:** `claude/workplan-strategic-review-2026-06-09`
**Trigger:** User request "lots of work in a week. update workplan after review main and siblings for relevant commits and overall strategy" following an extended session-pause (last PR I merged was [#1543](https://github.com/litlfred/qou/pull/1543), 2026-05-31).

## Headline

Main has had **~2481 commits in 7 days** across QA (~1107), review fixes (~211), Lean v4.24.0 repair (~172), audits (~73), and substantive structural migrations. My prior session's open carry-forward item (**operator-valued Wenzl combiner-convergence**, the last unaddressed gap from PR [#1543](https://github.com/litlfred/qou/pull/1543)) is **consciously parked pending upstream KLR infrastructure** — confirmed via the [`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) cont. 9 KLR roadmap and the two preflight refutations of Composites 4 (Wenzl × q-Pochhammer) and 1 (Demazure × q-Poch).

What I should pick up next is **not** continuation of the Wenzl path. The highest-leverage open work is in the Option-E and Lean-infrastructure neighbourhoods.

## What landed on main this past week (relevant to my scope)

| Cluster | Count | What it means for my queue |
|---|---|---|
| QA + Proof | ~1177 | Heavy QA pipeline expansion — sidecars, witness regen, section-title audits. My past audit docs may have stale sidecars; verify before any new claim. |
| Review fixes (Copilot/Gemini) | ~211 | Average ~5 fixes per PR. The discipline I installed in [#1543](https://github.com/litlfred/qou/pull/1543) (corpus-grep-before-declaring-open) should reduce the "Open Math A/B/N — already-implemented" review-comment churn I generated. |
| Lean v4.24.0 repair | ~172 | 40+ fixes across EmCoupling, HeckeEngine, BringShellBinding, SDP (`λ → lam` keyword changes, heartbeats, recDepth raises). **Gates upstream KLR/crystal work.** Need to re-check whether my IwahoriHecke / LRCoefficientHecke / WenzlAOperator classes still typecheck on the post-v4.24.0 build. |
| Cross-chapter detangler | ~14 | Quark sector moved Ch13→Ch9 (`104c46f9c`). My past audit-doc references to `predicted-spectra/` quark blocks may be stale. |
| Substrate-subdir migration | (Phase 6) | `computations/substrate/` — 11 modules; root-script shim via `_path_bridge`. My probe `binding_bring_enhancement_compare.py` already picked this up via auto-update. The post-merge linter-edits to my files (`lr-coefficient-hecke.md/.lean`, `binding_bring_enhancement_compare.py`, `2026-05-30-universal-branching-multinucleon-gap.md`) reflect the migration. |
| Falsified-conjecture deprecation | (multiple R100) | E.g., `conj-chirality-ribbon-frobenius` → `_deprecated/falsified-conjectures/`. Honest falsification tracking — my "open math" audit-doc framing should align. |

## Status of my prior carry-forward items (PR #1543 reanalysis)

| Item from #1543 audit | Status now |
|---|---|
| **Open Math A** (ρ_F derivation): structurally answered by `conj:kashaev-density-equals-sdp-multiplicity` | ✓ landed; no change |
| **Open Math B** (A=3 p/n asymmetry): answered by Bring color-tube weighting in `closed_form_tau_M.py` `bring_color_weighted` | ✓ landed; no change |
| **Wenzl combiner-convergence** (gap #4 of the 4-gap scope) | **PARKED** per 1ppq-qbeta cont. 9; not actively in-flight |
| **Disciplines installed** (corpus-grep-before-declaring-open + `docs/audits/README.md` + `proof-gap-audit` §K) | Live on main; effective |
| **post-mortem section** "Why was this missed?" | Live on main |

## What is actually active and overlaps my scope

Per the Explore-agent triage + STATUS.md cross-check:

1. **Option-E Phase 2** (Δ_λ closure via crystal vertex) — PR [#1516](https://github.com/litlfred/qou/pull/1516), [`option-e.md`](../coordination/option-e.md). All four single-vertex KL candidates **REFUTED**; next step is extending [`kazhdan_lusztig.py`](../../computations/substrate/kazhdan_lusztig.py) past n ≤ 4 cap to full `n^w_λ` enumeration on S_6. **Adjacent to my Wenzl-branching scope; not duplicating.**
2. **1ppQ Q_β c_3** ([`1ppq-qbeta.md`](../coordination/1ppq-qbeta.md), cont. 9-16): 28 single-formula candidates **SATURATED NEGATIVE**; Option A (CAL-3-anchored c_3 permanently) reinforced. No agent re-pitches at this point are productive.
3. **α_EM canonical chain**: Habiro element `[2]_q·(1−h²α)` merged (PR #1911); bar-EVEN vs bar-ODD residue distinction now wired.
4. **Mass-sweep gap A ≥ 4**: PR #1756 (α-cluster wire-up) shipped 7 atoms from B=0 to B_pred, m_err ~+0.9% → ~−0.1%. Non-α-cluster A > 12 still gated on H_{3A} kernel.
5. **Lake-cache discipline** ([`2026-06-07-lake-cache-restore-discipline.md`](../coordination/2026-06-07-lake-cache-restore-discipline.md)): **immediate-impact infrastructure** documented; should be the first step of any Lean-touching session.

## Recommended next work-tranche (priority order)

### 1. Lean v4.24.0 corpus-green verification — IMMEDIATE (~half session)

The Lean repair sprint (40+ fixes this week) may have left subtle drift in the classes I shipped:
- `QOU.BraidKnot.LRCoefficientHecke`
- `QOU.BraidKnot.WenzlAOperator`
- `QOU.BraidKnot.MagicABindingFormula`
- `QOU.IwahoriHecke.IwahoriHecke` (PR [#1524](https://github.com/litlfred/qou/pull/1524))

**Action:** Restore lake-cache per [`2026-06-07-lake-cache-restore-discipline.md`](../coordination/2026-06-07-lake-cache-restore-discipline.md) §"Step 0 + Step 2"; run `lake build QOU`; verify the four classes still typecheck. If any class needs a `λ → lam` keyword fix, ship the fix in one small commit.

**Rationale:** Sub-2-hour cost; un-gates everything else in the Wenzl / IwahoriHecke neighbourhood when KLR upstream eventually lands.

### 2. Option-E Phase 2 KL enumeration extension — half-to-full session

Extend [`kazhdan_lusztig.py`](../../computations/substrate/kazhdan_lusztig.py) past n ≤ 4 to S_6, then re-run the `n^w_λ` enumeration probe queued in PR [#1516](https://github.com/litlfred/qou/pull/1516). The witness `probe-option-e-phase2-crystal-vertex-candidates.witness.json` exists; the extension is mechanical.

**Rationale:** Highest-closure-potential active probe in the Δ_λ neighbourhood — refutation outcome pivots to GAP-A-3/A-4; positive outcome closes Option-E. Either way actionable.

**Coordination note:** PR [#1516](https://github.com/litlfred/qou/pull/1516) is in flight on `claude/coord-infra-1ppq-2026-05-31`. Before authoring, post intent on that PR per `local/coordinate` §3 (one comment, scope split).

### 3. Sidecar staleness sweep — half session (idle backlog)

Per CLAUDE.md §"5-minute idle trigger" + the new `## Refresh stale sidecars + witnesses` rule (added 2026-06-03 to CLAUDE.md): walk the cone of files I authored or modified across the past week's sessions; verify each `*.qa.json` sidecar has current `source_hashes` + `criteria.<crit>[-1].reviewer.script_hash`. Refresh up to 10 sidecars in one commit.

**Rationale:** Aligns with the QA-cluster surge on main; defensive maintenance.

### 4. Lake-cache restore-discipline tooling — quick wins

Per [`2026-06-07-lake-cache-restore-discipline.md`](../coordination/2026-06-07-lake-cache-restore-discipline.md) and [`2026-06-08-lean-cache-architecture.md`](../coordination/2026-06-08-lean-cache-architecture.md): the per-package cache seed design (PR #1957 producer + PR #1967 consumer) is end-to-end verified. If any of my Lean files added to `QOU` cause cache misses, document and seed.

**Rationale:** Infrastructure cost is paid by future agents; my contributions during this past tranche included scaffold Lean (`IwahoriHecke/Defn.lean`, `LRCoefficientHecke`, `WenzlAOperator`) — verify they land in the seeded cache cleanly.

## What I should NOT pick up

- **Wenzl operator-valued combiner-convergence (gap #4 of #1543's scope).** Parked pending upstream KLR. Re-pitching this without owner direction would burn a session.
- **Demazure-Lusztig variant for Q_β c_3.** Already refuted at the preflight stage (Composite 1 sign-flip at u²); proposing a v2 would violate CLAUDE.md §"Precision goals" no-new-ansatz rule.
- **A new "Open Math X" framing on anything.** The corpus-grep discipline I installed should catch this; verify any "open" claim against the checklist (CLAUDE.md §"Before declaring 'open'").

## Coordination

This workplan is **not** part of any specific multi-PR thread; it's a strategic refresh of my own session queue. No coordination comments warranted unless I pick up item 2 (Option-E extension), at which point I should post intent on PR [#1516](https://github.com/litlfred/qou/pull/1516).

The STATUS.md dashboard is up-to-date as of 2026-06-01 and lists all active threads; consult it at the top of every new session.

## References

- Explore-agent triage report: in-session synthesis (Reading the 2481-commit log; covered above).
- [`STATUS.md`](../../STATUS.md) — current dashboard.
- [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md) — 1ppQ Q_β master ledger (cont. 16 most recent).
- [`docs/coordination/option-e.md`](../coordination/option-e.md) — Δ_λ closure ledger.
- [`docs/coordination/2026-06-07-lake-cache-restore-discipline.md`](../coordination/2026-06-07-lake-cache-restore-discipline.md) — gating infrastructure.
- [`docs/audits/README.md`](../audits/README.md) — audit-doc process (installed in #1543).
- [`docs/audits/2026-05-31-binding-magic-A-wireup.md`](../audits/2026-05-31-binding-magic-A-wireup.md) — prior session's master audit.
- PRs I merged in the prior session: [#1515](https://github.com/litlfred/qou/pull/1515), [#1524](https://github.com/litlfred/qou/pull/1524), [#1532](https://github.com/litlfred/qou/pull/1532), [#1543](https://github.com/litlfred/qou/pull/1543).
