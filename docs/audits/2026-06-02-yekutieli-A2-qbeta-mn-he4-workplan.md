# Yekutieli-A.2 / Q_β Habiro / m_n wrapper / ⁴He channel-split workplan (2026-06-02)

**Branch:** `claude/yekutieli-A2-qbeta-mn-he4-channels-2026-06-02`
**Status:** Workplan stub; probes follow.
**Triggered by:** user 2026-06-02 "C D A B E" after PR #1675 merge.

## Scope

Four structural-research probes + one main-landing triage:

| # | Goal | Source |
|---|------|--------|
| C | Yekutieli Session A.2 — τ_q EM gauge coupling at h² | PR #1675 Item 4 NEGATIVE re-aim |
| D | Q_β Habiro element identification | research-queue.json (untouched) |
| A | m_n wrapper categorical analysis | PR #1675 Item 2 verdict (X(q) OK, wrapper suspect) |
| B | ⁴He channel-split categorical constraint | PR #1675 Item 3 verdict (underdetermined) |
| E | Triage `fc092f4e3` (Fermi-stat Lean + Q_β cross-atom) | main landing, may inform D |

## Sequence (per user)

C → D → A → B → E

## Discipline guards

- All probes: cross-anchor (q_proton AND q_muon) where applicable
- Tier verdicts; no fitted closures
- Re-use main commit `58308c24a` (qLambert), `0d58986b6` (post-rebase witness pattern)
- D guard: check `fc092f4e3` first to avoid duplicating Q_β work

## Cross-refs

- PR #1675 (merged) — X(q) Habiro + ⁴He (9,3) + Yekutieli-A first sub-probe
- PR #1673 (merged) — refuted multiplicative X(q) + reframed (4,4,4)
- PR #1662 (merged) — bar-symmetric discipline
- `docs/audits/2026-06-01-yekutieli-mp-substrate-derivation-scaffolding.md`
- `.beans/research-queue.json`
