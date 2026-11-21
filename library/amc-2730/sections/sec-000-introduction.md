---
doc_id: amc-2730
doc_title: "Braid representatives minimizing the number of simple walks *"
section_id: sec-000-introduction
section_title: "Introduction"
section_number: null
pages: 1-3
source_pdf: amc_2730.pdf
source_sha256: 65730074a2925c6e
toc_source: outline
doc_brief: "Braid representatives minimizing the number of simple walks * — Given a knot, we develop methods for finding a braid representative that minimizes the number of simple walks."
---
Introduction
The Jones polynomial VLptq is an invariant of knots and links defined using quantum rep-
resentations of braids. It can be uniquely characterized as the polynomial-valued invariant
of oriented links with V⃝ptq “ 1 for ⃝the unknot and satisfying the skein relation
t´1VL`ptq ´ tVL´ptq “ pt1{2 ´ t´1{2qVL0ptq,
*The authors are especially grateful to Alexander Stoimenow for providing crucial input. They would also like
to thank Homayun Karimi, Robert Osburn, Andrew Nicas, Will Rushworth, and Cornelia Van Cott for valuable
feedback.
†Corresponding author. The author would like to acknowledge funding from the Natural Sciences and Engi-
neering Research Council of Canada.
‡The author acknowledges funding from a USRA award and a Stewart award from McMaster University.
E-mail addresses: boden@mcmaster.ca (Hans U. Boden), mattshimoda@hotmail.com (Matthew Shimoda)
cb This work is licensed under https://creativecommons.org/licenses/by/4.0/
where L`, L´, L0 are identical outside a neighborhood, where they are as pictured
L`
L´
L0.
The Jones polynomial admits a combinatorial state sum formula that can be used to com-
pute it, but the complexity of the computation grows exponentially with the crossing num-
ber. So this method is impractical for computations that involve links with a large number
of crossings.
The colored Jones polynomial is a powerful knot invariant packaged as a sequence of
Laurent polynomials JN,Kpqq for N ě 2, with N “ 2 giving the usual Jones polynomial.
It encodes subtle geometric information about the knot complement and appears in several
famous open problems in quantum topology, including (i) the Volume Conjecture [18, 23];
(ii) the Slope Conjecture [12, 17]; and (iii) the AJ Conjecture [11]. The first relates the limit
of JN,Kpqq for q “ e2πi{N as N Ñ 8 to the hyperbolic volume of the knot complement;
the second posits that every Jones slope of a knot is the slope of an incompressible surface
in the knot complement; and the third asserts that the recurrence relation for the N-th
colored Jones polynomials is given by the A-polynomial of [9], a plane curve associated to
the character variety of SLp2, Cq representations of the knot group.
For further background information on the colored Jones polynomial and its relation to
the geometry of 3-manifolds, we refer the reader to the books [24] and [10] and their ex-
tensive bibliographies. The colored Jones polynomial also has intriguing number theoretic
interpretations that will not be discussed in this paper; for more details about these aspects,
we refer the reader to the recent papers [3, 4, 20, 21] and their bibliographies.
Our goal in this paper is to study a probabilistic method for computing the colored
Jones polynomial. This approach was first developed by Huynh and Lê in [15], and it
was later described in terms of walks along braids by Armond [2]. Armond identified
the special role played by simple walks, resulting in an extremely efficient algorithm for
computing JN,Kpqq, which has been implemented by Hajij and Levitt [14]. The algorithm
is exponential in the number of simple walks on the braid, so it is natural to try minimize
the number of simple walks before executing the program of [14]. However, as we shall
see, this number is highly dependent on the braid representative chosen.
We study how the number of simple walks changes under taking reflection, rotation,
and cyclic permutation of a given braid. We also examine the growth rate of the number
of simple walks for two families of torus knots. For instance, for the family of p2, nq torus
knots, the simple walks satisfy a Fibonacci recurrence and grow exponentially in n. For
the family of p3, nq torus knots, the simple walks satisfy a tribonacci recurrence and also
grow exponentially in n. We further prove that the total number of simple walks on a braid
and its reflection is invariant under cyclic permutation. This fact is used to facilitate finding
braid representatives with the least number of simple walks. For knots up to 13 crossings,
we developed a program that finds minimal braid representatives. When these braids are
used in conjunction with the program of Hajij and Levitt [14], this provides an efficient
method for computing the colored Jones polynomial for these knots.
We close this section with a brief synopsis of the rest of this paper. In Section 2, we re-
view the method from [2, 15] for computing the colored Jones polynomial. In Section 3, we
use it to compute JN,Kpqq in closed form for the knots 52, 61, and 72. These computations
were originally performed by Masbaum using skein theory, see [22]. In Section 4, we recall
the basic results about braid representatives for knots and study the effect of the Markov
moves on the set of simple walks. In Section 5, we introduce the set of semi-simple walks,
and we show that it is invariant under cyclic permutation of the braid word. In Sections 6
and 7, we study the growth rate of the number of simple walks for two families of torus
knots. In Section 8, we present the output of a program for finding braid representatives
that minimize the number of simple walks.
