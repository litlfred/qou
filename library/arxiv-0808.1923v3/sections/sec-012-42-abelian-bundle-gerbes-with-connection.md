---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-012-42-abelian-bundle-gerbes-with-connection
section_title: "Abelian Bundle Gerbes with Connection"
section_number: 4.2
pages: 33-36
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
In this section we consider the target 2-category T = B(S1-Tor), the monoidal category of S1-torsors
viewed as a 2-category with a single object [SW, Example A.2]. Associa ted to this 2-category is the
2-functor
iS1 : BBS1 /d47/d47 B(S1-Tor)
that sends the single 1-morphism of BBS1 to the circle, viewed as an S1-torsor over itself. The main
result of this section is:
Theorem 4.2.1. There is an equivalence
TransBBS1 (M, B(S1-Tor)) ∼= BGrb∇(M )
between the 2-category of transport 2-functors on M with values in B(S1-Tor) and with BBS1-structure,
and the 2-category of bundle gerbes with connection over M .
Let us ﬁrst recall the deﬁnition of bundle gerbes following [Mur96, M S00, Ste00, Wal07]. For a
surjective submersion π :Y /d47/d47 M , we ﬁrst deﬁne the following 2-category BGrb∇(π):
1. An object is a tuple ( B,L,ω,µ ) consisting of a 2-form B ∈ Ω 2(Y ), a principal S1-bundle L
with connection ω overY [2] of curvature curv(ω) = π∗
1B −π∗
2B, and an associative, connection-
preserving bundle isomorphism
µ :π∗
23L ⊗π∗
12L /d47/d47 π∗
13L
– 33 –
overY [3].
2. A 1-morphism ( B,L,ω,µ ) /d47/d47 (B′,L ′,ω ′,µ ′), also known as stable isomorphism , is a principal
S1-bundleA with connection ς overY of curvature curv(ς) = B −B′ together with a connection-
preserving bundle isomorphism
α :π∗
2A ⊗L /d47/d47 L′ ⊗π∗
1A
overY [2], such that the diagram
π∗
3A ⊗π∗
23L ⊗π∗
12L
id ⊗µ /d47/d47
π∗
23α ⊗id
/d15/d15
π∗
3A ⊗π∗
13L
π∗
13α
/d15/d15
π∗
23L′ ⊗π∗
2A ⊗L
id⊗π∗
12α
/d15/d15
π∗
23L′ ⊗π∗
12L′ ⊗π∗
1A
µ′ ⊗id
/d47/d47π∗
13L′ ⊗π∗
1A
(4.2.1)
of bundle isomorphisms over Y [3] is commutative.
3. A 2-morphism ( A,ς,α ) /d43/d51 (A′,ς ′,α ′) is a connection-preserving bundle isomorphism ϕ :
A /d47/d47 A′ overY , such that the diagram
π∗
2A ⊗L
π∗
2ϕ ⊗idL
/d15/d15
α /d47/d47L′ ⊗π∗
1A
idL′ ⊗π∗
1ϕ
/d15/d15
π∗
2A′ ⊗L
α′
/d47/d47L′ ⊗π∗
1A′
(4.2.2)
of bundle isomorphisms over Y [2] is commutative.
The full 2-category of bundle gerbes with connection over M is then deﬁned as the direct limit
BGrb∇(M ) := lim− →π
BGrb∇(π).
The strategy to prove Theorem 4.2.1 is to ﬁrst establish the equivale nce on a local level:
Proposition 4.2.2. For every surjective submersion π :Y /d47/d47 M there is a surjective equivalence of
2-categories:
Des2
π(iS1)∞ ∼= BGrb∇(π).
A 2-functor Des2
π(iS1)∞ /d47/d47 BGrb∇(π) realizing the claimed equivalence is deﬁned in the following
way. For a smooth descent object (triv,g,ψ,f ), the smooth 2-functor triv : P2(Y ) /d47/d47 BBS1 deﬁnes by
Theorem 4.1.1 a 2-form B ∈ Ω 2(Y ), this is the ﬁrst ingredient of the bundle gerbe. The pseudonatur al
transformation g yields a transport functor
F (g) : P1(Y [2]) /d47/d47 ΛiS1 B(S1-Tor)
– 34 –
with Λ BBS1-structure. Despite of the heavy notation, the following lemma tra nslates this functor into
familiar language.
Lemma 4.2.3. For X a smooth manifold, there is a canonical surjective equivale nce of monoidal
categories
Bun∇
S1 (X) ∼= Trans1
Λ BBS1 (X, ΛiS1 B(S1-Tor))
between principal S1-bundles with connection and transport functors with Λ BBS1-structure.
Proof. First of all, we have evidently Λ BBS1 = BS1. Second, there is a canonical equivalence of
categories
ΛiS1 B(S1-Tor) ∼=S1-Tor. (4.2.3)
This comes from the fact that an object is in both categories an S1-torsor. A morphism between
S1-torsors V and W in Λ iS1 B(S1-Tor) is by deﬁnition a 2-morphism
∗ S1
/d47/d47
V
/d15/d15
∗
W
/d15/d15
f ⑧⑧⑧⑧⑧⑧⑧⑧
/d123/d3 ⑧⑧⑧⑧⑧⑧
∗
S1
/d47/d47 ∗
in B(S1-Tor), and this is in turn an S1-equivariant map
f :W ⊗S1 /d47/d47 S1 ⊗V .
It can be identiﬁed canonically with an S1-equivariant map f −1 : V /d47/d47 W , i.e. a morphism in
S1-Tor. It is straightforward to see that (4.2.3) is even a monoidal eq uivalence. Then, the claim is
proved by Theorem 2.4.2. □
Now, via Lemma 4.2.3 the transport functor F (g) is a principal S1-bundle L with connection ω
overY [2]. This circle bundle will be the second ingredient of the bundle gerbe.
Lemma 4.2.4. The curvature of the connection ∇ on the circle bundle L satisﬁes
curv(ω) = π∗
1B −π∗
2B.
Proof. Let Uα be open sets covering Y [2], and let ( ~triv, ˜t) be a local iS1-trivialization of the transport
functor F (g) consisting of smooth functors ~trivα : P1(Uα) /d47/d47 BS1 and natural transformations
˜tα : F (g)|Uα
/d47/d47 (~trivα)iS1 .
We observe that the functors ~trivα and the natural transformation ˜tα lie in the image of the functor
F , such that there exist smooth pseudonatural transformations ρα : π∗
1 triv|Uα
/d47/d47 π∗
2 triv|Uα and
modiﬁcations tα :g|Uα
/d43/d51 ρα with
~trivα = F (ρα) and ˜tα = F (tα).
As found in [SW11] and reviewed in Section 2.3 of the present article, a ssociated to the smooth
pseudonatural transformation ρα is a 1-form ϕα ∈ Ω 1(Uα), and equation (4.1.4) infers in the present
situation
π∗
1B −π∗
2B = dϕα.
– 35 –
It remains to trace back the relation between ϕα and the curvature of the connection ω on circle bundle
L. Namely, if Aα is the 1-form corresponding to the smooth functor ~trivα, we have
Aα =ϕα and d Aα = curv(ω).
This shows the claim. □
In order to complete the construction of the bundle gerbe, we not e that the modiﬁcation f :π∗
23g ◦
π∗
12g /d43/d51 π∗
13g induces an isomorphism
F (f ) : π∗
23F (g) ⊗π∗
12F (g) /d47/d47 π∗
13F (g)
of transport functors; again by Lemma 4.2.3 this deﬁnes an isomorp hism
µ :π∗
12L ⊗π∗
23L /d47/d47 π∗
13L
of circle bundles with connection, which is the last ingredient of the bu ndle gerbe. The coherence
axiom of [SW, Deﬁnition 2.2.1] implies the associativity condition on µ. This shows that ( B,L, ∇,µ )
is a bundle gerbe with connection. The descent datum ψ has been forgotten by this construction.
Using Lemma 4.2.3 in the same way as just demonstrated it is easy to as sign bundle gerbe 1-
morphisms to descent 1-morphisms and bundle gerbe 2-morphisms t o descent 2-morphisms. Here the
coherence conditions of [SW, Deﬁnitions 2.2.2 and 2.2.3] translate int o the commutative diagrams
(4.2.1) and (4.2.2). The composition for 1-morphisms and 2-morphism s of bundle gerbes (which we
have not carried out above) is precisely reproduced by the compos ition laws of the descent 2-category
Des2
π(iS1)∞. This deﬁnes the 2-functor of Proposition 4.2.2.
It is evident that this 2-functor is an equivalence of 2-categories, since all manipulations we have
made are equivalences according to Lemma 4.2.3 and Theorem 4.1.1. It remains to remark that the
descent datum ψ can be reproduced in a canonical way from a given bundle gerbe using the existence
of dual circle bundles, see Lemma 1 in [Wal07]. This ﬁnishes the proof of Proposition 4.2.2.
It is clear that the equivalence of Proposition 4.2.2 is compatible with th e reﬁnement of surjective
submersions, so that it given an equivalence in the direct limits:
Des2(iS1)∞
M ∼= BGrb∇(M ).
With Theorem 3.2.2 this proves Theorem 4.2.1.
