---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-018-53-properties-of-reduced-surface-holonomy
section_title: "Properties of Reduced Surface Holonomy"
section_number: 5.3
pages: 52-56
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
The reduced surface holonomy has nice properties that we will reve al in the following. First we treat
the dependence of the reduced surface holonomy on the marking.
We arrange the set of markings of S into equivalence classes, as it is common in the theory of
Riemann surfaces. Two markings ( x, M) and ( x′, M′), with M = {αi,βi} and M′ = {α′
i,β ′
i}, are
called equivalent, if there exists a path γ : x /d47/d47 x′ and bigons ∆ i : αi /d43/d51 γ ◦α′
i ◦γ−1 and ∆ ′
i :
βi /d43/d51 γ ◦β′
i ◦γ−1.
Lemma 5.3.1. Let (x, M) and (x′, M′) be equivalent good markings. Then,
RHoltra(φ,x, M) = RHol tra(φ,x ′, M′).
Proof. Each equivalence between markings splits into a sequence of steps, in which a step is either
conjugation of all paths in the marking by a path γ : x /d47/d47 y, or changing one of the paths via a
bigon. Thus it suﬃces to prove the invariance of the reduced surfa ce holonomy under each of these
steps. Let tra red: P2(M ) /d47/d47 BG be a reduction of tra, and let t := Red ◦ trared.
In the ﬁrst part of the proof we look at a conjugation. Let Σ : τM /d43/d51 idx be a fundamental bigon
for a marking ( x, M). Denote by ( x′, Mγ) the marking obtained by conjugating all paths with γ. We
haveτMγ =γ ◦τM ◦γ−1, and Σ γ := idγ ◦ Σ ◦ idγ−1 is a fundamental bigon for ( x′, Mγ). We have the
two paths t φ,M and tφ,Mγ and the compositors cφ,t : tφ,M /d43/d51 t(τM) and cφ,t
γ : tφ,Mγ
/d43/d51 t(τMγ ), so
that
Holt(φ,x, M) = t(Σ) ·cφ,t and Hol t(φ,x ′, M′) = t(Σ γ) ·cφ,t
γ .
Here, and in the following we will suppress writing φ∗ when we apply t to paths or bigons in S.
There is a unique compositor 2-morphism c : tφ,Mγ
/d43/d51 t(γ) ◦ tφ,M ◦ t(γ)−1, and another unique
compositor 2-morphism c′ : t(τMγ ) /d43/d51 t(γ) ◦ t(τM) ◦t(γ)−1. We claim that the diagram
tφ,Mγ
c
/d11/d19
cφ, t
γ /d43/d51 t(τMγ )
c′
/d11/d19
t(Σ γ ) /d43/d51 idt(φ(x))
id
/d11/d19
t(γ) ◦ tφ,M ◦t(γ)−1
id◦cφ, t◦id
/d43/d51t(γ) ◦ t(τM) ◦t(γ)−1
id◦t(Σ) ◦id
/d43/d51t(γ) ◦ id ◦t(γ)−1
is commutative. The subdiagram on the left commutes because of th e coherence of compositors en-
forced by axiom (F3). In order to see that the subdiagram on the r ight commutes we note that
c′ = cτMγ ◦γ−1,γ ·cγ−1,τMγ . Axiom (F2) applied to the 2-morphisms id, Σ γ and id gives the commuta-
tivity with cγ−1,γ ·cγ−1,id on the right hand side of the diagram. But the latter expression is eq ual to
1 for the normalized 2-functor t.
Next we compute c. We note the compositor between t( γ ◦α ◦γ−1) and t( γ) ◦ t(α) ◦ t(γ−1) is
cα◦γ−1,γ ·cγ−1,α, while the one between t( γ ◦α−1 ◦γ−1) and t(γ)◦ t(α−1)◦ t(γ−1) is cα−1◦γ−1,γ ·cγ−1,α−1.
These two compositors are actually inverse to each other; this follo ws from axiom (F3) for compositors
– 52 –
and the fact that t is normalized. Also note that t( γ) ◦ t(γ−1) = id; again since t is normalized. Thus,
we see that c = 1. All together, we see that Hol t(φ,x, M) = Hol t(φ,x ′, M′).
In the second part of the proof we look at a change of one of the pa ths via a bigon. If M = {αi,βi}g
i=1
is a marking, we look at another marking M′ consisting of the same paths except for an index i0 where
a diﬀerent path α′
i0 is present, related to αi0 by a bigon ∆ : α′
i0
/d43/d51 αi0 . Let ∆ # :α′−1
i0
/d43/d51 α−1
i0 be
the “horizontally inverted” bigon given by ∆ #(s,t ) := ∆( s, 1 −t). We consider the 2-morphism
˜∆ := id ◦ (∆ ◦ idβi0 ◦ ∆ # ◦ idβ−1
i0
) ◦ id : τM′ /d43/d51 τM,
with the outer identities meant for all factors with indices not equal to i0. We also consider the
2-morphism
t∆ := id ◦ (t(∆) ◦ id ◦ t(∆ #) ◦ id) ◦ id : tφ,M′ /d43/d51 tφ,M.
If Σ : τM /d43/d51 idx is a fundamental bigon for M, then Σ ′ := Σ • ˜∆ is a fundamental bigon for M′. We
claim that the diagram
tφ,M′
c′ φ, t
/d43/d51
t∆
/d11/d19
t(τM′ )
t(Σ ′)
/d35/d43PPPPPPPPP
PPPPPPPPP
t( ˜∆)
/d11/d19
id
tφ,M cφ, t
/d43/d51 t(τM)
Σ
/d51/d59♥♥♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥♥♥
is commutative. Indeed, the rectangular part commutes due to ax iom (F2) for the 2-functor t, and
the triangular part commutes by deﬁnition of Σ ′. It remains to notice that t∆ = 1 ∈ Gred, since
the contributions of ∆ and ∆ # cancel. Then, the diagram implies the coincidence of the surface
holonomies. □
We summarize our results about the surface holonomy of non-abelia n gerbes in the following theo-
rem, which constitutes the main result of this section.
Theorem 5.3.2. Let G be a Lie 2-group, T be a 2-category, and i : BG /d47/d47 T be an equivalence of
2-categories. Let tra : P2(M ) /d47/d47 T be a transport 2-functor with BG-structure. Let S be a closed
oriented surface with a good marking (x, M), and let φ :S /d47/d47 M be a smooth map. Then, the reduced
surface holonomy
RHoltra(φ,x, M) ∈ Gred
depends only on the equivalence class of the marking, and onl y on the isomorphism class of tra.
Proof. After Lemma 5.3.1 it only remains to prove that the reduced s urface holonomy only depends
on the isomorphism class of tra. Indeed, if tra ∼= tra′ is an isomorphism we can choose the same
reduction for both. □
In Section 4 we have collected various equivalences between transp ort 2-functors and concrete
models of gerbes with connections. These equivalences were mostly established by zigzags of canonically
deﬁned 2-functors. On the level of isomorphism classes, such zigz ags give a well-deﬁned bijection. Since
the reduced surface holonomy is invariant under isomorphisms, the se bijections convey the concept of
reduced surface holonomy to a well-deﬁned, isomorphism-invariant concept for each of these concrete
models:
(i) The bijection
ˆH 2(M, G) ∼= h0Trans2
Gr(M,T )
– 53 –
of Theorem 4.1.6 between the non-abelian diﬀerential cohomology an d transport 2-functors equips
non-abelian cohomology with a well-deﬁned, isomorphism-invariant co ncept of surface holonomy.
In particular, it equips degree two Deligne cocycles and (fake-ﬂat) Breen-Messing cocycles with a
well-deﬁned, isomorphism-invariant concept of surface holonomy. We show below in Proposition
5.3.3 in the case of Deligne cocycles it reproduces the existing concep t of surface holonomy. In
the case of Breen-Messing cocycles such a concept was previously unknown; its is one of the main
results of this article.
(ii) The equivalence of Theorem 4.2.1 induces a canonical bijection
h0BGrb∇(M ) ∼= h0TransBBS1 (M, B(S1-Tor))
of between isomorphism classes of bundle gerbes with connections a nd isomorphism classes
of transport 2-functors, and so equips bundle gerbes with conne ction with a well-deﬁned,
isomorphism-invariant concept of surface holonomy. We show below in Proposition 5.3.3 that
it reproduces the existing concept of surface holonomy for abelian gerbes.
(iii) The injective map
h0(H-BGrb∇f f(M )) /d47/d47 h0(Trans2
BAUT(H)(M, B(H-BiTor)))
of Theorem 4.3.1 between isomorphism classes of fake-ﬂat non-abe lianH-bundle gerbes with con-
nection and transport 2-functors, equips fake-ﬂat non-abelian H-bundle gerbes with connection
with a well-deﬁned, isomorphism-invariant concept of surface holon omy. Such a concept was
previously unknown; it is one of the main results of this article.
Now we prove that the reduced surface holonomy of Theorem 5.3.2 r educes in the case G = BS1
to the established notion of surface holonomy for connections on BS1-gerbes. Let us ﬁrst recall that
established notion.
It can be given for an element ξ ∈ ˆH 2(M, BS1) of the (abelian) diﬀerential cohomology group
which classiﬁes BS1-gerbes. It is solely based on the fact that diﬀerential cohomology sits in an exact
sequence
1 /d47/d47 Ω 2
cl,Z(M ) /d47/d47 Ω 2(M ) I /d47/d47 ˆH 2(M, BS1) /d47/d47H 3(M, Z) /d47/d47 0 ,
in which Ω 2
cl,Z(M ) denotes the closed 2-forms with integral periods [Bry93]. If φ :S /d47/d47 M is a smooth
map from a closed oriented surface S to M , then φ∗ξ ∈ ˆH 2(S, BS1) projects to zero in 0 ∈ H 3(S, Z)
for dimensional reasons, and so is the image of a 2-form B ∈ Ω 2(S) under the map I in the sequence.
The abelian surface holonomy of ξ around φ is then deﬁned as
AbHolξ(φ) := exp
(
−
∫
S
B
)
∈ S1.
Since the diﬀerence between two choices of 2-forms is a closed 2-fo rm with integral periods, this integral
is independent of the choice of B.
Proposition 5.3.3. Let tra : P2(M ) /d47/d47 T be a transport 2-functor with BBS1-structure. Let
ξ ∈ ˆH 2(M, BS1) be the associated class under the bijection of Theorem 4.1.6 . Then,
RHoltra(φ,x, M) = AbHolξ(φ),
i.e. the reduces surface holonomy of tra coincides with the established notion of surface holonomy f or
abelian gerbes. In particular, it is independent of the mark ing.
– 54 –
Proof. For any smooth manifold X, we have an equality between Ω 2(X) and the objects of the
2-category Z 2
X (BS1)∞. The latter is isomorphic to the 2-category Funct ∞(P2(X), BS1) of smooth
2-functors via Theorem 4.1.1, and we have computed in Lemma 4.1.2 th at
F (Σ) = exp
(
−
∫
Σ
B
)
(5.3.1)
for any bigon Σ ∈ BX . By construction we have a commutative diagram
Ω 2(X) I /d47/d47
/d15/d15
ˆH 2(X, BS1)
/d15/d15
Funct∞(P2(X), BS1) /d47/d47 h0Trans2
BBS1(X, BBS1),
in which the map on the bottom is the inclusion of smooth 2-functors in transport 2-functors.
Note that Gred = S1 with Example 5.2.3 (a) and Red = id BBS1. Let tra red be a reduction of the
given transport 2-functor, corresponding to the class ξ under the vertical map on the right hand side of
the diagram. After pullback along φ :S /d47/d47 M we obtain the 2-form B ∈ Ω 2(S) such that I(B) = ξ.
Let F : P2(S) /d47/d47 BS1 be the smooth 2-functor that corresponds to B. By commutativity of the
diagram, we ﬁnd an isomorphism
F ∼=φ∗trared (5.3.2)
between transport 2-functors.
If now Σ is a fundamental bigon for the marking ( x, M), then we have on one side
AbHolξ(φ) := exp
(
−
∫
S
B
)
Lemma 5.1.3
= exp
(
−
∫
Σ
B
)
(5.3.1)
= F (Σ) = Hol F (id,x, M),
where the last equality is Deﬁnition 5.1.5 combined with the fact that F is a strict 2-functor (with
trivial compositors). Lemma 5.2.6 applied to the equivalence (5.3.2) sh ows that
HolF (id,x, M) = Holφ∗trar e d(id,x, M).
We have on the other side
Holφ∗trar e d(id,x, M) = Hol trar e d(φ,x, M) = RHol tra(φ,x, M),
this shows the claimed coincidence. □
Finally, let us comment on the dependence of the reduced surface h olonomy on the equivalence
class of a marking. Let S be a closed oriented surface, and let ( x, M) and ( x′, M′) two markings. A
standard result from the theory of Riemann surfaces is:
(i) There exists an orientation-preserving diﬀeomorphism f :S /d47/d47 S such that (x′, M′) = f (x, M),
(ii) The diﬀeomorphism f is homotopic to the identity map id S if and only if ( x, M) and (x′, M′) are
equivalent.
The quotient of the group of orientation-preserving diﬀeomorphis ms modulo those homotopic to the
identity is the mapping class group of S, denoted M(S). Thus, M(S) acts on the reduced surface
holonomies of a surface φ :S /d47/d47 M . Currently we do not know what this action is; in particular, we
do not know if it is trivial or not.
– 55 –
