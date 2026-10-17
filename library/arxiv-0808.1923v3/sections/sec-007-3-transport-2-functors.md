---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-007-3-transport-2-functors
section_title: "Transport 2-Functors"
section_number: 3
pages: 12-15
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
toc_source: outline
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transport of connections on gerbes."
---
Transport 2-Functors
In this section we introduce the central deﬁnition of this paper: transport 2-functors. For this purpose,
we deﬁne in Section 3.1 a 2-category of smooth descent data, based on the notions of smooth 2-
functors and transport functors. In Section 3.2 we deﬁne transport 2-functors as those 2-functors that
correspond to smooth descent data under the equivalence of Theorem 2.2.3. Section 3.3 describes some
basic properties of transport 2-functors, and in Section 3.4 we construct an explicit example.
3.1
Smooth Descent Data
In this section we select a sub-2-category Des2
π(i)∞of smooth descent data in the 2-category Des2
π(i)
of descent data described in Section 2.2. If (triv, g, ψ, f) is a descent object, we demand that the strict
2-functor triv : P2(Y )
/ Gr has to be smooth in the sense of Section 2.3, i.e. internal to diﬀeological
spaces. Imposing smoothness conditions for the pseudonatural transformation g and the modiﬁcations
ψ and f is more subtle since they do not take values in the Lie 2-category Gr but in the 2-category T
which is not assumed to be a Lie 2-category.
Brieﬂy, we proceed in the following two steps. We explain ﬁrst how the pseudonatural transforma-
tion
g : π∗
1trivi
/ π∗
2trivi
can be viewed as a certain functor F(g) deﬁned on P1(Y [2]). Secondly, we impose the condition that
F(g) is a transport functor. A little motivation might be the observation that F(g) corresponds then
(at least in some cases, by Theorem 2.4.2) to a principal bundle with connection over Y [2] – one of the
well-known ingredients of a (bundle) gerbe, see Sections 4.2 and 4.3.
Let us ﬁrst explain in general how a pseudonatural transformation between two 2-functors can
be viewed as a functor. We consider 2-functors F and G between 2-categories S and T . Since a
pseudonatural transformation ρ : F
/ G assigns 1-morphisms in T to objects in S and 2-morphisms
in T to 1-morphisms in S, the general idea is to construct a category S0,1 consisting of objects and
1-morphisms of S and a category ΛT consisting of 1-morphisms and 2-morphisms of T such that ρ
yields a functor
F(ρ) : S0,1
/ ΛT .
We assume that S is strict, so that forgetting its 2-morphisms produces a well-deﬁned category S0,1.
The construction of the category ΛT is more involved.
If T is strict, the objects of ΛT are the 1-morphisms of T .
A morphism between objects
f : Xf
/ Yf and g : Xg
/ Yg is a pair of 1-morphisms x : Xf
/ Xg and y : Yf
/ Yg
and a 2-morphism
Xf
x
/
f

Xg
ϕ⑤⑤⑤
⑤⑤⑤
z ⑤⑤⑤
⑤⑤⑤
g

Yf
y
/ Yg.
(3.1.1)
This gives indeed a category ΛT , whose composition is deﬁned by putting the diagrams (3.1.1) next
to each other. Clearly, any strict 2-functor f : T ′
/ T induces a functor Λf : ΛT ′
/ ΛT . For a
more detailed discussion of these constructions we refer the reader to Section 4.2 of [SW11].
– 12 –
Now let ρ : F
/ G be a pseudonatural transformation between two strict 2-functors from S
to T . Sending an object X in S to the 1-morphism ρ(X) and sending a 1-morphism f in S to the
2-morphism ρ(X) now yields a functor
F(ρ) : S0,1
/ ΛT .
It respects the composition due to axiom (T1) for ρ and the identities due to [SW, Lemma A.7].
Moreover, a modiﬁcation A : ρ1
+3 ρ2 deﬁnes a natural transformation F(A) : F(ρ1)
+3 F(ρ2),
so that the result is a functor
F : Hom(F, G)
/ Funct(S0,1, ΛT )
(3.1.2)
between the category of pseudonatural transformations between F and G and the category of functors
from S0,1 to ΛT , for S and T strict 2-categories and F and G strict 2-functors.
In case that the 2-category T is not strict, the construction of ΛT suﬀers from the fact that the
composition is not longer associative. The situation becomes treatable if one requires the objects Xf, Yf
and Xg, Yg and the 1-morphisms x and y in (3.1.1) to be contained the image of a strict 2-category
T str under some 2-functor i : T str
/ T . The result is a category ΛiT , in which the associativity
i(X)
f

i(Y )
,
i(Xf)
i(x) /
f

i(Xg)
ϕ✇✇✇✇
✇✇✇✇
w ✇✇✇
✇✇✇
g

i(Yf)
i(y)
/ i(Yg)
and
i(Xf)
i(x′◦x)

c−1
x,x′
✤✤✤✤

✤✤✤✤
i(x) /
f

i(Xg)
ϕ✇✇✇✇
✇✇✇✇
w ✇✇✇
✇✇✇
g

i(x′) / i(Xh)
h

ϕ′✇✇✇✇
✇✇✇✇
w ✇✇✇
✇✇✇
i(Yf)
i(y′◦y)
B
cy,y′
✤✤✤✤✤✤

✤✤✤✤✤✤
i(y)
/ i(Yg)
i(y′)
/ i(Yh).
Figure 1: Objects, morphisms and the composition of the category ΛiT (the
diagram on the right hand side ignores the associators and the bracketing of
1-morphisms). Here, c is the compositor of the 2-functor i.
of the composition is restored by axiom (F3) on the compositor of the 2-functor i. We omit a more
formal deﬁnition and refer the reader to Figure 1 for an illustration. For any 2-functor f : T
/ T ′,
a functor
ΛF : ΛiT
/ ΛF ◦iT ′
is induced by applying f to all involved objects, 1-morphisms, and 2-morphisms. We may now consider
strict 2-functors F and G from S to T str. Then, the functor (3.1.2) generalizes straightforwardly to a
functor
F : Hom(i ◦F, i ◦G)
/ Funct(S0,1, ΛiT )
between the category of pseudonatural transformations between i ◦F and i ◦G and the category of
functors from S0,1 to ΛiT . The following lemma follows directly from the deﬁnitions.
Lemma 3.1.1. The functor F has the following properties:
– 13 –
(i) It is natural with respect to strict 2-functors f : S′
/ S in the sense that the diagram
Hom(i ◦F, i ◦G)
f ∗

F
/ Funct(S0,1, ΛiT )
f ∗

Hom(i ◦F ◦f, i ◦G ◦f)
F
/ Funct(S′
0,1, ΛiT )
is strictly commutative.
(ii) It
preserves
the
composition
of
pseudonatural
transformations
in
the
sense
that
if
F, G, H : S
/ T str are three strict 2-functors, the diagram
Hom(i◦G, i◦H)×Hom(i◦F, i◦G)
◦

F ×F / Funct(S0,1, ΛiT )×Funct(S0,1, ΛiT )
⊗

Hom(i ◦H, i ◦F)
F
/ Funct(S0,1, ΛiT )
is commutative.
In Lemma 3.1.1 (ii) the symbol ⊗has the following meaning. The composition of morphisms in
ΛiT was deﬁned by putting the diagrams (3.1.1) next to each other as shown in Figure 1. But one can
also put the diagrams of appropriate morphisms on top of each other, provided that the arrow on the
bottom of the upper one coincides with the arrow on the top of the lower one. This is indeed the case
for the morphisms in the image of composable pseudonatural transformations under F × F, so that
the diagram in (ii) makes sense. In a more formal context, the tensor product ⊗can be discussed in
the formalism of weak double categories, but we will not stress this point.
In the following discussion the strict 2-category S is the path 2-groupoid of some smooth manifold,
S = P2(X). Notice that S0,1 = P1(X) is then the path groupoid of X. The 2-category T is the target
2-category, and the strict 2-category T str is the Lie 2-groupoid Gr.
Let (triv, g, ψ, f) be a descent object in the descent 2-category Des2
π(i). The pseudonatural trans-
formation g : π∗
1trivi
/ π∗
2trivi induces a functor
F(g) : P1(Y [2])
/ ΛiT .
In order to impose the condition that F(g) is a transport functor, we will use the functor
Λi : ΛGr
/ ΛiT
as its structure Lie groupoid. Further, the modiﬁcation ψ : idtrivi
/ ∆∗g induces via Lemma 3.1.1
(i) a natural transformation
F(ψ) : F(idtrivi)
+3 ∆∗F(g).
Finally, the modiﬁcation f induces via Lemma 3.1.1 (i) and (ii) a natural transformation
F(f) : π∗
23F(g) ⊗π∗
12F(g)
+3 π∗
13F(g).
Deﬁnition 3.1.2. A descent object (triv, g, ψ, f) is called smooth if the following conditions are satis-
ﬁed:
(i) the 2-functor triv : P2(Y )
/ Gr is smooth.
– 14 –
(ii) the functor F(g) is a transport functor with ΛGr-structure.
(iii) the natural transformations F(ψ) and F(f) are morphisms between transport functors.
In the same way we qualify smooth descent 1-morphisms and descent 2-morphisms. A descent
1-morphism
(h, ǫ) : (triv, g, ψ, f)
/ (triv′, g′, ψ′, f ′)
is converted into a functor
F(h) : P1(Y )
/ ΛiT
and a natural transformation
F(ǫ) : π∗
2F(h) ⊗F(g)
+3 F(g′) ⊗π∗
1F(h).
We say that (h, ǫ) is smooth, if F(h) is a transport functor with ΛGr-structure and F(ǫ) is a 1-
morphism between transport functors. A descent 2-morphism E : (h, ǫ)
+3 (h′, ǫ′) is converted into a
natural transformation
F(E) : F(h)
+3 F(h′),
and we say that E is smooth, if F(E) is a 1-morphism between transport functors. We claim two
obvious properties of smooth descent data:
(i) Compositions of smooth descent 1-morphisms and smooth descent 2-morphisms are again smooth,
so that smooth descent data forms a sub-2-category of Des2
π(i), which we denote by Des2
π(i)∞.
(ii) Pullbacks of smooth descend objects, 1-morphisms and 2-morphisms along reﬁnements of surjec-
tive submersions are again smooth, so that the direct limit
Des2(i)∞
M := lim
−
→
π Des2
π(i)∞
is a well-deﬁned sub-2-category of Des2(i)M.
In Section 4 we show that the 2-category Des2(i)∞
M of smooth descent data becomes nice and familiar
upon choosing concrete examples for the structure 2-groupoid i : Gr
/ T .
