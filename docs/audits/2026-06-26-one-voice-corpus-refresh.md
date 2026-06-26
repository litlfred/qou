# One-voice corpus audit — coverage, staleness, and refresh queue (2026-06-26)

## Why this doc exists

The user asked for a full one-voice audit refresh across all content
blocks (`/integration-audit all`, "refresh stale, do new"). The mechanical
QA tooling (`qa-sweep.ts`, `integration-audit.ts`, `qa-checkers-voice.ts`)
was relocated to the external `litlfred/folio-assistant` repo by the miga
migration. That repo is out of repo-scope in the web sandbox, returns 403
through the agent proxy, is not network-reachable, and no in-repo CI
workflow runs it. **The mechanical refresh therefore could not be run from
this session.** This doc records the hash-accurate diagnostic that *can* be
produced by reading the committed `.qa.json` sidecars directly, the fixes
applied by hand, and the precise scope a folio-assistant-enabled run must
cover.

## Coverage (2222 sidecars, 11 universal one-voice criteria)

Hash-accurate buckets (12-char SHA-256 prefix of each sibling vs the
sidecar's recorded `field_hash`; an entry is *stale* when the source
changed since it was written). Counts below are the **post-fix** state —
the 3 blocks edited in this PR (§Fixes) are now stale across all 11
criteria, so each row's `stale` is 238 and every row sums to the 2222
total sidecars:

| criterion | pass | fail | n/a | stale | missing |
|---|---|---|---|---|---|
| voice-ai-slop | 1914 | 0 | 2 | 238 | 68 |
| voice-author-notes-pollution | 1914 | 0 | 2 | 238 | 68 |
| voice-editorializing | 1914 | 0 | 2 | 238 | 68 |
| voice-emoji-content | 1914 | 0 | 2 | 238 | 68 |
| voice-first-person-work | 1914 | 0 | 2 | 238 | 68 |
| voice-scholarly-default | 1911 | 3 | 2 | 238 | 68 |
| voice-status-leak | 1914 | 0 | 2 | 238 | 68 |
| voice-status-section | 1906 | 0 | 2 | 238 | 76 |
| voice-time-stamped-notes | 1914 | 0 | 2 | 238 | 68 |
| voice-title-scholarly | 1644 | 0 | 272 | 238 | 68 |
| voice-unicode-crash | 1914 | 0 | 2 | 238 | 68 |

Pre-fix state (before this PR's 3 edits): `stale` was 235 and the three
now-cleared fails sat in the `fail` column — `voice-editorializing` 1,
`voice-status-section` 2. (`voice-statement-no-interpretation` is
statement-block-only; its ~1578 "missing" is by-design N/A, so it is
excluded from the universal set.)

**Headline:** the one-voice audit *has* been run broadly — ~1917/2222
fresh-pass per universal criterion. The drift is the work:

- **6 genuine fresh fails** corpus-wide (not the 272 a first, mis-bucketed
  pass mistook for failures — those 272 are `n/a` titleless intro/outro
  blocks, not violations).
- **238 blocks stale** (source changed since last sweep — verdict unknown
  until re-run; includes the 3 fixed here).
- **76 blocks never swept** on ≥1 universal criterion (mostly intro / outro
  / index prose). A mechanical leak-scan (emoji / status-header /
  first-person / TODO) over all 76 found **no clear violations** — only
  dates inside audit-doc link paths (regex false positives) and a few
  changelog-style dated notes in the `notation-collisions` reference doc.
  They need the canonical sweep to *record* entries, not fixes.

## Fixes applied by hand (3 of 6 fresh fails)

| block | criterion | fix |
|---|---|---|
| [`mass-modulus-em-phase-color-grading.md`](../../content/quantum-observable-universe/mass-endomorphism/mass-modulus-em-phase-color-grading.md) | voice-status-section | `## Archimedean status` → `## Archimedean realization` |
| [`qbeta-counit-transition.md`](../../content/quantum-observable-universe/particle-interactions/qbeta-counit-transition.md) | voice-status-section | `## Status of the agreement` → `## Agreement with the measured value` |
| [`qbeta-canonical-markov-weights-explicit-instance.md`](../../content/quantum-observable-universe/mass-endomorphism/qbeta-canonical-markov-weights-explicit-instance.md) | voice-editorializing | `(notably` → `(in particular` |

## Not fixed — 3 probable false positives (need canonical checker rerun)

The remaining 3 fresh fails are all `voice-scholarly-default` on prose that
reads as sound scholarly / mathematical English. The checker rule lives in
`folio-assistant` and can't be inspected from this sandbox, so the prose was
**not** rewritten to satisfy a checker that can't be re-run to confirm the
fix. Flagged for a folio-assistant-enabled rerun to confirm:

- `particle-interactions/qbeta-trace-counit-convergence.md:20` — "so their
  equality is required for consistency."
- `q-geometric-langlands/modular-s-transform-q-q-tilde.lean:118` — "so the
  `S`-duality is not vacuous." (Lean docstring)
- `quantum-observable-universes/qou-canonical-action.md:74` — "The *trace
  form* (string diagram) carries the categorical trace…"

## Refresh queue + command

The precise stale/missing/fail lists are in the sidecar
[`2026-06-26-one-voice-refresh-queue.json`](2026-06-26-one-voice-refresh-queue.json).
On any machine/session with `folio-assistant` access:

```bash
bash scripts/setup-folio-assistant.sh
# one-voice axis only:
bun run pipeline/integration-audit.ts content/quantum-observable-universe --axis one-voice
# or every axis (the user's "/integration-audit all"):
bun run pipeline/integration-audit.ts content/quantum-observable-universe --all
```

That invalidates the stale script entries and re-sweeps, which will (a)
re-verdict the 238 stale blocks, (b) populate the 76 never-swept blocks, and
(c) confirm/clear the 3 probable-false-positive fails above.
