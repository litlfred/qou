---
# qou-jyqd
title: convention-C audit skips _deprecated, but two deprecated producers are still named by content
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T19:36:56Z
updated_at: 2026-10-10T07:47:08Z
parent: qou-cdx1
---


Found 2026-08-29 while re-assessing `qou-jqjx` against main.

## The gap

`scripts/convention-c-producer-audit.py:62` — *"`_deprecated/` is skipped
entirely."* Right for its purpose: nobody runs deprecated code, so a
convention-C binding there is not a defect to fix.

Wrong for the corpus. **Deprecating a producer removes it from the audit's view
without removing its influence on the content**, because the numbers it
computed are already written into blocks. The convention-C arc reports its
remaining work as a count of ACTIONABLE sites (9 on main today, one of which
`qou-1jny` showed is a false positive). This category is not in that count and
structurally cannot be.

## Measured — and it is small, which is the good news

`scripts/convention-c-deprecated-citation-audit.py`, added with this bean:

    deprecated .py producers                 567
      carrying a convention-C shape          139
      ...AND named by something in content/    2

Two, not 139. The blind spot's live surface is tiny and nameable:

| producer | named by |
|---|---|
| `integer-lp-gluon.py` | `categorical-proton-properties.ts`, `categorical-neutron-properties.ts`, `gluon-stabiliser-ledger.ts` |
| `protium-witness.py` | `mass-theory/binding-scale-catalan.qa.json` |

## A hit is a DEPENDENCY or a CITATION, and the difference is the whole point

- **DEPENDENCY** — a block quotes the producer's numbers. Live content resting
  on a convention the corpus retired.
- **CITATION** — a block names it while *withdrawing* or auditing it. That is
  provenance, and it is what a corrected block should look like.

Both current hits are CITATIONS **on this branch**, because `qou-jqjx` already
withdrew the dependency. `protium-witness.py`'s single hit is a QA sidecar
recording a confirmed braid-word error.

**On `main` the same producer is still a DEPENDENCY.** `categorical-neutron-
properties.md` rests "a difference in depth rather than in the number of gluon
crossings" on `tr_M = -0.132 versus -0.006` — the two numbers that come from
this deprecated convention-C producer and do not survive the convention change.
`qou-vtlj` corrected the crossing count on main and, in doing so, moved the
surviving claim onto exactly those figures.

So: the excision is landing `qou-jqjx`, and this bean is the detector change
that stops the category recurring.

## Why a separate script rather than an edit to the audit

The audit is AST-based and deliberately strict; this is a text cross-reference
and deliberately loose, because a false positive costs one line of reading
while a miss costs a silent dependency. They also answer different questions —
"is this binding a defect" versus "does this dead code still reach the
content". Folding the second into the first would blur the ACTIONABLE count the
arc reports.

## One bug worth recording, because it is the trap this whole area is about

The first pattern was `q\s*\*\*\s*0\.5`, anchored on a bare `q`. The
motivating producer writes `z = 1.0 / (q0**0.5 + qi0**0.5)` — `q0`, not `q` —
so the detector **missed the one file it was written for** and reported a
single hit. Caught by running it and noticing the known case was absent, not by
review. Pattern is now `\bq\w*`.

A detector that silently misses its own motivating case is the same failure as
an assertion that compares a value to itself (`qou-26f2`): both report success
without having looked. Verified by re-running against the known answer, which
is the only check that would have caught it.

- [x] Measure the blind spot
- [x] Ship the cross-reference audit
- [x] Land `qou-jqjx` so `integer-lp-gluon.py` stops being a dependency on main
- [ ] Decide whether the main audit should call this script, or whether the two
      stay separate and the arc reports two numbers


---

## Re-measured on the merged tree, 2026-08-29

Main merged in (2,478 commits). Audit re-run:

    deprecated .py producers                 568
      carrying a convention-C shape          139
      ...AND named by something in content/    2

Unchanged at 2, and `integer-lp-gluon.py` now shows **four** content refs
rather than three — the neutron `.md` joined the list, because the merged
paragraph names the producer in prose while withdrawing it.

**That is the transition this bean was opened for.** All four refs are now
CITATIONS: blocks naming the producer as the source of a defect they have
withdrawn. Before `qou-jqjx` the same producer was a DEPENDENCY — the corpus
quoted its numbers as live results. Same file, same count, opposite meaning,
and the count alone cannot tell them apart. That is why the script reports and
does not adjudicate.

`protium-witness.py` is unchanged: one hit, a QA sidecar recording a confirmed
braid-word error. A citation.

So the convention-C blind spot has **no live dependency today**. The detector
stays, because the category will recur the next time a producer is deprecated
while its numbers are already written into a block.

## 2026-09-08: canonical ledger for the convention-C excision family is qou-wgta (the P0 excision tracker; owner-ruling milestone qou-cdx1, S2 science blocker qou-cds2); see docs/audits/2026-09-08-l2-1ppq-research-program-gaps.md §6.3 item 2 / §7.3 C3. Nine trackers, previously linked only cds2↔8iru and htsi→t9r1, now all point there.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-09-08 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

Two deprecated producers still named by content, while the producer audit
skips `_deprecated/` by design. Live: deprecating a producer removes it from
the audit's view without removing its influence on published numbers.
`scripts/convention-c-deprecated-citation-audit.py` exists for exactly this
and is not in the actionable count.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10 re-measure on `main` `ac111c1814`: the detector works, 3 hits, all CITATIONS

The deliverable is on `main` and runs clean. Fresh numbers against the
2026-08-29 ones in the table above:

| quantity | 2026-08-29 | 2026-10-10 |
|---|---:|---:|
| deprecated `.py` producers | 567 | **568** |
| ...carrying a convention-C shape | 139 | **139** |
| ...**AND named by something in `content/`** | **2** | **3** |

The third hit is new and is not a regression — it is a *correction banner* that
did not exist in August:

| producer | named by | DEPENDENCY or CITATION? |
|---|---|---|
| `integer-lp-gluon.py` | `categorical-neutron-properties.{md,ts,qa.json}`, `categorical-proton-properties.ts`, `gluon-stabiliser-ledger.ts` | **CITATION** |
| `protium-witness.py` | `mass-theory/binding-scale-catalan.qa.json` | **CITATION** |
| `transfer_matrix_symbolic.py` | `mass-theory/markov-trace-factorization.md` | **CITATION** |

Each adjudicated by reading the site, per this bean's own rule that the script
reports and does not adjudicate:

1. **`integer-lp-gluon.py`** — `qou-jqjx` HAS landed on `main`. The depth claim
   is struck through (`~~…~~`) and the paragraph beneath it names this producer
   as the *source of the retired numbers*: *"Those two figures come from
   `computations/_deprecated/integer-lp-gluon.py`, which computes the Markov
   trace on convention C with $\mathrm{tr}_M(e^-) = z^3$."* So the live
   DEPENDENCY this bean measured on `main` in August is gone, and what is left
   is exactly the provenance shape the bean says a corrected block should have.
2. **`protium-witness.py`** — a QA reviewer note citing it, alongside
   `borromean-markov-trace-closed-form.md`, as the source of the repo's own
   canonical braid word `(σ₀σ₁⁻¹)³` while **confirming a braid-word error** in
   the block. Provenance inside an audit record.
3. **`transfer_matrix_symbolic.py`** — a *"⚠ Readout corrected 2026-09-05"*
   banner naming it as the source of the wrong readout
   `z·(M)₁₁ + (M)₂₁`, with the three-bond table showing the corrected
   `z·(M)₂₁ + (M)₂₂` reproduces `z + d` exactly at every bond
   (`pp 0.612688037146`, `nn 0.403627738351`, `pn 0.508229789377`).

**So: zero live dependencies into a convention-C deprecated producer.** The
category this bean opened to catch is empty on `main`, and the detector that
keeps it empty exists.

## 🛑 But the detector is UNWIRED, and its number is being quoted for a DIFFERENT question

Two findings, and the second is the consequential one.

**It runs nowhere.** `grep -rn 'convention-c-deprecated-citation-audit'` over
`*.sh` / `*.yml` / `*.py` finds exactly two live hits: its own usage string, and
a prose citation in a planning doc. It is not in `scripts/precision-gates.sh`,
not in any workflow. Per AGENTS.md's own recurring lesson — *"a gate nobody
invokes is documentation"* — this is documentation. Not proposed for wiring
here: it is a loose text cross-reference by design and would be advisory at
best, and §🟥 ASK THE OWNER governs adding it to the blocking preflight.

**Its 3 is being read as an answer to T13's question, and the two questions are
different.** [`docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md:137`](../../docs/audits/2026-10-04-workplan-and-migration/TOOLS_report.md)
gives T13 ("move `computations/_deprecated` → `fsh-guts/`") the evidence

> `convention-c-deprecated-citation-audit.py` shows 0 content citations into
> `_deprecated` before the move

That is false in two ways. The audit shows **3**, not 0. And it could not answer
T13 even at 0, because it scans only the **139 of 568** deprecated producers
*carrying a convention-C shape* — T13 breaks on **any** reference. Measured
directly:

    git grep -l 'computations/_deprecated' -- 'folio/**' | grep -v '\.lake/'
    → 27 files   (11 .json, 7 .ts, 5 .lean, 4 .md)
    15 distinct deprecated producers / witnesses named

One of the 27 is **structural rather than prose**:
`mass-theory/wedderburn-weight-canonical.ts` carries

    computation: { engine: "python",
                   script: "computations/_deprecated/bw_wenzl_shadow_equivalence.py",
                   witness: "docs/audits/2026-05-01-p1-3a-bw-equivalence.witness.json",
                   status: "verified" }

— a content block declaring `status: "verified"` against a producer the corpus
deprecated. The other 6 `.ts` hits are `authorNotes` bodies, prose strings or
comments.

Recorded on `qou-6u3n` (TOOLS T13), which is where the decision lives. This bean
keeps it because the mis-citation is *of this bean's own script*, and that is
the reusable lesson: a narrow detector's count, quoted as evidence for a wider
claim, is the same defect class as everything in the detector-blindness
taxonomy, one level up.

**Status: staying `todo`** — not on the dependency question, which is closed,
but because the unwired-detector and T13-precondition items above are live and
unowned.
