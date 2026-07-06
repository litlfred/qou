# Coordination Ledger: #840 Stage 2 (Prop Revival)

**Date:** 2026-05-20  
**Session:** coordinate skill / PR #840 Stage 2: wire 5 propositions from #819 catalog  
**Status:** Review triage complete; all Copilot review items addressed (witness filename renamed, provenance wrapped via `WitnessBuilder.wrap_legacy`, scipy added to `requires`)

## Scope Map (10 sibling PRs)

### Overlapping Infrastructure

| PR | Title | Overlap | Relationship | Impact |
|----|-------|---------|--------------|--------|
| #823 | QA exhaustive checkers + sweep | Yes — QA sidecars | Blocks indirectly (stale on merge) | Expected; ci(qa-sweep) will refresh post-#840-merge |
| #818 | I1 Hecke/Hoefsmit probes | Minimal — witness provenance | Shares audit trail | Low risk; non-blocking |

### Independent (No Overlap)

| PR | Title | Domain | Status |
|----|-------|--------|--------|
| #839 | Lean typed stubs round 9 | Lean formalization | Orthogonal |
| #836 | c_5 follow-ups | Lean closed-forms + Python probes | Orthogonal |
| #841 | FR pullback k=1,2 identification | Empirical knot selection | Orthogonal |
| #827 | FR pullback k=3 fixes (DRAFT) | Rust + Python audit | Orthogonal |
| #817 | cor:knot-factor-amphicheiral fix | One .md block edit | Orthogonal |
| #807 | compute-audit P33/P34 patterns | Skill documentation | Orthogonal |
| #738 | detangler story coherence | Infrastructure skill | Orthogonal |
| #761 | Combined 10 open PRs | Hoefsmit/GP stack + audits | Potential CI conflict if merged first; no cherry-pick needed |

## Review Triage (#840)

**Copilot posted 6 review comments across 4 threads (2026-05-20T02:27:55Z).**

| Thread | File | Issue | Classification | Action |
|--------|------|-------|---|---|
| A | `wigner-np-pairing.ts:15` | `b-over-a-witness.json` filename mismatch (wiring audit regex) | **ACCEPT** | **RESOLVED** (commit `46d347d8` 2026-05-20): renamed `b-over-a-witness.json` → `b-over-a.witness.json` and updated `.ts` pointer + script output path |
| B | `catalan-binding.witness.json` | Missing provenance fields | **FIXED in diff** | WitnessBuilder.wrap_legacy() applied; fields present |
| C | `canonical-isospin-pyhecke.witness.json` | Missing provenance | **FIXED in diff** | Fields present |
| D | `atom-level-wedderburn-tower.witness.json` | Missing provenance | **FIXED in diff** | Fields present |
| E | `schur-weyl-mass-decomposition.ts` | Missing `scipy` in `requires` | **FIXED in diff** | scipy added |
| F | `e-infinity-page-identifications.ts` | Missing `scipy` in `requires` | **FIXED in diff** | scipy added |

**Summary:** All 6 Copilot review comments addressed in commit `46d347d8` (witness filename + provenance wrapping + scipy). Second-round Copilot review (`d9912989` rebase + cross-ref enrichment) addressed in commit `7bdb7c4e` (hardcoded CODATA → `codata_constants`, `start_time` for accurate `durationMs` across 4 wrapped scripts).

## Coordination Comments Posted

### To #823 (QA exhaustive checkers)
Documented the expected stale-sidecar event for #840's 5 blocks. Marked as "expected per rollout docs; ci(qa-sweep) will refresh."

### To #840 (status comment)
Consolidated the 6 review threads into a triage table with classifications (FIXED in diff / ACCEPT). Flagged the single manual fix (witness filename) and confirmed sibling independence.

## Main Branch Status

Latest: `2b99fbcb` (PR #831 merge, 2026-05-20).  
No file overlap with #840 scope.

## Next Steps

1. **DONE** (commit `46d347d8`): pushed witness-filename fix to #840
2. **CI validation**: wiring audit should pass after step 1
3. **Merge #840** when CI green
4. **No cherry-pick** between #840 and siblings required; all 10 are independent

## Notes

- The `b-over-a-witness.json` → `b-over-a.witness.json` rename is **already reflected in the file diff** (marked as "renamed" in computations/); only the .ts manifest pointer needs updating.
- All witness provenance fields were correctly added during the PR's work (WitnessBuilder.wrap_legacy applied to all deprecated scripts).
- No blocker PRs identified; merge order is flexible.
