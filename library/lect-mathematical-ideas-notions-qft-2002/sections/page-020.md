---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-020
section_title: "Page 20"
pages: 20-20
pdf_page: 20
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
20 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY

Theorem 3.10. The effective action Seg is given by the formula

Supa) = 22) _ > F

2 W
i>0

where
po(r)+1

By(a.2,....0) = TT 9i") Paar terete):

TEG1—irr(n,N)
where x, € V* is defined by x,(y) := B(a,y)

Thus, Ser = S +hS; + h?S. +.. The expressions h/S; are called the j-loop
corrections to the effective action.

This theorem allows physicists to worry only about 1-particle irreducible dia-
grams, and is the reason why you will rarely see other diagrams in a QFT textbook.
As before, it is very useful in doing low order computations, since the number of
1-particle irreducible diagrams with a given number of loops is much smaller than
the number of connected diagrams with the same number of loops.

Proof. The proof is based on the following lemma from graph theory.

Lemma 3.11. Any connected graph T can be uniquely represented as a tree, whose
vertices are 1-particle irreducible subgraphs (with external edges), and edges are the
bridges of T.

The lemma is obvious. Namely, let us remove all bridges from T. Then I will
turn into a union of 1-particle irreducible graphs, which should be taken to be the
vertices of the said tree.

The tree corresponding to the graph T is called the skeleton of T (see Fig. 9).

Graph: Skeleton:

FicuRE 9. The skeleton of a graph.

It is easy to see that the lemma implies the theorem. Indeed, it implies that
the sum over all connected graphs occuring in the expression of In(Zs/Zp) can be
written as a sum over skeleton trees, so that the contribution from each tree is
(proportional to) the contraction of tensors B; put in its vertices, and B; is the
(weighted) sum of amplitudes of all 1-particle irreducible graphs with i external
edges. |
