---
doc_id: pjm-v161-n1-p02-p
doc_title: "Studying links via closed braids. III. Classifying links which are closed 3-braids"
section_id: sec-050-resp-b-page-80
section_title: "(resp. b^ (page 80)"
section_number: null
pages: 80-80
source_pdf: pjm-v161-n1-p02-p.pdf
source_sha256: a93e922eab1ee67c
toc_source: inferred
doc_brief: "Studying links via closed braids. III. Classifying links which are closed 3-braids — 59 sections: Front matter; STUDYING LINKS VIA CLOSED BRAIDS I; it"
---
STUDYING LINKS VIA CLOSED BRAIDS III 
103
details from Figure 6.2. We have cut T open between the first and
second strands. We see that W contains the subword 
b^(b2)~
ιb^,
which is equivalent to (b2)~
ι(b^)
p+ι. 
We conclude that W does not
have shortest syllable length and is therefore not admissible.
Thus the only possibility is that each singularity of type [1-4] is
followed by another of type [1 - 4]. This completes the proof of
Lemma 6.5, and so also of the Classification Theorem. 
D
7. The algorithm and applications. Our task in this section is to
translate the Classification Theorem of §6 into an algorithm to decide
whether two links which are defined by closed 3-braids have the same
oriented link type in oriented 3-space. This problem is reduced, via
the Classification Theorem, to two other problems:
Problem A. Find unique representatives for conjugacy classes in B3 .
Problem B. Identify the unique representatives of the conjugacy
classes which correspond to links which are represented by more than
one conjugacy class of 3-braids.
There are several known solutions to Problem A and our algorithm
will use the solution which was given by Schreier in 1924 [Sc]. As
noted earlier, a new and different solution, due to P. J. Xu, is given in
[X]. In the latter conjugacy classes are represented by shortest words
in the elementary braids a\, a2, 03 which were used in the body of
this manuscript; the unique representatives of conjugacy classes are
shortest words in these generators, and therefore determine a surface
of maximum Euler characteristic with the link as its boundary. Our
reason for choosing Schreier's solution over Xu's at this time are that
it is a little bit easier to use than Xu's. Moreover, Xu has not yet
succeeded in finding normal forms which are expressed in terms of
shortest syllables as well as shortest words, so we do not have the
ability at this time to translate her work into an optimum algorithm
which orders braids by the complexity function which was the basis
of the work in this paper.
7.1. Schreier's solution to the conjugacy problem [Sc].
Step 0. We assume that we are given a 3-braid W = W(JL) which
is defined as a product of powers of the elementary braids σ\ and σ2
and their inverses, where a\ = <j\, a2 = σ2, #3 = σ2<
7i
CΓ^
1 Our goal
is to find a unique representative for the conjugacy class of W in B$.
