---
doc_id: arxiv-1409.4073v1
doc_title: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI"
section_id: sec-002-acknowledgements
section_title: "Acknowledgements"
section_number: null
pages: 5-9
source_pdf: 1409.4073v1.pdf
source_sha256: b40be7f0022f70a1
doc_brief: "SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION FABIO TONINI — W e introduce “sheaﬁﬁcation” functors from categories of (l ax monoidal) linear functors to categories of quasi-coherent sheaves"
---
I would like to thank Jarod Alper, David Rydh, Daniel Schäppi , Mattia Talpo and Angelo
Vistoli for the useful conversations I had with them and all t he suggestions they gave me.
1. Preliminaries on shea ves and fibered categories
Let π : X − → Aﬀ /R be a ﬁbered category. There is a functor of rings OX : X op − →(Sets)
deﬁned by OX (ξ) = H0(Oπ (ξ)), so that (X, OX ) is a ringed category. A presheaf of OX -modules
on X is a functor F : X op − → (Sets) together with an H 0(Oπ (ξ))-module structure on F (ξ)
for all ξ ∈ X such that, if ξ − →η is a map on X , then the map F (η) − → F(ξ) is H 0(Oπ (η ))-
linear. Morphism of presheaves of OX -modules are natural transformations respecting the modul e
structures. We denote by Mod OX the category of presheaves of OX -modules.
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 6
Deﬁnition 1.1. A quasi-coherent sheaf over X is a presheaf of OX -modules such that for all
maps ξ − →η in X the induced map
F (η) ⊗H0(Oπ (η )) H0(Oπ (ξ)) − → F(ξ)
is an isomorphism. We denote by QCoh X the full subcategory of Mod OX of quasi-coherent
sheaves.
Notice that by fpqc descent of modules a quasi-coherent shea f is a sheaf for the fpqc topology
of X .
If f : Y − → X is a morphism of ﬁbered categories and F ∈ Mod OX we deﬁne f ∗F =
F ◦ f : Y op f
− − → Xop F
− − →(Sets). This association deﬁnes a functor f ∗ : Mod OX − →Mod OY ,
called the pull-back functor, and restricts to a functor f ∗ : QCoh X − → QCoh Y. Notice that
f ∗OX = OY tautologically.
The category Mod OX is an abelian category and cokernels of maps between quasi-c oherent
sheaves are again quasi-coherent and thus cokernels in QCoh X . Notice that, since we have
restricted our ﬁber categories to aﬃne schemes, a map f : F − → G of quasi-coherent sheaves
is an epimorphism if and only if it is pointwise surjective, t hat is surjective in Mod OX . The
category QCoh X is R-linear but it is unclear if it is abelian. Moreover kernels i n Mod OX of
maps between quasi-coherent sheaves are almost never quasi -coherent, essentially because pull-
backs are not left exact. There is a natural condition on X which allows us to prove that QCoh X
is an R-linear abelian category.
Deﬁnition 1.2. An fpqc atlas (or simply atlas) of a ﬁbered category X is a representable fpqc
coveringX − → X from a scheme. A ﬁber category is called pseudo-algebraic if it has an atlas,
it is called quasi-compact if it has an atlas from an aﬃne scheme.
Letf : Y − → X be a morphism of ﬁbered categories. The map f is called pseudo-algebraic
(resp. quasi-compact) if for all maps T − → X from a scheme (resp. quasi-compact scheme) the
ﬁber product T ×X Y is pseudo-algebraic (resp. quasi-compact). It is called quasi-separated if
the diagonal Y − → Y ×X Y is quasi-compact.
If X is pseudo-algebraic then the diagonal ∆ X : X − → X ×R X is not necessarily representable.
It is unclear whether this is true or not if X is a fpqc stack, because it is not known if algebraic
spaces satisfy eﬀective descent along fpqc coverings.
Let f : Y − → X be a map of ﬁbered categories. If X and f are pseudo-algebraic then Y is
pseudo-algebraic. If Y is pseudo-algebraic and ∆ X is representable then f is pseudo-algebraic.
If C is a (not full) subcategory of X one can analogously deﬁne presheaves of (OX )|C -modules
and quasi-coherent sheaves on C just replacing all occurrences of X with C . We denote by
Mod(OX )|C and QCoh C the resulting categories.
Deﬁnition 1.3. We deﬁne Xﬂ (resp. Xsm, Xet) as the (not full) subcategory of X of objects
ξ : SpecB − → X which are representable and ﬂat (resp. smooth, étale) and th e arrows are
morphisms in X whose underlying map of aﬃne schemes is ﬂat (resp. smooth, ét ale).
IfX − → X is an fpqc atlas then by deﬁnition R =X ×X X is an algebraic space and the two
projections R ⇒X extends to a groupoid in algebraic spaces. We denote by QCoh (R ⇒X) the
category of quasi-coherent sheaves on R ⇒X (see [ SP014, Tag 0440]). By standard arguments
of fpqc descent for modules we have:
Proposition 1.4. If X admits an fpqc (resp. smooth, étale) atlas then the restricti on QCoh X − →
QCoh Xﬂ (resp. QCoh Xsm, QCoh Xet) is an equivalence of categories. If f : X − → X is an
fpqc atlas then f ∗ : QCoh X − → QCohX is faithful and it induces an equivalence QCoh X − →
QCoh(R ⇒X).
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 7
We see that if X is pseudo-algebraic then QCoh X is equivalent to anR-linear abelian category,
namely QCoh (R ⇒X). Moreover if α : F − → G is a map of quasi-coherent sheaves then Ker (α)
is deﬁned by taking Ker (α|Xﬂ ) ∈ QCoh Xﬂ , which is just given by Ker (α|Xﬂ )(SpecB
ξ
− − → X) =
Ker(α(ξ) : F (ξ) − → G(ξ)) forξ ∈ X ﬂ , and then extending it to the whole X . If X is an algebraic
stack or a scheme we see that QCoh X is equivalent to the usual category of quasi-coherent
sheaves via an R-linear and exact functor. If it is given a subcategory D of QCoh X , an exact
sequence of sheaves in D will always be an exact sequence in QCoh X of sheaves belonging to D.
We now deal with the problem of deﬁning a right adjoint of a pul l-back functor. Given
F ∈ Mod OX we deﬁne the global section F (X ) = Hom(OX, F ) of F , also denoted by H 0(X, F )
or simply H 0(F ), which is an OX (X )-module. More generally given a map of ﬁbered categories
g : Z − → X we deﬁne F (Z) = ( g∗F )(Z). If Z = SpecB is aﬃne we will often write F (B)
instead of F (SpecB).
Letf : Y − → X be a map of ﬁbered categories. Given G ∈ Mod OY and an object ξ : T − → X
of X we deﬁne
(fpG)(ξ) = G(T ×X Y)
Given another object ξ′ : T ′ − → X and a morphism β : ξ′ − →ξ in X there is an induced
morphism (fpG)(ξ) − →(fpG)(ξ′). This data deﬁne a functor fp : Mod OY − →Mod OX and we
have:
Proposition 1.5. Letf : Y − → X be a map of ﬁbered categories. Then fp is a right adjoint of
f ∗ and, if
Y ′ Y
X ′ X
g′
g
ff ′
is a 2-cartesian diagram of ﬁbered categories, there is an isomorphi sm of functors
g∗fp − →f ′
pg′∗ : Mod OY − →Mod OX ′
Iff is aﬃne then fp(QCoh Y) ⊆ QCoh X and (fp)| QCoh Y : QCoh Y − →QCoh X is right adjoint
to f ∗ : QCoh X − → QCoh Y.
Proof. The adjunction betweenf ∗ andfp can be found in [ SP014, Tag 00XF]. With notation from
this reference, we have that f
η I ≃ T ×X Y for an object η : T − → X. Moreover if F ∈ Mod OY
then F (T ×X Y) is the limit of F|T ×X Y over the whole T ×X Y. Thus what is denoted by pf
is easily seen to be equivalent to our fp if we take limits of R-modules and not of sets. The
isomorphism for the base change is tautological. For the las t claim we can assume that X is
an aﬃne scheme in which case the result follows because (usua l) push-forwards commutes with
arbitrary base changes. □
In general fp does not preserve quasi-coherent sheaves, even if f is a proper map of schemes.
To get a right adjoint of pullback we have to require more.
Deﬁnition 1.6. A pseudo-algebraic map f : Y − → X of ﬁbered categories is called ﬂat if given
an object ξ : T − → X of X and an atlas V − →T ×X Y the resulting map V − →T is ﬂat.
Proposition 1.7. Let f : Y − → X be a quasi-compact and quasi-separated map of pseudo-
algebraic ﬁbered categories. Then the composition QCoh Y
fp
− − →Mod OX − → Mod(OX )|Xﬂ
has values in QCoh Xﬂ . The induced map f∗ : QCoh Y − → QCoh X is a right adjoint of
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 8
f ∗ : QCoh X − → QCoh Y. If
Y ′ Y
X ′ X
g′
g
ff ′
is a 2-cartesian diagram of ﬁbered categories with X ′ pseudo-algebraic then Y ′ is pseudo-algebraic,
f ′ is quasi-compact and quasi-separated and there is a natural transformation of functors
g∗f∗ − →f ′
∗g′∗ : QCoh X − → QCoh Y ′
which is an isomorphism if g is ﬂat.
Proof. Consider the 2-Cartesian diagram in the statement. The diagonal of f ′ is quasi-compact
because it is base change of the diagonal of f . To see that fp(F )|Xﬂ is quasi-coherent for
F ∈ QCoh Y, we can assume X = SpecB aﬃne and that Y is quasi-compact with quasi-compact
diagonal. If U = SpecA − → Y is a fpqc atlas, it follows that R = U ×Y U is a quasi-compact
algebraic space. By covering R by ﬁnitely many aﬃne schemes Spec Ai we can write F (Y) as
kernel of a map F (A) − → ⊕iF (Ai). If we base change along a ﬂat map B − →B′ it is now easy
to see that F (Y ×BB′) ≃ F (Y) ⊗BB′, as required.
To deﬁne the natural transformation α : g∗f∗ − →f ′
∗g′∗ notice that there is a natural map
f∗F − →fpF which extends the identity on Xﬂ . Applying g∗ we get g∗f∗F − →g∗fpF ≃ f ′
pg′∗F
and then, restricting to X ′
ﬂ , a map (g∗f∗F )|X ′
ﬂ
− →(f ′
∗g′∗F )|X ′
ﬂ
. Since both sides are in QCoh X ′
ﬂ
this map uniquely extends to a natural transformation α as required. Finally assume that g is
ﬂat and let ξ : SpecB − → X′ ∈ X ′
ﬂ . If the composition Spec B − → X is in Xﬂ then one can
easily check that α(ξ) is an isomorphism. Otherwise, by deﬁnition of ﬂatness, ther e exists an
fpqc covering Spec B′ − →SpecB whose composition ξ′ : SpecB′ − → X′ satisﬁes the previous
condition. Since α(ξ) ⊗BB′ ≃α(ξ′) we get the desired result. □
Remark 1.8. There are set-theoretic problems in considering global sec tions of presheaves and
therefore push-forwards, because Mod OX is in general not locally small. The common way to
solve this problem is to use Grothendieck universes. Take a u niverse U and deﬁne rings inside
U , so that Aﬀ /R is small (with respect to a bigger universe). Fibered catego ries should then
be required to be small too. In this situation it is easy to sho w that Mod OX is locally small
and therefore global sections and push-forwards are well de ﬁned. With this approach we have
to be careful in considering (big) rings deﬁned starting fro m some F ∈ Mod OX : for instance
Spec OX (X ) is in general not an object of Aﬀ /R.
Notice that global sections and pushforwards of quasi-cohe rent sheaves are always well deﬁned
for a pseudo-algebraic ﬁbered category and a pseudo-algebr aic map respectively. The reason is
that if F ∈ QCoh X and p : X − → X is a fpqc atlas then F (X ) − →(p∗F )(X) is injective and
thus F (X ) is a set.
In the rest of the paper we will not be concerned about those se t-theoretic problems.
Deﬁnition 1.9. IfA is anR-algebra and F ∈ Mod OX then a compatible A-module structure on
F is the data of A-module structures on F (ξ) commuting with the H 0(Oπ (ξ))-module structure
on F (ξ) for all ξ ∈ X and such that, for all ξ − →η in X , the map F (η) − → F(ξ) isA-linear. We
deﬁne QCoh A X as the category of quasi-coherent sheaves over X with an A-module structure.
We also deﬁne XA as the ﬁber product Spec A ×R X .
Notice that if Y
g
− − → Xis a map of ﬁbered categories and F is a presheaf of OX -modules with
anA-module structure then g∗F inherits an A-module structure. In particular g∗ : QCoh X − →
QCoh Y extends to a functor QCoh A X − → QCohA Y.
SHEAFIFICATION FUNCTORS AND TANNAKA’S RECONSTRUCTION 9
Proposition 1.10. LetA be an R-algebra. Then the push-forward map QCoh XA − →QCoh X
extends naturally to an equivalence QCoh XA − →QCohA X .
Proof. The result is very simple if X is an aﬃne scheme. In general, if we set g : XA − → X for
the projection and we consider G ∈ QCoh XA, then g∗G ∈ QCoh X and it inherits an A-module
structure from the action of A on G. Therefore g∗G ∈ QCohA X . If h : SpecB − → X is a map
consider the diagrams
Spec(B ⊗RA) XA QCoh XA QCoh Spec(B ⊗RA)
SpecB X QCohA X QCohA SpecB
h′
g
h
g′
∗g∗g′
h′∗
h∗
The second diagram is 2-commutative and the last vertical map is an equivalence. Us ing those
diagrams it is easy to deﬁne a quasi-inverse QCoh A X − → QCoh XA of g∗.
□
We will almost always regard quasi-coherent sheaves over XA as objects of QCoh A X .
Remark 1.11. If F, G ∈ QCohA X then F ⊗ OX G does not correspond to the tensor product in
QCoh XA: F ⊗ OX G has two distinct A-module structures. Under the equivalence QCoh XA − →
QCohA X the tensor product of F and G, that we will denote by F ⊗ OXA
G, is given by
U ↦− → F(U ) ⊗H0(OU ) G(U )/⟨ax ⊗y −x ⊗ay | x ∈ F (U ),y ∈ G (U )⟩
Deﬁnition 1.12. A locally free sheaf E (of rank n) over X is a quasi-coherent sheaf such
that E(SpecB − → X ) is a ﬁnitely generated projective B-module (of rank n) for all maps
SpecB − → X. We denote by Loc X the subcategory of QCoh X of locally free sheaves.
We will say that a ﬁber category X has the resolution property if Loc X generates QCoh X .
