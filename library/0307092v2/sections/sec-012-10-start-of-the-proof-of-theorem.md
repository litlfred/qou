---
doc_id: 0307092v2
doc_title: "Extended Bloch group and the Cheeger–Chern–Simons class"
section_id: sec-012-10-start-of-the-proof-of-theorem
section_title: "Start of the proof of Theorem ??"
section_number: 10
pages: 36-41
source_pdf: 0307092v2.pdf
source_sha256: de2f7ddec49b2ce6
toc_source: outline
doc_brief: "Extended Bloch group and the Cheeger–Chern–Simons class — We deﬁne an extended Bloch group and show it is naturally isomorphic to H3(PSL(2, C)δ; Z)."
---
Lemma 10.1 The choice of strong ﬂattening of K does not aﬀect the resulting
element P
i ǫi[xi; pi, qi] ∈bP(C).
Proof If we have a diﬀerent choice of ﬂattenings wi satisfying the parity
and log-parameter conditions for a strong ﬂattening of K then Lemma 9.3
implies that the diﬀerence between the corresponding elements δ represents 0
in H3(J ). It is thus in the image of β. For E ∈C2 the eﬀect of changing δ
by β(E) is to change the element P
i ǫi[xi; pi, qi] ∈bP(C) by the cycle relation
about E of Lemma 6.1.
Since this is a consequence of the lifted ﬁve term
relations, the element in bP(C) is unchanged.
Ultimately we will want to see that P
i ǫi[xi; pi, qi] is independent of ﬂattening
rather than strong ﬂattening. This will follow in Section 11. The following
lemma only needs ﬂattening and not strong ﬂattening.
Lemma 10.2 Given a ﬂattening of K, the element P
i ǫi[xi; pi, qi] ∈bP(C) lies
in bB(C).
Proof For any Q–vector-space V , the skew-symmetric bilinear form ⟨⟩on J
induces a symmetric bilinear map
B : (J ⊗V ) ⊗(J ⊗V ) →V ∧V ,
(a ⊗v) ⊗(b ⊗w) 7→⟨a, b⟩v ∧w .
Theorem 4.1 of [13] says that after tensoring with Q, the bilinear form ⟨, ⟩
on Ker(β∗: J ⊗Q →C1 ⊗Q) induces two times the intersection form on
H1(∂K0; Q) = Ker β∗/ Im β. Hence, on (Ker β∗/ Im β) ⊗V = H1(∂K0) ⊗V =
H1(∂K0; V ), the above bilinear map B induces the map
B′ : (H1(∂K0) ⊗V ) ⊗(H1(∂K0) ⊗V ) →V ∧V
given by
([a] ⊗v) ⊗([b] ⊗w) 7→2([a] · [b]) v ∧w
where [a] · [b] is intersection form.
We take V = C. For our element w′ = w −πiδ ∈J ⊗C we have
B(w′, w′) = 2
X
i ǫi(log xi + piπi) ∧(−log(1 −xi) + qiπi) ∈C ∧C .
Thus, we want to show that B(w′, w′) = 0. If we have a strong ﬂattening,
w′ is in Ker(β∗) ⊗C and represents zero in H1(∂K0; C). Thus B(w′, w′) =
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
449
B′([w′], [w′]) = B′(0, 0) = 0, as desired. If the ﬂattening is not strong, then
rather than w′ representing zero in H1(∂K0; C), it represents πi times an
integral homology class α say, and we still have B(w′, w′) = B′([w′], [w′]) =
(α · α)πi ∧πi = 0.
At this point we have shown that the element P
i ǫi[xi; pi, qi] determined by
a strong ﬂattening of K lies in bB(C) and is independent of choice of strong
ﬂattening. In the remainder of this section we show that it depends only on
|K| and the ﬂat G–bundle over it.
Lemma 10.3 Changing the choice of the point z ∈∂H
3 in the deﬁnition of
strong ﬂattening (Deﬁnition 4.4) does not change the element P
i ǫi[xi; pi, qi] ∈
bB(C).
Proof This is a special case of the following lemma, since if we change the
1–cocycle corresponding to a G–labeling by the coboundary of the constant 0–
cochain with value g, the eﬀect is the same as replacing z by gz (see subsection
4.1.2).
Lemma 10.4 If we change the G–labeling of K by changing the corresponding
1–cocycle by a coboundary (subsection 4.1.2) then the element P
i ǫi[xi; pi, qi] ∈
bB(C) does not change.
Proof The corresponding result is known for the element in B(C), so the
change is in Ker( bB(C) →B(C)) = Q/Z. Thus, if we knew that the cobound-
ary action of 0–cochains was continuous using the standard topology of G =
PSL(2, C) the Lemma would follow. This continuity seems “self-evident” but
we do not know an easier proof than what follows, which directly proves the
local constancy of the element of bB(C) under this action.
It suﬃces to prove the lemma for the change given by the coboundary action
of a 0–cochain τ that takes the value 1 on all 0–simplices except one. Denote
that one 0–simplex by v. The eﬀect is that the ideal simplex corresponding
to a simplex ∆of K is unchanged if v is not one of its vertices, while if it
has vertices v, v1, v2, v3 with G–labels g, g1, g2, g3 before the change, then the
corresponding ideal simplex has vertices gz, g1z, g2z, g3z before the change and
gτ(v)z, g1z, g2z, g3z after. We assume τ(v) is suﬃciently close to 1 that none
of these latter simplices are degenerate (two vertices equal).
Since the ﬂattening condition on K is a discrete condition (it can only fail
by multiples of πi), it will stay valid if we vary strong ﬂattenings of simplices
Geometry & Topology, Volume 8 (2004)
450
Walter D Neumann
continuously as τ(v) ∈G varies (considering G = PSL(2, C) with its usual
topology, rather than as a discrete group). Thus we get a continuous family of
strong ﬂattenings of K as τ(v) varies in a neighborhood of 1 ∈G. We must
show that any two of them lead to equal elements of bB(C), ie, they can be
related using lifted ﬁve-term relations. Since only simplices in the star N of v
are aﬀected, it suﬃces to show that
X
∆i⊂N
ǫi([xi; pi, qi] −[x′
i; p′
i, q′
i]) = 0 ∈bP(C),
(13)
where ℓ([xi; pi, qi]) and ℓ([x′
i; p′
i, q′
i]) are the ﬂattenings of ∆i before and after
changing the G–label of v by τ(v).
Denote the 0–simplices in the simplicial link of v by v1, . . . , vm, and let their
G–labels be g1, . . . , gm. For each ordered 2–simplex ⟨vi, vj, vk⟩in the simplicial
link of v we wish to give a lifted ﬁve-term relation based on the ﬁve points gz,
gτ(v)z, giz, gjz, gkz so that when we sum these relations (with appropriate
signs) we get the left side of equation (13).
We already have ﬂattenings of the two simplices
⟨gz, g1z, g2z, g3z⟩
and
⟨gτ(v)z, g1z, g2z, g3z⟩.
We wish to ﬁnd ﬂattenings of the other three simplices
⟨gz, gτ(v)z, gjz, gkz⟩,
⟨gz, gτ(v)z, giz, gkz⟩,
⟨gz, gτ(v)z, giz, gjz⟩
so that we have an instance of the ﬁve-term relation.
Consider the appropriate signed sum of the three adjusted angles about the
1–simplex ⟨gjz, gkz⟩in the the ﬂattening condition of the ﬁve-term relation.
This sum is a multiple of π which should be zero. The two adjusted angles
at this edge in ⟨gz, giz, gjz, gkz⟩and ⟨gτ(v)z, giz, gjz, gkz⟩almost cancel in the
sum. Since we may assume τ(v) is close to 1, the angle at the edge ⟨gjz, gkz⟩
in the simplex ⟨gz, gτ(v)z, gjz, gkz⟩will be small. Thus the adjustment to this
angle must be zero. Similarly for the ⟨giz, gkz⟩edge of ⟨z, τ(v)z, giz, gkz⟩and
the ⟨giz, gjz⟩edge of ⟨z, τ(v)z, giz, gjz⟩. In each of these three simplices the
adjusted angle ⟨z, τ(v)z⟩equals the adjusted angle at the opposite edge and
is hence small, so the sum of these adjusted angles must be 0 (since it is a
multiple of π) so the ﬂattening condition holds also at the edge ⟨z, τ(v)z⟩.
It remains to choose the angle adjustments at edges of the form ⟨τ(v)z, giz⟩of
these simplices. We use the description of ﬂattenings in terms of rotation levels
on edges described at the end of section 5. So we position the developing map
restricted to N so that vertex v goes to gz = ∞. Then gτ(v)z is close to ∞, ie,
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
451
very far from the points gνz for ν = 1, . . . , m. Thus the segments joining gτ(v)z
to the points gνz will be almost mutually parallel, so we can choose the rotation
levels of these segments to be almost equal to each other. With such a choice it is
clear by inspection that the remaining ﬂattening conditions for the desired ﬁve-
term relations hold. When we sum these ﬁve-term relations with appropriate
signs, each ﬂattened simplex with vertices of the form gz = ∞, gτ(v)z, giz, gjz
occurs in two of the relations and cancels and we are left with the desired
relation (13).
This proves the existence of the desired lifted ﬁve-term relations when τ(v) is
close to 1. This shows that the element of bB(C) is locally constant under the
coboundary action of 0–cochains, and since the space GK(0) of 0–cochains is
connected, the Lemma follows.
Remark 10.5 The above lemma can be interpreted to say that, instead of
choosing a single z ∈∂H3 in Deﬁnition 4.4 to obtain the ideal simplex shapes
for the simplices of K, we can choose a diﬀerent z for each 0–simplex of K,
and the element of bB(C) is unaﬀected. This will be important when discussing
the applications to 3–manifolds in Section 14.
We have been assuming that K is a simplicial rather than quasi-simplicial
complex, but so far we have not really used this. We will initially prove Theorem
4.6 under the following assumption, which we will eliminate again in Proposition
11.2.
Assumption
K is a simplicial complex and the vertex orderings of the sim-
plices of K are inherited from an ordering of the set of 0–simplices of K.
Lemma 10.6 Changing the ordering of the 0–simplices of K does not change
the element P
i ǫi[xi; pi, qi] ∈bB(C).
Proof The full permutation group on K(0) is generated by transpositions on
adjacent elements with respect to the ordering, so we need only consider such
transpositions. If the two 0–simplices are not joined by a 1–simplex then the
the transposition has no eﬀect on the vertex-ordering of any 3–simplex so there
is nothing to prove. Assume therefore that v and w are two 0–simplices that
are adjacent in the ordering of K(0) and are joined by a 1–simplex. Only the 3–
simplices that have ⟨v, w⟩as an edge have their vertex-ordering changed by the
transposition, so we just consider these simplices. The conﬁguration of these
simplices is as in Lemma 6.1 and the same inductive argument used in the proof
Geometry & Topology, Volume 8 (2004)
452
Walter D Neumann
of that lemma lets us deduce the lemma from the case that there are just three
3–simplices about this 1–simplex and their vertex orderings are induced from
an ordering of the ﬁve 0–simplices involved. In the proof of Lemma 6.1 it is
shown that there is then a lifted ﬁve-term relation which replaces these three
simplices by two. After doing so, v and w no longer joined by an edge, so the
transposition no longer has an eﬀect on the vertex-order of any three-simplex,
so the lemma follows.
Finally for this section, we show that we can change the triangulation of K by
Pachner moves without changing the element of bB(C). These are the moves
(1 →4, 2 →3, 3 →2 and 4 →1 on numbers of simplices) that replace
a union of 3–simplices of K that is combinatorially equivalent to part of the
boundary of a 4–simplex by the union of the complementary set of 3–simplices
in the boundary of the 4–simplex. Only the 1 →4 Pachner move adds a new
0–simplex. In this case, we insert the new 0–simplex anywhere in the ordering
of 0–simplices and, if the old simplex had G–labels (g0, g1, g2, g3), we give
the four new simplices G–labels (g1, g2, g3, g), (g0, g2, g3, g), (g0, g1, g3, g), and
(g0, g1, g2, g), for some g̸ = g0, g1, g2, g3. We are again using the assumption of
a global ordering of the 0–simplices of K: if we only had local vertex-orderings
of simplices, we could not guarantee that the two 3–simplices produced by a
3 →2 Pachner move have vertex-orderings compatible with adjacent simplices.
Lemma 10.7 A change of triangulation of K by Pachner moves does not
change the represented element P
i ǫi[xi; pi, qi] ∈bB(C).
Proof We want to leave unchanged the ﬂattenings on the unaltered simplices
of K and put ﬂattenings on the new simplices to get a ﬂattening of the new
complex K′.
We can do this if and only if the ﬂattenings of the changed
simplices (the ones in K that have been replaced and the ones they have been
replaced by) give a ﬂattening of the boundary of the 4–simplex (in the sense
that log and parity parameters around edges are zero). In particular, the change
in the element of bB(C) is then an instance of the lifted ﬁve-term relation, and
hence zero. We thus need to know that any ﬂattening deﬁned on part of the
boundary of a 4–simplex can be extended over the whole 4–simplex. This is
the content of Lemma 3.5.
It follows from Pachner [19] that any two simplicial triangulations of |K| are
related by Pachner moves, so at this point we know that the element of bB(C)
is determined just by |K| and the ﬂat G–bundle over it. We will actually only
Geometry & Topology, Volume 8 (2004)
Extended Bloch group and the Cheeger–Chern–Simons class
453
need this in the case that |K| is a manifold, which is explicit in Pachner’s work.
In the next section we reduce to the case that |K| is a manifold and use this
to complete the proof of Theorem 4.6.
11
