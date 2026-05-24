# Coordination ledger — Library-reuse production-readiness

**Goal:** Promote QOU compute infra to publishable PyPI / npm / WASM artefacts per [workplan v2](../workplans/2026-05-24-library-reuse-production-readiness.md).

**Started:** 2026-05-24

## In-flight PRs

| # | Branch | What | Owner | State |
|---|---|---|---|---|
| #1066 | `claude/stoic-einstein-IhoId` | Workplan v2 doc | mine | reviewer ✅, awaiting merge |
| #1068 | `claude/qou-substrate-2026-05-24` | qou-substrate package scaffold + Phase B shim flip | mine | 10/10 unit tests ✅, validate-CI ⚠ failing setup-phase |
| #1072 | `claude/hecke-core-audit-2026-05-24` | hecke_core.py canonical/exploratory audit (prereq for pyhecke 1.0) | mine (audit agent) | draft, no checks yet |

## Sibling-PR triage (2026-05-24, claude/qou-substrate-2026-05-24)

| # | Title | Relationship | Action taken |
|---|---|---|---|
| #1062 | Library-reuse v1 workplan (Copilot) | **superseded by #1066** | posted close-by-reference comment (`4527559358`) |
| #1063 | Family A +2.89 % gap audit | adjacent (same mass-pipeline area; cites `hecke_core._q_gaussian_character_approx` which #1072 just flagged EXPLORATORY) | posted context comment (`4527558734`) |
| #1065 | low-isotope mass-table wrapper | **direct dep** — imports the three shimmed substrate-infra files | posted "no code change required" + canonical-binding-entry pointer (`4527558230`) |
| #1067 | script-quality baseline (1097 sidecars) | indirect — my Phase B may re-classify 3 of the 1097 audited scripts | posted false-positive-risk note + post-merge resweep nudge (`4527559089`) |
| #1074 | archimedean-wall checker fix | merging to main; my branch is behind | rebase after #1068 merges |
| #1075 | PR #31 redo workplan (figures) | non-overlap | skip |
| #650 | q-CLT scoping (Copilot draft 12 d stale) | non-overlap (cites `hecke_core.py:1847+` but it's a content-side question) | skip |
| #411 | Lake workspace baking (Copilot WIP) | infra-only | skip |

## Main delta (§8a, 2026-05-24)

My branch is 5 commits behind `origin/main` / 3 ahead. New on main since fork (`b918c27d`):

| Commit | What | Touches my scope? |
|---|---|---|
| `d128bdee` PR #1069 | coord doc: f64-default regression finding | no |
| `58a3dffc` PR #1070 | coord doc: RETRACT f64-default claim | no |
| `7df4a59e` PR #1071 | mass-table metadata + knot_operators sigma_inv signs | indirect (touches `canonical_mass_table_extended.py`; my PR doesn't) |
| `fb301ad0` PR #1073 | same as above, follow-up fix | indirect |
| (one more, TBC) | — | — |

**Decision:** rebase **after** PR #1068 merges, not before. The shim flip in `a88745f7` and the mass-table fixes are in disjoint files; no merge conflict expected. Doing it now would entangle the substrate work with the mass-table fixes for the reviewer.

## Open coordination questions

- **PR #1068 validate-CI failure** — needs log access to diagnose. Local full-script repro is green; failure is in the 29 s setup phase before any Python runs. Pending owner help or workflow re-run.
- **PR #1062 close** — should be closed by reference to #1066 (posted intent, awaiting close).
- **PR #1072 hecke_core split implementation** — the audit is done; the actual move-to-`_deprecated/hecke_core_legacy.py` for 29 EXPLORATORY + 12 utility-of-exploratory functions is the next branch (`claude/hecke-core-split-2026-05-24` or similar). Blocked on owner OK of the classification table.

## Out-of-scope siblings to NOT add without explicit OK (skill §8b)

Per skill §8b, do not silently expand scope. These are observed siblings that might *seem* related but should be left to their own owners:

- **#1067 / #1074** (script-quality sweep + drain) — Carl Leitner's QA workstream; coord-comment only.
- **#1063** (Family-A gap) — Carl Leitner's diagnostic; coord-comment only.

If the owner says "fold X in", do it; otherwise stay in lane.
