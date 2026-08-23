---
doc_id: arxiv-0903.0853v3
doc_title: "Local analytic classification of q-difference equations"
section_id: sec-226-4-also-see-the-revised-version-extensions-panach
section_title: "Also see the revised version “Extensions panach´ ees auto duales”, to be found on"
section_number: 4
pages: 139-163
source_pdf: 0903.0853v3.pdf
source_sha256: d4295d4b18b2f08f
doc_brief: "Local analytic classification of q-difference equations — 229 sections: Vector bundles associated to q-diﬀ; The q-Euler equation and conﬂuent ; The symmetric square of the q-Eule"
---
http://www.math.jussieu.fr/ bertrand/Recherche/reche rche.html.
134APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
diagram of exact sequences:
0
/d15/d15
0
/d15/d15
0 /d47/d47P1
w2◦v−1
1 /d47/d47M2
v2 /d47/d47
w3
/d15/d15
P2 /d47/d47
w3◦(v2)−1
/d15/d15
0
0 /d47/d47P1
w3◦w2◦v−1
1 /d47/d47M can /d47/d47
v3
/d15/d15
M ′ /d47/d47
v3
/d15/d15
0
P3
/d15/d15
P3
/d15/d15
0 0
(We call can the canonical projection from M to M ′.) Conversely, starting
from such a diagram of blended extensions, we recover a representative (M,u )
of a class in F(P1,P 2,P 3) as follows. The module M is the one sitting at the
center of the diagram. The submodule M1 is the image ofP1 by the monomor-
phismw3◦w2◦v−1
1 . Then, M2 is the preimage bycan of the submodule of M ′
deﬁned as the image ofP2 byw3◦(v2)−1. Of course, M0 :={0} andM3 :=M.
The structural morphisms ui, i = 1, 2, 3, are easy to deﬁne. It can then be
proven that one thus gets a bijective mapping fromF(P1,P 2,P 3) to the set of
equivalence classes of diagrams of blended extensions. (No te however that, in
loc. cit. , D. Bertrand is interested by a slightly diﬀerent equivalence relation.)
Actually, one can even deﬁne a category on both sides of this c orrespondence
and get an equivalence of these categories, see [ 52].
A.1.2. The devissage. — Our goal is to give conditions ensuring that
F(P1,...,P k) carries the structure of an aﬃne space over C, and to compute
its dimension. The case k = 2 suggests that we should assume the C-modules
Ext(Pj,P i) to be free of ﬁnite rank. (As we shall see, the only pairs that
matter are those with i < j.) Then, aiming at an induction argument, one
invokes a natural onto mapping:
F(P1,...,P k)−→F (P1,...,P k−1),
sending the class of (M,u ) deﬁned as above to the class of (M ′,u ′) deﬁned by:
M ′ = (0 =M0⊂M1⊂···⊂ Mk−1 =M ′) and u′ = (ui)1≤i≤k−1.
A.2. DIFFERENCE MODULES OVER DIFFERENCE RINGS 135
The preimage of the class of ( M ′,u ′) described above is identiﬁed with
Ext(Pk,M ′); and note that Ext(Pk,M ′) indeed only depends (up to a canon-
ical isomorphism) on the class of ( M ′,u ′). Under the assumptions we shall
choose, we shall see that Ext( Pk,M ′) can in turn be unscrewed (d´ eviss´ e)
in the Ext(Pk,P i) for i < k, and we expect to get a space with dimension∑
1≤i<j≤k
dim Ext(Pj,P i).
Remark A.1.1 . — Once described the space F(P1,...,P k), one can ask for
the seemingly more natural problem of the classiﬁcation of t hose objects M
such that grM≃ P (without prescribing the “polarization” u). One checks
that the group∏ Aut(Pi) operates on the spaceF(P1,...,P k): actually, (φi)∈∏ Aut(Pi) acts on the “class” of all pairs ( M,u ) through left compositions
φi◦ui. Then, our new classiﬁcation comes by quotienting F(P1,...,P k) by
this action. We shall not deal with that problem.
The use of homological algebra in classiﬁcation problems fo r functional
equations is ancient, but it seems that the ﬁrst step, the alg ebraic modeli-
sation, has sometimes been tackled rather casually: for ins tance, when identi-
fying a module of extensions with a cokernel, the explicit de scription of a map
is almost always given; the proof of its bijectivity comes so metimes; the proof
of its additivity seldom; the proof of its linearity (seemin gly) never. For that
reason, very great care has been given here to detailed algeb raic constructions
and proofs of “obvious” isomorphisms.
A.2. Diﬀerence modules over diﬀerence rings
Our classiﬁcation of isograded ﬁltered diﬀerence modules ov er a diﬀerence
ﬁeld will involve an aﬃne moduli space that is actually an aﬃn e scheme. To
obtain that, we will have to consider in section A.5 a functorin commutativeC-
algebras that involves diﬀerence modules over diﬀerence rings. Thus, in order
to study this “relative” situation, we must generalize our b asic constructions
to diﬀerence rings.
A.2.1. Diﬀerence rings, diﬀerence operators. — Let K be a com-
mutative ring and σ a ring automorphism of K. As noticed in 2.1.1, most
constructions and statements about diﬀerence ﬁelds and modu les remain
valid over the diﬀerence ring (K,σ ). Our favorite examples are, of course,
(C{z},σ q), (C({z}),σ q), (C[[z]],σ q) and ( C((z)),σ q).
136APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
More precisely, we shall assume the following situation. LetC be a commu-
tative ring (we may think of the the ﬁeld C of complex numbers, or else some
arbitrary ﬁeld of “constants”). Assume that K is a commutative C-algebra
andσ aC-algebra automorphism, that is, a C-linear ring automorphism. We
shall always assume that the automorphism σ is of inﬁnite order , i.e. the iter-
ates σk, k∈ Z, are all diﬀerent. (In the case of q-diﬀerences, this means that
q is not a root of unity.) Then the ring of constants:
K σ :={x∈K| σx =x}
is actually a sub C-algebra of K. The ring of σ-diﬀerence operators is deﬁned
as the ¨Ore-Laurent ring:
DK,σ :=K <T,T −1>
with T an invertible indeterminate, subject to the twisted commut ation rela-
tions:
∀k∈ Z,∀λ∈K , Tk.λ =σk(λ)T k.
Its elements are the non commutative Laurent polynomials ∑
−∞≪k≪+∞
akT k.
The ringDK,σ is actually is a C-algebra with center K σ. As a consequence,
the category Mod DK,σ of leftDK,σ-modules is a C-linear abelian category.
Mapping the element ∑ akT k ∈ DK,σ to the C-linear endomorphism∑ akσk of K, one deﬁnes a morphism of C-algebras from DK,σ toLC(K).
The image of this morphism is the sub- C-algebraK <σ,σ −1 > generated by
K (that is, the operators of left multiplication by elements o f K),σ and σ−1.
Beware however that neither K <σ,σ −1 > norDK,σ is a K-algebra, since K
is not central in either case.
Since we have assumed that σ is of inﬁnite order, one deduces from Artin-
Dedekind’s lemma on independence of characters that, whenK is a ﬁeld (more
generally, when it is an integral ring), the morphism is inje ctive, so that we
can identify:
DK,σ =K <σ,σ −1 >.
For this reason, we shall rather sometimes write K <σ,σ −1 > forDK,σ when
no confusion thus arises, even if K is not an integral ring.
A.2.2. Diﬀerence modules over diﬀerence rings. — We are interested
in the category Mod DK,σ of leftDK,σ-modules. We shall give two alternative
A.2. DIFFERENCE MODULES OVER DIFFERENCE RINGS 137
description of these modules.
To a leftDK,σ-moduleM, we associate the pair (V, Φ), where theK-module
V is obtained from M by restriction of scalars and where Φ is the σ-linear (or
semi-linear) automorphism of V deﬁned by x↦→σ.x (external multiplication
in theDK,σ-module M). The property of σ-linearity means:
∀λ∈K ,∀x∈V , Φ(λx) =σ(λ)Φ(x).
Conversely, from such a pair ( V, Φ), we can recover M as the DK,σ-
module having V as underlying group and the external product deﬁned
by (∑ akσk).x := ∑ akΦk(x). The fact that we do get a DK,σ-module
depends on the σ-linearity of Φ. If the DK,σ-module N likewise corresponds
to the pair (W,Ψ), thenDK,σ-linear maps from M toN are exactly the same
asK-linear maps f :V →W such that Ψ◦f =f◦ Φ. The category Mod DK,σ
is therefore equivalent to the following category: objects are the pairs (V, Φ),
where V is a K -module and Φ is a σ-linear automorphism of V ; morphisms
from (V, Φ) to (W,Ψ) are K-linear maps f :V→W such that Ψ◦f =f◦ Φ.
From now on, we shall move freely from DK,σ-modules to pairs ( V, Φ) and
conversely.
For any K-module V , write σ∗V the K-module obtained by restriction
of scalars through σ : K → K. This means that, writing µ.x the external
multiplication on V , the external multiplication on σ∗V is deﬁned by the
formula: (λ,x )↦→σ(λ).x. It follows that a σ-linear automorphism Φ : V→V
is just aK-linear isomorphism fromV toσ∗V . This allows for yet another de-
scription of the category Mod DK,σ . Noting that LK(V,W ) =LK(σ∗V,σ ∗W ),
we will ﬁnd that many linear properties of DK,σ-modules (like the deﬁnition
and study of tensor products in paragraph A.2.4; or the deﬁni tion and study
of “internal Hom” in paragraph A.2.5) are then immediate con sequences of
general linear algebra over K.
From general properties of the restriction of scalars, it fo llows that a se-
quenceM ′→M→M ′′ inMod DK,σ is exact if, and only if, it is exact as a se-
quence of K-modules. However, if an exact sequence 0 →M ′→M→M ′′→
0 splits in Mod DK,σ it splits in Mod K, but not conversely. Any such exact se-
quence is isomorphic to one whereM = (V, Φ),M ′ = (V ′, Φ′),M ′′ = (V ′′, Φ′′),
where V ′ is a sub-K-module of V and Φ ′ = Φ|V , and where V ′′ = V/V ′ and
Φ′′ is induced by Φ.
138APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
Deﬁnition A.2.1 . — A diﬀerence module over the diﬀerence C-algebra
(K,σ ) (more shortly, over K) is a left DK,σ-module which, by restriction of
scalars to K, yields a ﬁnite rank projective K-module.
In our second description, this is a pair ( V, Φ) such that V is a ﬁnite rank
projective K-module. We require that the module be projective for techni cal
reasons (such that good behaviour under extension of scalar s). The ﬁniteness
condition is natural in the context of functional equations .
Example A.2.2 . — We write 1 and call unit diﬀerence module theDK,σ-
module (K,σ ). As a DK,σ-module, is isomorphic to DK,σ/DK,σ(σ− 1).
For any invertible matrixA∈ GLn(K), putting ΦA(X) :=A−1(σX), we deﬁne
a diﬀerence module ( K n, ΦA). For instance, if n = 1 and A = (1), this is 1 .
Any diﬀerence module (V, Φ) such thatV is free overK is isomorphic to some
(K n, ΦA).
We write DiffMod (K,σ ) the full subcategory of Mod DK,σ with objects
the diﬀerence modules over K. Like Mod DK,σ , it is abelian and C-linear.
Thus, monomorphisms, epimorphisms, isomorphisms and exac t sequences in
DiffMod (K,σ ) are the same thing as in Mod DK,σ . Moreover, since an exten-
sion of ﬁnite rank projective K-modules is a ﬁnite rank projective K-module
it follows thatDiffMod (K,σ ) is a thick subcategory of Mod DK,σ , so that the
calculus of extensions inDiffMod (K,σ ) is the restriction of the calculus of ex-
tensions inMod DK,σ . For instance, computing Exti(M,N ) inDiffMod (K,σ )
or in Mod DK,σ is the same.
Remark A.2.3 . — Many constructions still make sense, and many proper-
ties remain true, and moreover useful, without the projecti veness or ﬁnite-
ness conditions. For instance, one may want to consider diﬀerence exten-
sion rings of (K,σ ), that is, diﬀerence rings ( K ′,σ ′) such that K⊂ K ′ and
σ′
|K =σ; in some interesting cases, K ′ is not a ﬁnite K-module: for instance,
C({z})⊂ C((z)). We will sometimes brieﬂy mention these generalisations ,
for future reference.
A.2.3. The functor Γ. — Let M := ( V, Φ) and N := ( W,Ψ) two
diﬀerence modules. Write Lσ(V,W ) := LK(V,σ ∗W ) the K-module of σ-
linear maps from V to W . For simplicity, we shall also (improperly) write
LK(M,N ) :=LK(V,W ) andLσ(M,N ) :=Lσ(V,W ).
A.2. DIFFERENCE MODULES OVER DIFFERENCE RINGS 139
For anyK-linear map f :V →W , the map Ψ◦f−f◦ Φ is σ-linear from
V to W . The map tΦ ,Ψ :f↦→Ψ◦f−f◦ Φ fromLK(M,N ) toLσ(M,N ) is
C-linear and, by deﬁnition, Hom(M,N ) is its kernel. We thus have an exact
sequence of C-modules:
0→ Hom(M,N )→L K(M,N )
tΦ , Ψ
−→L σ(M,N ).
This sequence is clearly functorial in M and inN (contravariant inM, covari-
ant inN). We shall see later that, under appropriate assumptions, its cokernel
is the module Ext(M,N ) (theorem A.4.1).
Deﬁnition A.2.4 . — The functor Γ of solutions is deﬁned as:
M ❀ Γ(M) := Hom(1,M ).
Proposition A.2.5. — The functor M ❀ Γ(M) from diﬀerence modules to
C-modules is left exact, and one has an identiﬁcation:
Γ(M) ={v∈V | Φ(v) =v}.
Proof. — The functoriality and exactness are plain. The identiﬁca tion comes
as follows: under the usual identiﬁcation f↦→v :=f(1) ofLK(K,V ) with V ,
the condition Φ◦f =f◦σ translates into Φ(v) =v.
Thei-th right derived functor of Γ is given by:
M ❀ Γi(M) = Exti(1,M ).
Remark A.2.6 . — The contents of this paragraph remain valid without con-
ditions for allDK,σ-modules.
A.2.4. T ensor products. — Let M := (V, Φ) and N := (W,Ψ) two diﬀer-
ence modules. According to [ 11,§3, no 3], one has a canonical isomorphism:
σ∗(V⊗KW )≃σ∗V⊗Kσ∗W.
It follows that there is a unique σ-linear isomorphism:
Φ⊗ Ψ :V⊗KW→σ∗(V⊗KW )
such that x⊗y↦→Φ(x)⊗ Ψ(y). This makes the tensor product M⊗N :=
(V⊗K W,Φ⊗ Ψ) into a diﬀerence module. Note however that the result is
not a tensor product of DK,σ-modules.
140APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
Proposition A.2.7. — The tensor product in DiffMod (K,σ ) is associa-
tive, commutative, bifunctorial (covariant in each argume nt) and exact. More-
over, there are canonical isomorphisms:
1⊗M≃M≃M⊗ 1.
Proof. — This follows immediately from the corresponding propert ies for pro-
jective K-modules, with the same meaning (commutativity is understo od up
to canonical isomorphisms, etc).
Remark A.2.8 . — The contents of this paragraph remain valid without con-
ditions for allDK,σ-modules, except for the exactness in the proposition: this
remains true forK-projectiveDK,σ-modules but reduces to right exactness for
generalDK,σ-modules.
A.2.5. Internal Hom. — LetM := (V, Φ) andN := (W,Ψ) two diﬀerence
modules; thenLK(V,W ) is projective of ﬁnite rank over K. For any K-linear
map u : V → W , the map Ψ ◦u◦ Φ−1 is K-linear. The map Γ : u ↦→
Ψ◦u◦ Φ−1 fromLK(V,W ) to itself is a K-linear automorphism, whence a
diﬀerence module:
Hom(M,N ) :=
(
LK(V,W ), Γ
)
.
This is called an “internal Hom”. For instance, Hom (1,M ) is canonically
isomorphic to M.
Theorem A.2.9. — Let M := (V, Φ), M ′ := (V ′, Φ′) and N := (W,Ψ) be
three diﬀerence modules. There is a canonical functorial iso morphism:
Hom
(
M, Hom(M ′,N )
)
≃ Hom(M⊗M ′,N ).
Proof. — From [ 11,§4.1, prop. 1], we have a canonical (and functorial) iso-
morphism:
LK
(
V,LK(V ′,W )
)
≃L K(V⊗KV ′,W ),
which sends f :V →L K(V ′,W ) to the unique linear map g :V⊗KV ′→W
such that g(v⊗v′) = f(v)(v′). Conversely, g : V⊗K V ′→ W is sent to f :
V→L K(V ′,W ) deﬁned byv↦→(v′↦→g(v⊗v′)). This yields the isomorphism
of the underlying K-modules. An easy computation then shows that:
Ψ◦g =g◦ (Φ⊗ Φ′)⇐⇒Γ◦f =f◦ Φ;
withf,g and Γ deﬁned as above. Functoriality comes from the correspo nding
assertion in linear algebra.
A.2. DIFFERENCE MODULES OVER DIFFERENCE RINGS 141
Remark A.2.10 . — The contents of this paragraph remain valid without
conditions for allDK,σ-modules.
A.2.6. Duality. — We keep the same notations as in paragraph A.2.5. Ac-
cording to [ 11,§4.2], the canonical morphism:
ν :LK(V,V ′)⊗KW→L K(V,V ′⊗KW )
is a monomorphism if W is projective and an isomorphism if V or W is pro-
jective of ﬁnite rank. One checks that the following diagram is commutative:
LK(V,V ′)⊗KW
/d15/d15
ν /d47/d47LK(V,V ′⊗KW )
/d15/d15
LK(V,V ′)⊗KW ν /d47/d47LK(V,V ′⊗KW )
The left vertical map is given by: f⊗w↦→(Φ′◦f◦ Φ−1)⊗ Ψ(w), while the
right vertical map is given by: g↦→(Φ′⊗ Ψ)◦g◦ Φ−1.
Proposition A.2.11. — For any three diﬀerence modules, ν induces a
canonical and functorial isomorphism of diﬀerence modules :
Hom(M,M ′)⊗N≃ Hom(M,M ′⊗N).
Proof. — Immediate from the discussion above.
Deﬁnition A.2.12 . — The dual of the diﬀerence module M is:
M ∨ := Hom(M, 1).
If M = (V, Φ), then M ∨ = (V ∗, Φ∨), where Φ ∨(u) := σ◦u◦ Φ−1. For
instance, for A∈ GLn(K), one has (K n, ΦA)∨ = (K n,A ∨), where A∨ := tA−1
is the contragredient of A.
Corollary A.2.13 . — We have a canonical and functorial isomorphism of
diﬀerence modules:
M ∨⊗N≃ Hom(M,N ).
Proof. — Set M ′ := 1 in the proposition.
Remark A.2.14 . — Part of these conclusions stay true for more general
DK,σ-modules. In the proposition, as well as in the corollary, th e map is a
monomorphism if M is an arbitrary DK,σ-module and N is a K-projective
DK,σ-module; and an isomorphism if M orN is a diﬀerence module, the other
being an arbitraryDK,σ-module.
142APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
A.3. Finitely ﬁltered diﬀerence modules
A.3.1. Isograded classiﬁcation of diﬀerence modules. — Let (K,σ )
be a diﬀerence ring, with K is a commutative C-algebra and σ a C-algebra
automorphism. Recall from the previous section that a diﬀere nce module
overK is a leftDK,σ-module which is projective of ﬁnite rank as a K-module
and that the category DiffMod (K,σ ) of diﬀerence modules is abelian and
C-linear. Diﬀerence modules over K can be realized as pairs (E, Φ), where E
is a projective K-module of ﬁnite rank and Φ is a semi-linear automorphism
of E. In this description, a morphism of diﬀerence modules from ( E, Φ) to
(F, Ψ) is a map u∈L K(E,F ) such that Ψ◦u =u◦ Φ.
As an instance of the general problem considered in section A .1, we ﬁx
diﬀerence modules Pi (1 ≤ i ≤ k) and consider ﬁnitely ﬁltered diﬀerence
modules M
with associated graded module P = P1⊕···⊕ Pk. We assume
that each such object M = (0 =M0⊂M1⊂···⊂ Mk =M) comes equipped
with an isomorphism u = (ui :Mi/Mi−1≃Pi)1≤i≤k from grM to P .
In accordance with the general problem described in section A.1, we
consider (M,u ) and ( M ′,u ′) to be equivalent if there exists a morphism
f :M→M ′ that respects the ﬁltration: f(Mi)⊂M ′
i for 1≤i≤k, and such
that, writing gi :Mi/Mi−1→M ′
i/M′
i−1 the morphisms thus induced by f|Mi,
one hasui =u′
i◦gi for 1≤i≤k. Since f respects the ﬁltration, one can deﬁne
grf : grM→ grM ′ and the above condition is equivalent tou
= grf◦u′. It is a
standard fact (and easy to prove) thatf is then automatically an isomorphism.
Our goal is to classify such pairs (M,u ) up to this equivalence relation. The
equivalence classes clearly form a set, which we write F(P1,...,P k). In this
section, we give some matricial descriptions, under additi onal assumptions.
A.3.2. Matricial description of diﬀerence modules. — Here, we
assume that the K-module E is free of ﬁnite rank n. This assumption will
be maintained in A.3.3 and A.4.2, where we pursue the matrici al description.
We then see that the diﬀerence module M = (E, Φ) is then isomorphic to
some (K n, ΦA) (example A.2.2). Indeed, choosing a basis B allows one to
identify E with K n. It is then clear that Φ( B) is also a basis of E, whence
the existence of A∈ GLn(K) such that Φ(B) = BA−1. If x∈ E has the
coordinate column vector X ∈ K n in basis B, i.e. if x =BX, computing
Φ(x) = Φ(BX) = Φ(B)σ(X) = BA−1σ(X) shows that Φ( x)∈ E has the
A.3. FINITELY FILTERED DIFFERENCE MODULES 143
coordinate column vector A−1σ(X); we thus may identify (E, Φ)≃ (K n, ΦA),
where ΦA(X) :=A−1σ(X).
Morphisms from (K n, ΦA) to (K p, ΦB) are matrices F ∈ Matp,n(K) such
that (σF )A = BF and their composition boils down to matrix product. In
particular, isomorphism of modules is described by gauge tr ansformations:
(K n, ΦA)≃ (K p, ΦB)⇐⇒n =p and∃F∈GLn(K) : B =F[A] := (σF )AF −1.
Remark A.3.1 . — A similar description can be given for free modules of
inﬁnite rank. Such a K-module is isomorphic to K (I), and one should replace
GLn(K) by GL I(K) and Mat p,n(K) by Mat J×I(K). Inﬁnite “matrices” are
to be understood as follows: elements of End K(K (I)) are families ( ai,j) of
elements ofK indexed byI×I and such that each column (j ﬁxed) has ﬁnite
support. The set Mat I(K) := End K(K (I)) is a unitary ring and GL I(K) :=
AutK(K (I)) is its group of units. There is a similar condition for Mat J×I(K).
A.3.3. Matricial description of ﬁltered diﬀerence modules. — Let
Pi = (Gi, Ψi) (1≤i≤k) be diﬀerence modules such that eachK-moduleGi is
free of ﬁnite rank ri . For each Gi, choose a basisDi, and write Bi∈GLri(K)
the invertible matrix such that Ψ i(Di) =DiBi.
LetM be a ﬁnitely ﬁltered diﬀerence module with associated gradedmodule
P =P1⊕···⊕ Pk; more precisely, M = (0 = M0⊂M1⊂···⊂ Mk =M) is
equipped with an isomorphism u = (ui :Mi/Mi−1≃Pi)1≤i≤k from grM toP .
LettingMi = (Ei, Φi), one builds a basisBi ofEi by induction on i = 1,...,k
in such a way thatBi−1⊂B i and thatB′
i :=Bi\B i−1 liftsDi viaui (showing
by the way that K-modules Ei are free of ﬁnite ranks r1 +··· +ri). Write
Φi (resp. Φi) the semi-linear automorphism induced by Φ (resp. by Φ i) on
Ei (resp. on Ei/Ei−1), andCi the basis of Ei/Ei−1 induced byB′
i, one draws
from equality ui◦ Φi = Ψ i◦ui (due to the fact that ui is a morphism) the
relation: Φi(Ci) =CiBi, then, from the latter, the relation:
Φi(B′
i)≡B ′
iBi (mod Ei−1).
Last, one gets that the matrix of Φ in basis B is block upper-triangular:
Φ(B) =B



B1 ⋆ ⋆
0 ... ⋆
0 0 Bk


.
144APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
As in A.3.2, we identify Pi (1≤ i≤ k) with (K ri, ΦAi), where Ai := B−1
i ∈
GLri(K). Likewise, P is identiﬁed with ( K n, ΦA0) and M with (K n, ΦA),
where n :=r1 +··· +rk and:
A0 =



A1 0 0
0 ... 0
0 0 Ak


 et A =



A1 ⋆ ⋆
0 ... ⋆
0 0 Ak


.
Note that these relations implicitly presuppose that a ﬁltration onM is given,
as well as an isomorphism from gr M to P . If moreover M ′ = (K n, ΦA′),
where A′ has the same form as A (i.e. M ′ is ﬁltered and equipped with an
isomorphism from grM ′ to P ), then, a morphism from M to M ′ respecting
ﬁltrations ( i.e. sending each Mi into M ′
i) is described by a matrix F in the
following block upper triangular form; and the induced endo morphism ofP≃
grM≃ grM ′ is described by the corresponding block diagonal matrix F0
F =



F1 ⋆ ⋆
0 ... ⋆
0 0 Fk


 et F0 =



F1 0 0
0 ... 0
0 0 Fk


.
In particular, a morphism inducing identity on P (thus ensuring that the ﬁl-
tered modulesM,M ′ belong to the same class inF(P1,...,P k)) is represented
by a matrix in G(K), where we denote G the algebraic subgroup of GLn de-
ﬁned by the following shape:



Ir1 ⋆ ⋆
0 ... ⋆
0 0 Irk


.
(The unipotent algebraic group G was previously introduced in paragraph
2.3.3, page 26.)
Now write AU the block upper triangular matrix with block diagonal com-
ponent A0 and with upper triangular blocks the Ui,j∈ Matri,rj(K) (1≤ i <
j≤k); here, U is an abrevation for the family ( Ui,j). For all F∈ G(K), the
matrix F[AU] is equal to AV for some family of Vi,j∈ Matri,rj(K). Thus, the
group G(K) operates on the set ∏
1≤i<j≤k
Matri,rj(K). The above discussion
can be summarised as follows:
A.4. EXTENSIONS OF DIFFERENCE MODULES 145
Proposition A.3.2. — The map sending U to the class of (K n, ΦAU ) induces
a bijection from the quotient of the set ∏
1≤i<j≤k
Matri,rj(K) under the action
of the group G(K) onto the set F(P1,...,P k).
Remark A.3.3 . — The point of the above trivial and rather long construc-
tion of triangular matrices is not so much that adequate base s exist, but that,
by choosing such triangular forms, one implicitly ﬁxes the s tructural isomor-
phisms Mi/Mi−1≃Pi.
A.4. Extensions of diﬀerence modules
Let 0→M ′→M→M ′′→ 0 an exact sequence inMod DK,σ . If M ′,M ′′ are
diﬀerence modules, so is M (it is projective of ﬁnite rank because we have a
split sequence ofK-modules). The calculus of extensions is therefore the same
inDiffMod (K,σ ) as in Mod DK,σ and we will simply write Ext(M ′′,M ′) the
group Ext DK,σ (M ′′,M ′) of classes of extensions of M ′′ by M ′. From general
homological algebra, we know that Ext( M ′′,M ′) is actually endowed with
a structure of C-module, whence a C-module structure on F(M ′,M ′′) (as
noted at the beginning of section A.1.1).
On the other hand, if M ′, M ′′ are free over K of respective ranks n′,
n′′, proposition A.3.2 of the previous section allows for a desc ription of
F(M ′,M ′′) as a quotient of the space Matn′,n′′(K) by aC-linear group action.
This also provides a C-module structure on F(M ′,M ′′). We shall show in
this section that these structures actually coincide. For a ny two left modules
M ′,M ′′ over a unitaryC-algebra, the linear structure on Ext(M ′′,M ′) is com-
pletely described in [ 12,§7] (5) and we shall rely on this description to make
explicit the corresponding structure of C-module of F(M ′,M ′′) in the case
of arbitrary diﬀerence modulesM ′ andM ′′. The main result is theorem A.4.1.
So let M = (E, Φ) and N = (F, Ψ). Any extension 0 →N→R→M→ 0
of M by N gives rise (by restriction of scalars) to an exact sequence o f K-
modules 0→F→G→E→ 0 such that, ifR = (G, Γ), the following diagram
5. And, to the best of our knowledge, nowhere else.
146APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
is commutative:
0 −−−−→F i−−−−→G
j
−−−−→E −−−−→0

↓ Ψ


↓ Γ


↓ Φ
0 −−−−→F i−−−−→G
j
−−−−→E −−−−→0
(We wrote againi,j the underlyingK-linear maps.) Since E is projective, the
sequence is split and one can from start identify G with theK-module F×E,
thus writing i(y) = ( y, 0) and j(y,x ) = x. The compatibility conditions
Γ◦i =i◦ Ψ and Φ◦j =j◦ Γ then imply:
Γ(y,x ) = Γu(y,x ) :=
(
Ψ(y) +u(x), Φ(x)
)
, with u∈L σ(E,F ),
where we writeLσ(E,F ) the set of σ-linear maps from E to F. (This means
that u is a group morphism such that u(λx) = σ(λ)u(x).) Setting moreover
Ru := (F×E, Γu), which is a diﬀerence module naturally equipped with a
structure of extension of M by N, we see that we have deﬁned a surjective
map:
Lσ(E,F )→ Ext(M,N ),
u↦→θu := class of Ru.
We can make precise the conditions under which u,v ∈L σ(E,F ) have the
same image θu = θv, i.e. under which Ru and Rv are equivalent extensions.
This happens if there exists a morphism φ : Ru→ Rv inducing the identity
map on M and N, that is, a linear map φ : F×E → F×E such that
Γv◦φ =φ◦ Γu (since it is a morphism of diﬀerence modules) and having the
form (x,y )↦→
(
y +f(x),x
)
(since it induces the identity maps on E and on
F). Now, the ﬁrst condition becomes:
∀(y,x )∈F×E ,
(
Ψ(y +f(x)) +v(x), Φ(x)
)
=
(
Ψ(y) +u(x) +f(Φ(x)), Φ(x)
)
,
that is:
u−v = Ψ◦f−f◦ Φ.
Remark by the way that, for allf∈L K(E,F ), the maptΦ ,Ψ (f) := Ψ◦f−f◦Φ
is σ-linear from E to F.
Theorem A.4.1. — The map u↦→θu fromLσ(E,F ) to Ext (M,N ) is func-
torial in M and in N , C-linear, and its kernel is the image of the C-linear
map:
tΦ ,Ψ :LK(E,F )→L σ(E,F ),
f↦→Ψ◦f−f◦ Φ.
A.4. EXTENSIONS OF DIFFERENCE MODULES 147
Proof. — Functoriality.
We shall only prove (and use) it on the covariant side, i.e. in N. We invoke
[12,§7.1 p. 114, example 3 and §7.4, p. 119, prop. 4]. Let θ be the class
in Ext(M,N ) of the extension 0 i→ N → R
j
→ M → 0 and g : N → N ′ a
morphism in DiffMod (K,σ ). Let
0 −−−−→N i−−−−→R
j
−−−−→M −−−−→0

↓ g


↓ h


↓ IdM
0 −−−−→N ′ i′
−−−−→R′ j′
−−−−→M −−−−→0
be a commutative diagram of exact sequences. If θ′ is the class in Ext(M,N )
of the extension 0 i′
→N ′→R′ j′
→M→ 0, then:
Ext(IdM,g )(θ) =g◦θ =θ′◦ IdM =θ′.
We take:
R′ :=R⊕N N ′ = R×N ′
{
(
i(n),−g(n)
)
| n∈N},
with i′,j ′ the obvious arrows, and for R the extension Ru; with the previous
notations for N,M,R , and also writing N ′ = (F ′, Ψ′), with compatibility
condition Ψ′◦g =g◦ Ψ, we see that the K-module underlying R⊕N N ′ is:
G′ := F×E×F ′
{
(
y, 0,−g(y)
)
| y∈F},
endowed with the semi-linear automorphism induced by the map Γu×Ψ′ from
F×E×F ′ to itself (the latter does ﬁx the denominator).
The map (y,x,y ′)↦→
(
y′ +g(y),x
)
from F×E×F ′ to F ′×E induces an
isomorphism from G′ to F ′×E and the induced semi-linear automorphism
on G′ is (y′,x )↦→
(
Ψ′(y′) +g
(
u(x)
)
, Φ(x)
)
, that is Γ gu, from which it follows
that R′ = Rgu. The arrows i′,j ′ are determined as follows: i′(y′) is the
class of (0,y ′) in G′, that is, under the previous identiﬁcation, i′(y′) = (y′, 0);
and j′(y′,x ) is the image of an arbitrary preimage, for instance the clas s of
(0,x,y ′): that image is j(0,x ) =x. We have therefore shown that the class of
the extension Ru by Ext(IdM,g ) is Rgu, which is the wanted functoriality. It
is expressed by the commutativity of the following diagram:
Lσ(E,F ) −−−−→Ext(M,N )

↓ Lσ (IdM ,g)


↓ Ext(IdM ,g)
Lσ(E,F ′) −−−−→Ext(M,N ′)
148APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
Linearity.
According to the remark just before the theorem, the map tΦ ,Ψ indeed sends
LK(E,F ) toLσ(E,F ).
Addition. The reference here is [12,§7.6, rem. 2 p. 124]. From the extensions
0 → N i→ R
p
→ M → 0 and 0 → N i′
→ R′ p′
→ M → 0 having classes
θ,θ ′∈ Ext1(M,N ), one computes θ +θ′ as the class of the extension 0 →
N i′′
→R′′ p′′
→M→ 0, where:
R′′ :={(z,z ′)∈R×R′| p(z) =p′(z′)}
{(−i(y),i ′(y))| y∈N} ,
andi′′(y) is the class of (0,i ′(y)), i.e. the same as the class of (i(y), 0); and p′′
sends the class of ( z,z ′) to p(z) = p′(z′). Taking R = Ru and R′ = Ru′, the
numerator of R′′ is identiﬁed with F×F×E equipped with the semi-linear
automorphism (y,y ′,x )↦→(Ψ(y)+u(x), Ψ(y′)+u′(x), Φ(x)). The denominator
is identiﬁed with the subspace{(−y,y, 0)|y∈F} equipped with the induced
map. The quotient is identiﬁed with 0 ×F×E, through the map (y,y ′,x )↦→
(0,y ′′,x ), where y′′ :=y′ +y, equipped with the semi-linear automorphism Φ ′′
which sends (0,y ′′,x ) to
(0, Ψ(y′) +u′(x) + Ψ(y) +u(x), Φ(x)) = (0, Ψ(y′′) + (u +u′)(x), Φ(x)).
This is indeed Ru+u′.
External multiplication. The reference here is [ 12, §7.6, prop. 4 p. 119].
Let λ∈ C. We apply the invoked proposition to the following commutat ive
diagram of exact sequences:
0 −−−−→N −−−−→Ru −−−−→M −−−−→0

↓ ×λ


↓ (×λ,IdM )


↓ IdM
0 −−−−→N −−−−→Rλu −−−−→M −−−−→0
Ifθ,θ′ are the classes in Ext(M,N ) of the two extensions, one infers from loc.
cit. that:
θ′◦ IdM = (×λ)◦θ =⇒θ′ =λθ.
The class of the extension Rλu is therefore indeed equal to the product of λ
by the class of the extension Ru.
Exactness.
It follows immediately from the computation shown just befo re the statement
of the theorem.
A.4. EXTENSIONS OF DIFFERENCE MODULES 149
A.4.1. The complex of solutions. — The following is sometimes consid-
ered as a diﬀerence analog of the de Rham complex in one variabl e, see for
instance [2, 54 ].
Deﬁnition A.4.2 . — We call complex of solutions of M in N the following
complex of C-modules:
tΦ ,Ψ :LK(E,F )→L σ(E,F ),
f↦→Ψ◦f−f◦ Φ.
concentrated in degrees 0 and 1.
It is indeed clear that the source and target are C-modules, that the map
tΦ ,Ψ does send the source to the target and that it is C-linear.
Corollary A.4.3 . — The homology of the complex of solutions is H 0 =
Hom(M,N ) and H 1 = Ext(M,N ), and these equalities are functorial.
Proof. — The statement about H 1 is the theorem. As regards H 0, the kernel
oftΦ ,Ψ is the C-module{f∈L K(E,F )| Ψ◦f =f◦ Φ}, that is, Hom(M,N );
and functoriality is obvious in that case.
Corollary A.4.4 . — From the exact sequence 0→N ′→N→N ′′→ 0, one
deduces the “cohomology long exact sequence”:
0→ Hom(M,N ′)→Hom(M,N )→ Hom(M,N ′′)
→ Ext(M,N ′)→ Ext(M,N )→ Ext(M,N ′′)→ 0.
Proof. — We keep the previous notations (and moreover adapt them to
N ′,N ′′). The exact sequence of projective K-modules 0→F ′→F→F ′′→ 0
being split, both lines of the commutative diagram:
0 −−−−→ LK(E,F ′)−−−−→ LK(E,F ) −−−−→ LK(E,F ′′) −−−−→0

↓ tΦ , Ψ ′


↓ tΦ , Ψ


↓ tΦ , Ψ ′′
0 −−−−→ Lσ(E,F ′) −−−−→ Lσ(E,F ) −−−−→ Lσ(E,F ′′) −−−−→0
are exact, and it is enough to call to the snake lemma.
A.4.2. Matricial description of extensions of diﬀerence modules. —
We now assumeE,F to be free of ﬁnite rank over K and accordingly identify
them with M = (K m, ΦA), A∈ GLm(K) and N = (K n, ΦB), B∈ GLn(K).
An extension of N by M then takes the form R = ( K m+n, ΦC), where
C =
( A U
0n,m B
)
for some rectangular matrix U∈ Matm,n(K); we shall write
150APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
C =CU. The injection M→R and the projection R→N have as respective
matrices
(Im
0n,m
)
and
(
0n,m In
)
. The extension thus deﬁned will be denoted
RU.
A morphism of extensions RU → RV is a matrix of the form F =(Im X
0n,m In
)
for some rectangular matrix X∈ Matm,n(K). The compatibility
condition with the semi-linear automorphisms writes:
(σF )CU =CVF⇐⇒U + (σX)B =AX +V⇐⇒V−U = (σX)B−AX.
Corollary A.4.5 . — TheC-module Ext1(N,M ) is thereby identiﬁed with the
cokernel of the endomorphism X↦→(σX)B−AX of Mat m,n(K).
Proof. — The above construction provides us with a bijection, but i t follows
from theorem A.4.1 that it is indeed an isomorphism.
By taking m = n = 1, and A := (1), B := (cz), we recover example 3.3.2
page 38. Letting c := 1 yields the case that was studied in paragraph 2.3.1.
A.5. Extension of scalars
We want to seeF(P1,...,P k) as a scheme overC, that is as a representable
functor C ′ ❀F(C ′⊗C P1,...,C ′⊗C Pk) from commutative C-algebras to
sets. To that end, we shall extend what we did to a “relative” s ituation.
LetC ′ be a commutative C-algebra. We set:
K ′ :=C ′⊗CK and σ′ := 1⊗Cσ.
Then K ′ is a commutative C ′-algebra and σ′ an automorphism of that C ′-
algebra. Moreover:
DK ′,σ′ :=K ′<σ ′,σ ′−1 >=K ′⊗KDK,σ =C ′⊗CDK,σ.
These equalities should be interpreted as natural (functor ial) isomorphisms.
From any diﬀerence module M = (E, Φ) over (K,σ ), one gets a diﬀerence
module M ′ = (E′, Φ′) over (K ′,σ ′) by putting:
E′ =K ′⊗KE =C ′⊗CE and Φ′ =σ′⊗K Φ = 1⊗C Φ.
A.5. EXTENSION OF SCALARS 151
(This is indeed a leftDK ′,σ′-module and it is projective of ﬁnite rank overK ′.)
We shall write it M ′ = C ′⊗k M to emphasize the dependency on C ′. The
following proposition is the tool to tackle the case k = 2.
Proposition A.5.1. — LetM,N be two diﬀerence modules over (K,σ ). One
has a functorial isomorphism of C ′-modules:
ExtDK′,σ ′(C ′⊗CM,C ′⊗CN)≃C ′⊗C ExtDK,σ (M,N ),
and a functorial epimorphism of C ′-modules:
C ′⊗C HomDK,σ (M,N )→ HomDK′,σ ′(C ′⊗CM,C ′⊗CN).
Proof. — We shall write M ′ =C ′⊗CM, E′ =K ′⊗KE etc. The K-modules
E,F beeing projective of ﬁnite rank, there are natural isomorph isms:
C ′⊗CLK(E,F ) =LK ′(E′,F ′) et C ′⊗CLσ(E,F ) =Lσ′(E′,F ′).
(This is immediate ifE andF are free, the general case follows.) By tensoring
the (functorial) exact sequence:
0→ HomDK,σ (M,N )→L K(E,F )→L σ(E,F )→ ExtDK,σ (M,N )→ 0,
we get the exact sequence:
C ′⊗CHomDK,σ (M,N )→C ′⊗CLK(E,F )→C ′⊗CLσ(E,F )→C ′⊗CExtDK,σ (M,N )→ 0.
Both conclusions then come by comparison with the exact sequ ence:
0→ HomDK′,σ ′(M ′,N ′)→L K ′(E′,F ′)→L σ′(E′,F ′)→ ExtDK′,σ ′(M ′,N ′)→ 0.
Proposition A.5.2. — Let 0 =M0⊂M1⊂···⊂ Mk =M be a k-ﬁltration
with associated graded module P1⊕···⊕ Pk. Then, setting M ′
i := C ′⊗C Mi
andP ′
i :=C ′⊗CPi, we get a k-ﬁltration 0 =M ′
0⊂M ′
1⊂···⊂ M ′
k =M ′ with
associated graded module P ′
1⊕···⊕ P ′
k.
Proof. — The Pi being projective as K-modules, the exact sequences 0 →
Mi−1→Mi→Pi→ 0 areK-split, so they give rise by the base change K ′⊗K
to exact sequences 0→M ′
i−1→M ′
i→P ′
i→ 0.
If (M,u ) denotes the pair made up of the above k-ﬁltered object and of a
ﬁxed isomorphism from grM toP1⊕···⊕ Pk, we shall write (C ′⊗CM, 1⊗Cu)
the corresponding pair deduced from the proposition.
152APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
Deﬁnition A.5.3 . — We deﬁne as follows a functor F from the category
of commutative C-algebras to the category of sets. For any commutative C-
algebra C ′, we set:
F(C ′) :=F(C ′⊗CP1,...,C ′⊗CPk).
For any morphism C ′→ C ′′ of commutative C-algebras, the map F(C ′)→
F(C ′′) is given by:
class of (M ′,u ′)↦→class of (C ′′⊗k′M ′, 1⊗Cu′).
The set F(C ′) is well deﬁned according to the previous constructions. Th e
map F(C ′)→ F(C ′′) is well deﬁned on pairs thanks to the proposition, and
the reader will check that it goes to the quotient. Last, the f unctoriality
(preservation of the composition of morphisms) comes from t he contraction
rule of tensor products:
C ′′′⊗C′′ (C ′′⊗C′M ′) =C ′′′⊗C′M ′.
A.6. Our moduli space
To simplify, herebelow, instead of saying “the functor F is represented by
an aﬃne space over C (with dimension d)”, we shall say “the functor F is an
aﬃne space over C (with dimension d)”. This is just the usual identiﬁcation
of a scheme with the space it represents.
Theorem A.6.1. — Assume that, for 1≤i<j ≤k, one has Hom (Pj,P i) =
0 and that the C-module Ext(Pj,P i) is free of ﬁnite rank δi,j. Then the functor
C ′ ❀ F(C ′) := F(C ′⊗C P1,...,C ′⊗C Pk) is an aﬃne space over C with
dimension ∑
1≤i<j≤k
δi,j.
Proof. — When k = 1, it is trivial. When k = 2, writingV the freeC-module
of ﬁnite rank Ext(P2,P 1), and appealing to proposition A.5.1, we see that this
is the functor C ′ ❀ C ′⊗C V , which is represented by the symetric algebra
of the dual of V , an algebra of polynomials over C. For k≥ 3, we use an
induction based on a lemma of Babbitt and Varadarajan [ 3, lemma 2.5.3, p.
139]:
Lemma A.6.2 . — Let u : F → G be a natural transformation between two
functors from commutative C-algebras to sets. Assume that G is an aﬃne
space over C and that, for any commutative C-algebra C ′, and for any b∈
A.6. OUR MODULI SPACE 153
G(C ′), the following functor “ﬁber above b” from commutative C ′-algebras to
sets:
C ′′ ❀u−1
C′′
(
G(C ′→C ′′)(b)
)
is an aﬃne space over C ′. Then F is an aﬃne space over C.
In loc. cit. , this theorem is proved for C = C, but the argument is plainly
valid for any commutative ring. Here is its skeleton. ChooseB =C[T1,...,T d]
representing G. Take for b the identity of G(B) = Hom( B,B ) (“general
point”); the ﬁber is represented by B[S1,...,S e]. One then shows that
C[T1,...,T d,S 1,...,S e] represents F. This gives by the way a computation
of dimF as dimG + dim of the general ﬁber. In our case, all ﬁbers will have
the same dimension.
On our way to the proof of theorem A.6.1, we shall now have a clo ser look
at these ﬁbers.
A.6.1. Structure of the ﬁbers. — Before going to the proof of the theo-
rem, we need an auxiliary result. Remember that, all along, w e assume that
Hom(Pj,P i) = 0 for 1≤i<j ≤k.
Proposition A.6.3. — Let C ′ be a commutative C-algebra and let M ′ be
a diﬀerence module over K ′ := C ′⊗C K, equipped with a (k− 1)-ﬁltration:
0 = M ′
0 ⊂ M ′
1 ⊂ ··· ⊂M ′
k−1 = M ′ such that gr M ′ ≃ P ′
1⊕···⊕ P ′
k−1
(as usual, P ′
i := C ′⊗C Pi). Then the functor in commutative C ′-algebras
C ′′ ❀ Ext(C ′′⊗C Pk,C ′′⊗C′ M ′) is an aﬃne space over C ′ with dimension∑
1≤i≤k
δi,k.
Proof. — After proposition A.5.1, this is the functor C ′′ ❀ C ′′ ⊗C′
Ext(P ′
k,M ′). From each exact sequence 0 → M ′
i−1 → M ′
i → P ′
i → 0
one draws the cohomology long exact sequence of corollary A. 4.4; but, from
proposition A.5.1, one draws that, for any commutativeC-algebraC ′, one has
Hom(C ′⊗CPj,C ′⊗CPi) = 0 and that the C ′-module Ext(C ′⊗CPj,C ′⊗CPi)
is free of ﬁnite rank δi,j. According to the equalities Hom( P ′
j,P ′
i ) = 0, the
long exact sequence is here shortened as:
0→ Ext(P ′
k,M ′
i−1)→ Ext(P ′
k,M ′
i)→ Ext(P ′
k,P ′
i )→ 0,
154APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
and, for i = 1,...,k − 1, these sequences are split, the term at the right being
free. So, in the end:
Ext(P ′
k,M ′)≃
⨁
1≤i≤k
Ext(P ′
k,P ′
i),
which is free of rank ∑
1≤i≤k
δi,k. As in the case k = 2 (which is a particular
case of the proposition), the functor mentioned is represen ted by the symetric
algebra of the dual of this module.
For allℓ such that 1≤ℓ≤k, let us write:
Vℓ :=
⨁
1≤i≤ℓ
Ext(Pℓ,P i),
Wℓ :=
⨁
1≤i<j≤ℓ
Ext(Pj,P i),
V ′
ℓ :=
⨁
1≤i≤ℓ
Ext(P ′
ℓ,P ′
i),
W ′
ℓ :=
⨁
1≤i<j≤ℓ
Ext(P ′
j,P ′
i).
We considerVℓ,W ℓ as aﬃne schemes overC andV ′
ℓ,W ′
ℓ as aﬃne schemes over
C ′, so that:
V ′
ℓ =C ′⊗CVℓ, W ′
ℓ =C ′⊗CWℓ.
We improperly writeC ′⊗CV the base change of aﬃne schemes SpecC ′⊗Spec C
V . Also, we do not distinguish between the direct sums of the fr eeC-modules
Ext(Pj,P i) and the product of the corresponding aﬃne schemes. Note that, in
the proof of the proposition, the isomorphism Ext( P ′
k,M ′)≃V ′
ℓ is functorial
in C ′. This entails:
Corollary A.6.4 . — Each ﬁber Ext (P ′
k,M ′) is isomorphic to V ′
k as a scheme
over C ′.
A.6.2. End of the proof of theorem A.6.1. — Now we end the proof of
the theorem. Besides functor F(C ′), we consider the functor C ′ ❀ G(C ′) :=
F(C ′⊗CP1,...,C ′⊗CPk−1), of which we assume, by induction, that it is an
aﬃne space of dimension ∑
1≤i<j≤k−1
δi,j. The natural transformation from F
to G is the one described in A.1.2. An element b∈ G(C ′) is the class of a
pair (M ′,u ′), a (k− 1)-ﬁltered object over C ′, and the corresponding ﬁber is
the one studied in the above auxiliary proposition A.6.3. Th e lemma A.6.2 of
Babbitt and Varadarajan then allows us to conclude.
A.7. EXTENSION CLASSES OF DIFFERENCE MODULES 155
Looking at the proof of A.6.2, one moreover sees that, if all ﬁ bers of u :
F→ G are isomorphic to a same aﬃne space V (up to obvious extension of
the base), then there is an isomorphism F≃V×CG such that u corresponds
to the second projection. With the previous notations, we se e that, writing
Fℓ the functor C ′ ❀ F(C ′⊗C P1,...,C ′⊗C Pℓ), corollary A.6.3 gives an
isomorphism of schemes:
Fℓ≃F ℓ−1×Vℓ.
By induction, we conclude:
Corollary A.6.5 . — The functor in C-algebrasC ′ ❀F(C ′⊗CP1,...,C ′⊗C
Pk) is isomorphic to the functor C ′ ❀⨁
1≤i<j≤ℓ Ext(C ′⊗CPk,C ′⊗CPi). That
is, we have an isomorphism of aﬃne schemes over C:
F(P1,...,P k)≃
∏
1≤i<j≤ℓ
Ext(Pk,P i).
A.7. Extension classes of diﬀerence modules
We shall now describe more precisely extension spaces in the case of a
diﬀerence ﬁeld (K,σ ). We keep all the previous notations. Our main tools
are theorem A.4.1 and its corollaries A.4.3 and A.4.5. We sha ll give more
“computational” variants of these results.
We use the cyclic vector lemma (lemma 2.1.1): the proof givenin [17] is valid
for general diﬀerence modules, under the assumption that the characteristic of
K is 0 and thatσ is not of ﬁnite order (e.g.q is not a root of unity). Although
most of what follows remains true for D-modules of arbitrary length (because
D is principal [ 12]), the proofs, inspired by [ 46, II.1.3], are easier for D/DP .
Recall that, the center ofD being C, all functors considered here are C-linear
and produce C-vector spaces. For a diﬀerence module M = (E, Φ), we still
write E the C-vector space underlying E.
Proposition A.7.1. — Let M := D/DP and N := (F, Ψ) two diﬀerence
modules. Then Ext i(M,N ) = 0 for i≥ 2 and there is an exact sequence of
C-vector spaces:
0→ Hom(M,N )→F
P (Ψ)
−→F→ Ext1(M,N )→ 0.
Proof. — From the presentation (in the category of left D-modules):
D ×P→D→ M→ 0,
156APPENDIX A. CLASSIFICATION OF ISOGRADED FILTERED DIFFEREN CE MODULES
one draws the long exact sequence:
0→ Hom(M,N )→Hom(D,N )→ Hom(D,N )
→ Ext1(M,N )→ Ext1(D,N )→ Ext1(D,N )→···
···→ Exti(M,N )→ Exti(D,N )→ Exti(D,N )→···
SinceD is free, Ext i(D,N ) = 0 for i≥ 1 and the portion Ext i−1(D,N )→
Exti(M,N )→ Exti(D,N ) of the long exact sequence gives the ﬁrst conclusion.
We are left to identify the portion Hom(D,M )→ Hom(D,M ). Of course,
x↦→λx :=
(
Q↦→Q.x =Q(Ψ)(x)
)
and f↦→f(1)
are isomorphisms from M to Hom(D,M ) and return reciprocal to each other.
Then, the map to be identiﬁed is f↦→f◦ (×P ), where, of course,×P denotes
the map Q↦→QP . Conjugating it with our isomorphisms yields x↦→
(
λx◦
(×P )
)
(1) = (P.1)(Ψ)(x), that is, P (Ψ).
Remark A.7.2 . — The complex F
P (Ψ)
−→ F (in degrees 0 and 1) thus has
cohomology Hom(M,N ), Ext1(M,N ). This is clearly functorial in N. On the
other hand, there is a part of arbitrariness in the choice of P , but, after [ 12]
§6.1, the homotopy class of the complex depends on M alone.
Corollary A.7.3 . — LetM = (E, Φ). The complex of solutions of M :
E Φ −Id−→E
has cohomology Γ(M), Γ1(M).
Proof. — In the proposition, take M := 1, P :=σq− 1 and N := (E, Φ).
Note that this is functorial in M.
Remark A.7.4 . — Applying the corollary to M ∨⊗N implies that the map
f↦→Ψ◦f◦ Φ−1−f has kernel Hom(M,N ) (which is obvious) and that its
cokernel is in one-to-one correspondance with Ext 1(M,N ), which is similar
to the conclusion of theorem A.4.1. However, in this way, we d o not get the
identiﬁcation of the operations on extensions: this would b e possible using
[12,§6.3].
Corollary A.7.5 . — Let M =D/DP . Then, for any dual P ∨ of P , the
complex:
K
P ∨(σ)
−→ K
has cohomology Γ(M), Γ1(M).
A.8. THE COHOMOLOGICAL EQUATION 157
Proof. — In the proposition, take N := 1 = (K,σ ). This gives Γ( M ∨),
Γ1(M ∨) as cohomology of K
P (σ)
−→K. Now, replace M byM ∨. (Of course, no
functoriality here!)
Example A.7.6 . — For u∈ K ∗ = GL 1(K), where K = C({z}) or C((z)),
put Mu := (K, Φu) =Dq/Dq(σq−u−1). A dual of σq−u−1 is, for instance,
σq−u. One has M ∨
u =Mu−1 and Mu⊗Mv =Muv.
From the corollaries above, we draw that K
u−1σq−1
−→ K, resp. K
σq−u
−→K has
cohomology Γ(Mu), Γ1(Mu). From the proposition, we draw thatK
v−1σq−u−1
−→
K has cohomology Hom(Mu,M v), Ext1(Mu,M v).
A.8. The cohomological equation
We here prepare the grounds for the examples of chapter 7 by gi ving some
