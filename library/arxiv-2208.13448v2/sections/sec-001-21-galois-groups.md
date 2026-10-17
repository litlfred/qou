---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-001-21-galois-groups
section_title: "Galois groups"
section_number: 2.1
pages: 2-3
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
toc_source: outline
---
of the diﬀerence Galois groups of q-hypergeometric equations, see [Roq11] and density
theorems [RS06, Pou20] but the present introduction does not pretend to be exhaustive.
Toward the proof of diﬀerential transcendence, we often need to prove that the diﬀerence
Galois group is suﬃciently big, making it important to be able to compute the latter.
However, the computation of diﬀerence Galois groups is in general a diﬃcult task. In the
literature one can ﬁnd many algorithms for the computation of Galois groups. The most
developed area is the one of diﬀerential equations: many algorithms are given to compute
diﬀerential Galois groups (which are algebraic groups attached to a linear diﬀerential
system), see for example [Kov86, SU93, CS99, BCWDV16, DW19]. There is a general
algorithm for the computation of the Galois groups of linear diﬀerential equations of an
arbitrary order but it is not eﬀective (see for example the algorithm of Hrushovski in
[Hru02] and some improvements [Fen15, AMP22]).
In contrast, the case of diﬀerence
equations is less developed. Algorithms have been given for the computation of diﬀerence
equations of order 1 and 2 in these four famous cases: the shift (see [VdPS97, Hen98]),
the q-diﬀerence (see [Hen97]), the Mahler (see [Roq18]) and the elliptic cases (see [DR15]).
For the shift case, an analogue of Hrushovski’s algorithm has been developed in [Fen18]. It
computes the Galois groups for equations of arbitrary order whose coeﬃcients are rational
functions but is still ineﬃcient. However, in general, for the Galois groups of diﬀerence
equations of order 3 or more, only few things are known. The aim of this article is to
explain how one can compute Galois groups of diﬀerence equations of order 3 under mild
assumptions on the diﬀerence ﬁeld to which the coeﬃcients of the diﬀerence equations
belong. In particular, it takes into account the four previous diﬀerence equations. We
highlight that we are mainly concerned by the theoretical aspects of the algorithm and no
study of complexity will be made. Throughout this paper, we explain what we need to be
able to do for using it in practice. In fact, the key point to apply it concretely is to be
able to ﬁnd rational (resp. hyperexponential) solutions to certain diﬀerence equations.
The starting point of this paper was an example suggested by Wadim Zudilin. This
example is running as a common thread throughout this paper. The following double sum
is related to the Rogers-Ramanujan identities
U(z, t) =
∞
X
m,n=0
qm2+3mn+3n2zmtn
(q; q)m(q3; q3)n
,
with (⋆; q)n = (1 −⋆) × · · · × (1 −⋆qn−1).
For each ﬁxed value of t, z 7→U(z, t) satisﬁes a q-diﬀerence equation:
(1.1)
ty(q3z) −(t + qt + q4z2)y(q2z) + q(t −q2z)y(qz) + q3zy(z) = 0.
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQ.
3
One of the questions asked by Zudilin was the computation of the Galois groups for the
values t = 1 and t = q2. We are going to compute the diﬀerence Galois groups over C(z1/∗)
for every value of t̸ = 0 and see that it does not depend on the parameter t. Note that
when t = 0, (1.1) is a q-diﬀerence equation of order 2 and the computation could be made
using [Hen98].
Theorem (Theorem 6.13). For all t ∈C∗, the diﬀerence Galois group of (1.1) is GL3(C).
Using [DHR21, Corollary 3.1] and Theorem 6.13, we may prove that for all t ∈C∗, there
are no nontrivial algebraic diﬀerential relations between U(z, t), U(qz, t) and U(q2z, t) over
C(z1/∗).
Now, we describe more precisely the content of this paper. After some reminders about
the Galois theory of diﬀerence equations in Section 2.1, we recall a criterion in Section 2.2
to know if the Galois group G of a diﬀerence equation is reducible or not. In Section 2.3,
we explain what we need, as a framework, in order to compute G in practice. In Section 3
we prove general results about Galois groups of diﬀerence systems of arbitrary order. We
explain the strategy for computing G if G is reducible in Section 3.1. If G is not reducible
we distinguish two cases: the imprimitive case and the primitive case. For the imprimitive
case, we give information (the connected component of the identity and its index in G) on
the possible Galois groups which occur when the order of the diﬀerence system is a prime
number in Section 3.2. Moreover, we know which information correspond to G thanks to
the knowledge of the determinant of G (which is the Galois group of an equation of order
1). After these general results, we recall the strategies for computing the Galois groups of
the diﬀerence equations of order 1 and the diagonal systems in Section 4 and the strategies
for the diﬀerence equations of order 2 in Section 5. Section 6 is devoted to the order three
case. We give an application to the diﬀerential transcendence in Section 7.
