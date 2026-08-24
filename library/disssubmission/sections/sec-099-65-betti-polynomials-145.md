---
doc_id: disssubmission
doc_title: "Tannakian categories of perverse sheaves on abelian varieties"
section_id: sec-099-65-betti-polynomials-145
section_title: "Betti polynomials 145"
section_number: 6.5
pages: 153-154
source_pdf: DissSubmission.pdf
source_sha256: 207fd5e3dc0d278d
doc_brief: "Tannakian categories of perverse sheaves on abelian varieties — 121 sections: Acknowledgements; Introduction; Introduction"
---
We ﬁrst deal with (i). For m∈{ 0,1} this is easily veriﬁed. In general one
computes that(t−1 +t)·Pm =Pm+1 +Pm−1 andt−1 +t = ξ2−2, so we have
the recursion formula
Pm+1 = ( ξ2−2)·Pm− Pm−1.
Assuming by induction that we already know the lemma forPm and Pm−1,
the coefﬁcient ofξ2c on the right hand side is
(−1)m+1−c[( m+c
m−c+1
)+2(m+1+c
m−c
)−( m+c
m−1−c
)].
The expression in square brackets is equal to(m+2+c
m+1−c
) due to the binomial
addition formulae
(m+1+c
m−c
)−( m+c
m−1−c
) =(m+c
m−c
), ( m+c
m−c+1
)+(m+c
m−c
) =(m+1+c
m+1−c
),
(m+1+c
m+1−c
)+(m+1+c
m−c
) =(m+2+c
m+1−c
).
This ﬁnishes the induction step and thereby proves equation (i). For ( ii)
note that
(−1)m−c(m+1+c
m−c
) =(−2c−2
m−c
)
and that form < 0 this binomial coefﬁcient vanishes ifc≥ 0. So it follows
that
∑
m≥0
(−1)m−c( 2g
d−m
)(m+1+c
m−c
) = ∑
m∈Z
( 2g
d−m
)(−2c−2
m−c
).
Now the sum on the right hand side is the coefﬁcient oftd−c in the power
series expansion of
(1+t)2g(1+t)−2c−2 = (1+t)2(g−c−1)
so that equation (ii) follows by direct inspection. □
Using the above lemma we can compute the Euler characteristic of the
stalk cohomology ofcδα for any partitionα and thereby conclude our proof
of the recursion formula in theorem 6.1 as follows.
COROLLARY 6.8. For any x∈ X(C) and any partitionα = (d1, . . . ,dn)
we have the formula
χ(H•(cδα)x
) = (−1)g ∑
c1,...,cn≥0
c1+···+cn=g
n
∏
k=1
(2(g−ck−1)
dk−ck
).
Proof.We have already remarked above that the negligible complexcδα
is a direct sum of degree shifts ofδX. Hence for anyx∈ X(C) we can write
it in the form
cδα = H•(cδα)x[−g]⊗C δX.
146 Chapter 6 – The generic rank of Brill-Noether sheaves
Since the Betti polynomial of the constant perverse sheaf isp(δX,ξ) = ξ2g
it follows that
p(cδα,ξ) = ξ2g·q(ξ),
whereq∈ C[ξ] is determined by
q(t1/2 +t−1/2) = ∑
m∈Z
(−1)m+gdimC(H m(cδα)x)·tm.
In particular, the Euler characteristic we are interested in is(−1)g times the
coefﬁcient ofξ2g in p(cδα,ξ). To compute this coefﬁcient, recall that by
deﬁnition we have a direct sum decompositionδα = pδα⊕cδα wherepδα
is a perverse sheaf without constituentsδX. The latter property implies that
the coefﬁcient ofte in h(pδα,t) vanishes for all|e|≥ g, hencep(pδα,ξ) is
a polynomial of degree less than 2g in ξ. In other words,
p(δα,ξ) = p(cδα,ξ) + terms of degree< 2g,
and it remains to note that in view of lemma 6.7 the coefﬁcient ofξ2g in the
polynomialh(δα,ξ) = h(δd1,ξ)··· h(δdn,ξ) is given by the sum displayed
on the right hand side of the corollary. □
