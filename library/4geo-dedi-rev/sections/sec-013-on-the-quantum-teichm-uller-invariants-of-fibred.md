---
doc_id: 4geo-dedi-rev
doc_title: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds"
section_id: sec-013-on-the-quantum-teichm-uller-invariants-of-fibred
section_title: "ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS (page 15)"
section_number: null
pages: 15-15
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
toc_source: inferred
doc_brief: "On the quantum Teichmüller invariants of fibred cusped 3-manifolds — 26 sections: Front matter; ON THE QUANTUM TEICHM ¨ULLER INVAR; ON THE QUANTUM TEICHM ¨ULLER INVAR"
---
14
ST´EPHANE BASEILHAC1, RICCARDO BENEDETTI2
written as PiQ−1
i
∈ˆTq
λ, where Pi, Qi ∈Tq
λ and ρλ(Pi), ρλ(Qi) are invertible endomorphisms of Vλ.
In such a case, ρλ ◦ϕq
λλ′(X′
i) = ρλ(Pi)ρλ(Qi)−1 is well-deﬁned (ie. independent of the choice of the
pair (Pi, Qi)).
By deﬁnition, the quantum Teichm¨uller space of S is the quotient set Tq
S := (`
λ ˆTq
λ)/ ∼, where ∼
identiﬁes the algebras ˆTq
λ and ˆTq
λ′ by ϕq
λλ′, for all ideal triangulations λ, λ′ of S. A representation of
Tq
S is a family of representations
ρ := {ρλ : Tq
λ →End(Vλ)}λ
indexed by the set of ideal triangulations of S, such that ρλ ◦ϕq
λλ′ makes sense for every λ, λ′ and is
isomorphic to ρλ′. In fact, it is enough to check the isomorphisms ρλ′ ∼= ρλ ◦ϕq
λλ′ whenever λ and λ′
diﬀer by a ﬂip.
3.3.1. Local representations. The irreducible representations of Tq
S were classiﬁed up to isomorphism
in [7]. The local representations of Tq
S are special reducible representations deﬁned as follows (see
[8, 11]). Deﬁne the triangle algebra T as the algebra over C with generators Y ±1
0
, Y ±1
1
, Y ±1
2
and
relations
(16)
Y0Y1 = q2Y1Y0, Y1Y2 = q2Y2Y1, Y2Y0 = q2Y0Y2.
Fix an ordering τ1, . . . , τ2m of the triangles of λ. Order the abstract edges ej
0, ej
1, ej
2 of τj so that the
induced cyclic ordering is counter-clockwise with respect to the orientation of S. Associate to τj a
copy Tj of the algebra T , with generators denoted by Y j
0 ,Y j
1 ,Y j
2 , so that Y j
i is associated to the edge
ej
i. There is an algebra embedding
(17)
iλ : Tq
λ →T1 ⊗. . . ⊗T2m
deﬁned on generators by (we denote a monomial ⊗jAj in ⊗jTj by omitting the terms Aj = 1):
• If ei is an edge of two distinct triangles τli and τri, and eli
ai, eri
bi are the edges of τli, τri
respectively identiﬁed to ei, then iλ(Xi) := Y li
ai ⊗Y ri
bi .
• If ei is an edge of a single triangle τki, and eki
ai, eki
bi are the edges of τki identiﬁed to ei, with
eki
ai on the right of eki
bi , then iλ(Xi) := q−1Y ki
ai Y ki
bi = qY ki
bi Y ki
ai .
A representation ρλ of Tq
λ is local if
ρλ = (ρ1 ⊗. . . ⊗ρ2m) ◦iλ : Tq
λ →End(V1 ⊗. . . ⊗V2m)
for some irreducible representations ρj : T →End(Vj) of T , j ∈{1, . . . , 2m}. So, a local representation
is an equivalence class of tuples (ρ1, . . . , ρ2m), where two tuples are equivalent if their restrictions to
the subalgebra iλ(Tq
λ) of T1 ⊗. . . ⊗T2m deﬁne the same representation. Two local representations
ρλ = (ρ1 ⊗. . . ⊗ρ2m) ◦iλ and ρ′
λ = (ρ′
1 ⊗. . . ⊗ρ′
2m) ◦iλ of Tq
λ are isomorphic if there are linear
isomorphisms Lj : Vj →V ′
j such that for every j = 1, . . . , 2m and Y ∈Tj we have
Lj ◦ρj(Y ) ◦(Lj)−1 = ρ′
j(Y ).
It is straightforward to check that this deﬁnition is independent of the choice of tuples (ρ1, . . . , ρ2m),
(ρ′
1, . . . , ρ′
2m). By deﬁnition a local representation ρ of Tq
S is a representation formed by local repre-
sentations ρλ.
3.3.2. Isomorphism classes and standard local representations. The isomorphism classes of irreducible
representations of the triangle algebra T are parametrized by tuples of non zero scalars (y0, y1, y2, h) ∈
(C•)4 such that hN = y0y1y2. The parameter h is called the load of the class. The isomorphism class
with parameters (y0, y1, y2, h) can be represented by standard representations ρ : T →End(CN),
which have the form
(18)
ρ(Yi) = yiAi, i ∈{0, 1, 2}
where y0, y1, y2 ∈C∗satisfy
yN
i = yi, i ∈{0, 1, 2}, h = y0y1y2
and A0, A1, A2 are the endomorphisms of CN deﬁned in (10).
