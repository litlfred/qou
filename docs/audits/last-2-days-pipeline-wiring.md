# Audit — last-2-days content vs computation-pipeline wiring

**Scope.** Commits on the qou repo since 2026-04-25 00:00 UTC.
**Question.** For every content block (`.ts` + `.md` + optional `.lean`)
added or modified in this window, is it wired to the computation
pipeline (witness JSON / Python feeder / Rust binary), and which
pipeline artifacts have no content home?

**Status.** In progress — audit being assembled. Results will be
checked into this file in subsequent commits on the branch.

## Plan

1. Enumerate added/modified blocks under
   `content/quantum-observable-universe/<chapter>/`.
2. For each, record: chapter, label, kind (definition / proposition /
   …), Added vs Modified, presence of meaningful Lean (sorry-count
   with `Ref:` annotations), computational evidence (cited witness
   JSON, sibling Python feeder, named Rust binary).
3. Bucket each block:
   - **wired-end-to-end** — narrative + Lean (no unjustified `sorry`)
     + compute evidence
   - **wired-partially** — Lean OR compute evidence, not both
   - **stub/skeleton** — `.ts` exists, but `.md` missing/short and no
     Lean, no compute
   - **math-only** — full narrative + Lean, no compute counterpart
4. Separately list new Python feeders / Rust bins / witness JSONs in
   the window that no content block references.

## Why this audit

PR #444 (joint-tower SDP + Clarabel + Rust GB-NF reducer + R5-minimal
α* verifier) introduced 357 file changes; PR #445 (C5 proof splits)
overlapped the same window. Several content blocks land alongside
new compute artifacts; a few may be orphaned in either direction.
Identifying those gaps unblocks the next iteration on the
**mass-derivation calculation** (sub-ppm convergence for partial-shell
isotopes ⁶Li / ⁷Li / ⁹Be / ¹⁰Be / ¹⁰B / ¹¹B), which is the active
work-stream on this branch.
