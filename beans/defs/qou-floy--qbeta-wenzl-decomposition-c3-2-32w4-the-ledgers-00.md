---
# qou-floy
title: 'qbeta Wenzl decomposition c3 = -2 - (3/2)W4: the ledger''s -0.0005 ppm ''exact match'' is convention-C; under canonical D it is +601 ppm'
status: todo
type: task
priority: normal
created_at: 2026-09-04T04:26:48Z
updated_at: 2026-09-04T06:28:44Z
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


## RESOLVED 2026-09-04 — the 51x gap is explained, and the ledger figure is reproducible from NOTHING

The earlier entry said "the residual C-vs-ledger gap is NOT explained here". It is
now, by a 216-combination sweep over every free input: the q0 pin (retired A /
CODATA-2022 muon / proton), `m_e` (0.51099895000 / 0.51099895069), the `Q_AME`
source (hardcoded 0.78233341 / hardcoded 0.78233356 / computed from CODATA), the
Markov convention (C / D), the `hbar_q` definition ((q-1)/q vs q-1/q) and three
coefficient variants (-2-1.5W4 / -2-W4 / -2+1.5W4).

**The committed witness reproduces UNIQUELY, to 4.2e-9:**

    A / me18 / Q_AME hardcoded 0.78233341 / convention C / hbar=(q-1)/q / -2-1.5W4
      -> eps = -0.025722396 ppm     (witness records -0.0257224)

That recipe names exactly what has since changed:

1. **`Q_AME` was HARDCODED at 0.78233341.** The producer now COMPUTES it as
   `M_N - M_P - m_e = 0.78233356` from `codata_constants`. A 1.9e-7 relative
   shift, which against a residual of order 0.03 ppm is the whole 51x.
2. **Convention C.** Canonical is D since 2026-08-09, worth ~2760x.

So the three-way discrepancy was never one mystery: it is two independent,
identifiable changes, and the pin is not among them.

**The ledger's -0.0005 ppm is reproduced by none of the 216.** Closest is
**+0.0046 ppm** — ten times the quoted figure's own magnitude away, and that
combination differs from the witness's recipe only by using the proton pin. No
self-consistent parameterisation lands on -0.0005.

I do not know how that number arose and am not guessing. What is measured: the
witness is exactly reproducible and the prose is not, and the prose disagrees
with the witness it cites by 0.0252 ppm.

## The Lean carrier was a tautology with a false docstring — FIXED and verified

`QOU/BraidKnot/QBetaWenzlDecomposition.lean` carried

    theorem q_beta_c3_wenzl_decomposition_exact {q : ℝ} :
      q_beta_c3_wenzl_coefficient q = -2 - (3/2 : ℝ) * wenzlAltWeight 4 q := by
      rfl

`def X := E` then `theorem X = E := rfl` — banned by AGENTS.md §"Strict Lean
Discipline" rule 5, and doubly misleading because its docstring said it "formally
asserts" the full `Q_beta` ansatz, which no part of that file models. The
`q_beta_c3_wenzl_coefficient` docstring separately asserted the -0.0005 ppm
figure as fact.

Replaced with a statement that can fail:

    theorem q_beta_c3_wenzl_coefficient_ne_neg_two {q : ℝ}
        (hW : wenzlAltWeight 4 q ≠ 0) :
        q_beta_c3_wenzl_coefficient q ≠ -2

`lean`-direct **exit 0, no diagnostics**; `#print axioms` reports
`[propext, Classical.choice, Quot.sound]` — **no `sorryAx`**. The module has
**zero importers**, so blast radius is nil. Both docstrings now carry the
measurement and its convention.

## Note for whoever re-runs the sweep

The Lean `qInteger` uses HALF-powers,
`(q^(k/2) - q^(-k/2)) / (q^(1/2) - q^(-1/2))`, while the Python probe and this
sweep use `(q^n - q^(-n)) / (q - 1/q)`. Those are different brackets (the Lean
one is the Python one at `sqrt q`). Not the cause of anything above — the sweep
reproduces the witness with the Python convention — but do not assume the two
`W_4` agree when carrying a number between them.
