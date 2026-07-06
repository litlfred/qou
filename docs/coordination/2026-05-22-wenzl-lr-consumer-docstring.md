# Coordination ledger — Wenzl-LR consumer docstring fix

**Branch:** `claude/wenzl-lr-consumer-fix-2026-05-22`
**PR:** [#878](https://github.com/litlfred/qou/pull/878)
**Goal:** discharge canonical-watcher queue item
`wenzl-lr-consumer-docstring-fix-2026-05-22` — align the docstring
Status section + witness `description` of
[`rho_k_full_via_wenzl_lr.py`](../../computations/rho_k_full_via_wenzl_lr.py)
with the file-top consumer-bug banner (lines 7-26).

**Scope:** documentation-only. No numerical behaviour change.

## Scope map (sibling classification per `local/coordinate.md §2`)

| PR | Topic | Overlap | Dependency | Cherry-pick |
|---:|---|---|---|---|
| **#878 (this)** | `rho_k_full_via_wenzl_lr.py` docstring + witness desc | — | — | — |
| #818 | I1 Hecke/Hoefsmit probe cluster — 14 probes incl. `prop:hecke-branching-trace-decomposition` | none | **forward-only**: my docstring cites the prop #818 wires as the future non-tensor Wenzl-bridge target. Neither PR blocks the other. | informational |
| #761 | Combined Hoefsmit/GP stack + 1ppb workplan v6 (Rust kernel) | none | **indirect**: my docstring points at `canonical_tr_m_via_rust.py` as the canonical replacement consumer; that script depends on Rust binaries built by #761's kernel. Replacement already exists on main; my doc just points at it. | none |
| #872 | qa-pipeline script-quality scaffold | none | — | — |
| #817 | `cor:knot-factor-amphicheiral` revise | none | — | — |
| #807 | compute-audit P33/P34 patterns | none | — | — |
| #774 | i3 audit heuristic tighten | none | — | — |

## Coordination comments posted

- #818 — single coordination comment classifying as "forward-only
  pointer, no action needed". Link:
  https://github.com/litlfred/qou/pull/818#issuecomment-4519654252.
- #761 — **deliberately skipped**. The relationship is indirect
  (Rust kernel → `canonical_tr_m_via_rust.py` → my docstring
  pointer). The canonical replacement consumer already exists on
  main; my PR just points at it. Per `local/coordinate.md §5d`,
  don't burn cycles when the relationship is weak.

## Discharge

| Action | Result |
|---|---|
| Canonical-watcher queue item `wenzl-lr-consumer-docstring-fix-2026-05-22` | **resolved** in `todos/canonical-watcher-queue.json` |
| Canonical-watcher ledger | appended at `todos/canonical-watcher-ledger.md` (gitignored) |
| Coordination comment on #818 | posted (one-way pointer, no action requested) |
| Coordination ledger (this file) | committed alongside the docstring fix |

## §6 escalations

None. The Wenzl-LR consumer-bug finding was already documented,
the consumer overlay was already disabled, the witness was already
`set_audit_only`, and the canonical replacement
(`canonical_tr_m_via_rust.py`) was already in place. This PR is a
docstring-only consistency fix on top of that prior work.

## Next concrete task (non-overlapping)

Per the resume `AskUserQuestion` answer earlier this session, the
queue's still-open canonical-discipline items are:

1. **P31-class-c-validation-imports** — 18 audit/probe scripts
   mechanical M_P_MEV → M_P_MEV_VALIDATION migration. Best driven
   by `/integration-backlog canonical` (one PR per ≤49-file batch).
2. **P31-class-a-batch** — 5 mass-prediction scripts blocked on
   Workplan-0b's M_N substrate derivation (over_count stalled at
   57; needs the substrate-pure M_N route picked from
   `docs/audits/2026-05-18-workplan-0b-mn-substrate-derivation.md`
   Routes A / B / C).
3. **TR_M_AT_Q0-vs-frobenius-pre-existing** (critical, needs-author) — pre-existing
   conflict tracked in
   `canonical-derivation-pipeline-compliance.witness.json::known_open_conflicts`.

This PR does not advance any of those; they remain queued.
