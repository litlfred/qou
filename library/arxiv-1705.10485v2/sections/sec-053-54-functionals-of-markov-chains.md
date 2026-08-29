---
doc_id: arxiv-1705.10485v2
doc_title: "Mod-φ convergence, II: Estimates on the speed of convergence"
section_id: sec-053-54-functionals-of-markov-chains
section_title: "Functionals of Markov chains"
section_number: 5.4
pages: 44-44
source_pdf: 1705.10485v2.pdf
source_sha256: b33759def53c6a43
doc_brief: "Mod-φ convergence, II: Estimates on the speed of convergence — In this paper, we give estimates for the speed of convergence towards a limiting stable law in the recently introduced setting of mod-φ"
---
In this section, we consider a discrete time Markov chain(Mt)t≥0 on a ﬁnite state spaceX, which
is ergodic (irreducible and aperiodic) with invariant measureπ. Its transition matrix is denotedP. To
simplify the discussion, we shall also assume that the Markov chain is stationary, that is to say that the
initial measure (i.e. the law ofM0) isπ; most results have easy corollaries for any initial measure, using
the fast mixing of such Markov chains.
Let us consider a sequence(ft)t≥0 of functions onX that is uniformly bounded by a constantK. We
set Yt = ft(Mt). We will show that{Yt}t∈N admits a uniform weighted dependency graph. The proof
roughly follows the one of [Fér16, Section 10], where it was proved that it has a (non-uniform) weighted
dependency graph, taking extra care of the dependence in the orderr of the cumulant in the bounds.
Instead of working directly with classical (joint) cumulants, we start by giving a bound for the so-called
Boolean cumulants. Classical cumulants are then expressed in terms of Boolean cumulants thanks to a
formula of Saulis and Statulevičius [SS91, Lemma 1.1]; see also a recent article of Arizmendi, Hasebe,
Lehner and Vargas [AHLV15] (we warn the reader that, in [SS91], Boolean cumulants are called centered
moments).
Let Z1,...,Z r be random variables with ﬁnite moments deﬁned on the same probability space. By
deﬁnition, their Boolean (joint) cumulant is
B(r)(Z1,...,Z r)
=
r−1∑
l=0
(−1)l ∑
1≤d1<···<dl≤r−1
E[Z1··· Zd1] E[Zd1+1··· Zd2]··· E[Zdl+1··· Zr].
While not at ﬁrst sight, this deﬁnition is quite similar to the deﬁnition of classical (joint) cumulants,
replacing the lattice of all set partitions by the lattice of interval set partitions; see [AHLV15, Section 2] for
details. Note however that, unlike classical cumulants, Boolean cumulants are not symmetric functionals.
Proposition 52.Letr≥ 1. With the above notation, there exists a constantθP depending onP with the
following property. For any integerst1≤t2≤···≤ tr, we have
⏐⏐⏐B(r)(Yt1,...,Y tr)
⏐⏐⏐≤M
r−1
