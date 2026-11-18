---
# qou-akdup
title: alpha-k witnesses duplicated at root and alpha/, in DIFFERENT conventions
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-19T20:30:00Z
updated_at: 2026-10-04T15:16:19Z
parent: qou-5vkl
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


---

## Do NOT close this with a derivation chain — measured 2026-08-23 (PR #5584)

Draining tier C of the derivation-chain gap (`dgpc`) took C-family from 14
witnesses to **4**, and the 4 that remain are exactly this bean's two pairs.
The obvious next move — author one chain per producer and drain them — is
**wrong here, and would actively make things worse.**

`derivation_chain_validator.py` matches a chain to witnesses by **producer
basename**. Both copies of each pair declare (or resolve to) the same producer
name, so a single chain for `alpha_k_jones_markov_h3.py` backs the root copy
and the `alpha/` copy alike. Since the two are in **different trace
conventions** — root is C (`z = 0.4993203341836944`, excised 2026-08-15),
`alpha/` is D (`z = 0.6126880371464652`, canonical) — such a chain would
certify a **convention-C witness under a convention-D derivation**. The count
would go down and the corpus would be worse.

That generalises past this bean, and is worth stating on its own: **the
derivation-chain mechanism has a convention blind spot.** One chain per
producer basename means any producer whose output exists in two conventions
gets both certified by whichever convention the chain happens to describe.
Nothing in the validator can see the difference.

### The asymmetry, re-measured on today's main

The two copies are not peers, and this settles the direction of the fix:

| | root `computations/` | `computations/alpha/` |
|---|---|---|
| h3 | 16 keys, `q0Anchor` **absent** | **18 keys**, `q0Anchor: proton` |
| h4 | **10 keys**, `q0Anchor` absent, **`scriptFile` absent** | **19 keys**, `q0Anchor: proton` |

The `alpha/` copies are supersets on both counts. The root h4 copy carries no
producer field at all, so the categoriser reaches it only by slug — it is a
stale artifact, not a second computation.

### So the disposition is retirement, not backing

Retire the two root copies in favour of the `alpha/` ones, repoint any
consumer, and then the `alpha/` pair can be chained safely — at which point
one chain per producer is correct again, because only one convention remains
under each name. Doing it in the other order bakes the C copies in.

Left undone deliberately on #5584: retiring a witness that something might
read is not a drive-by, and the four are the last of tier C precisely because
they need this decision rather than more authoring.

In-progress in Round 100 PR litlfred/qou#8447.
