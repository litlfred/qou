---
# qou-w0zn
title: 'GAP: hup off-diagonal (DU-UD=I) on the Young lattice — the last brick of the RSK-free SW-3 route'
status: todo
type: task
priority: normal
created_at: 2026-08-21T19:57:29Z
updated_at: 2026-08-21T19:58:02Z
---

## What landed (2026-08-21, bean qou-wtny, PR #5403)

QOU/Mathlib/YoungDiagramAddable.lean — sorry-free, axiom-clean:

    card_addableCells_eq_card_cornerCells_succ :
      (addableCells mu).card = (cornerCells mu).card + 1

for every Young diagram mu. Plus IsAddableCell + addCell (constructs mu u {c},
so the predicate is proved to mean "can be added"), mem_addableCells /
mem_cornerCells (the two Finsets ARE the intended sets), and the row-level
shift addableRows_eq : addableRows mu = insert 0 ((cornerRows mu).image (.+1)).

That is the DIAGONAL of DU - UD = I.

## The precise remaining obligation

hup (Sum_{lambda > mu} f^lambda = n . f^mu, for mu |- n-1) needs the full
DU - UD = I, of which two pieces are still missing.

**(1) The off-diagonal.** For mu != nu of the SAME size:

    #{lambda | lambda covers mu AND lambda covers nu}
      = #{kappa | kappa covered by mu AND kappa covered by nu}

Both sides are 1 when mu and nu differ by moving a single cell (the unique
witnesses being the union mu u nu and the intersection mu ^ nu), and both are 0
otherwise. This is a statement about PAIRS of diagrams; nothing in the landed
file touches it. The row-reindexing trick that made the diagonal easy does not
obviously transfer, because the two diagrams have independent row profiles.

**(2) The assembling induction.** Given diagonal + off-diagonal + hdown, hup
follows by induction on n:

    Sum_{lambda > mu} f^lambda
      = Sum_{lambda > mu} Sum_{nu < lambda} f^nu          (hdown)
      = <DU mu, f> = <UD mu, f> + <mu, f>                 (DU - UD = I)
      = Sum_{nu < mu} Sum_{lambda > nu} f^lambda + f^mu
      = (n-1) . Sum_{nu < mu} f^nu + f^mu                 (induction, nu |- n-2)
      = (n-1) . f^mu + f^mu = n . f^mu                    (hdown again)

Not formalised. Needs DU/UD as operators on the free N-module on partitions, or
an equivalent Finset-sum formulation.

**(3) Separately, hdown's INSTANTIATION.** hdown itself is proved at general n
(QOU.Mathlib.numStandardYoungTableaux_branching), but it is indexed by the
corner subtype {c // IsCornerCell mu c}, whereas BurnsideViaBranching.sum_sq_step
wants a Finset of shapes cut out by an incidence. Bridging needs corner-erasure
to be a bijection onto {mu in shapes (n-1) | mu covered by lambda}. Bookkeeping,
not mathematics, but not free.

## Do not duplicate — check route 2 first

Bean qou-3c2j (PRs #5139/#5151/#5156) reaches the same identity by the
representation-theoretic route and was closer as of 2026-08-19: one brick left
(sSup_isotypicComponents -> a finrank sum over PartitionIndex). If that landed,
this route's value is as an independent combinatorial CONFIRMATION, and the
honest move is to verify rather than re-derive (AGENTS.md "converge on landing").

## Note on the corpus's other statement of the identity

OVTopAssembly.sum_numSYT_sq_eq_factorial states the identity and, per qou-wtny's
own refinement, carries a sorryAx. NOT re-verified in this session — treat the
sorryAx claim as unconfirmed until someone runs #print axioms on it.
