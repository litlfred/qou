# Tranche 1 evidence — restore `thm:jones-markov-trace` to the 21 blocks that lost it?

Generated 2026-08-15 by `scripts/prune-tranche-sheet.ts thm:jones-markov-trace`.
Bean `prn1`. **Nothing is restored by this document.**

`2026-08-15-prune-damage-redrive.md` showed the prune damage cuts far better by
target than by source: `thm:jones-markov-trace` was stripped from 21 blocks in
one pass, so "must a reader have read it before these?" is **one** editorial
question with 21 applications, not 21 judgements. This is the evidence for that
one question.

## How to read the columns

- **prose link** — the narrative contains `](#thm:jones-markov-trace)`. Decisive
  in the affirmative: the prose is sending the reader there while `uses[]` omits
  it, so the block's own two halves contradict each other.
- **prose mention** — names the concept without linking. Suggestive only; a
  block may mention a theorem it does not depend on.
- **lean** — the block's `.lean` references `QOU.Braiding.JonesMarkovTrace`.
  This is the **formal** relation, which is not the editorial one, and it is
  reported rather than counted. A proof invokes lemmas no reader must have read.
- `n/a` means the file does not exist, so nothing was searched. It is not `no`.


Target exists: yes
Target Lean decl: `QOU.Braiding.JonesMarkovTrace`
Sources that lost it and still cannot reach it: **21**

| source | kind | prose link | prose mention | lean | declares now |
|---|---|---|---|---|---|
| `prop:shell-schur-weyl-self-duality` | proposition | no | no | no | 0 |
| `rem:hecke-algebra-from-braiding` | remark | no | no | *n/a — no .lean* | 0 |
| `prop:wedderburn-as-noncomm-fourier` | proposition | no | no | no | 0 |
| `prop:frobenius-self-duality-forces-lp-dual-extraction` | proposition | no | markov trace | no | 0 |
| `lem:vhat-pair-commutation-trace` | lemma | no | no | no | 0 |
| `prop:atom-knot-unique` | proposition | no | no | no | 1 |
| `lem:degree-one-braid-trivial-volume` | lemma | no | no | no | 0 |
| `prose:pre-archimedean-derivation-chain` | prose | no | markov trace | *n/a — no .lean* | 3 |
| `prop:atom-knot-mass-derivation` | proposition | no | no | no | 2 |
| `def:per-nucleon-channel-decomposition` | definition | no | no | no | 1 |
| `prop:three-calibration-discipline` | proposition | **YES** | jones-markov-trace, markov trace | no | 2 |
| `prop:recursive-atom-knot-atlas` | proposition | no | no | no | 4 |
| `prop:pieri-photon-shift` | proposition | no | no | no | 1 |
| `prop:y-lambda-cyclotomic-factorization` | proposition | no | no | no | 1 |
| `prop:y-lambda-recipe-from-partition` | proposition | no | no | no | 1 |
| `prop:qmn-recursive-memoized` | proposition | no | no | *n/a — no .lean* | 1 |
| `prop:demazure-fiber-markov-trace` | proposition | no | no | no | 1 |
| `def:phi-q-piece` | definition | no | no | no | 1 |
| `prop:wenzl-bridge-applicability-qou` | proposition | no | markov trace | no | 1 |
| `prop:wenzl-qmn-synergy` | proposition | no | markov trace | no | 1 |
| `prf:atom-knot-mass-derivation` | proof | **YES** | jones-markov-trace, markov trace | no | 2 |

**2 of 21 searchable blocks link to the target from their prose** (0 of 21 have no `.md` and were not searched at all).

For those, the narrative is sending the reader to `thm:jones-markov-trace` while `uses[]` omits it. That is the editorial relation contradicting itself in the same block, not a matter of taste:

- `prop:three-calibration-discipline`
- `prf:atom-knot-mass-derivation`

## What the sheet says, and what it does not

**Two blocks are near-certain restores**, and not on a matter of taste:
`prop:three-calibration-discipline` and `prf:atom-knot-mass-derivation` both
link to `thm:jones-markov-trace` from their prose while omitting it from
`uses[]`. The editorial relation is contradicting itself inside one block.

**Six of the 21 declare nothing at all, and ten declare exactly one edge** — so
16 of 21 carry at most a single prerequisite. That is the prune's fingerprint
rather than an authored convention.

**No formal evidence supports restoration anywhere.** Of the 18 blocks with a
`.lean` sibling, none references `QOU.Braiding.JonesMarkovTrace`. That is not an
argument against restoring — the two relations diverge legitimately, and `uses[]`
must never be populated from Lean — but it does mean the case here rests
entirely on editorial reading. Nobody should mistake the formal graph for
corroboration.

**Four more mention the Markov trace in prose without linking**
(`prop:frobenius-self-duality-forces-lp-dual-extraction`,
`prose:pre-archimedean-derivation-chain`, `prop:wenzl-bridge-applicability-qou`,
`prop:wenzl-qmn-synergy`). Suggestive, and exactly the set where a reader's
judgement is actually needed.

The remaining blocks show no textual signal either way. For those the question
is genuinely open, and "the prune removed it" is a reason to *ask*, not an
answer.

The `uses-editorial-review` two-reader standard governs what is applied.
