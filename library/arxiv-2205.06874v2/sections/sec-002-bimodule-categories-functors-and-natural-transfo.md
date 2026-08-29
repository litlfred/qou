---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-002-bimodule-categories-functors-and-natural-transfo
section_title: "(Bi)module categories, functors and natural transformations"
section_number: null
pages: 5-9
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
In this section, we summarise background on (bi)module categories, (bi)module functors and (bi)module
natural transformations from [EGNO, Ch. 7].
Definition 1.2. LetC,D be multitensor categories with associatorsa :⊗(⊗× id)⇒⊗ (id×⊗ ) and left and
right unit constraintsl :e⊗ id⇒ id, r : id⊗e⇒ id.
1. AC-(left) module categoryis a locally finiteC-linear abelian categoryM together with
• a functor▷ :C×M→M that is C-bilinear on the morphisms and exact in the first variable,
• natural isomorphismsc :▷(⊗× idM)⇒▷(idC×▷) and γ :e▷−⇒ idM
such that the following diagrams commute for allx,y,z ∈ ObC and m∈ ObM:
((x⊗y)⊗z)▷m
cx⊗y,z,m//
ax,y,z ▷1m

(x⊗y)▷ (z▷m)
cx,y,z▷m//x▷ (y▷ (z▷m))
(x⊗ (y⊗z))▷mcx,y⊗z,m
//x▷ ((y⊗z)▷m)
1x▷cy,z,m
55 (6)
(x⊗e)▷m
cx,e,m //
rX ▷1m
&&
x▷ (e▷m)
1x▷γm
xx
x▷m.
(7)
2. AD-right module categoryis a locally finiteC-linear abelian categoryM together with
• a functor◁ :M×D→M that is C-bilinear on the morphisms and exact in the second variable,
• natural isomorphismsd :◁(◁× idD)⇒◁(idM×⊗ ) and δ :−◁e⇒ idM
that make the following diagrams commute for allx,y,z ∈ ObD and m∈ ObM
((m◁x)◁y)◁z
dm◁x,y,z//
dm,x,y◁1z

(m◁x)◁ (y⊗z)
dm,x,y⊗z//m◁ (x⊗ (y⊗z))
(m◁ (x⊗y))◁zdm,x⊗y,z
//m◁ ((x⊗y)⊗z)
1m◁ax,y,z
55 (8)
m◁ (e⊗x)
dm,e,x //
1m◁lX
&&
(m◁e)◁x
δm◁1x
xx
m◁x.
(9)
3. A (C,D)-bimodule categoryis a locally finiteC-linear abelian categoryM with
• aC-left module category structure(▷,c,γ ),
• aD-right module category structure(◁,d,δ ),
• a natural isomorphismb :◁(▷× idD)⇒▷(idC×◁)
such that the following diagrams commute for allx,y∈ ObC, u,v∈ ObD and m∈ ObM
((x⊗y)▷m)◁u
bx⊗y,m,u//
cx,y,m◁1u

(x⊗y)▷ (m◁u)
cx,y,m◁u//x▷ (y▷ (m◁u))
(x▷ (y▷m))◁ubx,y▷m,u
//x▷ ((y▷m)◁u)
1x▷by,m,u
55 (10)
5
((x▷m)◁u)◁v
dx▷m,u,v//
bx,m,u◁1v

(x▷m)◁ (u⊗v)
bx,m,u⊗v//x▷ (m◁ (u⊗v))
(x▷ (m◁u))◁vbx,m◁u,v
//x▷ ((m◁u)◁v).
1x▷dy,m,u
55 (11)
AD-right module category can be defined more succinctly as aDrev-module category and a(C,D)-bimodule
category as aC⊠Drev-module category, where⊠ is the Deligne product. We expanded the definitions to set
up notation and introduce the relevant diagrams.
Remark 1.3. [EGNO, Prop. 7.1.3]
C-module category structures onM correspond bijectively to monoidal functorsF :C→ End(M). The
monoidal functor defined by aC-module structure assigns to an objectx inC the endofunctorx▷− :M→M
and to a morphismα :x→y inC the natural transformationα▷− :x▷−⇒ y▷−. The monoidal structure
of F is given by the natural isomorphismsγ :e▷−⇒ idM and cx,y,− : (x⊗y)▷−⇒ x▷ (y▷−).
Example 1.4. Every fusion categoryC is a (C,C)-bimodule category with▷ =◁ =⊗ :C×C→C and
coherence isomorphismscx,y,z =dx,y,z =bx,y,z =ax,y,z : (x⊗y)⊗z→x⊗ (y⊗z), γx =lx :e⊗x→x and
δx =rx :x⊗e→x.
Example 1.5. Any locally finiteC-linear abelian categoryM is a bimodule category over the fusion category
VectC of finite-dimensional complex vector spaces. ThisVectC-module category structure is unique up to
bimodule equivalence (cf. Definition 1.8).
Example 1.6. For any (C,D)-bimodule categoryM over pivotal fusion categoriesC,D the categoryMop is
a (D,C)-bimodule category with
◁op =▷(∗× idM)τ :M×C→M ▷op =◁(idM×∗ )τ :D×M→M , (12)
where∗ :C→C op,rev is the duality functor andτ the flip functor that exchanges the two factors in a cartesian
product. The coherence isomorphisms are given bycop
x,y,m =dm,y∗,x∗, dop
x,y,m =cy∗,x∗,m, bop
x,m,y =by∗,m,x∗.
We call it theopposite bimodule categoryM#.
Example 1.7. [EGNO, Ex. 7.4.10]
Indecomposable semisimple module categoriesM over the fusion categoryVecG := Vecω≡1
G , up to equivalence,
correspond to pairs(X,ψ ) of a finite transitiveG-set X∼=G/L and an elementψ∈H2(L, C×).
• The objects ofM areX-graded vector spaces.
• The simple objects ofM are of the formδx for x∈X .
• The action functor▷ : VecG×M→M is given byδg▷δx =δg▷x on the simple objects.
• The natural isomorphismc :▷(⊗× id)⇒▷(id×▷) is given byψ∈H2(L, C×).
Definition 1.8. LetC,D be multitensor categories.
1. AC-module functorF :M→N betweenC-module categoriesM,N is a C-linear right exact functor
F :M→N together with a natural isomorphisms :F▷⇒▷(idC×F ) that satisfies the pentagon and
the triangle axiom: for allx,y∈ ObC and m∈ ObM the following diagrams commute
F ((x⊗y)▷m)
F(cx,y,m)

sx⊗y,m// (x⊗y)▷F (m)
cx,y,F (m)
//x▷ (y▷F (m))
F (x▷ (y▷m))sx.y▷m
//x▷F (y▷m)
1x▷sy,m
66 (13)
F (e▷m)
F(γm) %%
se,m //e▷F (m)
γF(m)
yy
F (m).
(14)
2. AD-right module functorF :M→N betweenD-right module categoriesM,N is a C-linear right
exact functorF :M→N together with a natural isomorphismt :◁(F× idD)⇒F◁ that satisfies the
6
pentagon and the triangle axiom: for allx,y∈ ObD and m∈ ObM the following diagrams commute
(F (m)◁x)◁y
tm,x◁1y

dF(m),x,y
//F (m)◁ (x⊗y)
tm,x⊗y//F (m◁ (x⊗y))
F (m◁x)◁y tm◁x,y
//F ((m◁x)◁y)
F(dm,x,y)
66 (15)
F (m)◁e
δF(m) %%
tm,e //F (m◁e)
F(δm)yy
F (m).
(16)
3. A (C,D)-bimodule functorbetween (C,D)-bimodule categoriesM,N is a C-linear right exact functor
F :M→N with aC-module functor structures and aD-right module functor structuret that satisfy
the hexagon axiom: for allx∈ ObC, y∈ ObD and m∈ ObM the following diagram commutes
F (x▷m)◁y
sx,m◁1y

tx▷m,y//F ((x▷m)◁y)
F(bx,m,y)//F (x▷ (m◁y))
sx,m◁y

(x▷F (m))◁ybx,F(m),y
//x▷ (F (m)◁y)1x▷tm,y
//x▷F (m◁y).
(17)
An equivalence of (bi)module categoriesis a (bi)module functor that is an equivalence of categories.
Definition 1.9. LetC,D be multitensor categories.
1. AC-module natural transformationν : F ⇒ G forC-module functorsF,G :M→N is a natural
transformation such that the following diagram commutes for allx∈ ObC and m∈ ObM
F (x▷m)
sF
x,m

νx▷m //G(x▷m)
sG
x,m

x▷F (m) 1x▷νm
//x▷G(m).
(18)
2. AD-right module natural transformationν :F⇒G forD-right module functorsF,G :M→N is a
natural transformation such that the following diagram commutes for allx∈ ObD and m∈ ObM
F (m)◁x
tF
m,x

νm◁1x//G(m)◁x
tG
m,x

F (m◁x) νm◁x
//G(m◁x).
(19)
3. A (C,D)-bimodule natural transformationν :F→G between (C,D)-bimodule functorsF,G :M→N
is a natural transformationν :F⇒G that is aC-module and aD-right module natural transformation.
ForC-module categoriesM,N we denote byFunC(M,N ) the category ofC-module functorsF :M→N
andC-module natural transformations between them and writeEndC(M) = FunC(M,M). Analogously,
for (C,D)-bimodule categoriesM,N, we writeFun(C,D)(M,N ) for the category of(C,D)-bimodule functors
F :M→N and bimodule natural transformations between them andEnd(C,D)(M) = Fun(C,D)(M,M).
Composites of (bi)module functors inherit a (bi)module functor structure. IfG :M→N and F :N→P
are (C,D)-bimodule functors, then the(C,D)-bimodule functor structure forFG :M→P is given by
sFG =sF (idC×G)◦FsG :FG▷⇒▷(idC×FG ) (20)
tFG =FtG◦tF (G× idD) :◁(FG× idD)⇒FG◁.
7
For all bimodule functorsF,F′ :N→P , G,G′ :M→N and bimodule natural transformationsν :F⇒F′
and µ : G ⇒ G′ the natural transformations νG : FG ⇒ F′G and Fµ : FG ⇒ FG′ are bimodule
natural transformations with respect to this bimodule functor structure. As composites of bimodule natural
transformations are also bimodule natural transformations, it follows that(C,D)-bimodule categories, (C,D)-
bimodule functors and(C,D)-bimodule natural transformations form a 2-category.
The following examples show how the data of a (bi)module category can be recovered as coherence data of
(bi)module functors. They are the categorical counterparts of standard constructions for modules over rings.
Example 1.10.LetC,D be multitensor categories with (right) centresZ(C),Z(D) andM,N (C,D)-bimodule
categories.
1. For anyx∈ ObD the functorF =−◁x :M→M is aC-module functor with coherence isomorphisms
sc,m =bc,m,x : (c▷m)◁x→c▷ (m◁x). Any morphismα∈ HomD(x,y ) defines aC-module natural
transformationν =−◁α :−◁x⇒− ◁y. This defines a functorD→ EndC(M).
2. Ifx∈ ObZ(D) with half-braidingsσd,x :d⊗x→x⊗d, the functorF from 1. becomes a(C,D)-bimodule
functor withtm,d =d−1
m,d,x◦(1m◁σ−1
x,d)◦dm,x,d : (m◁x)◁d→ (m◁d)◁x. Forα∈ HomZ(D)(x,y ) the
morphismsνm = 1◁α :m◁x→m◁y define a(C,D)-bimodule natural transformationν :−◁x⇒−◁y.
This defines a functorZ(D)→ End(C,D)(M).
3. Analogously, forx∈ ObC F =x▷− :M→M with tm,d =bx,m,d : (x▷m)◁d→x▷ (m◁d) is a
D-right module functor. Any morphismα∈ HomC(x,y ) defines aD-right module natural transformation
ν =α▷− :x▷−⇒ y▷−. This defines a functorC→ EndDrev(M).
4. If x∈ ObZ(C) with half-braidings σc,x : c⊗x→ x⊗c, the functor F from 3. becomes a(C,D)-
bimodule functor withsc,m = cc,x,m◦ (σ−1
c,x▷ 1m)◦c−1
x,c,m : x▷ (c▷m)→ c▷ (x▷m). For any
morphism α∈ HomZ(C)(x,y ) the morphismsνm =α▷ 1m :x▷m→y▷m define aC-module natural
transformationν :x▷−⇒ y▷−. This defines a functorZ(C)→ End(C,D)(M).
5. For anyC-module categoryM and m∈ ObM, the functorF =−▷m :C→M is aC-module functor
with sx,y =cx,y,m : (x⊗y)▷m→x▷ (y▷m). Any morphismα∈ HomM(m,m′) defines aC-module
natural transformationν =−▷α :−▷m⇒− ▷m′.
IfM is a (C,D)-bimodule category, this defines a (C,D)-bimodule equivalenceM →FunC(C,M)
with respect to the(C,D)-bimodule structure on FunC(C,M) given by (c▷F )(x) = F (x⊗c) and
(F◁d)(x) =F (x)◁d for c,x∈ ObC, d∈ ObD.
6. For anyD-right module categoryM and m∈ ObM, the functorF =m◁− :D→M is aD-right
module functor withtx,y = dx,y,m : (m◁x)◁y→ m◁ (x⊗y). Any morphismα∈ HomM(m,m′)
defines aC-module natural transformationν =α◁− :m◁−⇒ m′◁−.
IfM is a (C,D)-bimodule category, this defines a(C,D)-bimodule equivalenceM→ FunDrev(D,M)
with respect to the(C,D)-bimodule structure onFunDrev(D,M) given by (c▷F )(x) = c▷F (x) and
(F◁d)(x) =F (d⊗x) for c∈ ObC, d,x∈ ObD.
7. IfC,D are pivotal fusion categories, any (C,D)-bimodule functor F : M → Ndefines a (D,C)-
bimodule functorF # :M#→N # with coherence isomorphismssF #
d,m =tF
m,d∗ and tF #
m,c =sF
c∗,m. Any
(C,D)-bimodule natural transformationν :F⇒G induces a (D,C)-bimodule natural transformation
ν# :G#⇒F # with ν#
m =νm.
8. For any (C,D)-bimodule functorF :M→N , the morphismssc,m : F (c▷m)→ c▷F (m) define
aD-right module natural isomorphismsc : F (c▷−) ⇒ c▷F (−). Analogously, the morphisms
tm,d :F (m)◁d→F (m◁d) define aC-module natural transformationtd :F (−)◁d⇒F (−◁d). This
follows from the hexagon identity(17) for a bimodule functor and the module functor structure(20) for
a composite functor.
IfC is a finite multitensor category as a bimodule category over itself, then all bimodule endofunctors ofC
are naturally isomorphic to functors of the formF =c⊗− :C→C with an objectc∈Z (C), as in Example
1.10, 4. and all bimodule natural transformations between them are of the formν =f⊗− :c⊗−⇒ c′⊗−
with a morphismf :c→c′ inZ(C). This identifiesEndC(C) with the centreZ(C).
Example 1.11. [EGNO, Prop. 7.13.8.] LetC be a finite multitensor category, viewed as a(C,C)-bimodule
category. Then the monoidal categoryEndC(C) is canonically monoidally isomorphic to the centreZ(C).
8
