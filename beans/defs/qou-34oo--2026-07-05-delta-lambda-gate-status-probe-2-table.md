---
# qou-34oo
title: 2026-07-05 delta-lambda gate-status PROBE 2 table is convention-C-frame and is being quoted as current
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-29T07:05:14Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-cdx1
---

docs/audits/2026-07-05-delta-lambda-gate-status.md section PROBE 2 quotes
|b4c|=1.9614, sum-g=3.6310, delivered x1.540 vs needed x2.093 ('74% of target,
~26% short'). Those are convention-C-frame, computed 2026-07-06, before owner
ruling R1 (2026-08-15) made convention D canonical.

The committed witness was regenerated 2026-08-23 under D + the proton pin and
now reads z=0.612688, |b4c|=1.17395, delivered x1.398, del/need 0.6664. The
audit prose was not updated with it, so the doc and the witness it cites
disagree.

Re-measured on PR #5966 (computations/probes/he4_body_order_shortfall_location_probe.py):
the C branch reproduces the audit's numbers exactly (1.9614 / 3.63097 / 1.54019
/ 2.09252), confirming the table is C-frame rather than merely old.

Under canonical D the shortfall is LARGER: 33.4% short, not 26%. Fix is a
currency note on the audit doc naming the frame, not a recomputation — the
C-frame numbers are correct for C and should be kept as recorded per the
convention-D excision policy (scope them, do not 'fix' them).


## 2026-10-10 re-audit verdict: **LIVE** (bean `qou-am5t`)

A dated audit doc (2026-07-05) quoting C-frame PROBE-2 figures that are being
cited as current. Dated audit docs are deliberately left as records of their
own analysis (the `4.66e6` drain precedent); what is live is the CITATION of
them elsewhere. Live, and it is a citation-hygiene item, not a code item.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.

## 2026-10-10: the CITATION half was already fixed — the same day this bean was filed

The 2026-10-10 re-audit verdict above says *"what is live is the CITATION of
them elsewhere"*. Measured: there is **one** genuine external citation, and it
is a dedicated correction.

[`docs/audits/2026-08-29-he4-magnitude-shortfall-location.md`](2026-08-29-he4-magnitude-shortfall-location.md)
opens **§1 "Currency correction — the audit table in circulation is stale"**,
names `|b₄ᶜ| = 1.9614`, `Σg = 3.6310`, `×1.540`, `×2.093` and *"~26 % short"*
explicitly as **convention-C-frame**, gives the D values, carries the full
four-row comparison, and states 33.4 % against 26.4 %. It was written
**2026-08-29**; this bean was created **2026-08-29T07:05**. Both halves of the
work were done the same day and the bean never recorded that its own fix had
landed.

That is the third instance of this pattern found today, and the others are
worse: `qou-wgta` item 1 was fixed on the day *it* was filed and never
recorded, and `qou-4bq3` was fixed six weeks before a triage called it LIVE.
**A bean's own body is not evidence about the state of the tree** — AGENTS.md
path 6 says this of beans and this arc keeps proving it.

Every external hit on the bare figures (`1.9614`, `3.6310`, `1.540`, `26%`) is
otherwise digit-string noise — isotope-witness mass values, `_deprecated/`
braid-registry JSON, `.work/` regen logs — not a citation of this table.

### What was actually missing: the REVERSE pointer

Measured: `grep -c '2026-08-29-he4-magnitude\|shortfall-location'` on the
2026-07-05 doc returned **0**. A reader opening the stale doc had no way to
learn the correction existed. That is precisely this bean's own prescription —
*"a currency note on the audit doc naming the frame, not a recomputation"* —
and it is now in place on **both** `### The numbers` sections (PROBE 2 at the
`|b_A^c|` table, PROBE 2b at the `y_λ` trace table).

### Three refinements this bean does not carry

**1. `×2.093` is frame-ROBUST, and the bean says otherwise.** The body reads
*"Those are convention-C-frame"* of all four figures. Re-measured with
`he4_body_order_shortfall_location_probe.py`:

| quantity | C | D | |
|---|---:|---:|---|
| `\|b₄ᶜ\|` | 1.9614 | 1.17395 | −40 % |
| `Σg` | 3.6310 | 2.95077 | −19 % |
| delivered | ×1.54019 | ×1.39785 | −9 % |
| **needed** | **2.09252** | **2.09746** | **+0.24 %** |
| del/need | 0.7360 | 0.6664 | 26.4 % → 33.4 % short |

`needed` is AME-derived and moves 0.24 %. This matters because the 2026-07-05
doc's **open-work** sections (§"What it would require to advance", and the
untried-magnitude-lever paragraph) hand future agents *"supply the measured
2.093× at A=4 and 0 at A=6"* — and that target is **intact**. A blanket "all
C-frame" would have an agent discard a target that survives.

**2. The probe's verdict relocates the question, beyond currency.** In both
`f_pn` typings canonical D is *farther* from target than excised C, and `b₃` has
the **wrong sign** under both (−2.74 D / −3.22 C vs AME +1.43). So *"does the
bond convention close the gap"* is answered **no** and the shortfall is in the
body-order content. Scope-(a).

**3. PROBE 2b's D-frame status is UNMEASURED, not shifted — and that is a
bigger exposure than PROBE 2's.** Everything in that section is `y_λ`-weighted,
and `y_λ` is where `z` enters. Under D,
`QOU.SchurWeyl.ocneanuWeight_conventionD_eq_zero_of_three_rows` (sorry-free,
general `n`) zeroes **every** shape with a third row; of the 77 partitions of 12
exactly **7** have ≤2 rows, so the `H_12` trace is supported on **7 of 77**
blocks under D and **70 carry weight exactly zero**. Whether any of the 10
`e_4[h_3]` partitions forming `T_[1⁴]` is among those 7 decides whether
`T_[1⁴]` is *exactly zero* under D (headline void) or merely reduced.

🛑 **I did not settle it, and will not report a number for it.** Two attempts at
the `e_4[h_3]` plethysm **failed their own calibration** — fractional Schur
multiplicities, and a dimension check of **1955987** against the section's
stated **15400** — so the Murnaghan–Nakayama implementation was wrong both
times and no row-count claim follows. The calibration is what caught it, twice.
Settling it needs `computations/probes/su4_1111_markov_trace_probe.py`, which is
one of the two genuinely broken producers on `main` (an `mpf` reaching a
`scipy.sparse` matrix).

### Witness

Re-running the probe left `he4-body-order-shortfall-location.witness.json` with
**every number byte-identical** — the only payload change is two `content/` →
`folio/` paths the tree rename (#7485) left stale. Committed as such; it is a
provenance repair, not a recomputation.

**Re-scoped**, not closed: the currency work is done and the open item is now
PROBE 2b's `y_λ` support under D, which is blocked on the broken producer.

## Implementation & Witness Progress (PR #8273)
- Branch: `qou-10v9-34oo-43v0-580o-5ovu-5pgl` (`f56a97d3d6ca66bf63033f62ab41236e038a488a`), PR: `litlfred/qou#8273`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/Probe2ShortfallFrameChiCacheClobberPslqDetectorSpellingStage2CacheGuardAndBorromeanLiteral.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/probe2_shortfall_frame_chi_cache_clobber_pslq_detector_spelling_stage2_cache_guard_and_borromean_literal_probe.py` -> `computations/probes/probe2-shortfall-frame-chi-cache-clobber-pslq-detector-spelling-stage2-cache-guard-and-borromean-literal.witness.json` (`allPassed: true`, `scriptCommitSha: e98d91d4e01bb7197ccdfc0c0a05bab481cf2839`)

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8273, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
