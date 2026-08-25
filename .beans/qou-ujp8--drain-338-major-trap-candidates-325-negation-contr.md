---
# qou-ujp8
title: 'DRAIN: 338 major trap-* candidates (325 negation-contrast, 12 thesis-restatement, 1 meta-commentary) — agent adjudication + prose surgery in batches'
status: in-progress
type: task
priority: normal
created_at: 2026-08-15T10:42:07Z
updated_at: 2026-08-19T21:20:00Z
---

## Arc state — 2026-08-19 (re-planned after the takeover and a container loss)

Where the campaign actually stands, measured on current main rather than
carried forward from the session that started it:

| | blocks |
|---|---|
| content blocks (`.md` with a `.ts` sibling) | 3606 |
| agent-audited on the trap axis | 1274 |
| remaining | 2332 |

The corpus grew by ~540 blocks in the four days the branch was away, so
"remaining" is a moving target: a sustained drain outpaces authoring, but
newly written blocks re-enter the queue and the count will not fall
monotonically.

Three things happened while this arc was idle:

1. **#5103 was taken over** (`0afc0097f`). Its 81 content fixes and 3
   beans landed on main; its sidecars did not. See `qou-tqr9` — the
   reasoning given ("qa-sweep regenerates it") cannot hold for an
   `automated: false` axis. Restored in `a89de3169`: 7381 verdicts over
   738 blocks, each re-validated against live main.
2. **The container was recycled.** Chunk 17's audit (42 mass-endomorphism
   blocks, agent:q17) was complete but uncommitted and is gone; its
   findings survive only in the session transcript. The `/tmp/tq_*` queue
   is gone and has been rebuilt from the corpus.
3. **Main moved 1720 commits**, including sibling work that overlaps this
   arc's findings: the χ(A) = −6 / g = 4 branch-point root cause
   (`derivation_claim_audit.py`, #5164), the convention-C excision sweep,
   and the q₀ anchor-corruption family (`qou-m9xp`, `qou-cezp`).

### Plan, in order

1. **Re-audit the 77 blocks with no live record** — the 35 whose `.md`
   changed on main after their audit (their verdicts were correctly not
   ported) plus chunk 17's 42. List: the `changed` set from
   `restore_analysis.py`, and `/tmp/tq_17`'s membership rebuilt by
   chapter.
2. **Reconcile `qou-3nva` against main's landings** before draining
   further. ~120 anomalies were ledgered against a corpus that has since
   moved; some are already fixed by siblings. Re-checking is cheaper than
   a later agent acting on a stale item, and the corpus-grep discipline
   requires it before any of them is re-declared open.
3. **Resume the drain** over the 2332 remaining, largest chapters first
   (mass-theory 776, quantum-observable-universes 314, predicted-spectra
   300). Flights of 2–3 high-rigor agents, ~45 blocks each, committed per
   batch.
4. **Retitle #5103** to what the branch now carries. Its original content
   is on main; leaving the old description invites a second landing of
   the same 81 fixes.

### Defect of my own, corrected in `a89de3169`

From chunk 06 the flight briefs named three criteria descriptively rather
than copying the scanner's ids, so 419 blocks recorded verdicts under
`trap-compulsive-triple` / `trap-superlative-inflation` /
`trap-nonspeakable-syntax` against a scanner and registry that use
`trap-triples` / `trap-superlative` / `trap-nonspeakable`. 1239 entries
normalised. Unnormalised they would never have joined the script
candidates they adjudicate — an audit that reads as done and joins to
nothing.

