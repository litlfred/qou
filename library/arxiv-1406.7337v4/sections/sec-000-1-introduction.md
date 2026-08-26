---
doc_id: arxiv-1406.7337v4
doc_title: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu"
section_id: sec-000-1-introduction
section_title: "Introduction"
section_number: 1
pages: 1-2
source_pdf: 1406.7337v4 (1).pdf
source_sha256: 5bae8237742733b9
doc_brief: "Semi-Adequate Closed Braids and Volume Adam Giambrone Alma College giambroneaj@alma.edu — In this paper, we show that the volumes for a family of A-adequate closed braids can be bounded above and"
---
One of the current aims of knot theory is to strengthen the relationships among the hyperbolic volume
of the link complement, the colored Jones polynomial, and data extracted from link diagrams. In a recent
monograph, Futer, Kalfagianni, and Purcell ([8], or see [7] for a survey of results) showed that, for suﬃciently
twisted negative braid closures and for certain Montesinos links, the volume of the link complement can be
bounded above and below in terms of the twist number of an A-adequate link diagram. The results for
Montesinos links were recently generalized by Purcell and Finlinson in [5]. Similar results for alternating
links were previously given by Lackenby in [13], with the lower bounds improved upon by Agol, Storm, and
W. Thurston in [1] and the upper bounds improved upon by Agol and D. Thurston in the appendix of [13]
and more recently improved upon by Dasbach and Tsvietkova in [4]. In a previous paper ([12]), the author
showed that the volumes for a large family of A-adequate link complements can be bounded in terms of
two diagrammatic quantities: the twist number and the number of certain alternating tangles in a given
A-adequate diagram.
In this paper, we show that the volumes for a family of A-adequate closedn-braids can be bounded above
and below in terms of the twist number t(D), the numbert+(D) of positive twist regions, the number t−(D)
of negative twist regions, the number n of braid strings, and the number m of special types of state circles
(called non-essential wandering circles ) that arise from a given closed braid diagram. Let v8 = 3.6638...
denote the volume of a regular ideal octahedron and let v3 = 1.0149... denote the volume of a regular ideal
tetrahedron. The main results of this paper, where the words “certain” and “more general” will be made
precise later, are stated below.
Theorem 1.1. ForD(K) a certain A-adequate closed n-braid diagram, the complement of K satisﬁes the
volume bounds
v8
2 · (t(D)− 2(n +m− 2))≤v8· (t−(D)− (n +m− 2))≤ vol(S3\K)< 10v3· (t(D)− 1).
For D(K) a more general A-adequate closed n-braid diagram, the complement of K satisﬁes the volume
bounds
v8· (t−(D)−t+(D)− (n +m− 2))≤ vol(S3\K)< 10v3· (t(D)− 1) = 10v3· (t−(D) +t+(D)− 1).
1
arXiv:1406.7337v4  [math.GT]  22 May 2015
AB
Figure 1: A crossing neighborhood of a link diagram, along with its A-resolution and B-resolution.
By restricting to a family of A-adequate closed 3-braids, we show that the volumes can also be bounded
in terms of the parameter s from the Schreier normal form of the 3-braid. It should be noted that the lower
bound provided in this paper, which relies on the more recent machinery of [8], is often an improvement over
the one given in [11].
Theorem 1.2. ForD(K) a certain A-adequate closed 3-braid diagram, the complement of K satisﬁes the
volume bounds
v8· (s− 1)≤ vol(S3\K)< 4v8·s.
In addition to providing diagrammatic volume bounds, we also show that, for the same family of A-
adequate closed 3-braids, the parameters k and s from the Schreier normal form can actually be read oﬀ of
the original 3-braid diagram.
The volumes for many families of link complements have also been expressed in terms of coeﬃcients of
the colored Jones polynomial ([3], [4], [8], [9], [10], [11], [16]). Denote the jth colored Jones polynomial of a
link K by
J j
K(t) =αjtmj +βjtmj−1 +··· +β′
jtrj +1 +α′
jtrj,
where j∈ N and where the degree of each monomial summand decreases from left to right. We will show
that, for ﬁxed n, the volumes for many of the closed n-braids considered in this paper can be bounded in
terms of the stable penultimate coeﬃcient β′
K :=β′
j (wherej≥ 2) of the colored Jones polynomial. A result
of this nature shows that the given collection of closed n-braids satisﬁes a Coarse Volume Conjecture ([8],
Section 10.4). This result, which is stated below, can be viewed as a corollary of Theorem 1.1.
Corollary 1.1. ForD(K) a certain A-adequate closed n-braid diagram, the complement of K satisﬁes the
volume bounds
v8· (|β′
K|− 1)≤ vol(S3\K)< 20v3·
(
|β′
K| +n +m− 7
2
)
.
Acknowledgments
I would like to thank Efstratia Kalfagianni for helpful conversations that led to this project. I would also like
to thank the anonymous referee for helpful comments that led to an improvement in the quality of exposition
in this paper.
