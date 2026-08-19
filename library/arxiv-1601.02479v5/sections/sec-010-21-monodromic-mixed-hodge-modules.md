---
doc_id: arxiv-1601.02479v5
doc_title: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A"
section_id: sec-010-21-monodromic-mixed-hodge-modules
section_title: "Monodromic mixed Hodge modules"
section_number: 2.1
pages: 13-20
source_pdf: 1601.02479v5.pdf
source_sha256: 52c2dcd4adf2e72b
doc_brief: "COHOMOLOGICAL DONALDSON–THOMAS THEORY OF A — This paper concerns the cohomological aspects of Donaldson – Thomas theory for Jacobi algebras and the associated cohomo logical Hall alge- bra"
---
we deﬁne as in [43, 44] the category MHM( X) of mixed Hodge modules on X. See
[42] for an overview of the theory. There is an exact functor rat X : D(MHM(X)) →
D(Perv(X)) which takes a complex of mixed Hodge modules F to its underlying
complex of perverse sheaves, and commutes with f∗, f!, f ∗, f !, DX and tensor prod-
uct. If no remark is made to the contrary, and a non-derived targ et or domain
category is not speciﬁed, all these functors, and indeed all funct ors for the en-
tirety of this paper, will be considered as derived functors, even if their non-derived
versions are well-deﬁned.
Set B to be the full subcategory of mixed Hodge modules on A1 containing those
F ∈ Ob(MHM(A1)) such that ( Gm → A1)∗F is an admissible variation of mixed
Hodge structure. Set C to be the full subcategory of B for which the objects are the
admissible variations of mixed Hodge structure on A1. Then we deﬁne the category
of monodromic mixed Hodge structures MMHS to be the Serre quotient B/C.
Fix X and let BX be the full subcategory containing those F ∈ MHM(X × A1)
such that for each x ∈ X, the total cohomology of ( {x} × Gm → X × A1)∗F is an
admissible variation of mixed Hodge structure on Gm. Via Saito’s description of
MHM(X × A1), the category BX ⊂ MHM(X × A1) is the full subcategory, closed
under extensions, and containing the following types of objects
(1) Mixed Hodge modules ˜IC Y ×A1 (L)[dim(Y ) + 1], where Y ⊂ X is an ir-
reducible closed subvariety, and L is a pure weight n variation of Hodge
structure on Y ′ × Gm, for Y ′ an open dense subvariety of Yreg, and n ∈ Z.
(2) Mixed Hodge modules ˜IC Y ×{0}(L)[dim(Y )], for L a pure weight n variation
of Hodge structure on Y ′ ⊂ Yreg ⊂ X as above.
Here ˜IC Y ×A1(L)[dim(Y ) + 1] and ˜IC Y ×{0}(L)[dim(Y )] are the lifts of intersection
complexes to mixed Hodge modules deﬁned in [44, Thm.3.21]. By semisimplic ity,
any object P of type (1) splits into a direct sum P ∼
= P1 ⊕ P⁄=1, where
Pi = ˜IC Y ×A1(Li)[dim(Y ) + 1]
for L1 ⊂ L the maximal pure variation of Hodge structure to have trivial mon-
odromy around Y × {0}, and L⁄=1 its complement.
Inside BX there is a Serre subcategory CX given by the full subcategory of
MHM(X × A1) containing those objects F such that the total cohomology of each
({x} × A1 → X × A1)∗F is an admissible variation of mixed Hodge structure on
A1. It is generated under extensions by simple objects of the form P1.
By Schmid’s rigidity theorem, the total cohomology of the restriction to the ﬁbres
{x}× A1 of any such mixed Hodge module is constant, and CX is the essential image
of the functor π ∗[1] : MHM( X) → MHM(X × A1), where
π : X × A1 → X
14 BEN DA VISON AND SVEN MEINHARDT
is the projection. We deﬁne following [30, Sec.7] the category of monodromic mixed
Hodge modules MMHM(X) = BX /CX. Since the objects of MMHM( X) are the
objects of BX , we deduce that all isomorphism classes of objects in MMHM( X) are
obtained from iterated extensions of simple objects of type (1) sa tisfying L = L⁄=1,
and of type (2). We identify MMHS with MMHM(pt).
In [30] the category of monodromic mixed Hodge modules is presente d as a
subcategory of MHM( X × A1), whereas for us it is a quotient. We collect together
some category theoretic lemmas that clarify this shift in point of view .
Lemma 2.1. Let Ψ : B → B be a functor, and let ν : id B → Ψ be a natural trans-
formation satisfying
(1) Ψ( ν ) =ν Ψ : Ψ → Ψ 2, i.e. Ψ(ν F ) =ν Ψ( F ) for all objects F in B.
(2) Ψ( ν ) =ν Ψ is an isomorphism of functors.
Let D ⊂ B be the full subcategory containing those objects F of B such thatν F : F →
Ψ( F ) is an isomorphism. Then the inclusion functor ι : D → B is right adjoint to
ψ
B D .
Ψ
ι
Condition (2) implies that Ψ( F ) ∈ ob(D) for all F ∈ ob(B), and so we obtain a
factorization Ψ : B → D
ι
− → B. In the lemma, and from now on, we abuse notation
by denoting the resulting functor B → D also by Ψ.
Proof. Via the above abuse of notation we consider ν as a natural transformation
idB → ι ◦ Ψ. We claim that this is the unit of the adjunction, while
η := (ν |D)−1 : Ψ |D → idD = Ψ ◦ ι
will be the unit. We need to check that the compositions of morphisms
Ψ
Ψ(ν )
− − − →Ψ ιΨ
η Ψ
− − →Ψ(23)
ι
ν ι
− →ιΨ ι
ι(η )
− − →ι(24)
are the identity. Pick F ∈ ob(B). Then
ηΨ( F ) ◦ Ψ(ν F ) =ν −1
Ψ( F ) ◦ Ψ(ν F )
= idΨ( F ) .
Pick F ∈ ob(D). Then
ι(ηF ) ◦ν ι(F ) =ν −1
F ◦ν F
= idF .
□
Lemma 2.2. With the assumptions of Lemma 2.1, assume also that B is Abelian,
and Ψ is exact. Let C be the full subcategory of B containing those objects F for
which Ψ( F ) = 0 . Then C is a Serre subcategory. We denote the Serre quotient
B/C. The functor Ψ induces a functor ˜Ψ : B/C → B , which is right adjoint to the
canonical functor Q : B → B /C.
Proof. The category C is a Serre subcategory by exactness of Ψ. By the universal
property of B/C, Ψ induces a functor ˜Ψ : B/C → B . We claim that ν : id B → Ψ pro-
vides a unit for the adjunction. Let F ∈ B /C, and consider the mapν F : F → Ψ( F ).
Since Ψ( ν F ) is an isomorphism, and Ψ is exact, we deduce that Ψ(ker( ν F )) =
Ψ(coker(ν F )) = 0, and so ν F represents an isomorphism
ν F in B/C. Arguing as
above, (ν F )−1 provides the counit to the adjunction. □
COHAS AND QUANTUM ENVELOPING ALGEBRAS 15
The proof of the following lemma is again constructed from the above adjunc-
tions, and is omitted.
Lemma 2.3. With the assumptions of Lemmas (2.1) and (2.2), the induced f unctor
˜Ψ : B/C → D is an equivalence of categories, with inverse equivalence t he composi-
tion of canonical functors D → B → B /C.
Now we apply these abstractions to certain categories of mixed Hod ge modules.
We deﬁne as in [30] the exact functor Ψ X : BX → B X :
Ψ X (F ) = ( X × A2 id ×+
− − − − →X × A1)∗
(
F ⊠ (Gm → A1)!QGm[1]
)
.
The functor is exact since it sends each of the simple mixed Hodge mod ules identi-
ﬁed at the start of this section to mixed Hodge modules. Consider th e distinguished
triangle
QA1 → ({0}֒→A1)∗Q{0}
s
− →(Gm
j
− →A1)!QGm[1]
We deﬁne the natural transfromation ν , for F ∈ B X , via the following composition
of mixed Hodge modules on X × A1
F ∼
=(X × A2 id ×+
− − − − →X × A1)∗
(
F ⊠ ({0}֒→A1)∗Q{0}
) s′
− →
(X × A2 id ×+
− − − − →X × A1)∗
(
F ⊠ (Gm → A1)!QGm[1]
) ∼
= Ψ( F )
where
s′ = (X × A2 id ×+
− − − − →X × A1)∗ (idF ⊠s) .
Lemma 2.4. The pair (Ψ X ,ν ) satisﬁes the conditions of Lemma 2.1.
Proof. Consider the commutative diagram
(25) X × A1 × A1 × A1 idX×A1 ×+
/d47/d47
idX ×+× idA1
/d15/d15
X × A1 × A1
idX ×+
/d15/d15
X × A1 × A1 idX ×+ /d47/d47 X × A1.
We have
Ψ X (ν F ) = (id X ×+)∗(ν F ⊠ idj!QGm [1])
= (id X ×+)∗(idX × + × idA1 )∗(idF ⊠s ⊠ idj!QGm [1])
= (id X ×+)∗(idF ⊠ +∗ (s ⊠ idj!QGm [1]))
where we have used commutativity of (25) for the ﬁnal equality. On the other hand,
we have
ν Ψ X (F ) =(idX ×+)∗(idΨ X (F ) ⊠s)
=(idX ×+)∗(idX × + × idA1)∗(idF ⊠ idj!QGm [1] ⊠s)
=(idX ×+)∗(idF ⊠ +∗ (idj!QGm [1] ⊠s))
and
+∗(s ⊠ idj!QGm [1]) = + ∗(idj!QGm [1] ⊠s)
by commutativity of +. We compute
cone(ν Ψ X (F )) ∼
=(idX ×+)∗(F ⊠ +∗(j!QGm[1] ⊠ cone(s)))
∼
=(idX ×+)∗(F ⊠ +∗(j!QGm[1] ⊠ QA1[1]))
but
+∗(j!QGm [1] ⊠ QA1[1])) ∼
= H∗(A1, j!QGm) ⊗ QA2[2] = 0
proving that ν Ψ X (F ) is an isomorphism. □
16 BEN DA VISON AND SVEN MEINHARDT
Lemma 2.5. Setting Ψ = Ψ X , B = BX in Lemma (2.2), we have C = CX .
Proof. We denote by π : X × A1 → X the projection. By deﬁnition, C is the full
subcategory containing those objects F such that Ψ X (F ) = 0. This is equivalent
to the condition that the natural composition
π ∗π ∗F = (X×A2 id ×+
− − − − →X×A1)∗ (F ⊠ QA1) → (X×A2 id ×+
− − − − →X×A1)∗ (F ⊠ Q0[1]) = F
is an isomorphism. It follows that the objects of C are contained in the objects of CX .
On the other hand, the natural transformation π ∗π ∗π ∗ → π ∗ is an isomorphism
and the reverse inclusion holds. □
Via the same arguments, we deduce the following Lemma.
Lemma 2.6. Under the assumptions of Lemma 2.5 and with the terminology o f
Lemma 2.1, D is the full subcategory of BX containing those objects F satisfying
π ∗F = 0.
The (sub)category D is identiﬁed as the category of monodromic mixed Hodge
modules by Kontsevich and Soibelman; as we have shown, it is equivalen t to our
(quotient) category of monodromic mixed Hodge modules.
The natural pushforward (X×Gm → X×A1)! : MHM( X×Gm)mon → MMHM(X)
is an equivalence of categories, where MHM( X × Gm)mon is the full subcategory of
MHM(X ×Gm) containing those F such that the total cohomology of each pullback
({x} × Gm → X × Gm)∗F is an admissible variation of mixed Hodge structure. An
explicit inverse equivalence Θ X is provided by
(26) Θ X : F ↦→(X × Gm → X × A1)∗ ˜Ψ X F .
where ˜Ψ X is functor induced by Ψ X, as above. In terms of the two types of simple
mixed Hodge modules identiﬁed at the start of the section, we have
Θ X ˜IC Y ×A1(L)[dim(Y ) + 1] ∼
= ˜IC Y ×Gm (L⁄=1)[dim(Y ) + 1]
Θ X ˜IC Y ×{0}(L)[dim(Y )] ∼
= ˜IC Y ×Gm (L ⊠ QGm)[dim(Y ) + 1].
From the existence of a right adjoint to the functor BX → MMHM(X), one can
show (see e.g. [1, 06XM]) that the natural functor
D(BX )/DCX (BX ) → D (BX /CX) = D(MMHM(X))
is an equivalence of categories, where DCX (BX ) is the full subcategory of D(BX )
consisting of those objects whose cohomology objects lie in CX . The subcategory
DCX (BX ) is stable under the Verdier duality functor DX×A1, and so we obtain a
Verdier duality functor on D(MMHM(X)) which we denote Dmon
X . The associated
graded object Gr W
• (F ) of an object in CX with respect to the weight ﬁltration is
also in CX , and so the weight ﬁltration descends to MMHM( X).
Deﬁnition 2.7. Given an element G ∈ MMHM(X), we say it is pure of weight i
if GrW
j G is zero for all j ⁄= i. Given an element F ∈ D (MMHM(X)), we say that
F is pure of weight i if each Hj(F ) is pure of weight i + j, or we just say that F
is pure if it is pure of weight zero.
Remark 2.8. The equivalence (X × Gm → X × A1)! : MHM( X × Gm)mon →
MMHM(X) does not preserve the weight ﬁltration; for instance QGm[1] is a pure
variation of Hodge structure of weight 1, while the monodrom ic mixed Hodge struc-
ture (Gm → A1)!QGm[1] ∼
= ({0}֒→A1)∗Q{0} is pure of weight zero.
If f : X → Y is a morphism of varieties, we deﬁne the functors f !, f ∗, f!, f∗
between the associated derived categories of monodromic mixed Ho dge modules to
be those induced by the functors ( f × idA1 )!, (f × idA1 )∗, (f × idA1)!, (f × idA1)∗
between the associated derived categories of mixed Hodge modules .
COHAS AND QUANTUM ENVELOPING ALGEBRAS 17
Deﬁnition 2.9. Assume X is a variety X
τ
− →NQ0 over a monoid NQ0 of dimension
vectors for a quiver Q. We deﬁne H(X, F ) to be the total cohomology of τ∗F . So
H(X, F ) may be thought of as a cohomologically graded NQ0 -graded monodromic
mixed Hodge module on a point, e.g. the NQ0-graded monodromic mixed Hodge
structure underlying the total hypercohomology of F . Similarly, we deﬁne Hc(X, F )
to be the total cohomology of τ!F .
The monoidal structures ⊗ on D≥(MMHM(X)) and D≤(MMHM(X)) are de-
ﬁned by
(27) F ⊗ G := (X × A1 × A1 id ×+
− − − − →X × A1)∗(pr∗
1,2 F ⊗ pr∗
1,3 G)
where pr i,j : X × A1 × A1 → X × A1 is the projection onto the ith and the jth
component.
Remark 2.10. More generally, let X be a monoid in SchY , the category of schemes
over Y , with ﬁnite type monoid map ⊕ : X ×Y X → X. Then deﬁne
F ⊠⊕ G := (X ×Y X × A1 × A1 ⊕×+
− − − →X × A1)∗(pr∗
1,3 F ⊗ pr∗
2,4 G).
We recover (27) in the special case in which (X
idX
− − →X) is considered as a monoid
in SchX . In addition, for F , G objects of D≥(MMHM(X)), D≥(MMHM(Y )) or
D≤(MMHM(X)), D≤(MMHM(Y )) respectively, we deﬁne
F ⊠G := (X×Y ×A1×A1 idX×Y ×+
− − − − − − − →X×Y ×A1)∗(pr∗
1,3 F ⊗pr∗
2,4 G) ∈ D(MMHM(X×Y )).
This external tensor product is biexact and preserves weigh t ﬁltrations by [30, Sec.4],
[11, Prop.3.2] , or the proof of Proposition 3.8 below.
There is a fully faithful embedding MHM( X) → MMHM(X) given by
i∗ = (X
x↦→(x,0)
− − − − − →X × A1)∗
which is furthermore a monoidal functor, commuting with Verdier du ality, as i is
proper.
Deﬁne Θ X as in (26). Let e : X
x↦→(x,1)
− − − − − →X × Gm be the natural inclusion.
Then e∗Θ X [−1] : MMHM( X) → MHM(X) is also faithful (again using rigidity for
variations of mixed Hodge structure [46, Thm.4.20]), and so we can de ﬁne an exact
faithful (non-derived) functor
(28) forg mon
X : MMHM( X) → Perv(X)
by setting forg mon
X := rat X e∗Θ X [−1].
Let f be a regular function on a smooth algebraic variety X. Deﬁne X<0 =
f −1(R<0) and X0 = f −1(0). We deﬁne the functor ψ f : D(Perv(X)) → D (Perv(X))
ψ f := (X0 → X)∗(X0 → X)∗(X<0 → X)∗(X<0 → X)∗
and deﬁne φ f := cone(( X0 → X)∗(X0 → X)∗ → ψ f ); this cone can indeed be
made functorial — see [26] for details, or the proof of Proposition 3 .11 below for a
functorial deﬁnition of φ f . The functors ψ f and φ f have lifts to endofunctors of
D(MHM(X)), forming a key part of Saito’s theory.
In the sequel we consider vanishing cycles always as a functor D(MHM(X)) →
D(MMHM(X)) via the deﬁnition of [30, Def.27]
(29) φ mon
f := (X × Gm → X × A1)!φ f /u(X × Gm → X)∗.
In (29), u denotes the coordinate on Gm.
18 BEN DA VISON AND SVEN MEINHARDT
Example 2.11. Let f = 0 . Then φ f (F ) ∼
= F [1], since ψ f (F ) = 0 . Likewise,
φ mon
f F = ( X × Gm → X × A1)!(X × Gm → X)∗F [1]. We deduce that φ mon
f F =
j!j∗G[1] where G = (X × A1 π
− →X)∗F and j : X × Gm → X × A1 is the inclusion.
Let i : X × {0}֒→X × A1 be the complement to j. Since G is by deﬁnition trivial
in MMHM(X), we deduce from the distinguished triangle j!j∗ → id → i∗i∗ that
φ mon
f F ∼
= i∗F in MMHM(X). In other words, φ mon
0 F ∼
= F , where we consider F
on the right hand side of the isomorphism as a monodromic mixe d Hodge module
via pushforward along X
i : x↦→(x,0)
− − − − − − − →X × A1.
Remark 2.12. Generalising the above example; in fact it follows from exac tness
of the functors φ f /u[−1] (see [3]),π ∗[1] and j! thatφ mon
f is exact in general.
We collect together some useful properties of φ mon
f .
Proposition 2.13. (1) (Verdier duality): There is a natural isomorphism
Dmon
X φ mon
f ∼
=φ mon
f DX : D(MHM(X)) → D (MMHM(X)),
where DX is the usual Verdier duality functor.
(2) (Interaction with adjunction): If p : X → Y is a map of varieties, and f is
a regular function on Y , then there is a natural transformation φ mon
f p∗ →
p∗φ mon
f p , which is moreover a natural isomorphism if p is proper.
(3) (Homotopy invariance): Let X ′ → X be an aﬃne ﬁbration with d-dimensional
ﬁbres. Then the natural map φ mon
f F → p∗φ mon
f p p∗F is an isomorphism, as
is the natural map p!φ mon
f p p∗F → φ mon
f F ⊗ Hc(Ad).
(4) (Exactness): The functor φ mon
f : D(MHM(X)) → D (MMHM(X)) is exact,
i.e. it restricts to an exact functor MHM(X) → MMHM(X).
(5) (Vanishing cycle decomposition theorem) Let F ∈ MMHM(X) be pure of
weight m for some m ∈ Z, let p : X → Y be a proper map, and let f be a
regular function on Y . Then there is a non-canonical isomorphism
p∗φ mon
f p F ∼
= H(p∗φ mon
f p F ).
(6) (Thom–Sebastiani isomorphism): Let fj : Xj → C be regular functions, for
j = 1 , 2. Then there is a natural ismorphism of bifunctors MHM(X) ×
MHM(X) → MMHM(X):
φ mon
f1 (•) ⊠φ mon
f2 (•) →φ mon
f1⊞f2 (• ⊠ •)|f −1
1 (0)×f −1
2 (0).
(7) (Integral identity): Let V+ ⊕ V− be a C∗-equivariant vector bundle on the
space X, given a C∗-action, where the weights of the action on V+ are all
1, and the weights of the action on V− are all −1. Let f be a C∗-invariant
function. Below, for a vector bundle V ′ we denote the total space of V ′ also
by V ′. Then the natural map
(V+ → X)!(V+ → V+ ⊕ V−)∗φ mon
f (QV+⊕V− → (V+ → V+ ⊕ V−)∗QV+ )
is an isomorphism.
The ﬁrst ﬁve statements follow from the corresponding statemen ts for φ f . The
ﬁrst of these is proved at the level of perverse sheaves as the ma in theorem of [33],
and for mixed Hodge modules as the main theorem of [41], see also Sch ¨ urmann’s ap-
pendix to [5]. The second statement is given by combining [44, Thm.2.14, Thm.4.3].
Homotopy invariance then follows from the homotopy invariance sta tement for per-
verse sheaves. The hard part of the exactness statement is the statement that the
shift of the usual vanishing cycle functor, φ f [−1], is exact. This is a result of Gab-
ber, and can be found in [3]. The version of the decomposition theor em quoted here
follows from Saito’s version of the decomposition theorem [44], and st atements (4)
and (2). The statement regarding the Thom–Sebastiani isomorph ism is in fact false
COHAS AND QUANTUM ENVELOPING ALGEBRAS 19
after replacing φ mon
f with φ f [−1]. The statement involving φ mon
f is due to Saito
[39]; again we refer the reader to Sch¨ urmann’s appendix to [5] for t he compatibility
between this proof and the proof of Massey [32] at the level of com plexes of perverse
sheaves. The integral identity is proved in the above form in [30], and is a central
background result in the proof of the integrality conjecture 6 in [30]. Somewhat
surprisingly, given its crucial role in the theory in other treatments of Hall algebras
in Donaldson–Thomas theory, it is the only one of the seven facts ab out vanishing
cyclesabove that we will not use.
For ease of exposition we make the following simpliﬁcation in what follows .
Assumption 2.14. For all functions f : X → C for which we wish to take φ mon
f ,
if X is smooth, we assume that crit(f ) ⊂ f −1(0) as sets.
Under the assumption, the Thom–Sebastiani isomorphism for mixed Hodge mod-
ules simpliﬁes to
φ mon
f1 (F ) ⊠φ mon
f2 (G) →φ mon
f1⊞f2 (F ⊠ G).
The assumption can be dropped, with a little care. If it does not hold, one can
instead work with the functor φ mon,ﬁb
f :=⨁
a∈A1
C
φ mon
f −a, or with exponential mixed
Hodge structures — see [13], [30], respectively.
Consider the embedding Db(MHM(pt))
i∗
− → Db(MMHM(pt)). The former cate-
gory contains the element
L := H c(A1, Q),
which is pure: it is concentrated entirely in cohomological degree 2, a nd has weight
2. There is no square root of L in Db(MHM(pt)), i.e. an element L1/2 such that
(L1/2)⊗2 ∼
= L, but after embedding Db(MHM(pt)) in Db(MMHS) there is a square
root. We set
L1/2 := Hc(A1,φ mon
x2 QA1 ),
where x2 : A1 → C is considered as a regular function, and QA1 is the constant
(cohomologically shifted) mixed Hodge module on A1. Using the Thom–Sebastiani
isomorphism one may show that this is indeed a tensor square root of L. We ﬁx an
isomorphism
l : L1/2 ⊗ L1/2 ∼
= L.
This amounts to ﬁxing an isomorphism r : Q[−2] ∼
= forgmon
pt L, since up to sign there
is a canonical isomorphism H c(A1,φ x2QA1) ∼
= Q[−1] given by picking one of the
two natural basis elements of H c(A1,ψ x2QA1) ∼
= Q ⊕ Q. In particular, since A1
carries a canonical orientation, there is a canonical choice of r and thus of l. We
set
(30) L−1/2 := HomDb(MMHM(pt))(L1/2, Q),
so there is a canonical isomorphism
L1/2 ⊗ L−1/2 ∼
= Q
with target the monoidal unit in MMHM(pt).
Since L is pure, we deduce from Remark 2.10 that L1/2 is pure, concentrated
in cohomological degree 1. Note that due to the deﬁnition of the cat egory of
monodromic mixed Hodge modules on a point (i.e. monodromic mixed Hodg e
structures), this cohomological degree is with respect to the per verse t-structure on
the underlying derived category of constructible sheaves on A1 ∼
= A1 × pt.
If F ∈ MMHM(X) and G ∈ MMHM(pt) we use the abbreviation
F ⊗ G := F ⊗τ∗G,
6The similarity between the names of the “integral identity” and the “integrality conjecture”
is merely coincidencidental.
20 BEN DA VISON AND SVEN MEINHARDT
whereτ : X → pt is the map to a point.
For X a variety and d ∈ Z we deﬁne
Ld/2
X = Ld/2 ⊗ QX .
If X is a smooth equidimensional variety, we deﬁne
IC X (Q) := L− dim(X)/2
X .
This complex of monodromic mixed Hodge modules is pure, and an elemen t of
MMHM(X), again by Remark 2.10. If X is not smooth, but is irreducible, we de-
ﬁne the monodromic mixed Hodge module IC X (Q) := L− dim(Xreg )/2 ⊗ ˜IC X (QXreg ),
where ˜IC X (QXreg ) is the usual intersection cohomology mixed Hodge module com-
plex of X given by intermediate extension of QXreg . Since ˜IC X (QXreg ) is con-
centrated in cohomological degree dim( Xreg), it follows that IC X (Q) is indeed a
monodromic mixed Hodge module. If X is a ﬁnite disjoint union of irreducible
varieties, we deﬁne
IC X (Q) :=
⨁
Z∈π 0(X)
IC Z(Q).
Remark 2.15. Because of the shift in the deﬁnition of IC X (Q), there are natural
isomorphisms Dmon
X IC X (Q) ∼
= IC X (Q) and Dmon
X φ mon
f IC X (Q) ∼
=φ mon
f IC X (Q) for
X a ﬁnite disjoint union of irreducible varieties, and f a regular function on X.
For X a smooth equidimensional variety we deﬁne
H(X, Q)vir := H(X, IC X (Q))
∼
=L− dim(X)/2 ⊗ H(X, Q) ∈ D b(MMHM(pt)),
and since in the stack-theoretic sense the dimension of dim(B C*) is −1, we extend
this notation by deﬁning
H(BC∗, Q)vir := L1/2 ⊗ H(BC∗, Q) ∈ D (MMHM(pt)).
