---
doc_id: arxiv-0707.2340v2
doc_title: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS"
section_id: sec-007-33-determinantal-probability-measures
section_title: "Determinantal Probability Measures"
section_number: 3.3
pages: 17-20
source_pdf: 0707.2340v2.pdf
source_sha256: bf0f91277a5874ff
doc_brief: "NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS — W e introduce the class of strongly Rayleigh probability measures by means of geometric properties of their generating polyno mials that amount"
---
nantal probability measure on 2 [n] to be a measure µ ∈ Pn such that there is an
n × n matrix A so that for any subset S of [ n] one has
µ({T : S ⊆ T }) = det( A[S]), (11)
where as before A[S] denotes the principal submatrix of A whose rows and columns
are indexed by S. As discussed in e.g. [5, 57], such measures have important appli-
cations ranging from fermionic processes/continuous scaling limits o f discrete point
processes [23, 59] to the distribution of eigenvalues of random mat rices and zeros
of the Riemann zeta function [21], transfer current matrices [16], non-intersecting
random walks [47], Poissonized versions of the Plancherel measure o n partitions
[13] and Young diagrams [64], discrete orthogonal polynomial ensem bles [46], etc.
Recall that a square matrix A is said to be a contraction if ||A|| ≤ 1, where || · ||
denotes the supremum (operator) norm. Clearly, a positive semi-d eﬁnite matrix is
a contraction if and only if all its eigenvalues are in the interval [0 , 1]. Such matrices
were called positive contractions in [57].
Theorem 3.4. Suppose that µ is a determinantal measure on 2[n] whose corre-
sponding matrix is a positive contraction. Then µ is CNA +.
18 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
This is one of the main results of [57] (cf. [57, Theorem 8.1]), where ex terior
(Grassmann) algebra methods were used to investigate determina ntal probability
measures and, in particular, to prove the above theorem. As note d in loc. cit., The-
orem 3.4 provides a powerful tool for studying determinantal pro bability measures,
comparable to the FKG theorem in the theory of positive association , and is crucial
to most of the results in e.g. [59].
Let us show that Theorem 3.4 actually follows from Theorem 4.9 of §4.2 and
the fact that determinantal measures induced by positive contra ctions are strongly
Rayleigh:
Proposition 3.5. Suppose that µ is a determinantal measure on 2[n] whose corre-
sponding matrix is a positive contraction. Then µ is strongly Rayleigh.
Proof. Since positive deﬁnite matrices are dense in the set of all positive sem i-
deﬁnite matrices, by Proposition 3.1 (3) it is enough to prove the sta tement for
invertible positive contractions. Elementary computations show th at
gµ(z1, . . . , zn) = det( I − A + AZ) = det( A) · det(A−1 − I + Z),
where Z = diag(z1, . . . , zn). Since A is an invertible positive contraction, A−1 − I is
positive semi-deﬁnite and det( A) > 0, so by (6) the polynomial gµ is real stable. □
Another main result of [57] is that if A and B are commuting positive contrac-
tions and A ≤ B, then the measure corresponding to B stochastically dominates
the one corresponding to A (Deﬁnition 2.14). In §4.3 we extend this result using the
theory of stability and strongly Rayleigh measures and we prove tha t the condition
[A, B] = 0 (where [ ·, ·] denotes the Lie bracket) can be dropped from the hypothesis.
3.4. Graphs, Laplacians, Spanning T rees and the Random Cluster M odel.
Let G = ( V, E) be a graph with vertex set V = [ n] and edge set E. Associate to
each edge e ∈ E a variable we. If e connects i and j let Ae be the n × n positive
semi-deﬁnite matrix with the ii-entry and the jj -entry equal to 1, the ij-entry and
ji-entry equal to −1, and all other entries equal to 0. The Laplacian, L(G), of G is
deﬁned by
L(G) =
∑
e∈E
weAe.
Let
fG(z, w) = det( L(G) + Z).
Thus, by (6), fG is a multi-aﬃne real stable polynomial with non-negative coeﬃ-
cients. The Principal Minors Matrix-Tree Theorem (see, e.g., [18]) sa ys that
fG(z, w) =
∑
F
zroots(F )wedges(F ),
where the sum is over all rooted spanning forests F in G, roots( F ) ⊆ V is the set
of roots of F and edges( F ) ⊆ E is the set of edges used in F . Alternatively, we
may write fG as
fG(z, w) =
∑
F
wF ∏
C∈C(F )
(
∑
j∈C
zj),
where C(F ) is the partition of V whose parts are the vertices in the maximal trees
in F and the sum is over all forests in G. Since the class of stable polynomials is
closed under diﬀerentiation and specialization of variables at real va lues (see, e.g.,
[9]) we have that the spanning tree polynomial TG(w) =∑
T wT , where the sum is
NEGATIVE DEPENDENCE AND THE GEOMETRY OF POLYNOMIALS 19
over all spanning trees, is real stable (which is widely known). The co rresponding
probability measure is usually called the uniform random spanning tree measure
and is consequently strongly Rayleigh. Now if 1 denotes the vector of all ones as
in §2 then
fG(1, w) =
∑
F
ωG(F )wF ,
where the sum is over all spanning forests (independent sets) in G and ωG(F ) is
the product of the sizes of the connected components of F . In [72, Conjecture 5.10]
Wagner conjectured that fG(1, w) is a Rayleigh polynomial. By the above discus-
sion we have shown that more is actually true, namely:
Theorem 3.6. For any graph G the polynomial fG(1, w) is real stable.
Let G = ( V, E) be a graph and let q > 0 and 0 ≤ p ≤ 1 be parameters. The
random cluster (RC) model , see [33], is the measure µ on 2 E deﬁned by
µ(F ) = 1
ZRC
qk(F )p|F |(1 − p)|E\F |, F ⊆ E,
where k(F ) is the number of connected components in the graph ( V, F ) and ZRC
is the appropriate normalizing factor. The uniform spanning tree me asure can be
obtained from this model by letting p → 0 and q/p → 0, see [33, Section 1.5]. If
q ≥ 1, the RC model satisﬁes PLC and is therefore positively associated . If q ≤ 1,
NLC is satisﬁed, but other negative correlation properties are larg ely a matter of
conjecture. We are interested in properties closed under extern al ﬁelds so we assume
that p = 1 /2. The generating polynomial of µ is then a constant multiple of the
multivariate Tutte polynomial (see [70]):
ZG(z, q) =
∑
F ⊆E
qk(F )zF , z = (ze)e∈E.
If G = Cn, n ≥ 3, is a cycle and E = [n], then
ZG(z, q) =
n∏
j=1
(q + zj) + (q − 1)z1 · · · zn
and
∂ZG
∂z1
∂ZG
∂z2
− ZG
∂2ZG
∂z1∂z2
= q2(1 − q)
n∏
j=3
zj(q + zj),
so in this case the RC measure is Rayleigh, but not strongly Rayleigh.
If G is a tree, then
ZG(z, q) = q
∏
e∈E
(q + ze),
so the RC model is strongly Rayleigh. We conclude that on a general g raph G, the
RC model is strongly Rayleigh if and only if G is acyclic.
With the help of Mathematica c© , the third author has veriﬁed that the RC model
is Rayleigh for all simple graphs with at most ﬁve vertices.
20 J. BORCEA, P. BR ¨AND ´EN, AND T. M. LIGGETT
