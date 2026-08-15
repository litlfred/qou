---
doc_id: arxiv-math-0508100v6
doc_title: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT"
section_id: sec-009-31-the-loop-expansion
section_title: "The loop expansion"
section_number: 3.1
pages: 8-9
source_pdf: 0508100v6.pdf
source_sha256: 9cc100a86b40c336
doc_brief: "ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT — To a knot in 3-space, one can associate a sequence of Laurent p olynomials, whose nth term is the nth colored Jones polynomial."
---
JK,n (eh) =
∞∑
i=0
aK,i (n) hi ∈ Q[[h]].
It turns out that aK,i (n) is a polynomial in n with degree less than or equal to i, see [ BNG96]. Hence
there are rational numbers aK,i,j , depending on the knot K, such that
ASYMPTOTICS OF THE COLORED JONES FUNCTION OF A KNOT 9
JK,n (eh) =
∑
0≤j≤i
aK,i,j njhi =
∑
0≤i, 0≤j≤i
aK,i,j (nh)jhi−j
=
∑
0≤j,k
aK,j +k,j (nh)j hk.
If we deﬁne
RK,k (x) =
∑
0≤j
aK,j +k,j xj ∈ Q[[x]],
then we have the following loop expansion
JK,n (eh) =
∞∑
k=0
RK,k (nh)hk ∈ Q[[h]](10)
It turns out that RK,k (x) ∈ Q(ex) are rational functions for all k. In fact, the MMR Conjecture states
that
RK, 0(x) = 1
∆ K(ex) ∈ Q[[x]].
More generally, Rozansky [ Roz98] proves there are Laurent polynomials PK,k (t) ∈ Q[t±1] such that in Q[[x]],
RK,k (x) = PK,k (ex)
∆ K(ex)2k+1 .
Remark 3.1. For every i, j, the function K → aK,i,j is a ﬁnite type invariant of degree i. Although the
polynomials PK,k (t) are not ﬁnite type invariants (with respect to the usual crossing change of knots), they
are ﬁnite type invariants with respect to a loop move described in [ GR04]. We will not use these facts in our
paper.
