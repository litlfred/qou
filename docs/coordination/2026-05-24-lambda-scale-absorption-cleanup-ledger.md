# Coordination ledger — `claude/yekutieli-mass-table-gap4-2026-05-24`

**Date opened:** 2026-05-24
**Branch:** `claude/yekutieli-mass-table-gap4-2026-05-24`
**PR:** [#1080](https://github.com/litlfred/qou/pull/1080) (opened 2026-05-24)
**Goal:** Propagate the 2026-05-23 absorption finding (`λ_scale` absorbed into `VolDensity(K)`) into every doc / audit / coord / cheat-sheet that still uses the obsolete "λ_scale closure" framing; clean up stale top-level orphan docs; do a parallel review of Gap #4 closed-form tr_M migration scope.

## Scope map (at /coordinate run, 2026-05-24 evening)

| PR | State | Classification | Relationship |
|---|---|---|---|
| **[#1080](https://github.com/litlfred/qou/pull/1080)** (this) | open | **own** | Framing fix + docs cleanup + Gap #4 finding |
| [#1063](https://github.com/litlfred/qou/pull/1063) | open | **direct overlap** | Family A gap audit + Strategy I (Yekutieli) closure path — Strategy I was PURGED 2026-05-24; absorption framing applies |
| [#1065](https://github.com/litlfred/qou/pull/1065) | open | adjacent | low_isotope mass-table wrapper; uses "Family-A gap" wording |
| [#1072](https://github.com/litlfred/qou/pull/1072) | open | parallel finding | hecke_core canonical-vs-exploratory audit; corroborates my Gap #4 finding |
| #1075, #1066, #1068, #1067, #1074, #1062 | open | low overlap | Workplans, library packaging, QA mechanics — not in critical-path |
| #411, #650 | open | none | Stuck Copilot drafts (April / mid-May) |

## §6 Framing inconsistency surfaced + resolved

A semantic split on `λ_scale` was active across open PRs at the time of /coordinate:

- **Old framing (still in #1063 amendment, #1065 results table, many docs/audits):**
  `λ_scale` is a separate substrate-derived constant; the 2.89% m_p residual is a "λ_scale closure" problem; alternative derivations (Bring-Bloch, Yekutieli per-cell, etc.) compete to land on the categorically-exact value.
- **Current canonical framing (per `ffdd84409`, 2026-05-23):**
  `λ_scale` is **absorbed** into the per-knot `VolDensity(K)` evaluation. There is no separate constant. The 2.89% residual is the gap between the framework's current `VolDensity(𝓑₃)` computation and its categorically-exact value — refinement is a per-knot `VolDensity` problem, not a "λ_scale closure" task. Yekutieli per-cell variant was briefly in production then PURGED 2026-05-24 (`71d674da1`).

**Resolution.** New canonical reference doc [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) created on this branch. AGENTS.md and `docs/canonical-derivation-cheat-sheet.md` both gained prominent top-line warnings pointing at it. Three coordination comments posted on sibling PRs (#1063, #1065, #1072) flagging the framing issue + the canonical reference. No silent rewrites; sibling-PR authors free to revise or push back.

## Commits on this branch

| Commit | Scope |
|---|---|
| [`fbc40b43e`](https://github.com/litlfred/qou/commit/fbc40b43e) | fix(witnesses): m_p formula text λ_Y → λ_A + deprecate broken isotope-mass-table.py |
| [`3edfcea84`](https://github.com/litlfred/qou/commit/3edfcea84) | gap #4 analysis + shared `compute_tau_M_nucleon_H3` helper in `closed_form_tau_M.py` |
| [`d4b727d1a`](https://github.com/litlfred/qou/commit/d4b727d1a) | docs(handover): next-agent orientation carried over from PR #863 |
| [`7e6e7734a`](https://github.com/litlfred/qou/commit/7e6e7734a) | docs(framing): reframe ~3% m_p gap as `VolDensity` refinement, NOT `λ_scale` closure |
| [`56fc7401a`](https://github.com/litlfred/qou/commit/56fc7401a) | docs(cleanup): 32 zero-ref top-level orphans → `docs/_archive/orphan-top-level/`; `docs/README.md` |
| [`79d659d4e`](https://github.com/litlfred/qou/commit/79d659d4e) | docs(framing): canonical `lambda-scale-absorbed-into-vol-density.md` reference; AGENTS.md + cheat-sheet + README all point at it |

## Coordination comments posted

| Sibling | Comment | URL |
|---|---|---|
| #1063 | Heads-up on Strategy I PURGE + canonical absorption reference + suggested touch-up | [#issuecomment-4527581472](https://github.com/litlfred/qou/pull/1063#issuecomment-4527581472) |
| #1065 | "Family-A gap" → `VolDensity(𝓑₃)` gap reframing + canonical doc pointer | [#issuecomment-4527582145](https://github.com/litlfred/qou/pull/1065#issuecomment-4527582145) |
| #1072 | Corroborating finding on `binding_canonical.binding_canonical` as the canonical scalar entry + flag `TR_M_AT_Q0_vs_frobenius_proof` open conflict | [#issuecomment-4527582924](https://github.com/litlfred/qou/pull/1072#issuecomment-4527582924) |

No further comments on the lower-overlap PRs (workplans / packaging / QA mechanics) — not in my critical path; their scope doesn't intersect.

## Cherry-pick map

None planned.  All sibling work either runs independently or is too WIP for cherry-pick.

## Next concrete task

PR [#1080](https://github.com/litlfred/qou/pull/1080) opened 2026-05-24; `/prepare-merge` ran (rebase clean, witness-pipeline refresh committed, validate has 330 pre-existing main-side issues unrelated to this branch); Gemini + Copilot review requested.  Address review comments as they arrive.

Follow-up after merge (not in scope here):
- Extend the audit-doc reframing into the ~10 remaining stale-framing audit docs in `docs/audits/` (flagged by `grep -rln "Family A gap\|λ_scale closure"`); none are blocking.

## Watch main

Will watch `origin/main` for any commit that touches:
- `docs/canonical-derivation-cheat-sheet.md`
- `_li_2_q_util.py` (`lambda_scale_*` / `vol_density_*` functions)
- `m_p_borromean_verification_50dps.py`
- `mass_table_comprehensive.py`

If sibling PRs land that re-introduce the old framing, will append a §6 escalation row here and post on the offending PR.
