---
# qou-zjfs
title: 'check-sidecars: two pre-existing gate items (authors-note sidecar unreachable; canonical-mass guard false positive)'
status: todo
type: task
priority: normal
created_at: 2026-08-23T13:04:40Z
updated_at: 2026-08-23T13:05:10Z
---

Found while running `scripts/check-sidecars.sh` as the pre-commit preflight on
PR #5538. **Neither item is caused by that branch**; both are recorded here so
the gate's ⚠ is explained rather than ignored.

## 1. CORRECTED — the documented sidecar-staleness test is 86 % false positive

**My first two write-ups of this item were wrong. Both are retracted here.**

*First claim (wrong):* "`check-sidecars.sh` flagged the sidecar as stale."
It does not compute hashes for a content block at all. It greps for criterion
names in a fixed family (`q-usage-*`, `wall-side-correct`, `one-voice-*`,
`da-*`, `*-integrity`, `remark-*`), prints `<none cached>` when that regex
misses, and prints the `→ qa-sweep` line **unconditionally** for every changed
block. `<none cached>` is informational, not a verdict.

*Second claim (wrong):* "`qa-sweep` cannot enumerate label-less `prose()`
blocks." Refuted by timestamps: **12 of 25** stale label-less sidecars were
written *after* their `.md` last changed and still record a mismatched hash.
The sweep reaches them fine.

*What is actually true* — measured on `notation-register`, then corpus-wide:

    source_hashes.ts      = raw .ts bytes                    MATCHES
    source_hashes.md      = e927608180e0                     matches nothing
    per-criterion field_hash.md = cd6f0a9d492b = raw .md     MATCHES (current)

The **per-criterion `field_hash` is live and correct**; the **top-level
`source_hashes.md` is never refreshed** when criteria are re-run. The `ts` one
looks right only because the `.ts` rarely changes. Sidecars in this state show
`field_hash` sets containing *both* the stale top hash and the current one — the
sweep appends per-criterion entries without rewriting the header.

**Corpus-wide, over the 3612 blocks with both a `.qa.json` and a `.md`:**

| measure | count |
|---|---|
| top-level `source_hashes.md` stale | **376** |
| per-criterion `field_hash.md` stale | **51** |
| both stale (genuinely unswept) | 51 |
| top stale, criteria fresh — **false positive** | **325** |

So **86 % of apparent sidecar staleness needs no work**, and the real backlog is
51 blocks, not 376.

**Why this costs real budget.** AGENTS.md §"Refresh stale sidecars + witnesses"
tells agents to key staleness on `source_hashes.{md,ts,lean}` and caps the idle
pass at ≤ 10 sidecars. An agent following that spends its whole budget on blocks
whose cached verdicts are already current. This is the same failure mode AGENTS.md
already documents one field over for `witness.scriptCommitSha` — *"two false
positives and zero true positives ... it spent the idle-pass witness budget on
producer re-runs that fix nothing."*

**Fix belongs upstream, not here.** Either `qa-sweep` should rewrite
`source_hashes` when it rewrites criteria (it lives in `litlfred/folio-assistant`),
or AGENTS.md should key the documented staleness test on `field_hash` instead.
Owner call which; do not hand-edit sidecars either way.

## 2. canonical-mass status guard: false positive

    computations/binding_hbarq_rung_forward_test.py:30
    mass: m_p/(m_e·Vol(𝓑₃)) = ρ_p/ℏ_q² ≈ 258  (ρ_p = linking_weight ≈ 2.53, O(1))

The guard looks for a **deprecated absolute-mass status figure** (966 / 406 /
2.89 % / −57 %). This line cites none of them: it is a *ratio* inside an
explicit ℏ_q→0 **scaling** argument ("the mass multiplier is O(1/ℏ_q²) while
the binding multiplier is O(1)"), not a claim about `m_p`'s live accuracy. The
guard is matching the `m_p/(m_e·Vol(𝓑₃))` shape.

Per the guard's own message this wants an `ALLOWLIST_SUBSTR` entry. Left alone
on #5538: unrelated domain (mass/binding vs Specht/RSK), someone else's file,
and a one-line allowlist edit belongs with whoever owns that guard's tuning.
