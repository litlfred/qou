---
# qou-20sx
title: Weak-isospin (up/down-type) grading orthogonal to generation winding — the convergence target unlocking charmed-hadron masses + sin^2theta_W + hypercharge Y
status: in-progress
type: feature
priority: normal
tags:
    - reorg-2026-10-04
    - 8f-ew
created_at: 2026-08-02T19:10:31Z
updated_at: 2026-11-23T21:39:56Z
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



## Session Intent (2026-11-23)
Claimed by `claude/w2-h7-h8-hypercharge-zremoval-20261123` (W2: H7/H8 two-row Wedderburn pair identities, coideal Killing-norm hypercharge slope 1/2, and Z-channel Yukawa removal).


Claimed by claude/w2-h7-h8-hypercharge-zremoval-20261123 (Worker 15)



## Session Results (2026-11-23 — PR litlfred/qou#9216, Issue #9215)
- **Branch:** `claude/w2-h7-h8-hypercharge-zremoval-20261123` (`b4948fad7d2` pre-registration -> `a9bdf696a8d` Lean + probe -> `e857686ddb1` witness).
- **Lean (`QOU/QBeta/CrossNucleonPairWedderburnZRemoval.lean`):** 35 theorems, `0 sorry`, `0` custom axioms (`[propext, Classical.choice, Quot.sound]` only, `§7c` generic, zero empirical constants in `.lean`). Proves Convention-D two-row Wedderburn collapse on `H_7(q)` (`C_7 = 429`, corank `4,611`) and `H_8(q)` (`C_8 = 1,430`, corank `38,890`), quantum Schur–Weyl character decompositions, right-spectator `z_D`/`z_D_bar` factorization (`L7e`, `L8e`), inductive left-spectator weight-counting operator `L_{m+1}(q)` with `L_2(q) = (q^2+1) L_1(q) - q^2 I_2` (`L8s` vs `L7s`), all-`q` pinned pair identity `alpha_6(q) + beta_6(q) = 1` excluding pure Coulomb on Hecke insertions, split-bundle `F = V_2 (+) W_3^*` Killing norms (`Tr_F((2 T_3)^2) = 2`, `Tr_F((Y/2)^2) = 5/6`, `Tr_G(T_3^2) = 2`, `Tr_G((Y/2)^2) = 10/3`, `sin^2 theta_W^0 = 3/8`) fixing GMN slope `1/2` (`(q_u, q_d) = (2/3, -1/3)`, chiral anomaly cancellation), and separated-hadron `Z`-channel Yukawa suppression `< 10^-280` for `x >= 653`.
- **80-dps Probe & Witness (`computations/probes/w2_h7_h8_wedderburn_zremoval/w2-h7-h8-wedderburn-zremoval.witness.json`):** `19/19` assertions passed (`< 10^-78` agreement on `H_7(q_0)` and `H_8(q_0)` Hoefsmit character traces across `pp`, `pn`, `nn` dressings; `x(r_{pi+-}) = 653.34488... => lambda(r_{pi+-}) = 1.8027e-284 < 10^-280`).
- **Status:** Kept `in-progress` per Rule 13a / reviewer-separated closure discipline.
