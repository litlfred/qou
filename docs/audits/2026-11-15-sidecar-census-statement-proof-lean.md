# QA sidecar census: statement ↔ proof ↔ Lean (2026-11-15)

Measured on `litlfred/qou` main `b2b349f36`, folio `quantum-observable-universe`,
with the platform's own freshness rule (`entryIsFresh` + `hashBlockFiles` from
`cat-harness-tools/pipeline/qa-utils.ts`, lite mount). Script:
`qa-sidecar-census.ts` in this folder; raw rows in the two JSON files.

## How a sidecar works

- Each block `<name>.{ts,md,lean}` has `<name>.qa.json` (`block-qa/v1`).
- `source_hashes` = 12-char SHA-256 prefixes of the block's files.
- `criteria.<id>` is an append-only list of verdicts. Each verdict carries
  `field_hash` (hashes of md/ts/lean, and `lean_statement` = signature-only
  hash) at review time.
- A verdict is **fresh** iff every file the criterion `depends_on` still hashes
  to its `field_hash` (signature hash for `lean_granularity: "statement"`).
- **unhashed** = verdict has no `field_hash`. These record no block version and
  adjudicate nothing. Almost all are the 2026-07-07/08 heuristic drain
  (`local/qa-agent-drain-heuristic`), whose note reads e.g. "Both Lean and MD
  files exist and appear substantive". Already prefixed `[EXPIRED-NO-FIELD-HASH]`
  (bean `qou-pwut`). **They are not reviews.**
- Writer for genuine verdicts: `bun run folio/pipeline/qa-agent-entry.ts
  --block <md> --criterion <id> --result pass|fail|warn|n/a --evidence ...`
  (fail/warn require evidence; hashes are taken from current files).

## Which criteria are "the two checks"

| User's check | Registered criterion | What it actually compares |
|---|---|---|
| Narrative proof matches the statement | **none dedicated.** Nearest: `da-non-sequitur`, `da-circular`, `da-false-claim` on the `prf:` block | Generic devil's-advocate objections on the proof block's own text |
| Narrative ↔ Lean | `proof-narrative-lean-equiv` (on the statement block) | `.md` **statement** vs Lean **signature** only. By design a proof-body change does not stale it |
| (also) | `da-lean-narrative-divergence` | Lean proves something weaker/different than the `.md` claims |

Structural gap: a `prf:` block's verdict depends only on the proof block's own
md/ts. Editing the **statement** it proves never makes it stale.

## Counts

### A. Statement blocks (theorem 55, lemma 50, proposition 629, corollary 17 = 751)

462 have a Lean file (sibling or `lean.ref`).

| criterion (on the 462 Lean-backed) | fresh | stale | unhashed | missing |
|---|---|---|---|---|
| `proof-narrative-lean-equiv` | **0** | 42 | 406 | 14 |
| `proof-statement-integrity` | 1 | 14 | 433 | 14 |
| `da-lean-narrative-divergence` | 1 | 183 | 267 | 11 |

Over all 751: `proof-narrative-lean-equiv` fresh 1 (an `n/a`), stale 115,
unhashed 540, missing 95. Stale verdicts are mostly `local/narrative-lean-rerate`
from 2026-06.

### B. Proof blocks (`prf:`, 443)

435 of the 751 statements have a `prf:` block; 316 do not (153 of those have Lean).

| criterion | fresh | stale | unhashed | missing |
|---|---|---|---|---|
| `da-non-sequitur` | 60 (all pass) | 60 | 297 | 26 |
| `da-circular` | 60 | 60 | 297 | 26 |
| `da-false-claim` | 62 (2 fail) | 60 | 295 | 26 |

"Fresh" here only means the proof block's own text is unchanged; the statement
may have moved (gap above).

### Work by chapter (Lean-backed statements / proof blocks)

| chapter | Lean-backed | prf |
|---|---|---|
| mass-theory | 159 | 154 |
| quantum-observable-universes | 64 | 58 |
| predicted-spectra | 39 | 33 |
| knots-particles-confinement | 24 | 21 |
| mass-endomorphism | 23 | 22 |
| lifting-and-descent | 23 | 22 |
| brings-surface | 20 | 23 |
| braids-and-knots | 19 | 16 |
| information-theory | 14 | 15 |
| nuclear-interactions | 14 | 15 |
| observations | 11 | 17 |
| climax-volume-mass | 13 | 7 |
| 12 smaller chapters | 39 | 40 |
| **total** | **462** | **443** |

## Tooling notes

- `qa-sweep.ts` does not load on the lite platform mount (`Cannot find package
  'fast-xml-parser'`); bean `qou-4jhp` records a further load failure at pin
  `b61e856`. `qa-agent-entry.ts` (the agent-verdict writer) is qou-side and
  does not need the sweep.
- AGENTS.md (2026-09-07) lists "mass-refreshing sidecars" as needing the
  owner's go, so nothing has been written.
