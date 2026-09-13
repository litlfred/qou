# PR #6233 (orphaned FormB probe) adjudication + `qou-cds1` state of play

**Status: IN PROGRESS.** This document is being written as the measurements land.

## Scope

Two linked questions, neither of which is settled here — the verdict is the
owner's; this document exists to make the call cheap.

1. **PR #6233** preserves two files found *untracked* in a working tree on
   2026-08-30, provenance unknown:
   `computations/qbeta/qbeta_block_resolved_formB_probe.py` and its witness.
   Neither is on `main`. The preserving author claimed **no** verification.
   Question: does the probe do what it claims, do its three recorded
   assertions reproduce, and which of the PR's own three outcomes applies?

2. **Bean `qou-cds1`** — re-derive the Q_β `c_k` ladder under convention D.
   Question: what is actually done, what is blocking, and would the #6233
   probe (if sound) advance it?

## Findings

_(populated below as they are measured)_
