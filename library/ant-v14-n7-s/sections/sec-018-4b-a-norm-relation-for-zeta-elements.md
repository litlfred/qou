---
doc_id: ant-v14-n7-s
doc_title: "Algebra & Number Theory Volume 14 No. 7 msp"
section_id: sec-018-4b-a-norm-relation-for-zeta-elements
section_title: "4B. A norm relation for zeta elements"
section_number: null
pages: 23-26
source_pdf: ant-v14-n7-s.pdf
source_sha256: ab695eddd565addf
---
zeta elements cZm,n,a which is analogous to Theorem 3.13, but simpler to prove.
Deﬁnition 4.7. For p prime, deﬁne a map
τp: Y∗
F(pm, pmn)→ Y∗
F(m, mn)
by composing the right-translation action of
( p
0
0
1
)
∈ GL∗
2(A f
F) with the natural projection.
Theorem 4.8. Suppose p is a prime with p| m, and suppose that a∈ OF maps to a generator of the
quotient OF/(pOF+ Z)∼= Z/pZ. Then we have the norm relation
(τp)∗(cZpm,n,a)=(Up)∗(Zm,n,a).
For simplicity, we give the proof under the slightly stronger hypothesis that p| n (rather than just
that every prime above p divides n, which is our running hypothesis). This only makes a difference
if p is ramiﬁed in F, and the proof can be extended to handle this extra case at the cost of slightly more
complicated notation; we leave the necessary modiﬁcations to the interested reader.
Firstly, note that there is a commutative diagram
Y∗
F(pm, pmn)
pr1 //
τp ((
Y∗
F(pm, mn)
pr2 // Y∗
F(m(p), mn)
π2
vv
π1

Y∗
F(m, mn) Y∗
F(m, mn)
(4-1)
where the top maps are the natural projection maps, τp is the twisted degeneracy map of the previous
section, andπ1,π 2 are the degeneracy maps of Section 2C.
Lemma 4.9. Let n′=(p)−1n. Under pushforward by the natural projection map
pr1: Y∗
F(pm, pmn)→ Y∗
F(pm, mn)= Y∗
F(pm, pmn′),
we have
(pr1)∗(cZpr+1,n,a)= cZpr+1,n′,a.
Proof. This is immediate from the corresponding norm-compatibility property of the Siegel units, which
is Proposition 3.5. Compare [Lei et al. 2014, Theorem 3.1.1]. □
1690 David Loeﬄer and Chris Williams
So we need to compare the classes Zpm,n′,a and Zm,n,a. Note that these both involve the same Siegel
unit cg0,1/m N. Let us write ua for the element
( 1
0
−a
1
)
.
Deﬁnition 4.10. (i) Let αpm,n,a denote the composition of the maps
YQ(pm, m N)↪→ Y∗
F(pm, mn) ua−→Y∗
F(pm, mn) pr2−→Y∗
F(m(p), mn).
(ii) Let ιm,n,a denote, as above, the composition of the maps
YQ(m, m N)↪→ Y∗
F(m, mn) ua−→Y∗
F(m, mn).
The following lemma is the key component in the proof of Theorem 4.8.
Lemma 4.11. Suppose that a∈ OF is a generator of OF/(pOF+ Z). Then:
(i) The mapαpm,n,a is injective.
(ii) The diagram
YQ(pm, m N)  αpm,n,a //

Y∗
F(m(p), mn)
π1

YQ(m, m N)  ιm,n,a // Y∗
F(m, mn)
is Cartesian, where the left vertical arrow is the natural projection.
The proof of this lemma is taken essentially verbatim from [Lei et al. 2018, Lemma 7.3.1], where the
analogous result is proved for real quadratic ﬁelds.
Proof. To prove part (i), note that the image of αpm,n,a is the modular curve of level
GL2(A f
Q)∩ u−1
a UF(m(p), mn)ua.
This intersection is the set of
( r
t
s
u
)
∈ GL2(ˆZ) such that
(r− at s + a(r− u)− a2t
t at + u
)
≡ I mod
( m pm
mn mn
)
.
We want to show that this is equal to UQ(pm, m N). Clearly, any
( r
t
s
u
)
in the intersection satisﬁes
(r s
t u
)
≡
(1∗
0 1
)
mod
( m ∗
m N m N
)
,
whilst
s+ a(r− 1)≡ 0 mod mp.
Suppose m= pqm′ with m′ coprime to p. We know that both summands are zero modulo m, so it sufﬁces
to check that they are both zero modulo pq+1. Since a generates OF/(pOF+ Z),{1, a} is a basis of
(OF/pq+1OF)⊗ Zp as a module over Z/pq+1Z; so both summands must be individually zero modulo
pq+1. But this means precisely that
(r
t
s
u
)
∈ UQ(mp, m N), as required.
p-adic Asai L-functions of Bianchi modular forms 1691
Part (ii) follows from the observations that the horizontal maps are both injections and that both vertical
maps are ﬁnite of degree p2. □
Remark 4.12. Since this lemma is crucial to the proof, we expand slightly on what part (i) really says.
The mapαmp,n,a is p-to-1 on connected components, in the sense that the preimage of a single component
of Y∗
F(pr(p), pr n) contains p connected components of Y∗
F(pr+1, pr N). The condition on a ensures that
the map ua “twists” these p components away from each other inside that single component of the target
space, so that their images are disjoint. In particular, the result would certainly fail without this condition;
for instance, if a= 0 then the map factors through YQ(m(p), m N).
Proof of Theorem 4.8. The Cartesian diagram of Lemma 4.11 shows that
(αmp,n,a)∗(cCm N)=(π1)∗(cZm,n,a).
But by deﬁnition,
(αmp,n,a)∗(cCm N)=(pr2)∗(cZmp,n′,a)=(pr2)∗(pr1)∗(cZmp,n,a), (4-2)
where the second equality follows from Lemma 4.9. From the commutative diagram (4 -1), we know that
(τp)∗=(π2)∗(pr2)∗(pr1)∗, whilst by deﬁnition (Up)∗=(π2)∗(π1)∗. Hence applying (π2)∗ to (4-2) gives
the result. □
We can now deduce the proof of the main theorem:
Proof of Theorem 3.13. We need to show that, for each j∈(Z/pr Z)×, we have
∑
k∈Z/pr+1Z
k= j mod pr
c4pr+1,n,ka=(Up)∗· c4pr,n, ja. (†)
We have a commutative diagram
⨆
k Y∗
F(pr+1, pr+1n)(k) τp //
spr+1

Y∗
F(pr, pr n)( j)
spr

Y∗
F,1(n) // Y∗
F,1(n)
The left-hand side of ( †) is exactly the pushforward of ∑
k cZpr+1,n,a(k) along the left vertical arrow
(where again we are using the notation x(k) for the projection of x to the k-th component). Theorem 4.8
shows that the pushforward of the same element along τp is(Up)∗cZpr,n,a( j). So it sufﬁces to check
that the operators(Up)∗ on Y∗
F(pr, pr n)( j) and on Y∗
F,1(n) are compatible under spr , which is clear by
inspecting a set of single-coset representatives (using our running assumption that all primes above p
divide n).
The case where r= 0 is a special case, since we must exclude the term c4p1,n,0 from the above sum,
introducing the−1 term of the theorem. □
1692 David Loeﬄer and Chris Williams
