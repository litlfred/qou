---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-003-22-local-trivializations-and-descent-data
section_title: "Local Trivializations and Descent Data"
section_number: 2.2
pages: 7-10
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
Let T be a 2-category. A key feature of a transport 2-functor is that it is locally trivializable. Local
trivializations of a 2-functor F : P2(M ) /d47/d47 T are deﬁned with respect to three attributes:
1. A strict 2-groupoid Gr, the structure 2-groupoid . In Section 2.3 we will require that Gr is a Lie
2-groupoid, and formulate smoothness conditions with respect to its smooth structure.
2. A 2-functor i : Gr /d47/d47 T that indicates how the structure 2-groupoid is realized in the targe t
2-category.
3. A surjective submersion π :Y /d47/d47 M , which serves as an “open cover” of the base manifold M .
For a surjective submersion π :Y /d47/d47 M the ﬁbre products Y [k] := Y ×M... ×MY are again smooth
manifolds in such a way that the projections πi1...ip :Y [k] /d47/d47 Y [p] (to the indexed factors) are smooth
maps. An example is an open cover U = {Uα} of M , for which the disjoint union of all open sets Uα
together with the projection to M is a surjective submersion. In this example, the k-fold ﬁbre product
is the disjoint union of the k-fold intersections of the open sets Uα.
Deﬁnition 2.2.1. A π-locali-trivialization of a 2-functor F : P2(M ) /d47/d47 T is a pair (triv,t ) of a
strict 2-functor
triv : P2(Y ) /d47/d47 Gr
– 7 –
and a pseudonatural equivalence
P2(Y )
π∗ /d47/d47
triv
/d15/d15
P2(M )
t ✈✈✈✈✈✈
✈✈✈✈✈✈
/d118/d126 ✈✈✈✈✈✈
✈✈✈✈✈✈ F
/d15/d15
Gr i
/d47/d47T .
For the notion of a pseudonatural equivalence we refer to [SW, App endix A]. According to the
conventions we ﬁxed there, it includes a weak inverse ¯t together with modiﬁcations
it : ¯t ◦t /d43/d51 idπ∗F and jt : id trivi
/d43/d51 t ◦ ¯t (2.2.1)
satisfying the so-called zigzag identities.
In the following we use the abbreviation triv i :=i ◦ triv, and we write Triv 2
π(i) for the 2-category
of 2-functors F : P2(M ) /d47/d47 T with π-local i-trivializations (together with all pseudonatural trans-
formations and all modiﬁcations). Next we come to the deﬁnition of a 2-category Des2
π(i) of descent
data with respect to a surjective submersion π :Y /d47/d47 M and a structure 2-groupoid i : Gr /d47/d47 T .
Deﬁnition 2.2.2. A descent object is a quadruple (triv,g,ψ,f ) consisting of a strict 2-functor
triv : P2(Y ) /d47/d47 Gr,
a pseudonatural equivalence
g : π∗
1trivi /d47/d47 π∗
2trivi,
and invertible, coherent modiﬁcations
ψ : id trivi
/d43/d51 ∆ ∗g and f : π∗
23g ◦π∗
12g /d43/d51 π∗
13g.
The coherence conditions for the modiﬁcations ψ and f can be found in [SW, Deﬁnition 2.2.1].
Let us brieﬂy rephrase the above deﬁnition in case that Y is the union of open sets Uα: ﬁrst there
are strict 2-functors triv α : P2(Uα) /d47/d47 Gr. To compare the diﬀerence between triv α and trivβ on a
two-fold intersection Uα ∩Uβ there are pseudonatural equivalences gαβ : (trivα)i /d47/d47 (trivβ)i. If we
assume for a moment that gαβ was the transition function of some ﬁbre bundle, one would demand
that 1 = gαα on every Uα and that gβγgαβ = gαγ on every three-fold intersection Uα ∩Uβ ∩Uγ. In
the present situation, however, these equalities have been replac ed by modiﬁcations: the ﬁrst one by
a modiﬁcation ψα : id (trivα )i
/d43/d51 gαα and the second one by a modiﬁcation fαβγ :gβγ ◦gαβ /d43/d51 gαγ.
Next we describe how to extract a descend object from a local triv ialization of a 2-functor following
[SW, Section 2.3]. Let F : P2(M ) /d47/d47 T be a 2-functor with a π-local i-trivialization (triv,t ). Using
the weak inverse ¯t : trivi /d47/d47 π∗F of t we deﬁne
g :=π∗
2t ◦π∗
1 ¯t :π∗
1trivi /d47/d47 π∗
2 trivi.
This composition is well-deﬁned since π∗
1π∗F =π∗
2π∗F . Let it andjt be the modiﬁcations (2.2.1). We
obtain ∆ ∗g =t ◦ ¯t, so that the deﬁnition ψ :=jt yields the invertible modiﬁcation ψ : id trivi
/d43/d51 ∆ ∗g.
Similarly, one deﬁnes with it the invertible modiﬁcation f . The quadruple (triv ,g,ψ,f ) obtained like
this is a descend object in the sense of Deﬁnition 2.2.2; see [SW, Lemma 2.3.1].
– 8 –
Next suppose (triv ,g,ψ,f ) and (triv ′,g ′,ψ ′,f ′) are descent objects. A descent 1-morphism
(triv,g,ψ,f ) /d47/d47 (triv′,g ′,ψ ′,f ′) is a pair ( h,ǫ ) consisting of a pseudonatural transformation
h : trivi /d47/d47 triv′
i
and an invertible modiﬁcation
ǫ :π∗
2h ◦g /d43/d51 g′ ◦π∗
1h
satisfying two natural coherence conditions; see [SW, Deﬁnition 2.2 .2]. Finally, we suppose that
(h1,ǫ 1) and ( h2,ǫ 2) are descent 1-morphisms from a descent object (triv ,g,ψ,f ) to another descent
object (triv ′,g ′,ψ ′,f ′). A descent 2-morphism (h1,ǫ 1) /d43/d51 (h2,ǫ 2) is a modiﬁcation
E :h1 /d43/d51 h2
satisfying another coherence condition; see [SW, Deﬁnition 2.2.3].
Descent objects, 1-morphisms and 2-morphisms form a 2-catego ry Des2
π(i), called the descent 2-
category. In concrete examples of the target 2-category T these structures have natural interpretations
in terms of smooth maps and diﬀerential forms, as we show in Section 4. The extraction of a descent
object from a local trivialization outlined above extends to a 2-func tor
Exπ : Triv2
π(i) /d47/d47 Des2
π(i), (2.2.2)
which we have described in [SW, Section 2.3].
In order to avoid the dependence to the ﬁxed surjective submers ionπ :Y /d47/d47 M , we have shown in
[SW, Section 4.2] that the two 2-categories Triv 2
π(i) and Des2
π(i) form a direct system for reﬁnements
of surjective submersions over M . The corresponding direct limits are 2-categories
Triv2(i)M := lim− →π
Triv2
π(i) and Des2(i)M := lim− →π
Des2
π(i).
For instance, an object in the direct limit is a pair of a surjective subm ersion π and an object in the
corresponding 2-category Triv 2
π(i) or Des2
π(i). 1-morphisms and 2-morphisms are deﬁned over common
reﬁnements. The 2-functor Ex π from (2.2.2) induces an equivalence
Triv2(i)M ∼= Des2(i)M
between these two direct limit 2-categories [SW, Proposition 4.2.1].
Finally, we want to get rid of the chosen trivializations that are attac hed to the objects of Triv 2(i)M .
We denote by Functi(P2(M ),T ) the 2-category of locally i-trivializable 2-functors, i.e. 2-functors which
admit aπ-locali-trivialization, for some surjective submersionπ. We have shown [SW, Theorem 4.3.1]:
Theorem 2.2.3. There is an equivalence
Functi(P2(M ),T ) ∼= Des2(i)M
between 2-categories of locally i-trivializable 2-functors and their descend data.
In Section 3 we select a sub-2-category of Des2(i)M consisting of smooth descend data . The corre-
sponding sub-2-category of Functi(P2(M ),T ) is the one we are aiming at – the 2-category of transport
2-functors.
– 9 –
