---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-020-on-the-quantum-teichm-uller-invariants-of-fibred
section_title: "ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS (page 22)"
section_number: null
pages: 22-22
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
toc_source: inferred
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 26 sections: Front matter; ON THE QUANTUM TEICHM ¨ULLER INVAR; ON THE QUANTUM TEICHM ¨ULLER INVAR"
---
ON THE QUANTUM TEICHM¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS
21
according to the cases (a) or (b) described at the beginning of Step 3. A simple dimensional count
shows that π0 is surjective, with generic ﬁbre isomorphic to (C∗)3m. Then, take a point y0 ∈π−1
0 (x0).
We get
(31)
ρ0(Xs) = x0(es)Ali
ai ⊗Ari
bi
or
ρ0(Xs) = q−1x0(es)Aki
aiAki
bi
again according to the cases (a) or (b) above. We have to check that the sequence of local representa-
tions ρj constructed by starting from ρ0 is consistent, that is, compatible with w under the diagonal
exchanges. Using the notations of Figure 3, by the tetrahedral and edge relations satisﬁed by the
quantum shape parameters, for all j ∈{0, . . . , k} we have
(32)
xj(e5) = −q−1w2, xj+1(e5) = −qw−1
2
and
(33)
xj+1(e1) = xj(e1)w−1
0
,
xj+1(e2) = xj(e2)w−1
1
xj+1(e3) = xj(e3)w−1
0
,
xj+1(e4) = xj(e4)w−1
1 .
In particular, (32) for j = 0 is consistent with the relation w2 = −qy3
1y1
0 required by Proposition
4.1 (where y3
1 = y0
ri,bi and y1
0 = y0
li,ai).
Then, comparing (33) and (26) we see that for every
j ∈{0, . . . , k}, ρj is indeed deﬁned by identities like (31), with x0 replaced by xj.
By (29), the representations ρ0, . . . , ρk belong to a local representation ρ = {ρλ : Tq
λ →End(Vλ)}λ
of Tq
S. By (19), (31) and the similar identities for ρj, we see that the parameters of ρj are
({xj(e)}e∈λ(1)
j , h)
where xj(e) = (xj(e))N and
(34)
h =
Y
e∈λ(1)
j
xj(e).
For this identity, ﬁrst note that the right hand side, say hj, does not depend on j. Indeed, by (32),
(33) and the tetrahedral and edge relations for w0, w1 and w2, we see that
Q5
i=1 xj(ei) = Q5
i=1 xj+1(ei)
under a diagonal exchange. Since the quantum shear-bend coordinates of edges not touched by a
diagonal exchange are not altered, we deduce that hj = hj+1 for every j = 0, . . . , k −1. Now we
can check (34) as follows. Consider a triangle τ j
s of λj, with edges Xi, Xj, Xk, where i < j < k.
The weak branching ˜b provides a bijection p: {i, j, k} 7→{0, 1, 2}. Then iλj(H) is a tensor product of
monomials associated to the triangles of λj, and the monomial for τ j
s is q
−σ|τj
s Y s
p(i)Y s
p(j)Y s
p(k) where
−σ|τ j
s is the contribution to the summand −σij −σik −σjk of −P
l<l′ σll′ coming from the triangle
τ j
s . Noting that the product Y s
0 Y s
1 Y s
2 is invariant under cyclic permutations, one checks immediately
that q
−σ|τl
j Y s
p(i)Y s
p(j)Y s
p(k) = q−1Y s
0 Y s
1 Y s
2 . So
iλj(H) = ⊗2m
s=1(q−1Y s
0 Y s
1 Y s
2 )
and hence
ρj(H) = ⊗2m
s=1(ys
0ys
1ys
2q−1As
0As
1As
2) = xj(e1) . . . xj(en)Id(CN)⊗2m.
Summarizing our discussion, we have proved the following result. It concludes the proof of Step 3
of our First Main Theorem, and hence of Theorem 1.1 in the introduction.
Proposition 4.5. The QH triangulation (TCφ,˜b, w) determines a sequence of standard local repre-
sentations ρj : Tq
λj →End((CN)⊗2m) associated to the triangulated surfaces (S, λj), with parameters
({xj(e)}e∈λ(1)
j , h), h = Q
e∈λ(1)
j
xj(e),
and belonging to a local representation ρ of Tq
S. Moreover, Hred
N (TCφ,˜b, w)T intertwins the represen-
tations ρ0 and ρk.
