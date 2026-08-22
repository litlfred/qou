---
# qou-tqr9
title: 'Agent-adjudicated QA axes are silently lost by "regenerate rather than merge" conflict resolution'
status: in-progress
type: task
priority: normal
created_at: 2026-08-19T21:20:00Z
updated_at: 2026-08-22T02:30:00Z
---

The standard resolution for a `.qa.json` conflict is: do not hand-merge
generated output, let `qa-sweep` regenerate it against the merged tree
(`local/integration-audit`). That is right for **script** criteria and
wrong for **agent-adjudicated** ones, and nothing in the tooling marks
the difference at the point where an agent is choosing a resolution.

Measured instance. The #5103 takeover (`0afc0097f`) resolved 742 sidecar
conflicts to main's side, stating "the honest sidecar state is whatever
qa-sweep produces against the merged tree, which the QA pipeline
regenerates on its next pass." No pass can produce those entries: the
`trap-*` family is `automated: false`, so `qa-sweep` regenerates the
high-recall SCRIPT candidates and never the verdicts. 7381 agent verdicts
over 738 blocks — each one an agent having read a block in full across
ten categories — went back to reading as never-audited. Restored in
`a89de3169` by re-validating each entry's `field_hash.md` against live
main and porting only the 97 % that still certify the current source.

The exposure is not limited to `trap-*`. Every agent-adjudicated axis has
the same shape: `da-*` (devils-advocate), `clarity-*`, `q-usage-*`, and
the `lean-vacuity-review-ledger` verdicts. Each one is expensive to
produce, cheap to drop, and drops **silently** — the sidecar stays
well-formed and the axis just reports fewer findings.

Candidate fixes, cheapest first:

1. **Say it in the skill.** `local/integration-audit` and
   `local/prepare-merge-auto` should carve out agent-kind entries from
   the "regenerate, don't merge" rule, with the reason (a verdict has no
   producer) rather than just the instruction.
2. **Make the resolution mechanical.** A small script that takes the
   union of both sides' agent entries and drops those whose `field_hash`
   no longer matches the merged tree. That is what the restoration did by
   hand; it generalises to any axis and removes the judgement call.
3. **Make the loss visible.** A check that fails when a merge or takeover
   reduces the count of agent-kind entries on any axis, so the drop is a
   red check rather than a silent regression.

Item 2 is the one that would have prevented this without anyone needing
to know the axis was agent-adjudicated.

## 2026-08-22 — items 1 and 2 landed

**Item 2 (the mechanical resolution) is done**, and it is the one that
removes the judgement call:
[`scripts/qa-sidecar-agent-union.py`](../scripts/qa-sidecar-agent-union.py).

    python3 scripts/qa-sidecar-agent-union.py --against <ref> [--apply|--check]

It unions the agent-kind entries of every `.qa.json` at `<ref>` into the
working tree, carrying an entry over only when its `field_hash.md` still
matches the live `.md` — the same per-entry validation the hand
restoration in `a89de3169` did, generalised to any axis, since nothing
in it is `trap-*`-specific. It is additive: it never deletes an entry,
so it cannot itself cause the loss it exists to prevent. `--check` exits
1 when the tree is missing a live-valid entry the ref carries.

Two properties worth keeping if this is ever rewritten. Numbers are
parsed as `Decimal` and re-serialised verbatim, and `ensure_ascii` is
off — a naive `json.dumps` round-trip rewrites `0.000074` to `7.4e-05`
and escapes `Möbius`, which is what made the first hand-restoration
attempt unreviewable (1172 spurious deletions in the diff, against 3
real ones). Round-trip was checked byte-identical on 199/200 sampled
sidecars; the 200th differs only in a trailing newline the source lacks,
and the write path now preserves that too.

**Item 1 (say it in the skill) is done** —
[`local/integration-audit`](../.claude/skills/local/integration-audit.md)
§"Resolving a sidecar conflict" and
[`local/prepare-merge-auto`](../.claude/skills/local/prepare-merge-auto.md)
Phase 1 + anti-patterns. Both give the reason (a verdict has no
producer) rather than only the instruction, and name the measured cost.

**Item 3 (make the loss visible) is still open.** `--check` is the
mechanism; what is missing is a caller — a CI step or a `/prepare-merge`
gate that runs it against the pre-rebase ref and fails red. It stays
open deliberately rather than being marked done by the existence of the
flag: with Actions auto-triggers disabled repo-wide, wiring it into a
workflow buys nothing today, so the honest home for it is the
agent-side merge pipeline.

## 2026-08-22 — why the filter key is `field_hash.md` and not `field_hash`

Raised by the #5367 sibling on PR #5419: the standing advice as worded in the
#5103 note — *"keep the union, drop entries whose `field_hash` no longer
matches"* — **degenerates when a block's `.ts` is rewritten.** `field_hash`
covers the `.ts` as well as the `.md`, so a manifest rewrite makes *both*
sides' entries stale at the same instant and a whole-object filter deletes all
of them. Their worked case: `mass-theory/atomic-q-reeb-universal-rho`, where
#5367 rewrites the `.ts` and the sidecar carries 67 criteria that exist nowhere
else.

**The implemented script is not affected**, and the reason is worth keeping if
it is ever rewritten. [`scripts/qa-sidecar-agent-union.py:180`](../scripts/qa-sidecar-agent-union.py)
reads the **`.md` sub-key only**:

```python
entry_md = (entry.get("field_hash") or {}).get("md")
```

So a `.ts` rewrite carries every entry through; only a `.md` edit drops one.
That is correct for `trap-*` — a trap verdict is a judgement about prose — and
deliberately **permissive** for `clarity-*`, `q-usage-*` and `da-*`, which do
depend on `kind` / `title` / `uses[]`. Permissive is the right direction here:
stale-but-present is recoverable by re-running the axis; deleted is not
recoverable at all, which is the whole reason this bean exists.

**Do not "tighten" the key to the whole `field_hash` object.** It looks like a
correctness improvement and is the failure mode described above.

Separately, and one layer up from the sidecars: `content/pipeline/qa-agent-drain-queue.ts`
— the script that *builds* the audit queue — has two unresolvable imports,
`./qa-utils` and `./qa-criteria-registry`, neither of which exists anywhere in
the tree. Same silent-failure shape as the unloadable manifests #5367 found: if
the queue builder cannot run, "not in the queue" and "already audited" are
indistinguishable from outside. Not part of this bean's fix; recorded here
because it is the same class and the same blast radius.

## 2026-08-22 — CORRECTION to item 2: the filter was dropping 56% of what it protects

Found while building the `qou-supr` checker. The union script's staleness test
read:

```python
if live_md is not None and entry_md != live_md:
    stale += 1; continue
```

When an entry carries **no** `field_hash.md`, `entry_md` is `None`, so
`entry_md != live_md` is true and the entry was **skipped as stale** — silently,
under a message saying the hash "no longer certifies the live `.md`", when in
fact there was never a hash to check.

Measured corpus-wide over 126,156 agent-kind entries:

| producer | entries | without `field_hash.md` |
|---|---:|---:|
| `local/*` | 78,904 | **68,342 (87 %)** |
| `agent:*` | 36,206 | 0 (0 %) |
| everything else | 11,046 | 1,965 |
| **total** | **126,156** | **70,307 (55.7 %)** |

So the script recovered the `trap-*` campaign's own entries perfectly — those
all carry hashes — and would have dropped **87 % of the `local/*` verdicts**,
which are exactly the `da-*` / `clarity-*` / `q-usage-*` axes this bean names as
equally exposed. The one axis it was tested on was the one axis it worked for.

**Fixed**: a hash-less entry cannot be *shown* stale, so it is carried and
counted separately (`N carried without a field_hash.md`). Verified against a
synthetic ref — the hash-less entry is now carried where it was previously
dropped, and a genuinely stale hash is still dropped:

```
no hash      md=None          OLD drops: True   NEW drops: False
stale hash   md=deadbeef0000  OLD drops: True   NEW drops: True
```

This is the direction the bean already argued for and the direction I described
to #5367 as deliberate — *stale-but-present is recoverable, deleted is not*. The
code did not match the argument. It does now.

**What was NOT wrong**: the script is still additive and still never deletes
from the working tree, so it never *caused* a loss. It was incomplete as a
recovery tool, which is a different failure and a quieter one.

