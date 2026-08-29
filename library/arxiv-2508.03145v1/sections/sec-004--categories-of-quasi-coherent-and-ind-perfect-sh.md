---
doc_id: arxiv-2508.03145v1
doc_title: "Θ-Categories and Tannakian duality"
section_id: sec-004--categories-of-quasi-coherent-and-ind-perfect-sh
section_title: "-Categories of quasi-coherent and ind-perfect sheaves"
section_number: null
pages: 15-23
source_pdf: 2508.03145v1.pdf
source_sha256: 2bf03452cb503e96
doc_brief: "Θ-Categories and Tannakian duality — We introduce a notion ofΘ-categories, which is a refinement of the notion of symmetric monoidal∞-categories."
---
For a commutativek-algebraA, we considerQCoh(SpecA), also denoted by
QCoh(A), the symmetric monoidal∞-category of complexes ofA-modules.
When A varies in commutativek-algebras this defines an fpqc-stack in pre-
sentable symmetric monoidal∞-categories
QCoh: Affop
k −→∞-Cat⊗
pr.
We will need a slight modification of the stackQCoh, which involves ind-
perfect complexes. For any small stack F, the dualizable objects in the
symmetric monoidal∞-category QCoh(F ) are the perfect complexes, whose
∞-category will be denotedPerf(F ). It comes equipped with the restriction
of the symmetric monoidal structure ofQCoh(F ), and as such forms a small,
stable symmetric monoidal∞-category.
Definition 2.1. The presentable symmetric monoidal∞-category of ind-
perfect complexes onF is the ind-completion ofPerf(F ). It is denoted by
dPerf(F ) := Ind(Perf(F )).
For any small stackF∈ Stk we have a natural adjunction of presentable
symmetric monoidal∞-categories
dPerf(F ) ⇆ QCoh(F ),
where the left adjoint is the canonical extension by filtered colimits of the
inclusion Perf(F )⊂ QCoh(F ). When X = SpecA is an affinek-scheme,
or more generally a quasi-compact and quasi-separatedk-scheme, then the
perfect complexes are compact generators ofQCoh(X), and thus the above
adjunction is an equivalence. However, we warn the reader that for a gen-
eral stack, even representable by a nice Artin stack, perfect complexes might
not even be compact objects in quasi-coherent complexes. In general, the
natural∞-functor dPerf(F )→ QCoh(F ) is therefore neither fully faithful nor
essentially surjective.
We want to enhance the two∞-functorsF7→ dPerf(F )andF7→ QCoh(F )
from small stacks to∞-Cat⊗
pr, to∞-functors to∞-CatΘ
pr. This is straight-
forward for quasi-coherent complexes (see Remark 2.3 below), but more in-
volved for ind-perfect complexes because the (L)Sym-monad does not pre-
serve perfect complexes. We will therefore construct explicit models for
15
these symmetric monoidal∞-categories with strict representatives of the in-
volved monads. A more intrinsic approach should follow from the techniques
of [Rak20, §4.2].
We letX∗ : I→ Affk be a small diagram of affinek-schemes overF such
that the canonical morphismcolimi∈IXi→F is an equivalence. Dually, this
yields a diagram of (discrete) commutativek-algebras A∗ : Iop→ k-CAlg♡.
This diagram can be seen as a commutative algebra object in the ((1, 1)-)
categoryofpresheavesofabeliangroups Fun(Iop, Ab), sothatwecanconsider
the abelian categoryA∗-Mod of presheaves ofA∗-modules. Recall that an
object M inA∗-Mod consists ofAi-modules Mi for alli∈I, and morphisms
u∗ : Aj⊗AiMi→Mj ofAj-modules for allu: j→i inI, satisfying the usual
compatibilities with compositions and identity inI. The abelian category
A∗-Mod possesses enough projective objects: these are the direct sums of free
A∗-modules F (i) on objectsi∈ I, characterized by the functorial bijection
Hom(F (i),M )≃Mi. They can also be written more explicitly asF (i)(j) =L
j→iAj for j∈I.
We letscA∗-Mod be the category of simplicial-cosimplicial objects in the
abelian categoryA∗-Mod. As explained in [BCN21] the categoryscA∗-Mod
is endowed with a model category structure whose weak equivalences are
induced by the totalization functor to presheaves of cochain complexes of
abelian groups
Tot⊕ : scA∗-Mod−→ Fun(Iop,C (Z)).
The fibrations are the levelwise fibrations of simplicial-cosimplicial abelian
groups of [BCN21, Defn. 5.2]. A set of generating cofibrations is given by the
family of morphismsF (i)⊗ZE→F (i)⊗ZE′ wherei varies inI andE→E′
is a generating cofibration of the model category of simplicial-cosimplicial
abelian groups (see proof of [BCN21, Thm. 5.5]). We note in particular that
theevaluationfunctorat i∈I,scA∗-Mod→scAi-Mod preservescofibrations
and trivial cofibrations.
LetL(scA∗-Mod) be the∞-category obtained fromscA∗-Mod by invert-
ing the weak equivalences. The∞-categoryL(scA∗-Mod) is presentable and
closed symmetric monoidal, and is equivalent to the lax limit of the diagram
i7→ QCoh(Ai) (see e.g. [Har19]). The limit of this diagram,QCoh(F ), sits
as a full symmetric monoidal sub-∞-category inL(scA∗-Mod): it consists
precisely of objectsM such that for any morphismj→ i in I the induced
morphism
Aj⊗L
AiMi→Mj
is an equivalence of simplicial-cosimplicial modules (i.e. a quasi-isomorphism
on the correspondingTot⊕).
16
Let us now consider the category scA∗-CAlg of strictly commutative
simplicial-cosimplicial A∗-algebras, together with its natural forgetful func-
torscA∗-CAlg→scA∗-Mod. We can lift the (semi-)model category structure
along this forgetful functor, which now becomes a right Quillen functor pre-
serving all weak equivalences. It induces a right adjoint∞-functor between
presentable∞-categories
L(scA∗-CAlg)→L(scA∗-Mod).
Similarly, ifO is a cofibrant model for the simplicialE∞-operad we can con-
siderO-algebras inside scA∗-Mod, together with its natural (semi-)model
category structure lifted from the forgetful functorscA∗-AlgO→scA∗-Mod.
The canonical projectionO→∗ to the terminal operad provides a factor-
ization of (right Quillen) forgetful functors
scA∗-CAlg→scA∗-AlgO→scA∗-Mod.
Lemma 2.2. Upon inverting weak equivalences, the above sequence of right
Quillen functors induces a sequence of right adjoints between presentable∞-
categories
L(scA∗-CAlg)→L(scA∗-AlgO)≃ CAlg(L(scA∗-Mod))→L(scA∗-Mod).
that endows the presentable symmetric monoidal∞-categoryL(scA∗-Mod)
with the structure of aΘ-category.
Proof. On localizations, we obtain a sequence of conservative right adjoints
that furthermore preserve geometric realizations, since these can be com-
putedbythediagonalinthesimplicialdirection. Inparticular, L(scA∗-CAlg)
and L(scA∗-AlgO) can be identified with∞-categories of modules for two
monads on L(scA∗-Mod). In the second case, this is the E∞-monad and
we obtain the middle equivalence. Both monads preserve sifted colimits by
(the proof of) [BCN21, Prop. 5.17], so that the forgetful∞-functors pre-
serve sifted colimits as well. Finally, the forgetful functorL(scA∗-CAlg)→
L(scA∗-AlgO)≃ CAlg(L(scA∗-Mod)) also preserves coproducts, which are
computed by (derived) tensor products.
Finally, we define aΘ-structure on QCoh(F ) simply by pull-back along
the inclusion QCoh(F )⊂L(scA∗-Mod)
L(scA∗-CAlg) // CAlg(L(scA∗-Mod)) //L(scA∗-Mod)
Θ-CAlg(QCoh(F )) //
OO
CAlg(QCoh(F )) //
OO
QCoh(F ),
OO
17
where each square above is cartesian. Using Lemma 2.2 and the fact that
QCoh(F )⊂L(scA∗-Mod) is closed under colimits, one sees that this indeed
defines a Θ-structure. We will writeQCohLSym(F ) for this Θ-structure and
refer to it as theLSym Θ-structure. We leave it to the reader to construct
functorialities inF to provide a well defined∞-functor F7→ QCohLSym(F )
from small stacks toΘ-categories.
Remark2.3. Onecanalsogiveamoreintrinsicdescriptionof QCohLSym(F ),
as follows. Let LSym-CAlg(k) denote the ∞-category of LSym-algebras
over k, that is, algebras for theLSym-monad on QCoh(k) induced by the
symmetric algebra monad on flat k-modules by right-left extension (see
[BCN21,Rak20]). This comes with a forgetful functor LSym-CAlg(k) →
k-CAlg to E∞-algebras over Z that preserves limits and colimits (sifted col-
imits and tensor products).
For each discretek-algebra A, we then have a natural sequence of right
adjoint forgetful functors
A/LSym-CAlg(k)→A/k-CAlg→A-Mod(QCoh(k))≃ QCoh(A)
depending functorially onA. Since the first functor preserves colimits and
A/k-CAlg≃ CAlg(QCoh(A)) by [Lur22, Cor. 3.4.1.7], this determines aΘ-
structure onQCoh(A), equivalent to the LSymΘ-structure considered above.
Using this, we obtain a functorQCohLSym : Affop
k →∞ -CatΘ
pr satisfying fpqc
descent (since QCoh does). For each cardinalκ, we then define
QCohLSym : Stκ−small,op
k →∞ -CatΘ
pr
to be the unique extension preservingκ-small limits (using Remark 1.6).
We now turn to the case of ind-perfect complexes. For theΘ-structure on
dPerf(F ), we will need a slight modification of the previous construction. For
this, we letP⊂ scA∗-Mod be the full sub-category of objectsM satisfying
the following conditions.
(1) The objectM is cofibrant.
(2) For anyi∈ I, Tot⊕(Mi) defines a compact object in QCoh(Ai) and
moreover for anyi→j the induced morphismAj⊗AiMi→Mj is an
equivalence of simplicial-cosimplicialAj-modules.
The localization of P along its weak equivalences is equivalent, via the
canonical inclusion, toPerf(F )⊂ QCoh(F )⊂L(scA∗-Mod).
18
For any integern≥ 0 we have an endofunctorΘn : P→ P sending M
to its genuinen-th symmetric power (M⊗n)Σn. This defines an N-graded
object in the categoryFun(P, P), that is, a functor
Θ∗ : N→ Fun(P, P),
where N is the discrete category of natural numbers. The functor Θ∗ is
moreover an N-graded monad, or equivalently,Θ∗ : N→ Fun(P, P) admits a
natural structure of a lax monoidal functor, where the monoidal structure
on N is given by the multiplication and the monoidal structure onFun(P, P)
is the composition of endo-functors. The lax monoidal structure is given by
the natural morphisms
Θm(Θn(M∗)) = ((M⊗n
∗ )Σn)⊗m
Σm≃ (M⊗nm
∗ )Σn⋉Σ×n
m
−→(M⊗nm
∗ )Σnm
induced by the canonical mapΣn ⋉Σ×n
m → Σnm. The graded monadΘ∗ will
be denoted byLSym∗.
Similarly, any cofibrant simplicial operadO such thatO(k)hΣk has the
homotopy type of a finite CW complex gives rise to anN-graded monad
Sym∗
O : N→ Fun(P, P)
by sendingn to (O(n)⊗ (−)⊗n)hΣn. The finiteness condition onO implies
that each endofunctor(O(n)⊗(−)⊗n)hΣn preserves the sub-categoryP. The
lax monoidal structure on Sym∗
O is the usual one and endowsSym∗
O with
the structure of a graded monad overP. Moreover, the canonical projection
O→∗ to the terminal simplicial operad (which is not cofibrant anymore),
produces a canonical morphism of graded monads
Sym∗
O→ LSym∗.
We now apply this to cofibrant models for theEn-operads, and obtain a
sequence of morphisms of graded monads onP
Id = Sym∗
E0→···→ Sym∗
En→ Sym∗
En+1→···→ LSym∗. (S)
These monads preserve the weak equivalences onP, so that they induce a
sequence of morphisms of graded monads on the localizationPerf(F ). We
thus obtain a sequence (S) in the∞-category of lax monoidal∞-functors
N→ Fun(Perf(F ), Perf(F )),
19
from the multiplicative monoidN to the monoidal∞-category of endo-∞-
functorsof Perf(F ). Nowrecallthatthereisacanonicalfullmonoidalembed-
ding Fun(Perf(F ), Perf(F )),→ Fun(dPerf(F ),dPerf(F )), whose essential image
consists of filtered colimit preserving∞-functors that also preserve compact
objects. We can therefore identify the sequence (S) with a sequence in the
∞-category of graded monads ondPerf(F ). Taking the sum overN, we get a
sequence of monoids inFun(dPerf(F ),dPerf(F ))
Id→···→ SymEn→ SymEn+1→···→ LSym
whose colimit provides the desired morphism of monads ondPerf(F )
Sym = colimnSymEn→ LSym.
Note that Sym is identified with the E∞-monad, and therefore the ∞-
categories of algebras and their forgetful∞-functors
LModLSym(dPerf(F ))→ LModSym(dPerf(F ))→ dPerf(F )
defines a Θ-structure ondPerf(F ).
We have thus constructed aΘ-category, denoted bydPerfLSym(F ), with
underlying symmetric monoidal∞-category equivalent todPerf(F ). We leave
it to the reader that this can be made functorial inF and provides a well
defined∞-functor
dPerfLSym(−) : Stsmall
k →∞ -CatΘ
pr
fromsmallstacksto Θ-categories. Thecanonicalfunctor dPerf(F )→ QCoh(F )
can be lifted to a morphism ofΘ-categories
dPerfLSym(F )→ QCohLSym(F ).
Note that this comparison map is an equivalence whenever the stackF ≃
SpecA is affine.
Definition 2.4. Let F be a small stack overk. We define the LSym Θ-
categories of quasi-coherentand ind-perfect complexes on F to be the Θ-
categories QCohLSym(F ) and dPerfLSym(F ) constructed above.
For each stackF∈ Stk, theΘ-categories QCohLSym(F ) and dPerfLSym(F )
are equipped with a natural map fromdPerfLSym(k)≃ QCohLSym(k). They
thus acquire a naturalk-linear structure in the following sense.
20
Definition 2.5.We define ak-linear Θ-categoryto be a map ofΘ-categories
dPerfLSym(k)≃ QCohLSym(k)→T Θ. We will write
k/∞-CatΘ
pr := dPerfLSym(k)/∞-CatΘ
pr
for the (2,∞)-category ofk-linear Θ-categories.
Lemma 2.6. The underlying∞-categoryT of ak-linear Θ-categoryT Θ is
a stable presentable∞-category.
Proof. The underlying symmetric monoidal∞-functor u: QCoh(k)→T in-
duces a natural tensored structure ofT over QCoh(k) by the simple formula
E⊗x :=u(E)⊗x, forE∈ QCoh(k). As QCoh(k)is stable, this automatically
implies the stability ofT.
2.2 Tannakian Θ-categories and Tannakian gerbes
For the sake of simplicity we will only deal with the neutral case in the
present work.
Definition 2.7. A neutralized k-linear Tannakian Θ-category is a map of
k-linear Θ-categories
ω : T Θ−→dPerfLSym(k)≃ QCohLSym(k)
satisfying the following conditions.
(T1) Theunderlyingpresentablesymmetricmonoidal ∞-categoryT is"rigid":
it is compactly generated and compact objects inT coincide with du-
alizable objects.
(T2) The underlying∞-functorω : T→ dPerf(k)≃ QCoh(k) is conservative.
(T3) Let QCoh(k)≤0⊂ QCoh(k) denote the full sub-∞-category of connec-
tive objects. The full sub-∞-category ω−1(QCoh(k)≤0)⊂ T then de-
fines the connective part of a bounded (on compact objects)t-structure
on T for whichω becomes t-exact.
Let us writek/∞-CatΘ
pr/k :=
 
k/∞-CatΘ
pr

QCohLSym(k) for the (2,∞)-
category ofk-linear Θ-categories over QCohLSym(k) and
k-TanΘ
∗ ⊆k/∞-CatΘ
pr/k
for the full sub-(2,∞)-category on the neutralized k-linear Tannakian Θ-
categories. Here the "∗" refers to the neutralized assumption. As ω is
conservative, the(2,∞)-category k-TanΘ
∗ is in fact a(1,∞)-category.
21
Definition 2.8. A pointed (or neutralized) Tannakian gerbe over k is a
pointed stackF∈∗/Stk satisfying the following conditions.
(G1) The natural morphism of fpqc-sheaves∗→ π0(F ) is an isomorphism.
(G2) The stackF is pointed Q-local: for any morphism of pointed and con-
nected stacksu: G1→G2 whose induced∞-functoru∗ : QCoh(G2)→
QCoh(G1) is an equivalence, the induced morphism in mapping spaces
u∗ : MapStk(G2,F )→ MapStk(G1,F )
is an equivalence.
(G3) There exists a coconnectivek-linear LSym-algebra B and an equiva-
lence
SpecB≃ Ω∗F
(see [Toe06] for the notion of spectrum of coconnectiveLSym-algebras
and the theory of affine stacks). Moreover, B is of positive Tor-
dimension (also called connectively flat): ifE is a coconnective object
in QCoh(k), thenE⊗kB remains coconnective.
(G4) The k-linear Θ-functor ω : dPerfLSym(F )→ dPerfLSym(k), obtained by
pull-back along the base point∗→ F, makesdPerfLSym(F ) into a Tan-
nakian Θ-category.
We will writek-Gerb∗⊂∗/Stk for the full sub-∞-category on the pointed
Tannakian gerbes overk.
LetT Θ be ak-linear Θ-category. For a commutativek-algebraA, we set
FibLSym(T Θ)(A) := Mapk/∞-CatΘ
pr
(T, QCohLSym(A)).
Since QCohLSym defines an fpqc-stack ofk-linear Θ-categories, varyingA in-
sidethecategoryofcommutative k-algebrasyieldsanfpqc-stack FibLSym(T Θ),
called thestack of Θ-fiber functors onT Θ. This is part of an adjunction
FibLSym : k/∞-CatΘ
pr
// Stop
k : QCohLSym.oo
Indeed, since QCohLSym satisfies fpqc descent, there is a natural equivalence
for F∈ Stk and T Θ∈k/∞-CatΘ
pr
Mapk/∞-CatΘ
pr
(T Θ, QCohLSym(F ))≃ MapStk(F, FibLSym(T Θ)).
22
In particular, we have adjunction morphisms
βT Θ : T Θ→ QCohLSym 
FibLSym(T Θ)

F→ FibLSym 
QCohLSym(F )

.
Thesecondmorphism, composedwiththecanonicalmorphism dPerfLSym(F )→
QCohLSym(F ), induces a morphism
αF : F→ FibLSym dPerfLSym(F )

.
This extends naturally to the neutralized, or pointed, situation as follows.
Let us writeFibLSym
∗ (T Θ)⊂ FibLSym(T Θ) for the full sub-stack consisting of
all fiber functors locally equivalent toω : T Θ → QCohLSym(k). This full
sub-stack can also be written
FibLSym
∗ (T Θ)≃BautΘ(ω)⊂ FibLSym(T Θ)
whereautΘ(ω)isthestackof Θ-auto-equivalencesof ω. Thestack FibLSym
∗ (T Θ)
is connected (by definition) and canonically pointed atω. Note that anyΘ-
endomorphism ofω is also a self-equivalence, as a consequence of the rigidity
condition (T1).
Similarly, if x:∗ →F is a pointed connected stack, we can identify
QCohLSym(F ) with an object ink/∞-CatΘ
pr/k using its canonical fiber func-
tor at the basepointx∗ : QCohLSym(F )→ QCohLSym(k). This yields a similar
adjunction
FibLSym
∗ : k/∞-CatΘ
pr/k // (∗/Stcn
k )op : QCohLSym
oo
where∗/Stcn
k denotes the∞-category of pointed connected stacks. Using
the unit and counit of this adjunction, together with natural morphism
dPerfLSym→ QCohLSym(F ), we obtain two canonical morphisms
βT Θ : T Θ→ QCohLSym(FibLSym
∗ (T Θ)) αF : F→ FibLSym
∗ (dPerfLSym(F ))
The Tannakian duality investigated in the next chapter ensures thatβ
andαaresomehow equivalenceswhen T Θ isTannakianand F isaTannakian
gerbe. We will only have partial answers, but we refer to Remarks 2.13 and
2.15 for some indications of how better results can be obtained.
