---
# qou-tfj0
title: 'GAP: canonical_tr_m_three_path_comparison asserts bridge = markov_peel while its own numbers disagree by 32-55%, and He-4 bridge is 0.0'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T14:23:36Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-9nnz
---

Surfaced while draining slice B of `qou-srvu` (witnesses reporting
`allPassed: true` while asserting nothing). This one is not a hygiene item —
it is a live contradiction between a witness's stated headline and its own
recorded numbers, and the missing assertion is exactly what hides it.

## The contradiction

`computations/canonical_tr_m_three_path_comparison.py` states as CONCLUSION 1
in its module docstring, and repeats in the witness `description` and in
`verdict.canonical_path`:

> Hoefsmit+Wenzl bridge = markov_peel. Both compute the sum over lambda of
> y_lambda(q) * chi^lambda(beta) with the canonical Markov weights; they are
> two algorithms for the same mathematical object.

Its own hardcoded comparison table gives them as identical:

    atom    bridge     markov_peel
    D       0.3883     0.3883      <- "bridge & peel agree"
    T       0.1041     0.1041
    3He     0.2065     0.2065
    4He     0.0553     0.0553

**The committed witness disagrees, and so does a fresh run on `main`:**

    atom      bridge_canonical      markov_peel      peel/bridge
    deuteron  0.5751722439177719    0.3882864715...  0.6750785972
    tritium   0.2293101021045565    0.1040521187...  0.4537615993
    helium-3  0.4037670368514282    0.2065408586...  0.5115347210
    helium-4  0.0                   0.0553483459...  None

The script prints a tick when `abs(ratio - 1) < 1e-3` and a cross otherwise.
It prints **a cross for all four atoms**. The witness reports
`allPassed: true`.

## Which column moved

`markov_peel` reproduces the docstring table EXACTLY (0.3883 / 0.1041 /
0.2065 / 0.0553). `bridge_canonical` does not. So the bridge side moved, by
roughly x1.48 (D), x2.20 (T), x1.95 (3He), and 4He is **absent**, which the
ratio code turns into `0.0` -> `None` rather than flagging.

Confirmed at the source: `computations/atomic-tr-m-mpfr-50dps.witness.json`
carries `helium-3` `tr_M_at_q0_50dps = "0.403767136906005195191097664298..."`,
i.e. the 0.4038 in the comparison, not the 0.2065 in the docstring.

## Why nothing caught it

The comparison witness has **zero assertions**, so `all([]) is True` and it
reads green to every consumer. That is `qou-srvu` exactly: the defect is not
that a check failed, it is that the claim was never expressed as a check, so
a 32-55 % disagreement sits under a green flag.

## Why slice B did not fix it

Two reasons, both deliberate.

1. **Adding the assertion would turn the witness RED on a substantive
   question, not a hygiene one.** The honest assertion here is
   `peel_vs_bridge_ratio ~ 1` at the file's own 1e-3 bar, and it fails for
   all four atoms. Landing that as a drain would flip a consumer-visible
   `allPassed` while leaving the underlying disagreement unadjudicated.
2. **The fix belongs upstream, in a producer slice B may not touch.** The
   bridge values come from `atomic_tr_m_mpfr_50dps.py`, which writes 2
   witnesses of which only 1 is in slice B — classified `MULTI-SLICE` under
   the coordinator's rule that a producer writing outside your slice must not
   be re-run.

## What the next agent has to decide

Which of these is true, because the two have opposite fixes:

- **The bridge witness regressed** (import-cone drift or a convention change
  in `atomic_tr_m_mpfr_50dps.py`), and CONCLUSION 1 is still correct — then
  the bridge is what needs re-deriving, and every downstream consumer of
  `atomic-tr-m-mpfr-50dps.witness.json` is affected.
- **The bridge is correct and CONCLUSION 1 is stale** — then the docstring,
  the witness `description` and `verdict.canonical_path` all state a refuted
  claim, and `markov_peel` is not the canonical path they say it is.

Do not assume the first. The docstring's own item 4 notes that "the literal
braid traces differ by a factor of 2" for the T/3He pair via the per-strand
(c, d) crossing parameters, so a factor-of-~2 normalisation difference is a
live candidate explanation for D/3He — but it does not explain T at 2.20, and
it does not explain 4He being absent from the bridge witness entirely.

## Reproduce

    python3 -u computations/canonical_tr_m_three_path_comparison.py

Reads existing witnesses and recomputes nothing, so it is instant and safe.
A re-run on this container changed only `engineVersion` / `environment`
stamps — every computed value is byte-identical to the committed witness, so
the numbers above are the state of `main`, not an artefact of this container.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8388, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
