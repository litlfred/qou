---
# qou-eg4l
title: mpf-into-f-string crashes on mpmath 1.3.0 but NOT 1.4.1 — one latent site, and my first detector returned 0 against a true 5646
status: in-progress
pr: 8189
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-24T19:29:11Z
updated_at: 2026-10-10T07:55:52Z
parent: qou-9nnz
---



## The finding, and it CORRECTS a stated mechanism

Main's `17bf432f9e` fixed `wedderburn_pair_volumes.py` crashing on an `mpf`
reaching an f-string `:.4f`, and gave the mechanism as:

> "mpf has no `__format__` for the float presentation types, so `:.4f` raises
> TypeError"

**That is version-dependent, not universal.** Measured directly:

    mpmath 1.4.1:  f"{mp.mpf(1.5):.10f}"  ->  '1.5000000000'   NO crash
                   f"{mp.mpf(1.5):.2e}"   ->  '1.50e+00'       NO crash

So the crash is real on **1.3.0** and gone on **1.4.1**. This container
upgraded mpmath 1.3.0 -> 1.4.1 mid-session — visible in the `environment`
blocks of regenerated audit witnesses — which explains an otherwise confusing
pair of facts: the sibling's producer "exits 1 before writing anything", while
my run of the SAME producer at ~17:00 completed and wrote the witness. Neither
observation was wrong; they were taken on different mpmath.

The fix itself is still correct and should stand: `mp.nstr` is what AGENTS.md
prefers for display, and it does not depend on the mpmath version. What needs
correcting is only the scope — this is a **latent, environment-dependent**
crash, not a defect that fires everywhere.

## One live latent site

    computations/markov/markov_pipeline_cross_validator.py:254-255
        realizer={mp.mpf(c['realizer_value']):.10f}
        term6={mp.mpf(c['term6_value']):.10f}
        rel_diff={mp.mpf(c['rel_diff']):.2e}

Unwrapped `mpf` into float presentation specs. Fine on 1.4.1, would exit 1 on
1.3.0 before writing. Worth converting to `mp.nstr` for the same reason the
sibling's was — not urgent while the container is on 1.4.1.

## The measurement, including how badly my first attempt failed

    naive regex for the pattern          0     <- WRONG, and I nearly
                                                 reported "not a class" on it
    correct grep, raw hits            5646
    after removing float()/nstr wraps    7
    genuinely unwrapped mpf              1     <- the site above

**My first detector returned 0 against a true 5646.** It was an over-clever
character class that matched nothing. A null result from a hand-written regex
is not evidence of absence — this is entry N+1 in
`docs/audits/2026-08-15-detector-blindness-taxonomy.md`, and it happened in the
same session where I quoted that taxonomy at a subagent.

**6 of the surviving 7 were false positives**, all matching on `mpfr` in the
*filename* or a nearby string while the formatted value was a float timing
(`{time.time()-t0:.1f}s`, `{speedup:.2f}`). Filename proximity is not type
information.

## Why this is not a sweep

One site, latent, on a version the container no longer runs. Converting it is
a one-line change; enumerating "all mpf into f-strings" corpus-wide is not
statically decidable without type inference, and the 5646 -> 7 -> 1 funnel
shows why a grep-driven sweep would be almost entirely false positives. The
runtime signal — a producer that exits 1 — is the reliable detector, and it
already caught the only instance that mattered.


## 2026-10-10 re-audit verdict: **REPARENT** (bean `qou-am5t`)

Not a convention question. An `mpf` reaching an f-string `:.4f` crashes on
mpmath 1.3.0 and not 1.4.1 -- an environment/serialization defect. Keep open,
re-home.

Full 41-bean triage table and the method behind it: [`docs/coordination/convention-d-migration-status.md`](../../docs/coordination/convention-d-migration-status.md) §9.


## Round 52 Progress
- [x] PR https://github.com/litlfred/qou/pull/8189 (`523155d5604cc384f307eb1cb22785f1fded85da`): replaced `mpf.__format__` (`:.10f`, `:.2e`) sites with `mp.nstr(...)` in `computations/markov/markov_pipeline_cross_validator.py`, wired `record_upstream` + `w.add_upstream_records`, and regenerated `markov-pipeline-cross-validation.witness.json`.
