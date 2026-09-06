---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-014-44-2-bundles-with-connections
section_title: "2-Bundles with Connections"
section_number: 4.4
pages: 41-46
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
Apart from the equivalence between transport functors and prin cipalG-bundles with connection (Theo-
rem 2.4.2), our paper [SW09] also contains an analogous equivalence f or vector bundles with connection.
It has an immediate generalization to 2-vector bundles with many app lications, on which we shall give
a brief outlook.
Suppose 2Vect is some 2-category of 2-vector spaces. Given a 2- group G, a representation of G on
such a 2-vector space is a 2-functor
ρ : BG /d47/d47 2Vect.
A 2-vector bundle with connection and structure 2-group G is nothing but a transport 2-functor
tra : P2(X) /d47/d47 2Vect with BG-structure. Important classes of 2-vector bundles are line 2-bu ndles
and string bundles.
4.4.1 Models for 2-V ector Spaces
Depending on the precise application there is some ﬂexibility in what one may want to understand
under a 2-vector space. Usually 2-vector spaces are abelian modu le categories over a given monoidal
category. For k a ﬁeld, two important classes of examples are the following. First, let ˆk be the discrete
monoidal category over k. Then, 2Vect is 2-category of module categories over ˆk. This is equivalent
to the 2-category of categories internal to k-vector spaces. These Baez-Crans 2-vector spaces [BC04]
are appropriate for the discussion of Lie 2-algebras.
The second model for 2Vect is the 2-category of module categorie s over the monoidal category
Vect(k) of k-vector spaces,
2Vect := Vect(k)-Mod.
– 41 –
In its totality this is rather unwieldy, but it contains two important su b-2-categories: the 2-category
KV(k) of Kapranov-Voevodsky 2-vector spaces [KV94] and the 2-category Bimod( k), whose objects
are k-algebras, whose 1-morphisms are bimodules over these algebras a nd whose 2-morphisms are
bimodule homomorphisms [Shu08]. Indeed, there is an inclusion 2-func tor
ι : Bimod(k) /d31 /d127 /d47/d47 Vect(k)-Mod
that sends a k-algebra A to the category A-Mod of ordinary (say, right) A-modules. This is a module
category over Vect(k) by tensoring a right module from the left by a vector space. A 1-mo rphism, an
A-B-bimoduleN , is sent to the functor that tensores a right A-module from the right by N , yielding a
rightB-module. A bimodule morphism induces evidently a natural transform ation of these functors.
If one restricts the 2-functor ι to the full sub-2-category formed by those algebras that are dir ect
sumsA =k⊕n of the ground ﬁeld algebra, the 2-vector spaces in the image of ι are of the form Vect(k)n,
i.e. tuples of vector spaces. The 1-morphisms in the image are ( m ×n)-matrices whose entries are
k-vector spaces. These form the 2-category of Kapranov-Voev odsky 2-vector spaces [KV94].
4.4.2 The canonical Representation of a 2-Group
Every automorphism 2-group AUT( H) of a Lie group H has a canonical representation on 2-vector
spaces, namely
BAUT(H) A /d47/d47 Bimod(k) ι /d47/d47 Vect(k)-Mod, (4.4.1)
where the 2-functor A is deﬁned similar as the one we have used for the non-abelian bundle ge rbes in
(4.3.1). It sends the single object to k regarded as a k-algebra, it sends a 1-morphism ϕ ∈ Aut(H) to
the bimodule ϕk in the notation of Section 4.3.2, and it sends a 2-morphism ( ϕ,h ) : ϕ /d43/d51 ch ◦ϕ to
the multiplication with h from the left.
Now let G be any smooth Lie 2-group corresponding to a smooth crossed mod ule (G,H,t,α ). We
have a canonical 2-functor
BG /d47/d47 BAUT(H) : ∗
g
/d27/d27
g′
/d67/d67h
/d11/d19
∗ ✤ /d47/d47 ∗
αg
/d27/d27
αg′
/d67/d67h
/d11/d19
∗ (4.4.2)
whose composition with (4.4.1) gives a representation of G, that we call the canonicalk-representation.
Example 4.4.1. A very simple but useful example is the canonical C-representation of BC ×. In this
case the composition (4.4.1) is the 2-functor
ρ : BBC × /d47/d47 Vect(C)-Mod : ∗
id
/d27/d27
id
/d67/d67z
/d11/d19
∗ ✤ /d47/d47 Vect(C)
− ⊗C
/d36/d36
− ⊗C
/d58/d58
−·z
/d11/d19
Vect(C)
for all z ∈ C ×. Notice that Vect( C) is the canonical 1-dimensional 2-vector space over C in the same
sense in that C is the canonical 1-dimensional complex 1-vector space. Therefor e, transport 2-functors
tra : P2(M ) /d47/d47 Vect(C)-Mod
– 42 –
with BBC ×-structure deserve to be addressed as line 2-bundles with connection . Two remarks:
1. Going through the discussion of abelian bundle gerbes with connec tion in Section 4.2 it is easy to
see that line 2-bundles with connection are equivalent to bundle gerb es with connection deﬁned
via line bundles instead of circle bundles.
2. The ﬁbre tra( x) of a line 2-bundle tra at a point x is an algebra which is Morita equivalent to the
ground ﬁeld C. These are exactly the ﬁnite rank operators on a separable Hilbert space. Thus,
line 2-bundles with connection are a form of bundles of ﬁnite rank ope rators with connection,
this is the point of view taken in [BCM +02].
The 2-functor A : BAUT(H) /d47/d47 Bimod(k) we have used above can be deformed to a 2-functor
Aρ using an ordinary representation ρ : BH /d47/d47 Vect(k) of H. It sends the object of BAUT(H) to
the algebra Aρ(∗) which is the vector space generated from all the linear maps ρ(h). A 1-morphism
ϕ ∈ Aut(H) is again sent to the bimodule ϕAρ(∗), and the 2-morphisms as before to left multiplications.
The original 2-functor is reproduced by A =Atrivk from the trivial representation of H on k.
Example 4.4.2. For G a compact simple and simply-connected Lie group, we consider the lev el k
central extension Hk := ˆΩkG of the group of based loops in G. For a positive energy representation
ρ : B ˆΩkG /d47/d47 Vect(k) the algebra Aρ(∗) turns out to be a von Neumann-algebra while the bimodules
ϕAρ(∗) are Hilbert bimodules. In this inﬁnite-dimensional case we have to ma ke the composition of
1-morphisms more precise: here we take not the algebraic tensor p roduct of these Hilbert bimodules
but the Connes fusion tensor product [ST04]. Connes fusion produ ct still respects the composition: for
A a von Neumann algebra and ϕA the bimodule structure on it induced from twisting the left action
by an algebra automorphism ϕ, we have
ϕA ⊗ϕ′A ≃ ϕ′◦ϕA
under the Connes fusion tensor product. Now let G = Stringk(G) be the string 2-group deﬁned from
the crossed module ˆΩkG /d47/d47 P0G of Fr´ echet Lie groups [BCSS07]. Together with the projection
2-functor (4.4.2) we obtain an induced representation
i : BStringk(G) /d47/d47 BimodCF(k)
The ﬁbres of a transport 2-functor
tra : P2(M ) /d47/d47 BimodCF(k) (4.4.3)
with BStringk(G)-structure are hence von Neumann algebras, and its parallel tra nsport along a path is
a Hilbert bimodule for these ﬁbres. In conjunction with the result [BS 09, BBK12] that String k(G)-2-
bundles have the same classiﬁcation as ordinary ﬁbre bundles whose structure group is the topological
String group, this says that transport 2-functors (4.4.3) have t o be addressed as String 2-bundles with
connection, see [ST04].
4.4.3 Twisted V ector Bundles
Vector bundles over M twisted by a class ξ ∈ H 3(M, Z) are the same thing as gerbe modules for
a bundle gerbe G whose Dixmier-Douady class is ξ [BCM+02]. These modules are in turn nothing
else but certain (generalized) 1-morphisms in the 2-category of bu ndle gerbes BGrb(M ) [Wal07]. The
– 43 –
same is true for connections on twisted vector bundles. More prec isely, a twisted vector bundle with
connection is the same as a 1-morphism
E : G /d47/d47 Iρ
from the bundle gerbe G with connection to the trivial bundle gerbe I equipped with the connection
2-form ρ ∈ Ω 2(M ).
Now let
tra : P2(M ) /d47/d47 Vect(C)-Mod
be a transport 2-functor which plays the role of the bundle gerbe G, but we allow an arbitrary structure
2-group G and any representation ρ : BG /d47/d47 Vect(C)-Mod. Let tra ∞ : P2(M ) /d47/d47 BG be a
smooth 2-functor which plays the role of the trivial bundle gerbe. W e shall now consider transport
transformations
A : tra /d47/d47 tra∞
ρ .
Let π :Y /d47/d47 M be a surjective submersion for which tra admits a local trivialization w ith smooth
descent data (triv,g,ψ,f ). The descent data of tra ∞ is of course (π∗tra∞, id, id, id). Now the transport
transformation A has the following descent data: the ﬁrst part is a pseudonatural t ransformation
h : triv /d47/d47 π∗tra∞ whose associated functor F (h) : P1(Y ) /d47/d47 Λρ(Vect(C)-Mod) is a transport
functor with Λ BG-structure. The second part is a modiﬁcation ǫ :π∗
2h◦g /d43/d51 id◦π∗
1h whose associated
natural transformation
F (ǫ) : π∗
2F (h) ⊗ F (g) /d47/d47 π∗
1F (h)
is a morphism of transport functors over Y [2]. According to the coherence conditions on descent
1-morphisms, it ﬁts into the commutative diagram
π∗
3 F (h) ⊗π∗
23F (g) ⊗π∗
12F (g)
π∗
23F (ǫ) ⊗id /d47/d47
id⊗F (f )
/d15/d15
π∗
2 F (h) ⊗π∗
12F (g)
π∗
12F (ǫ)
/d15/d15
π∗
3 F (h) ⊗π∗
13F (g)
π∗
13F (ǫ)
/d47/d47π∗
1 F (h)
(4.4.4)
of morphisms of transport functors over Y [3] and satisﬁes ∆ ∗F (ǫ) ◦ F (ψ) = id. The transport functor
F (h) : P1(Y ) /d47/d47 Λρ(Vect(C)-Mod)
together with the natural transformation F (ǫ) is the general version of a vector bundle with connection
twisted by a transport 2-functor tra. According to Sections 4.1 a nd 4.3, the twists can thus be Breen-
Messing gerbes or non-abelian bundle gerbes with connection.
Depending on the choice of the representation ρ, our twisted vector bundles can be translated into
more familiar language. Let us demonstrate this in the case of Examp le 4.4.1, in which the twist is a
line 2-bundle with connection, i.e. a transport 2-functor
tra : P2(M ) /d47/d47 Vect(C)-Mod
with BBC ×-structure. In order to obtain the usual twisted vector bundles , we restrict the target
2-category to BVect(C), the monoidal category of complex vector spaces considered as a 2-category.
The following Lie category Gl is appropriate: its objects are the nat ural numbers N, and it has only
morphisms between equal numbers, namely all matrices Gl n(C). The composition is the product of
– 44 –
matrices. The Lie category Gl is strictly monoidal: the tensor produ ct of two objects m,n ∈ N is
the product nm ∈ N, and the one of two matrices A ∈ Gl(m) and B ∈ Gl(n) is the ordinary tensor
product A ⊗B ∈ Gl(m ×n). In fact, Gl carries a second monoidal structure coming from th e sum of
natural numbers and the direct sum of matrices, so that Gl is actu ally a bipermutative category , see
Example 3.1 of [BDR04].
Notice that we have a canonical inclusion functor ι : BC × /d31 /d127 /d47/d47 Gl, which induces another inclusion
ι∗ : Trans2
BBC ×(M, BVect(C)) /d47/d47 Trans2
BGl(M, BVect(C))
of line 2-bundles with connection into more general vector 2-bundle s with connection. Here we have
used the representation
ρ : BGl /d47/d47 BVect
obtained as a generalization of Example 4.4.1 from C × = Gl 1(C) to Gl n(C) for all n ∈ N. The
composition ρ ◦ι reproduces the representation of Example 4.4.1.
Using the above inclusion, the given transport 2-functor tra induc es a transport 2-functor ι∗ ◦ tra :
P2(M ) /d47/d47 BVect(C) with BGl-structure, and one can study transport transformations
A : tra /d47/d47 tra∞
ρ
in that greater 2-category Trans 2
BGl(M, BVect(C)). Along the lines of the general procedure described
above, we have transport functors F (g) and F (h) coming from the descent data of tra and A, respec-
tively. In the present particular situation, the ﬁrst one takes valu es in the category Λ ρ◦ιBVect1(C)
whose objects are one-dimensional complex vector spaces and wh ose morphisms from V to W are
invertible linear maps f :W ⊗ C /d47/d47 C ⊗V . Similar to Lemma 4.2.3, this category is equivalent to
the category Vect 1(C) of one dimensional complex vector spaces itself. Thus, the trans port functor
F (g) with BC ×-structure is a complex line bundle L with connection over Y [2]. The second transport
functor, F (h), takes values in the category Λ ρ◦ιBVect(C). This category is equivalent to the category
Vect(C) itself. It has Λ ιBGl-structure, which is equivalent to Gl. Thus, F (h) is a transport functor
with values in Vect( C) and Gl-structure. It thus corresponds to a ﬁnite rank vector b undle E overY
with connection.
Since all identiﬁcations we have made so far a functorial, the morphis ms F (f ) and F (ǫ) of transport
functors induce morphisms of vector bundles that preserve the c onnections, namely an associative
morphism
µ :π∗
23L ⊗π∗
12L /d47/d47 π∗
13L
of line bundles over Y [2], and a morphism
̺ :π∗
2E ⊗L /d47/d47 π∗
1E
of vector bundles over Y which satisﬁes a compatibility condition corresponding to (4.4.4). This
reproduces the deﬁnition of a twisted vector bundle with connectio n [BCM +02]. We remark that
the 2-form ρ that corresponds to the smooth 2-functor tra ∞
ρ which was the target of the transport
transformationA we have considered, is related to the curvature of the connection on the vector bundle
E: it requires that
curv(E) = In · (curv(L) −π∗ρ),
whereIn is the identity matrix and n is the rank of E. This condition can be derived similar to Lemma
4.2.4.
– 45 –
