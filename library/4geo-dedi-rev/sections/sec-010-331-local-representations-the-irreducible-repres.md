---
doc_id: 4geo-dedi-rev
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-010-331-local-representations-the-irreducible-repres
section_title: "Local representations. The irreducible representations of Tq"
section_number: 3.3.1
pages: 15-17
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "HAL Id: hal-01812027 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: ST ´EPHANE B"
---
S were classiﬁed up to isomorphism
in [7]. The local representations of Tq
S are special reducible representations deﬁned as follows (see
[8, 11]). Deﬁne the triangle algebra T as the algebra over C with generators Y±1
0 , Y±1
1 , Y±1
2 and
relations
(16) Y0Y1 =q2Y1Y0, Y1Y2 =q2Y2Y1, Y2Y0 =q2Y0Y2.
Fix an ordering τ1,...,τ 2m of the triangles of λ. Order the abstract edges ej
0,ej
1,ej
2 of τj so that the
induced cyclic ordering is counter-clockwise with respect to the orientation of S. Associate to τj a
copyTj of the algebraT , with generators denoted by Yj
0 ,Yj
1 ,Yj
2 , so that Yj
i is associated to the edge
ej
i . There is an algebra embedding
(17) iλ : Tq
λ→T 1⊗... ⊗T 2m
deﬁned on generators by (we denote a monomial ⊗jAj in⊗jTj by omitting the terms Aj = 1):
• If ei is an edge of two distinct triangles τli and τri, and eli
ai, eri
bi
are the edges of τli, τri
respectively identiﬁed to ei, then iλ(Xi) :=Yli
ai⊗Yri
bi
.
• If ei is an edge of a single triangle τki, and eki
ai, eki
bi
are the edges of τki identiﬁed to ei, with
eki
ai on the right of eki
bi
, then iλ(Xi) :=q−1Yki
aiYki
bi
=qYki
bi
Yki
ai .
A representation ρλ of Tq
λ is local if
ρλ = (ρ1⊗... ⊗ρ2m)◦ iλ : Tq
λ→ End(V1⊗... ⊗V2m)
for some irreducible representationsρj :T →End(Vj) ofT ,j∈{ 1,..., 2m}. So, a local representation
is an equivalence class of tuples ( ρ1,...,ρ 2m), where two tuples are equivalent if their restrictions to
the subalgebra iλ(Tq
λ) of T1⊗... ⊗T 2m deﬁne the same representation. Two local representations
ρλ = (ρ1⊗... ⊗ρ2m)◦ iλ and ρ′
λ = (ρ′
1⊗... ⊗ρ′
2m)◦ iλ of Tq
λ are isomorphic if there are linear
isomorphisms Lj : Vj→V′
j such that for every j = 1,..., 2m and Y ∈T j we have
Lj◦ρj(Y )◦ (Lj)−1 =ρ′
j(Y ).
It is straightforward to check that this deﬁnition is independent of the choice of tuples ( ρ1,...,ρ 2m),
(ρ′
1,...,ρ ′
2m). By deﬁnition a local representation ρ of Tq
S is a representation formed by local repre-
sentationsρλ.
3.3.2. Isomorphism classes and standard local representations. The isomorphism classes of irreducible
representations of the triangle algebraT are parametrized by tuples of non zero scalars (y0,y 1,y 2,h )∈
(C•)4 such that hN =y0y1y2. The parameter h is called the load of the class. The isomorphism class
with parameters ( y0,y 1,y 2,h ) can be represented by standard representations ρ :T → End(CN),
which have the form
(18) ρ(Yi) = yiAi, i∈{ 0, 1, 2}
where y0, y1, y2∈ C∗ satisfy
yN
i =yi, i∈{ 0, 1, 2}, h= y0y1y2
and A0,A 1,A 2 are the endomorphisms of CN deﬁned in (10).
ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS 15
Any local representation of Tq
λ has dimensionN2m. The isomorphism class of a local representation
ρλ of Tq
λ is determined by:
• a non zero complex weight xi associated to each edge of λ;
• a N-th root h of x1...x n, called the load.
The weights xi and the load h are such that
(19) ρλ(XN
i ) =xiIdV1⊗...⊗V2m, ρλ(H) =hIdV1⊗...⊗V2m
where H is a central element of Tq
λ, called the principal central element , given by
(20) H =q− ∑
l<l′σll′X1...X n.
Note that hN = x1...x n. It is straightforward to check that two local representations are iso-
morphic if and only if they are isomorphic as local representations. We call ( {x1,...,x n},h ) the
parameters ofρλ. We say that a local representation ρλ = (ρ1⊗... ⊗ρ2m)◦ iλ is standard if every ρi
is. This notion naturally extends to representations of Tq
S. Every point of ( C∗)n can be realized as the
n-tuple of parameters xi,i = 1,...,n , of a standard local representation of Tq
λ. There is a one-to-one
correspondence between isomorphism classes of local representations{ρλ : Tq
λ→ End(V1⊗...⊗V2m)}λ
of Tq
S and families of parameters {({x1,...,x n}λ,hλ)}λ such that
(21) hλ =hλ′ and xi =ϕ1
λλ′(x′
i)
for every i = 1,...,n and any two ideal triangulations λ, λ′ of S with edge weights {x1,...,x n},
{x′
1,...,x ′
n} and loads hλ, hλ′ respectively. The edge weights xi of a local representation ρλ : Tq
λ→
End(Vλ) deﬁne its “classical shadow”
sh(ρλ) : T1
λ→ End(C)
by taking the restriction of ρλ to the subalgebra C[X±N
1 ,...,X ±N
n ]∼= T1
λ of the center of Tq
λ. This
notion extends immediately to local representations ρ ={ρλ : Tq
λ→ End(Vλ)}λ of Tq
S; the classical
shadow
sh(ρ) ={sh(ρλ) : T1
λ→ End(C)}λ
is a representation of the coordinate ringT1
S of the Teichm¨ uller space (considered as a rational manifold
with transition functions the maps ϕ1
λλ′). Every representation of T1
S is the shadow of N local
representations of Tq
S. The shadows of local representations encode the Zariski open subset of X(S)
made of the so-called peripherically generic characters. These include all the augmented characters of
injective representations.
The load h has the following geometric interpretation. Let [( r,{ξΓ}Γ∈Π)] be the augmented char-
acter of S determined by sh(ρ). Each Γ ∈ Π is a group generated by the class in π1(S) of a small
loop mj in S going once and counter-clockwise around the j-th puncture, for some j∈{ 1,...,r }
and some choice of basepoints. Since π1(S) is a free group, r: π1(S)→PSL (2, C) can be lifted to a
homomorphism ˆr: π1(S)→ SL(2, C); the ﬁxed point ξΓ∈ P1 is then contained in an eigenspace of
ˆr(mj), corresponding to an eigenvalue aj∈ C. Then
(22) hN = (−1)ra−1
1 ...a −1
r .
Finally, the decomposition into irreducible summands of a local representation ρλ of Tq
λ is ([13])
(23) ρλ =⊕ρλ(µ)⊂ρλ ρλ(µ)
where the sum ranges over the set of all spaces ρλ(µ) formed by intersecting one eigenspace for each
of the so-called (central) puncture elements of Tq
λ. Each space ρλ(µ) is also the isotypical component
of an irreducible representation µ of Tq
λ, that is, the direct sum of all irreducible summands of ρλ
isomorphic toµ. Every irreducible representation of Tq
λ has an isotypical summand appearing in some
local representation, and has multiplicity Ng in it.
