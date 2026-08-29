---
# qou-g7z6
title: Drain the mass-endomorphism sidecar backlog (126/126 stale)
status: in-progress
type: task
priority: normal
created_at: 2026-08-29T12:04:07Z
updated_at: 2026-08-29T12:04:08Z
---

Surfaced while verifying #6016, not caused by it.

`bun run folio-assistant/content/pipeline/qa-staleness.ts content/quantum-observable-universe/mass-endomorphism`
reports **126 blocks; fresh=0, stale/partial=126** on 2026-08-29. Pre-existing.
#6016 refreshed exactly one sidecar — the block whose `.lean` it renamed — and
reverted the other 127 so a rename PR did not become a chapter sweep.

**Why this is a batch audit run, not idle-pass work.** A chapter-scoped
`qa-sweep` rewrites all 128 sidecars in one go, which AGENTS.md explicitly
sanctions as a single bulk commit ("regenerate N sidecars after checker fix")
— but the idle-backlog policy caps a pass at ≤ 10 sidecars, so this does not
fit there.

**Most of it is not mechanical.** The stale sets are dominated by
agent-reviewed criteria — `da-*` (13 of them), `voice-*`, `proof-rater-*`,
`expo-milnor-clarity`, `milnor-brevity` — which a sweep marks
`[needs-agent]` rather than resolving. The script criteria re-run cheaply; the
agent ones are the actual cost, and whoever takes this should scope that first.

Two measured cautions for whoever does:
- `qa-sweep` / `qa-staleness` take a **directory**; a file path dies `ENOTDIR`.
- Never hand-edit a sidecar to clear staleness.

Unclaimed as of 2026-08-29; opened so it is not lost in a chat transcript.


---

## 2026-08-29 — SCOPED. The split is 37 % mechanical / 63 % agent

The bean asked whoever took this to scope the agent share first. Measured, on
`origin/main`:

    126 blocks, ALL `PART` (none fresh, none wholly stale)
    3,130 stale criterion-occurrences over 98 distinct criteria

      automated (script, cheap re-run)   1,155   36.9 %
      agent-reviewed (the real cost)     1,975   63.1 %   over 39 distinct criteria
      unresolved                             0    0.0 %

So the bean's qualitative call — *"most of it is not mechanical"* — is right,
and the number is **63 %**, not a handful of criteria.

**Classify by the registry's `automated:` field, not by the name prefix.** The
prefix is not a reliable guide: `proof-*` splits across both kinds
(`proof-lean-compiles` is automated, `proof-rater-novelty` is not), and the
whole `trap-*` family is agent despite looking like a lint. Source of truth is
`folio-assistant/content/pipeline/qa-criteria-registry.ts`, which carries
`automated: true|false` on each of its 121 entries (80 automated, 41 agent).

**A parser caution, because it bit here and it is the usual class.** A first
pass matched whole registry entries with `\{\s*id:\s*"..."(.*?)\n  \}` and
silently dropped **41 % of the occurrences** into "not in this registry" —
every `da-*` and every `trap-*`, i.e. exactly the agent-heavy families whose
size is the question. They were in the registry all along; the entry-boundary
pattern did not match them. Walking `id:` markers and taking the first
`automated:` before the next `id:` resolves all 98 criteria with none left
over. If a scoping run reports a large unclassified bucket, suspect the parser
before believing the bucket.

**Heaviest agent criteria** (occurrences): `fit-section-chapter` 95,
`da-false-claim` 95 and each of the twelve other `da-*` at 95, `milnor-brevity`
76, `expo-milnor-clarity` 76, then the `proof-rater-*` trio and the
`proof-no-*` family at 33 each.

### What this means for whoever drains it

- The **mechanical 37 %** is one sanctioned bulk `qa-sweep` over the chapter
  directory — AGENTS.md permits the single bulk commit for exactly this.
- The **agent 63 %** is not drained by that sweep; it is *marked*
  `[needs-agent]`, which converts a silent backlog into an explicit queue of
  ~1,975 judgements. That is a real budget, and it should be a deliberate
  decision rather than a side effect of running the sweep.

Not run here: firing a 128-file sidecar rewrite that also opens a ~2,000-item
agent queue is a scoping decision for the owner, not an idle-pass action. The
measurement above is what was missing to make that decision.
