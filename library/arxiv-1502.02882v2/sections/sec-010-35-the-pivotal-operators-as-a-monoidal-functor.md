---
doc_id: arxiv-1502.02882v2
doc_title: "Fusion categories via string diagrams Bruce Bartlett"
section_id: sec-010-35-the-pivotal-operators-as-a-monoidal-functor
section_title: "The pivotal operators as a monoidal functor"
section_number: 3.5
pages: 16-18
source_pdf: 1502.02882v2.pdf
source_sha256: 43641c6f3aed63dd
doc_brief: "Fusion categories via string diagrams Bruce Bartlett — We use the string diagram calculus to give graphical proofs of the basic results of Etingof, Nikshych and Ostrik [9] on fusion categories."
---
We want to precisely relate the pivotal operators with the more traditional no-
tion of the ‘double dual functor’. We ﬁrst need to show that the pivotal operators
can be viewed as equipping the identity functor with coherence isomorphisms
making it into a monoidal functor.
Lemma 3.23. SupposeF,G : D→ D′ are linear functors between semisimple
categories. Let θi : F (Xi)→ G(Xi) be a collection of maps, where Xi ranges
over the representatives of the simple objects of D. Then there exists a unique
natural transformation θ :F⇒G such that θXi =θi.
Proof. LetA∈ D, and for eachi, choose a basis{eα :Xi→A} for Hom(Xi,A )
with corresponding dual basis{eβ :A→Xi}. Set θA =∑
i,αG(eα)◦θi◦F (eα).
The rest of the proof (naturality of θ and its uniqueness) is the same as [3,
Lemma 3.9].
16
This allows us to extend the pivotal operators Ti
jk, initially deﬁned only on
the simple objects, to a natural transformation T≡{TA,B : A⊗B→A⊗B}
where A and B are arbitrary objects of C.
Corollary 3.24. The pivotal operators Ti
jk extend uniquely to a natural trans-
formation T :⊗⇒⊗ from the tensor functor ⊗ : C ⊠ C→ C to itself.
Proof. The pivotal operators Ti
jk : Hom(Xi,Xj⊗Xk)→ Hom(Xi,Xj⊗Xk)
induce maps
Tj,k :Xj⊗Xk→Xj⊗Xk
for each pair of simple objectsXj,Xk, deﬁned uniquely by the requirement that
for each simple object Xi, the map on the hom-sets given by post-composing
with Tj,k,
post(Tj,k) : Hom(Xi,Xj⊗Xk)→ Hom(Xi,Xj⊗Xk)
f↦→Tj,k◦f
is equal to Ti
jk. That is, we require post( Tj,k) = Ti
j,k as endomorphisms of
the vector space Hom(Xi,Xj⊗Xk). By the Yoneda lemma, this indeed gives
unique well-deﬁned maps Tj,k. Now apply Lemma 3.23 to the case D = C ⊠ C,
D′ = C, and F (=G) given by the tensor functor ⊗ : C ⊠ C→ C.
Recall that a monoidal functor ( F,T,φ ) : C→ D between monoidal cate-
gories C and D consists of a functor F : C → D together with natural iso-
morphisms{TA,B :F (A)⊗F (B)→F (A⊗B), A,B∈ C} andφ : 1D→F (1C)
satisfying certain coherence equations.
Proposition 3.25. The pivotal operatorsTi
jk, when extended to a natural trans-
formation{TA,B :A⊗B→A⊗B}, obey the coherence isomorphisms making
T := (id,T, id) : C→ C a monoidal functor.
Proof. By Lemma 3.23, we only need to check the coherence equations on the
simple objects. The unit coherence equations are T 1
i,1 =T 1
1,i = id, which is au-
tomatically satisﬁed due to the rigidity equations (2). The coherence conditions
on T are:
(F (Xj)⊗F (Xk))⊗F (Xl)
F (Xj⊗Xk)⊗F (Xl) F ((Xj⊗Xk)⊗Xl)
F (Xj⊗ (Xk⊗Xl))
F (Xj)⊗ (F (Xk)⊗F (Xl)) F (Xj)⊗F (Xk⊗Xl)
TXj,Xk⊗ id
TXj⊗Xk,Xl
F (aXj,Xk,Xl)
aF (Xj ),F (Xk),F (Xl)
id⊗TXk,Xl
TXj,Xk⊗Xl
(20)
Apply this diagram to the basis vectors (3), working in a pivotal basis to simplify
the calculation. It becomes the requirement that
=
∑
n,γ,δ
(Fi
jkl)αmβ
γnδ
 (21)
17
To prove (21), insert the graphical deﬁnition (18) of the pivotal operators into
(21), and expand out the left hand side using the associator expansion (4). As
in the proof of Theorem 3.10, we obtain two diagrams which are rigidly isotopic,
hence equal.
Corollary 3.26. In a pivotal basis, the pivotal symbols satisfy
ϵi
jk,αϵm
kl,β =ϵi
nl,γϵn
jk,δ whenever (Fi
jkl)γnδ
αmβ⁄= 0. (22)
Proof. This is precisely what (21) says, in a pivotal basis.
Remark 3.27. The equation (22) satisﬁed by theϵi
jk,α is formally similar to the
equation satisﬁed by the 2nd Stiefel-Whitney 2-cocycle w2(M)∈H 2(M, Z/2Z)
of an oriented manifold M in ˇCech cohomology [22]. It can be thought of as a
‘Z/2 version’ of the 2-cocycle condition in Davydov-Yetter cohomology of the
fusion category, see Example 6.3.
Let us summarize the results of this section explicitly as follows.
Theorem 3.28 (cf. [9, Thm 2.6]) . Every fusion category C over C comes
equipped with a canonical monoidal endofunctor T : C→ C, the pivotal endo-
functor, satisfying:
• The underlying functor of T is the identity functor,
• The monoidal coherence isomorphisms T : A⊗B → A⊗B ofT are
speciﬁed by the pivotal operatorsTi
jk, extended to a natural transformation
using Corollary 3.24,
• T2 = id.
