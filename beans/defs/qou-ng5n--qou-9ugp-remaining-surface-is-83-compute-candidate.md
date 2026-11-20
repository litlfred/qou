---
# qou-ng5n
title: qou-9ugp remaining surface is 83 COMPUTE candidates, not the 48 reported — 35 in computations/ top level are counted nowhere
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-04T04:05:58Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-trd0
---

## Measured 2026-09-04 with a committed, self-tested tool

Do not quote this; re-run it. `computations/audits/retired_pin_live_code_audit.py`
(`--selftest` 8/8) over `computations tools scripts`:

    files containing the string  : 209   (what grep reports)
    ...with it in LIVE CODE      :  97   (grep over-counts 2.15x)
      COMPUTE    83      <- candidates
      UNCLEAR     2
      REFERENCE  12

    COMPUTE by directory:
      computations                                  35
      computations/qbeta                            29
      computations/audits                            9
      computations/substrate                         6
      computations/habiro                            2
      computations/hecke                             1
      computations/markov                            1
      tools/qou-substrate/python/qou_substrate       1

## The correction

A 2026-09-04 check-in recorded the remaining surface as **"48 producers, NOT the
137 a grep reports — grep over-counts ~3x. Breakdown: qbeta 31, audits 11,
substrate 6."**

Two things are wrong with it, and the second is the costly one.

**The over-count factor is 2.15x, not ~3x** (209 -> 97). Minor.

**The 48 is THREE DIRECTORIES, read as the whole tree.** qbeta, audits and
substrate together are 44 of the 83 COMPUTE candidates. The other 39 —
**35 of them in `computations/` TOP LEVEL**, plus habiro, hecke, markov and
`qou_substrate` itself — appear in no reported figure at all. An agent working
from 48 drains three directories, reports the tranche complete, and leaves
~39 files still binding the retired pin as a number.

Same failure shape as the "31 producers COMPLETE" correction earlier in this
arc: a scoped count inherited and re-reported as a total. The defence is that
the tool is committed and prints its own scope line, so the next reader can see
what was and was not scanned.

## COMPUTE is a CANDIDATE list, and that is calibrated rather than asserted

Hand-checked 4 files: **3 true positives**, each literally
`q = mp.mpf("1.1099785955573347...")` — `gap_a4_numeric_search`,
`lever1_gevrey_order_pin`, `binding_wn_derive_or_refute`. **1 false positive**:
`muon_pin_three_values_probe`, which carries the pin inside an assertion DETAIL
STRING and is legitimately about the three muon values.

The tool now requires the literal to PARSE as a number, which is what separates
`mp.mpf("1.10997...")` from prose containing a number; that case is pinned in
the selftest. Several `audits/` entries will still be legitimate for the same
reason — confirm one at a time, do not sweep.

## Not yet drained

Nothing in this bean is fixed. It is the measurement plus the tool. The drain
order that follows the risk is: `computations/` top level (35, largest and
entirely unreported), then qbeta (29), then the rest.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8403, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
