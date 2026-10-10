---
# qou-4sdp
title: Agent QA verdicts go stale in the FIXED direction and no sweep can clear them
status: completed
type: task
priority: normal
created_at: 2026-08-24T21:17:34Z
updated_at: 2026-08-24T22:47:07Z
---

`qou-h1p7` established that a `.qa.json` criterion holds a HISTORY of entries,
and that a stale `pass` from July looks authoritative until something re-runs
the checker. This is the mirror case, and it is worse to spot: a stale **fail**
from an AGENT, quoting prose that has since been deleted.

`qa-sweep.ts` re-runs SCRIPT criteria only. It cannot touch an agent verdict,
so an agent `fail` survives every sweep, every edit, and every fix — the block
goes on reporting a problem that no longer exists, and the only way to tell is
to open the evidence and grep the quoted string.

## Three found so far, all while fixing something else

| block | criterion | agent verdict | quotes prose that is now |
|---|---|---|---|
| `rem:markov-axioms-primitive` | `trap-meta-commentary` | 2026-08-15 | deleted (`qou-h1p7`) |
| `rem:bar-involution-c5-algebraic-identities` | `trap-meta-commentary` | 2026-08-15 | deleted (`qou-spud`) |
| `rem:qou-motivic-galois-instance-verification` | `trap-superlative` | 2026-08-22 | deleted 2026-08-23 |

Each verified by grepping the verdict's own quoted string against the current
`.md`: 0 matches in all four strings checked.

The third is the sharpest. `trap-superlative` quotes *"conj:motivic-perpetual-
obstruction **becomes an unconditional theorem** for the QOU substrate"* and
*"almost_everywhere_nontrivial **functions as a substrate axiom**"*. The block's
own `authorNotes` entry, dated **the very next day**, records that both were
corrected. So the block simultaneously carries a note saying "fixed" and a
verdict saying "broken", and the verdict is the one a QA reader sees first.

## Why it matters more than a cosmetic staleness

A stale agent `fail` is indistinguishable from a live one, so it consumes
exactly the attention a real finding would — and it trains a reader to discount
the axis. Three of the small number of blocks I happened to open were in this
state; the corpus-wide rate is **unmeasured**, and measuring it is the first
step, not fixing them one at a time.

## What would settle it

A sweep that, for every agent verdict carrying `evidence` with a quoted string,
checks whether that string still occurs in the block's current `.md` / `.lean`.
A verdict whose evidence has vanished is not necessarily wrong — the criterion
may have other grounds — but it is certainly unverified, and should be
re-queued for adjudication rather than left presenting as current. The queue
already exists (`content/pipeline/qa-agent-drain-queue.ts`); what is missing is
the detector that feeds it.

Not attempted here: this is a corpus-wide measurement plus an adjudication
pass, and both are their own work.

---

## MEASURED 2026-08-24 — 166 verdicts point at prose that no longer exists

`scripts/qa-stale-agent-evidence.py` (new). Over every `.qa.json` in the
corpus, taking each criterion's **latest** entry:

| | count | share |
|---|---|---|
| agent `fail`/`warn` verdicts | **1,442** | |
| `live` — the quoted text is still there | 730 | 50.6 % |
| `edited` — sentence rewritten, a leading phrase survives | 93 | 6.4 % |
| **`gone` — no trace of the quoted sentence left** | **166** | **11.5 %** |
| `unquotable` — evidence carries no searchable quote | 453 | 31.4 % |

Of the 989 **decidable** verdicts, **166 (16.8 %) have no textual anchor at
all**. Concentrated in the trap family: `trap-superlative` 57,
`trap-thesis-restatement` 23, `trap-closing-aphorism` 23, `trap-nonspeakable`
18, `trap-meta-commentary` 17.

`unquotable` is a third of the population and is **not** a clean bill: those
verdicts read like *"Closer restated the para-2 roadmap already given
(R-matrix, hexagon, Hecke-skein)"* — accurate, perhaps, but unfalsifiable by
anything but a human re-reading. Evidence that cannot be checked is its own
finding.

### My first number was wrong by 2.6x, and how

The first version of the detector reported **437** vanished (43.4 % of
decidable). Two extraction artifacts, both caught by hand-checking samples
before reporting:

* A *"widest span between the first and last quote"* strategy stitched two
  separate short quotes into one. Evidence reading *"grades a −0.6 % residual
  'excellent' and +10.3 % 'fair'"* became the fragment
  `excellent' and $+10.3\%$ 'fair`, which appears in no source — while both
  words are present. Strategy dropped.
* Agents render an em dash as `-` inside their quotes, so
  `'- all four readings equal, as they are for $4_1$ -'` failed a literal
  search against prose that contains it. Both sides are now folded to bare
  lowercase words (dashes, quotes, math and markdown emphasis stripped) and
  the search runs on the longest *wordy core* of each quote rather than the
  whole span.

A third over-count survived that fix and is now split out rather than removed:
a sentence that was **edited** rather than deleted still fails a whole-quote
search, but the construct the verdict flagged may well have survived the edit.
93 of them. Only `gone` is reported as anchorless.

So **166 is a floor**. Matching is deliberately loose in the direction that
under-reports.

### Verified by hand, not just by script

Six rows checked against their sources directly. The two artifacts above were
found that way; three `gone` rows
(`diophantine-birthday-trajectory`, `birthday-axioms-do-not-pin-the-birthday`
×2) were confirmed absent, and two rows I had first read as stale
(`rem:wedderburn-as-noncomm-fourier-context`,
`rem:spin-involution-lp-dual-invariance-interpretation`) turned out to be the
`edited` case — which is why that category exists.

### Where this leaves the class

The detector is the piece the bean said was missing; it exists and is
repeatable (`python3 scripts/qa-stale-agent-evidence.py [--list]`). What it
does **not** do is decide any verdict — a `gone` verdict is *unverified*, not
*wrong*, and clearing 166 of them means an adjudication pass through
`qa-agent-drain-queue.ts`, which is its own work and is not attempted here.

Advisory by construction: it exits 0 always. Wiring it as a gate would need a
baseline first, since 166 is the standing state and not a regression.

### Placement

Kept as a Python script in `scripts/`, beside its closest sibling
`qa-duplicate-verdict-check.py`, which is also Python and also walks the
sidecars. It is generic — it hardcodes nothing about this folio and takes its
root from `$QOU_ROOT` or the cwd — so it could move to the platform if a
second folio ever needs it. Not moved speculatively.
