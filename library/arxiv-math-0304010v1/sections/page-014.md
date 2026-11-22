---
doc_id: arxiv-math-0304010v1
doc_title: "Kerov's central limit theorem for the Plancherel measure on Young diagrams"
section_id: page-014
section_title: "Page 14"
section_number: null
pages: 14-14
source_pdf: 0304010v1.pdf
source_sha256: fc2296c027b3feb0
toc_source: undetermined
doc_brief: "Kerov's central limit theorem for the Plancherel measure on Young diagrams — Consider random Young diagrams with ﬁxed number n of boxes, dis- tributed according to the Plancherel measure Mn."
---
Corollary 2.8. For any k = 2, 3, . . .
epk
k = pk−1 + ⟨a linear combination of pk−2, . . ., p1⟩.
Conversely, for any k = 1, 2, . . .
pk = epk+1
k + 1 + ⟨a linear combination of epk, . . ., ep2⟩.
□
By Corollary 2.8, the elements ep2, ep3, . . . are algebraically independent genera-
tors of the algebra A:
A = R[ep2, ep3, . . .].
Deﬁnition 2.9 (cf.
[EO]). The weight grading of the algebra A is deﬁned by
setting
wt(epk) = k,
k = 2, 3, . . .
Equivalently, the weight grading is the image of the standard grading of Λ under
the algebra morphism
Λ = R[p1, p2, p3 . . . ] →A = R[ep2, ep3, . . .],
p1 →0,
pk →epk,
k = 2, 3, . . .
(2.18)
This deﬁnition is motivated by Proposition 2.11 below.
This morphism induces an algebra isomorphism Λ/p1Λ →A. Let us emphasize
the diﬀerence from the isomorphism Λ →A (Deﬁnition 1.6).
The weight grading induces a ﬁltration in A, which we call the weight ﬁltration
and denote by the same symbol wt( · ). Note that
wt(pk) = k + 1,
k = 1, 2, . . .,
because the top weight homogeneous component of pk is epk+1/(k+1), see Corollary
2.8.
Deﬁnition 2.10. a) We deﬁne an action of the multiplicative group of positive
real numbers on the set D0 by setting
ωs(x) = s−1ω(sx),
ω ∈D0,
s > 0,
x ∈R.
In other words, the graph of y = ωs(x) is obtained from that of y = ω(x) by the
transformation (x, y) 7→(s−1x, s−1y).
b) Since A = R[ep2, ep3, . . .], we may deﬁne the symbol f[ω] (where ω ranges over
D0) for any f ∈A. Speciﬁcally, write f as a polynomial in ep2, ep3, . . . and then
specialize each epk to epk[ω]. In this way, we realize A as an algebra of functions on
D0.
Proposition 2.11. Let f ∈A be homogeneous with respect to the weight grading,
Deﬁnition 2.9. Then for any ω ∈D0 and s > 0,
f[ωs] = s−wt(f)f[ω].
Proof. By the deﬁnition of the weight grading, it suﬃces to check that
epk[ωs] = s−kepk[ω],
k = 2, 3, . . .,
ω ∈D0,
s > 0.
(2.19)
Remark that the function σ(x) = 1
2(ω(x)−|x|) transforms in the same way as ω(x).
Then (2.19) is clear from Proposition 2.2.
□
14
