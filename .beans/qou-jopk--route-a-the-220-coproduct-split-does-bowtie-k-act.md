---
# qou-jopk
title: 'ROUTE A: the 2=2+0 coproduct split - does bowtie_K ACT on the depth-2 volume stratum?'
status: completed
type: task
priority: normal
created_at: 2026-09-04T20:42:08Z
updated_at: 2026-09-04T22:16:50Z
---

ROUTE A of epic qou-2q85. THE CHEAPEST LIVE ROUTE, and the only one needing NO new object.

WHAT IT IS. def:hq-bi-filtration's coproduct law splits depth: Delta_q(H_q^(n,K)) subset of + over n1+n2=n of H_q^(n1,K1) tensor H_q^(n2,K2). At n=2 the splits are 2=1+1 and 2=2+0. The 1+1 component needs the depth-1 stratum nobody has built (that is ROUTE B). The 2+0 component pairs the EXISTING depth-2 volume stratum with the EXISTING depth-0 interface layer.

SO THE QUESTION IS A MODULE STRUCTURE, NOT A MAP: does bowtie_K ACT on H_q^(2,K)? Not 'does the convolution layer map into the volume layer' - it cannot, 0+0=0 - but 'does it act on it', which the coproduct's 2+0 term is exactly the shape of.

WHAT TO CHECK FIRST, cheaply: is the action compatible with the Markov trace? tr_M is depth-PRESERVING (H_q^(n,K) -> P_n/P_{n-1}) per the same table, so a bowtie_K action on H_q^(2,K) would have to commute with tr_M to be meaningful for volume. That commutation is a finite check on objects that already exist.

COST: no new content object; a compatibility statement plus its proof. RISK: the action may be trivial - the 2+0 term could be the unit action, in which case nothing is learned. That is worth knowing early and is itself cheap to test.

DEFAULT IF NOTHING DONE: nothing changes; the two layers stay disconnected.

SETTLED 2026-09-04. THE ACTION EXISTS, IS WELL-DEFINED ON THE VOLUME STRATUM, AND IS TRIVIAL.

FIRST, A CORRECTION TO MY OWN FRAMING OF THIS ROUTE. I described the mechanism as the coproduct's 2 = 2+0 split. WRONG: a coproduct DECOMPOSES an element; it does not let a degree-0 element act on a degree-2 one. The action comes from the PRODUCT, via 0 + 2 = 2 - the same shuffle-additivity. H^(0) is a subalgebra and H^(2) is a module over it, automatically, in any filtered algebra. So the action does not need constructing; it is already there.

SECOND, THE POSITIVE HALF, PROVED. The action is well-defined ON THE VOLUME STRATUM: if degree-0 times degree-1 stays degree-1, multiplying a decomposable by a degree-0 element leaves it decomposable, so the action descends to the indecomposable quotient where the volume lives. QOU/Eightfold/IndecomposableQuotientPrune.lean: smul_mul_mem_decomposable, mkQ_smul_mul_eq_zero, both sorry-free, [propext, Quot.sound] only.

THIRD, THE NEGATIVE HALF - FROM THE CORPUS'S OWN TABLE. def:hq-bi-filtration's low-(n,K) grid gives H_q^(0,K) EXPLICITLY:
    unknot 0_1      -> scalars
    trefoil 3_1     -> e_(3) +/- e_(1,1,1)
    figure-8 4_1    -> e_(2,2)
    Bring input     -> scalars
At every tabulated cell the depth-0 stratum is spanned by the CENTRAL IDEMPOTENT, which is the UNIT of the localised algebra e_K H_q e_K - and H_q^(2,K) is BY DEFINITION the e_K-isotypic piece. The unit acts as the identity (unit_smul_eq_self, no axioms at all). So the action exists, descends, and DOES NOTHING.

WHAT ESCAPES, and it is not route A. bowtie_K is depth 0 but sits at a DIFFERENT CELL - the grid row gives it in H_6(q) on an EW braid in B_6, not at the cell of the knot whose volume is in question. A non-trivial action would have to come from the coproduct's CELL-MERGING K_1 * K_2 = K, which moves the VERTICAL axis, not the depth axis. That is a different structure from the one this bean proposed and this settlement does not touch it. If anyone opens it, open it as a new bean on the K-axis, not as a revival of A.

ONE THING CAUGHT BY THE COMPILER, worth recording: my first draft of this section contained 'theorem smul_mem_decomposable ... : exists y in decomposable mul, c . x = y OR True' - a TAUTOLOGICAL conclusion, the pattern banned by AGENTS.md Strict Lean Discipline section 5, in a file whose subject is honest pruning. Deleted rather than repaired. The file now passes a banned-pattern sweep (no ': True', no ':= trivial', no native_decide, no sorry) at 8 declarations.

CONSEQUENCE FOR EPIC qou-2q85: routes B and C were already closed; A is now closed too. The epic is down to E (qou-960k, PGL(3)/Fock-Goncharov, the only route aimed at flavour), D (qou-blla, template only, does not cross depth) and F (qou-zovy, hygiene). NO SURVIVING DEPTH-CROSSING ROUTE.
