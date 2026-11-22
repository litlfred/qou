---
doc_id: arxiv-1304.2934v4
doc_title: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS"
section_id: sec-front-matter
section_title: "Front matter"
section_number: null
pages: 1-4
source_pdf: 1304.2934v4.pdf
source_sha256: b7ed2a9e85264568
toc_source: outline
doc_brief: "MOD-φ CONVERGENCE, I: NORMALITY ZONES AND PRECISE DEVIATIONS — In this paper, we use the framework of mod-φ convergence to prove pre- cise large or moderate deviations for quite general sequences of"
---
MOD-φ CONVERGENCE, I:
NORMALITY ZONES AND PRECISE DEVIATIONS
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
ABSTRACT. In this paper, we use the framework of mod-φ convergence to prove pre-
cise large or moderate deviations for quite general sequences of real valued random
variables (Xn)n∈N, which can be lattice or non-lattice distributed. We establish precise
estimates of the ﬂuctuations P[Xn ∈tnB], instead of the usual estimates for the rate of
exponential decay log(P[Xn ∈tnB]). Our approach provides us with a systematic way
to characterise the normality zone, that is the zone in which the Gaussian approxima-
tion for the tails is still valid. Besides, the residue function measures the extent to which
this approximation fails to hold at the edge of the normality zone.
The ﬁrst sections of the article are devoted to a proof of these abstract results and
comparisons with existing results. We then propose new examples covered by this the-
ory and coming from various areas of mathematics: classical probability theory, number
theory (statistics of additive arithmetic functions), combinatorics (statistics of random
permutations), random matrix theory (characteristic polynomials of random matrices
in compact Lie groups), graph theory (number of subgraphs in a random Erd˝os-Rényi
graph), and non-commutative probability theory (asymptotics of random character val-
ues of symmetric groups). In particular, we complete our theory of precise deviations
by a concrete method of cumulants and dependency graphs, which applies to many
examples of sums of “weakly dependent” random variables. The large number as well
as the variety of examples hint at a universality class for second order ﬂuctuations.
Date: November 24, 2015.
1
arXiv:1304.2934v4  [math.PR]  23 Nov 2015
2
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
CONTENTS
1.
Introduction
4
1.1.
Mod-φ convergence
4
1.2.
Theoretical results
5
1.3.
Applications
7
1.4.
Forthcoming works
8
1.5.
Discussion on our hypotheses
8
Acknowledgements
9
2.
Preliminaries
9
2.1.
Basic examples of mod-convergence
9
2.2.
Legendre-Fenchel transforms
12
2.3.
Gaussian integrals
13
3.
Fluctuations in the case of lattice distributions
14
3.1.
Lattice and non-lattice distributions
14
3.2.
Deviations at the scale O(tn)
16
3.3.
Central limit theorem at the scales o(tn) and o((tn)2/3)
21
4.
Fluctuations in the non-lattice case
25
4.1.
Berry-Esseen estimates
26
4.2.
Deviations at scale O(tn)
29
4.3.
Central limit theorem at the scales o(tn) and o((tn)2/3)
30
4.4.
Normality zones for mod-φ and mod-Gaussian sequences
35
4.5.
Discussion and reﬁnements
36
5.
An extended deviation result from bounds on cumulants
38
5.1.
Bounds on cumulants and mod-Gaussian convergence
38
5.2.
Precise deviations for random variables with control on cumulants
39
5.3.
Link with the Cramér-Petrov expansion
43
6.
A precise version of the Ellis-Gärtner theorem
44
6.1.
Technical preliminaries
45
6.2.
A precise upper bound
46
6.3.
A precise lower bound
47
7.
Examples with an explicit generating function
48
7.1.
Mod-convergence from an explicit formula for the Laplace transform
48
7.2.
Additive arithmetic functions of random integers
50
7.3.
Number of cycles in weighted probability measure
55
7.4.
Rises in random permutations
58
7.5.
Characteristic polynomials of random matrices in a compact Lie group
61
8.
Mod-Gaussian convergence from a factorization of the PGF
64
8.1.
Background: central limit theorem from location of zeros
64
8.2.
Mod-Gaussian convergence from non-negative factorizations
64
8.3.
Two examples: uniform permutations and uniform set-partitions
67
8.4.
Third cumulant of the number of blocks in uniform set-partitions
68
9.
Dependency graphs and mod-Gaussian convergence
69
9.1.
The theory of dependency graphs
70
9.2.
Joint cumulants
72
9.3.
Useful combinatorial lemmas
73
9.4.
Proof of the bound on cumulants
76
9.5.
Sums of random variables with a sparse dependency graph
78
10.
Subgraph count statistics in Erdös-Rényi random graphs
80
MOD-φ CONVERGENCE, I
3
10.1.
A bound on cumulants
81
10.2.
Polynomiality of cumulants
83
10.3.
Moderate deviations for subgraph count statistics
85
11.
Random character values from central measures on partitions
88
11.1.
Preliminaries
91
11.2.
Bounds and limits of the cumulants
93
11.3.
Asymptotics of the random character values and partitions
96
References
100
4
VALENTIN FÉRAY, PIERRE-LOÏC MÉLIOT, AND ASHKAN NIKEGHBALI
