---
# qou-akdup
title: 'alpha-k witnesses duplicated at root and alpha/, in DIFFERENT conventions'
status: todo
type: task
priority: normal
created_at: 2026-08-19T20:30:00Z
updated_at: 2026-08-19T20:30:00Z
---

`alpha-k-jones-markov-h3.witness.json` and `-h4` exist at **two paths**, and the
copies are not stale duplicates of one computation — they are in **different
trace conventions**:

| | `computations/` (root) | `computations/alpha/` |
|---|---|---|
| `z` | **0.4993203341836944** | **0.6126880371464652** |
| convention | `√q/(q+1)` = **C** (excised 2026-08-15) | `q³/(q²+1)` = **D** (canonical) |
| q₀ | muon (h4 `substrate.q_0` = 1.10997859…) | proton, declared (`q0Anchor`, `q0Value`) |
| timestamp | 2026-05-30 | 2026-08-14 |

Verified against the definitions at q₀ = 1.1099785827513808:
`z_C = 0.4993203341836945`, `z_D = 0.6126880371464653`. The match is exact.

The root copies are the pre-refactor artifacts the Phase-5 subdirectory move
left behind; `alpha/` holds the current regeneration.

## Live consumers read the ROOT (convention-C) copy

`base = Path(__file__).parent` in both cases, so the bare filename resolves to
the root copy:

- `computations/codata_reconciliation.py:177`
- `computations/h4_markov_weights_closed_form.py:300` (`Path(__file__).with_name(...)`)

**Not over-claimed:** `codata_reconciliation`'s actual check is
`α_2 − z²` — the Markov axiom (M2), which holds for **any** `z`. It is
convention-*invariant*, so no corrupted number reaches its output. What is
wrong is the provenance label and the fact that a `z` read from that file would
be the excised convention.

## Why this is NOT fixed here

Pointing the consumers at `alpha/` is directionally right under the D ruling,
but two things block a drive-by fix:

1. **The h4 copies are different payloads, not the same payload at two
   conventions.** The root h4 carries `substrate`, `wedderburn_h4` and
   `wedderburn_h3_crosscheck`; the `alpha/` h4 carries none of them — and
   `h4_markov_weights_closed_form.py:380` reads exactly
   `{XCHECK_SOURCE}:substrate.q_0`. Repointing breaks the read; deprecating the
   root copy destroys data the replacement does not have.
2. **This is a C→D migration step**, and AGENTS.md scopes that as a tracked
   sweep needing sign-off, not something to start inside a drain PR.

## Related, and probably the same tranche

`alpha-k-h3-{0,1,2,3}.derivation.json` — four **fully-trusted** chains — carry
convention-C numeric leaves: `alpha-k-h3-2` has `target_value 0.24932079597942414`
and `0.4993203341836944² = 0.2493207…`. Under the D ruling these need the same
scope label the c_k ladder got (bean `qou-cds1`), or re-derivation. They are not
wrong *as recorded* — they are C-frame and unlabelled.

## Suggested disposition

1. Decide which h4 payload is canonical (or merge them).
2. Repoint the two consumers; deprecate the superseded root copies.
3. Label the four `alpha-k-h3-*` chains C-frame, per the c_k precedent.

Found while draining tier C (bean `dgpc`), PR #5289.
