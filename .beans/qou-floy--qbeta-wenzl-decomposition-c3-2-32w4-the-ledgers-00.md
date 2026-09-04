---
# qou-floy
title: 'qbeta Wenzl decomposition c3 = -2 - (3/2)W4: the ledger''s -0.0005 ppm ''exact match'' is convention-C; under canonical D it is +601 ppm'
status: todo
type: task
priority: normal
created_at: 2026-09-04T04:26:48Z
updated_at: 2026-09-04T04:27:25Z
---

## The claim

[`docs/coordination/2026-06-13-qbeta-habiro-element-ledger.md`](docs/coordination/2026-06-13-qbeta-habiro-element-ledger.md) L20-22:

> **Finding**: The residual **exactly matches** $-2 - \frac{3}{2} W_4(q)$, where
> $W_4(q) = \frac{1}{[4]_q!}$ is the alternating Wenzl weight.
> **Precision**: ... yields an error of **-0.0005 ppm** (compared to the N=2
> baseline error of 1.27 ppm and N=3 bound of 0.0094 ppm).
> **Physical Meaning**: The $-2$ scalar originates from the $F_3$ truncation
> (Habiro braiding projection). The $-\frac{3}{2} W_4$ explicitly involves the
> Wenzl weight over 4-strands ...

## Measured 2026-09-04, all three pins x both conventions

`eps_ppm = (Q_pred / Q_AME - 1) * 1e6`, at `mp.dps = 200`, reproducing
`probe_q_beta_wenzl_projectors.main()` exactly:

    pin                         convention C      convention D (CANONICAL)
    retired A                     -0.2175             600.9364
    muon CODATA-2022              -0.2177             600.9362
    proton (canonical)            -0.1871             600.9666

## Three separate conclusions, and the third is the one to carry

**1. The convention is the cause; the pin is not.** C -> D moves it ~2,760x
(0.22 -> 601 ppm). The pin moves it **0.03 ppm** in either convention. My first
hypothesis was that the agreement was a retired-pin artefact; that is WRONG and
the measurement above is what corrected it.

**2. Under the canonical convention the claim does not hold.** The ledger's
"exactly matches ... -0.0005 ppm" is a **convention-C** result. Convention D has
been canonical since the 2026-08-09 excision, and the probe now computes in D.
At the canonical convention the same expression misses by **+601 ppm** -- about
1.2 million times the claimed error, and ~470x WORSE than the N=2 baseline
(1.27 ppm) the ledger compares against.

This is exactly what AGENTS.md predicts: *"The ladder must be RE-DERIVED under
D, and that is not a z-swap ... treat every c_k conclusion as C-conditional."*
This bean is that warning with a number on it.

**3. THREE DIFFERENT NUMBERS ARE ON RECORD FOR ONE QUANTITY, and even convention
C does not reproduce either of the other two.**

    ledger prose                -0.0005 ppm
    its own cited witness       -0.0257 ppm     (51x apart from the ledger)
    current code, convention C  -0.1871 ppm     (7x apart from the witness)
    current code, convention D  +600.97 ppm     (canonical)

So the ledger already disagreed with the witness it cites, by 51x, before any
convention question. The residual C-vs-ledger gap is NOT explained here -- CODATA
2018 -> 2022 on `M_N`/`M_P` accounts for only ~0.22 ppm on Q_AME, so something
else in the probe's cone has also moved. Do not treat "convention" as the whole
explanation.

## Scope: (a), not (b)

This is a **scope-limited negative**. It says: *this expression, evaluated at the
canonical convention, does not reproduce Q_beta to the claimed precision.* It
does NOT exclude the Wenzl weight `1/[4]_q!` as an ingredient of a c_3 closure,
and the physical story about the `F_3` truncation is untouched by it. No proved
invariant forbids the ingredient, so per AGENTS.md no (b) claim may be written.

## What is fixed here and what is not

Fixed: `probe_q_beta_wenzl_projectors` now reads q0 by name (it held the retired
literal), and its witness is regenerated, so the 601 ppm is on the record instead
of a stale -0.0257.

NOT fixed, and deliberately: the ledger prose still claims the exact match. It
gets a dated correction pointing here rather than a rewrite -- the C-frame result
is a real historical measurement and AGENTS.md says to re-scope such findings,
never to delete them.
