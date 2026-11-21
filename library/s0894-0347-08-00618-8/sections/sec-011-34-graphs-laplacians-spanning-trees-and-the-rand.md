---
doc_id: s0894-0347-08-00618-8
doc_title: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8"
section_id: sec-011-34-graphs-laplacians-spanning-trees-and-the-rand
section_title: "Graphs, Laplacians, spanning trees and the random cluster model"
section_number: 3.4
pages: 18-20
source_pdf: S0894-0347-08-00618-8.pdf
source_sha256: 7c0b2ca41992b21c
toc_source: outline
doc_brief: "AMERICAN MATHEMATICAL SOCIETY S 0894-0347(08)00618-8 — 24 sections: Front matter; Introduction; A plethora of negative dependence"
---
Let G = (V, E) be a graph with vertex set V = [n] and edge set E. Associate to
each edge e ∈E a variable we. If e connects i and j let Ae be the n × n positive
semi-deﬁnite matrix with the ii-entry and the jj-entry equal to 1, the ij-entry and
ji-entry equal to −1, and all other entries equal to 0. The Laplacian, L(G), of G is
deﬁned by
L(G) =

e∈E
weAe.
Let
fG(z, w) = det(L(G) + Z).
Thus, by (6), fG is a multi-aﬃne real stable polynomial with non-negative coeﬃ-
cients. The Principal Minors Matrix-Tree Theorem (see, e.g., [18]) says that
fG(z, w) =

F
zroots(F )wedges(F ),
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS
539
where the sum is over all rooted spanning forests F in G, roots(F) ⊆V is the set
of roots of F and edges(F) ⊆E is the set of edges used in F. Alternatively, we
may write fG as
fG(z, w) =

F
wF

C∈C(F )
(

j∈C
zj),
where C(F) is the partition of V whose parts are the vertices in the maximal trees
in F and the sum is over all forests in G. Since the class of stable polynomials is
closed under diﬀerentiation and specialization of variables at real values (see, e.g.,
[9]) we have that the spanning tree polynomial TG(w) = 
T wT , where the sum is
over all spanning trees, is real stable (which is widely known). The corresponding
probability measure is usually called the uniform random spanning tree measure
and is consequently strongly Rayleigh. Now if 1 denotes the vector of all ones as
in §2, then
fG(1, w) =

F
ωG(F)wF ,
where the sum is over all spanning forests (independent sets) in G and ωG(F) is
the product of the sizes of the connected components of F. In [72, Conjecture 5.10]
Wagner conjectured that fG(1, w) is a Rayleigh polynomial. By the above discus-
sion we have shown that more is actually true, namely:
Theorem 3.6. For any graph G the polynomial fG(1, w) is real stable.
Let G = (V, E) be a graph and let q > 0 and 0 ≤p ≤1 be parameters. The
random cluster (RC) model (see [33]) is the measure µ on 2E deﬁned by
µ(F) =
1
ZRC
qk(F )p|F |(1 −p)|E\F |,
F ⊆E,
where k(F) is the number of connected components in the graph (V, F) and ZRC
is the appropriate normalizing factor. The uniform spanning tree measure can be
obtained from this model by letting p →0 and q/p →0; see [33, Section 1.5]. If
q ≥1, the RC model satisﬁes PLC and is therefore positively associated. If q ≤1,
NLC is satisﬁed, but other negative correlation properties are largely a matter
of conjecture. We are interested in properties closed under external ﬁelds, so we
assume that p = 1/2. The generating polynomial of µ is then a constant multiple
of the multivariate Tutte polynomial (see [70]):
ZG(z, q) =

F ⊆E
qk(F )zF ,
z = (ze)e∈E.
If G = Cn, n ≥3, is a cycle and E = [n], then
ZG(z, q) =
n

j=1
(q + zj) + (q −1)z1 · · · zn
and
∂ZG
∂z1
∂ZG
∂z2
−ZG
∂2ZG
∂z1∂z2
= q2(1 −q)
n

j=3
zj(q + zj),
so in this case the RC measure is Rayleigh, but not strongly Rayleigh.
If G is a tree, then
ZG(z, q) = q

e∈E
(q + ze),
540
J. BORCEA, P. BR¨AND´EN, AND T. M. LIGGETT
so the RC model is strongly Rayleigh. We conclude that on a general graph G, the
RC model is strongly Rayleigh if and only if G is acyclic.
With the help of Mathematica c
⃝, the third author has veriﬁed that the RC model
is Rayleigh for all simple graphs with at most ﬁve vertices.
