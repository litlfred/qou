---
doc_id: lect-mathematical-ideas-notions-qft-2002
doc_title: "Mathematical ideas and notions of quantum field theory"
section_id: page-016
section_title: "Page 16"
pages: 16-16
pdf_page: 16
source_pdf: lect-mathematical-ideas-notions-qft-2002.pdf
source_sha256: 95cac1ccd6c80226
text_source: ocr
granularity: page
doc_brief: "Mathematical ideas and notions of quantum field theory — 78 sections: Page 1; Page 2; Page 3"
---
16 MATHEMATICAL IDEAS AND NOTIONS OF QUANTUM FIELD THEORY

Physicists call the expression (In(Z/Zo))o the classical (or tree) approxima-
tion to the quantum mechanical quantity hln(Z/Zp), and the sum (In(Z/Z))o +
A(In(Z/Zo))1 the one loop approximation. Similarly one defines higher loop approx-
imations. Note that the classical approximation is obtained by finding the critical
point and value of the classical action S(#), which in the mechanics and field theory
situation corresponds to solving the classical equations of motion.

3.7. Nonlinear equations and trees. As we have noted, Theorem 3.5 does not
involve integrals and is purely combinatorial. Therefore, there should exist a purely
combinatorial proof of this theorem. Such a proof indeed exists. Here we will give
a combinatorial proof of the first statement of the Theorem (formula (10)).

Consider the equation S’(z) = 0, defining the critical point xo. This equation
can be written as « = G(x), where

B(x) = —S° gi BB,(a,2,...,2,2)/(6- Dh,

iD

where B-! : V* — V is the operator corresponding to the form B~!.

In the sense of power series norm, ( is a contracting mapping. Thus, 2 =
limnoo 6% (a), for any initial vector « € V. In other words, we will obtain xo if
we keep substituting the series 3(x) into itself. This leads to summation over trees
(explain why!). More precisely, we get the following expression for zo:

ni x
to = 19 ) > may

n TEGO (n,1)

where G (n, 1) is the set of trees with one external vertex and n; internal vertices
of degree i. Now, since S(x) = B(a,x)/2+ >° g;Bi(a,2,...,x)/i!, the expression
—S(ao) equals the sum of expressions ([] aT over all trees (without exter-
nal vertices). Indeed, the term B(xo,2o)/2 corresponds to gluing two trees with
external vertices (identifying the two external vertices, so that they disappear); so
it corresponds to summing over trees with a marked edge, i.e. counting each tree
as many times as it has edges. On the other hand, the term g;B;(xo,-..,20)/i!
corresponds to gluing i trees with external vertices together at the external vertices
(making a tree with a marked vertex). So )° 9;B;(xo,...,2%9)/i! corresponds to
summing over trees with a marked vertex, i.e. counting each trees as many times
as it has vertices. But the number of vertices of a tree exceeds the number of edges
by 1. Thus, the difference —S(a9) of the above two contributions corresponds to
summing over trees, counting each exactly once. This implies formula (10).

3.8. Counting trees and Cayley’s theorem. In this section we will apply The-
orem 3.5 to tree counting problems, in particular will prove a classical theorem due
to Cayley that the number of labeled trees with n vertices is n"~?.
We consider essentially the same example as we considered above: d= 1, B; =
2
—1, gi = 9. Thus, we have S(a) = 4 — ge*. By Theorem 3.5, we have
1

yr" ed) = —S(20),

n>0  TET(n)

where T(n) is the set of isomorphism classes of trees with n vertices, and 2o is the
root of the equation S'(x) = 0, i.e. x = ge”.
