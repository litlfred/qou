---
doc_id: arxiv-2607.10525v1
doc_title: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES"
section_id: sec-003-22-equivariant-tensor-categories-and-their-modul
section_title: "Equivariant tensor categories and their module categories"
section_number: 2.2
pages: 4-9
source_pdf: 2607.10525v1.pdf
source_sha256: b893cb4c87ea1d66
doc_brief: "FIBER FUNCTORS OF EQUIVARIANTIZATIONS OF FINITE TENSOR CATEGORIES — LetGbe a finite group acting on a finite tensor categoryC."
---
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 5
2.2.1.Group actions on tensor categories.LetG be the strict monoidal category
associated with a groupG. An action ofGon a tensor categoryCis a monoidal
functor
G−→Aut⊗(C).
By the coherence theorem for tensor categories withG-action [Gal17, Theorem 2.4],
we may and do assume that theG-action is strict. We writeg∗ for the tensor au-
toequivalence attached tog, so thatg∗h∗ = (gh)∗ ande∗ = idC. Equivariant module
categories will not be strictified; their coherence maps are retained below.
2.2.2.The semidirect product.For a tensor categoryCwith a strictG-action, the
semidirect productC⋊Gis the monoidal category
C⋊G=
M
g∈G
Cg,
where each homogeneous componentC g is a copy ofC[Tam01, Nik08]. We write
[X,g]for the objectX∈Cplaced in degreeg. The tensor product and unit are
(1)[X,g]⊗[Y,h] = [X⊗g ∗(Y),gh],1 C⋊G = [1,e],
with associativity and unit constraints induced from those ofC. WhenGis finite,
C⋊Gis a finite tensor category. For an arbitrary subsetS⊆G, we use the notation
(C⋊G) S :=
M
s∈S
Cs.
IfSis a subgroup, this is the tensor subcategoryC⋊S. IfS=gKis a left coset, then
(C⋊G)gK isnaturallya((C⋊G) gKg−1,C⋊K)-bimodulecategoryundertensorproduct.
This notation will also be used for arbitrary faithfully graded tensor categories.
2.2.3.H-equivariant module categories.We follow [Gal11, ENO11] for equivariant
module categories and their use in constructing module categories over equivarianti-
zations.
LetH⊆Gbe a subgroup acting on a finite tensor categoryC. Given aC-module
categoryM, wetwistthe module structure by any elementg∈H.
For eachg∈H, letM g be the category with the same underlying abelian category
asMand withC-action
X⊗gM:=g ∗(X)⊗M.
The associativity and unit constraints are those induced from the module structure
ofMand the tensor structure ofg ∗. Since the action onCis strict,(M g)h =M gh
asC-module categories.
We now make explicit the monoidal category that records twisted module autoe-
quivalences. LetAut H
C (M)be the groupoid whose objects are pairs(g,F), where
g∈Hand
(F,cF ) :M−→M g
6 C. GALINDO, C. GALLEGO, AND Y. MORALES
is aC-module equivalence. There are no morphisms between objects of different
degrees, and morphisms in degreegareC-module natural isomorphisms. If(g,F)
and(h,E)are objects, define
(g,F)⊗(h,E) := (gh,F◦E),
where theC-module constraint on the composite is
(2)
cF◦E
X,M :F(E(X ⊗M))
F(c E
X,M )
−−−−−−→F(h∗(X)⊗E(M))
cF
h∗(X),E(M)
−−−−−−−−→(gh)∗(X)⊗F(E(M)).
With the usual horizontal product of module natural isomorphisms, composition
makes this a strict monoidal groupoid with unit(e,idM). The degree map
π1 : AutH
C (M)−→H ,(g,F)7−→g,
is a strict monoidal functor.
AnH-equivariantC-module categoryis aC-module categoryMtogether with a
strong monoidal section
ρ:H −→AutH
C (M), π 1◦ρ= id H.
We work with normalized sections. Explicitly, the data consist ofC-module equiva-
lences
(Uh,ch) :M−→M h, h∈H,
and module natural isomorphisms
µg,h :U gUh
∼
− →Ugh
such that
(3)(µ gh,k)M◦(µg,h)Uk(M) = (µg,hk)M◦Ug((µh,k)M)
for allg,h,k∈HandM∈M, and such that eachµ g,h is a module natural transfor-
mation, equivalently
(4)
(id(gh)∗(X)⊗(µg,h)M)◦c g
h∗(X),U h(M)◦Ug(ch
X,M)
=c gh
X,M◦(µg,h)X⊗M
for allX∈CandM∈M. Normalization means
(5)U e = idM, c e = id, µ e,h =µ h,e = idUh.
Every strong monoidal section is monoidally isomorphic to a normalized one, so this
convention does not change the equivalence classes under consideration.
Under these conventions, normalizedH-equivariantC-module structures onM
are equivalent to(C⋊H)-module structures extending the originalC-action. The
correspondence is given explicitly by
(6)[X,h] ⊗M:=X ⊗Uh(M).
The associativity constraint for this action is built fromch andµ g,h; conversely, the
action of[1,h]recoversU h, and the module associativity recoversch andµ g,h.
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 7
AnH-equivariantC-module category will be called indecomposable when its un-
derlyingC-module category is indecomposable.
2.3.The equivariant categoryCG and its module categories.Given aG-action
on a tensor categoryC, one forms theequivariant categoryCG.
Its objects are pairs(X,u)whereX∈ Candu={u g :g ∗(X)→X} g∈G is a
collection of isomorphisms satisfyingugh =u g◦g∗(uh)for allg,h∈Gandu e = idX.
The tensor product is(X,u)⊗(Y,v) = (X⊗Y,w), wherew g =u g⊗vg, and the unit
object is(1,id 1).
By [EGNO15, Section 4.15 and Example 7.12.25], ifCis a finite tensor category
with aG-action, thenC G is also a finite tensor category.
LetH⊆Gbe a subgroup, and letMbe anH-equivariantC-module category with
structureρ:H →Aut H
C (M). Forgetting the module functor structures, the functors
Uh define an action ofHon the underlying abelian categoryM. One can therefore
form the equivariant categoryMH, and the tensor categoryCG acts on it.
The categoryM H is defined analogously toC G: objects are pairs(M,v)where
M∈Mandv={v h :U h(M)→M} h∈H satisfyv e = idM and the equivariance
conditionv h1h2◦(µh1,h2)M =v h1◦Uh1(vh2)for allh 1,h 2∈H. Morphisms are defined
similarly to preserve the equivariant structure.
It follows from [GM12, Lemma 3.3] thatMH is a leftC G-module category. The
action of(X,u)∈C G on(M,v)∈M H is given by(X,u)⊗(M,v) = (X⊗M,ev), where
evh = (uh⊗vh)◦c h
X,M forh∈H.
We use the following description of exact module categories over equivariantiza-
tions, due to Galindo–Mombelli [GM12, Proposition 3.4].
Proposition 2.2.LetGbe a finite group acting on a finite tensor categoryC. Then
the following hold.
(1)IfMis anH-equivariantC-module category, thenM H is an exactCG-module
category if and only ifMis an exactC-module category.
(2)IfNis an indecomposable exact module category overC G, then there exists a
subgroupH⊆Gand anH-equivariantC-module categoryM, whose under-
lyingC-module category is indecomposable and exact, such thatN≃MH.
2.3.1.Equivalence classes of equivariant module categories.Werecordwhentwoequi-
variantC-module categories produce equivalentCG-module categories.
LetL⊆G, and letMandNbe twoL-equivariantC-module categories, with
structure functorsUℓ andU ′
ℓ, respectively. Recall that anL-equivariant equivalence
is aC-module functorF:M → Ntogether with module natural isomorphisms
wℓ :U ′
ℓ◦F→F◦U ℓ satisfying the coherence condition
wℓm
M ◦(µ′
ℓ,m)F(M) =F((µ ℓ,m)M)◦w ℓ
Um(M)◦U′
ℓ(wm
M)
for allℓ,m∈LandM∈M. In the strict case this reduces to the usual formula
wℓm
M =w ℓ
Um(M)◦U ′
ℓ(wm
M). This convention is compatible with the correspondence
betweenL-equivariantC-module categories and(C⋊L)-module categories.
8 C. GALINDO, C. GALLEGO, AND Y. MORALES
Forg∈G, the rule
Adg([V,h]) = [g∗(V),ghg −1]
defines a tensor autoequivalence ofC⋊Gand restricts toC⋊K≃C⋊gKg −1. IfN
is aK-equivariantC-module category andH=gKg −1, letgNbe theH-equivariant
module category obtained by pulling the corresponding(C⋊K)-module structure
back alongAdg−1. On the underlying category,
V• gN= (g −1)∗(V)▷N, U ′
h =U g−1hg,
with module constraints and coherence maps transported from those ofN.
Definition 2.3.Two pairs(H,M)and(K,N), whereMis anH-equivariantC-
module category andNis aK-equivariantC-module category, are calledconjugate
if there existsg∈Gsuch that
(1)H=gKg −1, and
(2)Mis equivalent to gNasH-equivariantC-module categories.
The equivalence relation among these equivariantized module categories is the fol-
lowing.
Theorem 2.4.LetGbe a finite group acting on a finite tensor categoryC. Let
H,K⊆Gbe subgroups. LetMbe anH-equivariantC-module category and letNbe
aK-equivariantC-module category. Assume that the underlyingC-module categories
ofMandNare indecomposable and exact. Then the equivariantizationsM H and
NK are equivalent asC G-module categories if and only if(H,M)and(K,N)are
conjugate.
Proof.LetD=C⋊G, with its canonical faithfulG-grading, and useD S for the sum of
the homogeneous components indexed by a subsetS⊆G. TheH- andK-equivariant
structures makeMandNintoD H- andDK-module categories. By [GM12, Propo-
sition 3.4(1)], they are indecomposable exact asDH- andDK-module categories, re-
spectively. Their restrictions to the neutral componentD e =Care the original
indecomposableC-module categories. Hence(H,M)and(K,N)are type-1 pairs in
the terminology of [MCnM20, Subsection 5.1].
By [GM12, Proposition 3.4(3)] and the argument proving [GM12, Proposition
3.4(5)] via Tambara’s correspondence [Tam01, Theorem 4.1], the categoriesMH and
NK are equivalent asC G-module categories if and only if the inducedD-module
categories
IndD
DH(M) :=D⊠ DHM,
IndD
DK(N) :=D⊠ DKN
are equivalent.
By [MCnM20, Definition 5.10 and Proposition 5.12], applied to theG-graded tensor
categoryD, these induced module categories are equivalent if and only if there exists
g∈Gsuch that:
(1)H=gKg −1, and
FIBER FUNCTORS OF EQUIV ARIANTIZATIONS 9
(2)D gK ⊠DKN≃MasD H-module categories.
The functor
Φg :D gK−→DK,[V,gk]7−→[(g −1)∗(V),k],
induced by left tensoring with[1,g−1], is an equivalence of(DH,DK)-bimodule cat-
egories, where the leftD H-action onD K is transported alongAd g−1 :D H →D K.
Consequently, the relative tensor product isNwith itsDH-action pulled back along
Adg−1, and hence
DgK ⊠DKN≃ gN
asD H-module categories. By construction, the right-hand side is precisely theH-
equivariantC-module category introduced above. Thus, by [MCnM20, Def. 5.10,
Prop. 5.12], this equivalence relation is precisely the conjugacy condition above.□
3.Fiber functors forC G
