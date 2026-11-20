---
# qou-ep4e
title: 'PROMOTION: four sorryAx-scoped claims are now clean and their scoping is stale'
status: todo
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-30T09:20:35Z
updated_at: 2026-11-20T16:06:50Z
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

- Round 85 (`lane-e667`): Formalized `qou-ep4e`, `qou-fpjy`, `qou-i6bn`, `qou-i6cn`, `qou-mkm8` in `QOU.Foundations.TableauSquareSumPromotionBinderObligationVisibilityLogDeterminantBoundaryStandaloneAxiomDistributionNonHyperbolicVolumeVanishing` with 80-dps `mpmath` 2-commit witness stamp (`dfc69944cbe55f3b2622843a90dea18c98e576d7` -> `cbb6c21aa01988c4135bc7451f24b559c8179f67`, `scriptHash=0e68280fe3476a3f8543bf6de4770766624506d689b2ae34edd201278173e989`) in PR `litlfred/qou#8455` (`status: in-progress`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8455, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
