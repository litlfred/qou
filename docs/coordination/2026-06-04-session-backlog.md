# Session backlog — 2026-06-04 (canonical-discipline + Geom + QA hygiene)

Durable note of what landed this session and what remains, so the next
agent picks up cleanly. Written at session end per the work-plan policy.

## Landed on `main` this session (6 PRs)

| PR | Theme | Key result |
|----|-------|-----------|
| #1819 | NEGATIVE-finding re-entry guard | AST guard (9 detection vectors) blocks purged `lambda_scale_*` / Yekutieli-`−G·h²` forms from re-entering production compute; strict CI step. |
| #1828 | fitted-labelled audit scope fix | `_deprecated/` + `__pycache__/` excluded from `fitted_labelled_canonical_audit.py`; flagged count 3→0. |
| #1830 | `conj:tau-all-orders-bridge` | Sharpened the Geom open link (Link 5 of `rem:geom-bridge-status`) into a dichotomy: τ is either an order-mixing map or the two sides are distinct invariants. Lean classes (no instances = honest open state). |
| #1837 | h⁶ empirical test | **α is degree-4** (α₆=α₈=0 — the order-6 Q₈ product is traceless); κ infinite. Naive number-level fit is **non-discriminating** (under-determined). Refines, does not resolve, the dichotomy. |
| #1843 | relocate fitted_labelled sidecar | Orphaned script-qa sidecar (script moved to `audits/` in the 2026-06-02 reorg) relocated + refreshed. |
| #1845 | orphan-sidecar sweep | Removed **333** orphaned script-qa sidecars at the pre-reorg `computations/script-qa/` path (183 GONE scripts + 150 MOVED). |

## Remaining backlog (priority order)

### 1. Regenerate the 150 moved-script `script-qa` sidecars (QA hygiene)
The 150 MOVED scripts deleted in #1845 now have **no** per-script
aggregate until a full `script-sweep` regenerates them at the correct
subdir path (`computations/<subdir>/script-qa/<name>.script-qa.json`).
The authoritative per-criterion data is safe in
`content/pipeline/script-sidecars/` — this is a regeneration, not a
recovery.
- **How:** `bun run content/pipeline/script-sweep.ts` (full, or
  `--filter` per subdir to keep diffs reviewable). Heavy: 150 scripts ×
  8 checkers; touches the criterion store (`last_run_at` + per-entry).
- **Watch:** coordinate with `qa-staleness-per-entry-srchash` sibling
  (it owns staleness-detection granularity) before a broad criterion-store
  write.

### 2. Geom: the banded-kernel Lean refinement (the real open formalisation)
Per #1837, `conj:tau-all-orders-bridge` hypothesis (1) is **trivially
inhabited** at the number level — even a single T at all orders is
vacuous because each row of T has independent free entries. The genuine
open content is a **finite-support / banded-kernel** constraint on T
(`T_{k,j} = f(k−j)`, a convolution from a fixed categorical operator),
which a fibre-functor realisation of τ would supply. Adding that
constraint to the `TauOrderMixingMap` Lean class is the non-trivial next
step; without it the conjecture collapses to excluded middle.
- Full context: [`docs/coordination/2026-06-04-geom-tau-all-orders.md`](2026-06-04-geom-tau-all-orders.md).
- The dichotomy is **documented as open** — do not force a resolution
  (three-calibration discipline).

### 3. Optional: add a paper `-- Ref:` to `fitted_labelled_canonical_audit.py`
Copilot (#1843) noted `has_references_to_paper: fail` for this infra
script. It's a legitimate minor finding (the audit checker reads metadata
only); clearing it means adding a real paper reference to the *script*
content, not hand-editing the generated sidecar. Low priority.

### 4. Remote branch cleanup (blocked)
~1640 `claude/*` branches remain on `origin`; this session's local
merged branches were deleted, but **remote** deletes return HTTP 403
(same account-level wall as the CI billing block). Cherry-equivalence to
`main` is verified, so the work is safe — this is GitHub branch-page
cruft only. Retry when the 403/billing wall clears (owner action).

## Standing environment facts (for the next agent)

- **CI is `ci=billing`** — every workflow dies in ~3 s at provisioning;
  red CI is the billing wall, **not** code. Local validators
  (`bun run validate <paper>`, the `--strict` audits) are the merge gate.
  See [`2026-06-04-ci-billing-blocked.md`](2026-06-04-ci-billing-blocked.md).
- **Gemini review** is daily-quota-limited (recovers in ~24 h);
  **Copilot** reviews intermittently ("unable to run full agentic suite"
  but still posts substantive comments).
- **Lean (elan) is offline** in this sandbox (`release.lean-lang.org`
  unreachable); `.lean` is verified by design (`native_decide` / `rfl` /
  class-only skeletons) and by CI when billing restores.
