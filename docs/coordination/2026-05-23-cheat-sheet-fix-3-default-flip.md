# Coordination ledger — cheat-sheet §5 fix #3 default flip

**Goal**: refine the §5 fix #3 closure (`atomic_tr_m_mpfr_50dps.py --method` default) from Python to Rust.

**Owner**: @litlfred (per session-2026-05-23 "work on queue" directive).

## Scope map (2026-05-23)

| PR | branch | role | state |
|----|--------|------|-------|
| **#946** | `claude/rust-tr-m-default-2026-05-23` | **active** — flip default `--method` `hoefsmit-python` → `canonical-rust` | open, ready |
| #895 | `claude/cheat-sheet-fix-3-rust-lr-adapter-2026-05-22` | **merged** — wired `--method canonical-rust` option (kept Python default for back-compat) | closed-merged |
| #901 | (already merged) | wired the Rust LR adapter at the kernel level | merged |
| #920 | `claude/cheat-sheet-tracker-2026-05-22` | meta-tracker — marks fix #3 ✅ closed by #895+#901+#915 | open |
| #915 | `claude/atomic-tr-m-helium4-wenzl-bridge-2026-05-22` | refactor `atomic_tr_m_helium4` to Wenzl bridge — same family, different file | open |
| #921 | `claude/closed-form-tau-M-refactor-2026-05-22` | §5 fix #4 (closed-form tr_M for `binding_canonical`) — different fix-id | open |
| #935 | `claude/reeb-garside-compute-verification-2026-05-22` | §5 fix #5 (Reeb-flow / Garside verification) — different fix-id | open |

## Classification (skill §2)

- **Overlap**: PR #946 ↔ #895 — same file (`atomic_tr_m_mpfr_50dps.py`), same `--method` choice; #946 is a refinement (default flip), not a re-implementation.
- **Dependency**: #946 depends on #895 (which wired the option); #946 is a sequel.
- **Cherry-pick**: not applicable — #895 already merged, #946 has new content.

The other 3 selected siblings (#920, #915, #921, #935) are sibling-thread coordination (cheat-sheet §5 cluster), no file overlap with #946.

## Coordination actions taken (2026-05-23)

1. **#920**: posted substantive comment explaining PR #946 refines #895's fix #3 closure with the default flip; flagged that the tracker can optionally note the refinement (no row-status change needed).
2. **#915, #921, #935**: posted short FYI comments noting #946 is the §5 fix #3 default-flip refinement, no file conflict.

## Open questions for the owner

- **Is the default flip wanted?** PR #895 deliberately kept `default="hoefsmit-python"` for back-compat. My PR #946 reverses that choice. Same pattern as #886's `--method laurent_q_rust` default flip (which the owner directed). If the back-compat preservation in #895 was a stronger signal than the §5 fix #3 closure direction, please flag and I'll close #946.

## Bench / correctness snapshot

- PR #895's bench: 76-90× speedup at A=3; cross-check rel.diff < 2 × 10⁻³⁰ at 25 dps.
- PR #946 is a pure default change; same Rust kernel, same correctness.
- Graceful fallback (line 198-202) auto-uses Python if `hecke-canonical-chi` binary not built — no regression risk.

## Cross-references

- [`docs/canonical-derivation-cheat-sheet.md §5`](../canonical-derivation-cheat-sheet.md) — Migration Backlog.
- [`docs/coordination/2026-05-22-cheat-sheet-manager.md`](2026-05-22-cheat-sheet-manager.md) — PR #920's per-session ledger (cheat-sheet §5 cluster).
- [`.claude/skills/local/coordinate.md`](../../.claude/skills/local/coordinate.md) — protocol followed.
