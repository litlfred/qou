---
doc_id: 0309214v3
doc_title: "The colored Jones function is q-holonomic"
section_id: sec-008-51-finding-a-recursion-relation-for-multisums
section_title: "Finding a recursion relation for multisums"
section_number: 5.1
pages: 16-18
source_pdf: 0309214v3.pdf
source_sha256: 53967ef30b0aedb9
doc_brief: "The colored Jones function is q-holonomic — A function of several variables is called holonomic if, roug hly speaking, it is determined from ﬁnitely many of its values via ﬁnitely many l inear"
---
Our starting point are multisums of q –proper hypergeometric functions. Recall
the deﬁnition 2.3 of a q –proper hypergeometric function F (n, k) from Section
2.4, and let G denote
G(n) :=
∑
k≥0
F (n, k)
throughout this section.
With the notation of Equation (1), Wilf–Zeilberger show tha t:
Theorem 5 ([33, Sec.5.2])
(a) F (n, k) satisﬁes a k –free recurrence relation of order at most
J ⋆ := (4ST B2)r
r!
Geometry & Topology, Volume 9 (2005)
The colored Jones function is q –holonomic 1269
where B = max s,t{|bs|, |vt|, |as|, |ut|} + maxµ,ν |aµ,ν | where aµ,ν are the coeﬃ-
cients of the quadratic form A.
(b) Moreover, G(n) satisﬁes an inhomogeneous recursion relation of order at
most J ⋆ .
Let us brieﬂy comment on the proof of this theorem. A certiﬁcate is an operator
of the form
P (E, Q) +
r∑
i=1
(Ei − 1)Ri(E, E1, . . . , Er, Q, Q1, . . . , Qr)
that annihilates F (n, k), where P and Ri are operators with P a polynomial
in E, Q, with P ⁄= 0. Here E is the shift operator on n, Ei (for i = 1, . . . , r)
are shift operators in ki , and Q is the multiplication operator by qk and Qi (for
i = 1, . . . , r) are the multiplication operator by qki , where k = (k1, . . . , kr).
The important thing is that P (E, Q) is an operator that does not depend on
the summation variables k. A certiﬁcate implies that for all ( n, k) we have:
P (E, Q)F (n, k) +
r∑
i=1
(Gi(n, k1, . . . , ki−1, ki + 1, ki+1, . . . , kr) −
Gi(n, k1, . . . , ki−1, ki, ki+1, . . . , kr)) = 0 ,
where Gi(n, k) = RiF (n, k). Summing over k ≥ 0, it follows that G(n) satisﬁes
an inhomogeneous recursion relation P G = error(n). Here error( n) is a sum of
multisums of q –proper hypergeometric functions of one variables less. It erating
the process, we ﬁnally arrive at a homogeneous recursion rel ation for G.
How can one ﬁnd a certiﬁcate given F (n, k)? Suppose that F satisﬁes a k–free
recursion relation AF = 0, where A = A(E, Q, E1, . . . , Er) is an operator that
does not depend on the Qi . Then, evaluating A at E1 = . . . Er = 1, we obtain
that
A = A(E, Q, 1, . . . ,1) +
r∑
i=1
(Ei − 1)Ri(E, Q, E1, . . . , Er)
is a certiﬁcate.
How can we ﬁnd a k–free recursion relation for F ? Let us write
A =
∑
(i,j)∈S
σi,j(Q)EiEj
where S is a ﬁnite set, j = ( j1, . . . , jr), Ej = Ej1
1 . . . Ejr
r , and σi,j(Q) are
polynomial functions in Q with coeﬃcients in Q(q); see [30]. The condition
Geometry & Topology, Volume 9 (2005)
1270 Stavros Garoufalidis and Thang T Q Lˆ e
AF = 0 is equivalent to the equation ( AF )/F = 0. Since F is q –proper
hypergeometric, the latter equation is the vanishing of a ra tional function in
Q1, . . . , Qr . By cleaning out denominators, this is equivalent to a syste m of
linear equations (namely, the coeﬃcients of monomials in Qi are zero), with
unknowns the polynomial functions σi,j . For a careful discussion, see [30]. As
long as there are more unknowns than equations, the system is guaranteed to
have a solution. [33] estimate the number of equations and un knowns in terms
of F (n, k), and prove Theorem 5.
Wilf–Zeilberger programmed the above proof, see [28]. As ti me passes the
algorithms get faster and more reﬁned. For the state-of-the -art algorithms and
implementations, see [26, 27] and [30], which we will use bel ow.
Alternative algorithms of noncommutative elimination, us ing noncommutative
Gr¨ obner basis, have been developed by Chyzak and Salvy, [8]. In order for ha ve
Gr¨ obner basis, one needs to use the following localization of the q –Weyl algebra
Br = Q(q, Q1, . . . , Qr)⟨E1, . . . , Er⟩
(Relq) .
and Gr¨ obner basis[8].
In case r = 1, B1 is a principal ideal domain [7, Chapter 2, Exercise 4.5]. In that
case one can associate an operator in B1 (unique up to units) that generates
that annihilating ideal of G(n). For a conjectural relation between this operator
for the sl2 –colored Jones function of a knot and hyperbolic geometry, s ee [11].
Let us point out however that none of the above algorithms can ﬁnd generators
for the annihilating ideal of the multisum G(n). In fact, it is an open problem
how to ﬁnd generators for the annihilating ideal of G(n) in terms of generators
for the annihilating ideal of F (n, k), in theory or in practice. We thank M
Kashiwara for pointing this out to us.
