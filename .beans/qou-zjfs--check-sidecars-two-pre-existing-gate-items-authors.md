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


## 3. RETRACTED (2026-08-23) — the drain is safe; this was an off-pin clone

**Everything in this section is withdrawn.** It reported that a per-block
`qa-sweep` degrades verdicts and can erase findings, and told agents not to drain
sidecars here. That is wrong.

The cause was the platform clone sitting at `c396c1f`, **65 commits behind the
pin** `e1030e8` — `qa-sweep` dirties the clone on every run, which makes
`setup-folio-assistant.sh` silently skip its checkout step forever. Re-tested at
the pin, `physics-names-knot-operations` gives **0 verdict changes** and keeps its
recorded major.

The drain then ran for real: **45 blocks, 4 verdict changes**, every one
enumerated and accounted for (PR #5553) — two *new* findings surfaced, two cleared
by legitimate re-evaluation against content that had moved. Not the 39 changes
this section reported.

Root cause and the guard that now catches it: bean `qou-a5p6` / PR #5549
(`report_off_ref` warns when the clone is not at the pin).

**§1 and §2 above are unaffected** — §1's 376/51/325 measurement is computed from
committed `.qa.json` bytes, independent of clone version, and it is what made the
45-block drain correctly targetable.

The original text follows, kept because the reasoning is the record of how it went
wrong.

### (retracted) A per-block `qa-sweep` in this environment is LOSSY

Attempted the ≤ 10-sidecar idle drain against the 51 (from §1's corrected count).
It worked mechanically — 10 blocks swept, all criterion-fresh afterwards, and
`source_hashes.md` refreshed too — **and the diff was not safe to commit.**
Discarded; nothing pushed.

Diffed all 9 changed sidecars against `origin/main`: **39 verdict changes**, none
of them the harmless hash/timestamp refresh the policy contemplates.

| change | count | why it matters |
|---|---|---|
| `detangler-*` `pass` → **`n/a`** | 36 (4 criteria × 9 blocks) | the detangler checkers produce **no verdict** in this container — a single-block sweep evidently cannot supply the graph/chapter context they need |
| `detangler-no-forward-ref` **`fail`/major → `n/a`** | 1 (`physics-names-knot-operations`) | **erases a recorded major finding** and replaces it with "not applicable" |
| `q-usage-narrative-chapter-mismatch` `pass` → `warn` | 3 | new warnings, uninvestigated |

The middle row is the stopper. A `chore(qa-sweep)` commit that reads as routine
would have quietly turned a red into a non-verdict — the audit-dodging shape
AGENTS.md §1a forbids, arrived at by tooling rather than intent.

**Consequence for the idle policy.** AGENTS.md §0b tells an idle agent to refresh
≤ 10 stale sidecars per pass. In *this* environment that instruction is unsafe:
the refresh degrades every `detangler-*` criterion to `n/a` and can drop findings.
Either the drain needs an environment where the detangler checkers run, or the
sweep needs to preserve a criterion it cannot evaluate instead of overwriting it
with `n/a`.

This also retroactively explains why reverting the incidental `intro.qa.json`
rewrite earlier was right — same 556-line diff, same degradation, undiagnosed at
the time.

**Bonus correction to §1.** The pilot showed `qa-sweep` *does* rewrite
`source_hashes.md` when it actually runs on a block. So §1's "the top-level hash
is never refreshed" is too strong — what is measured is the *state* (376 top-stale
vs 51 criterion-stale, 325 false positives); the mechanism is not established, and
I am not going to guess at it a fourth time.

**Also measured, and it partly un-retracts §1's second retraction:** direct
per-block targeting **is** a no-op for label-less `prose()` blocks — confirmed on
two (`blocks: 0`), against `blocks: 1` for a labelled sibling. Of the 51, **45 are
labelled** (directly targetable) and **5 are label-less**. So the enumeration gap
is real; what was wrong was calling it the cause of the 325.
