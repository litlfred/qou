---
# qou-bake
title: 'GAP: five keystone witnesses are hand-written — no script emits them, and probes read them as inputs'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T12:36:18Z
updated_at: 2026-10-04T15:19:59Z
parent: qou-5vkl
---

## The finding

Five committed witnesses under `computations/` are produced by **nothing**:

    keystone-habiro-wrt-s3-2i.witness.json
    keystone-qdeform-projector-shift.witness.json
    keystone-schurweyl-dual-sides.witness.json
    keystone-schurweyl-su2-rowcount.witness.json
    keystone-wrt-color-schurweyl.witness.json

Each **names its producer** in the `computation` field — all five point at a
`docs/audits/scripts/keystone_*_probe.py` — and **all five of those probes are
print-only**: no `WitnessBuilder`, no `json.dump`, no `write_text`, no `.save()`.
A repo-wide grep for each filename returns only READERS (other probes citing
them as input) and, for `keystone-schurweyl-dual-sides`, nothing at all.

So these are **hand-transcribed records of printed output**, not generated
artifacts.

## Correcting my own earlier claim

The `qou-tekx` triage put these in a "producer not found" bucket on the strength
of `scriptFile: None`. **That read the wrong field.** The provenance was there
all along in `computation`. What is actually missing is not the producer's
identity but the *generation path*: `scriptFile`, `scriptHash` and `q0Anchor`
cannot be populated by re-running, because re-running writes nothing.

Also recorded so the next agent does not repeat it: **git cannot attribute these
in an agent clone.** `git log --diff-filter=A` names `df5a7ee4e5a` for all five,
and `git rev-list --count df5a7ee4e5a` is **1** — it is a grafted shallow-boundary
root, so everything looks new there. The attribution is an artifact of the
shallow clone, exactly the hazard AGENTS.md records for `scriptCommitSha`.

## Why it matters beyond provenance

All five carry **B** (CODATA-2018 muon, `1.1099785955541805`), and they are
**read as inputs by live probes**. `keystone_wrt_schurweyl_plancherel_4count_probe.py`
hardcodes `WRT`/`CANON_W` read off `keystone-wrt-color-schurweyl.witness.json`
(the "#2603 witness") — which is why PR #6202 deliberately did NOT migrate that
probe's `Q0`. The chain closes: an un-produced, hand-written, B-pinned witness
is the reason a live probe cannot move to the canonical pin.

## The fix, and why it is its own tranche

Teach the five probes to emit their own witness via `WitnessBuilder`, which
stamps `scriptFile`/`scriptHash`/`q0Anchor` for free. Then they are reproducible,
the audits can see them, and `plancherel_4count` can migrate once its input does.

**This moves numbers** — the probes now read the proton pin (PR #6202) while the
committed witnesses hold B, so a generated witness will differ from the
hand-written one by ~11.5 ppb, and any difference beyond that is a transcription
error worth knowing about. That comparison is the whole value of doing it, and
it needs its own PR with a field-by-field diff, not a side effect of a pin fix.


## First regeneration check found one bad witness (2026-08-30) — see `qou-j3u0`

Before writing emitters, the five were checked by re-running each producer
pinned to the witness's own q₀ and comparing. Result:

- `keystone-wrt-color-schurweyl` — **reproduces faithfully** (one field recorded
  at 13 sig figs vs 14 printed; a truncation, not an error).
- `keystone-schurweyl-dual-sides`, `keystone-schurweyl-su2-rowcount` — one
  number each, both reproduce.
- `keystone-habiro-wrt-s3-2i` — one number not located by a string scan;
  **unchecked**, the scan over-reports across precisions.
- `keystone-qdeform-projector-shift` — **CONTRADICTS its producer at the same
  pin**: T_electron differs by 16 orders of magnitude, δ by 47 %, and the
  bar-parity conclusion flips. Bean `qou-j3u0`.

This changes the emitter plan: do **not** regenerate that one into a committed
witness until it is established which computation is correct. Emitting would
silently overwrite a recorded conclusion with a different one.

In-progress in Round 101 PR litlfred/qou#8450.
