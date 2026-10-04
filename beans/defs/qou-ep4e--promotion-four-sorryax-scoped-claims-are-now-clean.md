---
# qou-ep4e
title: 'PROMOTION: four sorryAx-scoped claims are now clean and their scoping is stale'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:20:35Z
updated_at: 2026-10-04T15:22:15Z
parent: qou-6qbv
---

Surfaced by lean-axiom-guard while running /prepare-merge on PR 6096 (the Roth arc). NOT this
branch's work and not this branch's arc -- recording it because the guard explicitly asks for a
follow-up and nothing else will notice.

The guard's own words:

    *** PROMOTION -- an upstream gap closed:
        QOU.BraidKnot.OVTopAssembly.sum_numSYT_sq_eq_factorial
        QOU.BraidKnot.RSKBurnsideDischarge.rskBurnsideHolds
        QOU.BraidsAndKnots.PlancherelNormalisation.sum_sytDim_sq_eq_factorial
        QOU.BraidsAndKnots.PlancherelNormalisation.nuV_top_closed_form_unconditional
      Update the registry AND the claims that were scoped around the sorryAx.

Two distinct pieces of work, and the second is the one that rots:

1. The registry entry still records these four as sorryAx-dependent. Mechanical.
2. THE CLAIMS THAT WERE SCOPED AROUND THE sorryAx ARE NOW UNDERSTATED. Whatever prose, blocks or
   downstream lemmas hedge on "conditional on the RSK/Burnside discharge" are hedging on a
   condition that has been met. An understated claim passes every gate in this repo -- build,
   axioms, witnesses -- because it is TRUE. It just is not the theorem that was proved. That is
   the same failure mode as correction 24 from the Roth arc, where a weaker-but-true bound cost an
   exponent and nothing caught it.

The guard reports the promotion once, at the moment the olean set is fresh enough to see it. If
nobody acts on it the message is simply not printed again in any way that distinguishes it from
the ordinary clean run, so this bean is the durable record.

Related: o1b7 (wire rskBurnsideHolds), qou-0cyu (the TL/Hecke chain programme), agrd.
