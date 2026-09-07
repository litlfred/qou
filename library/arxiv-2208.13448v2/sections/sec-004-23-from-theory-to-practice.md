---
doc_id: arxiv-2208.13448v2
doc_title: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS"
section_id: sec-004-23-from-theory-to-practice
section_title: "From theory to practice"
section_number: 2.3
pages: 7-9
source_pdf: 2208.13448v2.pdf
source_sha256: 8bfa244cf7ca867d
doc_brief: "ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER THREE EQUATIONS — In this paper we consider the problem of computing the diﬀere nce Galois groups of order three equations for a large"
---
can compute theoretically the Galois group of a diﬀerence equ ation of order 3. In practice
we may also need to make more assumptions on the diﬀerence ﬁeld (k, φ) in order to
compute eﬀectively the diﬀerence Galois groups:
• Assume that k is an eﬀective ﬁeld, i.e. that one can compute representative s of
the four operations + , −, ×, / and one can eﬀectively test whether two elements
of k are equal.
• Assume that, given a homogeneous linear diﬀerence system [ A] with A ∈ GLn(k),
we can eﬀectively ﬁnd a basis of its rational solutions, i.e. i ts solutions Y ∈ kn.
• Assume that given a diﬀerence operator L, if L admits at least one right factor
of order one, then we are able to compute eﬀectively one of such right factors.
When C = Q, for the cases (S, Q, M), the two ﬁrst points are satisﬁed. One can ﬁnd
some references for the second point in this table:
cases (S) (Q) (M) (E)
ref. [Abr95, AB98, vH98, AB01] [Abr95, AB01, Abr02] [CDDM18] [DR15, Com22]
Note that in the elliptic case the second point is not satisﬁe d, unless considering the case
n = 2, see [ DR15] (note that the latter is concerned by the more general probl em of solving
Riccati equations), or when the framework is modiﬁed, see fo r instance [ Com22]. Thus, in
that case, our algorithm may not lead to a systematic computa tion of the diﬀerence Galois
group. It will reduce the computation to the determination o f rational solutions of certain
linear diﬀerence equations that may be complicated to solve c oncretely. Throughout this
paper, we will emphasize which kind of equations we have to be able to solve.
We saw in Section 2.2 that the study of the irreducibility of the Galois groups is c losely
related to the factorisation of the diﬀerence operator. From Lemma 2.5, when we look at
a right factor of order one, we have to solve a Riccati equatio n of the form
n∑
i=0
ai
i−1∏
j=0
φj(α) = 0 .
8 THOMAS DREYFUS AND MARINA POULET
When C = Q, we are able to compute right-factors of order 1 in the cases ( S,Q,E)
but we want to emphasis that the complexity is exponential, i n the order of the equation,
contrary to the search of rational solutions, whose complex ity is polynomial. Here-below,
one can ﬁnd some references for these computations:
cases (S) (Q) (E)
ref. [Pet92, CvH06, ABPS21] [APP98, CvH06, ABPS21] [DR15, Com22]
For the Mahler case, the computation of Riccati solution is a work in progress by the ﬁrst
author of this paper, Chyzak, Dumas and Mezzarobba.
Example 2.7. Let us now present the strategy of [ABPS21] to show that the diﬀerence
Galois group of (1.1) over C(z1/∗) is irreducible, which is equivalent to show that the
corresponding operator has no factor of order 1. We point out the fact that C(z1/∗) is not
an eﬀective ﬁeld but the strategy still work in that case. Ass ume that t ⁄= 0 . Let us begin
by proving that there is no right factor of order one. Let
L = a0 + a1φ + a2φ2 + a3φ3
be the q-diﬀerence operator corresponding to (1.1), and let L∨ be its dual. By [ABPS21,
Lemma 3] , For any α ∈ k× there exist λ ∈ C×, ℓ ∈ N∗ and unitary b, c, r ∈ C[z1/ℓ] \ {0}
such that
α = λ b
c
φ(r)
r
and
• gcd(b, φk(c)) = 1 for all k ∈ {0, 1, 2};
• gcd(b, r) = 1 ;
• gcd(c, φ(r)) = 1 .
Using this, one can deduce by [ABPS21, Lemma 3] that if φ − α is a right factor of order
1 of L for some α ∈ k×, then, in the above decomposition for α, we have b|a0, c|φ−2(a3),
and
(2.4) λ3a3bφ(b)φ2(b)φ3(r)+λ2a2bφ(b)φ2(c)φ2(r)+λa1bφ(c)φ2(c)φ(r)+a0cφ(c)φ2(c)r = 0.
The strategy to decide whether L has a right factor of order one is the following. For
every unitary pair (b, c) ∈
(
C[z1/ℓ] \ {0}
)2
such that b|a0, c|φ−2(a3), we decide whether
there exist λ ∈ C× and r ∈ C[z1/ℓ] \ {0} such that (2.4) holds. If we ﬁnd a solution then
we have a right factor of order one, otherwise there is no righ t factor of order one. Here,
since a0 = q3z, a3 = t are monomials in z (recall that t ⁄= 0) the choices are very limited.
The only possibilities for the pair (b, c) are (zd, 1), with 0 ⩽ d ⩽ 1. Recall that deg(a3) = 0 ,
deg(a2) = 2 , deg(a1) = deg( a0) = 1 . The degrees of the terms in (2.4) are respectively
given by
3d + deg r(z), 2 + 2d + deg r(z), 1 + d + deg r(z), 1 + deg r(z)
and a direct calculation shows that, for 0 ⩽ d ⩽ 1, 2 + 2 d + deg r(z) is greater than the
remaining ones, whence there is no solution. We proceed simi larly with the dual for the
ON THE COMPUTATION OF THE DIFFERENCE GALOIS GROUPS OF ORDER T HREE EQ. 9
left factor of length one.
L∨ = a3(q−3z)σ−3
q + a2(q−2z)σ−2
q + a1(q−1z)σ−1
q + a0(z)
= σ−3
q
(
a3(z) + a2(qz)σq + a1(q2z)σ2
q + a0(q3z)σ3
q
)
Here the possible pairs for (b, c) are (1, zd), with 0 ⩽ d ⩽ 1. The degrees of the terms of
the equation corresponding to (2.4) are
1 + deg r(z), 1 + d + deg r(z), 2 + 2d + deg r(z), 3d + deg r(z).
Again, for 0 ⩽ d ⩽ 1, 2 + 2d + deg r(z) is greater than the remaining ones.
