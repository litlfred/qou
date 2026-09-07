---
# qou-1y5d
title: 'REFUTED: bypassing WitnessBuilder does not predict raw-float64 dirt — 1 of 84 vs 132 of 957'
status: completed
type: task
priority: normal
created_at: 2026-09-07T08:27:41Z
updated_at: 2026-09-07T08:28:13Z
---

## What I proposed, and why it is wrong

At the end of the previous turn I wrote that `qou-x631` "has now produced three
dirty witnesses in two days" and that "the durable fix is at that epic's probe
template". I then found what looked like the mechanism: **all six probes in that
family write their witness with raw `json.dumps` and none uses
`WitnessBuilder`** — so they never touch `_precision.fmt`, which is exactly why
their floats reached the record.

That story is coherent, it fits all three cases, and it is **false as a general
mechanism.** Measured corpus-wide over every `computations/*.py` that writes a
`*.witness.json` (excluding `_deprecated/`):

| route | producers | with a baselined dirty witness | dirty fields |
|---|---|---|---|
| hand-rolled `json.dumps` | 106 | **0** (0.0 %) | **0** |
| via `WitnessBuilder` | 957 | **132** (13.8 %) | **6,129** |

The correlation runs the **opposite** way to my hypothesis. Bypassing the
canonical builder does not predict dirt; the dirt is overwhelmingly in
producers that *do* use it.

## Ruled out as a resolver artifact

The first table resolves producer→witness by filename stem, which could hide
hand-rolled producers that name their witness differently. Re-measured by
reading the **literal witness filename out of each source**: of the 106,
**84 name their witness as a string literal** (22 build it dynamically), and of
those 84 exactly **one** has a baselined dirty witness —
`derived_masses.py` → `free-neutron-decay.witness.json`, 19 fields.

So the 0 is real, not a measurement gap. **1 of 84 against 132 of 957.**

## What this means

- **There is no template fix to make.** The three `qou-x631` probes were
  hand-rolled *and* dirty; that is a property of those three, not of the route.
  Building a "producers that bypass WitnessBuilder" detector would flag 105
  clean files to catch 1.
- **`WitnessBuilder` is not a precision guarantee either**, which is the more
  useful half of this. 132 of its 957 users still write raw float64 — the
  builder serializes what it is handed, and `fmt` is the author's call at each
  field. That is consistent with everything drained this session: every fix was
  at a `float(...)` **call site**, never at the writer.
- **The existing guard is the right shape and is already wired.**
  `scripts/precommit-precision-warn.sh` is a `PreToolUse` hook in
  `.claude/settings.json` (line 44) running the raw-float64 ratchet on
  witness-touching commits. It is **warn-only by owner ruling (2026-08-25)** —
  the push-side block was offered and declined. So new dirt landing is the
  designed behaviour, not a hole.

## The honest residual

Three dirty witnesses from one epic in two days is still a real rate, and I
drained them after the fact each time. But the mechanism is not the witness
writer, so a structural fix would have to key on something else — and I do not
have a candidate that survives measurement. Recording the refutation rather
than shipping a detector built on a story that does not hold.
