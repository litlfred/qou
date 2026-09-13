---
# qou-0fmb
title: 'PLAN: wire IwahoriHecke algebra to the BraidedTower theorem (#7153) -- discharge qou-301d instance (growing filtration + h!=0)'
status: todo
type: task
priority: normal
created_at: 2026-09-12T11:54:27Z
updated_at: 2026-09-12T20:51:08Z
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


--------
**2026-09-12, MAJOR RE-SCOPE: S2 is NOT open. Jones' existence theorem is PROVED in the corpus, with uniqueness — in a DIFFERENT Markov-trace abstraction that nothing bridges.**

This plan scoped S2 (qou-g8i1) as "package the Ocneanu/Markov trace ... Jones'
existence theorem is open here". Measured on main (cb2d1f765), that is wrong.

  QOU/SchurWeyl/MarkovTraceInstance.lean   (200 lines, CODE-sorry 0, axiom-decls 0)
    wtrace          x |-> sum_{|nu|=n+1} W_nu * tr(rho_nu x), bundled ->L[R]
    wtrace_cyclic   T1  trace property
    wtrace_one      T2  normalisation
    wtrace_markov   T3  Markov stabilisation
    wtrace_incl     tr_{n+1}(incl x) = tr_n x   -- TOWER compatibility
    ocneanuMarkovTrace : HeckeCoset.MarkovTraceFamily R q q^-1 (q^3/(q^2+1))
    eq_wtrace_of_markov  -- every such trace IS this one

  QOU/SchurWeyl/MarkovTraceUnique.lean     (139 lines, CODE-sorry 0)
    structure MarkovTraceFamily (K) (q qi z)
      tr : (n : N) -> Hecke K q qi n ->L[K] K
      tr_one, tr_cyclic, tr_incl, tr_markov
    markovTrace_unique : any two agree

At CONVENTION D, z = q^3/(q^2+1) -- the canonical one -- with genericity
(q != 0, q^2 != 1, q^2+1 != 0, q^2 not a root of unity). So the existence AND
uniqueness of the Ocneanu trace on the Hecke tower are both proved.

**THE REAL GAP: there are TWO Markov-trace abstractions and NOTHING bridges them.**

  HeckeCoset.MarkovTraceFamily   LEVEL-INDEXED: one tr per n, tied by tr_incl.
                                 SchurWeyl. Has the genuine trace.
  OcneanuTrace.MarkovTrace       ONE algebra A + filtration H : N -> Subalgebra
                                 + ONE tr. MathlibExt. What BraidedTower /
                                 TowerSpanReduction / DisjointBlockTraceLaw consume.

Measured: grep for OcneanuTrace across QOU/SchurWeyl/ returns NOTHING. Zero
bridge. This is the SAME "two halves exist and are unconnected" pattern this plan
was opened to record, one level up -- and it is the same Fin-n-vs-N shape
difference that S1 resolved for the ALGEBRA, now recurring for the TRACE.

**Everything now funnels to ONE object: the colimit colim_n Hecke K q qi n.**
Building an OcneanuTrace.MarkovTrace out of the MarkovTraceFamily needs a single
algebra containing every level -- i.e. the colimit -- and then:

  * the TRACE descends for FREE. tr_incl IS exactly the colimit-compatibility
    condition; that is what it is for. No new trace mathematics is needed.
  * the FILTRATION needs heckeIncl INJECTIVE, which is ALSO what strict growth
    (qou-p8yg) needs.

So the epic's remaining work is not four steps. It is one construction (the
colimit / or the identification twH n ~= Hecke (n-1)) plus one lemma (heckeIncl
injective), and both S2 and qou-p8yg fall out of it.

Measured NOT-present, so do not assume: heckeIncl injectivity does not exist
anywhere (the only "inject" hits alongside heckeIncl are my own docstrings in
HeckeTowerWitness), and there is no DirectLimit of Hecke in the corpus.
