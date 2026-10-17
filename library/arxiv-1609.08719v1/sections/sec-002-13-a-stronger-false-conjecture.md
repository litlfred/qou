---
doc_id: arxiv-1609.08719v1
doc_title: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE"
section_id: sec-002-13-a-stronger-false-conjecture
section_title: "A stronger, false conjecture"
section_number: 1.3
pages: 1-2
source_pdf: 1609.08719v1.pdf
source_sha256: f61ff2111e9a97f9
toc_source: outline
doc_brief: "AN EXPERIMENTAL INVESTIGATION OF NEUMANN’S CONJECTURE — We use a large census of hyperbolic 3-manifolds to experimentally investigate a conjecture of Neumann regarding the Bloch Group."
---
A stronger, false conjecture
2
1.4.
Exotic volumes
2
Acknowledgments
3
2.
Background
3
2.1.
Cross-ratios
3
2.2.
The invariant trace ﬁeld
3
2.3.
The Bloch group
4
2.4.
Gluing Equations
4
2.5.
Ptolemy coordinates
7
2.6.
Lattice matching
8
3.
Experimentation
10
3.1.
Manifold generation
10
3.2.
Lattice matching
11
3.3.
Linear combinations for exotic volumes
11
4.
A counter-example to conjecture 1.3
11
5.
Evidence for conjecture 1.2
12
5.1.
Examples of missing ﬁelds
12
5.2.
Data analysis
12
6.
Selected examples
14
References
17
Date: 2016-09-17.
2010 Mathematics Subject Classiﬁcation. 57N10 (primary), and 57M27 (secondary).
This work was supported in part by the National Science Foundation through the Research
Experiences for Undergraduates (DMS# 1359307) at the University of Maryland, College Park.
1
arXiv:1609.08719v1  [math.GT]  28 Sep 2016
2
GILLES AND HUSTON
1. Introduction
Our primary result, described in section 3, is a large census of hyperbolic 3-
manifolds, organized by invariant trace ﬁeld, together with tables expressing vol-
umes as linear combinations of other manifolds’ volumes. This census is available
at http://www.curve.unhyperbolic.org/linComb.
Examining this census has
allowed us, in many cases, to explicitly list manifolds which give rise to elements in
the Bloch groups of certain invariant trace ﬁelds that span all the elements of that
Bloch group we observed, supporting a conjecture of Neumann.
1.1. Neumann’s conjecture. For a hyperbolic 3-manifold M, we denote the el-
ement it induces in the Bloch Group (see section 2.3) as [M]. The conjecture we
primarily studied was given in [Neu11], and stated in this form by [GTZ15]:
Conjecture 1.1 (Neumann). Let F ⊂C be a number ﬁeld not contained in R,
and let M be the set of manifolds with invariant trace ﬁelds contained in F,
M := {M ∼= H3/Γ | Q(tr Γ(2)) ⊆F}.
Let N = {[M] | M ∈M} be elements of the Bloch group determined by manifolds in
M (see section 2.3). Then integral combinations of elements of N generate B(F).
1.2. Neumann’s weaker conjecture. Neumann has also proposed a weaker con-
jecture which our results also support.
Conjecture 1.2 ([Neu11, Conjecture 1]). Every non-real concrete number ﬁeld k
