---
doc_id: 4geo-dedi-rev
doc_title: "HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not"
section_id: sec-011-16-st-ephane-baseilhac1-riccardo-benedetti-2
section_title: "ST ´EPHANE BASEILHAC1, RICCARDO BENEDETTI 2"
section_number: 16
pages: 17-18
source_pdf: 4GEO-DEDI-REV.pdf
source_sha256: e4d52947b71a3f37
doc_brief: "HAL Id: hal-01812027 HAL is a multi-disciplinary open access archive for the deposit and dissemination of scientific re- search documents, whether they are published or not — 27 sections: ST ´EPHANE B"
---
3.4. Intertwiners of local representations. Let (S,λ ) andq be as before. Any surface R obtained
by splitting S along some (maybe all) edges of λ inherits an orientation from S, and an ideal trian-
gulation µ from λ. By gluing along edges backwards, one says that ( S,λ ) is obtained by fusion from
(R,µ ). In such a case, every local representation ηµ = (η1⊗... ⊗η2m)◦ iµ of Tq
µ determines a local
representationρλ of Tq
λ by setting ρλ = (η1⊗... ⊗η2m)◦ iλ. One says that ηµ representsρλ.
Given local representations η ={ηµ : Tq
µ→ End(Wµ)}µ, ρ ={ρλ : Tq
λ→ End(Vλ)}λ of Tq
R and Tq
S
respectively, one says thatρ is obtained by fusion from η ifηµ representsρλ for all ideal triangulations
µ of R, where λ is the ideal triangulation of S obtained by fusion from µ.
In [11], the following result is proved. The intertwiners Lρρ′
λλ′∈L ρρ′
λλ′ in the statement are called QT
intertwiners.
Theorem 3.9. There exists a collection {(Lρρ′
λλ′,ψρρ′
λλ′)}, indexed by the couples of isomorphic local
representationsρ ={ρλ : Tq
λ→ End(Vλ)}λ, ρ′ ={ρ′
λ : Tq
λ→ End(V′
λ)}λ of Tq
S and by the couples of
ideal triangulations λ, λ′ of S, such that:
(1)Lρρ′
λλ′ is a set of projective classes of linear isomorphisms Lρρ′
λλ′ : Vλ → Vλ′ such that for every
X′∈ Tq
λ′ we have
Lρρ′
λλ′◦ (ρλ◦ϕq
λλ′)(X′)◦ (Lρρ′
λλ′)−1 =ρ′
λ′(X′).
(2) ψρρ′
λλ′ : H1(S; Z/NZ)×Lρρ′
λλ′→L ρρ′
λλ′ is a free transitive action.
(3) Let R be a surface such that S is obtained by fusion from R. Let η ={ηµ : Tq
µ→ End(Wµ)}µ,
η′ ={η′
µ : Tq
µ→ End(W′
µ)}µ be two local representations of Tq
R such that ρ,ρ′ are obtained respectively
by fusion from η, η′. Then, for every ideal triangulations µ, µ′ of R, if λ, λ′ are the corresponding
ideal triangulations of S, there exists an inclusion map j :Lηη′
µµ′→L ρρ′
λλ′ such that for every L∈L ηη′
µµ′
and every c∈H1(R; Z/NZ) the following holds:
(j◦ψηη′
µµ′)(c,L ) =ψρρ′
λλ′(π∗(c),j (L))
whereπ : R→S is the projection map.
(4) For every isomorphic local representations ρ, ρ′, ρ′′ of Tq
S and for every ideal triangulations λ, λ′,
λ′′ of S the composition map
Lρρ′
λλ′×Lρ′ρ′′
λ′λ′′ −→ Lρρ′′
λλ′′
(L1,L 2) ↦−→ L2◦L1
is well-deﬁned, and for all c, d∈H1(S; Z/NZ) it satisﬁes
ψρ′ρ′′
λ′λ′′(d,L 2)◦ψρρ′
λλ′(c,L 1) =ψρρ′′
λλ′′(c +d,L 2◦L1).
It is also proved in [11] that any collection of intertwiners satisfying a weak form of conditions (3)
and (4) (not involving the actions ψρρ′
λλ′) contains the collection{Lρρ′
λλ′}. So the latter is minimal with
respect to these conditions.
Note that property (3) describes the behaviour of the intertwiners in Lρρ′
λλ′ under cut-and-paste
of subsurfaces along edges of λ, λ′. In particular, it implies that they can be decomposed into
elementary intertwiners as follows. Any two ideal triangulations λ, λ′ of S can be connected by
a sequence λ = λ0 → ... → λk+1 = λ′ consisting of k diagonal exchanges followed by an edge
reindexingλk→λk+1 (with same underlying triangulation). Then, any projective class of intertwiners
[Lρρ′
λλ′]∈L ρρ′
λλ′ can be decomposed as
(24) Lρρ′
λλ′ =Lρρ′
λ′λ′◦Lρρ
λkλk+1
◦···◦ Lρρ
λ0λ1
whereLρρ
λiλi+1
∈L ρρ
λiλi+1
intertwinsρλi andρλi+1◦ (ϕq
λiλi+1
)−1, related by the i-th diagonal exchange,
for every i∈{ 0,...,k − 1}, and Lρρ′
λ′λ′ intertwinsρλ′ and ρ′
λ′ on the triangulation λ′. In general the
intertwinerLρρ′
λλ′ depends on the choice of sequence λ =λ0→... →λk+1 =λ′, but the set Lρρ′
λλ′ and
the action ψρρ′
λλ′ do not.
ON THE QUANTUM TEICHM ¨ULLER INVARIANTS OF FIBRED CUSPED 3-MANIFOLDS 17
