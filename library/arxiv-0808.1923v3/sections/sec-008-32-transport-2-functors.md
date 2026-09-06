---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-008-32-transport-2-functors
section_title: "Transport 2-Functors"
section_number: 3.2
pages: 15-18
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
Now we come to the central deﬁnition of this paper.
Deﬁnition 3.2.1. LetM be a smooth manifold, Gr be a strict Lie 2-groupoid, T be a 2-category and
i : Gr /d47/d47 T be a 2-functor. A transport 2-functor on M with values in T and with Gr-structure is a
2-functor
tra : P2(M ) /d47/d47 T
such that there exists a surjective submersion π :Y /d47/d47 M and a π-locali-trivialization (triv,t ) whose
descent object Exπ(tra, triv,t ) is smooth.
A 1-morphism between transport 2-functors tra and tra ′ is a pseudonatural transformation
A : tra /d47/d47 tra′ such that there exists a surjective submersion π together with π-local i-trivializations
of tra and tra ′ for which the descent 1-morphism Ex π(A) is smooth. 2-morphisms are deﬁned in the
– 15 –
same way. Transport 2-functors tra : P2(M ) /d47/d47 T with Gr-structure, 1-morphisms, and 2-morphisms
form a sub-2-category of the 2-category of locally i-trivializable 2-functor Funct i(P2(M ),T ), and we
denote this sub-2-category by Trans 2
Gr(M,T ). We emphasize that being a transport 2-functor is a
property, not additional structure. In particular, no surjectiv e submersion or open cover is contained
in the structure of a transport 2-functor: they are manifestly globally deﬁned objects.
We want to establish an equivalence between transport 2-functor s and their smooth descent data.
In order to achieve this equivalence we have to make a slight assumpt ion on the 2-functor i. We call a
2-functori : Gr /d47/d47 T full and faithful , if it induces an equivalence on Hom-categories. In particular,
i is full and faithful if it is an equivalence of 2-categories, which is in fac t true in all examples we are
going to discuss.
Theorem 3.2.2. LetM be a smooth manifold, and let i : Gr /d47/d47 T be a full and faithful 2-functor.
Then, the equivalence of Theorem 2.2.3 restricts to an equiv alence
Trans2
Gr(M,T ) ∼= Des2(i)∞
M
between transport 2-functors and their smooth descent data .
Theorem 3.2.2 is proved by the following two lemmata. As an intermediat e step we introduce –
for a surjective submersion π – the sub-2-category Triv 2
π(i)∞ of Triv2
π(i) as the preimage of Des2
π(i)∞
under the 2-functor Ex π.
Lemma 3.2.3. The 2-functor Exπ restricts to an equivalence of 2-categories
Triv2
π(i)∞ ∼= Des2
π(i)∞.
Proof. It is clear that Ex π restricts properly. Recall from [SW, Section 3] that inverse to Ex π is
a “reconstruction” 2-functor Rec π. In order to prove that the image of the restriction of Rec π is
contained in Triv 2
π(i)∞ we have to check that Ex π ◦ Recπ restricts to an endo-2-functor of Des2
π(i)∞.
In the proof of [SW, Lemma 4.1.2] we have explicitly computed this 2-fu nctor, and by inspection of
the corresponding expressions one recognizes its image as smooth descent data.
The second part of the proof is to show that the components of tw o pseudonatural equivalences
ρ : Exπ ◦ Recπ /d47/d47 id and η : id /d47/d47 Recπ ◦ Exπ that establish the equivalence of [SW, Proposition
4.1.1] are in Des2
π(i)∞ and Triv2
π(i)∞, respectively. For the transformation ρ, this is again by inspection
of the formulae in the proof of [SW, Lemma 4.1.2]. For the transforma tion η, we suppose F is a 2-
functor with a π-local i-trivialization (t, triv) with smooth descent data (triv ,g,ψ,f ). We have to
prove that the descent 1-morphism Ex π(η(F,t, triv)) is smooth. Indeed, according to the deﬁnition of
η given in the proof of [SW, Lemma 4.1.3] it is given by the pseudonatural transformation g and a
modiﬁcation composed from the modiﬁcations f andψ. The descent object is by assumption smooth,
and so is η(F ). The same argument shows that the component η(A) of a pseudonatural transformation
A :F /d47/d47 F ′ with smooth descent data is smooth. □
Next we go to the direct limit
Triv2(i)∞
M := lim− →π
Triv2
π(i)∞.
The equivalence of Lemma 3.2.3 induces an equivalence
Ex : Triv 2(i)∞
M /d47/d47 Des2
π(i)∞
– 16 –
in the direct limit. Next we show that the 2-categories Triv 2(i)∞
M and Trans 2
Gr(M,T ) are equivalent.
We have an evident 2-functor
v∞ : Triv2(i)∞
M /d47/d47 Trans2
Gr(X,T )
induced by forgetting the chosen trivialization.
Lemma 3.2.4. Under the assumption that the 2-functor i is full and faithful, the 2-functor v∞ is an
equivalence of 2-categories.
Proof. It is clear that an inverse functor w∞ takes a given transport 2-functor and picks some
smooth local trivialization for some surjective submersion π :Y /d47/d47 M . It follows immediately that
v∞ ◦w∞ = id. It remains to construct a pseudonatural equivalence id ∼=w∞ ◦v∞, i.e. a 1-isomorphism
A : (tra,π, triv,t ) /d47/d47 (tra,π ′, triv′,t ′)
in Triv 2(i)∞
M , where the original π-local trivialization (triv ,t ) has been forgotten and replaced by a
new π′-local trivialization (triv ′,t ′). But since the 1-morphisms in Triv 2(i)∞
M are just pseudonatural
transformation between the 2-functors ignoring the trivialization s, we only have to prove that the
identity pseudonatural transformation
A := id tra : tra /d47/d47 tra
of a transport 2-functor tra has smooth descent data ( h,ǫ ) with respect to any two trivializations
(π, triv,t ) and (π′, triv′,t ′).
The ﬁrst step is to choose a reﬁnement ζ : Z /d47/d47 Y ×M Y ′ of the common reﬁnement of the
to surjective submersions. One can choose Z such that is has contractible connected components. If
c :Z ×[0, 1] /d47/d47 Z is such a contraction, it deﬁnes for each point z ∈Z a pathcz :z /d47/d47 zk that moves
z to the distinguished point zk to which the component of Z that contains z is contracted. It further
deﬁnes for each path γ : z1 /d47/d47 z2 a bigon cγ : γ /d43/d51 c−1
z2 ◦cz1. Axiom (T2) for the pseudonatural
transformation
h :=t′ ◦ ¯t : trivi /d47/d47 triv′
i
applied to the bigon cγ yields the commutative diagram
h(z2) ◦ trivi(γ)
h(γ) /d43/d51
id◦trivi(cγ )
/d11/d19
triv′
i(γ) ◦h(z1)
triv′
i(cγ )◦id
/d11/d19
h(z2) ◦ trivi(c−1
z2 ◦cz1)
h(c−1
z2 ◦cz1 )
/d43/d51 triv′
i(c−1
z2 ◦cz1) ◦h(z1).
Notice that the 1-morphisms h(zj) : triv i(zj) /d47/d47 triv′
i(zj) have by assumption preimages κj :
triv(zj) /d47/d47 triv′(zj) under i in Gr, and that the 2-morphism h(c−1
z2 ◦cz1) also has a preimage Γ
in Gr. Thus,
h(γ) = i
(
(triv′(cγ) ◦ id)−1 • Γ • (id ◦ triv(cγ))
)
.
This is nothing but the Wilson line W F (h),Λi
z1,z2 of the functor F (h) and it is smooth since triv and
triv′ are smooth 2-functors. Hence, by Theorem 3.12 in [SW09], F (h) is a transport functor with
ΛGr-structure.
– 17 –
It remains to prove that the modiﬁcation ǫ : π∗
2h ◦g /d43/d51 g′ ◦π∗
1h induces a morphism F (ǫ) of
transport functors. This simply follows from the general fact tha t under the assumption that the
functor i : Gr /d47/d47 T is full, every natural transformation η between transport functors with Gr-
structure is a morphism of transport functors. We have not stat ed that explicitly in [SW09] but it
can easily be deduced from the naturality conditions on trivializations t andt′ and on η, evaluated for
paths with a ﬁxed starting point. □
With Theorem 3.2.2 we have established an equivalence between globally deﬁned transport 2-
functors and locally deﬁned smooth descent data. In Section 4 we w ill identify smooth descent data
with various models of gerbes with connections. Under this identiﬁca tions, Theorem 3.2.2 describes
the relation between these gerbes with connections and their para llel transport.
