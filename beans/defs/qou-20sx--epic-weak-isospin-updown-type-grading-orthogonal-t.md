---
# qou-20sx
title: Weak-isospin (up/down-type) grading orthogonal to generation winding — the convergence target unlocking charmed-hadron masses + sin^2theta_W + hypercharge Y
status: todo
type: feature
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-08-02T19:10:31Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-8lxd
---


Former title (before 2026-10-04, when this became a story under a programme epic): EPIC: weak-isospin (up/down-type) grading orthogonal to generation winding — the convergence target unlocking charmed-hadron masses + sin^2theta_W + hypercharge Y

## Scope (written 2026-10-10, owner decision 7b)

This node is the home for the **electroweak front** of the eightfold-way programme (epic `qou-8lxd`). Its target is a weak-isospin grading $T_3$ (up-type vs down-type) on the substrate states. That grading must be orthogonal to the generation winding (the torus knots $T(2,n)$ that index generations). With $T_3$ in hand, three things become assemblable:

- hypercharge $Y = 2(Q - I_3)$, which also needs a lepton-number map for $Y = B - L$;
- the $U(1)_Y$ normalisation, and with it $\sin^2\theta_W$;
- the up/down split needed for charmed and strange hadron masses.

It is open research, so per AGENTS.md rule 13a this bean is not closed until the mathematics closes.

**Children** (all `8f-ew`, reparented here 2026-10-10 from the epic):

| bean | what it is |
|---|---|
| `qou-buxs` | test whether the chiral $T_3$ grading supplies the mixed sign of $\Delta_\lambda$ |
| `qou-fbrp` | wire $T_3$ into $Y = 2(Q - I_3)$ and the $\sin^2\theta_W$ normalisation |
| `qou-h72x` | $\sin^2\theta_W$ comparison (inconclusive; inherits open $Y$ and $N=3$) |
| `qou-zd6l` | Weinberg angle: Higgs-vev automorphism not formalised |
| `qou-ghwy` | `close_321_weinberg_gap.py` is float64 end to end |
| `qou-kl39` | no state→$L$ map, so $Y = B - L$ cannot be assembled |
| `qou-ukqh` | categorical Higgs mechanism not derived |
| `qou-z3x8` | electroweak scale $v$: no derivation |
| `qou-pj82` | CKM: no flavour basis, no mixing-matrix object |
| `qou-y0mq` | PMNS: blocked on the flavour basis and the three-generation structure |
| `qou-ud3o` | categorical Wick rotation ($i\mapsto -i$ braiding flip) |

The brief that proposed this said 12 children; the measured count of open `8f-ew` beans other than this node and the epic is **11**. `qou-dnm1` (scrapped) and `qou-tdrd` (completed, the derived $T_3$ that `qou-buxs` consumes) are not reparented.

Upstream dependencies are outside this node: flavour SU(3) (`qou-j3w6`, owner chose to leave it as is on 2026-10-10) and the generation count (`qou-xtcl`, kept open on 2026-10-10).

## Round 66 Update (PR #8239)
- Formalized in `WeakIsospinGradingColourFibreRoutesLightQuarkExtractionTauLogConvexityAndPmnsCarrier.lean` and verified via 80-dps `mpmath` witness in PR #8239.

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8211, #8239, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
