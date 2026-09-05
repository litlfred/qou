---
doc_id: arxiv-0808.1923v3
doc_title: "Connections on Non-Abelian Gerbes and their Holonomy"
section_id: sec-011-4-transport-2-functors-are-non-abelian-gerbes
section_title: "Transport 2-Functors are Non-Abelian Gerbes"
section_number: 4
pages: 25-33
source_pdf: 0808.1923v3.pdf
source_sha256: 3c53f7c0fd9acf89
doc_brief: "Connections on Non-Abelian Gerbes and their Holonomy — We introduce an axiomatic framework for the parallel transp ort of connections on gerbes."
---
In this section we show that transport 2-functors reproduce – s ystematically, by choosing appropriate
target 2-categories and structure 2-groups – four known conc epts of gerbes with connections: Deligne
cocycles and Breen-Messing cocycles (Section 4.1), abelian bundle g erbes (Section 4.2), and non-
abelian bundle gerbes (Section 4.3). In Section 4.4 we establish a furt her relation between transport
2-functors and 2-vector bundles with connection. Conversely, a ll these structures are examples of
transport 2-functors.
4.1 Diﬀerential Non-Abelian Cohomology
In this section we set up a classifying theory for transport 2-func tors P2(M ) /d47/d47 T with structure Lie
2-groupoidi : BG /d47/d47 T , for G a Lie 2-group coming from a smooth crossed module ( G,H,t,α ),T an
arbitrary 2-category, and i an equivalence of categories. The latter condition together with Th eorem
3.2.2 implies that we have equivalences
Trans2
BG(M,T ) ∼= Des2(i)∞
M ∼= Des2(idBG)∞
M (4.1.1)
of 2-categories.
Our strategy is to translate the structure of the 2-category Des2(idBG)∞
M into an equivalent 2-
category of “non-abelian diﬀerential cocycles” made up of smooth functions and diﬀerential forms,
with respect to open covers of M . Isomorphism classes of non-abelian diﬀerential cocycles form a se t
which we deﬁne as the non-abelian diﬀerential cohomology of M ; it classiﬁes transport 2-functors on
M with BG-structure up to isomorphism.
4.1.1 Smooth F unctors and Diﬀerential F orms
For the translation of the 2-category Des2(idBG)∞
M into smooth functions and diﬀerential forms we recall
a general result about the 2-category Funct ∞(P2(X), BG) of smooth 2-functors, smooth pseudonatural
– 25 –
transformations, and smooth modiﬁcations deﬁned on a smooth ma nifold X, with values in the Lie
2-groupoid BG. Following [SW11, Section 2.2], it corresponds to the following struct ure expressed in
terms of smooth functions and diﬀerential forms:
(i) A smooth 2-functor F : P2(X) /d47/d47 BG induces a pair of diﬀerential forms: a 1-form A ∈ Ω 1(X, g)
with values in the Lie algebra of G, and a 2-form B ∈ Ω 2(X, h) with values in the Lie algebra of
H, such that
dA + [A ∧A] = t∗ ◦B. (4.1.2)
(ii) A smooth pseudonatural transformation ρ :F /d47/d47 F ′ gives rise to a 1-form ϕ ∈ Ω 1(X, h) and a
smooth map g :X /d47/d47 G, such that
A′ +t∗ ◦ϕ = Ad g(A) −g∗ ¯θ (4.1.3)
B′ +α∗(A′ ∧ϕ) + dϕ + [ϕ ∧ϕ] = ( αg)∗ ◦B. (4.1.4)
The identity id : F /d47/d47 F has ϕ = 0 and g = 1. If ρ1 and ρ2 are composable pseudonatural
transformations, the 1-form of their composition ρ2 ◦ρ1 is (αg2 )∗ ◦ϕ1 +ϕ2, and the smooth map
is g2g1 :X /d47/d47 G.
(iii) A smooth modiﬁcation A :ρ /d43/d51 ρ′ gives rise to a smooth map a :X /d47/d47 H, such that
g′ = (t ◦a) ·g and ϕ′ + (r−1
a ◦αa)∗(A′) = Ada(ϕ) −a∗ ¯θ. (4.1.5)
The identity modiﬁcation id ρ has a = 1. If two modiﬁcations A1 and A2 are vertically compos-
able, A2 • A1 has the map a2a1. If two modiﬁcations A1 : ρ1 /d43/d51 ρ′
1 and A2 : ρ2 /d43/d51 ρ′
2 are
horizontally composable, A2 ◦ A1 has the map a2α(g2,a 1).
The structure (i), (ii) and (iii) forms a strict 2-category Z 2
X(G)∞, which we call the 2-category of
G-connections on X [SW11].
Theorem 4.1.1 ([SW11, Theorem 2.20]) . The correspondences described above furnish a strict 2-
functor
Funct∞(P2(X), BG) D /d47/d47Z 2
X (G)∞,
which is an isomorphism of 2-categories.
We remark that we have already used this isomorphism on the level of objects as a bijection (3.3.1).
For a general Lie 2-group G the correspondence between a smooth 2-functor F : P2(X) /d47/d47 BG
and the pair (A,B ) with A ∈ Ω 1(X, g) and B ∈ Ω 2(X, h) is established by an iterated integration and
described in detail in [SW11, Section 2.3.1]. For the Lie 2-group G = BS1 it reduces to the following
relation.
Lemma 4.1.2. LetB ∈ Ω 2(X) be a 2-form. Then, the smooth 2-functor F : P2(X) /d47/d47 BBS1 that
corresponds to B under the isomorphism of Theorem 4.1.1 is given by
F (Σ) = exp
(
−
∫
[0,1]2
Σ ∗B
)
,
for all bigons Σ ∈ BX .
– 26 –
Proof. We go through the construction in [SW11, Section 2.3.1] and r educe everything to the case
G = BS1. The 1-form AΣ in [SW11, Equation 2.26] is
AΣ = −
∫
[0,1]
Σ ∗B ∈ Ω 1([0, 1]),
with the integration performed over the second factor of [0 , 1]2. It extends (due to the sitting in-
stants of Σ) to a 1-form on R, and so corresponds via [SW09, Proposition 4.7] to a smooth functo r
FAΣ : P1(R) /d47/d47 BS1, which is just a smooth map fΣ : R × R /d47/d47 S1. The correspondence between
the 1-form AΣ and the function fΣ is by [SW09, Lemma 4.1]:
fΣ (t0,t 1) = exp
(∫ t1
t0
−AΣ
)
.
According to the prescription, [SW11, Equation 2.27] and [SW11, Pro position 2.17] deﬁne
F (Σ) = fΣ (0, 1)−1 = exp
(∫ 1
0
AΣ
)
= exp
(
−
∫
[0,1]2
Σ ∗B
)
.
□
4.1.2 Non-abelian Diﬀerential Cocycles
We want to translate the structure of the 2-category Des2
π(idBG)∞ of smooth descent data with respect
to a surjective submersion π :Y /d47/d47 M into smooth functions and diﬀerential forms, using Theorem
4.1.1 as a dictionary.
We recall that an object in Des2
π(idBG)∞ is a collection (triv,g,ψ,f ) containing a smooth 2-functor
triv : P2(Y ) /d47/d47 BG, a pseudonatural transformation g :π∗
1triv /d47/d47 π∗
2 triv whose associated functor
F (g0) : P1(Y [2]) /d47/d47 BG is a transport functor, and modiﬁcations ψ and f whose associated natural
transformations F (ψ) and F (f ) are morphisms between transport functors.
We begin with looking at a sub-2-category U ⊆ Des2
π(idBG)∞ in which all pseudonatural transfor-
mations and modiﬁcations are smooth, i.e. correspond to trivial tra nsport functors and morphisms
between trivial transport functors. An object (triv ,g ∞,ψ ∞,f ∞) in U corresponds under Theorem 4.1.1
to the following structure:
(a) an object ( A,B ) := D(triv) in Z 2
Y (G)∞, i.e. diﬀerential forms A ∈ Ω 1(Y, g) and B ∈ Ω 2(Y, h)
satisfying relation (4.1.2).
(b) a 1-morphism
(g,ϕ ) := D(g∞) : π∗
1 (A,B ) /d47/d47 π∗
2(A,B )
in Z 2
Y [2] (G)∞, i.e. a smooth function g :Y [2] /d47/d47 G and a 1-form ϕ ∈ Ω 1(Y [2], h) satisfying the
relations (4.1.3) and (4.1.4).
(c) a 2-morphism
f := D(f∞) : π∗
23(g,ϕ ) ◦π∗
12(g,ϕ ) /d43/d51 π∗
13(g,ϕ )
in Z 2
Y [3] (G)∞ and a 2-morphism
ψ := D(ψ∞) : id (A,B) /d43/d51 ∆ ∗(g,ϕ )
in Z 2
Y (G)∞; these are smooth functions f : Y [3] /d47/d47 H and ψ : Y /d47/d47 H satisfying relations
(4.1.5).
– 27 –
The coherence conditions for f∞ andψ∞ [SW, Deﬁnition 2.2.1] imply the following equations of smooth
functions, expressed as pasting diagrams:
π∗
2(A,B )
π∗
23(g,ϕ) /d47/d47/d79/d79
π∗
12(g,ϕ)
π∗
3(A,B )
π∗
34(g,ϕ)
/d15/d15
π∗
1(A,B )
π∗
13(g,ϕ)④④④④④④④④
/d61/d61④④④④④④④④
π∗
123f
❈❈❈❈
/d29/d37❈❈❈❈❈❈
π∗
14(g,ϕ)
/d47/d47π∗
4(A,B )/d11/d19
π∗
134f
=
π∗
2(A,B )
π∗
24(g,ϕ)
❈❈❈❈❈❈❈❈
/d33/d33❈❈❈❈❈❈❈❈
π∗
23(g,ϕ) /d47/d47/d79/d79
π∗
12(g,ϕ)
π∗
3(A,B )
π∗
34(g,ϕ)
/d15/d15
/d121/d1
π∗
234f④④④ ④④④
④④④④
π∗
1(A,B )
π∗
14(g,ϕ)
/d47/d47/d11/d19
π∗
124f
π∗
4(A,B )
(4.1.6)
in the 2-category Z 2
Y [4] (G)∞ and
π∗
2 (A,B )
∆ ∗
22(g,ϕ)
✾✾✾✾
/d28/d28✾✾✾✾
idπ ∗
2 (A,B )
/d8/d8
π∗
2ψrrrr
/d117/d125 rrrr
π∗
1 (A,B )
(g,ϕ)
/d66/d66✆✆✆✆✆✆✆✆✆
(g,ϕ)
/d47/d47π∗
2(A,B )
∆ ∗
122f
/d11/d19
= id (g,ϕ) =
π∗
1 (A,B )
(g,ϕ)
/d28/d28✾✾✾✾✾✾✾✾✾
π∗
1(A,B )
∆ ∗
11(g,ϕ)
✆✆✆✆
/d66/d66✆✆✆✆
idπ ∗
1 (A,B ) /d45/d45
π∗
1ψ
▲▲▲▲▲▲
/d33/d41▲▲▲▲
(g,ϕ)
/d47/d47π∗
2 (A,B )
∆ ∗
112f
/d11/d19
(4.1.7)
in the 2-category Z 2
Y [2] (G)∞. We call the structure (a), (b), (c) subject to the two condition s (4.1.6)
and (4.1.6) a diﬀerential G-cocycle for the surjective submersion π :Y /d47/d47 X.
We proceed similarly with a 1-morphism ( h∞,ǫ ∞) between objects (triv ,g ∞,ψ ∞,f ∞) and
(triv′,g ′
∞,ψ ′
∞,f ′
∞) in U, and obtain:
(d) a 1-morphism ( h,φ ) := D(h∞) : ( A,B ) /d47/d47 (A′,B ′) in Z 2
Y (G)∞, i.e. a smooth function
h : Y /d47/d47 G and a 1-form φ ∈ Ω 1(Y, h) satisfying relations (4.1.3) and (4.1.4),
(e) a 2-morphism ǫ := D(ǫ) : π∗
2(h,φ ) ◦ (g,ϕ ) /d43/d51 (g′,ϕ ′) ◦π∗
1(h,φ ) in Z 2
Y [2] (G)∞, i.e. a smooth
function ǫ :Y [2] /d47/d47 H satisfying (4.1.5).
The coherence conditions of Deﬁnition [SW, Deﬁnition 2.2.2] result in th e identities
(A,B )
id
/d27/d27
∆ ∗(g,ϕ) /d47/d47
ψ
/d11/d19
(h,φ)
/d15/d15
(A,B )
(h,φ)
/d15/d15
∆ ∗ǫ✉✉✉✉✉✉
✉✉✉✉✉✉
/d118/d126 ✉✉✉✉✉
✉✉✉✉✉
(A′,B ′)
∆ ∗(g′,ϕ′)
/d47/d47 (A′,B ′)
=
(A,B ) id /d47/d47
(h,φ)
/d15/d15
(A,B )
(h,φ)
/d15/d15
id(h,φ )
✉✉✉✉✉
✉✉✉✉✉
/d118/d126 ✉✉✉✉✉✉✉✉✉✉
(A′,B ′)
∆ ∗(g′,ϕ′)
/d67/d67id /d47/d47 (A′,B ′)
ψ′
/d11/d19
(4.1.8)
– 28 –
in the 2-category Z 2
Y (G)∞ and
π∗
2(A,B )
π∗
23(g,ϕ)
/d17/d17
π∗
1 (A,B )
π∗
12(g,ϕ)
/d58/d58
π∗
13(g,ϕ) /d47/d47
f
✥✥✥✥✥✥
/d11/d19 ✥✥✥✥
π∗
1 (h,φ)
/d15/d15
π∗
3 (A,B )
π∗
3 (h,φ)
/d15/d15
π∗
13ǫsssss
sssss
/d117/d125 ssssssssss
π∗
1 (A′,B ′)
π∗
13(g′,ϕ′)
/d47/d47π∗
3 (A′,B ′)′
=
π∗
1 (A,B )
π∗
1 (h,φ)
/d15/d15
π∗
12(g,ϕ)/d47/d47π∗
2 (A,B )
π∗
2 (h,φ)
/d15/d15
π∗
12ǫ✉✉✉✉✉
✉✉✉✉✉
/d118/d126 ✉✉✉✉✉✉✉✉✉✉
π∗
23(g,ϕ)/d47/d47π∗
3(A,B )
π∗
3 (h,φ)
/d15/d15
π∗
23ǫ✉✉✉✉✉
✉✉✉✉✉
/d118/d126 ✉✉✉✉✉✉✉✉✉✉
π∗
1 (A′,B ′)
π∗
13(g′,ϕ′)
/d63/d63
f ′
/d11/d19
π∗
12(g′,ϕ′)
/d47/d47π∗
2(A′,B ′)
π∗
23(g′,ϕ′)
/d47/d47π∗
3(A′,B ′) (4.1.9)
in the 2-category Z 2
Y [3] (G)∞. The structure (d), (e) subject to the conditions (4.1.8) and (4.1 .9) is
called a 1-morphism between diﬀerential G-cocycles for the surjective submersion π.
Finally, a 2-morphism induces a 2-morphism E : (h,φ ) /d43/d51 (h′,φ ′) in Z 2
Y (G)∞, i.e. a smooth
function E : Y /d47/d47 H that satisﬁes (4.1.5), and the coherence condition of [SW, Deﬁnition 2.2.3]
infers the identity
π∗
1(A,B )
(g,ϕ) /d47/d47
π∗
1 (h′,φ′)
/d37/d37
π∗
1 (h,φ)
/d15/d15
π∗
1E/d107/d115
π∗
2(A,B )
ǫ ✈✈✈✈✈✈
✈✈✈✈✈✈
/d118/d126 ✈✈✈✈✈
✈✈✈✈✈ π∗
2 (h,φ)
/d15/d15
π∗
1(A′,B ′)
(g′,ϕ′)
/d47/d47π∗
2(A′,B ′)
=
π∗
1(A,B )
(g,ϕ) /d47/d47
π∗
1 (h′,φ′)
/d15/d15
π∗
2 (A,B )
π∗
2 (h,φ)
/d121/d121
ǫ′ ✈✈✈✈✈✈
✈✈✈✈✈✈
/d118/d126 ✈✈✈✈✈
✈✈✈✈✈ π∗
2h2
/d15/d15
π∗
2E/d107/d115
π∗
1(A′,B ′)
(g′,ϕ′)
/d47/d47π∗
2(A′,B ′)
in the 2-category Z 2
Y [2] (G)∞. Such data is called a 2-morphism between diﬀerential G-cocycles.
We have now collected, in a systematical way, objects, 1-morphism s, and 2-morphisms of a 2-
category, the 2-category of degree two diﬀerential G-cocycles, which we denote by Z 2
π(G)∞. By con-
struction we have a 2-functor
Des2
π(idBG)∞ ⊇ U
Dπ /d47/d47Z 2
π(G)∞,
and Theorem 4.1.1 implies immediately that it is an isomorphism of 2-categ ories.
Next we argue that for certain surjective submersions, the sub- 2-category U is in fact equivalent to
Des2
π(idBG)∞. These are submersions for which Y and Y [2] have contractible connected components;
we will call these two-contractible. Any good open cover gives rise to a two-contractible surjective
submersion; in particular, any surjective submersion can be reﬁne d by a two-contractible one.
Proposition 4.1.3. Let G be a Lie 2-group and let π : Y /d47/d47 M be a two-contractible surjective
submersion. Then, the inverse of the 2-functor Dπ induces an equivalence of categories:
Z 2
π(G)∞ ∼= Des2
π(idBG)∞.
Proof. By [SW09, Corollary 3.13] transport functors over contr actible manifolds are naturally equi-
valent to smooth functors. This applies to the transport functor s F (g) contained in a descent object
(triv,g,ψ,f ), and to the transport functor F (h) contained in a descent 1-morphism ( h,ǫ ). Such
natural equivalences induce a descent 1-morphism (triv ,g,ψ,f ) ∼= (triv,g ∞,ψ ′,f ′) and a descent 2-
morphism (h,ǫ ) ∼= (h∞,ǫ ′) with g∞ and h∞ smooth. Since the embedding of smooth functors into
transport functors is full, all the modiﬁcations ψ′, f ′, ǫ′ are then automatically smooth. This shows
that Des2
π(idBG)∞ is equivalent to its subcategory U. □
– 29 –
4.1.3 Explicit Local Data
In order to make the structure of the 2-category Z 2
π(G)∞ of degree two diﬀerential G-cocycles more
transparent, we shall spell out all details in case that the surject ive submersion π comes from an
open cover V = {Vi} of M . In particular, we express the diagrammatic equations above in ter ms of
actual equations, using the relation between the Lie 2-groupoid BG and the crossed module (G,H,t,α )
established in Section 3.3.
Firstly, a diﬀerential G-cocycle ((A,B ), (g,ϕ ),ψ,f ) has the following smooth functions and diﬀer-
ential forms:
(a) On every open set Vi,
ψi :Vi /d47/d47 H , Ai ∈ Ω 1(Vi, g) and Bi ∈ Ω 2(Vi, h).
(b) On every two-fold intersection Vi ∩Vj,
gij :Vi ∩Vj /d47/d47 G and ϕij ∈ Ω 1(Vi ∩Vj, h).
(c) On every three-fold intersection Vi ∩Vj ∩Vk,
fijk :Vi ∩Vj ∩Vk /d47/d47 H.
The cocycle conditions are the following:
1. Over every open set Vi,
dAi + [Ai ∧Ai] = t∗(Bi) (4.1.10)
gii = t(ψi) (4.1.11)
ϕii = −(r−1
ψi ◦αψi )∗(Ai) −ψ∗
i ¯θ.
2. Over every two-fold intersection Vi ∩Vj ,
Aj = Ad gij (Ai) −g∗
ij ¯θ −t∗(ϕij)
Bj = ( αgij )∗(Bi) −α∗(Aj ∧ϕij) − dϕij − [ϕij ∧ϕij]
1 = fijjψj =fiijαgij (ψi). (4.1.12)
3. Over every three-fold intersection Vi ∩Vj ∩Vk,
gik = t(fijk )gjkgij
Adfijk (ϕik) = ( αgjk )∗(ϕij) +ϕjk + (r−1
fijk
◦αfijk )∗(Ak) +f ∗
ijk ¯θ.
4. Over every four-fold intersection Vi ∩Vj ∩Vk ∩Vl,
fiklα(gkl,fijk ) = fijlfjkl . (4.1.13)
Additionally, the curvature of the diﬀerential cocycle is according t o Deﬁnition 3.3.5 given by
Hi := dBi +α∗(Ai ∧Bi) ∈ Ω 3(Vi, h).
– 30 –
Secondly, a 1-morphism (( h,ǫ ),φ ) between diﬀerential cocycles (( A,B ), (g,ϕ ),ψ,f ) and
((A′,B ′), (g′,ϕ ′),ψ ′,f ′) has the following structure:
(a) On every open set Vi,
hi :Vi /d47/d47 G and φi ∈ Ω 1(V, h).
(b) On every two-fold intersection Vi ∩Vj,
ǫij :Vi ∩Vj /d47/d47 H.
The following conditions have to be satisﬁed:
1. Over every open set Vi,
B′
i = ( αhi)∗(Bi) −α∗(A′
i ∧φi) − dφi − [φi ∧φi] (4.1.14)
A′
i = Ad hi(Ai) −t∗(φi) −h∗
i ¯θ (4.1.15)
ψ′
i = ǫiiα(hi,ψi). (4.1.16)
2. Over every two-fold intersection Vi ∩Vj ,
g′
ij = t(ǫij)hjgijh−1
i (4.1.17)
ϕ′
ij = Ad ǫij ((αhj )∗(ϕij) +φj) − (αg′
ij )∗(φi) − (r−1
ǫij ◦αǫij )∗(A′
j) −ǫ∗
ij ¯θ (4.1.18)
3. Over every three-fold intersection Vi ∩Vj ∩Vk,
f ′
ijk =ǫikα(hk,fijk )α(g′
ik,ǫ −1
ij )ǫ−1
jk . (4.1.19)
Finally, a 2-morphism E between diﬀerential cocycles has, for any open set Vi, a smooth function
Ei :Vi /d47/d47 H such that on every open set Vi
h′
i = t(Ei)hi
φ′
i = Ad Ei(φi) − (r−1
Ei ◦αEi)∗(A′
i) −E∗
i ¯θ
and, on every 2-fold intersection Vi ∩Vj,
ǫ′
ij =α(g′
ij,Ei)ǫijE−1
j .
Concluding this discussion we note the following normalization lemma, wh ich we need for the
discussion of surface holonomy. It can be seen as a variant of the m aybe familiar normalization result
for ˇCech cocycles.
Lemma 4.1.4. Every diﬀerential G-cocycle with respect to an open cover {Vi}i ∈I is 1-isomorphic to
a diﬀerential G-cocycle with
ψi = 1 , gii = 1 , fiij =fijj = 1 and fiji =y−1
ij α(xij,yij)
for all i,j ∈ I, and elements xij ∈ G and yij ∈ H. In particular, if G = BA for an abelian Lie group
A, then fiji = 1.
– 31 –
Proof. Suppose (( A,B ), (g,ϕ ),ψ,f ) is a diﬀerential G-cocycle with respect to {Vi}. It is easy to see
that one can always pass to a1-isomorphic cocycle with ψi = 1, gii = 1, and fiij =fijj = 1. In order to
achieve the remaining condition for fiji, we choose a total order on the index set I of the open cover,
and look at smooth maps
ǫij :=
{
1 i ≤j
fiji i>j
deﬁned on Vi ∩Vj. Then we deﬁne yet another diﬀerential G-cocycle ((A′,B ′), (g′,ϕ ′),ψ ′,f ′) via
equations (4.1.14) to (4.1.19), and it is straightforward to see that this one has the claimed form. □
4.1.4 Non-abelian Diﬀerential Cohomology
The 2-categories Z 2
π(G)∞ of degree two diﬀerential G-cocycles form a direct system for surjective
submersions over M , and so do the sets h 0(Z 2
π(G)∞) of isomorphism classes of objects.
Deﬁnition 4.1.5. The direct limit
ˆH 2(M, G) := lim− →π
h0(Z 2
π(G)∞)
is called the degree two diﬀerential non-abelian cohomology of M with values in G.
The terminology “non-abelian diﬀerential cohomology” is motivated b y the following observation.
If one drops all diﬀerential forms from the local data described in S ection 4.1.3, and only keeps the
smooth functions, the corresponding limit coincides with the non-abelian cohomology H 2(M, G), as
it appears for instance in [Gir71, Bre94, Bar04, Woc11]. Thus, Deﬁn ition 4.1.5 extends ordinary
non-abelian cohomology by diﬀerential form data.
We remark that by Lemma 4.1.4 and the fact that every surjective s ubmersion can be reﬁned by
an open cover, one can deﬁne non-abelian diﬀerential cohomology b y only using cocycles that are
normalized in the sense of Lemma 4.1.4.
Since every surjective submersion can be reﬁned to a two-contra ctible one (for example, by a good
open cover), it also suﬃces to take the limit over the two-contract ible surjective submersions. Then,
Proposition 4.1.3 and Theorem 3.2.2 imply via (4.1.1) the following classiﬁca tion result.
Theorem 4.1.6. Let G be a Lie 2-group, and let i : BG /d47/d47 T be an equivalence of 2-categories.
Then, there is a bijection
h0Trans2
Gr(M,T ) ∼= ˆH 2(M, G).
In other words, transport 2-functors on M with BG-structure are classiﬁed up to isomorphism by the
non-abelian diﬀerential cohomology of M with values in G.
Let us specify two particular examples of diﬀerential non-abelian co homology which have appeared
before in the literature:
1. The Lie 2-group G = BS1. We leave it as an easy exercise to the reader to check that our
diﬀerential non-abelian cohomology is precisely degree two Deligne co homology,
ˆH 2(M, BS1) = H 2(M, D(2)).
Deligne cohomology [Bry93] is a well-known local description of abelian g erbes with connection.
– 32 –
2. The Lie 2-group G = AUT(H) for H some ordinary Lie group H. We also leave it to the reader
to check that our diﬀerential cocycles are precisely the local desc ription of connections in non-
abelian gerbes given by Breen and Messing [BM05] (see Remark 4.1.7 be low). Thus, we have an
equality
ˆH 2(M, AUT(H)) =



Equivalence classes of local data
of Breen-Messing H-gerbes
with connection over M


 .
Summarizing, the theory of transport 2-functors covers both D eligne cocycles and Breen-Messing
cocycles.
Remark 4.1.7. We remark that condition (4.1.10) between the 1-curving A and the 2-curving B of a
diﬀerential G-cocycle is present neither in Breen-Messing gerbes [BM05] nor in t he non-abelian bundle
gerbes of [ACJ05], which we discuss in Section 4.3. Breen and Messing c all the local 2-form
t∗(Bi) − dAi − [Ai ∧Ai]
which is here zero by (4.1.10), the fake curvature of the gerbe. In this terminology, transport 2-functors
only cover Breen-Messing gerbes with vanishing fake curvature.
The crucial point is here that unlike transport 2-functors, neithe r Breen-Messing gerbes nor non-
abelian bundle gerbes have concepts of holonomy or parallel transp ort. And indeed, equation (4.1.10)
comes from an important consistency condition on this parallel tran sport, namely from the target-
source matching condition for the transport 2-functor, which ma kes it possible to decompose parallel
transport into pieces. So we understand equation (4.1.10) as an integrability condition which is neces-
sarily for a consistent parallel transport. In other words, vanish ing fake curvature is not specifying a
subclass of connections, it is a necessary condition every connection has to satisfy.
