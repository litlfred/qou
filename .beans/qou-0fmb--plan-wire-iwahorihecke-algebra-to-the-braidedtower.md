---
# qou-0fmb
title: 'PLAN: wire IwahoriHecke algebra to the BraidedTower theorem (#7153) -- discharge qou-301d instance (growing filtration + h!=0)'
status: todo
type: task
priority: normal
created_at: 2026-09-12T11:54:27Z
updated_at: 2026-09-12T11:54:28Z
---

Parent epic: qou-08a2. Records the 2026-09-12 finding that the growing+h!=0 BraidedTower instance (qou-301d's remaining gap) is a WIRING job, not a from-scratch build -- the two halves already exist and are unconnected.

## The two halves (both on main / in flight)
- ABSTRACT theorem (PR #7153, open, bean qou-301d): class BraidedTower (quad/far/braid) => sandwichReduces_all => towerSpan_of_braided => disjointBlock_of_braided. The q!=1 rewriting SandwichReduces is PROVED, generic in the tower. Its own caveat: "no BraidedTower instance with a growing filtration + h!=0 is constructed."
- CONCRETE algebra (QOU/IwahoriHecke/, 20 files, 1 axiom): Defn.lean has IwahoriHecke W R q with T_quadratic + T_braid PROVED over Mathlib Coxeter (GroupTheory/Coxeter/{Basic,Length,Inversion,Matrix}); qou-uoal (COMPLETED) gave the coset basis finrank(Hecke) <= (n+1)! sorry-free (HeckeCoset.lean = the Hn+1 = Hn (+) Hn gn Hn structure #7153 said "Mathlib does not supply"); BraidTower.lean has braidTower : BraidGroupN m ->* BraidGroupN(m+1) + braidTrace_peel (the Markov recursion); MarkovTrace.lean has GradedMarkovTraceExistence + markovTrace_cyclic.
- The gap (measured): grep of IwahoriHecke/ for OcneanuTrace/MarkovTrace R A/BraidedTower/TowerSpan is EMPTY. The concrete algebra is not wired to the abstract framework.

## Multi-session steps (the "all mathlib infra" to bean)
S1 (child): a single R-algebra A carrying g:N->A and a growing H:N->Subalgebra (the abstract MarkovTrace tower shape), built from the IwahoriHecke type-A tower / BraidTower.braidTower colimit. h = q - q^-1 != 0. This is the main construction gap.
S2 (links qou-g8i1): package the Ocneanu/Markov trace as the abstract MarkovTrace.tr : A ->L R with z, zinv and the markov / markov_inv axioms. qou-g8i1 (the z_d bond rule tr(x sigma_i)=z_d tr x) IS this axiom; IwahoriHecke/MarkovTrace + BraidTower.braidTrace_peel supply the peel. Do not duplicate g8i1.
S3: prove far (distant generators commute) on the N-indexed generators, from the Coxeter/braid structure.
S4 (child): instantiate #7153 BraidedTower (T_quadratic->quad h!=0, T_braid->braid, S3->far) and fire disjointBlock_of_braided => discharge qou-301d's instance UNCONDITIONALLY.

## Discipline
No fit (the whole point is derivation). Per rule 13a this arc and its children stay open until the math closes; the instance is the honest remaining gap. #7203 (rank-2 H2 functional, MERGED e0c10a77) is the h!=0 base object but single-generator (cannot grow); the symmetric-group tower #7131 is growing but h=0 -- S1 must supply the missing growing+h!=0 quadrant.

Links: qou-08a2 (epic), qou-301d/#7153 (theorem), qou-uoal (coset basis DONE), qou-g8i1 (Markov bond rule), qou-mbm9 (IwahoriHecke 36-axiom build), qou-nkd8 (class strengthening), qou-1ty8/#7203 (rank-2 base, merged).
