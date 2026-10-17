---
doc_id: arxiv-1203.2182v1
doc_title: "Volume Conjecture: Reﬁned and Categoriﬁed"
section_id: sec-001-11-generalized-volume-conjecture
section_title: "Generalized volume conjecture"
section_number: 1.1
pages: 2-4
source_pdf: 1203.2182v1.pdf
source_sha256: 2fe21af194f65227
toc_source: inferred
---
Generalized volume conjecture
2
1.2
Quantum volume conjecture
3
1.3
Quantization and deformation of algebraic curves
3
2.
The new conjectures: incorporating t
5
2.1
Quantum volume conjecture: reﬁned
6
2.2
Generalized volume conjecture: reﬁned
6
3.
Examples coming from knots
7
3.1
Sr homological invariants of (2, 2p + 1) torus knots
11
3.1.1
Reﬁned braid operators and gamma factors
14
3.1.2
From partition functions to superpolynomials
20
3.1.3
Homological algebra of colored knot invariants
25
3.2
Recursion relations for homological knot invariants
31
3.2.1
Unknot
31
3.2.2
Trefoil
33
3.2.3
Recursion in various limits
35
3.3
Reﬁned A-polynomials and the reﬁned “volume” S0(u, t)
37
3.3.1
Reﬁned A-polynomial and S0(u, t) for the unknot
38
3.3.2
Reﬁned A-polynomial and S0(u, t) for the trefoil
39
3.3.3
Saddle point analysis of the homological torus knot invariants
41
3.3.4
Asymptotic behavior in diﬀerent grading conventions
45
3.4
Relation to algebraic K-theory
49
3.4.1
Quantizability of reﬁned A-polynomials
51
4.
Examples coming from reﬁned BPS invariants
53
4.1
Reﬁned quantum mirror curves
57
4.2
Reﬁned mirror curves, S0(u, t) and quantizability
59
4.3
Reﬁnement as a twisted mass parameter
62
A. Miscellaneous results on knot invariants
67
A1
Macdonald polynomials
67
A2
Consistency check of the gamma factor (3.47) and (3.48)
69
A3
WKB analysis
70
A3.1
Another expression for Pn(T 2,2p+1; q, t)
70
A3.2
Asymptotic limit of PSn−1
DGR (T 2,2p+1; a, q, t) with a = q2t2
71
– 1 –
B. Proof of the gamma factor (3.47) and (3.48), by Hidetoshi Awata
74
C. Reﬁned A-polynomials
78
C1
Newton polygons
78
C2
Matrix forms of A-polynomials
81
1. Introduction
The story of the “volume conjecture” started with the crucial observation [1] that the so-called
Kashaev invariant of a knot K deﬁned at the n-th root of unity q = e2πi/n in the classical
limit has a nice asymptotic behavior determined by the hyperbolic volume Vol(M) of the
knot complement M = S3 \ K. Shortly after, it was realized [2] that the Kashaev invariant
is equal to the n-colored Jones polynomial of a knot K evaluated at q = e2πi/n, so that the
volume conjecture could be stated simply as
lim
n→∞
2π log |Jn(K; q = e2πi/n)|
n
= Vol(M) .
(1.1)
The physical interpretation of the volume conjecture was proposed in [3]. Besides ex-
plaining the original observation (1.1) it immediately led to a number of generalizations, in
which the right-hand side is replaced by a function of various parameters (see [4] for a review).
Below we state two such generalizations – associated, respectively, with the parameters ℏand
u – that in the rest of the paper will be “reﬁned” or, morally speaking, “categoriﬁed.”
1.1 Generalized volume conjecture
Once the volume conjecture is put in the context of analytically continued Chern-Simons
theory, it becomes clear that the right-hand side is simply the value of the classical SL(2, C)
Chern-Simons action functional on a knot complement M. Since classical solutions in Chern-
Simons theory (i.e. ﬂat connections on M) come in families, parametrized by the holonomy of
the gauge connection on a small loop around the knot, this physical interpretation immediately
leads to a “family version” of the volume conjecture [3]:
Jn(K; q = eℏ)
n→∞
ℏ→0
∼
exp
1
ℏS0(u) + . . .

(1.2)
parametrized by a complex variable u. Here, the limit on the left-hand side is slightly more
interesting than in (1.1) and, in particular, also depends on the value of the parameter u:
q = eℏ→1 ,
n →∞,
qn = eu ≡x
(ﬁxed)
(1.3)
In fact, Chern-Simons theory predicts all of the subleading terms in the ℏ-expansion denoted
by ellipsis in (1.2). These terms are the familiar perturbative coeﬃcients of the SL(2, C)
Chern-Simons partition function on M.
– 2 –
