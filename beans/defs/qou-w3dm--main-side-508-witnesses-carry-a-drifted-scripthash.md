---
# qou-w3dm
title: 'MAIN-SIDE: ~508 of 2749 witnesses carry a drifted scriptHash (18%)'
status: in-progress
type: task
priority: high
tags:
    - reorg-2026-10-04
created_at: 2026-08-08T07:40:00Z
updated_at: 2026-10-04T15:14:57Z
parent: qou-5vkl
---

Found during the PR #4513 prepare-merge gate check. **This is a main-side
condition, not caused by #4513** — recorded so it is not lost inside the
narrower bean `qou-p2ka`.

## How it surfaced

The Phase-4 gate ("compute changed => producer re-run + witness refreshed")
flagged `computations/probes/qbeta-3bp8-annihilator-continuation-w1.witness.json`
as stale against #4513's producer edit. Checking whether reverting that edit
would restore the match showed it would NOT:

    witness scriptHash        1f36cf6623d1
    producer on origin/main   40a4ab595325   <- already mismatched
    producer on the PR head   26fafbd3b5b0
    witness computedAt        2026-08-01

The witness was **already stale on main**. That prompted a corpus-wide scan.

## Measurement

Scanned every `computations/**/*.witness.json`, resolving each witness's
producer and comparing `sha256(producer)[:12]` against the recorded
`witness.scriptHash`:

    witnesses scanned          2749
      no scriptHash recorded    427
      producer not resolvable    91
      scriptHash DRIFTED        508      (18% of scanned)

Examples: `atom-mass-atomic-braid`, `chi-inter-and-nchir-rank`,
`delta-lambda-dominant-pin-probe`, `feynman-qou-comparison`,
`he4-canonical-tr-m-block-fingerprint`, `he4-sdp-compositional-probe`.

## HONEST SCOPE — 508 is a CANDIDATE count, not a confirmed one

The producer for each witness was resolved by `scriptFile`/`script` field when
present, else by stem matching (`<name>.py` / `<name>_probe.py`). That
heuristic can mis-resolve — a witness pointed at the wrong file reports a
spurious drift. So:

  * **508 is an upper bound on real drift**, needing per-item confirmation.
  * The 91 "producer not resolvable" and 427 "no scriptHash recorded" are
    separate sub-classes, each worth its own look — the second especially,
    since a witness with no `scriptHash` cannot be staleness-checked at all
    and is invisible to this whole discipline.

This overlaps the P30 provenance work landing on main (`#4715`, `#4717` —
"does the claimed producer actually write the witness? 3, not 324"), which is
attacking the same `scriptFile`-accuracy problem from the other side. **Check
that work before draining this**: its discriminator is probably the right
producer-resolution oracle to use here, and would turn this candidate count
into a confirmed one.

## Why it matters

A drifted `scriptHash` means the recorded numbers were produced by a version of
the script that no longer exists. The witness may still be correct — or may
silently encode superseded values, which is exactly the failure `qou-vbw1`
documented (a q0 unit conflation that made nine probes stale, invisible until
re-run). At 18% the discipline is not currently load-bearing.

## Suggested first step

Re-run the scan using the P30 provenance discriminator instead of stem
matching, split the result into (a) confirmed drift, (b) mis-resolved producer,
(c) no-hash, and size each. Do NOT mass-regenerate: that is a large compute
sweep and needs scoped sign-off, and some producers are hours-long (see
`qou-p2ka`).

---

# ATTACK VECTORS (2026-08-08)

## Where it sits in the chain

Not on the derivation chain at all — this is the **provenance layer** that
guards every step of it. A witness is the serialized output of one chain step;
`scriptHash` is the only mechanism asserting that the recorded numbers came from
the code currently in the tree. It intervenes between **a compute step and every
downstream consumer of its numbers**.

That placement is why 18% drift matters more than it looks: a stale witness does
not announce itself, and consumers read numbers, not provenance.

## AV1 — confirm the count with the P30 oracle, do not re-measure with mine

My resolver used `scriptFile` when present, else stem matching. #4715/#4717
built an actual producer/consumer discriminator ("does the claimed producer
actually write the witness? 3, not 324"). Re-run the scan with THAT as the
resolver and split into: confirmed drift / mis-resolved producer / no-hash.
Only the first bucket is real work. Do this before anything else — the 508 may
shrink a lot.

## AV2 — the 427 no-hash witnesses are the more dangerous class

A witness with a drifted hash is at least VISIBLE to the discipline. A witness
with NO `scriptHash` is invisible: it can never be flagged stale, so it silently
passes every freshness check forever. This is the same shape as the
phantom-citation class (#4513) and the vacuity-audit gaps (#4712): **a check
that does not apply is indistinguishable from a check that passed.**
Prioritise backfilling `scriptHash` over regenerating drifted ones.

## AV3 — rank by blast radius, not by count

A drifted witness that nothing consumes is bookkeeping. One consumed by the mass
path or a dashboard is a live wrong-number risk. Cross-reference the drift list
against the no-free-parameter certificate's consumer set and the L2 dashboards,
and drain that intersection first.

## AV4 — make the gate mechanical

Once confirmed, a `--check-witness-freshness` mode that exits non-zero belongs
in the same place `check-sidecars.sh` runs, so this cannot re-accumulate. That
is the durable fix; regeneration alone just resets the clock.

## GUARD

Do NOT mass-regenerate. Some producers run for hours (see `qou-p2ka`, where A2
exceeded the container restart interval twice). Regeneration is a scoped compute
sweep needing sign-off, not an idle-time drain.
