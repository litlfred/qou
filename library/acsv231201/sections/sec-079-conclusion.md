---
doc_id: acsv231201
doc_title: "Analytic Combinatorics in Several Variables Expanded Second Edition"
section_id: sec-079-conclusion
section_title: "Conclusion"
section_number: null
pages: 453-456
source_pdf: ACSV231201.pdf
source_sha256: 1a664d0bf666041e
toc_source: outline
doc_brief: "Analytic Combinatorics in Several Variables Expanded Second Edition — 100 sections: Front matter; Preface to the second edition; Preface to the first edition"
---
435
Problem 13.8. Find a way analogous to Theorem 13.8 to conclude minimal-
ity in some oﬀ-diagonal direction for some class of multi-aﬃne polynomials.
Replace the multi-aﬃne hypothesis in Theorem 13.8 by something weaker so
that the conclusion still holds.
Naively applying Gr¨obner basis methods typically breaks symmetry, but
recent research in computer algebra has given eﬀective methods for solving
polynomial systems with symmetric polynomials, including critical point sys-
tems [HL16; Fau+23].
Problem 13.9. Incorporate software for symmetric polynomial solving into
packages for ACSV computations.
Exercise 13.4. In four variables, let G = 1 −e1 + 27e4 be the Gillis–Reznick–
Zeilberger denominator, let K = 1 −e1 + 2e3 + 4e4 be the Kauers–Zeilberger
denominator, let S = e3(1 −x, 1 −y, 1 −z, 1 −w) be the Szeg˝o denominator,
and let L = e2(1 −x, 1 −y, 1 −z, 1 −w) be the Lewy–Askey denominator.
(a) Express G, K, S, and L as polynomials P1, . . . , P4 in the elementary sym-
metric functions e1, . . . , e4.
(b) Compute a Gr¨obner basis for ⟨P1, . . . , P4⟩as polynomials in the variables
e1, . . . , ed and describe the variety Ve deﬁned by the points (e1, . . . , ed)
where the Pj simultaneously vanish.
(c) Use this computation to ﬁnd the elements of V(G, K, S, L).
13.8 Conclusion
This book aims to illustrate eﬀective methods for computing asymptotic ap-
proximations to the coeﬃcients of multivariate generating functions. Such meth-
ods have many applications, and have already been used to study problems
arising in, among other areas, dynamical systems, bioinformatics, number the-
ory, statistical physics, algebraic statistics, string theory, information theory,
and queueing theory. We expect the number of applications to grow steadily.
While many (most?) applied problems can be tackled by a smooth point anal-
ysis, there are many interesting problems that involve much more complicated
local geometry, such as the tiling models discussed in Section 11.4.
From the standpoint of mathematical analysis, many of the tools required
to extend the basic ACSV results already exist. Problems for which mini-
mal points control asymptotics usually sidestep complicated topology, and the
Morse-theoretic intuition behind our results can often be ignored in such cases
436
Challenges and extensions
by casual users seeking to solve a speciﬁc problem. However, substantial topo-
logical diﬃculties can arise when dealing with contributing points that are not
necessarily minimal. We believe that to make further progress in this area, sub-
stantial work in the Morse-theoretic framework will be required.
This book is certainly not the last word on the subject, but rather an invita-
tion to the reader to join in further development of this research area, which
combines beauty, utility, and tractability, and which has given the current au-
thors considerable challenge and enjoyment over many years.
Notes
ACSV was the subject of an AMS-sponsored Mathematical Research Commu-
nity in 2020–2022, and a 2022 workshop at the American Institute of Math-
ematics. Among the topics discussed at these events, which still have active
research collaborations, are characterizations of CPAI [Gil22], software for
ACSV [LMS22], rational embeddings of algebraic functions [Gre+22], and
work in progress by Drmota and Pak on multivariate characterizations of so-
called N-algebraic functions. The methodology for algebraic functions given
at the end of Section 13.5 is contemporaneous to this edition and appears in
the preprint [BJP23], along with a new formula for coeﬃcient asymptotics in
terms of the deﬁning algebraic function.
Proving minimality by conventional means in Exercise 13.3 (c) above is
quite challenging; it is the basis of Problem B5 on the 2020 Putnam examina-
tion. The approach of Exercise 13.4 was suggested by Brendan Rhoades, and
Example 13.2 is adapted from [Sta99, Section 6.3].
Additional exercises
Exercise 13.5. (binomial transition) Consider the binomial coeﬃcient gener-
ating function (1 −x −y)−1, and compute ﬁrst-order asymptotics for the coef-
ﬁcient ars, where s/r →0 as r, s →∞. How many diﬀerent cases are there in
the analysis?
Exercise 13.6. Let P(x, y) = (1 −x)y2 −x2 as in Example 13.6.
(a) Show that for suﬃciently small ε > 0 there are two liftings by π−1 of the
centered circle of radius ε in C∗to a contour in V∗and that one of them
describes the positive square root y = x/
√
1 −x.
(b) Find all aﬃne critical points of V∗in direction (1, 0).
(c) Find all critical points at inﬁnity of V∗in direction (1, 0).
13.8 Conclusion
437
(d) Which of these critical points are at ﬁnite height?
(e) Which is more of a problem for computation, the double zero of P or the
existence of a critical point at inﬁnity?
Exercise 13.7. Find a general formula for det ΓΨ in terms of the partial deriva-
tives of Q when Q vanishes to degree 3 and is locally the product of three
transversely intersecting smooth divisors.
Appendix A
