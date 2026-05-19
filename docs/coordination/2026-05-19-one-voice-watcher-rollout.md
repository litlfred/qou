# 2026-05-19 — one-voice watcher rollout coordination

## Goal

Roll out the `one-voice-integration-watcher` + per-block QA sidecar
infrastructure landed in PR #821 across the sibling-PR set, then
proceed to: (a) more automated checkers (reduce needs-agent
backlog), (b) exhaustive sweep across remaining sections,
(c) start the watcher in idle-sweep mode, (d) wire the QA gate
into CI.

## Baseline

| Item | Value |
|------|-------|
| Origin PR | [#821](https://github.com/litlfred/qou/pull/821) — merged 2026-05-19 |
| Merge SHA | `b8d4b15c` |
| Author | litlfred (via Claude Code) |
| Schema | [`folio-assistant/schemas/block-qa.ts`](../../folio-assistant/schemas/block-qa.ts) (`BlockQaReport`, `QaCriterionEntry`) |
| Skill | [`.claude/skills/local/one-voice-integration-watcher.md`](../../.claude/skills/local/one-voice-integration-watcher.md) |
| CLI | `content/pipeline/qa-{sweep,staleness,merge-findings}.ts` |
| Test sweep | `content/quantum-observable-universe/organic-chemistry/` (16 blocks, 8 automated criteria pass / 3 adjudicated pass) |

## Sibling scope map

| PR | Branch | Relevance | Classification | Coordination comment |
|----|--------|-----------|----------------|----------------------|
| #820 | `claude/detangler-bib-followup-batch-2026-05-19` | 654 Ref upgrades touch many `.md`; will flip sidecars stale on merge | **overlap-content** (heavy churn, sidecar-relevant) | [#issuecomment-4490122558](https://github.com/litlfred/qou/pull/820#issuecomment-4490122558) |
| #806 | `claude/lean-substantive-pass-2026-05-19` | 188 Lean canonicals enriched; `wall-side-correct` and `voice-scholarly-default` directly fire | **overlap-content** (Lean + manuscript prose) | [#issuecomment-4490123664](https://github.com/litlfred/qou/pull/806#issuecomment-4490123664) |
| #738 | `claude/detangler-story-coherence` | "Story coherence first-class" overlaps `fit-section-chapter` criterion | **dependency-possible** (cherry-pick candidate either direction) | [#issuecomment-4490124827](https://github.com/litlfred/qou/pull/738#issuecomment-4490124827) |
| #807 | `claude/compute-audit-P33-P34-2026-05-19` | Parallel watcher-skill work; QA sidecar schema could host compute criteria too | **infra-mirror** (registry extension candidate) | [#issuecomment-4490125949](https://github.com/litlfred/qou/pull/807#issuecomment-4490125949) |
| #801 / #814 / #816 / #817 / #818 / #822 | various proof / probe branches | Single-block scope; watcher idle-sweep will catch on merge | **independent** (no comment needed) | — |
| #761 | `claude/combine-all-open-prs` | Combined umbrella PR; QA infra arrives via #821 merge | **inherited** (no separate comment) | — |
| #774 | `claude/iw-meta-tighten-guarded-off-heuristic` | Meta-watcher heuristic change, unrelated domain | **independent** | — |

## Coordination posture

- **Outbound:** four comments posted (see table above).
- **Inbound:** no sibling has flagged a conflict with #821 yet.
- **Cherry-pick candidates (either direction):**
  - From #738 → us: a `story-coherence` signal that the
    `fit-section-chapter` automated checker could read.
  - From us → #807: the multi-reviewer sidecar pattern, registered
    `domain: "compute"` criteria.

## Next-branch work (planned)

New branch: **`claude/qa-exhaustive-checkers-and-sweep`** (or similar).
Scope:

1. **More automated checkers.** Promote `voice-ai-slop` from
   agent-only to heuristic + agent (the heuristic catches obvious
   tells; agent handles borderline). Add `voice-scholarly-default`
   heuristic (second-person address, lecturer cadence patterns).
2. **Exhaustive baseline sweep.** Run `qa-sweep` across every
   chapter in `content/quantum-observable-universe/`, dispatching
   the agent for non-automated criteria. Persist sidecars.
3. **Start the watcher.** Arm `/integration-watch one-voice` so
   the idle sweep picks up any block that goes stale.
4. **CI wiring.** Add `bun run qa-sweep:ci` to a workflow step so
   PRs fail on critical findings.
5. **Ledger continuation.** Append per-section sweep results to
   this file as the rollout progresses.

## Anti-patterns to avoid

- ❌ Re-running sweeps over `organic-chemistry/` (already covered;
  16/16 fresh). Idle sweep will refresh only if a block changes.
- ❌ Mixing the QA-infrastructure work with the sibling rollout
  comments — coordination is informational, the work is on a new
  branch.
- ❌ Adding compute criteria to the registry before #807 lands —
  let that PR own its domain; offer the schema, don't pre-empt.

## Round 2 — auto-detect-new-skills convention (2026-05-19 T17:47Z)

Added a new rule across three skill files so in-flight branches
detect newly-added skill files on every `git fetch origin main`
and prompt the user before adopting (via AskUserQuestion).

| Skill | Section added | What it does |
|-------|---------------|--------------|
| `local/watch.md` | §3.Q3a | `/watch` flow: scan `--diff-filter=A` for new `.claude/skills/local/*.md` files; prompt 3-chip adopt/defer/skip |
| `local/coordinate.md` | §8a-bis | Coordinator triage cycle: same scan during §8 watch-main pass |
| `local/integration-watcher.md` | §3c | Parent contract: all five integration-watcher children inherit the rule automatically |

Convention published in PR #823 commit `7176d54c`. One-time
announcement comments posted on the four siblings:

| PR | Comment |
|----|---------|
| #820 | [#issuecomment-4490469971](https://github.com/litlfred/qou/pull/820#issuecomment-4490469971) |
| #806 | [#issuecomment-4490471321](https://github.com/litlfred/qou/pull/806#issuecomment-4490471321) |
| #738 | [#issuecomment-4490472275](https://github.com/litlfred/qou/pull/738#issuecomment-4490472275) |
| #807 | [#issuecomment-4490473244](https://github.com/litlfred/qou/pull/807#issuecomment-4490473244) |

Future skill landings (after this round) will be auto-discovered
by every in-flight branch's next `/watch` or `/coordinate` cycle
without manual announcement. The cost-saving target is sibling-PR
review churn caused by branches that didn't know a relevant new
infrastructure had landed.
