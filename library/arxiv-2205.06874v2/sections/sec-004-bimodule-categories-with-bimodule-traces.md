---
doc_id: arxiv-2205.06874v2
doc_title: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg"
section_id: sec-004-bimodule-categories-with-bimodule-traces
section_title: "Bimodule categories with bimodule traces"
section_number: null
pages: 9-11
source_pdf: 2205.06874v2.pdf
source_sha256: 9b41365160c17ab4
doc_brief: "State sum models with defectsbased on spherical fusion categories Catherine Meusburger Department Mathematik Friedrich-Alexander-Universität Erlangen-Nürnberg — We define a"
---
(Bi)module traces on (bi)module categories over fusion categories were first introduced by Schaumann in
[S13] and investigated further in [S15]. We summarise (bi)module traces for finite semisimple (bi)module
categories over pivotal fusion categories from [S13, S15]. To keep notation simple, we focus on left module
categories and identify(C,D)-bimodule categories withC⊠Drev-left module categories.
Definition 1.13. [S13, Def. 3.7]
LetC be a pivotal multifusion category andM a finite semisimpleC-module category.
A trace onM is a collection of morphismsθm : EndM(m)→ C indexed by objectsm∈ ObM that satisfy
9
1. cyclicity: θm(β◦α) =θm′(α◦β) for allα∈ HomM(m,m′) and β∈ HomM(m′,m ).
2. non-degeneracy: for allm,m′∈ ObM the following bilinear maps are non-degenerate.
HomM(m′,m )× HomM(m,m′)→ C, (β,α )↦→θm(β◦α)
A trace onM is called aC-module traceif θc▷m(α) =θm(trC(α)) for allα∈ EndM(c▷m), where trC(α)
is the partial trace ofα with respect toC
trC(α) = (evL
c▷ 1m)◦c−1
c∗,c,m◦ (1c∗▷α)◦cc∗,c,m◦ (coevR
c ▷ 1m) :m→m.
Analogously, aD-right module trace on aD-right module categoryM is defined as aDrev-module trace and
a (C,D)-bimodule trace on a(C,D)-bimodule categoryM as aC⊠Drev-module trace.
As for spherical categories, thedimension of an objectm in a (bi)module categoryM with a (bi)module
trace is dim(m) =θm(1m) and for any setI of representatives of the isomorphism classes of simple objects
dim(M) =
∑
m∈I
dim(m)2. (21)
IfC is spherical, the condition thatθ is aC-module trace implies for allc∈ ObC and m∈ ObM
dim(c▷m) = dim(c) dim(m). (22)
It is shown in [S13, Prop. 4.4] that aC-module trace on anindecomposablefinite semisimple module category
M is unique up to rescalingθm→ zθm with z∈ C×. The existence of aC-module trace on aC-module
categoryM is a condition on the dimensions of simple objects ofC andM, see [S13, Sec. 5].
Example 1.14. A pivotal fusion categoryC as a (C,C)-bimodule category over itself has a bimodule trace if
and only ifC is spherical.
Example 1.15. Each (C,D)-bimodule trace on a finite semisimple(C,D)-bimodule categoryM defines a
(D,C)-bimodule trace on the opposite bimodule categoryM# from Example 1.6.
Example 1.16.[S13, Ex. 3.13] An indecomposable module category over the pivotal fusion category(VecG,κ ),
given by a pair(G/L,ψ ) as in Example 1.7, admits a module trace iffκ|L≡ 1. Any indecomposable semisimple
module category overVecG with the standard spherical structure admits a module trace.
(Bi)module traces on (bi)module categories equip (bi)module functors between them with additional structure.
It is shown in [S13, Th. 4.5] that for module categoriesM andN over a pivotal fusion categoryC with module
traces, any module functorF :M→N is naturally isomorphic to its double left adjointFll :M→N . This
defines a pivotal structure in the sense of [S15, Def. A.12], namely a natural 2-isomorphismω : id⇒∗∗ ,
where∗ is the contravariant 2-functor that assigns each module category to itself, each functor to its left dual
and each module natural transformationν :F⇒G to the induced natural transformationν∗ :Gl⇒Fl.
Theorem 1.17. [S13, Th. 4.5], [S15, Th. 5.8]
1. For all pivotal fusion categoriesC the 2-categoryModθ(C) ofC-module categories withC-module traces,
C-module functors between them andC-module natural transformations is pivotal.
2. For all pivotal fusion categoriesC,D the 2-categoryBimodθ(C,D) of (C,D)-bimodule categories with
bimodule traces,(C,D)-bimodule functors between them and(C,D)-bimodule transformations is pivotal.
In particular, this yields pivotal structures on the finite multifusion categoriesEndC(M). If the underlying
fusion categoryC is spherical, these pivotal structures become spherical. IfM is also indecomposable, then
EndC(M) is a spherical fusion category. An earlier proof of this was given by Mueger in [Mu03, Th. 5.16].
Corollary 1.18. [S13, Prop. 5.10] For any spherical fusion categoryC and anyC-module categoryM with a
C-module trace,EndC(M) is spherical. IfM is indecomposable,EndC(M) is a spherical fusion category.
For any module categoryM over a fusion categoryC with aC-module trace, the multifusion categoryEndC(M)
acts onM. This action functor is given by the evaluation of endofunctors and natural transformations
between them on objects and morphisms ofM. IfC is pivotal, thenEndC(M) is pivotal and the module
trace ofM also satisfies the module trace condition for theEndC(M)-module category structure.
10
Corollary 1.19. [S13, Cor. 4.6] LetC be a pivotal fusion category andM be aC-module category with a
C-module traceθ. Thenθ is also anEndC(M)-module trace.
More explicitly, the pivotal structure from Theorem 1.17 and Corollaries 1.18 and 1.19 is given as follows. If
we denote byFl :M→M the left adjoint of aC-module functorF :M→M , byηF : idN⇒FF l the unit
and byϵF :FlF⇒ idM the counit of this adjunction, then the component morphismsωF :Fll⇒F of the
pivotal structure are characterised by the condition
θM
Fl(n)(β◦ϵF
m◦Fl(α)) =θN
n (ϵFl
n ◦Fll(β)◦ωF−1
m ◦α) (23)
for all α ∈ HomN (n,F (m)) and β ∈ HomM(m,F l(n)). This condition encodes the chain of natural
isomorphisms that definesωF in equation (4.14) in [S13].
Condition (23) implies an identity that generalises Corollary 1.19 toC-module functors that are not endo-
functors. It is obtained from the (co)evaluations for the right duals induced byωF :Fll⇒F
η′F =FlωF◦ηFl
: idM⇒FlF ϵ ′F =ϵFl
◦ωF−1Fl :FF l⇒ idN. (24)
Corollary 1.20. LetC be a pivotal fusion category andM,N C-module categories withC-module traces.
Then anyC-module functorF :M→N satisfies
θM
m (ϵF
m◦Fl(α)◦η′F
m ) =θN
F(m)(α) (25)
for allm∈ ObM, n∈ ObN and morphismsα :F (m)→F (m).
Proof. This follows by settingn =F (m) and β =η′F
m =Fl(ωF
m)◦ηFl
m :m→FlF (m) in (23). By cyclicity
of θM, the left-hand side of(23) is equal to the left-hand side of(25). The right-hand side of(23) can
be simplified using the naturality ofωF and the for the defining identities for the unit and counit of an
adjunction and yields the right-hand side of (25).
Note that for an endofunctorF :M→M , condition(25) is just the partial trace condition from Definition
1.13 for theEndC(M)-module structure onM and Corollary 1.20 reduces to Corollary 1.19.
