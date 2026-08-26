---
doc_id: arxiv-math-0203003v2
doc_title: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in represe"
section_id: sec-005-5-comparison-of-f-with-the-classical-kazhdan-lus
section_title: "Comparison of F with the classical Kazhdan-Lusztig functor"
section_number: 5
pages: 10-12
source_pdf: 0203003v2.pdf
source_sha256: 7579ae76959396b8
doc_brief: "On the quantum Kazhdan-Lusztig functor Pavel I. Etingof Adriano A. Moura etingof@math.mit.edu adrianoam@ime.unicamp.br Introduction One of the most exciting developments in representation the ory in t"
---
The sense in which the functor F is a q-analog of the Kazhdan-Lusztig functor is not straight for-
ward, and needs to be explained.
Indeed, the Kazhdan-Lusztig functor is a functor from the fu sion category of representations of
an aﬃne Kac-Moody algebra ˆg at some level k to the category of representations of the quantum
groupUv(g), where v =e
πi
m(k+h∨ ) . On the other hand, in this paper we do not seem to be consideri ng
any q-fusion categories.
10
Nevertheless, there is a sense in which F is a q-analogue of the Kazhdan-Lusztig functor. A
two-line justiﬁcation is that while the Kazhdan-Lusztig fu nctor arises from the analysis of the
monodromy of the Knizhnik-Zamolodchikov equations, the fu nctor F arises in a similar way from
the analysis of the monodromy of the quantum Knizhnik-Zamol odchikov equations. To some extent
this is explained in [FR92] and [KS95]. However, let us give a somewhat more vivid explanation,
in the special case g = sln. This explanation uses the small elliptic quantum group of T arasov and
Varchenko.
Recall that the classical Kazhdan-Lusztig functor F 0, essentially, does the following. Given a
ﬁnite dimensional representation V of g and a (generic) level k, it introduces on V an action of the
quantum group Uv(g), with v =e
πi
m(k+h∨ ) . More precisely, one ﬁrst uses the exchange construction
for ˆg at level k to turn V into a representation of the exchange dynamical quantum gro up Fv(G),
G =SLn (see [EV99]), and then turns it into a representation of Uv(g) by sending the dynamical
parameter to inﬁnity.
On the other hand, given a (generic) level k and a ﬁnite dimensional representation V of
Uq(g), the functor F introduces on V an action of the elliptic quantum group Eτ,γ/ 2(g), with
τ = − (k+h∨ ) log q
πi , and γ = log q
πi (by ﬁrst aﬃnizing V and then applying the functor F).
Now, one may check using modular invariance of theta-functi ons that Eτ,γ/ 2(g) is isomorphic to
E−1/τ,γ/ 2τ (g) (the corresponding dynamical R-matrices are gauge equiva lent). Thus, V becomes a
representation ofE−1/τ,γ/ 2τ (g). This representation is easily seen to be an evaluation rep resentation,
i.e., it factors through the small elliptic quantum group e−1/τ,γ/ 2τ (g) ([TV01]).
Finally, we claim that if k is ﬁxed then the algebra e−1/τ,γ/ 2τ (g) is a q-deformation of the
exchange dynamical quantum group Fv(G) (which allows us to regard F as a q-deformation of
F 0). Indeed, it is easy to check that as ω → ∞,eω,a (g) degenerates into Fe− 2πia (G). Since we have
−1/τ = πi
(k+h∨ ) log q , and γ/ 2τ = − 1
2(k+h∨ ) , the claim follows.
A Appendix : Meromorphicity of the R-matrix
In this appendix we give a new proof of Theorem 2.1.
Let U be a neighborhood of zero in Cn, and G : U → Cn be an analytic mapping, such that
G(0) = 0. Let p ∈ C, |p|> 1.
Lemma A.1. Let f ∈zCn[[z]] be a formal solution to the diﬀerence equation
f (pz) = G(f (z))
Then f converges to an analytic function in some neighborhood of ze ro.
Proof. Let f (z) = ∑
n≥1fnzn, and G(y) = ∑
n≥1gnyn, where gn are multilinear operators. Since
G is analytic at zero, there exists A >0 such that the norms of the coeﬃcients are estimated by
|gn|<A n for all n.
Let k0 be so big that for k ≥k0 one has |(pk −g1)−1|< 2|p|−k, and 2A< |p|k/ 2. Let C be such
that |fk|<C for k<k 0, and let B >max(1, AC
|p|1/ 2−1 ).
Let us prove by induction in k that |fk|<CB k−1. The statement is clear for k<k 0 (asB >1).
Assume that the statement is known for all n<k , for some k ≥k0, and prove it for k. We have
fk = (pk −g1)−1 ∑
1<r≤k
∑
i1,...,i r:∑ ij =k
gr(fi1,...,f ir )
11
Now, |gr(fi1,...,f ir )| ≤ |gr| ∏ r
l=1 |fil|< (AC)rBk−r, and the number of terms with gr is dominated
by the binomial coeﬃcient
( k − 1
r − 1
)
(as ij ≥ 1, r> 1). Thus, we have
|fk|< 2(AC/B )(1 +AC/B )k−1|p|−kBk <CB k−1,
since 2A< |p|k/ 2 and 1 + AC/B < |p|1/ 2. The inductive step is proved.
This implies that f (z) converges for small z. We are done.
Now we proceed with the proof of Theorem 2.1. Recall the cross ing symmetry condition (equa-
tion (9.19) of [EFK98])
(((RV,W (z)−1)t1 )−1)t1 ) = (q2ρ ⊗ 1)RV,W (zq 2mh∨
)(q−2ρ ⊗ 1) (A.1)
where t1 is transposition in the ﬁrst component and ρ is the half-sum of positive roots of g. It is
valid for any ﬁnite dimensional representations. If |q| ⁄= 1, it can be regarded as an equation of the
type f (pz) = G(f (z)) considered above. Namely, f takes values in the space of endomorphisms
of V ⊗W , p = q±2mh∨
, G(X) = ((( X −1)t1)−1)t1, and the origin in End( V ⊗W ) is at the point
X = RV,W (0), which is a ﬁxed point of G. Thus, by Lemma A.1, the function RV,W (z) is analytic
near zero. Then the meromorphicity in the whole complex plan e follows immediately from the
diﬀerence equation (A.1) and the fact that in our case G is a birational isomorphism. □
Remark: It is clear that the same result and proof applies to V,W being in category O as Uq(g)
modules (since the R-matrix has zero weight, and the weight s paces ofV ⊗W are ﬁnite dimensional).
