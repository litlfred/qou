---
description: Dispatch one or more background sub-agents against parallel fronts with a standardized live progress contract, and monitor them on a 2-minute heartbeat (consolidated DID/DOING/NEXT/BLOCKERS synthesis, with real log tails — not static "still running").
---

Run the **`local/dispatch-agent`** skill. The full protocol lives in
[`.claude/skills/local/dispatch-agent.md`](../skills/local/dispatch-agent.md);
this command is the user-invocable wrapper.

## Quick checklist (read the skill for details)

1. **Scope one agent per independent front**; give each a short stable
   `<LABEL>`. Use `isolation: "worktree"` when agents mutate files.
2. **Paste the §1 progress contract** into every agent prompt — the
   `### ⟦PROGRESS⟧ <LABEL> · step N` block with DID / DOING / NEXT /
   BLOCKERS, live log tails, advancing step counter.
3. **Launch all agents in one message** (parallel `Agent` calls); record
   each `agentId ↔ LABEL` in `/tmp/<session>-dispatch-map.txt`.
4. **Arm the 2-minute heartbeat** before ending the turn: run
   `python3 scripts/agent-progress.py <tasks-dir>`, post ONE consolidated
   table (one row per agent, newest block), then `ScheduleWakeup`
   (`delaySeconds: 120`, prompt `/dispatch-agent heartbeat`) to re-tick.
5. **Nudge silent agents** (`SendMessage`) if a block is > 3 min stale.
6. **Verify each `⟦DONE⟧` yourself** (lean-direct exit 0, sorry-free)
   before merging — the agent's self-report is a claim, not proof. When
   all agents are `[DONE]`, post the final synthesis and
   `ScheduleWakeup({stop:true})`.

Special arg: `/dispatch-agent heartbeat` — a re-tick (from the scheduled
wakeup): run the extractor, post the consolidated synthesis, re-arm or
stop per §3b/§4.

**Anti-patterns:** going dark (no heartbeat), semi-static updates (no log
tail / no step counter), reading the full `*.output` JSONL into context,
trusting a DONE line without re-verification, or ticking slower than the
2-minute cadence the user asked for.
