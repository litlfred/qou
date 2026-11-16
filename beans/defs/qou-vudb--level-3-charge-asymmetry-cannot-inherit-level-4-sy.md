---
# qou-vudb
title: 'Level-3 charge asymmetry cannot inherit level-4 symmetry: wrong A-scaling, and no fixed block to restrict to'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T11:00:10Z
updated_at: 2026-10-04T15:21:14Z
parent: qou-10v9
---

## The question

Owner, 2026-08-30: *"go ahead on the level-3/level-4 charge symmetry question"*.

`shell-schur-weyl-self-duality-interpretation` says Schur-Weyl self-duality is
**exact at level 4 (the shell)** while conjugate symmetry **breaks at level 3
(the inter-nucleon pair) via skein asymmetry**. Can a level-3 quantity inherit
charge symmetry from the level-4 structure?

**No, for two independent reasons.** One structural (Lean, sorry-free), one
measured (probe, 7/7).

## Prior art found first

`mba-sidecar-mirror-cancellation` already has the mirror-pair crossing
statistics: `sigma + sigma^-1 = 10A - 2` and `avg = 2A + 1` are bar-even and
**A-only, hence mirror-invariant**, while the bar-odd writhe `w = 4Z` is *"the
unique distinguishing statistic"*, `w(Z,N) - w(N,Z) = 4(Z-N)`. It records
observed splits and says the magnitude is *"open and unfitted"*. This work
prices it.

## Reason 1 (structural) — there is no invariant block to restrict TO

`QOU/MassTheory/PairIsospinAssignment.lean`, instantiating the corpus's own
`ShellSchurWeylSelfDuality` carrier at both levels:

    level3_no_fixed_point_level4_has_one :
      (forall b : Block,  not shellDuality.SelfDual b)
      and (exists b : Block4, shellDuality4.SelfDual b)

- **n = 2 (the pair):** the two partitions `(2)` and `(1,1)` are conjugate to
  each other, so the transpose is a **fixed-point-free swap**. `no_selfDual`.
- **n = 4 (the first shell):** `(2,2)* = (2,2)`, and `selfDual4_iff` proves it
  is the **unique** fixed point among the five partitions of 4.

So the corpus's architectural claim is **a theorem about partitions**, not a
modelling stipulation. And it is exactly why inheritance fails: a shell-level
charge-conjugation-invariant object has **no invariant pair-level block to
restrict to**. There is nothing at level 3 for level 4's symmetry to land on.

## Reason 2 (measured) — the A-scaling is wrong, and shells do not help

`computations/probes/mirror_charge_asymmetry_scaling_probe.py`, 20 odd-A mirror
pairs A = 3..41 against AME2020, proton pin, convention D, 7/7 assertions.

Under the Sec.10a log form the binding is additive over bonds, so a mirror
pair's difference collapses **exactly**:

    B(Z,N) - B(N,Z) = (n_pp - n_nn) * (B_pp - B_nn)

with `B_pp - B_nn = -1.74707324276 MeV` a **constant**, fixed by the skein
relation. So the model's whole mirror asymmetry is one constant times a bond
count, and the A-dependence is chosen by the assembly, not by physics:

    power law |dB| ~ A^p, least squares log-log, 20 pairs
      observed (AME2020)            p = 0.87383652
      model, chain assembly         p = 0            (flat by construction)
      model, complete graph         p = 1.1137411    (linear by construction)
      pure Coulomb (A-1)/A^(1/3)    p = 0.78040779   on THIS grid

The observed exponent is **bracketed by the two assemblies and matched by
neither**. It sits near the pure-Coulomb reference (steeper by 0.093 -- the
residual is presumably Nolen-Schiffer/CSB plus surface), and nowhere near 0 or 1.

**Do not quote the A=7 near-agreement as a success.** `chain/obs` runs
2.287 (A=3) -> 1.063 (A=7) -> 0.494 (A=15) -> 0.239 (A=39): a flat line crossing
a rising curve. The crossing is a coincidence of the crossing point, not a fit.

**LEVEL-4 TEST, the direct one.** If shell closure restored charge symmetry
downward, the model should do *better* at magic-touching pairs. Mean
`|ln(chain/obs)|`:

    magic-touching pairs (6):  0.90805485
    all others          (14):  0.89842358

**Magic pairs are marginally WORSE.** No rescue.

## Scope

Reason 1 is **exact and unconditional** (Lean, generic CommRing, 0 sorry 0
axiom). Reason 2 is **(a)** -- a measurement of A-scaling; the additive-mirror
identity it rests on is exact for the log form.

**Nothing is refuted.** `prop:skein-crossing-asymmetry` remains true of the
object it is about; what is established is its price and its reach.

## What this closes and what it opens

CLOSED: inheritance. A level-3 charge-symmetric observable cannot be obtained
by assembling the current bond factors, under either assembly, at any A, and
closed shells do not help.

OPEN, and now sharper: the model has **no EM channel at all** (qou-9v7t said
this from the other side). The observed mirror splitting is ~90% Coulomb, and
the model reproduces it with a *strong-channel* constant that has no business
carrying it. A repair supplies an explicit EM term at level 3 whose A-scaling
is Coulomb's, and lets the skein asymmetry be what it is -- small -- rather than
standing in for electromagnetism.

Parents: qou-1pig (the parity defect), qou-rvse (scrapped repair), qou-brng.

- **Round 55 Progress (`2026-11-16T21:09:27Z`)**: Opened [`litlfred/qou#8202`](https://github.com/litlfred/qou/pull/8202) (`61d4706edbc97c195108082e38b072c982ba2984`, Commit 1 `842a8da69cdb997861cc48f6f16593cc33e1e707`). Keeping bean at `status: in-progress` pending owner review.
